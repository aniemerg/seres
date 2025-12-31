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
from typing import Optional, Dict, Any, Iterable

from src.kb_core.kb_loader import KBLoader
from src.kb_core.calculations import calculate_duration, calculate_energy, CalculationError
from src.kb_core.unit_converter import UnitConverter
from src.kb_core.schema import Quantity
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


def _as_quantity(entry: Any) -> Quantity:
    """Normalize dict/object entries into a Quantity."""
    if isinstance(entry, dict):
        item_id = entry.get("item_id")
        qty = entry.get("qty") if entry.get("qty") is not None else entry.get("quantity")
        unit = entry.get("unit", "kg")
    else:
        item_id = getattr(entry, "item_id", None)
        qty = getattr(entry, "qty", None)
        if qty is None:
            qty = getattr(entry, "quantity", None)
        unit = getattr(entry, "unit", "kg")
    return Quantity(item_id=item_id, qty=float(qty or 0), unit=unit)


def _collect_machine_requirements(process_def: Dict[str, Any]) -> Dict[str, str]:
    """Collect required machine IDs from process definition."""
    required: Dict[str, str] = {}

    for machine_id in process_def.get("requires_ids", []) or []:
        required[machine_id] = "1 unit"

    for req in process_def.get("resource_requirements", []) or []:
        if isinstance(req, dict) and req.get("machine_id"):
            qty = req.get("qty", 1.0)
            unit = req.get("unit", "hr")
            required[req["machine_id"]] = f"{qty} {unit}"

    return required


def _format_quantity_list(items: Iterable[Quantity]) -> list[str]:
    lines = []
    for item in items:
        lines.append(f"{item.item_id}: {item.qty:.2f} {item.unit}")
    return lines


def _calculate_readiness(process_model, converter: UnitConverter) -> Dict[str, str]:
    inputs = {_as_quantity(q).item_id: _as_quantity(q) for q in process_model.inputs}
    outputs = {_as_quantity(q).item_id: _as_quantity(q) for q in process_model.outputs}

    readiness = {"duration": "ok", "energy": "ok"}

    try:
        _ = calculate_duration(process_model, inputs, outputs, converter)
    except CalculationError as exc:
        readiness["duration"] = f"error: {exc}"
    except Exception as exc:
        readiness["duration"] = f"error: {exc}"

    if not getattr(process_model, "energy_model", None):
        readiness["energy"] = "n/a (no energy_model)"
    else:
        try:
            _ = calculate_energy(process_model, inputs, outputs, converter)
        except CalculationError as exc:
            readiness["energy"] = f"error: {exc}"
        except Exception as exc:
            readiness["energy"] = f"error: {exc}"

    return readiness


