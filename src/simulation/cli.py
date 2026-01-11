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
from src.kb_core.override_resolver import resolve_recipe_step_with_kb
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
    snapshot_file = sim_dir / "snapshot.json"
    exists = snapshot_file.exists()

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
    snapshot_file = sim_dir / "snapshot.json"
    if snapshot_file.exists():
        print(f"Error: Simulation '{args.sim_id}' already exists", file=sys.stderr)
        return 1

    # Create new simulation
    engine = SimulationEngine(args.sim_id, kb_loader, sim_dir)
    engine.load()  # This will create the initial SimStartEvent for new sims

    print(f"✓ Created simulation '{args.sim_id}'")
    print(f"  Location: {engine.sim_dir}")
    print(f"  Snapshot: {engine.snapshot_file}")
    print(f"  Events: {engine.event_log_file}")
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
    unknown_mass_count = 0

    for item_id, inv in sorted(state['total_imports'].items()):
        print(f"  {item_id}: {inv['quantity']:.2f} {inv['unit']}")

        # Calculate mass contribution (Issue #10)
        if inv['unit'] == 'kg':
            # Direct mass measurement
            total_mass += inv['quantity']
        elif inv['unit'] == 'unit':
            # Look up item mass
            item = kb_loader.get_item(item_id)
            if item:
                item_dict = item.model_dump() if hasattr(item, 'model_dump') else item
                item_mass = item_dict.get('mass')
                if item_mass is not None:
                    total_mass += item_mass * inv['quantity']
                else:
                    unknown_mass_count += 1
            else:
                unknown_mass_count += 1
        else:
            # Unknown unit (L, m3, etc.)
            unknown_mass_count += 1

    # Display total with unknown count
    if unknown_mass_count > 0:
        print(f"  Total imported mass: ~{total_mass:.1f} kg ({unknown_mass_count} items with unknown mass)")
    else:
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

    for machine_req in process_def.get("required_machines", []) or []:
        if isinstance(machine_req, dict):
            machine_id = list(machine_req.keys())[0]
            count = machine_req[machine_id]
        elif isinstance(machine_req, str):
            machine_id = machine_req
            count = 1
        else:
            continue
        required[machine_id] = f"{count} unit"

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


def _build_dependency_tree(item_id: str, kb_loader: KBLoader, depth: int = 0, max_depth: int = 10, visited: set = None) -> dict:
    """
    Recursively build dependency tree for an item.

    Returns dict with:
    - item_id: str
    - item_name: str
    - qty: float
    - unit: str
    - mass: float (if available)
    - recipe_id: str (if has recipe)
    - inputs: list of dependency trees
    - processes: list of process IDs
    - is_import: bool
    - is_boundary: bool (raw material)
    - warnings: list of strings
    """
    if visited is None:
        visited = set()

    if depth > max_depth:
        return {
            "item_id": item_id,
            "warnings": [f"Max depth {max_depth} reached"]
        }

    # Avoid circular dependencies
    if item_id in visited:
        return {
            "item_id": item_id,
            "warnings": ["Circular dependency detected"]
        }

    visited.add(item_id)

    # Get item info
    item = kb_loader.get_item(item_id)
    if not item:
        return {
            "item_id": item_id,
            "warnings": ["Item not found in KB"]
        }

    item_dict = item.model_dump() if hasattr(item, "model_dump") else item
    result = {
        "item_id": item_id,
        "item_name": item_dict.get("name", item_id),
        "mass": item_dict.get("mass", 0),
        "unit": item_dict.get("unit", "unit"),
        "is_import": item_dict.get("is_import", False),
        "warnings": []
    }

    # Check for recipe
    recipe_id = item_dict.get("recipe")
    if not recipe_id:
        result["warnings"].append("No recipe defined")
        result["is_import"] = True
        visited.remove(item_id)
        return result

    recipe = kb_loader.get_recipe(recipe_id)
    if not recipe:
        result["warnings"].append(f"Recipe {recipe_id} not found")
        result["is_import"] = True
        visited.remove(item_id)
        return result

    recipe_dict = recipe.model_dump() if hasattr(recipe, "model_dump") else recipe
    result["recipe_id"] = recipe_id
    result["processes"] = []
    result["inputs"] = []

    # Collect inputs from recipe steps
    all_inputs = {}

    for step in recipe_dict.get("steps", []):
        process_id = step.get("process_id")
        if not process_id:
            continue

        result["processes"].append(process_id)

        process = kb_loader.get_process(process_id)
        if not process:
            result["warnings"].append(f"Process {process_id} not found")
            continue

        process_dict = process.model_dump() if hasattr(process, "model_dump") else process

        # Check if boundary process
        if process_dict.get("process_type") == "boundary":
            result["is_boundary"] = True

        # Aggregate inputs from all processes
        for inp in process_dict.get("inputs", []):
            inp_dict = inp if isinstance(inp, dict) else inp.model_dump()
            inp_id = inp_dict.get("item_id")
            inp_qty = float(inp_dict.get("qty", 0))
            inp_unit = inp_dict.get("unit", "kg")

            if inp_id not in all_inputs:
                all_inputs[inp_id] = {"qty": 0, "unit": inp_unit}
            all_inputs[inp_id]["qty"] += inp_qty

    # Recursively build dependency trees for inputs
    for inp_id, inp_info in all_inputs.items():
        child_tree = _build_dependency_tree(inp_id, kb_loader, depth + 1, max_depth, visited.copy())
        child_tree["qty"] = inp_info["qty"]
        child_tree["unit"] = inp_info["unit"]
        result["inputs"].append(child_tree)

    visited.remove(item_id)
    return result


