#!/usr/bin/env python3
"""
Build an import-only SimPlan for a target machine.
Imports all recipe inputs (or BOM components if no recipe).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from src.kb_core.kb_loader import KBLoader


def _model_to_dict(obj):
    if obj is None:
        return {}
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if hasattr(obj, "dict"):
        return obj.dict()
    return {}


def _get_recipe_inputs(recipe):
    inputs = recipe.get("inputs") or []
    if inputs:
        return inputs
    for step in recipe.get("steps", []) or []:
        for entry in step.get("inputs", []) or []:
            inputs.append(entry)
    return inputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Build import-only plan for a machine.")
    parser.add_argument("--machine-id", required=True, help="Target machine item id")
    parser.add_argument("--sim-id", required=True, help="Simulation id to use")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--out", help="Output plan JSON path")
    parser.add_argument(
        "--allow-bom",
        action="store_true",
        help="Allow BOM fallback when no recipe is available (default: error).",
    )
    args = parser.parse_args()

    kb_root = Path(args.kb_root)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    plan = SimPlan(sim_id=args.sim_id, target_machine_id=args.machine_id)
    plan.add_note(f"Import-only plan for {args.machine_id}")

    machine_model = kb.get_item(args.machine_id)
    machine = _model_to_dict(machine_model)
    recipe_id = machine.get("recipe")

    if recipe_id:
        recipe_model = kb.get_recipe(recipe_id)
        recipe = _model_to_dict(recipe_model)
        if not recipe:
            print(f"Error: recipe '{recipe_id}' not found for {args.machine_id}", file=sys.stderr)
            return 1

        # Import recipe inputs
        for entry in _get_recipe_inputs(recipe):
            item_id = entry.get("item_id")
            qty = entry.get("qty") or entry.get("quantity") or 0
            unit = entry.get("unit", "kg")
            if item_id and qty:
                plan.add_import(item_id, float(qty), unit, reason="import_only_recipe_input")

        # Import machines required by recipe steps
        for step in recipe.get("steps", []) or []:
            process_id = step.get("process_id")
            if not process_id:
                continue
            process_model = kb.get_process(process_id)
            process = _model_to_dict(process_model)
            for req in process.get("resource_requirements", []) or []:
                machine_id = req.get("machine_id")
                qty = req.get("qty") or req.get("quantity") or 1
                unit = req.get("unit", "count")
                if machine_id:
                    plan.add_import(machine_id, float(qty), unit, reason=f"process:{process_id}")

        plan.target_recipe_id = recipe_id
        plan.build_machine = False
    else:
        if not args.allow_bom:
            print(
                f"Error: no recipe for machine '{args.machine_id}'. "
                "Add a recipe or pass --allow-bom to fallback.",
                file=sys.stderr,
            )
            return 1
        bom = kb.get_bom(args.machine_id)
        if not bom:
            print(f"Error: BOM not found for machine '{args.machine_id}'", file=sys.stderr)
            return 1

        components = bom.get("components", [])
        if not components:
            print(f"Error: BOM for '{args.machine_id}' has no components", file=sys.stderr)
            return 1

        for comp in components:
            item_id = comp.get("item_id") or comp.get("id")
            qty = comp.get("qty") or comp.get("quantity") or 1
            unit = comp.get("unit", "count")
            if not item_id:
                continue
            plan.add_import(item_id, float(qty), unit, reason="import_only_bom")

    out_path = Path(args.out) if args.out else (REPO_ROOT / "out" / f"plan_{args.machine_id}_import_only.json")
    plan.save(out_path)
    print(f"Wrote plan: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