def cmd_plan(args, kb_loader: KBLoader):
    """Preflight a process or recipe to show immediate blockers."""
    converter = UnitConverter(kb_loader)

    if args.process:
        process_model = kb_loader.get_process(args.process)
        if not process_model:
            print(f"Error: Process '{args.process}' not found", file=sys.stderr)
            return 1

        process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
        required = _collect_machine_requirements(process_def)

        print(f"=== Plan: process {args.process} ===")
        if required:
            print("Required machines/resources:")
            for machine_id, detail in sorted(required.items()):
                print(f"  {machine_id}: {detail}")
        else:
            print("Required machines/resources: none")

        inputs = [_as_quantity(q) for q in process_def.get("inputs", [])]
        outputs = [_as_quantity(q) for q in process_def.get("outputs", [])]
        if inputs:
            print("Inputs:")
            for line in _format_quantity_list(inputs):
                print(f"  {line}")
        else:
            print("Inputs: none")

        if outputs:
            print("Outputs:")
            for line in _format_quantity_list(outputs):
                print(f"  {line}")
        else:
            print("Outputs: none")

        readiness = _calculate_readiness(process_model, converter)
        print("Duration calculation:", readiness["duration"])
        print("Energy calculation:", readiness["energy"])
        return 0

    if args.recipe:
        recipe_model = kb_loader.get_recipe(args.recipe)
        if not recipe_model:
            print(f"Error: Recipe '{args.recipe}' not found", file=sys.stderr)
            return 1

        recipe_def = recipe_model.model_dump() if hasattr(recipe_model, "model_dump") else recipe_model
        required = {}
        missing_steps = []

        for step in recipe_def.get("steps", []):
            process_id = step.get("process_id")
            process_model = kb_loader.get_process(process_id)
            if not process_model:
                missing_steps.append(process_id)
                continue
            process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
            required.update(_collect_machine_requirements(process_def))

        print(f"=== Plan: recipe {args.recipe} ===")
        if required:
            print("Required machines/resources:")
            for machine_id, detail in sorted(required.items()):
                print(f"  {machine_id}: {detail}")
        else:
            print("Required machines/resources: none")

        inputs = recipe_def.get("inputs", [])
        if inputs:
            print("Inputs:")
            for line in _format_quantity_list([_as_quantity(q) for q in inputs]):
                print(f"  {line}")
        else:
            print("Inputs: none specified (recipe uses step processes)")

        if missing_steps:
            print("Missing processes:")
            for proc_id in sorted(missing_steps):
                print(f"  {proc_id}")

        print("Duration/Energy calculation: not evaluated for recipes (step overrides possible)")
        return 0

    print("Error: Provide --process or --recipe", file=sys.stderr)
    return 1


def _parse_bootstrap_entry(entry: str) -> tuple[str, float, str]:
    """Parse bootstrap entries like item_id[:qty[:unit]]."""
    parts = entry.split(":")
    item_id = parts[0]
    qty = 1.0
    unit = "unit"
    if len(parts) >= 2 and parts[1]:
        qty = float(parts[1])
    if len(parts) >= 3 and parts[2]:
        unit = parts[2]
    return item_id, qty, unit


def cmd_scaffold(args, kb_loader: KBLoader):
    """Create a simulation with optional bootstrap imports."""
    sim_dir = SIMULATIONS_DIR / args.sim_id
    log_file = sim_dir / "simulation.jsonl"
    if log_file.exists():
        print(f"Error: Simulation '{args.sim_id}' already exists", file=sys.stderr)
        return 1

    engine = SimulationEngine(args.sim_id, kb_loader, sim_dir)
    engine.load()

    imported = []
    if args.bootstrap:
        for raw_entry in args.bootstrap.split(","):
            entry = raw_entry.strip()
            if not entry:
                continue
            item_id, qty, unit = _parse_bootstrap_entry(entry)
            result = engine.import_item(item_id, qty, unit)
            if not result.get("success"):
                print(f"✗ Failed to import {item_id}: {result.get('message', 'Unknown error')}", file=sys.stderr)
                return 1
            imported.append((item_id, qty, unit))

    engine.save()

    print(f"✓ Created simulation '{args.sim_id}'")
    print(f"  Location: {engine.sim_dir}")
    print(f"  Log file: {engine.log_file}")
    if imported:
        print("  Imported:")
        for item_id, qty, unit in imported:
            print(f"    - {item_id}: {qty} {unit}")
    return 0


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

    # plan
    plan_parser = sim_subparsers.add_parser('plan', help='Preflight a process or recipe')
    plan_group = plan_parser.add_mutually_exclusive_group(required=True)
    plan_group.add_argument('--process', help='Process ID')
    plan_group.add_argument('--recipe', help='Recipe ID')

    # scaffold
    scaffold_parser = sim_subparsers.add_parser('scaffold', help='Create a simulation with optional bootstrap imports')
    scaffold_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    scaffold_parser.add_argument(
        '--bootstrap',
        help='Comma-separated items to import (item_id[:qty[:unit]])'
    )

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
        'plan': cmd_plan,
        'scaffold': cmd_scaffold,
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
