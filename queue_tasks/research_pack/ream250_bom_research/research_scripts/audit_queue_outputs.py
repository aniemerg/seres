#!/usr/bin/env python3
"""Audit reAM250 BOM research queue state against result outputs.

This is deliberately separate from validate_results.py. The validator checks
files that exist. This audit checks queue bookkeeping and accepts legacy done
items whose historical output artifacts are no longer present.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any

import validate_results


TASK_PREFIX = "research_task:ream250_bom_row_"

# 2026-06-16 13:47:00 local project run time, when the stricter result schema
# and --require-output/--validate-output workflow became the active baseline.
DEFAULT_LEGACY_CUTOFF_EPOCH = 1781632020.0


def load_queue(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not path.exists():
        raise FileNotFoundError(f"queue file does not exist: {path}")
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        if str(obj.get("id", "")).startswith(TASK_PREFIX):
            items.append(obj)
    return items


def validate_output(path: Path) -> list[str]:
    try:
        data = validate_results.load_result(path)
        return validate_results.validate_result(data)
    except Exception as exc:
        return [str(exc)]


def fmt_time(value: Any) -> str:
    if not isinstance(value, (int, float)):
        return "unknown"
    return dt.datetime.fromtimestamp(value).isoformat(sep=" ", timespec="seconds")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit reAM250 BOM research queue outputs without failing accepted legacy done items."
    )
    parser.add_argument("--queue", type=Path, default=Path("out/work_queue.jsonl"))
    parser.add_argument(
        "--legacy-cutoff-epoch",
        type=float,
        default=DEFAULT_LEGACY_CUTOFF_EPOCH,
        help=(
            "Done items completed before this epoch may have missing output files "
            "without failing the audit. Default: %(default)s"
        ),
    )
    parser.add_argument(
        "--no-validate-existing",
        action="store_true",
        help="Only check file presence; do not validate existing result files.",
    )
    args = parser.parse_args()

    items = load_queue(args.queue)
    counts: dict[str, int] = {}
    for item in items:
        status = item.get("status") or "pending"
        counts[status] = counts.get(status, 0) + 1

    existing_ok: list[str] = []
    existing_invalid: list[tuple[str, str, list[str]]] = []
    missing_current: list[tuple[str, str, Any]] = []
    missing_legacy: list[tuple[str, str, Any]] = []

    for item in items:
        if item.get("status") != "done":
            continue
        item_id = str(item.get("id", ""))
        context = item.get("context") if isinstance(item.get("context"), dict) else {}
        output_value = context.get("output_path")
        output_path = Path(output_value) if output_value else None
        completed_at = item.get("completed_at")

        if not output_path or not output_path.exists():
            row = (item_id, str(output_path or ""), completed_at)
            if isinstance(completed_at, (int, float)) and completed_at < args.legacy_cutoff_epoch:
                missing_legacy.append(row)
            else:
                missing_current.append(row)
            continue

        if args.no_validate_existing:
            existing_ok.append(item_id)
            continue

        issues = validate_output(output_path)
        if issues:
            existing_invalid.append((item_id, str(output_path), issues))
        else:
            existing_ok.append(item_id)

    print("reAM250 BOM queue/output audit")
    print(f"queue: {args.queue}")
    print(
        "counts: "
        + ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    )
    print(f"done_outputs_valid_or_present: {len(existing_ok)}")
    print(f"legacy_done_without_output_accepted: {len(missing_legacy)}")
    print(f"current_done_without_output_errors: {len(missing_current)}")
    print(f"existing_output_validation_errors: {len(existing_invalid)}")

    if missing_legacy:
        print("\nAccepted legacy done items without current output:")
        for item_id, output_path, completed_at in missing_legacy:
            print(f"- {item_id} ({fmt_time(completed_at)}): {output_path}")

    if missing_current:
        print("\nCurrent done items missing output:")
        for item_id, output_path, completed_at in missing_current:
            print(f"- {item_id} ({fmt_time(completed_at)}): {output_path}")

    if existing_invalid:
        print("\nExisting output validation failures:")
        for item_id, output_path, issues in existing_invalid:
            print(f"- {item_id}: {output_path}")
            for issue in issues:
                print(f"  - {issue}")

    return 1 if missing_current or existing_invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