def _aggregate_materials(tree: dict, multiplier: float = 1.0) -> dict:
    """
    Aggregate all materials from dependency tree.

    Returns dict with:
    - raw_materials: dict of {item_id: {qty, unit, mass}}
    - imports: dict of {item_id: {qty, unit, mass}}
    - intermediates: dict of {item_id: {qty, unit, mass}}
    - processes: list of process_ids
    """
    raw_materials = {}
    imports = {}
    intermediates = {}
    processes = []

    def add_to_dict(target: dict, item_id: str, qty: float, unit: str, mass: float = 0):
        if item_id not in target:
            target[item_id] = {"qty": 0, "unit": unit, "mass": 0}
        target[item_id]["qty"] += qty
        target[item_id]["mass"] += mass

    def traverse(node: dict, mult: float):
        item_id = node.get("item_id")
        qty = node.get("qty", 1.0) * mult
        unit = node.get("unit", "unit")
        mass = (node.get("mass") or 0) * mult

        # Collect processes
        for proc in node.get("processes", []):
            if proc not in processes:
                processes.append(proc)

        # Classify this node
        if node.get("is_boundary"):
            add_to_dict(raw_materials, item_id, qty, unit, mass)
        elif node.get("is_import") or not node.get("inputs"):
            add_to_dict(imports, item_id, qty, unit, mass)
        else:
            # Has inputs, so it's an intermediate
            add_to_dict(intermediates, item_id, qty, unit, mass)

        # Recursively traverse inputs
        for child in node.get("inputs", []):
            child_qty = child.get("qty", 1.0)
            traverse(child, mult * child_qty)

    traverse(tree, multiplier)

    return {
        "raw_materials": raw_materials,
        "imports": imports,
        "intermediates": intermediates,
        "processes": processes
    }


