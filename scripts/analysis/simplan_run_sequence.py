#!/usr/bin/env python3
"""
Execute a sequence of per-machine SimPlans in a single simulation.

Each plan is executed in full before moving to the next (no merge).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_runner import execute_plan


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


def main() -> int:
    parser = argparse.ArgumentParser(description="Run per-machine SimPlans sequentially in one sim.")
    parser.add_argument(
        "--runbook",
        default=str(REPO_ROOT / "runbooks" / "machine_runbook_queue_sequential.md"),
        help="Runbook markdown file with machine list",
    )
    parser.add_argument(
        "--machine-list",
        help="Plaintext file with one machine id per line",
    )
    parser.add_argument("--plans-dir", default=str(REPO_ROOT / "out" / "simplans"))
    parser.add_argument("--sim-id", required=True, help="Simulation id for sequential run")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--reset", action="store_true", help="Reset sim before first plan")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without executing")
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue to next plan after errors",
    )
    parser.add_argument("--limit", type=int, help="Limit number of machines")
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

    plans_dir = Path(args.plans_dir)
    failures = 0
    for idx, machine_id in enumerate(machines, start=1):
        plan_path = plans_dir / f"{machine_id}_optimized.json"
        if not plan_path.exists():
            print(f"[{idx}/{len(machines)}] Missing plan for {machine_id}: {plan_path}", file=sys.stderr)
            failures += 1
            if not args.continue_on_error:
                return 1
            continue

        plan = SimPlan.load(plan_path)
        plan.sim_id = args.sim_id

        print(f"[{idx}/{len(machines)}] Executing {machine_id}")
        result = execute_plan(
            plan=plan,
            kb_root=Path(args.kb_root),
            sim_root=Path(args.sim_root),
            reset=args.reset and idx == 1,
            dry_run=args.dry_run,
        )
        if not result.get("success"):
            failures += 1
            print(f"FAIL: {machine_id} -> {result}", file=sys.stderr)
            if not args.continue_on_error:
                return 1
        else:
            print(f"OK: {machine_id}")

    if failures:
        print(f"Completed with {failures} failure(s).", file=sys.stderr)
        return 1
    print("Completed all plans successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
