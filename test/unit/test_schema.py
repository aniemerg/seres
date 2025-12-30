"""
Tests for kb_core.schema

Tests two-layer model architecture:
- Raw models accept incomplete/invalid data
- Validated models enforce strict requirements
"""
import pytest
from pydantic import ValidationError

from src.kb_core.schema import (
    # Raw models
    RawTimeModel,
    RawEnergyModel,
    RawProcess,
    RawRecipe,
    RawRecipeStep,
    RawItem,
    RawQuantity,
    # Validated models
    TimeModel,
    EnergyModel,
    Process,
    Recipe,
    RecipeStep,
    Item,
    Quantity,
)


# =============================================================================
# Raw Model Tests (Permissive Parsing)
# =============================================================================

class TestRawTimeModel:
    """Test RawTimeModel permissive parsing."""

    def test_accepts_new_schema(self):
        """Raw model accepts new schema."""
        data = {
            "type": "linear_rate",
            "rate": 10.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "input_ore"
        }
        model = RawTimeModel.model_validate(data)
        assert model.type == "linear_rate"
        assert model.rate == 10.0
        assert model.rate_unit == "kg/hr"
        assert model.scaling_basis == "input_ore"

    def test_accepts_deprecated_fields(self):
        """Raw model accepts deprecated fields for migration."""
        data = {
            "type": "linear_rate",
            "rate_kg_per_hr": 10.0  # Deprecated
        }
        model = RawTimeModel.model_validate(data)
        assert model.rate_kg_per_hr == 10.0

    def test_accepts_missing_fields(self):
        """Raw model accepts missing optional fields."""
        data = {"type": "linear_rate"}
        model = RawTimeModel.model_validate(data)
        assert model.type == "linear_rate"
        assert model.rate is None

    def test_accepts_extra_fields(self):
        """Raw model accepts extra fields."""
        data = {
            "type": "linear_rate",
            "rate": 10.0,
            "unknown_field": "should be ignored"
        }
        model = RawTimeModel.model_validate(data)
        assert model.type == "linear_rate"


class TestRawEnergyModel:
    """Test RawEnergyModel permissive parsing."""

    def test_accepts_new_schema(self):
        """Raw model accepts new schema."""
        data = {
            "type": "per_unit",
            "value": 50.0,
            "unit": "kWh/kg",
            "scaling_basis": "input_water"
        }
        model = RawEnergyModel.model_validate(data)
        assert model.type == "per_unit"
        assert model.value == 50.0

    def test_accepts_missing_fields(self):
        """Raw model accepts missing fields."""
        data = {"type": "per_unit"}
        model = RawEnergyModel.model_validate(data)
        assert model.value is None


class TestRawProcess:
    """Test RawProcess permissive parsing."""

    def test_accepts_complete_process(self):
        """Raw model accepts complete process."""
        data = {
            "id": "test_process_v0",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 10.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 9.0, "unit": "kg"}],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            }
        }
        model = RawProcess.model_validate(data)
        assert model.id == "test_process_v0"
        assert model.process_type == "continuous"
        assert len(model.inputs) == 1

    def test_accepts_missing_process_type(self):
        """Raw model accepts missing process_type (for migration)."""
        data = {
            "id": "old_process_v0",
            "inputs": [],
            "outputs": []
        }
        model = RawProcess.model_validate(data)
        assert model.process_type is None

    def test_accepts_missing_time_model(self):
        """Raw model accepts missing time_model."""
        data = {
            "id": "incomplete_process_v0",
            "inputs": [],
            "outputs": []
        }
        model = RawProcess.model_validate(data)
        assert model.time_model is None

    def test_accepts_deprecated_est_time_hr(self):
        """Raw model accepts deprecated est_time_hr field."""
        data = {
            "id": "old_process_v0",
            "est_time_hr": 2.0,
            "inputs": [],
            "outputs": []
        }
        model = RawProcess.model_validate(data)
        assert model.est_time_hr == 2.0


