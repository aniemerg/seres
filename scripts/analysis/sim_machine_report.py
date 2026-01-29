#!/usr/bin/env python3
"""
Report machine sets for a simulation:
- imported machines (from snapshot total_imports)
- produced machines (process_complete outputs + build events)
- machines in inventory (from snapshot inventory)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Set, List
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


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
    parser = argparse.ArgumentParser(description="Report machine sets for a simulation.")
    parser.add_argument("--sim-id", required=True, help="Simulation id")
    parser.add_argument("--sim-root", default=str(REPO_ROOT / "simulations"), help="Sim root")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--out-dir", default=str(REPO_ROOT / "out"), help="Output directory")
    args = parser.parse_args()

    sim_dir = Path(args.sim_root) / args.sim_id
    snapshot = _load_snapshot(sim_dir)
    events = _load_events(sim_dir)
    machine_ids = _load_kb_machine_ids(Path(args.kb_root))

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

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_list(out_dir / f"{args.sim_id}_imported_machines.txt", imported_machines)
    _write_list(out_dir / f"{args.sim_id}_produced_machines.txt", produced_machines)
    _write_list(out_dir / f"{args.sim_id}_machines_in_inventory.txt", machines_in_inventory)

    print(f"imported_machines: {len(imported_machines)}")
    print(f"produced_machines: {len(produced_machines)} (process+build)")
    print(f"machines_in_inventory: {len(machines_in_inventory)}")
    print(f"out_dir: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
