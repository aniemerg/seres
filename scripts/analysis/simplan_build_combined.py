#!/usr/bin/env python3
"""
Build a combined SimPlan for a list of machines.

Steps:
- Parse machine IDs from a runbook queue markdown file or a plain list.
- Run greedy optimizer per machine to generate optimized plans.
- Merge plans into a single combined plan.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_optimizer_greedy import main as greedy_main
from src.kb_core.kb_loader import KBLoader
from src.kb_core.unit_converter import UnitConverter


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


def _load_machine_list(list_path: Path) -> List[str]:
    machines: List[str] = []
    with list_path.open(encoding="utf-8") as f:
        for line in f:
            entry = line.strip()
            if not entry or entry.startswith("#"):
                continue
            machines.append(entry)
    return machines


def _run_optimizer(
    machine_id: str,
    sim_id: str,
    kb_root: Path,
    sim_root: Path,
    iterations: int,
    max_depth: int,
    out_path: Path,
    allow_bom: bool,
) -> None:
    args = [
        "--machine-id", machine_id,
        "--sim-id", sim_id,
        "--kb-root", str(kb_root),
        "--sim-root", str(sim_root),
        "--iterations", str(iterations),
        "--max-depth", str(max_depth),
        "--out", str(out_path),
    ]
    if allow_bom:
        args.append("--allow-bom")

    sys.argv = ["simplan_optimizer_greedy.py"] + args
    try:
        greedy_main()
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 0
        if code != 0:
            raise RuntimeError(f"optimizer failed for {machine_id} (exit {code})")
    if not out_path.exists():
        raise RuntimeError(f"optimizer did not write plan for {machine_id}")


def _merge_import(
    merged: SimPlan,
    item_id: str,
    qty: float,
    unit: str,
    reason: Optional[str],
    converter: UnitConverter,
) -> None:
    existing = merged.imports.get(item_id)
    if not existing:
        merged.add_import(item_id, qty, unit, reason=reason)
        return

    if existing.unit == unit:
        existing.qty += qty
        if reason and existing.reason != reason:
            existing.reason = f"{existing.reason}; {reason}" if existing.reason else reason
        return

    converted = converter.convert(qty, unit, existing.unit, item_id)
    if converted is not None:
        existing.qty += converted
        if reason and existing.reason != reason:
            existing.reason = f"{existing.reason}; {reason}" if existing.reason else reason
        return

    reverse = converter.convert(existing.qty, existing.unit, unit, item_id)
    if reverse is not None:
        existing.qty = reverse + qty
        existing.unit = unit
        if reason and existing.reason != reason:
            existing.reason = f"{existing.reason}; {reason}" if existing.reason else reason
        return

    raise RuntimeError(
        f"Unit mismatch for import '{item_id}': '{existing.unit}' vs '{unit}'"
    )


def _merge_plans(
    plans: List[SimPlan],
    kb: KBLoader,
    sim_id: str,
    allow_bom: bool,
) -> SimPlan:
    converter = UnitConverter(kb)
    merged = SimPlan(sim_id=sim_id, target_machine_id="multi_machine_plan")
    merged.build_machine = False

    for plan in plans:
        if plan.build_machine or not plan.target_recipe_id:
            if not allow_bom:
                raise RuntimeError(
                    f"Plan for '{plan.target_machine_id}' is missing a recipe target; "
                    "add a recipe or enable --allow-bom."
                )
        for item_id, imp in plan.imports.items():
            _merge_import(merged, item_id, imp.qty, imp.unit, imp.reason, converter)
        for recipe in plan.recipes:
            merged.add_recipe(recipe.recipe_id, recipe.quantity, reason=recipe.reason)
        if plan.target_recipe_id:
            merged.add_recipe(plan.target_recipe_id, 1, reason="target_recipe")
        elif allow_bom:
            merged.add_note(
                f"Import-only machine '{plan.target_machine_id}' has no recipe target.",
                style="warning",
            )
        for note in plan.notes:
            merged.add_note(note.message, style=note.style)

    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description="Build combined SimPlan from machine list.")
    parser.add_argument(
        "--runbook",
        default=str(REPO_ROOT / "runbooks" / "machine_runbook_queue_sequential.md"),
        help="Runbook markdown file with machine list",
    )
    parser.add_argument(
        "--machine-list",
        help="Plaintext file with one machine id per line",
    )
    parser.add_argument("--sim-id", required=True, help="Simulation id for combined plan")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--iterations", type=int, default=3, help="Greedy iterations per machine")
    parser.add_argument("--max-depth", type=int, default=6, help="Max recursion depth")
    parser.add_argument("--out", help="Output combined plan path")
    parser.add_argument("--plans-dir", default=str(REPO_ROOT / "out" / "simplans"))
    parser.add_argument("--limit", type=int, help="Limit number of machines")
    parser.add_argument(
        "--allow-bom",
        action="store_true",
        help="Allow BOM fallback when no recipe is available",
    )
    parser.add_argument(
        "--reuse-plans",
        action="store_true",
        help="Reuse existing optimized plans if present",
    )
    args = parser.parse_args()

    runbook_path = Path(args.runbook)
    list_path = Path(args.machine_list) if args.machine_list else None
    if list_path:
        machines = _load_machine_list(list_path)
    else:
        machines = _load_machine_ids(runbook_path)
    if args.limit:
        machines = machines[: args.limit]
    if not machines:
        print("No machines found in list.", file=sys.stderr)
        return 1

    kb_root = Path(args.kb_root)
    sim_root = Path(args.sim_root)
    plans_dir = Path(args.plans_dir)
    plans_dir.mkdir(parents=True, exist_ok=True)

    plan_paths: List[Path] = []
    for machine_id in machines:
        out_path = plans_dir / f"{machine_id}_optimized.json"
        plan_paths.append(out_path)
        if args.reuse_plans and out_path.exists():
            continue
        sim_id = f"{args.sim_id}__{machine_id}"
        print(f"Optimizing {machine_id} -> {out_path}")
        _run_optimizer(
            machine_id=machine_id,
            sim_id=sim_id,
            kb_root=kb_root,
            sim_root=sim_root,
            iterations=args.iterations,
            max_depth=args.max_depth,
            out_path=out_path,
            allow_bom=args.allow_bom,
        )

    plans: List[SimPlan] = []
    for path in plan_paths:
        plans.append(SimPlan.load(path))

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    merged = _merge_plans(plans, kb, sim_id=args.sim_id, allow_bom=args.allow_bom)
    metadata = {
        "machine_count": len(machines),
        "machines": machines,
    }
    if list_path:
        metadata["source_machine_list"] = str(list_path)
    else:
        metadata["source_runbook"] = str(runbook_path)
    merged.metadata.update(metadata)

    out_path = Path(args.out) if args.out else (REPO_ROOT / "out" / f"plan_{args.sim_id}_combined.json")
    merged.save(out_path)
    print(f"Wrote combined plan: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
