#!/usr/bin/env python3
"""Audit machine entries for process-selection readiness.

This script is intentionally conservative: it does not delete or deprecate
machines. It adds/removes `machine_audit_*` trust tags and writes review reports
so process selection can filter out risky entries without breaking existing
references.

`capabilities_count` is reported as metadata only. A missing `capabilities` list
is not itself a risk tag because many older machines declare their function via
process resource use, notes, or `processes_supported`.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.paths import KB_ROOT


AUDIT_TAGS = {
    "machine_audit_closure_blocked",
    "machine_audit_deprecated",
    "machine_audit_duplicate_candidate",
    "machine_audit_imported",
    "machine_audit_misplaced_file",
    "machine_audit_no_capabilities",
    "machine_audit_no_declared_support",
    "machine_audit_placeholder",
    "machine_audit_semantic_mismatch",
    "machine_audit_stub",
}


PLACEHOLDER_WORDS = ("placeholder", "tbd", "dummy", "provisional")
STUB_WORDS = ("stub", "created during adr 003 migration")
DEPRECATED_WORDS = ("deprecated", "consolidated into")


DOMAIN_PATTERNS = [
    (
        "metal_spinning",
        re.compile(r"\bmetal[_ -]?spinning\b|spin[- ]?form|spun\b", re.I),
        re.compile(r"\bmetal[_ -]?spinning\b|spin[- ]?form|metal[_ -]?forming|lathe", re.I),
    ),
    (
        "wire_drawing",
        re.compile(r"\bwire[_ -]?drawing\b|drawn wire|drawing .*wire", re.I),
        re.compile(r"\bwire\b.*\bdrawing\b|\bdrawing\b.*\bwire\b|\bdie\b", re.I),
    ),
    (
        "ceramic_sintering",
        re.compile(r"ceramic.*sinter|sinter.*ceramic|firing ceramic|ceramic firing|porcelain", re.I),
        re.compile(r"ceramic|kiln|sinter|furnace|hot press|hot[_ -]?press", re.I),
    ),
    (
        "ceramic_forming",
        re.compile(r"ceramic.*form|form.*ceramic|green ceramic|ceramic.*press", re.I),
        re.compile(r"ceramic|press|mold|compaction|forming", re.I),
    ),
    (
        "textile",
        re.compile(r"textile|weav|knit|yarn|fiber", re.I),
        re.compile(r"textile|weav|knit|yarn|fiber|spinning|tension", re.I),
    ),
    (
        "machining",
        re.compile(r"machin|milling|turning|reaming|threading", re.I),
        re.compile(r"machin|mill|lathe|cutting|drilling|reaming|threading", re.I),
    ),
    (
        "casting",
        re.compile(r"casting|cast\b|mold.*metal|molten", re.I),
        re.compile(r"casting|cast|mold|melting|furnace", re.I),
    ),
    (
        "chemical",
        re.compile(r"chemical|reactor|leach|precipitation|synthesis|neutralization", re.I),
        re.compile(r"chemical|reactor|leach|precipitation|synthesis|agitation|processing", re.I),
    ),
    (
        "assembly",
        re.compile(r"assembly|install|integration|fasten|wiring", re.I),
        re.compile(r"assembly|tool|fixtur|labor|wiring|mechanical|electrical", re.I),
    ),
]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def machine_paths() -> list[Path]:
    roots = [KB_ROOT / "items", KB_ROOT / "imports"]
    paths: list[Path] = []
    for root in roots:
        if root.exists():
            paths.extend(root.rglob("*.yaml"))
    return sorted(paths)


def is_machine(data: dict[str, Any]) -> bool:
    return data.get("kind") == "machine"


def compile_exclusion_patterns(values: list[str]) -> list[re.Pattern[str]]:
    return [re.compile(value, re.I) for value in values]


def is_excluded(
    machine_id: str,
    data: dict[str, Any],
    path: Path,
    patterns: list[re.Pattern[str]],
) -> bool:
    text = " ".join([machine_id, str(data.get("name", "")), str(path)])
    return any(pattern.search(text) for pattern in patterns)


def normalized_name(machine_id: str, data: dict[str, Any]) -> str:
    name = str(data.get("name") or machine_id).lower()
    name = re.sub(r"\bv0\b|\(v0\)|basic|simple|general|standard", "", name)
    return re.sub(r"[^a-z0-9]+", " ", name).strip()


def process_search_text(data: dict[str, Any]) -> str:
    return " ".join(
        [
            str(data.get("id", "")),
            str(data.get("name", "")),
            str(data.get("notes", "")),
        ]
    ).lower()


def process_domain_text(data: dict[str, Any]) -> str:
    return " ".join([str(data.get("id", "")), str(data.get("name", ""))]).lower()


def machine_search_text(machine_id: str, data: dict[str, Any]) -> str:
    return " ".join(
        [
            machine_id,
            str(data.get("name", "")),
            " ".join(str(cap) for cap in data.get("capabilities") or []),
            " ".join(str(proc) for proc in data.get("processes_supported") or []),
            str(data.get("notes", "")),
        ]
    ).lower()


def collect_resource_uses() -> dict[str, list[dict[str, str]]]:
    uses: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in (KB_ROOT / "processes").glob("*.yaml"):
        data = load_yaml(path)
        if data.get("kind") != "process":
            continue
        process_id = str(data.get("id") or path.stem)
        machine_ids = [
            str(req.get("machine_id") or req.get("resource_type"))
            for req in data.get("resource_requirements") or []
            if isinstance(req, dict) and (req.get("machine_id") or req.get("resource_type"))
        ]
        unique_machine_count = len(set(machine_ids))
        for req in data.get("resource_requirements") or []:
            if not isinstance(req, dict):
                continue
            machine_id = req.get("machine_id") or req.get("resource_type")
            if machine_id:
                uses[str(machine_id)].append(
                    {
                        "id": process_id,
                        "name": str(data.get("name") or ""),
                        "path": str(path.relative_to(REPO_ROOT)),
                        "search_text": process_search_text(data),
                        "domain_text": process_domain_text(data),
                        "unique_machine_count": str(unique_machine_count),
                    }
                )
    return uses


def collect_closure_errors() -> dict[str, list[str]]:
    out: dict[str, list[str]] = defaultdict(list)
    path = Path("out/closure_errors.jsonl")
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        ctx = row.get("context") or {}
        machine_id = ctx.get("detected_in_machine")
        item_id = ctx.get("item_id")
        if machine_id:
            out[str(machine_id)].append(str(item_id or "unknown"))
    return out


def collect_duplicate_groups(machines: list[tuple[str, dict[str, Any], Path]]) -> dict[str, list[str]]:
    by_name: dict[str, list[str]] = defaultdict(list)
    by_id: dict[str, list[str]] = defaultdict(list)
    for machine_id, data, _path in machines:
        by_name[normalized_name(machine_id, data)].append(machine_id)
        by_id[machine_id].append(machine_id)

    groups: dict[str, list[str]] = {}
    for vals in by_name.values():
        unique = sorted(set(vals))
        if len(unique) > 1:
            for machine_id in unique:
                groups[machine_id] = unique
    for machine_id, vals in by_id.items():
        if len(vals) > 1:
            groups[machine_id] = sorted(set(vals))
    return groups


def function_evidence(machine_id: str, data: dict[str, Any], path: Path, uses: list[dict[str, str]]) -> list[str]:
    evidence: list[str] = []
    notes = str(data.get("notes") or "").strip()
    if data.get("capabilities"):
        evidence.append("capabilities")
    if data.get("processes_supported"):
        evidence.append("processes_supported")
    if uses:
        evidence.append("process_resource_use")
    if notes and not any(word in notes.lower() for word in PLACEHOLDER_WORDS + STUB_WORDS):
        evidence.append("functional_notes")
    if data.get("bom"):
        evidence.append("bom")
    if data.get("recipe"):
        evidence.append("recipe")
    if path.exists():
        evidence.append("machine_file")
    return evidence


def semantic_mismatches(machine_id: str, data: dict[str, Any], uses: list[dict[str, str]]) -> list[str]:
    machine_text = machine_search_text(machine_id, data)
    out: list[str] = []
    for use in uses:
        if int(use.get("unique_machine_count") or "1") > 1:
            continue
        process_text = use["domain_text"]
        for domain, process_re, machine_re in DOMAIN_PATTERNS:
            if process_re.search(process_text) and not machine_re.search(machine_text):
                out.append(f"{use['id']}:{domain}")
                break
    return out


def selection_status(
    excluded: bool,
    audit_tags: list[str],
    evidence: list[str],
    mismatches: list[str],
    resource_use_count: int,
) -> str:
    tag_set = set(audit_tags)
    if excluded:
        return "excluded_by_pattern"
    if "machine_audit_imported" in tag_set:
        return "avoid_imported"
    if "machine_audit_closure_blocked" in tag_set:
        return "blocked_closure"
    if "machine_audit_deprecated" in tag_set:
        return "avoid_deprecated"
    if mismatches:
        return "review_semantic_mismatch"
    if "machine_audit_placeholder" in tag_set or "machine_audit_stub" in tag_set:
        return "review_placeholder_or_stub"
    if resource_use_count and "functional_notes" in evidence:
        return "usable_unreviewed"
    if resource_use_count and ("capabilities" in evidence or "processes_supported" in evidence):
        return "usable_metadata_only"
    if "capabilities" in evidence and not resource_use_count:
        return "metadata_only_no_usage"
    if "functional_notes" in evidence:
        return "named_function_no_usage"
    return "unknown_or_unsupported"


def merge_trust_tags(
    existing_tags: list[str],
    audit_tags: list[str],
    excluded: bool,
) -> list[str]:
    if excluded:
        return existing_tags
    non_audit_tags = [tag for tag in existing_tags if tag not in AUDIT_TAGS]
    return non_audit_tags + [
        tag for tag in sorted(set(audit_tags)) if tag not in non_audit_tags
    ]


def update_trust_tags_text(text: str, tags: list[str]) -> str:
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^trust_tags\s*:", line):
            start = i
            break

    block = []
    if tags:
        block = ["trust_tags:\n"] + [f"- {tag}\n" for tag in tags]

    if start is None:
        insert_at = len(lines)
        while insert_at > 0 and not lines[insert_at - 1].strip():
            insert_at -= 1
        return "".join(lines[:insert_at] + block + lines[insert_at:])

    end = start + 1
    while end < len(lines):
        line = lines[end]
        if re.match(r"^[A-Za-z0-9_].*:\s*", line):
            break
        if line.startswith("- ") or not line.strip() or line.startswith("  "):
            end += 1
            continue
        break
    return "".join(lines[:start] + block + lines[end:])


def audit(apply: bool, exclude_patterns: list[re.Pattern[str]] | None = None) -> None:
    exclude_patterns = exclude_patterns or []
    machines: list[tuple[str, dict[str, Any], Path]] = []
    for path in machine_paths():
        data = load_yaml(path)
        if is_machine(data):
            machines.append((str(data.get("id") or path.stem), data, path))

    uses = collect_resource_uses()
    closure = collect_closure_errors()
    duplicate_groups = collect_duplicate_groups(machines)
    rows: list[dict[str, Any]] = []
    changed = 0

    for machine_id, data, path in machines:
        relative_path = path.relative_to(KB_ROOT).as_posix()
        excluded = is_excluded(machine_id, data, path, exclude_patterns)
        capabilities = data.get("capabilities") or []
        processes_supported = data.get("processes_supported") or []
        machine_uses = uses.get(machine_id, [])
        existing_tags = [str(tag) for tag in data.get("trust_tags") or []]
        audit_tags: list[str] = []

        if not excluded:
            searchable_text = " ".join(
                [machine_id, str(data.get("name", "")), str(data.get("notes", ""))]
            ).lower()
            if closure.get(machine_id):
                audit_tags.append("machine_audit_closure_blocked")
            if not capabilities and not processes_supported and not machine_uses:
                audit_tags.append("machine_audit_no_declared_support")
            if duplicate_groups.get(machine_id):
                audit_tags.append("machine_audit_duplicate_candidate")
            if relative_path.startswith("items/parts/"):
                audit_tags.append("machine_audit_misplaced_file")
            if relative_path.startswith("imports/") or data.get("is_import") is True:
                audit_tags.append("machine_audit_imported")
            if any(word in searchable_text for word in PLACEHOLDER_WORDS):
                audit_tags.append("machine_audit_placeholder")
            if any(word in searchable_text for word in STUB_WORDS):
                audit_tags.append("machine_audit_stub")
            if any(word in searchable_text for word in DEPRECATED_WORDS):
                audit_tags.append("machine_audit_deprecated")

        evidence = function_evidence(machine_id, data, path, machine_uses)
        mismatches = semantic_mismatches(machine_id, data, machine_uses)
        if mismatches and not excluded:
            audit_tags.append("machine_audit_semantic_mismatch")

        reported_audit_tags = (
            [tag for tag in existing_tags if tag in AUDIT_TAGS]
            if excluded
            else audit_tags
        )
        final_tags = merge_trust_tags(existing_tags, audit_tags, excluded)

        if apply and final_tags != existing_tags:
            text = path.read_text(encoding="utf-8")
            path.write_text(update_trust_tags_text(text, final_tags), encoding="utf-8")
            changed += 1

        rows.append(
            {
                "id": machine_id,
                "name": data.get("name") or "",
                "path": str(path.relative_to(REPO_ROOT)),
                "excluded_by_pattern": excluded,
                "audit_tags": ";".join(reported_audit_tags),
                "selection_status": selection_status(
                    excluded,
                    audit_tags,
                    evidence,
                    mismatches,
                    len(machine_uses),
                ),
                "evidence_sources": ";".join(evidence),
                "risk_flags": ";".join(sorted(set(reported_audit_tags))),
                "use_mismatch_count": len(mismatches),
                "use_mismatch_examples": ";".join(mismatches[:5]),
                "resource_use_count": len(machine_uses),
                "capabilities_count": len(capabilities),
                "processes_supported_count": len(processes_supported),
                "closure_missing_items": ";".join(closure.get(machine_id, [])),
                "duplicate_group": ";".join(duplicate_groups.get(machine_id, [])),
            }
        )

    out_dir = Path("out/machine_audit")
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "machine_process_selection_audit.csv"
    if not rows:
        raise RuntimeError(f"No machine entries found under {KB_ROOT}")
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    tag_counts = Counter(tag for row in rows for tag in str(row["audit_tags"]).split(";") if tag)
    status_counts = Counter(str(row["selection_status"]) for row in rows)
    clean_count = sum(1 for row in rows if not row["audit_tags"] and not row["excluded_by_pattern"])
    excluded_count = sum(1 for row in rows if row["excluded_by_pattern"])
    md_lines = [
        "# Machine Process Selection Audit",
        "",
        "Generated by `scripts/audit_machines.py`.",
        "",
        f"- Total machines: {len(rows)}",
        f"- Clean non-excluded machines: {clean_count}",
        f"- Machines excluded by an explicit pattern: {excluded_count}",
        "",
        "## Audit Tag Counts",
        "",
    ]
    for tag, count in tag_counts.most_common():
        md_lines.append(f"- `{tag}`: {count}")
    md_lines.extend(
        [
            "",
            "## Selection Status Counts",
            "",
        ]
    )
    for status, count in status_counts.most_common():
        md_lines.append(f"- `{status}`: {count}")
    md_lines.extend(
        [
            "",
            "## Report",
            "",
            f"- CSV: `{csv_path}`",
            "",
            "Use `selection_status` and `evidence_sources` for process-selection review.",
            "Do not treat `capabilities` alone as proof that a machine is ready.",
            "Machines with `usable_unreviewed` have functional evidence but still need",
            "item/process-specific review before being used for nominal local routes.",
            "",
        ]
    )
    (out_dir / "README.md").write_text("\n".join(md_lines), encoding="utf-8")

    print(
        f"machines={len(rows)} changed={changed} "
        f"clean_non_excluded={clean_count} excluded={excluded_count}"
    )
    for tag, count in tag_counts.most_common():
        print(f"{tag}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write audit tags back into machine trust_tags")
    parser.add_argument(
        "--exclude-pattern",
        action="append",
        default=[],
        metavar="REGEX",
        help="exclude matching machine IDs, names, or paths from automatic tagging; repeatable",
    )
    args = parser.parse_args()
    try:
        patterns = compile_exclusion_patterns(args.exclude_pattern)
    except re.error as exc:
        parser.error(f"invalid --exclude-pattern: {exc}")
    audit(apply=args.apply, exclude_patterns=patterns)


if __name__ == "__main__":
    main()
