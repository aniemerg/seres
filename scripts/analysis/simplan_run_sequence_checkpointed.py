#!/usr/bin/env python3
"""
Execute per-machine SimPlans sequentially with per-machine checkpoints.

Each successful machine build writes a checkpoint copy of snapshot.json and
events.jsonl, plus a progress marker for resume.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

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


def _checkpoint_dir(sim_root: Path, sim_id: str, override: Optional[str]) -> Path:
    if override:
        return Path(override)
    return sim_root / sim_id / "checkpoints"


def _checkpoint_name(idx: int, machine_id: str) -> str:
    return f"{idx:03d}_{machine_id}"


def _write_progress(checkpoint_dir: Path, data: Dict[str, object]) -> None:
    progress_path = checkpoint_dir / "progress.json"
    progress_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _load_progress(checkpoint_dir: Path) -> Optional[Dict[str, object]]:
    progress_path = checkpoint_dir / "progress.json"
    if not progress_path.exists():
        return None
    return json.loads(progress_path.read_text(encoding="utf-8"))


def _append_checkpoint_log(checkpoint_dir: Path, data: Dict[str, object]) -> None:
    log_path = checkpoint_dir / "checkpoints.jsonl"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")


def _write_checkpoint(
    checkpoint_dir: Path,
    sim_dir: Path,
    idx: int,
    machine_id: str,
    sim_id: str,
    plan_path: Path,
) -> Optional[str]:
    snapshot_path = sim_dir / "snapshot.json"
    if not snapshot_path.exists():
        print("WARN: snapshot.json missing; skipping checkpoint copy.", file=sys.stderr)
        return None
    checkpoint_name = _checkpoint_name(idx, machine_id)
    ckpt_path = checkpoint_dir / checkpoint_name
    ckpt_path.mkdir(parents=True, exist_ok=True)
    shutil.copy2(snapshot_path, ckpt_path / "snapshot.json")
    events_path = sim_dir / "events.jsonl"
    if events_path.exists():
        shutil.copy2(events_path, ckpt_path / "events.jsonl")

    meta = {
        "checkpoint": checkpoint_name,
        "index": idx,
        "machine_id": machine_id,
        "sim_id": sim_id,
        "plan_path": str(plan_path),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    (ckpt_path / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    _append_checkpoint_log(checkpoint_dir, meta)
    _write_progress(checkpoint_dir, meta)
    return checkpoint_name


def _latest_checkpoint_from_dir(checkpoint_dir: Path) -> Optional[Dict[str, object]]:
    progress = _load_progress(checkpoint_dir)
    if progress:
        return progress
    candidates: List[tuple[int, str, Path]] = []
    for child in checkpoint_dir.iterdir():
        if not child.is_dir():
            continue
        if not (child / "snapshot.json").exists():
            continue
        prefix = child.name.split("_", 1)[0]
        if not prefix.isdigit():
            continue
        candidates.append((int(prefix), child.name, child))
    if not candidates:
        return None
    idx, name, _path = sorted(candidates, key=lambda c: c[0])[-1]
    return {"checkpoint": name, "index": idx}


def _restore_checkpoint(checkpoint_dir: Path, sim_dir: Path, checkpoint_name: str) -> None:
    ckpt_path = checkpoint_dir / checkpoint_name
    snapshot_path = ckpt_path / "snapshot.json"
    if not snapshot_path.exists():
        raise FileNotFoundError(f"Checkpoint missing snapshot.json: {ckpt_path}")
    sim_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(snapshot_path, sim_dir / "snapshot.json")
    events_path = ckpt_path / "events.jsonl"
    if events_path.exists():
        shutil.copy2(events_path, sim_dir / "events.jsonl")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run per-machine SimPlans sequentially with checkpoints."
    )
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
    parser.add_argument(
        "--checkpoint-dir",
        help="Directory to store checkpoints (default: <sim_root>/<sim_id>/checkpoints)",
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Print step-by-step execution trace for each plan",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from latest checkpoint and skip completed machines",
    )
    parser.add_argument(
        "--resume-from",
        help="Resume from a specific checkpoint name (e.g., 012_machine_id)",
    )
    parser.add_argument(
        "--force-resume",
        action="store_true",
        help="Resume even if checkpoint machine id does not match current list",
    )
    args = parser.parse_args()

    if args.resume and args.reset:
        print("Error: --resume cannot be used with --reset.", file=sys.stderr)
        return 1

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

    sim_root = Path(args.sim_root)
    sim_dir = sim_root / args.sim_id
    checkpoint_dir = _checkpoint_dir(sim_root, args.sim_id, args.checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    start_index = 1
    if args.resume or args.resume_from:
        if args.resume_from:
            checkpoint_info = {"checkpoint": args.resume_from}
        else:
            checkpoint_info = _latest_checkpoint_from_dir(checkpoint_dir)
            if not checkpoint_info:
                print("Error: no checkpoints found to resume from.", file=sys.stderr)
                return 1
        checkpoint_name = str(checkpoint_info.get("checkpoint"))
        idx = checkpoint_info.get("index")
        _restore_checkpoint(checkpoint_dir, sim_dir, checkpoint_name)
        if idx is None:
            prefix = checkpoint_name.split("_", 1)[0]
            if prefix.isdigit():
                idx = int(prefix)
        if isinstance(idx, int):
            if idx <= len(machines):
                machine_at_idx = machines[idx - 1]
                if (checkpoint_info.get("machine_id") or machine_at_idx) != machine_at_idx:
                    if not args.force_resume:
                        print(
                            f"Error: checkpoint machine mismatch at index {idx}: "
                            f"{checkpoint_info.get('machine_id')} vs {machine_at_idx}",
                            file=sys.stderr,
                        )
                        return 1
                start_index = idx + 1
        print(f"Resuming from checkpoint {checkpoint_name}; starting at index {start_index}.")

    plans_dir = Path(args.plans_dir)
    failures = 0
    for idx, machine_id in enumerate(machines, start=1):
        if idx < start_index:
            continue
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
            sim_root=sim_root,
            reset=args.reset and idx == 1,
            dry_run=args.dry_run,
            trace=args.trace,
        )
        if not result.get("success"):
            failures += 1
            print(f"FAIL: {machine_id} -> {result}", file=sys.stderr)
            if not args.continue_on_error:
                return 1
        else:
            print(f"OK: {machine_id}")
            if not args.dry_run:
                checkpoint_name = _write_checkpoint(
                    checkpoint_dir=checkpoint_dir,
                    sim_dir=sim_dir,
                    idx=idx,
                    machine_id=machine_id,
                    sim_id=args.sim_id,
                    plan_path=plan_path,
                )
                if checkpoint_name:
                    print(f"Checkpointed: {checkpoint_name}")

    if failures:
        print(f"Completed with {failures} failure(s).", file=sys.stderr)
        return 1
    print("Completed all plans successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
