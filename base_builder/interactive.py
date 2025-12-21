"""
Interactive mode for base builder - Claude controls the simulation.

This module provides tools that Claude can use directly in conversation
to control a simulation.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional, Dict, Any

from base_builder.kb_loader import KBLoader
from base_builder.sim_engine import SimulationEngine

# Global state
_current_sim: Optional[SimulationEngine] = None
_kb: Optional[KBLoader] = None

REPO_ROOT = Path(__file__).parent.parent
KB_ROOT = REPO_ROOT / "kb"
SIMULATIONS_DIR = REPO_ROOT / "simulations"


def init_simulation(sim_id: str) -> Dict[str, Any]:
    """
    Initialize or load a simulation.

    Args:
        sim_id: Simulation ID

    Returns:
        Status dict with simulation info
    """
    global _current_sim, _kb

    # Load KB if not already loaded
    if _kb is None:
        print("Loading knowledge base...")
        _kb = KBLoader(KB_ROOT)
        _kb.load_all()
        print(f"✓ Loaded: {len(_kb.processes)} processes, {len(_kb.recipes)} recipes, "
              f"{len(_kb.items)} items, {len(_kb.boms)} BOMs")

    # Create or load simulation
    sim_dir = SIMULATIONS_DIR / sim_id
    _current_sim = SimulationEngine(sim_id, _kb, sim_dir)

    # Try to load existing state
    loaded = _current_sim.load()

    if loaded:
        return {
            "status": "loaded",
            "sim_id": sim_id,
            "current_time_hours": _current_sim.state.current_time_hours,
            "inventory_items": len(_current_sim.state.inventory),
            "active_processes": len(_current_sim.state.active_processes),
            "machines_built": len(_current_sim.state.machines_built),
            "total_imports": len(_current_sim.state.total_imports),
        }
    else:
        return {
            "status": "new",
            "sim_id": sim_id,
            "current_time_hours": 0,
            "inventory_items": 0,
            "active_processes": 0,
            "machines_built": 0,
            "total_imports": 0,
        }


def view_state() -> Dict[str, Any]:
    """
    View current simulation state.

    Returns:
        Current state dict
    """
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    inventory_summary = {}
    for item_id, inv_item in _current_sim.state.inventory.items():
        inventory_summary[item_id] = f"{inv_item.quantity} {inv_item.unit}"

    imports_summary = {}
    total_imports_mass = 0.0
    for item_id, inv_item in _current_sim.state.total_imports.items():
        imports_summary[item_id] = f"{inv_item.quantity} {inv_item.unit}"
        # Estimate mass
        if inv_item.unit == "kg":
            total_imports_mass += inv_item.quantity

    active_procs = []
    for proc in _current_sim.state.active_processes:
        active_procs.append({
            "process_id": proc.process_id,
            "started_at": proc.started_at,
            "ends_at": proc.ends_at,
            "time_remaining_hours": proc.ends_at - _current_sim.state.current_time_hours,
        })

    return {
        "current_time_hours": _current_sim.state.current_time_hours,
        "inventory": inventory_summary,
        "active_processes": active_procs,
        "machines_built": _current_sim.state.machines_built,
        "total_imports": imports_summary,
        "total_imports_mass_kg": total_imports_mass,
    }


def start_process(process_id: str, scale: float, duration_hours: float) -> Dict[str, Any]:
    """Start a process."""
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    result = _current_sim.start_process(process_id, scale, duration_hours)
    _current_sim.save()  # Persist state
    return result


def run_recipe(recipe_id: str, quantity: int) -> Dict[str, Any]:
    """Run a recipe."""
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    result = _current_sim.run_recipe(recipe_id, quantity)
    _current_sim.save()  # Persist state
    return result


def build_machine(machine_id: str) -> Dict[str, Any]:
    """Build a machine from BOM."""
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    result = _current_sim.build_machine(machine_id)
    _current_sim.save()  # Persist state
    return result


def import_item(item_id: str, quantity: float, unit: str) -> Dict[str, Any]:
    """Import item from Earth (minimize!)."""
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    result = _current_sim.import_item(item_id, quantity, unit)
    _current_sim.save()  # Persist state
    return result


def preview_step(duration_hours: float) -> Dict[str, Any]:
    """Preview what would happen if time advanced."""
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    return _current_sim.preview_step(duration_hours)


def advance_time(duration_hours: float) -> Dict[str, Any]:
    """Advance simulation time."""
    if _current_sim is None:
        return {"error": "No simulation active. Call init_simulation(sim_id) first."}

    return _current_sim.advance_time(duration_hours)


def get_kb_stats() -> Dict[str, Any]:
    """Get KB statistics."""
    if _kb is None:
        return {"error": "KB not loaded. Call init_simulation(sim_id) first."}

    return {
        "processes": len(_kb.processes),
        "recipes": len(_kb.recipes),
        "items": len(_kb.items),
        "boms": len(_kb.boms),
        "load_errors": len(_kb.load_errors),
    }


# Export functions for easy import
__all__ = [
    "init_simulation",
    "view_state",
    "start_process",
    "run_recipe",
    "build_machine",
    "import_item",
    "preview_step",
    "advance_time",
    "get_kb_stats",
]
