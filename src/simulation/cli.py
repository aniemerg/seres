"""
Simulation CLI - Command-line interface for simulation operations.

Provides commands for managing and running simulations:
- init: Create new simulation
- import: Import items from Earth
- start-process: Start a process
- run-recipe: Run a recipe
- build-machine: Build a machine
- advance-time: Advance simulation time
- preview: Preview next step
- view-state: View current state
- list: List all simulations

Each command loads simulation, executes action, saves state, and reports results.
"""
import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine

REPO_ROOT = Path(__file__).parent.parent.parent
KB_ROOT = REPO_ROOT / "kb"
SIMULATIONS_DIR = REPO_ROOT / "simulations"


def load_or_create_simulation(sim_id: str, kb_loader: KBLoader, create: bool = False) -> SimulationEngine:
    """
    Load existing simulation or create new one.

    Args:
        sim_id: Simulation ID
        kb_loader: KB loader instance
        create: If True, create new simulation (fail if exists)
               If False, load existing (fail if doesn't exist)

    Returns:
        SimulationEngine instance
    """
    sim_dir = SIMULATIONS_DIR / sim_id
    log_file = sim_dir / "simulation.jsonl"
    exists = log_file.exists()

    if create and exists:
        print(f"Error: Simulation '{sim_id}' already exists", file=sys.stderr)
        sys.exit(1)

    if not create and not exists:
        print(f"Error: Simulation '{sim_id}' not found", file=sys.stderr)
        sys.exit(1)

    # Create engine
    engine = SimulationEngine(sim_id, kb_loader, sim_dir)

    # Load existing state if not creating
    if not create:
        success = engine.load()
        if not success:
            print(f"Error: Failed to load simulation '{sim_id}'", file=sys.stderr)
            sys.exit(1)

    return engine


# ============================================================================
# Commands
# ============================================================================

def cmd_init(args, kb_loader: KBLoader):
    """Initialize a new simulation."""
    # Check if simulation already exists
    sim_dir = SIMULATIONS_DIR / args.sim_id
    log_file = sim_dir / "simulation.jsonl"
    if log_file.exists():
        print(f"Error: Simulation '{args.sim_id}' already exists", file=sys.stderr)
        return 1

    # Create new simulation
    engine = SimulationEngine(args.sim_id, kb_loader, sim_dir)
    engine.load()  # This will create the initial SimStartEvent for new sims

    print(f"✓ Created simulation '{args.sim_id}'")
    print(f"  Location: {engine.sim_dir}")
    print(f"  Log file: {engine.log_file}")
    return 0


def cmd_view_state(args, kb_loader: KBLoader):
    """View current simulation state."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)
    state = engine.get_state_dict()

    print(f"=== Simulation: {args.sim_id} ===")
    print(f"Time: {state['current_time_hours']:.1f} hours ({state['current_time_hours']/24:.1f} days)")
    print(f"Energy Consumed: {state.get('total_energy_kwh', 0.0):.2f} kWh")

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
    print(f"  Total imported mass: ~{total_mass:.1f} kg")

    return 0


def cmd_import(args, kb_loader: KBLoader):
    """Import an item from Earth."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.import_item(args.item, args.quantity, args.unit)

    if result['success']:
        print(f"✓ Imported {args.quantity} {args.unit} of '{args.item}'")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to import: {result.get('message', 'Unknown error')}", file=sys.stderr)
        return 1


