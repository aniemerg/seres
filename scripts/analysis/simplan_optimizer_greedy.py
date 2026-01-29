#!/usr/bin/env python3
"""
Greedy optimizer: expand imported items into local recipes to improve ISRU.
"""
from __future__ import annotations

import argparse
import copy
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_runner import execute_plan
from src.kb_core.kb_loader import KBLoader
from src.kb_core.unit_converter import UnitConverter
from src.indexer.closure_analysis import ClosureAnalyzer


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


def _is_import_item(item_id: str, item: Dict[str, Any]) -> bool:
    if item.get("is_import", False):
        return True
    if item_id.startswith("import_"):
        return True
    if "_imported" in item_id.lower():
        return True
    recipe_id = item.get("recipe")
    if recipe_id and _is_recipe_import_stub(recipe_id):
        return True
    return False


def _can_expand_item(
    item_id: str,
    kb: KBLoader,
    allow_machine_build: bool,
) -> bool:
    item_model = kb.get_item(item_id)
    item = _model_to_dict(item_model)
    if not item:
        return False
    if _is_import_item(item_id, item):
        return False
    if item.get("kind") == "machine" and not allow_machine_build:
        return False
    recipe_id = item.get("recipe")
    if not recipe_id or _is_recipe_import_stub(recipe_id):
        return False
    recipe_model = kb.get_recipe(recipe_id)
    if not recipe_model:
        return False
    return True


def _get_recipe_inputs(recipe: Dict[str, Any]) -> List[Dict[str, Any]]:
    inputs = recipe.get("inputs") or []
    if inputs:
        return inputs
    # fallback to step inputs
    for step in recipe.get("steps", []) or []:
        for entry in step.get("inputs", []) or []:
            inputs.append(entry)
    return inputs


def _get_recipe_outputs(recipe: Dict[str, Any]) -> List[Dict[str, Any]]:
    outputs = recipe.get("outputs") or []
    if outputs:
        return outputs
    for step in recipe.get("steps", []) or []:
        for entry in step.get("outputs", []) or []:
            outputs.append(entry)
    return outputs


def _compute_recipe_runs(
    item_id: str,
    qty: float,
    unit: str,
    recipe: Dict[str, Any],
    converter: UnitConverter,
) -> int:
    outputs = _get_recipe_outputs(recipe)
    for outp in outputs:
        out_id = outp.get("item_id")
        out_qty = outp.get("qty") or outp.get("quantity") or 0.0
        out_unit = outp.get("unit", unit)
        if out_id != item_id or out_qty <= 0:
            continue
        # Convert requested qty into output unit if needed
        req_qty = qty
        if unit != out_unit:
            converted = converter.convert(qty, unit, out_unit, item_id)
            if converted is not None:
                req_qty = converted
        return max(1, int(math.ceil(req_qty / out_qty)))
    return 1


