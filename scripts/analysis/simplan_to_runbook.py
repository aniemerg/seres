#!/usr/bin/env python3
"""
Generate a sim-runbook Markdown file from a SimPlan.

Optionally simulate the plan to compute advance-time deltas for each recipe.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_runner import _order_recipes
from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


def _advance_until_idle(engine: SimulationEngine) -> Optional[str]:
    while engine.scheduler.event_queue:
        next_event = engine.scheduler.event_queue.peek()
        if not next_event:
            break
        delta = next_event.time - engine.scheduler.current_time
        if delta <= 0:
            delta = 0.0
        try:
            engine.advance_time(delta)
        except Exception as exc:
            return str(exc)
    return None


def _compute_recipe_durations(
    plan: SimPlan,
    kb_root: Path,
    sim_root: Path,
    sim_id: str,
    reset: bool,
) -> Dict[str, float]:
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_dir = sim_root / sim_id
    if reset and sim_dir.exists():
        shutil.rmtree(sim_dir)

    engine = SimulationEngine(sim_id, kb, sim_dir)
    if sim_dir.exists() and (sim_dir / "snapshot.json").exists():
        engine.load()

    for item_id, imp in sorted(plan.imports.items()):
        if engine.has_item(item_id, imp.qty, imp.unit):
            continue
        engine.import_item(item_id, imp.qty, imp.unit)

    recipe_order = _order_recipes(plan, kb)
    recipe_map = {r.recipe_id: r for r in plan.recipes}
    durations: Dict[str, float] = {}

    for rid in recipe_order:
        recipe = recipe_map[rid]
        start_time = engine.scheduler.current_time
        result = engine.run_recipe(recipe.recipe_id, recipe.quantity)
        if not result.get("success"):
            raise RuntimeError(f"Recipe failed in preview: {recipe.recipe_id}")
        error = _advance_until_idle(engine)
        if error:
            raise RuntimeError(f"Advance failed in preview for {recipe.recipe_id}: {error}")
        durations[rid] = max(0.0, engine.scheduler.current_time - start_time)

    if plan.target_recipe_id and plan.target_recipe_id not in durations:
        start_time = engine.scheduler.current_time
        result = engine.run_recipe(plan.target_recipe_id, 1)
        if not result.get("success"):
            raise RuntimeError(f"Target recipe failed in preview: {plan.target_recipe_id}")
        error = _advance_until_idle(engine)
        if error:
            raise RuntimeError(f"Advance failed in preview for {plan.target_recipe_id}: {error}")
        durations[plan.target_recipe_id] = max(0.0, engine.scheduler.current_time - start_time)

    engine.save()
    return durations


def _yaml_dump(commands: List[Dict[str, Any]]) -> str:
    try:
        import yaml  # type: ignore
    except Exception as exc:
        raise RuntimeError("PyYAML is required to write runbooks") from exc

    return yaml.safe_dump(
        commands,
        sort_keys=False,
        default_flow_style=False,
    )


def _build_runbook_commands(
    plan: SimPlan,
    kb: KBLoader,
    advance_map: Optional[Dict[str, float]],
) -> List[Dict[str, Any]]:
    commands: List[Dict[str, Any]] = []

    commands.append({
        "cmd": "sim.use",
        "args": {"sim-id": plan.sim_id},
    })
    commands.append({
        "cmd": "sim.reset",
        "args": {"sim-id": plan.sim_id},
    })
    commands.append({
        "cmd": "sim.note",
        "args": {
            "style": "milestone",
            "message": "Simulation reset. Starting combined build.",
        },
    })

    for item_id, imp in sorted(plan.imports.items()):
        commands.append({
            "cmd": "sim.import",
            "args": {
                "item": item_id,
                "quantity": imp.qty,
                "unit": imp.unit,
                "ensure": True,
            },
        })

    for note in plan.notes:
        commands.append({
            "cmd": "sim.note",
            "args": {
                "style": note.style,
                "message": note.message,
            },
        })

    recipe_order = _order_recipes(plan, kb)
    recipe_map = {r.recipe_id: r for r in plan.recipes}
    for rid in recipe_order:
        recipe = recipe_map[rid]
        commands.append({
            "cmd": "sim.run-recipe",
            "args": {
                "recipe": recipe.recipe_id,
                "quantity": recipe.quantity,
            },
        })
        if advance_map and rid in advance_map:
            hours = round(advance_map[rid], 6)
            if hours > 0:
                commands.append({
                    "cmd": "sim.advance-time",
                    "args": {
                        "hours": hours,
                    },
                })

    if plan.target_recipe_id and plan.target_recipe_id not in recipe_map:
        commands.append({
            "cmd": "sim.run-recipe",
            "args": {
                "recipe": plan.target_recipe_id,
                "quantity": 1,
            },
        })
        if advance_map and plan.target_recipe_id in advance_map:
            hours = round(advance_map[plan.target_recipe_id], 6)
            if hours > 0:
                commands.append({
                    "cmd": "sim.advance-time",
                    "args": {
                        "hours": hours,
                    },
                })

    if plan.build_machine:
        commands.append({
            "cmd": "sim.build-machine",
            "args": {
                "machine": plan.target_machine_id,
            },
        })

    commands.append({
        "cmd": "sim.status",
        "args": {},
    })

    return commands


def _write_runbook(path: Path, title: str, commands: List[Dict[str, Any]]) -> None:
    yaml_block = _yaml_dump(commands).strip()
    content = "\n".join([
        f"# {title}",
        "",
        "Generated from a SimPlan.",
        "",
        "```sim-runbook",
        yaml_block,
        "```",
        "",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate runbook Markdown from a SimPlan.")
    parser.add_argument("--plan", required=True, help="Path to SimPlan JSON")
    parser.add_argument("--out", help="Output runbook path")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument(
        "--no-advance",
        action="store_true",
        help="Omit advance-time steps (run-recipe only)",
    )
    parser.add_argument(
        "--preview-sim-id",
        help="Simulation id to use for advance-time calculation",
    )
    parser.add_argument(
        "--keep-preview",
        action="store_true",
        help="Keep preview simulation data after computing durations",
    )
    args = parser.parse_args()

    plan_path = Path(args.plan)
    plan = SimPlan.load(plan_path)

    kb_root = Path(args.kb_root)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    advance_map: Optional[Dict[str, float]] = None
    preview_sim_id = args.preview_sim_id or f"{plan.sim_id}__runbook_preview"
    if not args.no_advance:
        advance_map = _compute_recipe_durations(
            plan=plan,
            kb_root=kb_root,
            sim_root=Path(args.sim_root),
            sim_id=preview_sim_id,
            reset=True,
        )
        if not args.keep_preview:
            preview_dir = Path(args.sim_root) / preview_sim_id
            if preview_dir.exists():
                shutil.rmtree(preview_dir)

    commands = _build_runbook_commands(plan, kb, advance_map)

    out_path = Path(args.out) if args.out else (REPO_ROOT / "runbooks" / f"{plan.sim_id}_runbook.md")
    title = f"{plan.target_machine_id} SimPlan Runbook"
    _write_runbook(out_path, title, commands)
    print(f"Wrote runbook: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
