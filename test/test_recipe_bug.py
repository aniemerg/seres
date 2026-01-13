"""
Test to reproduce the multi-step recipe bug.

This test creates a simple 2-step recipe and verifies that both steps execute.
"""
import pytest
from pathlib import Path
from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


def test_two_step_recipe_completes():
    """
    Test that a 2-step recipe completes both steps.

    This is a failing test that reproduces the bug where the second step
    of a multi-step recipe never executes.
    """
    # Load KB
    kb = KBLoader(Path('kb'))
    kb.load_all()

    # Create simulation
    engine = SimulationEngine(kb_loader=kb, sim_id="test_recipe_bug")

    # Import required resources
    engine.import_item("regolith_lunar_mare", 4000, "kg")
    engine.import_item("magnetic_separator_drum_v0", 1, "unit")
    engine.import_item("vibratory_feeder_v0", 1, "unit")
    engine.import_item("furnace_high_temp", 1, "unit")
    engine.import_item("crucible_graphite", 1, "unit")
    engine.import_item("chemical_separation_equipment", 1, "unit")
    engine.import_item("labor_bot_general_v0", 3, "unit")
    engine.import_item("electrical_energy", 500, "kWh")

    # Run the 2-step nickel extraction recipe
    result = engine.run_recipe("recipe_nickel_metal_from_regolith_v0", quantity=1)

    assert result["success"], f"Recipe failed to start: {result.get('message')}"

    recipe_run_id = result["recipe_run_id"]

    # Advance time to let the first step complete and second step start
    # Step 0 completes at 1.0 hours, Step 1 starts at 1.0 and completes at 41.0 hours
    engine.advance_time(20)

    # Check recipe progress after first step
    progress1 = engine.orchestrator.get_recipe_progress(recipe_run_id)
    print(f"\nProgress after 20 hours:")
    print(f"  Total steps: {progress1['total_steps']}")
    print(f"  Completed: {progress1['completed_steps']}")
    print(f"  Active: {progress1['active_steps']}")
    print(f"  Scheduled: {progress1['scheduled_steps']}")
    print(f"  Is complete: {progress1['is_completed']}")

    # Get the recipe run to inspect state
    recipe_run = engine.orchestrator.get_recipe_run(recipe_run_id)
    print(f"\nRecipe run state:")
    print(f"  Completed steps: {recipe_run.completed_steps}")
    print(f"  Active steps: {recipe_run.active_steps}")
    print(f"  Scheduled steps: {recipe_run.scheduled_steps}")

    # Check what steps are ready
    ready_steps = engine.orchestrator.get_ready_steps(recipe_run_id)
    print(f"  Ready steps: {ready_steps}")

    # Check dependency graph
    print(f"\nDependency graph:")
    for i, node in enumerate(recipe_run.dependency_graph.nodes):
        status = engine.orchestrator.get_step_status(recipe_run_id, i)
        print(f"  Step {i}: {node.process_id}")
        print(f"    Dependencies: {node.dependencies}")
        print(f"    Status: {status}")

    # First step should be completed
    assert 0 in recipe_run.completed_steps, "Step 0 (beneficiate) should be completed"

    # Second step should be active or scheduled or completed
    # With the fix, step 1 starts at 1.0, so by 20 hours it should be active
    assert 1 in recipe_run.active_steps or 1 in recipe_run.scheduled_steps or 1 in recipe_run.completed_steps, \
        "Step 1 (nickel_extraction) should be scheduled, active, or completed after step 0 completes"

    # Advance more time to let second step complete (completes at 41 hours)
    engine.advance_time(30)

    # Check final progress
    progress2 = engine.orchestrator.get_recipe_progress(recipe_run_id)
    print(f"\nProgress after 50 total hours:")
    print(f"  Total steps: {progress2['total_steps']}")
    print(f"  Completed: {progress2['completed_steps']}")
    print(f"  Active: {progress2['active_steps']}")
    print(f"  Scheduled: {progress2['scheduled_steps']}")
    print(f"  Is complete: {progress2['is_completed']}")

    # Check inventory for nickel_metal (output of step 2)
    if "nickel_metal" in engine.state.inventory:
        nickel_item = engine.state.inventory["nickel_metal"]
        nickel_qty = nickel_item.quantity
    else:
        nickel_qty = 0
    print(f"\nNickel metal in inventory: {nickel_qty} kg")

    # Both steps should be completed
    assert progress2['completed_steps'] == 2, \
        f"Expected 2 completed steps, got {progress2['completed_steps']}"

    # Recipe should be complete
    assert progress2['is_completed'], "Recipe should be marked as complete"

    # Should have nickel_metal in inventory
    assert nickel_qty > 0, "Should have nickel_metal in inventory after recipe completes"


if __name__ == "__main__":
    test_two_step_recipe_completes()
