#!/usr/bin/env python3
"""Generate reAM250 BOM-to-KB row conversion queue tasks."""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import re
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
TASK_DIR = Path("queue_tasks/research_pack/ream250_bom_to_kb_conversion")
VALIDATOR = TASK_DIR / "research_scripts/schema_validate_row_conversions.py"
ROW_DIR = Path("research/ream250_bom")
BASELINE_HASHES = ROW_DIR / "kb_conversion/baseline_hashes.json"
DEFAULT_OUTPUT = Path("out/ream250_kb_row_conversion_tasks.jsonl")
DEFAULT_QUEUE = Path("out/work_queue.jsonl")
DEFAULT_LOCK = Path("out/work_queue.lock")
DEFAULT_REGISTRY = Path("queue/gap_type_registry.json")
TASK_PREFIX = "research_task:ream250_kb_row_"
ITEM_PREFIX = "ream250_kb_row_"
ROW_FILE_RE = re.compile(r"ream250_bom_row_(\d{4})_(.+)\.md$")
SECTION_HEADING = "## KB Conversion"


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def safe_token(value: str) -> str:
    token = re.sub(r"[^A-Za-z0-9]+", "_", value.strip()).strip("_")
    return token or "unknown"


def normalize_pre_section(text: str) -> str:
    return text.rstrip() + "\n"


def pre_conversion_text(text: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(SECTION_HEADING)}\s*$")
    match = pattern.search(text)
    if not match:
        return normalize_pre_section(text)
    return normalize_pre_section(text[: match.start()])


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_row_identity(path: Path) -> tuple[str, str]:
    match = ROW_FILE_RE.match(path.name)
    if not match:
        raise ValueError(f"unexpected row filename: {path}")
    return match.group(1), match.group(2)


def build_tasks(row_dir: Path) -> tuple[list[dict[str, Any]], dict[str, str]]:
    tasks: list[dict[str, Any]] = []
    hashes: dict[str, str] = {}
    for path in sorted(row_dir.glob("ream250_bom_row_*.md")):
        row_number, item_token = parse_row_identity(path)
        rel = repo_relative(path)
        baseline_hash = sha256_text(pre_conversion_text(path.read_text(encoding="utf-8")))
        hashes[rel] = baseline_hash
        item_id = f"{ITEM_PREFIX}{row_number}_{safe_token(item_token)}"
        context = {
            "task_type": "row_conversion",
            "source_research_file": rel,
            "source_research_sha256": baseline_hash,
            "baseline_hashes_path": repo_relative(REPO_ROOT / BASELINE_HASHES),
            "conversion_heading": SECTION_HEADING,
            "source_guide": "research/ream250_bom/bom_to_kb_lunarized_closure_abstraction_en.md",
            "schema": str(TASK_DIR / "conversion_section.schema.yaml"),
            "acceptance_criteria": str(TASK_DIR / "acceptance_criteria.md"),
            "output_path": rel,
            "output_validator": str(VALIDATOR),
            "done_criteria": (
                "Append or replace only the bottom ## KB Conversion section. "
                "Do not edit any content before that section. Validate and complete "
                "with --require-output --validate-output."
            ),
        }
        tasks.append(
            {
                "kind": "research",
                "gap_type": "research_task",
                "item_id": item_id,
                "source": "manual",
                "description": f"Convert reAM250 BOM research row {row_number} into a KB Conversion section.",
                "context": context,
            }
        )
    return tasks, hashes


def write_jsonl(path: Path, tasks: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False, sort_keys=True) + "\n")


def write_baseline_hashes(path: Path, hashes: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    parser.add_argument("--row-dir", type=Path, default=ROW_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--baseline-hashes", type=Path, default=BASELINE_HASHES)
    parser.add_argument("--replace-queue-prefix", action="store_true")
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()

    row_dir = args.row_dir if args.row_dir.is_absolute() else REPO_ROOT / args.row_dir
    output = args.output if args.output.is_absolute() else REPO_ROOT / args.output
    baseline_hashes = args.baseline_hashes if args.baseline_hashes.is_absolute() else REPO_ROOT / args.baseline_hashes
    queue = args.queue if args.queue.is_absolute() else REPO_ROOT / args.queue
    lock = args.lock if args.lock.is_absolute() else REPO_ROOT / args.lock
    registry = args.registry if args.registry.is_absolute() else REPO_ROOT / args.registry

    tasks, hashes = build_tasks(row_dir)
    write_jsonl(output, tasks)
    write_baseline_hashes(baseline_hashes, hashes)
    print(f"Wrote {len(tasks)} row conversion tasks to {repo_relative(output)}")
    print(f"Wrote baseline hashes to {repo_relative(baseline_hashes)}")
    if args.replace_queue_prefix:
        added = replace_queue_prefix(queue, lock, tasks)
        ensure_registry(registry, added)
        print(f"Replaced {TASK_PREFIX} entries in {repo_relative(queue)} with {added} pending tasks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
