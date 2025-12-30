"""
Tests for kb_core.validators

Tests validation rules per ADR-017.
"""
import pytest

from src.kb_core.validators import (
    validate_process,
    validate_recipe,
    validate_process_schema,
    validate_process_semantics,
    validate_process_unit_conversion,
    validate_process_cross_model,
    ValidationLevel,
    ValidationIssue,
)
from src.kb_core.schema import (
    Process,
    Recipe,
    RecipeStep,
    Quantity,
    TimeModel,
    EnergyModel,
)
from src.kb_core.unit_converter import UnitConverter


# =============================================================================
# Mock KB Loader (for UnitConverter)
# =============================================================================

class MockKBLoader:
    """Mock KB loader for testing."""

    def __init__(self):
        self.conversions = {
            ("kg", "g"): 1000.0,
            ("m3", "L"): 1000.0,
        }

        self.densities = {
            "water": 1000.0,
        }

        self.items = {
            "motor": {"mass_kg": 12.0},
        }

    def get_unit_conversion(self, from_unit, to_unit):
        return self.conversions.get((from_unit, to_unit))

    def get_material_density(self, material_name):
        return self.densities.get(material_name)

    def get_item(self, item_id):
        return self.items.get(item_id)


@pytest.fixture
def kb_loader():
    return MockKBLoader()


@pytest.fixture
def converter(kb_loader):
    return UnitConverter(kb_loader)


# =============================================================================
# Schema Validation Tests
# =============================================================================

