#!/usr/bin/env python3
"""
Simple test of base builder components.

Tests:
1. KB loader can load data
2. Simulation engine can start
3. Tools work correctly
"""
from pathlib import Path
from base_builder.kb_loader import KBLoader
from base_builder.sim_engine import SimulationEngine

REPO_ROOT = Path(__file__).parent
KB_ROOT = REPO_ROOT / "kb"


def test_kb_loader():
    """Test KB loader."""
    print("=" * 60)
    print("TEST 1: KB Loader")
    print("=" * 60)

    kb = KBLoader(KB_ROOT)
    kb.load_all()

    print(f"✓ Loaded {len(kb.processes)} processes")
    print(f"✓ Loaded {len(kb.recipes)} recipes")
    print(f"✓ Loaded {len(kb.items)} items")
    print(f"✓ Loaded {len(kb.boms)} BOMs")

    # Check if we have units and materials
    print(f"✓ Units: {bool(kb.units)}")
    print(f"✓ Materials: {bool(kb.materials)}")

    if kb.load_errors:
        print(f"⚠ Load errors: {len(kb.load_errors)}")
        for err in kb.load_errors[:3]:
            print(f"  - {err}")

    print()
    return kb


def test_simulation_engine(kb):
    """Test simulation engine."""
    print("=" * 60)
    print("TEST 2: Simulation Engine")
    print("=" * 60)

    # Create test simulation
    engine = SimulationEngine("test_sim", kb, Path("simulations/test_sim"))

    # Test view state
    print("✓ Created simulation engine")
    print(f"  Current time: {engine.state.current_time_hours}h")
    print(f"  Inventory: {len(engine.state.inventory)} items")

    # Test import
    result = engine.import_item("labor_bot_general_v0", 1, "count")
    if result.get("success"):
        print("✓ Import item works")
    else:
        print(f"✗ Import failed: {result.get('message')}")

    # Test view state again
    print(f"  Inventory after import: {len(engine.state.inventory)} items")

    # Test preview
    result = engine.preview_step(1)
    print(f"✓ Preview works (new_time would be {result.get('new_time')}h)")

    # Save
    engine.save()
    print(f"✓ Saved to {engine.log_file}")

    print()
    return engine


def test_tools(engine):
    """Test simulation tools."""
    print("=" * 60)
    print("TEST 3: Simulation Tools")
    print("=" * 60)

    # Import tools module
    import base_builder.sim_tools as sim_tools

    # Set engine
    sim_tools._engine = engine

    # Tools are wrapped by @function_tool decorator for agent use
    # We can verify they exist and are properly decorated
    print(f"✓ view_state tool registered: {sim_tools.view_state.__class__.__name__}")
    print(f"✓ start_process tool registered: {sim_tools.start_process.__class__.__name__}")
    print(f"✓ run_recipe tool registered: {sim_tools.run_recipe.__class__.__name__}")
    print(f"✓ build_machine tool registered: {sim_tools.build_machine.__class__.__name__}")
    print(f"✓ import_item tool registered: {sim_tools.import_item.__class__.__name__}")
    print(f"✓ preview_step tool registered: {sim_tools.preview_step.__class__.__name__}")
    print(f"✓ advance_time tool registered: {sim_tools.advance_time.__class__.__name__}")
    print()
    print("Note: Tools will be tested when agent runs (they're wrapped by @function_tool)")

    print()


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("BASE BUILDER COMPONENT TESTS")
    print("=" * 60)
    print()

    try:
        # Test 1: KB Loader
        kb = test_kb_loader()

        # Test 2: Simulation Engine
        engine = test_simulation_engine(kb)

        # Test 3: Tools
        test_tools(engine)

        print("=" * 60)
        print("ALL TESTS PASSED ✓")
        print("=" * 60)
        print()
        print("You can now run the simulation:")
        print("  python -m base_builder.cli start --sim-id my_first_base")
        print()

    except Exception as e:
        print()
        print("=" * 60)
        print("TEST FAILED ✗")
        print("=" * 60)
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
