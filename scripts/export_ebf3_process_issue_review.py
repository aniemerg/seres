#!/usr/bin/env python3
"""Export the EBF3 process issue review table into SimViewer JSON."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = ROOT / "research/ebf3_bom_sources/derived/ebf3_process_issue_review.csv"
OUT_JSON = ROOT / "apps/simviewer/public/data/ebf3_process_issue_review.json"

STRING_LIST_FIELDS = {
    "current_process_ids",
    "current_machine_ids",
    "decision_machine_ids",
    "machine_selection_statuses",
    "machine_risk_flags",
    "machine_evidence_sources",
}


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def parse_float(value: str) -> float | None:
    if not value.strip():
        return None
    try:
        return float(value)
    except ValueError:
        return None


def row_to_json(row: dict[str, str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in row.items():
        clean = value.strip()
        if key in STRING_LIST_FIELDS:
            out[key] = split_semicolon(clean)
        elif key in {"priority"}:
            out[key] = int(float(clean)) if clean else None
        elif key in {"mass_nominal_kg"}:
            out[key] = parse_float(clean)
        elif key == "recipe_exists":
            out[key] = clean.lower() == "true"
        else:
            out[key] = clean
    return out


def count(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(Counter(str(row.get(field) or "blank") for row in rows))


def main() -> None:
    with IN_CSV.open(newline="", encoding="utf-8") as handle:
        rows = [row_to_json(row) for row in csv.DictReader(handle)]

    payload = {
        "summary": {
            "total": len(rows),
            "worker_decision": count(rows, "worker_decision"),
            "policy": count(rows, "policy"),
            "queue_reason": count(rows, "queue_reason"),
            "route_decision": count(rows, "route_decision"),
        },
        "rows": rows,
        "sources": {
            "csv": str(IN_CSV.relative_to(ROOT)),
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"exported {len(rows)} rows to {OUT_JSON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