def _normalize_plan_quantities(
    plan: SimPlan,
    kb: KBLoader,
    converter: UnitConverter,
) -> None:
    """
    Recompute recipe run counts based on total downstream demand from target recipe.
    Only recipes already present in the plan are considered for local production.
    """
    if not plan.target_recipe_id:
        return

    # Map output item -> recipe_id (for recipes already in plan)
    output_to_recipe: Dict[str, str] = {}
    for entry in plan.recipes:
        recipe_model = kb.get_recipe(entry.recipe_id)
        recipe = _model_to_dict(recipe_model)
        if not recipe:
            continue
        target = recipe.get("target_item_id")
        if target:
            output_to_recipe[target] = entry.recipe_id

    recipe_demands: Dict[str, int] = {}

    def demand_item(item_id: str, qty: float, unit: str) -> None:
        recipe_id = output_to_recipe.get(item_id)
        if not recipe_id:
            # Ensure imports cover demand
            existing = plan.imports.get(item_id)
            if existing:
                if existing.unit == unit:
                    if existing.qty < qty:
                        existing.qty = qty
                else:
                    # Leave as-is if unit mismatch
                    pass
            else:
                plan.add_import(item_id, qty, unit, reason="demand_normalize")
            return

        recipe_model = kb.get_recipe(recipe_id)
        recipe = _model_to_dict(recipe_model)
        runs = _compute_recipe_runs(item_id, qty, unit, recipe, converter)
        recipe_demands[recipe_id] = recipe_demands.get(recipe_id, 0) + runs

        for entry in _get_recipe_inputs(recipe):
            in_id = entry.get("item_id")
            in_qty = entry.get("qty") or entry.get("quantity") or 0.0
            in_unit = entry.get("unit", "kg")
            if not in_id or in_qty <= 0:
                continue
            demand_item(in_id, float(in_qty) * runs, in_unit)

    # Seed demand from target recipe inputs
    target_model = kb.get_recipe(plan.target_recipe_id)
    target_recipe = _model_to_dict(target_model)
    for entry in _get_recipe_inputs(target_recipe):
        in_id = entry.get("item_id")
        in_qty = entry.get("qty") or entry.get("quantity") or 0.0
        in_unit = entry.get("unit", "kg")
        if not in_id or in_qty <= 0:
            continue
        demand_item(in_id, float(in_qty), in_unit)

    # Apply recomputed recipe run counts and prune unused recipes
    new_recipes = []
    for entry in plan.recipes:
        if entry.recipe_id not in recipe_demands:
            continue
        entry.quantity = recipe_demands[entry.recipe_id]
        new_recipes.append(entry)
    plan.recipes = new_recipes

    # Ensure imports cover all inputs for the remaining recipes
    total_inputs: Dict[str, Dict[str, float]] = {}
    for entry in plan.recipes:
        recipe_model = kb.get_recipe(entry.recipe_id)
        recipe = _model_to_dict(recipe_model)
        for inp in _get_recipe_inputs(recipe):
            in_id = inp.get("item_id")
            in_qty = inp.get("qty") or inp.get("quantity") or 0.0
            in_unit = inp.get("unit", "kg")
            if not in_id or in_qty <= 0:
                continue
            required_qty = float(in_qty) * entry.quantity
            slot = total_inputs.setdefault(in_id, {"qty": 0.0, "unit": in_unit})
            # If units differ, keep first unit and add raw qty (best-effort)
            if slot["unit"] == in_unit:
                slot["qty"] += required_qty
            else:
                slot["qty"] += required_qty

    for item_id, req in total_inputs.items():
        if item_id in output_to_recipe:
            continue
        existing = plan.imports.get(item_id)
        if existing and existing.unit == req["unit"]:
            if existing.qty < req["qty"]:
                existing.qty = req["qty"]
        elif not existing:
            plan.add_import(item_id, req["qty"], req["unit"], reason="input_cover")


def _diff_plans(before: SimPlan, after: SimPlan) -> Dict[str, List[str]]:
    before_imports = before.imports
    after_imports = after.imports
    before_recipes = {r.recipe_id: r.quantity for r in before.recipes}
    after_recipes = {r.recipe_id: r.quantity for r in after.recipes}

    added_imports = []
    removed_imports = []
    for item_id, entry in after_imports.items():
        if item_id not in before_imports:
            added_imports.append(f"{item_id} {entry.qty} {entry.unit}")
    for item_id in before_imports:
        if item_id not in after_imports:
            removed_imports.append(item_id)

    added_recipes = []
    removed_recipes = []
    for rid, qty in after_recipes.items():
        if rid not in before_recipes:
            added_recipes.append(f"{rid} x{qty}")
    for rid in before_recipes:
        if rid not in after_recipes:
            removed_recipes.append(rid)

    return {
        "added_imports": sorted(added_imports),
        "removed_imports": sorted(removed_imports),
        "added_recipes": sorted(added_recipes),
        "removed_recipes": sorted(removed_recipes),
    }