def _print_dependency_tree(tree: dict, indent: int = 0, show_warnings: bool = True):
    """Print formatted dependency tree."""
    prefix = "  " * indent
    item_id = tree.get("item_id", "unknown")
    item_name = tree.get("item_name", item_id)
    qty = tree.get("qty", 1.0)
    unit = tree.get("unit", "unit")
    mass = tree.get("mass", 0)

    # Build line
    line = f"{prefix}├─ {item_name}"
    if qty != 1.0 or unit != "unit":
        line += f" ({qty:.2f} {unit}"
        if mass and mass > 0:
            line += f", ~{mass:.2f} kg"
        line += ")"

    # Add annotations
    annotations = []
    if tree.get("is_boundary"):
        annotations.append("ISRU/boundary")
    if tree.get("is_import"):
        annotations.append("IMPORT")
    if tree.get("recipe_id"):
        annotations.append(f"← {tree['recipe_id']}")

    if annotations:
        line += f"  [{', '.join(annotations)}]"

    print(line)

    # Show warnings
    if show_warnings and tree.get("warnings"):
        for warning in tree["warnings"]:
            print(f"{prefix}  ⚠ {warning}")

    # Show processes
    if tree.get("processes"):
        proc_str = ", ".join(tree["processes"])
        print(f"{prefix}  via: {proc_str}")

    # Recursively print inputs
    for child in tree.get("inputs", []):
        _print_dependency_tree(child, indent + 1, show_warnings)


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
        target_item_id = recipe_def.get("target_item_id")

        if not target_item_id:
            print(f"Error: Recipe has no target_item_id", file=sys.stderr)
            return 1

        # Get target item info
        target_item = kb_loader.get_item(target_item_id)
        if not target_item:
            print(f"Error: Target item '{target_item_id}' not found", file=sys.stderr)
            return 1

        target_dict = target_item.model_dump() if hasattr(target_item, "model_dump") else target_item
        target_name = target_dict.get("name", target_item_id)
        target_mass = target_dict.get("mass")  # None if not defined

        print(f"{'='*80}")
        print(f"PRODUCTION PLAN: {target_name}")
        print(f"{'='*80}")
        print()
        # Handle missing mass gracefully (Issue #11)
        if target_mass is not None:
            print(f"TARGET: {target_item_id} (1 unit, {target_mass:.2f} kg)")
        else:
            print(f"TARGET: {target_item_id} (1 unit, mass unknown)")
        print()

        # Build dependency tree
        print("DEPENDENCY TREE:")
        print()
        dep_tree = _build_dependency_tree(target_item_id, kb_loader, max_depth=8)
        _print_dependency_tree(dep_tree)
        print()

        # Aggregate materials
        aggregated = _aggregate_materials(dep_tree)

        # Print aggregate materials
        print("AGGREGATE MATERIALS NEEDED:")
        print()

        raw_mats = aggregated["raw_materials"]
        if raw_mats:
            print("Raw Materials (ISRU/Boundary):")
            for item_id in sorted(raw_mats.keys()):
                info = raw_mats[item_id]
                print(f"  • {item_id}: {info['qty']:.2f} {info['unit']}", end="")
                if info['mass'] > 0:
                    print(f" (~{info['mass']:.2f} kg)")
                else:
                    print()
        else:
            print("Raw Materials (ISRU/Boundary): none")
        print()

        imports = aggregated["imports"]
        if imports:
            print("Must Import or Collect:")
            for item_id in sorted(imports.keys()):
                info = imports[item_id]
                print(f"  • {item_id}: {info['qty']:.2f} {info['unit']}", end="")
                if info['mass'] > 0:
                    print(f" (~{info['mass']:.2f} kg)")
                else:
                    print()
        else:
            print("Must Import or Collect: none")
        print()

        intermediates = aggregated["intermediates"]
        if intermediates:
            print("Intermediate Materials (produced & consumed):")
            for item_id in sorted(intermediates.keys()):
                info = intermediates[item_id]
                print(f"  • {item_id}: {info['qty']:.2f} {info['unit']}", end="")
                if info['mass'] > 0:
                    print(f" (~{info['mass']:.2f} kg)")
                else:
                    print()
            print()

        # Collect machine requirements
        required = {}
        missing_steps = []

        for step in recipe_def.get("steps", []):
            resolved_step = resolve_recipe_step_with_kb(step, kb_loader)
            if "_warning" in resolved_step:
                process_id = step.get("process_id")
                if process_id:
                    missing_steps.append(process_id)
            required.update(_collect_machine_requirements(resolved_step))

        print("MACHINES REQUIRED (for this recipe's direct processes):")
        if required:
            for machine_id, detail in sorted(required.items()):
                print(f"  - {machine_id}: {detail}")
        else:
            print("  none (may need machines from sub-recipes)")
        print()

        # Show process list
        processes = aggregated["processes"]
        if processes:
            print(f"PROCESSES IN DEPENDENCY CHAIN ({len(processes)} total):")
            for i, proc_id in enumerate(processes[:20], 1):  # Limit to first 20
                print(f"  {i}. {proc_id}")
            if len(processes) > 20:
                print(f"  ... and {len(processes) - 20} more")
            print()

        # Warnings
        if missing_steps:
            print("WARNINGS:")
            print("  Missing processes:")
            for proc_id in sorted(missing_steps):
                print(f"    - {proc_id}")
            print()

        print("NOTE: Time/energy calculations require simulation execution")
        print(f"{'='*80}")
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
    snapshot_file = sim_dir / "snapshot.json"
    if snapshot_file.exists():
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
    print(f"  Snapshot: {engine.snapshot_file}")
    print(f"  Events: {engine.event_log_file}")
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
        components = result.get('components_consumed', {})
        print(f"  Parts consumed: {len(components)}")
        for item_id, qty_str in components.items():
            print(f"    - {item_id}: {qty_str}")
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
                output_units = {}
                process_model = kb_loader.get_process(proc["process_id"])
                if process_model:
                    process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
                    for outp in process_def.get("outputs", []):
                        output_units[outp.get("item_id")] = outp.get("unit", "unit")
                for item_id, inv_item in proc['outputs'].items():
                    if isinstance(inv_item, (int, float)):
                        qty = float(inv_item)
                        unit = output_units.get(item_id, "unit")
                    else:
                        qty = inv_item.quantity if hasattr(inv_item, 'quantity') else inv_item['quantity']
                        unit = inv_item.unit if hasattr(inv_item, 'unit') else inv_item['unit']
                    print(f"      → {item_id}: {qty:.2f} {unit}")

    engine.save()
    return 0


