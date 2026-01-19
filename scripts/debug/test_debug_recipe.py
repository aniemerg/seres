"""
Debug script to trace multi-step recipe execution with full logging.
"""
import logging
import sys
from pathlib import Path

# Set up logging BEFORE importing engine
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s [%(name)s] %(message)s',
    stream=sys.stdout
)

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine

def test_recipe_with_debug():
    print("=" * 80)
    print("Starting debug trace of multi-step recipe")
    print("=" * 80)

    # Load KB
    print("\nLoading KB...")
    kb = KBLoader(Path('kb'))
    kb.load_all()

    # Create simulation
    print("\nCreating simulation...")
    engine = SimulationEngine(kb_loader=kb, sim_id="test_recipe_debug")

    # Import required resources
    print("\nImporting resources...")
    engine.import_item("regolith_lunar_mare", 4000, "kg")
    engine.import_item("magnetic_separator_drum_v0", 1, "unit")
    engine.import_item("vibratory_feeder_v0", 1, "unit")
    engine.import_item("furnace_high_temp", 1, "unit")
    engine.import_item("crucible_graphite", 1, "unit")
    engine.import_item("chemical_separation_equipment", 1, "unit")
    engine.import_item("labor_bot_general_v0", 3, "unit")
    engine.import_item("electrical_energy", 500, "kWh")

    # Run the 2-step nickel extraction recipe
    print("\n" + "=" * 80)
    print("Running recipe...")
    print("=" * 80)
    result = engine.run_recipe("recipe_nickel_metal_from_regolith_v0", quantity=1)

    if not result["success"]:
        print(f"ERROR: Recipe failed to start: {result.get('message')}")
        return

    recipe_run_id = result["recipe_run_id"]
    print(f"Recipe started with run_id: {recipe_run_id}")

    # Check initial state
    progress = engine.orchestrator.get_recipe_progress(recipe_run_id)
    print(f"\nInitial state:")
    print(f"  Scheduled steps: {progress['scheduled_steps']}")
    print(f"  Active steps: {progress['active_steps']}")
    print(f"  Completed steps: {progress['completed_steps']}")

    # Advance time to let first step complete (it should take ~100 hours)
    print("\n" + "=" * 80)
    print("FIRST ADVANCE: 150 hours")
    print("=" * 80)
    engine.advance_time(150)

    # Check state after first advance
    progress = engine.orchestrator.get_recipe_progress(recipe_run_id)
    recipe_run = engine.orchestrator.get_recipe_run(recipe_run_id)
    print(f"\nAfter 150 hours:")
    print(f"  Completed steps: {progress['completed_steps']}")
    print(f"  Active steps: {progress['active_steps']}")
    print(f"  Scheduled steps: {progress['scheduled_steps']}")
    print(f"  Recipe run - completed_steps set: {recipe_run.completed_steps}")
    print(f"  Recipe run - scheduled_steps dict: {recipe_run.scheduled_steps}")

    # Advance again to let second step complete
    print("\n" + "=" * 80)
    print("SECOND ADVANCE: 500 hours")
    print("=" * 80)
    engine.advance_time(500)

    # Check final state
    progress = engine.orchestrator.get_recipe_progress(recipe_run_id)
    print(f"\nAfter 650 total hours:")
    print(f"  Completed steps: {progress['completed_steps']}")
    print(f"  Active steps: {progress['active_steps']}")
    print(f"  Scheduled steps: {progress['scheduled_steps']}")
    print(f"  Is complete: {progress['is_completed']}")

    # Check inventory
    if "nickel_metal" in engine.state.inventory:
        nickel_qty = engine.state.inventory["nickel_metal"].quantity
        print(f"\nNickel metal in inventory: {nickel_qty} kg")
    else:
        print("\nNo nickel_metal in inventory!")

    print("\n" + "=" * 80)
    print("Debug trace complete")
    print("=" * 80)

if __name__ == "__main__":
    test_recipe_with_debug()
