#!/usr/bin/env python3
"""
ISRU assumption probe:
- Static closure analysis for a target machine
- Imported-item breakdown (static KB)
- Optional comparison to an existing simulation's provenance snapshot

This avoids running simulations and focuses on quick reality checks.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

from src.kb_core.kb_loader import KBLoader
from src.indexer.closure_analysis import ClosureAnalyzer
from src.simulation.engine import SimulationEngine


REPO_ROOT = Path(__file__).resolve().parents[2]
KB_ROOT = REPO_ROOT / "kb"
SIM_ROOT = REPO_ROOT / "simulations"


def _model_to_dict(obj: Any) -> Dict[str, Any]:
    if obj is None:
        return {}
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if hasattr(obj, "dict"):
        return obj.dict()
    return {}


def _is_recipe_import_stub(recipe_id: Optional[str]) -> bool:
    if not recipe_id:
        return False
    if recipe_id.startswith("recipe_import_placeholder_"):
        return True
    if "import_placeholder_v0" in recipe_id.lower():
        return True
    return False


def _load_kb(kb_root: Path) -> KBLoader:
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    return kb


def _summarize_machine(result: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "machine_id": result.get("machine_id"),
        "machine_name": result.get("machine_name"),
        "total_mass_kg": result.get("total_mass", 0.0),
        "isru_percent": result.get("isru_percent", 0.0),
        "imported_percent": result.get("imported_percent", 0.0),
        "unresolved_percent": result.get("unresolved_percent", 0.0),
    }


def _imported_breakdown(
    kb: KBLoader,
    analyzer: ClosureAnalyzer,
    imported_items: Dict[str, Dict[str, Any]],
    top_n: int,
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for item_id, data in imported_items.items():
        item_model = kb.get_item(item_id)
        item = _model_to_dict(item_model)
        recipe_id = item.get("recipe")
        rows.append({
            "item_id": item_id,
            "mass_kg": data.get("mass_kg", 0.0),
            "qty": data.get("qty", 0.0),
            "unit": data.get("unit", "count"),
            "kind": item.get("kind"),
            "is_import": analyzer._is_imported(item_id, item) if item else True,
            "has_recipe": bool(recipe_id),
            "recipe_id": recipe_id,
            "recipe_is_import_stub": _is_recipe_import_stub(recipe_id),
        })

    rows.sort(key=lambda r: r["mass_kg"], reverse=True)
    if top_n > 0:
        rows = rows[:top_n]
    return rows


def _load_sim_provenance(sim_id: str, item_id: Optional[str], kb: KBLoader) -> Dict[str, Any]:
    sim_dir = SIM_ROOT / sim_id
    snapshot = sim_dir / "snapshot.json"
    if not snapshot.exists():
        return {"error": f"simulation '{sim_id}' not found at {sim_dir}"}

    engine = SimulationEngine(sim_id, kb, sim_dir)
    if not engine.load():
        return {"error": f"failed to load simulation '{sim_id}'"}

    prov = engine.state.provenance
    if not prov:
        return {"error": f"no provenance data in simulation '{sim_id}'"}

    if item_id:
        item_prov = prov.get(item_id)
        if not item_prov:
            return {"error": f"item '{item_id}' not found in provenance data"}
        total = item_prov.in_situ_kg + item_prov.imported_kg + item_prov.unknown_kg
        isru_pct = (item_prov.in_situ_kg / total * 100.0) if total > 0 else 0.0
        return {
            "item_id": item_id,
            "total_kg": total,
            "in_situ_kg": item_prov.in_situ_kg,
            "imported_kg": item_prov.imported_kg,
            "unknown_kg": item_prov.unknown_kg,
            "isru_percent": isru_pct,
        }

    totals = {"in_situ_kg": 0.0, "imported_kg": 0.0, "unknown_kg": 0.0}
    for item_prov in prov.values():
        totals["in_situ_kg"] += item_prov.in_situ_kg
        totals["imported_kg"] += item_prov.imported_kg
        totals["unknown_kg"] += item_prov.unknown_kg
    total = totals["in_situ_kg"] + totals["imported_kg"] + totals["unknown_kg"]
    totals["total_kg"] = total
    totals["isru_percent"] = (totals["in_situ_kg"] / total * 100.0) if total > 0 else 0.0
    return totals


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Probe ISRU assumptions without running simulations."
    )
    parser.add_argument("--machine-id", required=True, help="Target machine item id")
    parser.add_argument("--kb-root", default=str(KB_ROOT), help="KB root directory")
    parser.add_argument("--top-imports", type=int, default=15, help="Top imported items to show")
    parser.add_argument("--sim-id", help="Optional simulation id to compare provenance")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    kb_root = Path(args.kb_root)
    kb = _load_kb(kb_root)
    analyzer = ClosureAnalyzer(kb)

    result = analyzer.analyze_machine(args.machine_id)
    summary = _summarize_machine(result)
    imported_rows = _imported_breakdown(kb, analyzer, result.get("imported_items", {}), args.top_imports)

    output: Dict[str, Any] = {
        "summary": summary,
        "imported_items_top": imported_rows,
        "errors": result.get("errors", []),
    }

    if args.sim_id:
        output["simulation_provenance"] = _load_sim_provenance(args.sim_id, args.machine_id, kb)

    if args.json:
        print(json.dumps(output, indent=2))
        return 0

    # Human-readable output
    print("ISRU Assumption Probe")
    print(f"Machine: {summary['machine_id']} ({summary.get('machine_name')})")
    print(
        f"Static closure ISRU: {summary['isru_percent']:.1f}% "
        f"(imported {summary['imported_percent']:.1f}%, unresolved {summary['unresolved_percent']:.1f}%)"
    )
    print(f"Total mass (KB): {summary['total_mass_kg']:.2f} kg")

    if output["errors"]:
        print("\nClosure analysis errors:")
        for err in output["errors"][:10]:
            print(f"- {err}")
        if len(output["errors"]) > 10:
            print(f"- ... and {len(output['errors']) - 10} more")

    print("\nTop imported items (static KB):")
    for row in imported_rows:
        recipe_note = ""
        if row["has_recipe"]:
            recipe_note = "import_stub" if row["recipe_is_import_stub"] else "has_recipe"
        else:
            recipe_note = "no_recipe"
        print(
            f"- {row['item_id']}: {row['mass_kg']:.2f} kg "
            f"({row['qty']} {row['unit']}) "
            f"[{row['kind'] or 'unknown'}; {recipe_note}]"
        )

    if args.sim_id:
        print(f"\nSimulation provenance ({args.sim_id}):")
        prov = output["simulation_provenance"]
        if "error" in prov:
            print(f"- {prov['error']}")
        else:
            print(
                f"- ISRU {prov['isru_percent']:.1f}% "
                f"(in-situ {prov['in_situ_kg']:.2f} kg, imported {prov['imported_kg']:.2f} kg)"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
