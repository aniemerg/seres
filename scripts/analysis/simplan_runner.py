#!/usr/bin/env python3
"""
Execute a SimPlan directly with SimulationEngine.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine
from src.simulation_parallel.intent_queue import DeferredIntentQueue
from src.simulation_parallel.runner import ConcurrentDESRunner
from src.simulation_parallel.session import Sim2Session


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


 


def _order_recipes(plan: SimPlan, kb: KBLoader) -> List[str]:
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
    plan: SimPlan,
    kb_root: Path,
    sim_root: Path,
    reset: bool = False,
    dry_run: bool = False,
    trace: bool = False,
    engine_mode: str = "sim",
    strategy: str = "sequential",
    max_no_progress: int = 1000,
    progress_every_steps: int = 1000,
    snapshot_interval_hours: Optional[float] = None,
    recipe_retry_delay_hours: Optional[float] = None,
) -> Dict[str, Any]:
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_dir = sim_root / plan.sim_id
    if reset and sim_dir.exists():
        shutil.rmtree(sim_dir)

    engine = SimulationEngine(plan.sim_id, kb, sim_dir)
    if sim_dir.exists() and (sim_dir / "snapshot.json").exists():
        engine.load()
    if engine_mode == "sim2":
        interval = 50.0 if snapshot_interval_hours is None else float(snapshot_interval_hours)
        engine.state_snapshot_interval_hours = max(0.0, interval)
        retry_delay = 24.0 if recipe_retry_delay_hours is None else float(recipe_retry_delay_hours)
        engine.RECIPE_RETRY_DELAY_HOURS = max(0.1, retry_delay)
    sim2_session: Optional[Sim2Session] = None
    sim2_runner: Optional[ConcurrentDESRunner] = None
    if engine_mode == "sim2":
        queue_file = sim_dir / "deferred_intents.json"
        if queue_file.exists():
            queue_data = json.loads(queue_file.read_text(encoding="utf-8"))
            queue = DeferredIntentQueue.from_dict(queue_data)
        else:
            queue = DeferredIntentQueue()
        sim2_session = Sim2Session(engine=engine, queue=queue, queue_file=queue_file)
        sim2_runner = ConcurrentDESRunner(sim2_session)

    if not dry_run:
        engine.log_annotation(
            key="scenario.id",
            value=plan.sim_id,
            tags=["scenario", "simplan"],
            source="simplan_runner",
        )
        engine.log_annotation(
            key="scenario.goal_target",
            value=plan.target_machine_id,
            tags=["scenario", "target"],
            source="simplan_runner",
        )
        engine.log_annotation(
            key="scenario.plan_type",
            value="simplan_combined",
            tags=["scenario", "plan"],
            source="simplan_runner",
        )
        engine.log_marker(
            name="simplan_start",
            tags=["milestone", "simplan", "phase"],
            source="simplan_runner",
            metadata={
                "imports_count": len(plan.imports),
                "recipes_count": len(plan.recipes),
                "build_machine": bool(plan.build_machine),
                "target_recipe_id": plan.target_recipe_id,
            },
        )

    def _trace(msg: str) -> None:
        if trace:
            print(msg)

    def _get_item_unit(item_id: str) -> str:
        model = kb.get_item(item_id)
        if not model:
            return "unit"
        item_dict = model.model_dump() if hasattr(model, "model_dump") else model
        return item_dict.get("unit") or "unit"

    def _current_quantity_in_unit(item_id: str, unit: str) -> float:
        inv = engine.state.inventory.get(item_id)
        if not inv:
            return 0.0
        if inv.unit == unit:
            return float(inv.quantity)
        converted = engine.converter.convert(float(inv.quantity), inv.unit, unit, item_id)
        return float(converted) if converted is not None else 0.0

    def _verify_target_output() -> Optional[str]:
        unit = _get_item_unit(plan.target_machine_id)
        if engine.has_item(plan.target_machine_id, 1.0, unit):
            return None
        inv_item = engine.state.inventory.get(plan.target_machine_id)
        if inv_item and getattr(inv_item, "quantity", 0) > 0:
            return None
        return f"Target output not found in inventory: {plan.target_machine_id}"

    _trace(
        f"PLAN target={plan.target_machine_id} "
        f"recipe={plan.target_recipe_id or 'none'} "
        f"build_machine={plan.build_machine} "
        f"imports={len(plan.imports)} "
        f"recipes={len(plan.recipes)}"
    )

    # Notes (no-op for engine; printed only if dry_run)
    if dry_run or trace:
        for note in plan.notes:
            print(f"NOTE [{note.style}]: {note.message}")

    # Imports
    for item_id, imp in sorted(plan.imports.items()):
        if dry_run:
            print(f"IMPORT {item_id} {imp.qty} {imp.unit} ({imp.reason or ''})")
            continue
        current_qty = _current_quantity_in_unit(item_id, imp.unit)
        needed_qty = max(0.0, float(imp.qty) - current_qty)
        if needed_qty <= 0.0:
            continue
        _trace(f"IMPORT {item_id} {needed_qty} {imp.unit} (target={imp.qty})")
        result = engine.import_item(item_id, needed_qty, imp.unit)
        if not result.get("success"):
            if not dry_run:
                engine.log_annotation(
                    key="scenario.status",
                    value="failed",
                    tags=["scenario", "status", "error"],
                    source="simplan_runner",
                )
                engine.log_marker(
                    name="simplan_failed_import",
                    tags=["milestone", "error", "imports"],
                    source="simplan_runner",
                    metadata={"item_id": item_id},
                )
                engine.save()
            return {"success": False, "error": "import_failed", "detail": result}

    if not dry_run:
        engine.log_marker(
            name="imports_complete",
            tags=["milestone", "imports", "phase"],
            source="simplan_runner",
        )

    def _advance_with_sim2(active_recipe_id: Optional[str] = None) -> Optional[str]:
        if sim2_runner is None:
            return "sim2 runner is not initialized"

        def _progress(update: Dict[str, Any]) -> None:
            prefix = "SIM2_TRACE" if trace else "SIM2_PROGRESS"
            print(
                f"{prefix} "
                f"step={update.get('step')} "
                f"time={update.get('time')} "
                f"queued_events={update.get('queued_events')} "
                f"active_processes={update.get('active_processes')} "
                f"completed_processes={update.get('completed_processes')} "
                f"deferred_intents={update.get('deferred_intents')} "
                f"promoted={update.get('promoted')}"
            )

        result = sim2_runner.run_to_completion_with_progress(
            max_no_progress=max_no_progress,
            progress_callback=_progress,
            progress_every_steps=progress_every_steps,
        )
        if result.get("status") == "completed":
            return None

        blocked_recipes = result.get("blocked_recipes") or []
        if active_recipe_id and blocked_recipes:
            for row in blocked_recipes:
                if row.get("recipe_id") == active_recipe_id:
                    issues = row.get("issues") or []
                    if issues:
                        return f"blocked recipe {active_recipe_id}: {issues[0]}"
        if blocked_recipes:
            for row in blocked_recipes:
                issues = row.get("issues") or []
                active_steps = row.get("active_steps") or []
                scheduled_steps = row.get("scheduled_steps") or []
                if not issues:
                    continue
                # "no_ready_steps" is informational when upstream steps are active/scheduled.
                if issues[0] == "no_ready_steps" and (active_steps or scheduled_steps):
                    continue
                return f"blocked recipe {row.get('recipe_id')}: {issues[0]}"

        return (
            f"sim2 blocked ({result.get('reason', 'unknown')}), "
            f"queued_events={result.get('summary', {}).get('queued_events')}, "
            f"active_processes={result.get('summary', {}).get('active_processes')}, "
            f"deferred_intents={result.get('summary', {}).get('deferred_intents')}"
        )

    def _run_recipe_and_advance(recipe_id: str, quantity: int) -> Dict[str, Any]:
        result = engine.run_recipe(recipe_id, quantity)
        if not result.get("success"):
            return result
        if engine_mode == "sim2":
            err = _advance_with_sim2(active_recipe_id=recipe_id)
        else:
            err = _advance_until_idle(engine)
        if err:
            return {"success": False, "error": "advance_failed", "message": err}
        return {"success": True}

    def _run_upfront_and_advance(recipe_batch: List[tuple[str, int]]) -> Optional[str]:
        for recipe_id, quantity in recipe_batch:
            result = engine.run_recipe(recipe_id, quantity)
            if not result.get("success"):
                return f"recipe_failed:{recipe_id}:{result.get('message')}"
        if engine_mode == "sim2":
            return _advance_with_sim2(active_recipe_id=None)
        return _advance_until_idle(engine)

    # Recipes (non-target first, dependency-ordered)
    recipe_order = _order_recipes(plan, kb)
    recipe_map = {r.recipe_id: r for r in plan.recipes}
    if strategy == "upfront":
        upfront_batch: List[tuple[str, int]] = []
        for rid in recipe_order:
            recipe = recipe_map[rid]
            if dry_run:
                print(f"RUN_RECIPE {recipe.recipe_id} x{recipe.quantity} ({recipe.reason or ''})")
                continue
            _trace(f"RUN_RECIPE {recipe.recipe_id} x{recipe.quantity}")
            upfront_batch.append((recipe.recipe_id, recipe.quantity))
        if dry_run:
            print("ADVANCE_UNTIL_IDLE")
        else:
            error = _run_upfront_and_advance(upfront_batch)
            if error:
                if not dry_run:
                    engine.log_annotation(
                        key="scenario.status",
                        value="failed",
                        tags=["scenario", "status", "error"],
                        source="simplan_runner",
                    )
                    engine.log_marker(
                        name="simplan_failed_advance",
                        tags=["milestone", "error", "recipes"],
                        source="simplan_runner",
                        metadata={"strategy": "upfront"},
                    )
                    if sim2_session:
                        sim2_session.save()
                    else:
                        engine.save()
                return {
                    "success": False,
                    "error": "advance_failed",
                    "detail": error,
                }
            for rid in recipe_order:
                _trace(f"RECIPE_DONE {rid}")
    else:
        for rid in recipe_order:
            recipe = recipe_map[rid]
            if dry_run:
                print(f"RUN_RECIPE {recipe.recipe_id} x{recipe.quantity} ({recipe.reason or ''})")
                print("ADVANCE_UNTIL_IDLE")
                continue
            _trace(f"RUN_RECIPE {recipe.recipe_id} x{recipe.quantity}")
            result = _run_recipe_and_advance(recipe.recipe_id, recipe.quantity)
            if not result.get("success"):
                if not dry_run:
                    engine.log_annotation(
                        key="scenario.status",
                        value="failed",
                        tags=["scenario", "status", "error"],
                        source="simplan_runner",
                    )
                    engine.log_marker(
                        name="simplan_failed_recipe",
                        tags=["milestone", "error", "recipes"],
                        source="simplan_runner",
                        metadata={"recipe_id": recipe.recipe_id},
                    )
                    if sim2_session:
                        sim2_session.save()
                    else:
                        engine.save()
                return {
                    "success": False,
                    "error": result.get("error", "recipe_failed"),
                    "recipe_id": recipe.recipe_id,
                    "detail": result,
                }
            _trace(f"RECIPE_DONE {recipe.recipe_id}")

    if not dry_run:
        engine.log_marker(
            name="recipes_complete",
            tags=["milestone", "recipes", "phase"],
            source="simplan_runner",
        )

    # Target recipe last (if present)
    if plan.target_recipe_id:
        if dry_run:
            print(f"RUN_RECIPE {plan.target_recipe_id} x1 (target_recipe)")
            print("ADVANCE_UNTIL_IDLE")
        else:
            _trace(f"RUN_TARGET_RECIPE {plan.target_recipe_id} x1")
            result = _run_recipe_and_advance(plan.target_recipe_id, 1)
            if not result.get("success"):
                engine.log_annotation(
                    key="scenario.status",
                    value="failed",
                    tags=["scenario", "status", "error"],
                    source="simplan_runner",
                )
                engine.log_marker(
                    name="simplan_failed_target_recipe",
                    tags=["milestone", "error", "target"],
                    source="simplan_runner",
                    metadata={"recipe_id": plan.target_recipe_id},
                )
                engine.save()
                return {
                    "success": False,
                    "error": "recipe_failed",
                    "recipe_id": plan.target_recipe_id,
                    "detail": result,
                }
            _trace(f"TARGET_RECIPE_DONE {plan.target_recipe_id}")
            engine.log_marker(
                name="target_recipe_complete",
                tags=["milestone", "target", "phase"],
                source="simplan_runner",
                metadata={"recipe_id": plan.target_recipe_id},
            )

    # Build machine
    if plan.build_machine:
        if dry_run:
            print(f"BUILD_MACHINE {plan.target_machine_id}")
        else:
            _trace(f"BUILD_MACHINE {plan.target_machine_id}")
            result = engine.build_machine(plan.target_machine_id)
            if not result.get("success"):
                engine.log_annotation(
                    key="scenario.status",
                    value="failed",
                    tags=["scenario", "status", "error"],
                    source="simplan_runner",
                )
                engine.log_marker(
                    name="simplan_failed_build",
                    tags=["milestone", "error", "build"],
                    source="simplan_runner",
                    metadata={"machine_id": plan.target_machine_id},
                )
                engine.save()
                return {"success": False, "error": "build_failed", "detail": result}
            _trace(f"BUILD_DONE {plan.target_machine_id}")
            engine.log_marker(
                name="target_build_complete",
                tags=["milestone", "target", "build"],
                source="simplan_runner",
                metadata={"machine_id": plan.target_machine_id},
            )

    if not dry_run and (plan.target_recipe_id or plan.build_machine):
        verify_error = _verify_target_output()
        if verify_error:
            engine.log_annotation(
                key="scenario.status",
                value="failed",
                tags=["scenario", "status", "error"],
                source="simplan_runner",
            )
            engine.log_marker(
                name="simplan_missing_target_output",
                tags=["milestone", "error", "target"],
                source="simplan_runner",
                metadata={"target_machine_id": plan.target_machine_id},
            )
            engine.save()
            return {"success": False, "error": "missing_target_output", "detail": verify_error}

    if not dry_run:
        engine.log_annotation(
            key="scenario.status",
            value="complete",
            tags=["scenario", "status"],
            source="simplan_runner",
        )
        engine.log_marker(
            name="simplan_complete",
            tags=["milestone", "simplan", "complete"],
            source="simplan_runner",
        )
        if sim2_session:
            sim2_session.save()
        else:
            engine.save()
        isru = _get_item_isru(engine, plan.target_machine_id)
        return {"success": True, "isru": isru}

    return {"success": True, "dry_run": True}


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute a SimPlan.")
    parser.add_argument("--plan", required=True, help="Path to plan JSON")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--reset", action="store_true", help="Delete existing sim directory first")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without executing")
    parser.add_argument("--trace", action="store_true", help="Print step-by-step execution trace")
    parser.add_argument("--engine", choices=["sim", "sim2"], default="sim", help="Execution engine mode")
    parser.add_argument("--strategy", choices=["sequential", "upfront"], default="sequential", help="Recipe submission strategy")
    parser.add_argument("--max-no-progress", type=int, default=1000, help="No-progress guard for sim2 advancement")
    parser.add_argument("--progress-every-steps", type=int, default=1000, help="Progress print cadence for sim2 (trace mode)")
    parser.add_argument(
        "--snapshot-interval-hours",
        type=float,
        default=None,
        help="State snapshot cadence in hours (sim2 mode; default 50h, 0=every step)",
    )
    parser.add_argument(
        "--recipe-retry-delay-hours",
        type=float,
        default=None,
        help="Blocked recipe retry delay in hours (sim2 mode; default 24h)",
    )
    args = parser.parse_args()

    plan_path = Path(args.plan)
    plan = SimPlan.load(plan_path)

    if args.dry_run:
        print("Dry run plan actions:")

    result = execute_plan(
        plan=plan,
        kb_root=Path(args.kb_root),
        sim_root=Path(args.sim_root),
        reset=args.reset,
        dry_run=args.dry_run,
        trace=args.trace,
        engine_mode=args.engine,
        strategy=args.strategy,
        max_no_progress=args.max_no_progress,
        progress_every_steps=args.progress_every_steps,
        snapshot_interval_hours=args.snapshot_interval_hours,
        recipe_retry_delay_hours=args.recipe_retry_delay_hours,
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
