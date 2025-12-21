"""
Command-line interface for individual simulation commands.

Allows running single commands against a simulation without maintaining
a persistent Python session.

Each command:
1. Loads the simulation from disk
2. Performs the requested action
3. Saves the updated state
4. Exits

Usage:
    python -m base_builder.cli view-state --sim-id my_sim
    python -m base_builder.cli import --sim-id my_sim --item carbon_anode --quantity 2 --unit kg
    python -m base_builder.cli start-process --sim-id my_sim --process alumina_extraction --scale 1 --duration 10
    python -m base_builder.cli advance-time --sim-id my_sim --hours 10
"""
import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from base_builder.kb_loader import KBLoader
from base_builder.sim_engine import SimulationEngine

REPO_ROOT = Path(__file__).parent.parent
KB_ROOT = REPO_ROOT / "kb"
SIMULATIONS_DIR = REPO_ROOT / "simulations"


def load_simulation(sim_id: str) -> tuple[SimulationEngine, KBLoader]:
    """Load a simulation and KB."""
    # Load KB
    kb_loader = KBLoader(KB_ROOT)
    kb_loader.load_all()

    # Load simulation
    sim_dir = SIMULATIONS_DIR / sim_id
    engine = SimulationEngine(sim_id, kb_loader, sim_dir)
    engine.load()

    return engine, kb_loader


def cmd_view_state(args):
    """View current simulation state."""
    engine, _ = load_simulation(args.sim_id)
    state = engine.get_state_dict()

    print(f"=== Simulation: {args.sim_id} ===")
    print(f"Time: {state['current_time_hours']:.1f} hours ({state['current_time_hours']/24:.1f} days)")
    print(f"\nInventory ({len(state['inventory'])} items):")
    for item_id, inv in sorted(state['inventory'].items()):
        print(f"  {item_id}: {inv['quantity']:.2f} {inv['unit']}")

    print(f"\nActive Processes ({len(state['active_processes'])}):")
    for proc in state['active_processes']:
        remaining = proc['ends_at'] - state['current_time_hours']
        print(f"  {proc['process_id']} (ends at {proc['ends_at']:.1f}h, {remaining:.1f}h remaining)")

    print(f"\nMachines Built ({len(state['machines_built'])}):")
    for machine in state['machines_built']:
        print(f"  {machine}")

    print(f"\nTotal Imports ({len(state['total_imports'])} items):")
    total_mass = 0.0
    for item_id, inv in sorted(state['total_imports'].items()):
        print(f"  {item_id}: {inv['quantity']:.2f} {inv['unit']}")
        if inv['unit'] == 'kg':
            total_mass += inv['quantity']
    print(f"  Total mass: ~{total_mass:.1f} kg")

    return 0


def cmd_import(args):
    """Import an item from Earth."""
    engine, _ = load_simulation(args.sim_id)

    result = engine.import_item(args.item, args.quantity, args.unit)

    if result['success']:
        print(f"✓ Imported {args.quantity} {args.unit} of '{args.item}'")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to import: {result.get('message', 'Unknown error')}")
        return 1


def cmd_start_process(args):
    """Start a process."""
    engine, _ = load_simulation(args.sim_id)

    result = engine.start_process(args.process, args.scale, args.duration)

    if result['success']:
        print(f"✓ Started process '{args.process}'")
        print(f"  Scale: {args.scale}")
        print(f"  Duration: {args.duration} hours")
        print(f"  Ends at: {result['ends_at']:.1f} hours")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to start process: {result.get('message', 'Unknown error')}")
        if result.get('error') == 'insufficient_inputs':
            print(f"  Missing inputs: {result.get('message')}")
        return 1


def cmd_run_recipe(args):
    """Run a recipe."""
    engine, _ = load_simulation(args.sim_id)

    result = engine.run_recipe(args.recipe, args.quantity)

    if result['success']:
        print(f"✓ Ran recipe '{args.recipe}' x{args.quantity}")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to run recipe: {result.get('message', 'Unknown error')}")
        return 1


def cmd_build_machine(args):
    """Build a machine from BOM."""
    engine, _ = load_simulation(args.sim_id)

    result = engine.build_machine(args.machine)

    if result['success']:
        print(f"✓ Built machine '{args.machine}'")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to build machine: {result.get('message', 'Unknown error')}")
        return 1


def cmd_preview(args):
    """Preview time advancement."""
    engine, _ = load_simulation(args.sim_id)

    preview = engine.preview_step(args.hours)

    print(f"=== Preview: Advance {args.hours} hours ===")
    print(f"Current time: {engine.state.current_time_hours:.1f}h")
    print(f"New time: {preview['new_time']:.1f}h")
    print(f"\nProcesses completing: {preview['completing_count']}")

    for proc in preview['processes_completing']:
        print(f"\n  Process: {proc['process_id']}")
        print(f"  Ends at: {proc['ends_at']:.1f}h")
        print(f"  Outputs:")
        for item_id, output in proc['outputs'].items():
            print(f"    {item_id}: +{output['quantity']} {output['unit']}")

    return 0


