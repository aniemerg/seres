"""
Simulation tools for the base builder agent.

Tools defined with @function_tool decorator from openai-agents library.
"""
from __future__ import annotations

from typing import Dict, Any, Optional
from agents import function_tool

# Import KB tools from queue_agents
from queue_agents.kb_tools import rg_search, read_file, write_file

# Global engine instance (set by agent runner)
_engine: Optional[Any] = None


@function_tool
def view_state() -> Dict[str, Any]:
    """
    Get current simulation state.

    Returns:
        {
            "current_time_hours": float,
            "inventory": {item_id: "quantity unit", ...},
            "active_processes": [{process_id, ends_at, ...}, ...],
            "machines_built": [machine_id, ...],
            "total_imports": {item_id: "quantity unit", ...},
            "total_imports_mass_kg": float (estimated)
        }
    """
    if _engine is None:
        return {"error": "Simulation engine not initialized"}

    state = _engine.get_state_dict()

    # Format inventory for readability
    inventory_summary = {}
    for item_id, inv_item in state["inventory"].items():
        inventory_summary[item_id] = f"{inv_item['quantity']} {inv_item['unit']}"

    # Format imports
    imports_summary = {}
    total_imports_mass = 0.0
    for item_id, inv_item in state["total_imports"].items():
        imports_summary[item_id] = f"{inv_item['quantity']} {inv_item['unit']}"
        # Try to estimate mass
        if inv_item["unit"] == "kg":
            total_imports_mass += inv_item["quantity"]

    # Format active processes
    active_procs = []
    for proc in state["active_processes"]:
        active_procs.append({
            "process_id": proc["process_id"],
            "started_at": proc["started_at"],
            "ends_at": proc["ends_at"],
            "time_remaining_hours": proc["ends_at"] - state["current_time_hours"],
        })

    return {
        "current_time_hours": state["current_time_hours"],
        "inventory": inventory_summary,
        "inventory_item_count": len(inventory_summary),
        "active_processes": active_procs,
        "active_processes_count": len(active_procs),
        "machines_built": state["machines_built"],
        "machines_built_count": len(state["machines_built"]),
        "total_imports": imports_summary,
        "total_imports_mass_kg_estimated": total_imports_mass,
    }


@function_tool
def start_process(
    process_id: str, scale: float, duration_hours: float
) -> Dict[str, Any]:
    """
    Start a process.

    Processes convert inputs to outputs over time. They require machines
    (not consumed) and consume input materials.

    Special: Regolith collection doesn't consume inputs (it's free/infinite).

    Args:
        process_id: Process to run (e.g., "regolith_mining_v0")
        scale: Scale factor for inputs/outputs (1.0 = base rate, 2.0 = double)
        duration_hours: How long to run the process

    Returns:
        {
            "success": bool,
            "message": str,
            "ends_at": float (simulation time when complete),
            ...
        }

    Errors:
        - missing_process: Process not defined in KB
        - missing_machine: Required machine not available
        - insufficient_inputs: Not enough input materials
    """
    if _engine is None:
        return {"success": False, "error": "Simulation engine not initialized"}

    return _engine.start_process(process_id, scale, duration_hours)


@function_tool
def run_recipe(recipe_id: str, quantity: int) -> Dict[str, Any]:
    """
    Run a recipe to produce items.

    Recipes define how to make parts/items from materials. They specify
    inputs, outputs, and duration per batch.

    Args:
        recipe_id: Recipe to run (e.g., "recipe_steel_ingot_v0")
        quantity: Number of batches to produce

    Returns:
        {
            "success": bool,
            "message": str,
            "duration_hours": float (total time for all batches),
            "ends_at": float (simulation time when complete),
            ...
        }

    Errors:
        - missing_recipe: Recipe not defined in KB
        - missing_machine: Required machine not available
        - insufficient_inputs: Not enough input materials
    """
    if _engine is None:
        return {"success": False, "error": "Simulation engine not initialized"}

    return _engine.run_recipe(recipe_id, quantity)


@function_tool
def build_machine(machine_id: str) -> Dict[str, Any]:
    """
    Build a machine from its Bill of Materials (BOM).

    Machines are built from component parts. Once built, they can be used
    by processes/recipes (as required_machines).

    This consumes all BOM components from inventory.

    Args:
        machine_id: Machine to build (e.g., "labor_bot_general_v0")

    Returns:
        {
            "success": bool,
            "message": str,
            "components_consumed": {item_id: "quantity unit", ...},
            ...
        }

    Errors:
        - missing_bom: BOM not defined in KB
        - insufficient_components: Missing required parts
    """
    if _engine is None:
        return {"success": False, "error": "Simulation engine not initialized"}

    return _engine.build_machine(machine_id)


@function_tool
def import_item(item_id: str, quantity: float, unit: str) -> Dict[str, Any]:
    """
    Import an item from Earth.

    WARNING: Imports are a FAILURE MODE in this simulation!

    The goal is to build using IN SITU resources (local regolith).
    Only import when:
    1. No local alternative exists AND
    2. KB is incomplete (in which case, delegate to kb_fixer first)

    Imports are tracked separately and count against mission success.

    Args:
        item_id: Item to import (e.g., "labor_bot_general_v0")
        quantity: Amount to import
        unit: Unit of quantity (e.g., "count", "kg")

    Returns:
        {
            "success": bool,
            "message": str,
            "imported": {
                "item_id": str,
                "quantity": float,
                "unit": str,
                "mass_kg": float (estimated)
            },
            ...
        }

    Errors:
        - missing_item: Item not defined in KB
    """
    if _engine is None:
        return {"success": False, "error": "Simulation engine not initialized"}

    return _engine.import_item(item_id, quantity, unit)


@function_tool
def preview_step(duration_hours: float) -> Dict[str, Any]:
    """
    Preview what would happen if time advanced.

    Does NOT commit changes. Use this before advance_time() to check:
    - Which processes will complete
    - What outputs they'll produce
    - If there are any issues

    Args:
        duration_hours: How much time to preview

    Returns:
        {
            "new_time": float,
            "processes_completing": [
                {
                    "process_id": str,
                    "ends_at": float,
                    "outputs": {item_id: {"quantity": float, "unit": str}}
                },
                ...
            ],
            "completing_count": int,
            "active_processes_count": int
        }
    """
    if _engine is None:
        return {"error": "Simulation engine not initialized"}

    return _engine.preview_step(duration_hours)


@function_tool
def advance_time(duration_hours: float) -> Dict[str, Any]:
    """
    Advance simulation time.

    COMMITS changes - processes complete, inventory updates, time advances.

    Always use preview_step() first to check what will happen!

    Steps:
    1. All processes ending <= new_time complete
    2. Their outputs are added to inventory
    3. Completed processes removed from active list
    4. Current time updated
    5. State saved to disk

    Args:
        duration_hours: How much time to advance

    Returns:
        {
            "new_time": float,
            "completed": [
                {
                    "process_id": str,
                    "ended_at": float,
                    "outputs": {item_id: {"quantity": float, "unit": str}}
                },
                ...
            ],
            "completed_count": int,
            "active_processes_remaining": int,
            "new_inventory": {item_id: "quantity unit", ...}
        }
    """
    if _engine is None:
        return {"error": "Simulation engine not initialized"}

    return _engine.advance_time(duration_hours)


# Export KB tools for agent use
__all__ = [
    "view_state",
    "start_process",
    "run_recipe",
    "build_machine",
    "import_item",
    "preview_step",
    "advance_time",
    "rg_search",
    "read_file",
    "write_file",
]
