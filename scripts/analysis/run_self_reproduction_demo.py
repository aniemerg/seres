#!/usr/bin/env python3
"""
Run the self-reproduction demo end-to-end and emit a story-friendly report.

- Executes the canonical machine list via SimPlan sequence
  (producing machines via process outputs and/or BOM builds).
- Writes outputs to out/self_repro_demo/.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_runner import execute_plan


def _load_machine_list(path: Path) -> List[str]:
    machines: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        entry = line.strip()
        if not entry or entry.startswith("#"):
            continue
        machines.append(entry)
    return machines


def _load_kb_machine_ids(kb_root: Path) -> Set[str]:
    from src.kb_core.kb_loader import KBLoader

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    machine_ids: Set[str] = set()
    for item_id, item in kb.items.items():
        item_dict = item.model_dump() if hasattr(item, "model_dump") else item
        if item_dict.get("kind") == "machine":
            machine_ids.add(item_id)
    return machine_ids


def _load_snapshot(sim_dir: Path) -> Dict[str, object]:
    snapshot_path = sim_dir / "snapshot.json"
    return json.loads(snapshot_path.read_text(encoding="utf-8"))


def _load_events(sim_dir: Path) -> List[Dict[str, object]]:
    events_path = sim_dir / "events.jsonl"
    events: List[Dict[str, object]] = []
    if not events_path.exists():
        return events
    with events_path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            events.append(json.loads(line))
    return events


def _write_list(path: Path, items: List[str]) -> None:
    path.write_text("\n".join(items) + ("\n" if items else ""), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the SERES self-reproduction demo.")
    parser.add_argument(
        "--machine-list",
        default=str(REPO_ROOT / "docs" / "self_reproducing_set.txt"),
        help="Canonical machine list for self-reproduction",
    )
    parser.add_argument(
        "--sim-id",
        default="self_repro_demo",
        help="Simulation id",
    )
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--plans-dir", default=str(REPO_ROOT / "out" / "simplans"))
    parser.add_argument("--reset", action="store_true", help="Reset sim before first plan")
    parser.add_argument("--trace", action="store_true", help="Print step-by-step execution trace")
    args = parser.parse_args()

    machine_list = _load_machine_list(Path(args.machine_list))
    if not machine_list:
        print("No machines found in list.", file=sys.stderr)
        return 1

    failures = 0
    plans_dir = Path(args.plans_dir)
    for idx, machine_id in enumerate(machine_list, start=1):
        plan_path = plans_dir / f"{machine_id}_optimized.json"
        if not plan_path.exists():
            print(f"[{idx}/{len(machine_list)}] Missing plan for {machine_id}: {plan_path}", file=sys.stderr)
            failures += 1
            continue

        plan = SimPlan.load(plan_path)
        plan.sim_id = args.sim_id

        print(f"[{idx}/{len(machine_list)}] Executing {machine_id}")
        result = execute_plan(
            plan=plan,
            kb_root=Path(args.kb_root),
            sim_root=Path(args.sim_root),
            reset=args.reset and idx == 1,
            trace=args.trace,
        )
        if not result.get("success"):
            failures += 1
            print(f"FAIL: {machine_id} -> {result}", file=sys.stderr)
        else:
            print(f"OK: {machine_id}")

    if failures:
        print(f"Completed with {failures} failure(s).", file=sys.stderr)
        return 1

    # Report section
    sim_dir = Path(args.sim_root) / args.sim_id
    out_dir = REPO_ROOT / "out" / "self_repro_demo"
    out_dir.mkdir(parents=True, exist_ok=True)

    machine_ids = _load_kb_machine_ids(Path(args.kb_root))
    snapshot = _load_snapshot(sim_dir)
    events = _load_events(sim_dir)

    state = snapshot.get("state", {})
    imports = state.get("total_imports", {}) or {}
    inventory = state.get("inventory", {}) or {}

    imported_machines = sorted([mid for mid in imports.keys() if mid in machine_ids])

    machines_in_inventory: List[str] = []
    for mid in machine_ids:
        inv_item = inventory.get(mid)
        if isinstance(inv_item, dict):
            qty = inv_item.get("quantity", 0) or 0
            if qty > 0:
                machines_in_inventory.append(mid)
    machines_in_inventory = sorted(set(machines_in_inventory))

    produced_via_process: Set[str] = set()
    produced_via_build: Set[str] = set()
    for ev in events:
        etype = ev.get("type")
        if etype == "process_complete":
            outputs = ev.get("outputs") or {}
            for item_id in outputs.keys():
                if item_id in machine_ids:
                    produced_via_process.add(item_id)
        elif etype == "build":
            mid = ev.get("machine_id")
            if mid in machine_ids:
                produced_via_build.add(mid)

    produced_machines = sorted(produced_via_process | produced_via_build)

    requested = set(machine_list)
    imported = set(imported_machines)
    produced = set(produced_machines)

    requested_not_produced = sorted(requested - produced)
    produced_not_requested = sorted(produced - requested)
    imported_not_produced = sorted(imported - produced)
    produced_not_imported = sorted(produced - imported)
    requested_not_imported = sorted(requested - imported)

    _write_list(out_dir / "requested_machines.txt", sorted(requested))
    _write_list(out_dir / "produced_machines.txt", produced_machines)
    _write_list(out_dir / "imported_machines.txt", imported_machines)
    _write_list(out_dir / "machines_in_inventory.txt", machines_in_inventory)
    _write_list(out_dir / "requested_not_produced.txt", requested_not_produced)
    _write_list(out_dir / "produced_not_requested.txt", produced_not_requested)
    _write_list(out_dir / "imported_not_produced.txt", imported_not_produced)
    _write_list(out_dir / "produced_not_imported.txt", produced_not_imported)
    _write_list(out_dir / "requested_not_imported.txt", requested_not_imported)

    summary = {
        "sim_id": args.sim_id,
        "requested_count": len(requested),
        "produced_count": len(produced),
        "imported_count": len(imported),
        "requested_not_produced": len(requested_not_produced),
        "produced_not_requested": len(produced_not_requested),
        "imported_not_produced": len(imported_not_produced),
        "produced_not_imported": len(produced_not_imported),
        "requested_not_imported": len(requested_not_imported),
        "success": {
            "requested_equals_produced": len(requested_not_produced) == 0 and len(produced_not_requested) == 0,
            "imports_subset_of_produced": len(imported_not_produced) == 0,
        },
    }

    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    summary_md = [
        "# Self-Reproduction Demo Summary",
        "",
        f"Simulation: `{args.sim_id}`",
        "",
        f"- Requested machines: {summary['requested_count']}",
        f"- Produced machines: {summary['produced_count']}",
        f"- Imported machines: {summary['imported_count']}",
        f"- Requested not produced: {summary['requested_not_produced']}",
        f"- Produced not requested: {summary['produced_not_requested']}",
        f"- Imported not produced: {summary['imported_not_produced']}",
        f"- Produced not imported: {summary['produced_not_imported']}",
        f"- Requested not imported: {summary['requested_not_imported']}",
        "",
        f"Requested == Produced: {summary['success']['requested_equals_produced']}",
        f"Imports ⊆ Produced: {summary['success']['imports_subset_of_produced']}",
    ]
    (out_dir / "summary.md").write_text("\n".join(summary_md) + "\n", encoding="utf-8")

    print(f"Report written to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