def _expand_item(
    plan: SimPlan,
    item_id: str,
    qty: float,
    unit: str,
    kb: KBLoader,
    converter: UnitConverter,
    visited: set,
    allow_machine_build: bool,
    depth: int,
    max_depth: int,
) -> bool:
    if depth > max_depth:
        plan.add_import(item_id, qty, unit, reason="max_depth")
        return False
    if item_id in visited:
        plan.add_import(item_id, qty, unit, reason="cycle")
        return False

    visited = visited | {item_id}
    item_model = kb.get_item(item_id)
    if not item_model:
        plan.add_import(item_id, qty, unit, reason="missing_item")
        return False

    item = _model_to_dict(item_model)
    if _is_import_item(item_id, item):
        plan.add_import(item_id, qty, unit, reason="import_item")
        return False

    if item.get("kind") == "machine" and not allow_machine_build:
        plan.add_import(item_id, qty, unit, reason="machine_import")
        return False

    recipe_id = item.get("recipe")
    if not recipe_id or _is_recipe_import_stub(recipe_id):
        plan.add_import(item_id, qty, unit, reason="no_recipe")
        return False

    recipe_model = kb.get_recipe(recipe_id)
    if not recipe_model:
        plan.add_import(item_id, qty, unit, reason="missing_recipe")
        return False

    recipe = _model_to_dict(recipe_model)
    runs = _compute_recipe_runs(item_id, qty, unit, recipe, converter)

    # Expand inputs first (post-order)
    for entry in _get_recipe_inputs(recipe):
        in_id = entry.get("item_id")
        in_qty = entry.get("qty") or entry.get("quantity") or 0.0
        in_unit = entry.get("unit", "kg")
        if not in_id or in_qty <= 0:
            continue
        _expand_item(
            plan,
            in_id,
            float(in_qty) * runs,
            in_unit,
            kb,
            converter,
            visited,
            allow_machine_build,
            depth + 1,
            max_depth,
        )

    # Ensure machines for process steps
    for step in recipe.get("steps", []) or []:
        process_id = step.get("process_id")
        if not process_id:
            continue
        process_model = kb.get_process(process_id)
        process = _model_to_dict(process_model)
        for req in process.get("resource_requirements", []) or []:
            machine_id = req.get("machine_id")
            m_qty = req.get("qty") or req.get("quantity") or 1
            m_unit = req.get("unit", "count")
            if not machine_id:
                continue
            # For now, import machines (no recursive build)
            plan.add_import(machine_id, float(m_qty), m_unit, reason=f"process:{process_id}")

    plan.remove_import(item_id)
    plan.add_recipe(recipe_id, runs, reason=f"expand:{item_id}")
    return True


