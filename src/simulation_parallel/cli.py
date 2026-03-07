"""
CLI commands for non-breaking concurrent DES runner (sim2 namespace).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.kb_core.kb_loader import KBLoader
from src.simulation_parallel.runner import ConcurrentDESRunner
from src.simulation_parallel.session import load_session, SIM2_DIR


def _load_kb() -> KBLoader:
    kb = KBLoader(Path("kb"), use_validated_models=False)
    kb.load_all()
    return kb


def cmd_sim2_init(args) -> int:
    kb = _load_kb()
    session = load_session(args.sim_id, kb, create=True)
    session.save()
    print(f"Initialized sim2 '{args.sim_id}' in {SIM2_DIR / args.sim_id}")
    return 0


def cmd_sim2_import(args) -> int:
    kb = _load_kb()
    session = load_session(args.sim_id, kb, create=False)
    result = session.engine.import_item(args.item, args.quantity, args.unit)
    if not result.get("success"):
        print(f"Import failed: {result.get('message')}", file=sys.stderr)
        return 1
    session.save()
    print(f"Imported {args.quantity} {args.unit} of {args.item}")
    return 0


def cmd_sim2_submit_process(args) -> int:
    kb = _load_kb()
    session = load_session(args.sim_id, kb, create=False)
    runner = ConcurrentDESRunner(session)
    result = runner.submit_process_intent(
        process_id=args.process,
        scale=args.scale,
        duration_hours=args.duration,
        output_quantity=args.output_quantity,
        output_unit=args.output_unit,
    )
    session.save()
    status = result.get("status")
    if status == "accepted":
        detail = result.get("detail", {})
        print(
            f"accepted process={args.process} run_id={detail.get('process_run_id')} "
            f"start={detail.get('start_time')} end={detail.get('end_time')}"
        )
        return 0
    if status == "deferred":
        detail = result.get("detail", {})
        print(
            f"deferred process={args.process} intent_id={detail.get('intent_id')} "
            f"reason={detail.get('reason')}"
        )
        return 0
    print(f"rejected process={args.process}: {result.get('detail', {}).get('message')}", file=sys.stderr)
    return 1


def cmd_sim2_run_to_completion(args) -> int:
    kb = _load_kb()
    session = load_session(args.sim_id, kb, create=False)
    runner = ConcurrentDESRunner(session)
    result = runner.run_to_completion(max_no_progress=args.max_no_progress)
    session.save()
    print(f"status={result.get('status')} steps={result.get('steps')}")
    summary = result.get("summary", {})
    if summary:
        print(
            "summary "
            f"time={summary.get('current_time')} "
            f"queued_events={summary.get('queued_events')} "
            f"active_processes={summary.get('active_processes')} "
            f"deferred_intents={summary.get('deferred_intents')}"
        )
    if result.get("blocked_intents"):
        print(f"blocked_intents={len(result['blocked_intents'])}")
    return 0 if result.get("status") == "completed" else 2


def cmd_sim2_status(args) -> int:
    kb = _load_kb()
    session = load_session(args.sim_id, kb, create=False)
    runner = ConcurrentDESRunner(session)
    summary = runner.status()
    print(
        f"sim2={args.sim_id} time={summary['current_time']} queued_events={summary['queued_events']} "
        f"active_processes={summary['active_processes']} completed_processes={summary['completed_processes']} "
        f"deferred_intents={summary['deferred_intents']} next_event_time={summary['next_event_time']}"
    )
    return 0


def cmd_sim2_export_view(args) -> int:
    from src.simviewer.config import load_config
    from src.simviewer.exporter import export_simviewer

    sim_id = args.sim_id
    config_path = Path(args.config) if getattr(args, "config", None) else None
    out_dir = Path(args.out) if getattr(args, "out", None) else (Path("out") / "simviewer" / sim_id / "dist")

    try:
        config = load_config(config_path, sim_id)
        if getattr(args, "sim_root", None):
            config.simulation_root = str(args.sim_root)
        else:
            config.simulation_root = "simulations_parallel"
        result = export_simviewer(Path("."), config, out_dir)
    except Exception as exc:
        print(f"Export failed: {exc}", file=sys.stderr)
        return 1

    summary = result.get("summary", {})
    print(
        f"exported sim2={sim_id} out={result.get('out_dir')} "
        f"time={summary.get('time_hours', 0.0)} "
        f"process_runs={summary.get('process_runs_total', 0)}"
    )
    return 0


def add_sim2_subcommands(subparsers):
    sim2_parser = subparsers.add_parser("sim2", help="Concurrent DES runner commands")
    sim2_sub = sim2_parser.add_subparsers(dest="sim2_command", help="sim2 command")

    p_init = sim2_sub.add_parser("init", help="Initialize sim2 simulation")
    p_init.add_argument("--sim-id", required=True)

    p_import = sim2_sub.add_parser("import", help="Import inventory item")
    p_import.add_argument("--sim-id", required=True)
    p_import.add_argument("--item", required=True)
    p_import.add_argument("--quantity", type=float, required=True)
    p_import.add_argument("--unit", required=True)

    p_submit = sim2_sub.add_parser("submit-process", help="Submit a process intent")
    p_submit.add_argument("--sim-id", required=True)
    p_submit.add_argument("--process", required=True)
    p_submit.add_argument("--scale", type=float, default=1.0)
    p_submit.add_argument("--duration", type=float)
    p_submit.add_argument("--output-quantity", type=float)
    p_submit.add_argument("--output-unit")

    p_run = sim2_sub.add_parser("run-to-completion", help="Advance sim2 until completion or blocked")
    p_run.add_argument("--sim-id", required=True)
    p_run.add_argument("--max-no-progress", type=int, default=1000)

    p_status = sim2_sub.add_parser("status", help="Show sim2 status")
    p_status.add_argument("--sim-id", required=True)

    p_export = sim2_sub.add_parser("export-view", help="Export sim2 data for simviewer")
    p_export.add_argument("--sim-id", required=True)
    p_export.add_argument("--out", help="Output dist directory (default: out/simviewer/<sim-id>/dist)")
    p_export.add_argument("--config", help="Optional simviewer config YAML")
    p_export.add_argument("--sim-root", help="Optional simulation root override (default: simulations_parallel)")


def run_sim2_command(args):
    if not getattr(args, "sim2_command", None):
        print("Error: No sim2 command specified", file=sys.stderr)
        return 1
    commands = {
        "init": cmd_sim2_init,
        "import": cmd_sim2_import,
        "submit-process": cmd_sim2_submit_process,
        "run-to-completion": cmd_sim2_run_to_completion,
        "status": cmd_sim2_status,
        "export-view": cmd_sim2_export_view,
    }
    handler = commands.get(args.sim2_command)
    if not handler:
        print(f"Error: Unknown sim2 command '{args.sim2_command}'", file=sys.stderr)
        return 1
    return handler(args)
