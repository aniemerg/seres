"""
CLI interface for base builder simulations.

Commands:
- start: Start a new simulation
- continue: Continue an existing simulation
- list: List all simulations
- analyze: Analyze simulation results
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

from base_builder.agent import run_simulation


REPO_ROOT = Path(__file__).parent.parent
SIMULATIONS_DIR = REPO_ROOT / "simulations"


def cmd_start(args):
    """Start a new simulation."""
    sim_id = args.sim_id
    model = args.model

    sim_dir = SIMULATIONS_DIR / sim_id

    # Check if simulation already exists
    if sim_dir.exists() and (sim_dir / "simulation.jsonl").exists():
        print(f"⚠ Simulation '{sim_id}' already exists!")
        print(f"Use 'continue' command to resume it, or choose a different sim_id.")
        return 1

    print(f"Starting new simulation: {sim_id}")
    print(f"Model: {model}")
    print()

    run_simulation(sim_id, model=model)

    return 0


def cmd_continue(args):
    """Continue an existing simulation."""
    sim_id = args.sim_id
    model = args.model
    prompt = args.prompt

    sim_dir = SIMULATIONS_DIR / sim_id

    # Check if simulation exists
    if not sim_dir.exists() or not (sim_dir / "simulation.jsonl").exists():
        print(f"⚠ Simulation '{sim_id}' not found!")
        print(f"Use 'start' command to create it, or use 'list' to see existing simulations.")
        return 1

    print(f"Continuing simulation: {sim_id}")
    print(f"Model: {model}")
    print()

    # Custom prompt or default continuation
    if not prompt:
        prompt = "Continue building the base. Check current state and decide next steps."

    run_simulation(sim_id, model=model, initial_prompt=prompt)

    return 0


def cmd_list(args):
    """List all simulations."""
    if not SIMULATIONS_DIR.exists():
        print("No simulations found.")
        return 0

    sims = []
    for sim_dir in SIMULATIONS_DIR.iterdir():
        if sim_dir.is_dir():
            log_file = sim_dir / "simulation.jsonl"
            if log_file.exists():
                # Read last line to get current state
                try:
                    last_state = None
                    with log_file.open("r") as f:
                        for line in f:
                            try:
                                event = json.loads(line.strip())
                                if event.get("type") == "state_snapshot":
                                    last_state = event
                            except json.JSONDecodeError:
                                continue

                    if last_state:
                        sims.append({
                            "sim_id": sim_dir.name,
                            "time_hours": last_state.get("time_hours", 0),
                            "inventory_items": len(last_state.get("inventory", {})),
                            "machines_built": len(last_state.get("machines_built", [])),
                        })
                    else:
                        sims.append({
                            "sim_id": sim_dir.name,
                            "time_hours": 0,
                            "inventory_items": 0,
                            "machines_built": 0,
                        })
                except Exception:
                    sims.append({
                        "sim_id": sim_dir.name,
                        "time_hours": "?",
                        "inventory_items": "?",
                        "machines_built": "?",
                    })

    if not sims:
        print("No simulations found.")
        return 0

    print("=" * 80)
    print("SIMULATIONS")
    print("=" * 80)
    print()

    for sim in sorted(sims, key=lambda s: s["sim_id"]):
        print(f"• {sim['sim_id']}")
        print(f"  Time: {sim['time_hours']}h")
        print(f"  Inventory: {sim['inventory_items']} items")
        print(f"  Machines: {sim['machines_built']}")
        print()

    return 0


def cmd_analyze(args):
    """Analyze a simulation."""
    sim_id = args.sim_id

    sim_dir = SIMULATIONS_DIR / sim_id
    log_file = sim_dir / "simulation.jsonl"

    if not log_file.exists():
        print(f"⚠ Simulation '{sim_id}' not found!")
        return 1

    print("=" * 80)
    print(f"ANALYSIS: {sim_id}")
    print("=" * 80)
    print()

    # Read all events
    events = []
    with log_file.open("r") as f:
        for line in f:
            try:
                events.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue

    # Count event types
    event_types = {}
    for event in events:
        event_type = event.get("type", "unknown")
        event_types[event_type] = event_types.get(event_type, 0) + 1

    # Get final state
    final_state = None
    for event in reversed(events):
        if event.get("type") == "state_snapshot":
            final_state = event
            break

    # Count imports
    imports = {}
    total_import_mass = 0.0
    for event in events:
        if event.get("type") == "import":
            item_id = event.get("item_id")
            quantity = event.get("quantity", 0)
            unit = event.get("unit", "")
            mass_kg = event.get("mass_kg", 0) or 0

            if item_id in imports:
                imports[item_id]["quantity"] += quantity
                imports[item_id]["mass_kg"] += mass_kg
            else:
                imports[item_id] = {
                    "quantity": quantity,
                    "unit": unit,
                    "mass_kg": mass_kg
                }

            total_import_mass += mass_kg

    # Count KB gaps
    kb_gaps = []
    for event in events:
        if event.get("type") == "kb_gap":
            kb_gaps.append({
                "gap_type": event.get("gap_type"),
                "details": event.get("details"),
            })

    # Print analysis
    print(f"Total events: {len(events)}")
    print()

    print("Event types:")
    for event_type, count in sorted(event_types.items()):
        print(f"  {event_type}: {count}")
    print()

    if final_state:
        print(f"Final time: {final_state.get('time_hours', 0)}h")
        print(f"Final inventory: {len(final_state.get('inventory', {}))} items")
        print(f"Machines built: {len(final_state.get('machines_built', []))}")
        if final_state.get('machines_built'):
            for machine in final_state['machines_built']:
                print(f"  - {machine}")
        print()

    if imports:
        print(f"Total imports: {len(imports)} unique items")
        print(f"Total import mass (estimated): {total_import_mass:.1f} kg")
        print()
        print("Imported items:")
        for item_id, data in sorted(imports.items()):
            print(f"  - {item_id}: {data['quantity']} {data['unit']} ({data['mass_kg']:.1f} kg)")
        print()
    else:
        print("No imports! ✓ Perfect ISRU usage")
        print()

    if kb_gaps:
        print(f"KB gaps found: {len(kb_gaps)}")
        for gap in kb_gaps[:10]:
            print(f"  - {gap['gap_type']}: {gap['details']}")
        if len(kb_gaps) > 10:
            print(f"  ... and {len(kb_gaps) - 10} more")
        print()

    return 0


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Base Builder Simulation CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # start command
    start_parser = subparsers.add_parser("start", help="Start a new simulation")
    start_parser.add_argument("--sim-id", required=True, help="Simulation ID")
    start_parser.add_argument("--model", default="gpt-4", help="Model to use (default: gpt-4)")

    # continue command
    continue_parser = subparsers.add_parser("continue", help="Continue existing simulation")
    continue_parser.add_argument("--sim-id", required=True, help="Simulation ID")
    continue_parser.add_argument("--model", default="gpt-4", help="Model to use")
    continue_parser.add_argument("--prompt", help="Custom continuation prompt")

    # list command
    list_parser = subparsers.add_parser("list", help="List all simulations")

    # analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a simulation")
    analyze_parser.add_argument("--sim-id", required=True, help="Simulation ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "start":
        return cmd_start(args)
    elif args.command == "continue":
        return cmd_continue(args)
    elif args.command == "list":
        return cmd_list(args)
    elif args.command == "analyze":
        return cmd_analyze(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    exit(main())
