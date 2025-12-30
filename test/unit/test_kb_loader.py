"""
Tests for kb_core.kb_loader

Tests eager loading, lazy loading, caching, and model parsing.
"""
import pytest
from pathlib import Path

from src.kb_core.kb_loader import KBLoader
from src.kb_core.schema import RawProcess, RawRecipe, RawItem, Process, Recipe, Item


@pytest.fixture
def test_kb_root(test_fixtures_dir):
    """Return path to test KB fixtures."""
    return test_fixtures_dir / "kb"


# =============================================================================
# Eager Loading Tests (load_all)
# =============================================================================

class TestEagerLoading:
    """Test eager loading with load_all()."""

    def test_load_all_with_raw_models(self, test_kb_root):
        """Load all KB data with raw models."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        loader.load_all()

        # Check processes loaded
        assert len(loader.processes) > 0
        assert "test_process_v0" in loader.processes

        # Check recipes loaded
        assert len(loader.recipes) > 0
        assert "test_recipe_v0" in loader.recipes

        # Check items loaded
        assert len(loader.items) > 0
        assert "test_material_v0" in loader.items
        assert "test_part_v0" in loader.items

        # Check units loaded
        assert "conversions" in loader.units
        assert len(loader.units["conversions"]) > 0

        # Check materials loaded
        assert "material_properties" in loader.materials
        assert "steel" in loader.materials["material_properties"]

    def test_load_all_with_validated_models(self, test_kb_root):
        """Load all KB data with validated models."""
        loader = KBLoader(test_kb_root, use_validated_models=True)
        loader.load_all()

        # Check processes are validated Process instances
        assert "test_process_v0" in loader.processes
        process = loader.processes["test_process_v0"]
        assert isinstance(process, Process)
        assert process.process_type == "continuous"
        assert process.time_model.type == "linear_rate"

        # Check recipes are validated Recipe instances
        assert "test_recipe_v0" in loader.recipes
        recipe = loader.recipes["test_recipe_v0"]
        assert isinstance(recipe, Recipe)
        assert recipe.target_item_id == "final_product"

        # Check items are validated Item instances
        assert "test_material_v0" in loader.items
        item = loader.items["test_material_v0"]
        assert isinstance(item, Item)
        assert item.kind == "material"

    def test_load_processes_raw(self, test_kb_root):
        """Load processes with raw models."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        loader.load_processes()

        assert len(loader.processes) > 0
        process = loader.processes["test_process_v0"]
        assert isinstance(process, RawProcess)
        assert process.id == "test_process_v0"
        assert process.process_type == "continuous"

    def test_load_recipes_raw(self, test_kb_root):
        """Load recipes with raw models."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        loader.load_recipes()

        assert len(loader.recipes) > 0
        recipe = loader.recipes["test_recipe_v0"]
        assert isinstance(recipe, RawRecipe)
        assert recipe.id == "test_recipe_v0"
        assert recipe.target_item_id == "final_product"

    def test_load_items_from_materials(self, test_kb_root):
        """Load items from items/materials/."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        loader.load_items()

        assert "test_material_v0" in loader.items
        item = loader.items["test_material_v0"]
        assert isinstance(item, RawItem)
        assert item.kind == "material"
        assert item.material_class == "metal"

    def test_load_items_from_parts(self, test_kb_root):
        """Load items from items/parts/."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        loader.load_items()

        assert "test_part_v0" in loader.items
        item = loader.items["test_part_v0"]
        assert isinstance(item, RawItem)
        assert item.kind == "part"
        assert item.material_class == "steel"

    def test_load_units(self, test_kb_root):
        """Load unit conversions."""
        loader = KBLoader(test_kb_root)
        loader.load_units()

        assert "conversions" in loader.units
        conversions = loader.units["conversions"]

        # Check specific conversion exists
        kg_to_g = next((c for c in conversions if c["from"] == "kg" and c["to"] == "g"), None)
        assert kg_to_g is not None
        assert kg_to_g["factor"] == 1000.0

    def test_load_material_properties(self, test_kb_root):
        """Load material properties."""
        loader = KBLoader(test_kb_root)
        loader.load_material_properties()

        assert "material_properties" in loader.materials
        assert "steel" in loader.materials["material_properties"]
        assert loader.materials["material_properties"]["steel"]["density_kg_per_m3"] == 7850


# =============================================================================
# Lazy Loading Tests (get_*)
# =============================================================================

class TestLazyLoading:
    """Test lazy loading with caching."""

    def test_get_process_lazy_load(self, test_kb_root):
        """Lazy load process on first access."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        # Process not loaded yet
        assert len(loader.processes) == 0

        # Lazy load on first access
        process = loader.get_process("test_process_v0")

        assert process is not None
        assert isinstance(process, RawProcess)
        assert process.id == "test_process_v0"

    def test_get_process_from_cache(self, test_kb_root):
        """Get process from cache on second access."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        # First access (lazy load)
        process1 = loader.get_process("test_process_v0")

        # Second access (from cache)
        process2 = loader.get_process("test_process_v0")

        # Should be same instance (cached)
        assert process1 is process2

    def test_get_process_not_found(self, test_kb_root):
        """Return None for non-existent process."""
        loader = KBLoader(test_kb_root)
        process = loader.get_process("nonexistent_process")

        assert process is None

    def test_get_recipe_lazy_load(self, test_kb_root):
        """Lazy load recipe on first access."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        recipe = loader.get_recipe("test_recipe_v0")

        assert recipe is not None
        assert isinstance(recipe, RawRecipe)
        assert recipe.target_item_id == "final_product"

    def test_get_recipe_not_found(self, test_kb_root):
        """Return None for non-existent recipe."""
        loader = KBLoader(test_kb_root)
        recipe = loader.get_recipe("nonexistent_recipe")

        assert recipe is None

    def test_get_item_from_materials(self, test_kb_root):
        """Lazy load item from materials."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        item = loader.get_item("test_material_v0")

        assert item is not None
        assert isinstance(item, RawItem)
        assert item.kind == "material"

    def test_get_item_from_parts(self, test_kb_root):
        """Lazy load item from parts."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        item = loader.get_item("test_part_v0")

        assert item is not None
        assert isinstance(item, RawItem)
        assert item.kind == "part"

    def test_get_item_not_found(self, test_kb_root):
        """Return None for non-existent item."""
        loader = KBLoader(test_kb_root)
        item = loader.get_item("nonexistent_item")

        assert item is None

    def test_get_item_from_cache(self, test_kb_root):
        """Get item from cache on second access."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        # First access (lazy load)
        item1 = loader.get_item("test_material_v0")

        # Second access (from cache)
        item2 = loader.get_item("test_material_v0")

        # Should be same instance (cached)
        assert item1 is item2


# =============================================================================
# Caching Tests
# =============================================================================

class TestCaching:
    """Test cache behavior."""

    def test_caching_enabled_by_default(self, test_kb_root):
        """Caching is enabled by default."""
        loader = KBLoader(test_kb_root)

        assert loader.cache_enabled is True
        assert loader._processes == {}
        assert loader._recipes == {}
        assert loader._items == {}

    def test_caching_can_be_disabled(self, test_kb_root):
        """Caching can be disabled."""
        loader = KBLoader(test_kb_root, cache_enabled=False)

        assert loader.cache_enabled is False
        assert loader._processes is None
        assert loader._recipes is None
        assert loader._items is None

    def test_lazy_load_with_caching_disabled(self, test_kb_root):
        """Lazy loading works without caching."""
        loader = KBLoader(test_kb_root, cache_enabled=False, use_validated_models=False)

        # Each access loads from file
        process1 = loader.get_process("test_process_v0")
        process2 = loader.get_process("test_process_v0")

        assert process1 is not None
        assert process2 is not None
        # Different instances (not cached)
        assert process1 is not process2


# =============================================================================
# Model Parsing Tests
# =============================================================================

class TestModelParsing:
    """Test raw vs validated model parsing."""

    def test_parse_raw_process(self, test_kb_root):
        """Parse process as raw model."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        process = loader.get_process("test_process_v0")

        assert isinstance(process, RawProcess)
        assert process.process_type == "continuous"
        assert process.time_model is not None
        assert process.time_model.type == "linear_rate"

    def test_parse_validated_process(self, test_kb_root):
        """Parse process as validated model."""
        loader = KBLoader(test_kb_root, use_validated_models=True)
        process = loader.get_process("test_process_v0")

        assert isinstance(process, Process)
        assert process.process_type == "continuous"
        assert process.time_model.type == "linear_rate"
        assert process.time_model.rate == 5.0

    def test_parse_raw_recipe(self, test_kb_root):
        """Parse recipe as raw model."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        recipe = loader.get_recipe("test_recipe_v0")

        assert isinstance(recipe, RawRecipe)
        assert recipe.target_item_id == "final_product"

    def test_parse_validated_recipe(self, test_kb_root):
        """Parse recipe as validated model."""
        loader = KBLoader(test_kb_root, use_validated_models=True)
        recipe = loader.get_recipe("test_recipe_v0")

        assert isinstance(recipe, Recipe)
        assert recipe.target_item_id == "final_product"
        assert len(recipe.steps) == 1

    def test_parse_raw_item(self, test_kb_root):
        """Parse item as raw model."""
        loader = KBLoader(test_kb_root, use_validated_models=False)
        item = loader.get_item("test_material_v0")

        assert isinstance(item, RawItem)
        assert item.kind == "material"
        assert item.material_class == "metal"

    def test_parse_validated_item(self, test_kb_root):
        """Parse item as validated model."""
        loader = KBLoader(test_kb_root, use_validated_models=True)
        item = loader.get_item("test_material_v0")

        assert isinstance(item, Item)
        assert item.kind == "material"
        assert item.material_class == "metal"


# =============================================================================
# Unit Conversion Support Tests
# =============================================================================

class TestUnitConversionSupport:
    """Test methods for UnitConverter support."""

    def test_get_material_density(self, test_kb_root):
        """Get material density."""
        loader = KBLoader(test_kb_root)
        loader.load_material_properties()

        density = loader.get_material_density("steel")
        assert density == 7850

    def test_get_material_density_not_found(self, test_kb_root):
        """Return None for unknown material."""
        loader = KBLoader(test_kb_root)
        loader.load_material_properties()

        density = loader.get_material_density("unobtanium")
        assert density is None

    def test_get_unit_conversion(self, test_kb_root):
        """Get unit conversion factor."""
        loader = KBLoader(test_kb_root)
        loader.load_units()

        factor = loader.get_unit_conversion("kg", "g")
        assert factor == 1000.0

    def test_get_unit_conversion_not_found(self, test_kb_root):
        """Return None for unknown conversion."""
        loader = KBLoader(test_kb_root)
        loader.load_units()

        factor = loader.get_unit_conversion("kg", "parsecs")
        assert factor is None


# =============================================================================
# Eager + Lazy Integration Tests
# =============================================================================

class TestEagerLazyIntegration:
    """Test interaction between eager and lazy loading."""

    def test_lazy_load_uses_eager_loaded_data(self, test_kb_root):
        """Lazy loader checks eager-loaded index first."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        # Eager load
        loader.load_processes()

        # Lazy load should return from eager-loaded index
        process = loader.get_process("test_process_v0")

        assert process is not None
        # Should be from eager-loaded index
        assert process is loader.processes["test_process_v0"]

    def test_eager_load_after_lazy_load(self, test_kb_root):
        """Eager load after lazy load works correctly."""
        loader = KBLoader(test_kb_root, use_validated_models=False)

        # Lazy load first
        process1 = loader.get_process("test_process_v0")

        # Eager load
        loader.load_processes()

        # Both should be available
        assert "test_process_v0" in loader.processes
        process2 = loader.get_process("test_process_v0")

        # Should return eager-loaded version
        assert process2 is loader.processes["test_process_v0"]


