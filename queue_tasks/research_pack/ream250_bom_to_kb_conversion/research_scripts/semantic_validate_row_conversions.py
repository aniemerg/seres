#!/usr/bin/env python3
"""Semantic-validate reAM250 BOM-to-KB row conversion batches.

This is a semantic warning layer on top of schema_validate_row_conversions.py.
The schema validator enforces hard consistency rules; this script reports batch
state and semantic warnings that are useful after running many workers.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

import schema_validate_row_conversions


REPO_ROOT = Path(__file__).resolve().parents[4]
ROW_HEADING = "## KB Conversion"
WORK_QUEUE = Path("out/work_queue.jsonl")

NARROW_KEY_REPLACEMENTS = {
    "rigid_flanged_plumbing_connection_section": "plumbing_connection",
    "structural_frame_rail_member": "structural_frame_member",
    "linear_guidance_carriage": "linear_guidance",
    "machine_enclosure_barrier_panel": "enclosure_barrier",
}

POWDER_RE = re.compile(
    r"\b(recoater|powder|powder[-_ ]?bed|powder[-_ ]?handling)\b",
    re.IGNORECASE,
)
FORM_DETAIL_IN_KEY_RE = re.compile(
    r"(^|_)(flanged|section|rail|carriage|panel|plate|cover|length|slot|tube|profile)(_|$)",
    re.IGNORECASE,
)


@dataclass
class RowRecord:
    path: Path
    rel: str
    source_text: str
    data: dict[str, Any]
    validator_issues: list[str] = field(default_factory=list)


@dataclass
class QueueAudit:
    status_counts: Counter[str] = field(default_factory=Counter)
    row_status_counts: Counter[str] = field(default_factory=Counter)
    active_leases: list[str] = field(default_factory=list)
    pending_with_conversion: list[str] = field(default_factory=list)
    done_without_conversion: list[str] = field(default_factory=list)


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_queue() -> list[dict[str, Any]]:
    path = REPO_ROOT / WORK_QUEUE
    if not path.exists():
        return []
    items: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        items.append(json.loads(line))
    return items


def conversion_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted((REPO_ROOT / "research/ream250_bom").glob("ream250_bom_row_*.md")):
        text = path.read_text(encoding="utf-8")
        if re.search(rf"(?m)^{re.escape(ROW_HEADING)}\s*$", text):
            files.append(path)
    return files


def load_row(path: Path) -> RowRecord:
    text = path.read_text(encoding="utf-8")
    pre, section = schema_validate_row_conversions.split_kb_conversion(text)
    data = schema_validate_row_conversions.parse_fenced_yaml(section)
    issues = schema_validate_row_conversions.validate_conversion_file(path)
    return RowRecord(
        path=path,
        rel=repo_relative(path),
        source_text=pre,
        data=data,
        validator_issues=issues,
    )


def row_haystack(row: RowRecord) -> str:
    sections = [
        row.source_text,
        str(row.data.get("decomposition", "")),
        str(row.data.get("process_abstraction", "")),
        str(row.data.get("identity_for_merge", "")),
        str(row.data.get("merge_pool", "")),
    ]
    return "\n".join(sections)


def is_sheet_plate_like_identity(text: str) -> bool:
    """Return true for cover/panel/guard style plate work, not heavy base plates."""
    tokens = [token for token in re.split(r"[^A-Za-z0-9]+|_", text.lower()) if token]
    token_set = set(tokens)
    if token_set & {"cover", "panel", "guard", "barrier"}:
        return True
    if token_set & {"shallow", "sheet", "thin"} and token_set & {"plate", "cover", "panel"}:
        return True
    return False


def audit_queue(rows_by_rel: dict[str, RowRecord]) -> QueueAudit:
    audit = QueueAudit()
    for item in load_queue():
        status = str(item.get("status") or "")
        audit.status_counts[status] += 1
        if item.get("lease_id") and status != "done":
            audit.active_leases.append(
                f"{item.get('id')} ({status}, lease={item.get('lease_id')})"
            )

        task_id = str(item.get("id") or "")
        if not task_id.startswith("research_task:ream250_kb_row_"):
            continue

        audit.row_status_counts[status] += 1
        output_path = item.get("context", {}).get("output_path")
        if not output_path:
            continue
        has_conversion = output_path in rows_by_rel
        if status == "pending" and has_conversion:
            audit.pending_with_conversion.append(output_path)
        if status == "done" and not has_conversion:
            audit.done_without_conversion.append(output_path)
    return audit


def warning_for_row(row: RowRecord) -> list[str]:
    warnings: list[str] = []
    data = row.data
    process = data.get("process_abstraction") or {}
    identity = data.get("identity_for_merge") or {}
    merge_pool = data.get("merge_pool") or {}
    downstream = data.get("downstream_decision_inputs") or {}

    primary = str(process.get("primary_process_bucket") or "")
    key = str(merge_pool.get("functional_purpose_key") or "")
    material = str(identity.get("material") or "")
    local_paths = downstream.get("local_manufacturing_paths_considered") or []
    if not isinstance(local_paths, list):
        local_paths = []

    if key in NARROW_KEY_REPLACEMENTS:
        warnings.append(
            f"functional_purpose_key `{key}` is narrow; prefer "
            f"`{NARROW_KEY_REPLACEMENTS[key]}`"
        )

    if key and FORM_DETAIL_IN_KEY_RE.search(key):
        warnings.append(
            f"functional_purpose_key `{key}` appears to contain component form detail"
        )

    haystack = row_haystack(row)
    identity_text = "\n".join(
        [
            str(identity.get("functional_purpose") or ""),
            str(identity.get("geometry_form") or ""),
            key,
        ]
    )
    if is_sheet_plate_like_identity(identity_text) and primary == "general_subtractive_machining":
        warnings.append(
            "plate-like cover/panel/guard uses `general_subtractive_machining`; "
            "consider `sheet_plate_cutting_drilling` with machining as supporting work"
        )

    if POWDER_RE.search(haystack) and key == "enclosure_barrier":
        warnings.append(
            "powder/recoater row uses `enclosure_barrier`; consider `powder_containment`"
        )

    if local_paths and primary not in local_paths:
        warnings.append(
            f"primary bucket `{primary}` is not listed in local_manufacturing_paths_considered"
        )

    if len(local_paths) > 2:
        warnings.append(
            "local_manufacturing_paths_considered has more than two paths; "
            "keep it focused on the selected closure path"
        )

    if "unknown" in material.lower() and len(local_paths) > 1:
        warnings.append(
            "material is unresolved and multiple local manufacturing paths are listed; "
            "move speculative material-driven alternatives to assumptions/unresolved/import risks"
        )

    return warnings


def render_count_table(title: str, counts: Counter[str]) -> list[str]:
    lines = [f"## {title}", ""]
    if not counts:
        lines.append("_None._")
        lines.append("")
        return lines
    for key, count in counts.most_common():
        lines.append(f"- `{key}`: {count}")
    lines.append("")
    return lines


def render_list(title: str, items: list[str], limit: int | None = None) -> list[str]:
    lines = [f"## {title}", ""]
    if not items:
        lines.append("_None._")
        lines.append("")
        return lines
    shown = items if limit is None else items[:limit]
    for item in shown:
        lines.append(f"- {item}")
    if limit is not None and len(items) > limit:
        lines.append(f"- ... {len(items) - limit} more")
    lines.append("")
    return lines


def warning_entries(warnings_by_row: dict[str, list[str]]) -> set[str]:
    entries: set[str] = set()
    for rel, warnings in warnings_by_row.items():
        for warning in warnings:
            entries.add(f"{rel}\t{warning}")
    return entries


def parse_warning_entries_from_report(path: Path) -> set[str]:
    if not path.exists():
        return set()
    entries: set[str] = set()
    current_row: str | None = None
    in_warnings = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Semantic Warnings"):
            in_warnings = True
            current_row = None
            continue
        if in_warnings and line.startswith("## "):
            break
        if not in_warnings:
            continue
        row_match = re.match(r"- `([^`]+)`\s*$", line)
        if row_match:
            current_row = row_match.group(1)
            continue
        warning_match = re.match(r"\s+- (.+)$", line)
        if current_row and warning_match:
            entries.add(f"{current_row}\t{warning_match.group(1)}")
    return entries


def format_warning_entry(entry: str) -> str:
    rel, warning = entry.split("\t", 1)
    return f"`{rel}` - {warning}"


def random_review_sample(
    rows: list[RowRecord],
    warnings_by_row: dict[str, list[str]],
    *,
    sample_size: int,
    seed: int,
) -> list[str]:
    if sample_size <= 0:
        return []
    warning_rows = set(warnings_by_row)
    candidates = [row for row in rows if row.rel not in warning_rows and not row.validator_issues]
    rng = random.Random(seed)
    sample = rng.sample(candidates, k=min(sample_size, len(candidates)))
    lines: list[str] = []
    for row in sorted(sample, key=lambda item: item.rel):
        process = row.data.get("process_abstraction") or {}
        merge_pool = row.data.get("merge_pool") or {}
        lines.append(
            f"`{row.rel}` - key `{merge_pool.get('functional_purpose_key')}`, "
            f"bucket `{process.get('primary_process_bucket')}`"
        )
    return lines


def build_report(
    rows: list[RowRecord],
    queue: QueueAudit,
    *,
    warning_limit: int,
    previous_warning_entries: set[str] | None = None,
    sample_size: int = 5,
    sample_seed: int = 0,
) -> tuple[str, bool, bool]:
    hard_errors: list[str] = []
    warnings_by_row: dict[str, list[str]] = {}
    bucket_counts: Counter[str] = Counter()
    key_counts: Counter[str] = Counter()
    singleton_keys: list[str] = []

    for row in rows:
        if row.validator_issues:
            for issue in row.validator_issues:
                hard_errors.append(f"{row.rel}: {issue}")
        process = row.data.get("process_abstraction") or {}
        merge_pool = row.data.get("merge_pool") or {}
        bucket_counts[str(process.get("primary_process_bucket") or "<missing>")] += 1
        key_counts[str(merge_pool.get("functional_purpose_key") or "<missing>")] += 1
        warnings = warning_for_row(row)
        if warnings:
            warnings_by_row[row.rel] = warnings

    hard_errors.extend(f"pending task already has conversion: {p}" for p in queue.pending_with_conversion)
    hard_errors.extend(f"done task is missing conversion: {p}" for p in queue.done_without_conversion)

    for key, count in sorted(key_counts.items()):
        if count == 1 and key != "<missing>":
            singleton_keys.append(key)

    lines: list[str] = [
        "# reAM250 BOM-to-KB Row Conversion Semantic Validate",
        "",
        "## Summary",
        "",
        f"- Conversion files: {len(rows)}",
        f"- Hard errors: {len(hard_errors)}",
        f"- Warning rows: {len(warnings_by_row)}",
        f"- Warning count: {sum(len(v) for v in warnings_by_row.values())}",
        "",
    ]
    lines.extend(render_count_table("Queue Status", queue.status_counts))
    lines.extend(render_count_table("Row Conversion Queue Status", queue.row_status_counts))
    lines.extend(render_count_table("Primary Process Buckets", bucket_counts))
    lines.extend(render_count_table("Functional Purpose Keys", key_counts))
    lines.extend(render_list("Active Leases", queue.active_leases, limit=warning_limit))
    lines.extend(render_list("Hard Errors", hard_errors, limit=warning_limit))

    lines.append("## Semantic Warnings")
    lines.append("")
    if not warnings_by_row:
        lines.append("_None._")
        lines.append("")
    else:
        emitted = 0
        for rel, warnings in sorted(warnings_by_row.items()):
            if emitted >= warning_limit:
                remaining = len(warnings_by_row) - emitted
                lines.append(f"- ... {remaining} more rows with warnings")
                break
            lines.append(f"- `{rel}`")
            for warning in warnings:
                lines.append(f"  - {warning}")
            emitted += 1
        lines.append("")

    current_warning_entries = warning_entries(warnings_by_row)
    new_warning_entries = (
        sorted(current_warning_entries - previous_warning_entries)
        if previous_warning_entries is not None
        else []
    )
    lines.append("## New Semantic Warnings")
    lines.append("")
    if previous_warning_entries is None:
        lines.append("_No previous report provided._")
    elif not new_warning_entries:
        lines.append("_None._")
    else:
        for entry in new_warning_entries[:warning_limit]:
            lines.append(f"- {format_warning_entry(entry)}")
        if len(new_warning_entries) > warning_limit:
            lines.append(f"- ... {len(new_warning_entries) - warning_limit} more")
    lines.append("")

    lines.append("## Random Review Sample")
    lines.append("")
    sample = random_review_sample(
        rows,
        warnings_by_row,
        sample_size=sample_size,
        seed=sample_seed,
    )
    if not sample:
        lines.append("_None._")
    else:
        for item in sample:
            lines.append(f"- {item}")
    lines.append("")

    lines.append("## Singleton Functional Keys")
    lines.append("")
    if not singleton_keys:
        lines.append("_None._")
    else:
        for key in singleton_keys[:warning_limit]:
            lines.append(f"- `{key}`")
        if len(singleton_keys) > warning_limit:
            lines.append(f"- ... {len(singleton_keys) - warning_limit} more")
    lines.append("")

    return "\n".join(lines), bool(hard_errors), bool(warnings_by_row)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the Markdown report to this path instead of stdout.",
    )
    parser.add_argument(
        "--warning-limit",
        type=int,
        default=80,
        help="Maximum rows/items to show in long report sections.",
    )
    parser.add_argument(
        "--previous-report",
        type=Path,
        help="Compare semantic warnings against a previous Markdown semantic validate report.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=5,
        help="Number of no-warning rows to include for random LLM/manual review. Default: 5.",
    )
    parser.add_argument(
        "--sample-seed",
        type=int,
        default=0,
        help="Deterministic seed for random review sample. Default: 0.",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return non-zero when semantic warnings are present.",
    )
    args = parser.parse_args()

    try:
        rows = [load_row(path) for path in conversion_files()]
    except Exception as exc:
        print(f"semantic validate failed while loading conversions: {exc}", file=sys.stderr)
        return 2

    rows_by_rel = {row.rel: row for row in rows}
    queue = audit_queue(rows_by_rel)
    previous_warning_entries = None
    if args.previous_report:
        previous = args.previous_report if args.previous_report.is_absolute() else REPO_ROOT / args.previous_report
        previous_warning_entries = parse_warning_entries_from_report(previous)
    report, has_hard_errors, has_warnings = build_report(
        rows,
        queue,
        warning_limit=args.warning_limit,
        previous_warning_entries=previous_warning_entries,
        sample_size=args.sample_size,
        sample_seed=args.sample_seed,
    )

    if args.output:
        output = args.output if args.output.is_absolute() else REPO_ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote semantic validate report: {repo_relative(output)}")
    else:
        print(report)

    if has_hard_errors:
        return 1
    if args.fail_on_warning and has_warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