def _build_import_only_plan(
    machine_id: str,
    sim_id: str,
    kb: KBLoader,
    allow_bom: bool = False,
) -> SimPlan:
    plan = SimPlan(sim_id=sim_id, target_machine_id=machine_id)
    plan.add_note(f"Import-only plan for {machine_id}")

    machine_model = kb.get_item(machine_id)
    machine = _model_to_dict(machine_model)
    recipe_id = machine.get("recipe")

    if recipe_id:
        recipe_model = kb.get_recipe(recipe_id)
        recipe = _model_to_dict(recipe_model)
        if not recipe:
            raise RuntimeError(f"Recipe '{recipe_id}' not found for {machine_id}")

        for entry in _get_recipe_inputs(recipe):
            in_id = entry.get("item_id")
            in_qty = entry.get("qty") or entry.get("quantity") or 0
            in_unit = entry.get("unit", "kg")
            if in_id and in_qty:
                plan.add_import(in_id, float(in_qty), in_unit, reason="import_only_recipe_input")

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
        return plan
    if not allow_bom:
        raise RuntimeError(
            f"No recipe for machine '{machine_id}'. Add a recipe or pass --allow-bom."
        )

    bom = kb.get_bom(machine_id)
    if not bom:
        raise RuntimeError(f"BOM not found for machine '{machine_id}'")
    components = bom.get("components", [])
    if not components:
        raise RuntimeError(f"BOM for '{machine_id}' has no components")
    for comp in components:
        item_id = comp.get("item_id") or comp.get("id")
        qty = comp.get("qty") or comp.get("quantity") or 1
        unit = comp.get("unit", "count")
        if item_id:
            plan.add_import(item_id, float(qty), unit, reason="import_only_bom")
    return plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Greedy ISRU optimizer.")
    parser.add_argument("--machine-id", required=True, help="Target machine item id")
    parser.add_argument("--sim-id", required=True, help="Base simulation id")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--iterations", type=int, default=5, help="Max greedy iterations")
    parser.add_argument("--max-depth", type=int, default=6, help="Max recursion depth")
    parser.add_argument("--out", help="Output plan path")
    parser.add_argument("--candidate", help="Force expansion of a specific import item")
    parser.add_argument("--verbose", action="store_true", help="Verbose decision logs")
    parser.add_argument(
        "--allow-bom",
        action="store_true",
        help="Allow BOM fallback when no recipe is available (default: error).",
    )
    args = parser.parse_args()

    kb_root = Path(args.kb_root)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    converter = UnitConverter(kb)

    base_plan = _build_import_only_plan(
        args.machine_id, args.sim_id, kb, allow_bom=args.allow_bom
    )
    base_result = execute_plan(
        base_plan, kb_root, Path(args.sim_root), reset=True, dry_run=False
    )
    if not base_result.get("success"):
        print(f"Baseline plan failed: {base_result}", file=sys.stderr)
        return 1

    best_plan = base_plan
    best_isru = base_result.get("isru", {}).get("isru_percent", 0.0)
    print(f"Baseline ISRU: {best_isru:.1f}%")

    improvements = 0
    skipped: set[str] = set()
    rejected: set[str] = set()
    for _ in range(args.iterations):
        # Rebuild candidate list from current plan imports
        candidate_rows: List[Tuple[str, float, float, str]] = []
        for item_id, imp in best_plan.imports.items():
            item_model = kb.get_item(item_id)
            item = _model_to_dict(item_model)
            mass_kg = 0.0
            if imp.unit == "kg":
                mass_kg = imp.qty
            else:
                if item and "mass" in item:
                    if imp.unit in ("count", "unit"):
                        mass_value = item.get("mass")
                        if mass_value is None:
                            mass_value = item.get("mass_kg")
                        if mass_value is None:
                            mass_value = 0.0
                        mass_kg = imp.qty * float(mass_value)
                    else:
                        converted = converter.convert(imp.qty, imp.unit, "kg", item_id)
                        if converted is not None:
                            mass_kg = converted
            candidate_rows.append((item_id, mass_kg, imp.qty, imp.unit))

        candidate_rows.sort(key=lambda row: row[1], reverse=True)

        selected = None
        if args.candidate:
            cand = best_plan.imports.get(args.candidate)
            if not cand:
                print(f"Candidate not in imports: {args.candidate}")
                break
            selected = (args.candidate, cand.qty, cand.unit)
        else:
            for item_id, mass_kg, qty, unit in candidate_rows:
                if item_id in skipped or item_id in rejected:
                    continue
                if item_id not in best_plan.imports:
                    continue
                if not _can_expand_item(item_id, kb, allow_machine_build=False):
                    skipped.add(item_id)
                    continue
                selected = (item_id, qty, unit)
                break

        if not selected:
            break

        item_id, qty, unit = selected
        if args.verbose:
            print(f"Selected candidate: {item_id} {qty} {unit}")
        if improvements >= args.iterations:
            break

        trial_plan = copy.deepcopy(best_plan)
        expanded = _expand_item(
            plan=trial_plan,
            item_id=item_id,
            qty=float(qty),
            unit=unit,
            kb=kb,
            converter=converter,
            visited=set(),
            allow_machine_build=False,
            depth=0,
            max_depth=args.max_depth,
        )
        if not expanded:
            if args.verbose:
                print(f"Expand skipped for {item_id}")
            skipped.add(item_id)
            continue
        _normalize_plan_quantities(trial_plan, kb, converter)

        trial_plan.sim_id = f"{args.sim_id}_opt_{improvements+1}"
        trial_path = REPO_ROOT / "out" / f"plan_{args.machine_id}_trial_{improvements+1}.json"
        trial_plan.save(trial_path)
        if args.verbose:
            diff = _diff_plans(best_plan, trial_plan)
            print("Plan diff:")
            for key in ("added_imports", "removed_imports", "added_recipes", "removed_recipes"):
                if diff[key]:
                    print(f"  {key}: {', '.join(diff[key][:10])}")
                    if len(diff[key]) > 10:
                        print(f"    ... {len(diff[key]) - 10} more")
        result = execute_plan(trial_plan, kb_root, Path(args.sim_root), reset=True, dry_run=False)
        if not result.get("success"):
            print(f"Trial failed for {item_id}: {result}")
            rejected.add(item_id)
            continue
        isru_pct = result.get("isru", {}).get("isru_percent", 0.0)
        print(f"Trial expand {item_id}: ISRU {isru_pct:.1f}%")

        if isru_pct > best_isru:
            best_isru = isru_pct
            best_plan = trial_plan
            improvements += 1
            print(f"Accepted {item_id} -> ISRU {best_isru:.1f}%")
        else:
            print(f"Rejected {item_id} (no improvement)")
            rejected.add(item_id)

    out_path = Path(args.out) if args.out else (REPO_ROOT / "out" / f"plan_{args.machine_id}_optimized.json")
    best_plan.save(out_path)
    print(f"Wrote optimized plan: {out_path}")
    print(f"Final ISRU: {best_isru:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
