#!/usr/bin/env python3
"""Export current KB EBF3 route-review item metadata into SimViewer JSON."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
RECIPE_DIR = ROOT / "kb/recipes"
ITEM_DIRS = [ROOT / "kb/items", ROOT / "kb/imports"]
OUT_JSON = ROOT / "apps/simviewer/public/data/ebf3_route_audit.json"

LABELS = [
    "Route decision",
    "Simulation import mass policy",
    "Executable first-pass process",
    "Material",
    "Material class",
    "Lunar availability class",
    "Mass used for first-pass accounting",
    "Parent ids",
    "Primary local process candidate",
    "Secondary process candidates",
    "Ready machine ids considered",
    "Blocked machine or process reason",
    "Critical performance requirements",
    "Confidence",
    "Flags",
    "Reasoning",
    "Prior disposition",
    "Reason",
    "Next step",
]

LOCAL_DECISIONS = {"lunar_candidate", "lunar_candidate_flagged"}
IMPORT_DECISIONS = {"earth_import", "route_gap", "defer_import_fallback", "import_as_leaf", "defer_split_import_fallback"}


def split_semicolon(value: str | None) -> list[str]:
    if not value or value == "none":
        return []
    return [part.strip() for part in value.split(";") if part.strip() and part.strip() != "none"]


def clean_value(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"\s+", " ", value).strip()
    return value[:-1] if value.endswith(".") else value


def as_float(value: str | None) -> float | None:
    if not value:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", value)
    if not match:
        return None
    return float(match.group(0))


def route_group(decision: str, policy: str) -> str:
    if decision in LOCAL_DECISIONS or policy in {"local_nominal", "sensitivity_flag"}:
        return "local"
    if decision in IMPORT_DECISIONS or policy in {"import_nominal", "import_until_gap_resolved"}:
        return "import"
    return "other"


def read_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data if isinstance(data, dict) else {}


def parse_note_labels(notes: str) -> dict[str, str]:
    label_pattern = "|".join(re.escape(label) for label in sorted(LABELS, key=len, reverse=True))
    pattern = re.compile(rf"(?:(?<=^)|(?<=\s))({label_pattern}):\s*", re.IGNORECASE)
    matches = list(pattern.finditer(notes or ""))
    out: dict[str, str] = {}
    for idx, match in enumerate(matches):
        key = match.group(1).lower()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(notes)
        out[key] = clean_value(notes[start:end])
    return out


def read_item_paths() -> dict[str, str]:
    paths: dict[str, str] = {}
    for root in ITEM_DIRS:
        if not root.exists():
            continue
        for path in root.rglob("*.yaml"):
            data = read_yaml(path)
            item_id = data.get("id")
            if isinstance(item_id, str):
                paths[item_id] = str(path.relative_to(ROOT))
    return paths


def read_item_entries() -> dict[str, tuple[str, dict[str, Any]]]:
    entries: dict[str, tuple[str, dict[str, Any]]] = {}
    for root in ITEM_DIRS:
        if not root.exists():
            continue
        for path in root.rglob("*.yaml"):
            data = read_yaml(path)
            item_id = data.get("id")
            if isinstance(item_id, str):
                entries[item_id] = (str(path.relative_to(ROOT)), data)
    return entries


def count_values(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(Counter(str(row.get(field, "") or "blank") for row in rows))


def source_queue_type(notes: str) -> str:
    if "ebf3_leaf_decomposition_review.csv" in notes:
        return "leaf_decomposition_review_kb_recipe"
    if "ebf3_reachable_leaf_backfill_route_review.csv" in notes:
        return "reachable_leaf_backfill_kb_recipe"
    if "ebf3_process_route_review.csv" in notes:
        return "process_route_review_kb_recipe"
    return "kb_route_review_recipe"


def main() -> None:
    item_entries = read_item_entries()
    rows: list[dict[str, Any]] = []

    for item_id, (item_path, item) in sorted(item_entries.items()):
        review = item.get("ebf3_route_review")
        if not isinstance(review, dict) or review.get("variant_id") != "ebf3_route_review_v0":
            continue
        decision = clean_value(str(review.get("route_decision") or item.get("route_decision") or ""))
        policy = clean_value(str(review.get("simulation_import_mass_policy") or item.get("simulation_import_mass_policy") or ""))
        material = clean_value(str(item.get("material") or item.get("material_class") or ""))
        primary_process = clean_value(str(review.get("primary_process_id") or review.get("executable_process_id") or ""))
        executable_process = clean_value(str(review.get("executable_process_id") or primary_process))
        if not primary_process:
            primary_process = executable_process

        active_recipe_id = item.get("recipe") if isinstance(item.get("recipe"), str) else ""

        rows.append({
            "batch_id": "",
            "recipe_id": clean_value(active_recipe_id),
            "source_recipe_id": clean_value(str(review.get("source_recipe_id") or "")),
            "item_id": item_id,
            "parent_ids": review.get("parent_ids", []) if isinstance(review.get("parent_ids"), list) else [],
            "source_queue_type": clean_value(str(review.get("source_queue_type") or "kb_route_review_item_metadata")),
            "mass_nominal_kg": review.get("mass_nominal_kg") if isinstance(review.get("mass_nominal_kg"), (int, float)) else None,
            "material": material,
            "availability_class": clean_value(str(review.get("availability_class") or "")),
            "route_group": route_group(decision, policy),
            "route_decision": decision,
            "primary_process_id": primary_process,
            "secondary_process_ids": review.get("secondary_process_ids", []) if isinstance(review.get("secondary_process_ids"), list) else [],
            "ready_machine_ids": review.get("ready_machine_ids", []) if isinstance(review.get("ready_machine_ids"), list) else [],
            "blocked_machine_or_process_reason": clean_value(str(review.get("blocked_machine_or_process_reason") or "")),
            "critical_performance_requirements": clean_value(str(review.get("critical_performance_requirements") or "")),
            "simulation_import_mass_policy": policy,
            "confidence": clean_value(str(review.get("confidence") or "")),
            "flags": review.get("flags", []) if isinstance(review.get("flags"), list) else [],
            "reasoning_brief": clean_value(str(review.get("reasoning_brief") or "")),
            "item_path": item_path,
            "audit_verdict": "",
            "proposed_decision": "",
            "proposed_policy": "",
            "severity": "",
            "issue_type": "",
            "semantic_reasoning": "",
            "recommended_edit": clean_value(str(review.get("recommended_edit") or "")),
            "integration_decision": "",
            "integration_note": "",
        })

    summary = {
        "total": len(rows),
        "route_groups": count_values(rows, "route_group"),
        "route_decisions": count_values(rows, "route_decision"),
        "simulation_import_mass_policy": count_values(rows, "simulation_import_mass_policy"),
        "availability_class": count_values(rows, "availability_class"),
        "confidence": count_values(rows, "confidence"),
        "audit_verdict": count_values(rows, "audit_verdict"),
        "severity": count_values(rows, "severity"),
        "issue_type": count_values(rows, "issue_type"),
        "sources": {
            "kb_route_review_item_metadata": "kb/items/**/ebf3_*.yaml with ebf3_route_review.variant_id=ebf3_route_review_v0",
            "kb_route_review_recipes": "local/sensitivity EBF3 recipes remain in kb/recipes; import recipes are represented by is_import items per ADR-007",
            "legacy_research_csvs": (
                "research/ebf3_bom_sources/derived/ebf3_process_route_review.csv; "
                "research/ebf3_bom_sources/derived/ebf3_leaf_decomposition_review.csv; "
                "research/ebf3_bom_sources/derived/ebf3_reachable_leaf_backfill_route_review.csv"
            ),
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps({"summary": summary, "rows": rows}, indent=2), encoding="utf-8")
    print(f"exported {len(rows)} rows to {OUT_JSON.relative_to(ROOT)}")
    print(json.dumps(summary["simulation_import_mass_policy"], sort_keys=True))


if __name__ == "__main__":
    main()