def cmd_advance_time(args):
    """Advance simulation time."""
    engine, _ = load_simulation(args.sim_id)

    old_time = engine.state.current_time_hours  # Capture old time before advancing
    print(f"Advancing time by {args.hours} hours...")
    result = engine.advance_time(args.hours)

    print(f"✓ Time advanced")
    print(f"  Old time: {old_time:.1f}h")
    print(f"  New time: {result['new_time']:.1f}h")

    if result.get('completed_count', 0) > 0:
        print(f"  Completed {result['completed_count']} processes")

    # Don't need explicit save - advance_time saves automatically
    return 0


def cmd_list_sims(args):
    """List all simulations."""
    if not SIMULATIONS_DIR.exists():
        print("No simulations found.")
        return 0

    sims = []
    for sim_dir in SIMULATIONS_DIR.iterdir():
        if not sim_dir.is_dir():
            continue

        log_file = sim_dir / "simulation.jsonl"
        if not log_file.exists():
            continue

        # Read last state
        try:
            with log_file.open() as f:
                lines = f.readlines()
                for line in reversed(lines):
                    event = json.loads(line)
                    if event.get('type') == 'state_snapshot':
                        sims.append({
                            'sim_id': sim_dir.name,
                            'time_hours': event.get('time_hours', 0),
                            'inventory_items': len(event.get('inventory', {})),
                            'machines_built': len(event.get('machines_built', [])),
                        })
                        break
        except Exception:
            continue

    if not sims:
        print("No simulations found.")
        return 0

    print("=== Simulations ===")
    for sim in sorted(sims, key=lambda s: s['sim_id']):
        print(f"\n{sim['sim_id']}:")
        print(f"  Time: {sim['time_hours']:.1f} hours ({sim['time_hours']/24:.1f} days)")
        print(f"  Inventory: {sim['inventory_items']} items")
        print(f"  Machines: {sim['machines_built']}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Base Builder Simulation - Individual Commands",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # View simulation state
  python -m base_builder.cli_commands view-state --sim-id my_sim

  # Import materials
  python -m base_builder.cli_commands import --sim-id my_sim --item carbon_anode --quantity 2 --unit kg

  # Start a process
  python -m base_builder.cli_commands start-process --sim-id my_sim --process alumina_extraction_from_highlands_v0 --scale 1 --duration 10

  # Preview time advance
  python -m base_builder.cli_commands preview --sim-id my_sim --hours 10

  # Advance time
  python -m base_builder.cli_commands advance-time --sim-id my_sim --hours 10

  # List simulations
  python -m base_builder.cli_commands list
"""
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    subparsers.required = True

    # view-state
    parser_view = subparsers.add_parser('view-state', help='View current simulation state')
    parser_view.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_view.set_defaults(func=cmd_view_state)

    # import
    parser_import = subparsers.add_parser('import', help='Import item from Earth')
    parser_import.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_import.add_argument('--item', required=True, help='Item ID to import')
    parser_import.add_argument('--quantity', type=float, required=True, help='Quantity')
    parser_import.add_argument('--unit', required=True, help='Unit (kg, count, etc.)')
    parser_import.set_defaults(func=cmd_import)

    # start-process
    parser_process = subparsers.add_parser('start-process', help='Start a process')
    parser_process.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_process.add_argument('--process', required=True, help='Process ID')
    parser_process.add_argument('--scale', type=float, default=1.0, help='Scale factor (default: 1.0)')
    parser_process.add_argument('--duration', type=float, required=True, help='Duration in hours')
    parser_process.set_defaults(func=cmd_start_process)

    # run-recipe
    parser_recipe = subparsers.add_parser('run-recipe', help='Run a recipe')
    parser_recipe.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_recipe.add_argument('--recipe', required=True, help='Recipe ID')
    parser_recipe.add_argument('--quantity', type=int, default=1, help='Quantity to produce (default: 1)')
    parser_recipe.set_defaults(func=cmd_run_recipe)

    # build-machine
    parser_build = subparsers.add_parser('build-machine', help='Build a machine from BOM')
    parser_build.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_build.add_argument('--machine', required=True, help='Machine ID')
    parser_build.set_defaults(func=cmd_build_machine)

    # preview
    parser_preview = subparsers.add_parser('preview', help='Preview time advancement')
    parser_preview.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_preview.add_argument('--hours', type=float, required=True, help='Hours to advance')
    parser_preview.set_defaults(func=cmd_preview)

    # advance-time
    parser_advance = subparsers.add_parser('advance-time', help='Advance simulation time')
    parser_advance.add_argument('--sim-id', required=True, help='Simulation ID')
    parser_advance.add_argument('--hours', type=float, required=True, help='Hours to advance')
    parser_advance.set_defaults(func=cmd_advance_time)

    # list
    parser_list = subparsers.add_parser('list', help='List all simulations')
    parser_list.set_defaults(func=cmd_list_sims)

    args = parser.parse_args()
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
