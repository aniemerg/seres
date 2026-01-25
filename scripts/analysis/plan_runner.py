#!/usr/bin/env python3
"""
Execute a RunbookPlan directly with SimulationEngine.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.runbook_plan import RunbookPlan
from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


def _advance_until_idle(engine: SimulationEngine) -> Optional[str]:
    while engine.scheduler.event_queue:
        next_event = engine.scheduler.event_queue.peek()
        if not next_event:
            break
        delta = next_event.time - engine.scheduler.current_time
        if delta <= 0:
            # Guard against zero/negative jumps
            delta = 0.0
        try:
            engine.advance_time(delta)
        except Exception as exc:
            return str(exc)
    return None


def _get_item_isru(engine: SimulationEngine, item_id: str) -> Dict[str, Any]:
    prov = engine.state.provenance.get(item_id)
    if not prov:
        return {"item_id": item_id, "error": "no_provenance"}
    total = prov.in_situ_kg + prov.imported_kg + prov.unknown_kg
    isru_pct = (prov.in_situ_kg / total * 100.0) if total > 0 else 0.0
    return {
        "item_id": item_id,
        "total_kg": total,
        "in_situ_kg": prov.in_situ_kg,
        "imported_kg": prov.imported_kg,
        "unknown_kg": prov.unknown_kg,
        "isru_percent": isru_pct,
    }


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


def _get_recipe_inputs(recipe: Dict[str, Any]) -> List[Dict[str, Any]]:
    inputs = recipe.get("inputs") or []
    if inputs:
        return inputs
    merged = []
    for step in recipe.get("steps", []) or []:
        for entry in step.get("inputs", []) or []:
            merged.append(entry)
    return merged


def _get_recipe_outputs(recipe: Dict[str, Any]) -> Set[str]:
    outputs = set()
    for entry in recipe.get("outputs") or []:
        item_id = entry.get("item_id")
        if item_id:
            outputs.add(item_id)
    target = recipe.get("target_item_id")
    if target:
        outputs.add(target)
    if outputs:
        return outputs
    for step in recipe.get("steps", []) or []:
        for entry in step.get("outputs", []) or []:
            item_id = entry.get("item_id")
            if item_id:
                outputs.add(item_id)
    return outputs


def _order_recipes(plan: RunbookPlan, kb: KBLoader) -> List[str]:
    recipe_ids = [r.recipe_id for r in plan.recipes]
    if not recipe_ids:
        return []

    recipe_defs: Dict[str, Dict[str, Any]] = {}
    outputs_by_recipe: Dict[str, Set[str]] = {}
    inputs_by_recipe: Dict[str, Set[str]] = {}

    for rid in recipe_ids:
        model = kb.get_recipe(rid)
        recipe = _model_to_dict(model)
        if not recipe:
            continue
        recipe_defs[rid] = recipe
        outputs_by_recipe[rid] = _get_recipe_outputs(recipe)
        inputs = set()
        for entry in _get_recipe_inputs(recipe):
            item_id = entry.get("item_id")
            if item_id:
                inputs.add(item_id)
        inputs_by_recipe[rid] = inputs

    # Build dependency graph: producer -> consumer
    edges: Dict[str, Set[str]] = {rid: set() for rid in recipe_ids}
    indegree: Dict[str, int] = {rid: 0 for rid in recipe_ids}

    for consumer_id in recipe_ids:
        consumer_inputs = inputs_by_recipe.get(consumer_id, set())
        for producer_id in recipe_ids:
            if producer_id == consumer_id:
                continue
            producer_outputs = outputs_by_recipe.get(producer_id, set())
            if producer_outputs & consumer_inputs:
                if consumer_id not in edges[producer_id]:
                    edges[producer_id].add(consumer_id)
                    indegree[consumer_id] += 1

    # Kahn's algorithm with stable order
    queue = [rid for rid in recipe_ids if indegree.get(rid, 0) == 0]
    ordered: List[str] = []
    seen = set()
    while queue:
        rid = queue.pop(0)
        if rid in seen:
            continue
        seen.add(rid)
        ordered.append(rid)
        for child in sorted(edges.get(rid, [])):
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)

    # If cycle or missing defs, fall back to original order for remaining
    if len(ordered) < len(recipe_ids):
        remaining = [rid for rid in recipe_ids if rid not in ordered]
        ordered.extend(remaining)

    return ordered


def execute_plan(
    plan: RunbookPlan,
    kb_root: Path,
    sim_root: Path,
    reset: bool = False,
    dry_run: bool = False,
) -> Dict[str, Any]:
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_dir = sim_root / plan.sim_id
    if reset and sim_dir.exists():
        shutil.rmtree(sim_dir)

    engine = SimulationEngine(plan.sim_id, kb, sim_dir)
    if sim_dir.exists() and (sim_dir / "snapshot.json").exists():
        engine.load()

    # Notes (no-op for engine; printed only if dry_run)
    if dry_run:
        for note in plan.notes:
            print(f"NOTE [{note.style}]: {note.message}")

    # Imports
    for item_id, imp in sorted(plan.imports.items()):
        if dry_run:
            print(f"IMPORT {item_id} {imp.qty} {imp.unit} ({imp.reason or ''})")
            continue
        if engine.has_item(item_id, imp.qty, imp.unit):
            continue
        result = engine.import_item(item_id, imp.qty, imp.unit)
        if not result.get("success"):
            return {"success": False, "error": "import_failed", "detail": result}

    # Recipes (non-target first, dependency-ordered)
    recipe_order = _order_recipes(plan, kb)
    recipe_map = {r.recipe_id: r for r in plan.recipes}
    for rid in recipe_order:
        recipe = recipe_map[rid]
        if dry_run:
            print(f"RUN_RECIPE {recipe.recipe_id} x{recipe.quantity} ({recipe.reason or ''})")
            print("ADVANCE_UNTIL_IDLE")
            continue
        result = engine.run_recipe(recipe.recipe_id, recipe.quantity)
        if not result.get("success"):
            return {
                "success": False,
                "error": "recipe_failed",
                "recipe_id": recipe.recipe_id,
                "detail": result,
            }
        error = _advance_until_idle(engine)
        if error:
            return {
                "success": False,
                "error": "advance_failed",
                "recipe_id": recipe.recipe_id,
                "detail": error,
            }

    # Target recipe last (if present)
    if plan.target_recipe_id:
        if dry_run:
            print(f"RUN_RECIPE {plan.target_recipe_id} x1 (target_recipe)")
            print("ADVANCE_UNTIL_IDLE")
        else:
            result = engine.run_recipe(plan.target_recipe_id, 1)
            if not result.get("success"):
                return {
                    "success": False,
                    "error": "recipe_failed",
                    "recipe_id": plan.target_recipe_id,
                    "detail": result,
                }
            error = _advance_until_idle(engine)
            if error:
                return {
                    "success": False,
                    "error": "advance_failed",
                    "recipe_id": plan.target_recipe_id,
                    "detail": error,
                }

    # Build machine
    if plan.build_machine:
        if dry_run:
            print(f"BUILD_MACHINE {plan.target_machine_id}")
        else:
            result = engine.build_machine(plan.target_machine_id)
            if not result.get("success"):
                return {"success": False, "error": "build_failed", "detail": result}

    if not dry_run:
        engine.save()
        isru = _get_item_isru(engine, plan.target_machine_id)
        return {"success": True, "isru": isru}

    return {"success": True, "dry_run": True}


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute a RunbookPlan.")
    parser.add_argument("--plan", required=True, help="Path to plan JSON")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--reset", action="store_true", help="Delete existing sim directory first")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without executing")
    args = parser.parse_args()

    plan_path = Path(args.plan)
    plan = RunbookPlan.load(plan_path)

    if args.dry_run:
        print("Dry run plan actions:")

    result = execute_plan(
        plan=plan,
        kb_root=Path(args.kb_root),
        sim_root=Path(args.sim_root),
        reset=args.reset,
        dry_run=args.dry_run,
    )

    if not result.get("success"):
        print(f"Plan failed: {result}", file=sys.stderr)
        return 1

    if not args.dry_run:
        isru = result.get("isru", {})
        if "error" in isru:
            print(f"ISRU: no provenance data for {plan.target_machine_id}")
        else:
            print(
                f"ISRU for {plan.target_machine_id}: "
                f"{isru['isru_percent']:.1f}% "
                f"(in-situ {isru['in_situ_kg']:.2f} kg, imported {isru['imported_kg']:.2f} kg)"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
