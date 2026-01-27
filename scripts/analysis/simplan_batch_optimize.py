#!/usr/bin/env python3
"""
Batch optimize SimPlans for machines (short greedy runs).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.kb_core.kb_loader import KBLoader
from scripts.analysis.simplan_builder_import_only import main as build_import_only_main
from scripts.analysis.simplan_optimizer_greedy import main as greedy_main
from scripts.analysis.simplan import SimPlan


def _list_machine_ids(kb: KBLoader) -> List[str]:
    ids = []
    for item_id, item in kb.items.items():
        item_dict = item.model_dump() if hasattr(item, "model_dump") else item
        if item_dict.get("kind") == "machine":
            ids.append(item_id)
    return sorted(ids)


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch optimize ISRU SimPlans for machines.")
    parser.add_argument("--machines", nargs="*", help="Machine ids to process (default: all machines)")
    parser.add_argument("--limit", type=int, help="Max machines to process")
    parser.add_argument("--iterations", type=int, default=1, help="Greedy iterations per machine")
    parser.add_argument("--kb-root", default=str(REPO_ROOT / "kb"), help="KB root")
    parser.add_argument("--out-dir", default=str(REPO_ROOT / "out" / "simplans"), help="Output directory")
    args = parser.parse_args()

    kb = KBLoader(Path(args.kb_root), use_validated_models=False)
    kb.load_all()

    if args.machines:
        machine_ids = list(args.machines)
    else:
        machine_ids = _list_machine_ids(kb)

    if args.limit:
        machine_ids = machine_ids[: args.limit]

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    summary: List[Dict[str, Any]] = []

    for machine_id in machine_ids:
        sim_id = f"simplan_{machine_id}"
        print(f"\n== {machine_id} ==")

        # Build import-only plan
        plan_path = out_dir / f"{machine_id}_import_only.json"
        cmd_args = [
            "--machine-id", machine_id,
            "--sim-id", sim_id,
            "--out", str(plan_path),
            "--kb-root", str(args.kb_root),
        ]
        sys.argv = ["simplan_builder_import_only.py"] + cmd_args
        try:
            build_import_only_main()
        except SystemExit:
            pass
        except Exception as exc:
            summary.append({
                "machine_id": machine_id,
                "status": "skipped",
                "stage": "build_import_only",
                "error": str(exc),
            })
            print(f"Skipping {machine_id}: {exc}")
            continue

        # Run greedy optimizer
        opt_out = out_dir / f"{machine_id}_optimized.json"
        cmd_args = [
            "--machine-id", machine_id,
            "--sim-id", f"{sim_id}_opt",
            "--iterations", str(args.iterations),
            "--out", str(opt_out),
            "--kb-root", str(args.kb_root),
        ]
        sys.argv = ["simplan_optimizer_greedy.py"] + cmd_args
        try:
            greedy_main()
        except SystemExit:
            pass
        except Exception as exc:
            summary.append({
                "machine_id": machine_id,
                "status": "skipped",
                "stage": "optimize",
                "error": str(exc),
            })
            print(f"Skipping {machine_id}: {exc}")
            continue

        # Record summary
        result = {"machine_id": machine_id, "status": "ok", "plan": str(opt_out)}
        summary.append(result)

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nWrote summary: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