# =============================================================================
# Error Handling Tests
# =============================================================================

class TestErrorHandling:
    """Test error handling and reporting."""

    def test_load_missing_directory(self, tmp_path):
        """Handle missing KB directory gracefully."""
        missing_kb = tmp_path / "nonexistent_kb"
        loader = KBLoader(missing_kb)
        loader.load_processes()

        # Should record error
        assert len(loader.load_errors) > 0
        assert "not found" in loader.load_errors[0].lower()

    def test_load_invalid_yaml(self, tmp_path):
        """Handle invalid YAML gracefully."""
        kb_root = tmp_path / "kb"
        kb_root.mkdir()
        processes_dir = kb_root / "processes"
        processes_dir.mkdir()

        # Create invalid YAML file
        invalid_file = processes_dir / "invalid.yaml"
        invalid_file.write_text("{ invalid yaml content [")

        loader = KBLoader(kb_root)
        loader.load_processes()

        # Should record error
        assert len(loader.load_errors) > 0

    def test_error_tracking_across_loads(self, test_kb_root):
        """Errors accumulate across multiple loads."""
        missing_kb = test_kb_root / "nonexistent"
        loader = KBLoader(missing_kb)

        loader.load_processes()
        errors_after_processes = len(loader.load_errors)

        loader.load_recipes()
        errors_after_recipes = len(loader.load_errors)

        # Errors should accumulate
        assert errors_after_recipes > errors_after_processes