def cmd_status(args, kb_loader: KBLoader):
    """Show simulation metadata summary."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)
    state = engine.get_state_dict()
    schedule = engine.get_schedule_summary()
    converter = UnitConverter(kb_loader)

    def summarize_mass(
        items: Dict[str, Dict[str, Any]]
    ) -> tuple[float, int]:
        total_mass = 0.0
        unknown_mass_count = 0
        for item_id, inv in items.items():
            qty = inv.get("quantity", 0.0)
            unit = inv.get("unit")
            if unit == "kg":
                total_mass += qty
                continue
            converted = converter.convert(qty, unit, "kg", item_id)
            if converted is not None:
                total_mass += converted
                continue
            item = kb_loader.get_item(item_id)
            if item:
                item_dict = item.model_dump() if hasattr(item, "model_dump") else item
                item_mass = item_dict.get("mass")
                if item_mass is not None and unit in ("unit", "count"):
                    total_mass += item_mass * qty
                    continue
            unknown_mass_count += 1
        return total_mass, unknown_mass_count

    def summarize_volume(
        items: Dict[str, Dict[str, Any]]
    ) -> tuple[float, int]:
        total_volume = 0.0
        unknown_volume_count = 0
        for item_id, inv in items.items():
            qty = inv.get("quantity", 0.0)
            unit = inv.get("unit")
            if unit in ("m3", "liter", "L"):
                converted = converter.convert(qty, unit, "m3", item_id)
                if converted is not None:
                    total_volume += converted
                else:
                    unknown_volume_count += 1
            else:
                converted = converter.convert(qty, unit, "m3", item_id)
                if converted is not None:
                    total_volume += converted
        return total_volume, unknown_volume_count

    time_hours = state.get("current_time_hours", 0.0)
    days = time_hours / 24.0
    total_energy = state.get("total_energy_kwh", 0.0)

    inventory_count = len(state.get("inventory", {}))
    machines_built_count = len(state.get("machines_built", []))
    imports_count = len(state.get("total_imports", {}))

    import_mass, import_unknown_mass = summarize_mass(state.get("total_imports", {}))
    inventory_mass, inventory_unknown_mass = summarize_mass(state.get("inventory", {}))
    inventory_volume, inventory_unknown_volume = summarize_volume(state.get("inventory", {}))
    inventory_unit_total = 0.0
    for inv in state.get("inventory", {}).values():
        if inv.get("unit") in ("unit", "count"):
            inventory_unit_total += inv.get("quantity", 0.0)

    active_processes = schedule.get("active_processes", len(state.get("active_processes", [])))
    completed_processes = schedule.get("completed_processes", 0)
    queued_events = schedule.get("queued_events", 0)
    active_recipes = schedule.get("active_recipes", 0)
    completed_recipes = schedule.get("completed_recipes", 0)
    next_event_time = schedule.get("next_event_time")

    print(f"=== Simulation: {args.sim_id} ===")
    print(f"Time: {time_hours:.2f} hours ({days:.2f} days)")
    print(f"Energy: {total_energy:.2f} kWh")
    print(f"Inventory items: {inventory_count}")
    print(f"Machines built: {machines_built_count}")
    print(f"Imports tracked: {imports_count}")
    if import_unknown_mass > 0:
        print(f"Imported mass: ~{import_mass:.2f} kg ({import_unknown_mass} unknown)")
    else:
        print(f"Imported mass: ~{import_mass:.2f} kg")
    if inventory_unknown_mass > 0:
        print(f"Inventory mass: ~{inventory_mass:.2f} kg ({inventory_unknown_mass} unknown)")
    else:
        print(f"Inventory mass: ~{inventory_mass:.2f} kg")
    if inventory_volume > 0 or inventory_unknown_volume > 0:
        if inventory_unknown_volume > 0:
            print(f"Inventory volume: ~{inventory_volume:.3f} m3 ({inventory_unknown_volume} unknown)")
        else:
            print(f"Inventory volume: ~{inventory_volume:.3f} m3")
    if inventory_unit_total > 0:
        print(f"Inventory count: ~{inventory_unit_total:.2f} units")
    print(f"Processes: {active_processes} active, {completed_processes} completed")
    print(f"Recipes: {active_recipes} active, {completed_recipes} completed")
    print(f"Events queued: {queued_events}")
    if next_event_time is None:
        print("Next event time: none")
    else:
        print(f"Next event time: {next_event_time:.2f} hours")
    print(f"Snapshot: {engine.snapshot_file}")
    print(f"Events: {engine.event_log_file}")

    return 0


def cmd_list(args, kb_loader: KBLoader):
    """List all simulations."""
    if not SIMULATIONS_DIR.exists():
        print("No simulations found")
        return 0

    sims = []
    for sim_dir in SIMULATIONS_DIR.iterdir():
        if sim_dir.is_dir():
            snapshot_file = sim_dir / "snapshot.json"
            if snapshot_file.exists():
                sim_time = None
                try:
                    snapshot_data = json.loads(snapshot_file.read_text(encoding="utf-8"))
                    sim_time = snapshot_data.get("state", {}).get("current_time_hours")
                except Exception:
                    sim_time = None
                sims.append({
                    'id': sim_dir.name,
                    'time_hours': sim_time,
                    'path': str(sim_dir)
                })

    if not sims:
        print("No simulations found")
        return 0

    print(f"Found {len(sims)} simulation(s):\n")
    for sim in sorted(sims, key=lambda x: x['id']):
        print(f"  {sim['id']}")
        if sim.get('time_hours') is not None:
            days = sim['time_hours'] / 24.0
            print(f"    Sim time: {sim['time_hours']:.2f} hours ({days:.2f} days)")
        print(f"    Path: {sim['path']}")
        print()

    return 0


def cmd_visualize(args, kb_loader: KBLoader):
    """Generate visualizations for a simulation."""
    from src.simulation.visualize import visualize_simulation
    import os

    sim_dir = SIMULATIONS_DIR / args.sim_id
    log_file = sim_dir / "events.jsonl"

    if not log_file.exists():
        print(f"Error: Simulation '{args.sim_id}' not found", file=sys.stderr)
        return 1

    try:
        if "MPLCONFIGDIR" not in os.environ:
            print(
                "Note: set MPLCONFIGDIR to a writable path if Matplotlib cache errors occur.",
                file=sys.stderr,
            )
        # Determine output directory
        output_dir = None
        if hasattr(args, 'output') and args.output:
            output_dir = Path(args.output)

        # Generate visualizations
        visualize_simulation(sim_dir, output_dir)
        return 0

    except Exception as e:
        print(f"Error generating visualizations: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


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

    # status
    status_parser = sim_subparsers.add_parser('status', help='Show simulation metadata')
    status_parser.add_argument('--sim-id', required=True, help='Simulation ID')

    # list
    list_parser = sim_subparsers.add_parser('list', help='List all simulations')

    # visualize
    visualize_parser = sim_subparsers.add_parser('visualize', help='Generate visualizations')
    visualize_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    visualize_parser.add_argument('--output', help='Output directory for plots (default: sim_dir/plots)')

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
        'status': cmd_status,
        'list': cmd_list,
        'visualize': cmd_visualize,
    }

    handler = commands.get(args.sim_command)
    if not handler:
        print(f"Error: Unknown simulation command '{args.sim_command}'", file=sys.stderr)
        return 1

    return handler(args, kb_loader)