def cmd_start_process(args, kb_loader: KBLoader):
    """Start a process."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    # Duration is optional - engine will calculate if not provided
    # Can provide either duration OR (output_quantity + output_unit) for calculation
    result = engine.start_process(
        process_id=args.process,
        scale=args.scale if hasattr(args, 'scale') else 1.0,
        duration_hours=args.duration if args.duration else None,
        output_quantity=getattr(args, 'output_quantity', None),
        output_unit=getattr(args, 'output_unit', None)
    )

    if result['success']:
        duration = result.get('duration_hours', 0.0)
        calculated = result.get('duration_calculated', False)
        duration_source = "(calculated)" if calculated else "(provided)"
        print(f"✓ Started process '{args.process}'")
        print(f"  Duration: {duration:.2f} hours {duration_source}")
        print(f"  Ends at: {result.get('ends_at', 0.0):.2f} hours")
        if 'energy_kwh' in result:
            print(f"  Energy: {result['energy_kwh']:.2f} kWh")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to start process: {result.get('message', 'Unknown error')}", file=sys.stderr)
        if 'validation_errors' in result:
            print("\nValidation errors:", file=sys.stderr)
            for err in result['validation_errors']:
                print(f"  - {err['message']}", file=sys.stderr)
        return 1


def cmd_run_recipe(args, kb_loader: KBLoader):
    """Run a recipe."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.run_recipe(args.recipe, args.quantity)

    if result['success']:
        print(f"✓ Started recipe '{args.recipe}' (quantity: {args.quantity})")
        print(f"  Steps: {result.get('total_steps', 0)}")
        print(f"  Duration: {result.get('total_duration_hours', 0.0):.2f} hours")
        print(f"  Ends at: {result.get('ends_at', 0.0):.2f} hours")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to run recipe: {result.get('message', 'Unknown error')}", file=sys.stderr)
        return 1


def cmd_build_machine(args, kb_loader: KBLoader):
    """Build a machine from its BOM."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.build_machine(args.machine)

    if result['success']:
        print(f"✓ Built machine '{args.machine}'")
        print(f"  Parts consumed: {result.get('parts_consumed', 0)}")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to build machine: {result.get('message', 'Unknown error')}", file=sys.stderr)
        if 'missing_parts' in result:
            print("\nMissing parts:", file=sys.stderr)
            for part_id, qty, unit in result['missing_parts']:
                print(f"  - {part_id}: need {qty} {unit}", file=sys.stderr)
        return 1


def cmd_preview(args, kb_loader: KBLoader):
    """Preview simulation state after time advancement."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    current_time = engine.state.current_time_hours
    result = engine.preview_step(args.hours)

    print(f"=== Preview: +{args.hours} hours ===")
    print(f"Current time: {current_time:.2f} hours")
    print(f"After advance: {result['new_time']:.2f} hours")

    if result.get('processes_completing'):
        print(f"\nProcesses completing ({result['completing_count']}):")
        for proc in result['processes_completing']:
            print(f"  - {proc['process_id']} (at {proc['ends_at']:.2f}h)")
            if proc.get('outputs'):
                for item_id, item_info in proc['outputs'].items():
                    print(f"      → {item_id}: {item_info['quantity']:.2f} {item_info['unit']}")
    else:
        print("\nNo processes completing")

    return 0