class TestSchemaValidation:
    """Test schema validation rules."""

    def test_missing_process_type(self):
        """ERROR: process_type required."""
        process_dict = {
            "id": "test_v0",
            # Missing process_type
            "inputs": [],
            "outputs": [],
        }

        issues = validate_process_schema(process_dict)

        assert len(issues) > 0
        error = next((i for i in issues if i.rule == "process_type_required"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_invalid_process_type(self):
        """ERROR: process_type must be batch or continuous."""
        process_dict = {
            "id": "test_v0",
            "process_type": "invalid",
            "inputs": [],
            "outputs": [],
        }

        issues = validate_process_schema(process_dict)

        error = next((i for i in issues if i.rule == "process_type_invalid"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_time_model_type_mismatch_continuous(self):
        """ERROR: continuous requires linear_rate."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "batch",  # Wrong type for continuous
                "hr_per_batch": 2.0
            }
        }

        issues = validate_process_schema(process_dict)

        error = next((i for i in issues if i.rule == "time_model_type_mismatch"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "linear_rate" in error.message

    def test_time_model_type_mismatch_batch(self):
        """ERROR: batch requires batch type."""
        process_dict = {
            "id": "test_v0",
            "process_type": "batch",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",  # Wrong type for batch
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            }
        }

        issues = validate_process_schema(process_dict)

        error = next((i for i in issues if i.rule == "time_model_type_mismatch"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_linear_rate_missing_required_fields(self):
        """ERROR: linear_rate requires rate, rate_unit, scaling_basis."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                # Missing rate, rate_unit, scaling_basis
            }
        }

        issues = validate_process_schema(process_dict)

        # Should have 3 errors (one for each missing field)
        missing_field_errors = [i for i in issues if i.rule == "required_field_missing"]
        assert len(missing_field_errors) == 3

    def test_batch_missing_hr_per_batch(self):
        """ERROR: batch requires hr_per_batch."""
        process_dict = {
            "id": "test_v0",
            "process_type": "batch",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "batch",
                # Missing hr_per_batch
            }
        }

        issues = validate_process_schema(process_dict)

        error = next((i for i in issues if i.rule == "required_field_missing"), None)
        assert error is not None
        assert "hr_per_batch" in error.message

    def test_deprecated_field_rate_kg_per_hr(self):
        """ERROR: deprecated field rate_kg_per_hr."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore",
                "rate_kg_per_hr": 5.0  # Deprecated
            }
        }

        issues = validate_process_schema(process_dict)

        error = next((i for i in issues if i.rule == "deprecated_field"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "rate_kg_per_hr" in error.message

    def test_energy_model_invalid_type(self):
        """ERROR: energy_model type must be per_unit or fixed_per_batch."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            },
            "energy_model": {
                "type": "invalid_type",
                "value": 2.0
            }
        }

        issues = validate_process_schema(process_dict)

        error = next((i for i in issues if i.rule == "energy_model_type_invalid"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_energy_model_per_unit_missing_fields(self):
        """ERROR: per_unit requires value, unit, scaling_basis."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            },
            "energy_model": {
                "type": "per_unit",
                # Missing value, unit, scaling_basis
            }
        }

        issues = validate_process_schema(process_dict)

        missing_errors = [i for i in issues if i.rule == "required_field_missing" and "energy_model" in i.field_path]
        assert len(missing_errors) == 3

    def test_valid_process_passes_schema_validation(self):
        """Valid process passes schema validation."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[Quantity(item_id="metal", qty=90.0, unit="kg")],
            time_model=TimeModel(
                type="linear_rate",
                rate=5.0,
                rate_unit="kg/hr",
                scaling_basis="ore"
            )
        )

        issues = validate_process_schema(process)

        # No schema errors
        errors = [i for i in issues if i.level == ValidationLevel.ERROR]
        assert len(errors) == 0


# =============================================================================
# Semantic Validation Tests
# =============================================================================

class TestSemanticValidation:
    """Test semantic validation rules."""

    def test_scaling_basis_not_found_in_inputs_outputs(self):
        """ERROR: scaling_basis must exist in inputs/outputs."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 90.0, "unit": "kg"}],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "nonexistent_item"  # Not in inputs/outputs
            }
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "scaling_basis_not_found"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "nonexistent_item" in error.message

    def test_setup_hr_in_continuous_process(self):
        """ERROR: continuous processes cannot have setup_hr."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore",
                "setup_hr": 0.5  # Not allowed in continuous
            }
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "setup_hr_in_continuous"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_non_positive_rate(self):
        """ERROR: rate must be positive."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 0.0,  # Invalid
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            }
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "non_positive_value"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_negative_energy_value(self):
        """ERROR: energy value cannot be negative."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            },
            "energy_model": {
                "type": "per_unit",
                "value": -10.0,  # Invalid
                "unit": "kWh/kg",
                "scaling_basis": "ore"
            }
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "negative_value"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_invalid_compound_unit_format(self):
        """ERROR: rate_unit must be compound format."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "invalid",  # Not compound
                "scaling_basis": "ore"
            }
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "invalid_compound_unit"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_unknown_unit_in_rate(self):
        """ERROR: units must be known (caught by compound unit parsing)."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "unknownunit/hr",  # Unknown unit caught by parse_compound_unit
                "scaling_basis": "ore"
            }
        }

        issues = validate_process_semantics(process_dict)

        # Unknown units are caught by parse_compound_unit which raises ValueError
        # This is caught and reported as invalid_compound_unit error
        error = next((i for i in issues if i.rule == "invalid_compound_unit"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "Unknown numerator unit" in error.message


# =============================================================================
# Unit Conversion Validation Tests
# =============================================================================

class TestUnitConversionValidation:
    """Test unit conversion validation rules."""

    def test_conversion_not_possible_no_density(self, converter):
        """ERROR: Cannot convert without density."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "unknown_liquid", "qty": 100.0, "unit": "L"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",  # Need L->kg, but no density
                "scaling_basis": "unknown_liquid"
            }
        }

        issues = validate_process_unit_conversion(process_dict, converter)

        error = next((i for i in issues if i.rule == "conversion_not_possible"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "density" in error.fix_hint

    def test_conversion_possible_with_density(self, converter):
        """Conversion works with density."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "water", "qty": 100.0, "unit": "L"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",  # L->kg possible for water
                "scaling_basis": "water"
            }
        }

        issues = validate_process_unit_conversion(process_dict, converter)

        # No conversion errors
        conv_errors = [i for i in issues if i.rule == "conversion_not_possible"]
        assert len(conv_errors) == 0

    def test_conversion_not_possible_no_mass_kg(self, converter):
        """ERROR: Cannot convert count to mass without mass_kg."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "unknown_part", "qty": 10.0, "unit": "unit"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",  # Need unit->kg, but no mass_kg
                "scaling_basis": "unknown_part"
            }
        }

        issues = validate_process_unit_conversion(process_dict, converter)

        error = next((i for i in issues if i.rule == "conversion_not_possible"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "mass_kg" in error.fix_hint

    def test_energy_conversion_validation(self, converter):
        """Validate energy model unit conversion."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [{"item_id": "water", "qty": 100.0, "unit": "L"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "water"
            },
            "energy_model": {
                "type": "per_unit",
                "value": 50.0,
                "unit": "kWh/kg",  # L->kg conversion for water works
                "scaling_basis": "water"
            }
        }

        issues = validate_process_unit_conversion(process_dict, converter)

        # No conversion errors
        conv_errors = [i for i in issues if i.rule == "conversion_not_possible"]
        assert len(conv_errors) == 0


# =============================================================================
# Cross-Model Validation Tests
# =============================================================================