class TestRawRecipeStep:
    """Test RawRecipeStep with override support."""

    def test_accepts_complete_override(self):
        """Raw step accepts complete time_model override."""
        data = {
            "process_id": "crushing_v0",
            "time_model": {
                "type": "linear_rate",
                "rate": 50.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            }
        }
        model = RawRecipeStep.model_validate(data)
        assert model.time_model.type == "linear_rate"
        assert model.time_model.rate == 50.0

    def test_accepts_partial_override(self):
        """Raw step accepts partial override (no type field)."""
        data = {
            "process_id": "crushing_v0",
            "time_model": {
                "rate": 50.0  # Only override rate
            }
        }
        model = RawRecipeStep.model_validate(data)
        assert model.time_model.rate == 50.0
        assert model.time_model.type is None  # Not specified = partial

    def test_accepts_no_override(self):
        """Raw step accepts no override."""
        data = {"process_id": "crushing_v0"}
        model = RawRecipeStep.model_validate(data)
        assert model.time_model is None


# =============================================================================
# Validated Model Tests (Strict Validation)
# =============================================================================

class TestTimeModel:
    """Test TimeModel strict validation."""

    def test_accepts_valid_linear_rate(self):
        """Validated model accepts valid linear_rate."""
        data = {
            "type": "linear_rate",
            "rate": 10.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "ore"
        }
        model = TimeModel.model_validate(data)
        assert model.type == "linear_rate"
        assert model.rate == 10.0

    def test_accepts_valid_batch(self):
        """Validated model accepts valid batch."""
        data = {
            "type": "batch",
            "hr_per_batch": 1.0,
            "setup_hr": 0.1
        }
        model = TimeModel.model_validate(data)
        assert model.type == "batch"
        assert model.hr_per_batch == 1.0
        assert model.setup_hr == 0.1

    def test_rejects_invalid_type(self):
        """Validated model rejects invalid type."""
        data = {
            "type": "invalid_type",
            "rate": 10.0
        }
        with pytest.raises(ValidationError) as exc_info:
            TimeModel.model_validate(data)
        assert "type" in str(exc_info.value)

    def test_rejects_extra_fields(self):
        """Validated model rejects extra fields."""
        data = {
            "type": "linear_rate",
            "rate": 10.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "ore",
            "extra_field": "not allowed"
        }
        with pytest.raises(ValidationError) as exc_info:
            TimeModel.model_validate(data)
        assert "extra_field" in str(exc_info.value).lower()

    def test_batch_defaults_setup_hr(self):
        """Batch type defaults setup_hr to 0."""
        data = {
            "type": "batch",
            "hr_per_batch": 1.0
        }
        model = TimeModel.model_validate(data)
        assert model.setup_hr == 0.0


class TestEnergyModel:
    """Test EnergyModel strict validation."""

    def test_accepts_valid_per_unit(self):
        """Validated model accepts valid per_unit."""
        data = {
            "type": "per_unit",
            "value": 50.0,
            "unit": "kWh/kg",
            "scaling_basis": "water"
        }
        model = EnergyModel.model_validate(data)
        assert model.type == "per_unit"
        assert model.value == 50.0

    def test_accepts_valid_fixed_per_batch(self):
        """Validated model accepts valid fixed_per_batch."""
        data = {
            "type": "fixed_per_batch",
            "value": 100.0,
            "unit": "kWh"
        }
        model = EnergyModel.model_validate(data)
        assert model.type == "fixed_per_batch"
        assert model.value == 100.0

    def test_rejects_missing_value(self):
        """Validated model rejects missing required value."""
        data = {
            "type": "per_unit",
            "unit": "kWh/kg"
        }
        with pytest.raises(ValidationError) as exc_info:
            EnergyModel.model_validate(data)
        assert "value" in str(exc_info.value)


class TestProcess:
    """Test Process strict validation."""

    def test_accepts_valid_process(self):
        """Validated model accepts valid process."""
        data = {
            "id": "crushing_v0",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 10.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 9.0, "unit": "kg"}],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            }
        }
        model = Process.model_validate(data)
        assert model.id == "crushing_v0"
        assert model.process_type == "continuous"
        assert len(model.inputs) == 1

    def test_rejects_missing_process_type(self):
        """Validated model rejects missing process_type."""
        data = {
            "id": "bad_process_v0",
            "kind": "process",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            }
        }
        with pytest.raises(ValidationError) as exc_info:
            Process.model_validate(data)
        assert "process_type" in str(exc_info.value)

    def test_rejects_invalid_process_type(self):
        """Validated model rejects invalid process_type."""
        data = {
            "id": "bad_process_v0",
            "kind": "process",
            "process_type": "invalid",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            }
        }
        with pytest.raises(ValidationError) as exc_info:
            Process.model_validate(data)
        assert "process_type" in str(exc_info.value)

    def test_rejects_missing_time_model(self):
        """Validated model rejects missing time_model."""
        data = {
            "id": "bad_process_v0",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [],
            "outputs": []
        }
        with pytest.raises(ValidationError) as exc_info:
            Process.model_validate(data)
        assert "time_model" in str(exc_info.value)


