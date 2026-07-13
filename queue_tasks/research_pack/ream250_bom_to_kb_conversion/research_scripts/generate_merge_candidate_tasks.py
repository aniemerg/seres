#!/usr/bin/env python3
"""Generate reAM250 KB merge review tasks from row conversion sections."""
from __future__ import annotations

import argparse
import fcntl
import json
import re
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]
TASK_DIR = Path("queue_tasks/research_pack/ream250_bom_to_kb_conversion")
VALIDATOR = TASK_DIR / "research_scripts/schema_validate_row_conversions.py"
ROW_DIR = Path("research/ream250_bom")
MERGE_REVIEW_DIR = ROW_DIR / "kb_conversion/merge_reviews"
DEFAULT_OUTPUT = Path("out/ream250_kb_merge_review_tasks.jsonl")
DEFAULT_CANDIDATES = ROW_DIR / "kb_conversion/merge_candidates.jsonl"
DEFAULT_QUEUE = Path("out/work_queue.jsonl")
DEFAULT_LOCK = Path("out/work_queue.lock")
DEFAULT_REGISTRY = Path("queue/gap_type_registry.json")
TASK_PREFIX = "research_task:ream250_kb_merge_"
ITEM_PREFIX = "ream250_kb_merge_"
ROW_HEADING = "## KB Conversion"
ROW_FILE_RE = re.compile(r"ream250_bom_row_(\d{4})_(.+)\.md$")


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def safe_token(value: str) -> str:
    token = re.sub(r"[^A-Za-z0-9]+", "_", value.strip()).strip("_").lower()
    return token or "unknown"


def split_kb_conversion(text: str) -> str | None:
    pattern = re.compile(rf"(?m)^{re.escape(ROW_HEADING)}\s*$")
    match = pattern.search(text)
    if not match:
        return None
    return text[match.start() :]


def parse_conversion(path: Path) -> dict[str, Any] | None:
    section = split_kb_conversion(path.read_text(encoding="utf-8"))
    if not section:
        return None
    match = re.search(r"```yaml\s*\n(.*?)\n```", section, flags=re.DOTALL)
    if not match:
        return None
    data = yaml.safe_load(match.group(1)) or {}
    return data if isinstance(data, dict) else None


def row_identity(path: Path) -> tuple[int, str]:
    match = ROW_FILE_RE.match(path.name)
    if not match:
        raise ValueError(f"unexpected row filename: {path}")
    return int(match.group(1)), match.group(2)


def mass_value(data: dict[str, Any]) -> float | None:
    scale = ((data.get("identity_for_merge") or {}).get("scale_or_capacity") or {})
    mass = scale.get("mass_kg")
    if isinstance(mass, (int, float)) and mass > 0:
        return float(mass)
    return None


def eligible_rows(row_dir: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(row_dir.glob("ream250_bom_row_*.md")):
        data = parse_conversion(path)
        if not data:
            continue
        merge_pool = data.get("merge_pool") or {}
        if merge_pool.get("eligible") is not True:
            continue
        key = merge_pool.get("functional_purpose_key")
        mass = mass_value(data)
        if not key or mass is None:
            continue
        source_row_number, item = row_identity(path)
        identity = data.get("identity_for_merge") or {}
        rows.append(
            {
                "path": repo_relative(path),
                "source_row_number": source_row_number,
                "item": item,
                "functional_purpose_key": str(key),
                "mass_kg": mass,
                "material": identity.get("material"),
                "geometry_form": identity.get("geometry_form"),
                "precision_guardrails": list(merge_pool.get("precision_guardrails") or []),
            }
        )
    return rows


def build_groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[row["functional_purpose_key"]].append(row)

    groups: list[dict[str, Any]] = []
    ordinal = 1
    for key in sorted(buckets):
        bucket = sorted(buckets[key], key=lambda row: row["mass_kg"])
        current: list[dict[str, Any]] = []
        low = None
        for row in bucket:
            mass = row["mass_kg"]
            if not current:
                current = [row]
                low = mass
            elif low and mass / low <= 2.0:
                current.append(row)
            else:
                if len(current) >= 2:
                    groups.append(make_group(ordinal, key, current))
                    ordinal += 1
                current = [row]
                low = mass
        if len(current) >= 2:
            groups.append(make_group(ordinal, key, current))
            ordinal += 1
    return groups


def make_group(ordinal: int, key: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    masses = [row["mass_kg"] for row in rows]
    group_id = f"ream250_kb_merge_{ordinal:04d}_{safe_token(key)}"
    return {
        "group_id": group_id,
        "functional_purpose_key": key,
        "mass_window_kg": [min(masses), max(masses)],
        "candidate_rows": rows,
    }


def build_tasks(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    for group in groups:
        group_id = group["group_id"]
        output_path = MERGE_REVIEW_DIR / f"{group_id}.md"
        context = {
            "task_type": "merge_review",
            "group_id": group_id,
            "candidate_rows": group["candidate_rows"],
            "rough_match_basis": {
                "functional_purpose_key": group["functional_purpose_key"],
                "mass_window_kg": group["mass_window_kg"],
            },
            "schema": str(TASK_DIR / "merge_review.schema.yaml"),
            "acceptance_criteria": str(TASK_DIR / "acceptance_criteria.md"),
            "output_path": str(output_path),
            "output_validator": str(VALIDATOR),
            "done_criteria": (
                "Read every candidate row file and write one merge review Markdown file "
                "with YAML frontmatter. Validate and complete with --require-output "
                "--validate-output."
            ),
        }
        tasks.append(
            {
                "kind": "research",
                "gap_type": "research_task",
                "item_id": group_id,
                "source": "manual",
                "description": (
                    f"Review reAM250 KB merge candidate {group_id} "
                    f"({len(group['candidate_rows'])} rows)."
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
    parser.add_argument("--row-dir", type=Path, default=ROW_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--candidates-output", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--replace-queue-prefix", action="store_true")
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()

    row_dir = args.row_dir if args.row_dir.is_absolute() else REPO_ROOT / args.row_dir
    output = args.output if args.output.is_absolute() else REPO_ROOT / args.output
    candidates_output = args.candidates_output if args.candidates_output.is_absolute() else REPO_ROOT / args.candidates_output
    queue = args.queue if args.queue.is_absolute() else REPO_ROOT / args.queue
    lock = args.lock if args.lock.is_absolute() else REPO_ROOT / args.lock
    registry = args.registry if args.registry.is_absolute() else REPO_ROOT / args.registry

    rows = eligible_rows(row_dir)
    groups = build_groups(rows)
    tasks = build_tasks(groups)
    write_jsonl(candidates_output, groups)
    write_jsonl(output, tasks)
    print(f"Read {len(rows)} merge-eligible row conversions")
    print(f"Wrote {len(groups)} merge candidate groups to {repo_relative(candidates_output)}")
    print(f"Wrote {len(tasks)} merge review tasks to {repo_relative(output)}")
    if args.replace_queue_prefix:
        added = replace_queue_prefix(queue, lock, tasks)
        ensure_registry(registry, added)
        print(f"Replaced {TASK_PREFIX} entries in {repo_relative(queue)} with {added} pending tasks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
