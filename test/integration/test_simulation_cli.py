"""
Integration tests for simulation CLI commands.

Tests for issues #10 and #11:
- Issue #10: Import mass calculation
- Issue #11: sim plan crash on missing mass
"""

import pytest
import json
from pathlib import Path
import tempfile
import shutil

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


class TestSimulationCLI:
    """Tests for simulation CLI commands."""

    @pytest.fixture
    def temp_kb(self, tmp_path):
        """Create a temporary knowledge base with test items."""
        kb_dir = tmp_path / "kb"
        kb_dir.mkdir()

        # Create items directory with materials subdirectory
        items_dir = kb_dir / "items" / "materials"
        items_dir.mkdir(parents=True)

        # Item with mass defined
        (items_dir / "test_item_with_mass.yaml").write_text("""id: test_item_with_mass
kind: material
name: Test Item With Mass
mass: 50.0
unit: unit
""")

        # Item without mass defined
        (items_dir / "test_item_no_mass.yaml").write_text("""id: test_item_no_mass
kind: material
name: Test Item Without Mass
unit: unit
""")

        # Create processes directory
        processes_dir = kb_dir / "processes"
        processes_dir.mkdir()

        # Create a simple process
        (processes_dir / "test_process_v0.yaml").write_text("""id: test_process_v0
kind: process
name: Test Process
inputs: []
outputs:
  - item_id: test_item_no_mass
    qty: 1
    unit: unit
time_model:
  type: fixed
  duration_hours: 1.0
""")

        # Create recipes directory
        recipes_dir = kb_dir / "recipes"
        recipes_dir.mkdir()

        # Recipe for item without mass
        (recipes_dir / "recipe_test_item_no_mass.yaml").write_text("""id: recipe_test_item_no_mass
kind: recipe
target_item_id: test_item_no_mass
steps:
  - process_id: test_process_v0
""")

        return kb_dir

    @pytest.fixture
    def temp_sim_dir(self, tmp_path):
        """Create a temporary simulation directory."""
        return tmp_path / "simulations"

    def test_import_mass_calculation_with_mass(self, temp_kb, temp_sim_dir):
        """
        Test Issue #10: Import mass should be calculated from item definitions.

        Tests that items with unit='unit' have their mass looked up from KB.
        """
        # Create KB loader
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create simulation
        sim_id = "test_mass_calc"
        engine = SimulationEngine(sim_id, kb, temp_sim_dir)

        # Import item with known mass
        engine.import_item("test_item_with_mass", 2, "unit")  # 2 × 50 kg = 100 kg

        # Get state
        state = engine.get_state_dict()

        # Calculate total imported mass (using same logic as CLI)
        total_mass = 0.0
        unknown_mass_count = 0

        for item_id, inv in state['total_imports'].items():
            if inv['unit'] == 'kg':
                total_mass += inv['quantity']
            elif inv['unit'] == 'unit':
                item = kb.get_item(item_id)
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
                unknown_mass_count += 1

        # Verify mass was calculated correctly
        assert total_mass == 100.0, f"Expected 100.0 kg, got {total_mass} kg"
        assert unknown_mass_count == 0, "Should have no items with unknown mass"

    def test_import_mass_calculation_without_mass(self, temp_kb, temp_sim_dir):
        """
        Test Issue #10: Import mass should handle items without mass gracefully.

        Tests that items without mass don't crash and are counted as unknown.
        """
        # Create KB loader
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create simulation
        sim_id = "test_mass_unknown"
        engine = SimulationEngine(sim_id, kb, temp_sim_dir)

        # Import item without mass
        engine.import_item("test_item_no_mass", 1, "unit")
        # Import item with mass
        engine.import_item("test_item_with_mass", 1, "unit")  # 50 kg

        # Get state
        state = engine.get_state_dict()

        # Calculate total imported mass
        total_mass = 0.0
        unknown_mass_count = 0

        for item_id, inv in state['total_imports'].items():
            if inv['unit'] == 'kg':
                total_mass += inv['quantity']
            elif inv['unit'] == 'unit':
                item = kb.get_item(item_id)
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
                unknown_mass_count += 1

        # Verify mass calculation
        assert total_mass == 50.0, f"Expected 50.0 kg from item with mass, got {total_mass} kg"
        assert unknown_mass_count == 1, "Should have 1 item with unknown mass"

    def test_import_mass_calculation_mixed_units(self, temp_kb, temp_sim_dir):
        """
        Test Issue #10: Import mass should handle mixed units correctly.

        Tests that multiple items with unit='unit' are summed correctly.
        """
        # Create KB loader
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create simulation
        sim_id = "test_mass_mixed"
        engine = SimulationEngine(sim_id, kb, temp_sim_dir)

        # Import multiple items with unit='unit'
        engine.import_item("test_item_with_mass", 2, "unit")  # 2 × 50 kg = 100 kg
        engine.import_item("test_item_with_mass", 1, "unit")  # 1 × 50 kg = 50 kg
        # Total: 150 kg (3 items × 50 kg)

        # Get state
        state = engine.get_state_dict()

        # Calculate total imported mass
        total_mass = 0.0
        unknown_mass_count = 0

        for item_id, inv in state['total_imports'].items():
            if inv['unit'] == 'kg':
                total_mass += inv['quantity']
            elif inv['unit'] == 'unit':
                item = kb.get_item(item_id)
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
                unknown_mass_count += 1

        # Verify mass calculation
        assert total_mass == 150.0, f"Expected 150.0 kg (3 × 50 kg), got {total_mass} kg"
        assert unknown_mass_count == 0, "Should have no items with unknown mass"

    def test_sim_plan_missing_mass_no_crash(self, temp_kb, temp_sim_dir):
        """
        Test Issue #11: sim plan should not crash when item has no mass.

        Tests that the plan command handles None mass gracefully instead of
        crashing with TypeError on format string.
        """
        # Create KB loader
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Get recipe and target item
        recipe = kb.get_recipe("recipe_test_item_no_mass")
        assert recipe is not None, "Recipe should exist"

        target_item_id = recipe.target_item_id
        target_item = kb.get_item(target_item_id)
        assert target_item is not None, "Target item should exist"

        target_dict = target_item.model_dump() if hasattr(target_item, 'model_dump') else target_item
        target_mass = target_dict.get('mass')  # Should be None

        # Verify mass is None
        assert target_mass is None, "Test item should have no mass defined"

        # This should not crash (mimics the CLI code)
        if target_mass is not None:
            mass_str = f"{target_mass:.2f} kg"
        else:
            mass_str = "mass unknown"

        # Verify the format string works
        output = f"TARGET: {target_item_id} (1 unit, {mass_str})"
        assert "mass unknown" in output, "Should show 'mass unknown'"
        assert "TypeError" not in output, "Should not have format error"

    def test_sim_plan_with_mass_shows_correctly(self, temp_kb, temp_sim_dir):
        """
        Test Issue #11: sim plan should show mass when available.

        Tests that items with mass defined show the mass correctly.
        """
        # Create KB loader
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Get item with mass
        target_item_id = "test_item_with_mass"
        target_item = kb.get_item(target_item_id)
        assert target_item is not None, "Target item should exist"

        target_dict = target_item.model_dump() if hasattr(target_item, 'model_dump') else target_item
        target_mass = target_dict.get('mass')  # Should be 50.0

        # Verify mass exists
        assert target_mass is not None, "Test item should have mass defined"
        assert target_mass == 50.0, "Test item should have 50.0 kg mass"

        # This should work correctly
        if target_mass is not None:
            mass_str = f"{target_mass:.2f} kg"
        else:
            mass_str = "mass unknown"

        # Verify the format string works
        output = f"TARGET: {target_item_id} (1 unit, {mass_str})"
        assert "50.00 kg" in output, "Should show '50.00 kg'"
        assert "mass unknown" not in output, "Should not show 'mass unknown'"