class TestQuantity:
    """Test Quantity strict validation."""

    def test_accepts_valid_quantity(self):
        """Validated model accepts valid quantity."""
        data = {"item_id": "ore", "qty": 10.0, "unit": "kg"}
        model = Quantity.model_validate(data)
        assert model.item_id == "ore"
        assert model.qty == 10.0
        assert model.unit == "kg"

    def test_rejects_missing_item_id(self):
        """Validated model rejects missing item_id."""
        data = {"qty": 10.0, "unit": "kg"}
        with pytest.raises(ValidationError) as exc_info:
            Quantity.model_validate(data)
        assert "item_id" in str(exc_info.value)

    def test_rejects_missing_qty(self):
        """Validated model rejects missing qty."""
        data = {"item_id": "ore", "unit": "kg"}
        with pytest.raises(ValidationError) as exc_info:
            Quantity.model_validate(data)
        assert "qty" in str(exc_info.value)


class TestRecipeStep:
    """Test RecipeStep validation."""

    def test_accepts_step_with_override(self):
        """Validated step accepts override."""
        data = {
            "process_id": "crushing_v0",
            "time_model": {
                "rate": 50.0  # Partial override
            }
        }
        model = RecipeStep.model_validate(data)
        assert model.process_id == "crushing_v0"
        assert model.time_model.rate == 50.0

    def test_accepts_step_without_override(self):
        """Validated step accepts no override."""
        data = {"process_id": "crushing_v0"}
        model = RecipeStep.model_validate(data)
        assert model.time_model is None


# =============================================================================
# Two-Layer Conversion Tests
# =============================================================================

class TestRawToValidated:
    """Test conversion from raw to validated models."""

    def test_convert_raw_to_validated_process(self):
        """Can convert valid raw process to validated process."""
        raw_data = {
            "id": "test_v0",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 10.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 9.0, "unit": "kg"}],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            }
        }

        # Parse as raw
        raw_process = RawProcess.model_validate(raw_data)

        # Convert to validated (exclude None values from deprecated fields)
        validated_process = Process.model_validate(
            raw_process.model_dump(exclude_none=True)
        )

        assert validated_process.id == "test_v0"
        assert validated_process.process_type == "continuous"

    def test_raw_accepts_but_validated_rejects_invalid(self):
        """Raw accepts invalid data, validated rejects it."""
        raw_data = {
            "id": "bad_v0",
            "kind": "process",
            # Missing process_type
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            }
        }

        # Raw accepts it
        raw_process = RawProcess.model_validate(raw_data)
        assert raw_process.id == "bad_v0"

        # Validated rejects it
        with pytest.raises(ValidationError) as exc_info:
            Process.model_validate(raw_process.model_dump(exclude_none=True))
        assert "process_type" in str(exc_info.value)


# =============================================================================
# Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_lists_accepted(self):
        """Empty lists are valid."""
        data = {
            "id": "empty_v0",
            "kind": "process",
            "process_type": "batch",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            }
        }
        model = Process.model_validate(data)
        assert model.inputs == []
        assert model.outputs == []

    def test_zero_values_accepted(self):
        """Zero values are valid (though may trigger semantic validation later)."""
        data = {
            "type": "linear_rate",
            "rate": 0.0,  # Will fail semantic validation but schema allows it
            "rate_unit": "kg/hr",
            "scaling_basis": "ore"
        }
        model = TimeModel.model_validate(data)
        assert model.rate == 0.0

    def test_negative_values_accepted_by_schema(self):
        """Negative values accepted by schema (semantic validation will catch)."""
        data = {
            "type": "linear_rate",
            "rate": -5.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "ore"
        }
        model = TimeModel.model_validate(data)
        assert model.rate == -5.0