class TestCrossModelValidation:
    """Test cross-model validation rules."""

    def test_different_scaling_basis_warning(self):
        """WARNING: time and energy use different scaling_basis."""
        process_dict = {
            "id": "test_v0",
            "process_type": "continuous",
            "inputs": [
                {"item_id": "ore", "qty": 100.0, "unit": "kg"},
                {"item_id": "water", "qty": 10.0, "unit": "L"}
            ],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 5.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "ore"
            },
            "energy_model": {
                "type": "per_unit",
                "value": 2.0,
                "unit": "kWh/L",
                "scaling_basis": "water"  # Different from time_model
            }
        }

        issues = validate_process_cross_model(process_dict)

        warning = next((i for i in issues if i.rule == "different_scaling_basis"), None)
        assert warning is not None
        assert warning.level == ValidationLevel.WARNING

    def test_batch_with_per_unit_energy_warning(self):
        """WARNING: batch process with per-unit energy."""
        process_dict = {
            "id": "test_v0",
            "process_type": "batch",
            "inputs": [{"item_id": "parts", "qty": 10.0, "unit": "unit"}],
            "outputs": [],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 2.0
            },
            "energy_model": {
                "type": "per_unit",  # Expected fixed_per_batch for batch
                "value": 5.0,
                "unit": "kWh/unit",
                "scaling_basis": "parts"
            }
        }

        issues = validate_process_cross_model(process_dict)

        warning = next((i for i in issues if i.rule == "per_unit_energy_with_batch"), None)
        assert warning is not None
        assert warning.level == ValidationLevel.WARNING


# =============================================================================
# Recipe Validation Tests
# =============================================================================

class TestRecipeValidation:
    """Test recipe validation rules."""

    def test_missing_target_item_id(self):
        """ERROR: recipe requires target_item_id."""
        recipe_dict = {
            "id": "test_recipe_v0",
            # Missing target_item_id
            "steps": []
        }

        issues = validate_recipe(recipe_dict)

        error = next((i for i in issues if i.rule == "target_item_id_required"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_empty_steps(self):
        """WARNING: recipe has no steps."""
        recipe_dict = {
            "id": "test_recipe_v0",
            "target_item_id": "product",
            "steps": []
        }

        issues = validate_recipe(recipe_dict)

        warning = next((i for i in issues if i.rule == "empty_steps"), None)
        assert warning is not None
        assert warning.level == ValidationLevel.WARNING

    def test_step_missing_process_id(self):
        """ERROR: step requires process_id."""
        recipe_dict = {
            "id": "test_recipe_v0",
            "target_item_id": "product",
            "steps": [
                {
                    # Missing process_id
                    "notes": "Some step"
                }
            ]
        }

        issues = validate_recipe(recipe_dict)

        error = next((i for i in issues if i.rule == "missing_process_id"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_valid_recipe(self):
        """Valid recipe passes validation."""
        recipe = Recipe(
            id="test_recipe_v0",
            target_item_id="product",
            steps=[
                RecipeStep(process_id="test_process_v0")
            ]
        )

        issues = validate_recipe(recipe)

        # No errors
        errors = [i for i in issues if i.level == ValidationLevel.ERROR]
        assert len(errors) == 0


# =============================================================================
# Integration Tests
# =============================================================================

class TestValidationIntegration:
    """Test full validation pipeline."""

    def test_validate_process_all_rules(self, converter):
        """Validate process with all rules."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="water", qty=100.0, unit="L")],
            outputs=[Quantity(item_id="steam", qty=90.0, unit="L")],
            time_model=TimeModel(
                type="linear_rate",
                rate=5.0,
                rate_unit="kg/hr",
                scaling_basis="water"
            ),
            energy_model=EnergyModel(
                type="per_unit",
                value=50.0,
                unit="kWh/kg",
                scaling_basis="water"
            )
        )

        issues = validate_process(process, converter)

        # Should have no errors (water has density for L->kg conversion)
        errors = [i for i in issues if i.level == ValidationLevel.ERROR]
        assert len(errors) == 0

    def test_validate_process_with_errors(self, converter):
        """Validate process with multiple errors."""
        process_dict = {
            "id": "bad_process_v0",
            # Missing process_type (ERROR)
            "inputs": [{"item_id": "ore", "qty": 100.0, "unit": "kg"}],
            "outputs": [],
            "time_model": {
                "type": "linear_rate",
                "rate": 0.0,  # Invalid (ERROR)
                "rate_unit": "kg/hr",
                "scaling_basis": "nonexistent"  # Not found (ERROR)
            }
        }

        issues = validate_process(process_dict, converter)

        # Should have multiple errors
        errors = [i for i in issues if i.level == ValidationLevel.ERROR]
        assert len(errors) >= 3

    def test_validation_issue_to_dict(self):
        """ValidationIssue serializes to dict."""
        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="test_v0",
            message="Missing process_type",
            field_path="process_type",
            fix_hint="Add process_type"
        )

        result = issue.to_dict()

        assert result["level"] == "error"
        assert result["category"] == "schema"
        assert result["rule"] == "process_type_required"
        assert result["entity_id"] == "test_v0"
        assert result["message"] == "Missing process_type"
        assert result["fix_hint"] == "Add process_type"
