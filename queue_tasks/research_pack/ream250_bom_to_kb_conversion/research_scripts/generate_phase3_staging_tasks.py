#!/usr/bin/env python3
"""Generate reAM250 Phase 3 KB staging tasks from merge review files."""
from __future__ import annotations

import argparse
import fcntl
import json
import re
import time
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]
TASK_DIR = Path("queue_tasks/research_pack/ream250_bom_to_kb_conversion")
VALIDATOR = TASK_DIR / "research_scripts/schema_validate_row_conversions.py"
ROW_DIR = Path("research/ream250_bom")
MERGE_REVIEW_DIR = ROW_DIR / "kb_conversion/merge_reviews"
PHASE3_OUTPUT_DIR = ROW_DIR / "kb_conversion/phase3_staging"
DEFAULT_OUTPUT = Path("out/ream250_kb_phase3_staging_tasks.jsonl")
DEFAULT_QUEUE = Path("out/work_queue.jsonl")
DEFAULT_LOCK = Path("out/work_queue.lock")
DEFAULT_REGISTRY = Path("queue/gap_type_registry.json")
TASK_PREFIX = "research_task:ream250_kb_stage_"
ITEM_PREFIX = "ream250_kb_stage_"
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MERGE_ID_RE = re.compile(r"^ream250_kb_merge_(.+)$")


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def safe_token(value: str) -> str:
    token = re.sub(r"[^A-Za-z0-9]+", "_", value.strip()).strip("_").lower()
    return token or "unknown"


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.search(text)
    if not match:
        return None
    data = yaml.safe_load(match.group(1)) or {}
    return data if isinstance(data, dict) else None


def stage_id_from_group(group_id: str) -> str:
    match = MERGE_ID_RE.match(group_id)
    if match:
        return f"{ITEM_PREFIX}{safe_token(match.group(1))}"
    return f"{ITEM_PREFIX}{safe_token(group_id)}"


def completed_merge_reviews(merge_review_dir: Path) -> list[dict[str, Any]]:
    reviews: list[dict[str, Any]] = []
    for path in sorted(merge_review_dir.glob("ream250_kb_merge_*.md")):
        data = parse_frontmatter(path)
        if not data:
            continue
        group_id = data.get("group_id")
        merge_decision = data.get("merge_decision") or {}
        decision = merge_decision.get("decision")
        candidate_rows = data.get("candidate_rows") or []
        if not group_id or not decision or not isinstance(candidate_rows, list):
            continue
        reviews.append(
            {
                "path": repo_relative(path),
                "group_id": str(group_id),
                "phase2_decision": str(decision),
                "candidate_rows": candidate_rows,
                "proposed_closure_items": merge_decision.get("proposed_closure_items") or [],
            }
        )
    return reviews


def build_tasks(reviews: list[dict[str, Any]], output_dir: Path) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    for review in reviews:
        stage_id = stage_id_from_group(review["group_id"])
        output_path = output_dir / f"{stage_id}.stage.yaml"
        context = {
            "task_type": "phase3_staging",
            "stage_id": stage_id,
            "source_merge_review": review["path"],
            "source_phase2_decision": review["phase2_decision"],
            "candidate_rows": review["candidate_rows"],
            "phase2_proposed_closure_items": review["proposed_closure_items"],
            "schema": str(TASK_DIR / "phase3_staging.schema.yaml"),
            "acceptance_criteria": str(TASK_DIR / "acceptance_criteria.md"),
            "output_path": repo_relative(output_path),
            "output_validator": str(VALIDATOR),
            "done_criteria": (
                "Read the merge review, every candidate row source file, and existing KB "
                "candidates. Write one Phase 3 staging YAML file. Do not write kb/. "
                "Validate with --kind phase3_stage and complete with --require-output "
                "--validate-output."
            ),
        }
        tasks.append(
            {
                "kind": "research",
                "gap_type": "research_task",
                "item_id": stage_id,
                "source": "manual",
                "description": (
                    f"Create Phase 3 KB staging package {stage_id} from merge review "
                    f"{review['group_id']}."
                ),
                "context": context,
            }
        )
    return tasks


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def queue_entry_for_task(task: dict[str, Any]) -> dict[str, Any]:
    context = dict(task.get("context") or {})
    context["added_at"] = time.time()
    if task.get("description") and "description" not in context:
        context["description"] = task["description"]
    return {
        "id": f"{task['gap_type']}:{task['item_id']}",
        "kind": task.get("kind", "gap"),
        "reason": task["gap_type"],
        "gap_type": task["gap_type"],
        "item_id": task["item_id"],
        "source": task.get("source", "manual"),
        "context": context,
        "status": "pending",
    }


def replace_queue_prefix(queue_path: Path, lock_path: Path, tasks: list[dict[str, Any]]) -> int:
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w") as lockf:
        fcntl.flock(lockf, fcntl.LOCK_EX)
        try:
            existing: list[dict[str, Any]] = []
            if queue_path.exists():
                for line in queue_path.read_text(encoding="utf-8").splitlines():
                    if not line.strip():
                        continue
                    try:
                        obj = json.loads(line)
                    except Exception:
                        continue
                    if not str(obj.get("id", "")).startswith(TASK_PREFIX):
                        existing.append(obj)
            new_entries = [queue_entry_for_task(task) for task in tasks]
            with queue_path.open("w", encoding="utf-8") as f:
                for obj in existing + new_entries:
                    f.write(json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n")
            return len(new_entries)
        finally:
            fcntl.flock(lockf, fcntl.LOCK_UN)


def ensure_registry(registry_path: Path, usage_count: int) -> None:
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    if registry_path.exists():
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception:
            registry = {}
    else:
        registry = {}
    entry = registry.setdefault(
        "research_task",
        {
            "description": "Manual research task completed by writing task-specific artifacts.",
            "created_by": "ream250_bom_to_kb_conversion_task_pack",
            "created_at": time.time(),
            "usage_count": 0,
            "source": "manual",
        },
    )
    entry["usage_count"] = usage_count
    entry["source"] = entry.get("source") or "manual"
    registry_path.write_text(json.dumps(registry, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--merge-review-dir", type=Path, default=MERGE_REVIEW_DIR)
    parser.add_argument("--phase3-output-dir", type=Path, default=PHASE3_OUTPUT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--replace-queue-prefix", action="store_true")
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()

    merge_review_dir = args.merge_review_dir if args.merge_review_dir.is_absolute() else REPO_ROOT / args.merge_review_dir
    phase3_output_dir = args.phase3_output_dir if args.phase3_output_dir.is_absolute() else REPO_ROOT / args.phase3_output_dir
    output = args.output if args.output.is_absolute() else REPO_ROOT / args.output
    queue = args.queue if args.queue.is_absolute() else REPO_ROOT / args.queue
    lock = args.lock if args.lock.is_absolute() else REPO_ROOT / args.lock
    registry = args.registry if args.registry.is_absolute() else REPO_ROOT / args.registry

    reviews = completed_merge_reviews(merge_review_dir)
    tasks = build_tasks(reviews, phase3_output_dir)
    write_jsonl(output, tasks)
    print(f"Read {len(reviews)} completed merge reviews")
    print(f"Wrote {len(tasks)} Phase 3 staging tasks to {repo_relative(output)}")
    if args.replace_queue_prefix:
        added = replace_queue_prefix(queue, lock, tasks)
        ensure_registry(registry, added)
        print(f"Replaced {TASK_PREFIX} entries in {repo_relative(queue)} with {added} pending tasks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
