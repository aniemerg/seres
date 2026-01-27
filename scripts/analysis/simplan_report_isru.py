#!/usr/bin/env python3
"""
Report per-machine ISRU from a simulation and list imported items.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


def _load_machine_ids(runbook_path: Path) -> List[str]:
    machines: List[str] = []
    with runbook_path.open(encoding="utf-8") as f:
        for line in f:
            if not line.startswith("| "):
                continue
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(parts) < 2 or parts[0] == "Machine":
                continue
            machine_id = parts[0]
            if machine_id and machine_id not in {"—", "---"}:
                machines.append(machine_id)
    return machines


def _isru_from_prov(prov) -> Dict[str, Any]:
    total = prov.in_situ_kg + prov.imported_kg + prov.unknown_kg
    isru_pct = (prov.in_situ_kg / total * 100.0) if total > 0 else 0.0
    return {
        "total_kg": total,
        "in_situ_kg": prov.in_situ_kg,
        "imported_kg": prov.imported_kg,
        "unknown_kg": prov.unknown_kg,
        "isru_percent": isru_pct,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Report ISRU for machines in a sim.")
    parser.add_argument("--sim-id", required=True, help="Simulation id")
    parser.add_argument(
        "--runbook",
        default=str(REPO_ROOT / "runbooks" / "machine_runbook_queue_sequential.md"),
        help="Runbook markdown file with machine list",
    )
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument(
        "--all-imports",
        action="store_true",
        help="Include all imported items (default: machines only)",
    )
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    kb_root = Path(args.kb_root)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_dir = REPO_ROOT / "simulations" / args.sim_id
    engine = SimulationEngine(args.sim_id, kb, sim_dir)
    if not engine.load():
        print(f"Failed to load simulation: {sim_dir}", file=sys.stderr)
        return 1

    machines = _load_machine_ids(Path(args.runbook))
    results: List[Dict[str, Any]] = []
    missing: List[str] = []

    for machine_id in machines:
        prov = engine.state.provenance.get(machine_id)
        if not prov:
            missing.append(machine_id)
            continue
        data = _isru_from_prov(prov)
        data["machine_id"] = machine_id
        results.append(data)

    imported_rows: List[Dict[str, Any]] = []
    for item_id, prov in engine.state.provenance.items():
        total = prov.in_situ_kg + prov.imported_kg + prov.unknown_kg
        if total <= 0 or prov.imported_kg <= 0:
            continue
        item = kb.get_item(item_id)
        kind = None
        if item is not None:
            kind = item.get("kind") if hasattr(item, "get") else getattr(item, "kind", None)
        if not args.all_imports and kind != "machine":
            continue
        imported_rows.append({
            "item_id": item_id,
            "kind": kind,
            "imported_kg": prov.imported_kg,
            "total_kg": total,
            "imported_percent": (prov.imported_kg / total * 100.0) if total > 0 else 0.0,
        })

    imported_rows.sort(key=lambda r: r["imported_kg"], reverse=True)

    output = {
        "sim_id": args.sim_id,
        "machine_isru": results,
        "missing_machines": missing,
        "imported_items": imported_rows,
    }

    if args.json:
        print(json.dumps(output, indent=2))
        return 0

    print(f"ISRU report for sim: {args.sim_id}")
    for row in results:
        print(
            f"- {row['machine_id']}: ISRU {row['isru_percent']:.1f}% "
            f"(in-situ {row['in_situ_kg']:.2f} kg, imported {row['imported_kg']:.2f} kg)"
        )

    if missing:
        print("\nMachines missing provenance:")
        for machine_id in missing:
            print(f"- {machine_id}")

    if imported_rows:
        label = "Imported machines" if not args.all_imports else "Imported items"
        print(f"\n{label}:")
        for row in imported_rows[:50]:
            print(
                f"- {row['item_id']}: {row['imported_kg']:.2f} kg "
                f"({row['imported_percent']:.1f}%)"
            )
        if len(imported_rows) > 50:
            print(f"- ... and {len(imported_rows) - 50} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