def cmd_advance_time(args, kb_loader: KBLoader):
    """Advance simulation time."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.advance_time(args.hours)

    print(f"✓ Advanced time by {args.hours} hours")
    print(f"  New time: {result['new_time']:.2f} hours ({result['new_time']/24:.1f} days)")
    print(f"  Processes completed: {result['completed_count']}")
    print(f"  Total energy consumed: {result['total_energy_kwh']:.2f} kWh")

    if result['completed']:
        print(f"\nCompleted processes:")
        for proc in result['completed']:
            print(f"  - {proc['process_id']} (energy: {proc.get('energy_kwh', 0.0):.2f} kWh)")
            if proc.get('outputs'):
                for item_id, inv_item in proc['outputs'].items():
                    qty = inv_item.quantity if hasattr(inv_item, 'quantity') else inv_item['quantity']
                    unit = inv_item.unit if hasattr(inv_item, 'unit') else inv_item['unit']
                    print(f"      → {item_id}: {qty:.2f} {unit}")

    engine.save()
    return 0


def cmd_list(args, kb_loader: KBLoader):
    """List all simulations."""
    if not SIMULATIONS_DIR.exists():
        print("No simulations found")
        return 0

    sims = []
    for sim_dir in SIMULATIONS_DIR.iterdir():
        if sim_dir.is_dir():
            log_file = sim_dir / "simulation.jsonl"
            if log_file.exists():
                # Try to read first event to get sim info
                with open(log_file, 'r') as f:
                    first_line = f.readline()
                    if first_line:
                        event = json.loads(first_line)
                        sims.append({
                            'id': sim_dir.name,
                            'created': event.get('timestamp', 'unknown'),
                            'path': str(sim_dir)
                        })

    if not sims:
        print("No simulations found")
        return 0

    print(f"Found {len(sims)} simulation(s):\n")
    for sim in sorted(sims, key=lambda x: x['id']):
        print(f"  {sim['id']}")
        print(f"    Created: {sim['created']}")
        print(f"    Path: {sim['path']}")
        print()

    return 0


# ============================================================================
# Main CLI setup
# ============================================================================

def add_sim_subcommands(subparsers):
    """
    Add simulation subcommands to the main CLI.

    Called from src/cli.py to integrate sim commands.
    """
    sim_parser = subparsers.add_parser(
        'sim',
        help='Simulation commands'
    )

    sim_subparsers = sim_parser.add_subparsers(dest='sim_command', help='Simulation command')

    # init
    init_parser = sim_subparsers.add_parser('init', help='Initialize new simulation')
    init_parser.add_argument('--sim-id', required=True, help='Simulation ID')

    # view-state
    view_parser = sim_subparsers.add_parser('view-state', help='View simulation state')
    view_parser.add_argument('--sim-id', required=True, help='Simulation ID')

    # import
    import_parser = sim_subparsers.add_parser('import', help='Import item from Earth')
    import_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    import_parser.add_argument('--item', required=True, help='Item ID')
    import_parser.add_argument('--quantity', type=float, required=True, help='Quantity')
    import_parser.add_argument('--unit', required=True, help='Unit')

    # start-process
    start_parser = sim_subparsers.add_parser('start-process', help='Start a process')
    start_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    start_parser.add_argument('--process', required=True, help='Process ID')
    start_parser.add_argument('--scale', type=float, default=1.0, help='Scale factor')
    start_parser.add_argument('--duration', type=float, help='Duration in hours (optional, will calculate if omitted)')
    start_parser.add_argument('--output-quantity', type=float, help='Desired output quantity (for calculated duration)')
    start_parser.add_argument('--output-unit', type=str, help='Unit for output quantity (for calculated duration)')

    # run-recipe
    recipe_parser = sim_subparsers.add_parser('run-recipe', help='Run a recipe')
    recipe_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    recipe_parser.add_argument('--recipe', required=True, help='Recipe ID')
    recipe_parser.add_argument('--quantity', type=int, default=1, help='Batch quantity')

    # build-machine
    build_parser = sim_subparsers.add_parser('build-machine', help='Build a machine')
    build_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    build_parser.add_argument('--machine', required=True, help='Machine ID')

    # preview
    preview_parser = sim_subparsers.add_parser('preview', help='Preview time advancement')
    preview_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    preview_parser.add_argument('--hours', type=float, required=True, help='Hours to preview')

    # advance-time
    advance_parser = sim_subparsers.add_parser('advance-time', help='Advance simulation time')
    advance_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    advance_parser.add_argument('--hours', type=float, required=True, help='Hours to advance')

    # list
    list_parser = sim_subparsers.add_parser('list', help='List all simulations')

    return sim_parser


def run_sim_command(args, kb_loader: KBLoader):
    """
    Execute a simulation command.

    Called from src/cli.py after parsing args.
    """
    if not hasattr(args, 'sim_command') or args.sim_command is None:
        print("Error: No simulation command specified", file=sys.stderr)
        print("Use: python -m src.cli sim <command> --help", file=sys.stderr)
        return 1

    # Dispatch to command handlers
    commands = {
        'init': cmd_init,
        'view-state': cmd_view_state,
        'import': cmd_import,
        'start-process': cmd_start_process,
        'run-recipe': cmd_run_recipe,
        'build-machine': cmd_build_machine,
        'preview': cmd_preview,
        'advance-time': cmd_advance_time,
        'list': cmd_list,
    }

    handler = commands.get(args.sim_command)
    if not handler:
        print(f"Error: Unknown simulation command '{args.sim_command}'", file=sys.stderr)
        return 1

    return handler(args, kb_loader)
