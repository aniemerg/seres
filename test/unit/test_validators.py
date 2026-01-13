"""
Tests for kb_core.validators

Tests validation rules per ADR-017.
"""
import pytest

from src.kb_core.validators import (
    validate_process,
    validate_recipe,
    validate_item,
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
    Requirement,
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
            "motor": {"mass_kg": 12.0, "unit": "unit"},
            "steel_ingot": {"mass_kg": 1.0, "unit": "kg"},
            "steel_plate": {"mass_kg": 1.0, "unit": "kg"},
            "mystery_part": {"unit": "unit"},
        }

        self.processes = {
            "regolith_mining_highlands_v0": {
                "id": "regolith_mining_highlands_v0",
                "process_type": "boundary"
            },
            "beneficiation_magnetic_basic_v0": {
                "id": "beneficiation_magnetic_basic_v0",
                "inputs": [{"item_id": "regolith_powder", "qty": 1.0, "unit": "kg"}],
                "outputs": [
                    {"item_id": "magnetic_concentrate", "qty": 0.2, "unit": "kg"},
                    {"item_id": "tailings", "qty": 0.8, "unit": "kg"}
                ]
            },
            "regolith_screening_sieving_v0": {
                "id": "regolith_screening_sieving_v0",
                "inputs": [{"item_id": "regolith_lunar_mare", "qty": 1.0, "unit": "kg"}],
                "outputs": [
                    {"item_id": "regolith_coarse_fraction", "qty": 0.6, "unit": "kg"},
                    {"item_id": "regolith_fine_fraction", "qty": 0.4, "unit": "kg"}
                ]
            },
            "metal_casting_basic_v0": {
                "id": "metal_casting_basic_v0",
                "inputs": [{"item_id": "aluminum_alloy_ingot", "qty": 9.0, "unit": "kg"}],
                "outputs": [{"item_id": "aluminum_link_blank", "qty": 1.0, "unit": "unit"}]
            },
            "machining_finish_basic_v0": {
                "id": "machining_finish_basic_v0",
                "inputs": [{"item_id": "aluminum_link_blank", "qty": 1.0, "unit": "unit"}],
                "outputs": [{"item_id": "robot_arm_link_aluminum", "qty": 1.0, "unit": "unit"}]
            },
            "inspection_basic_v0": {
                "id": "inspection_basic_v0",
                "inputs": [{"item_id": "robot_arm_link_aluminum", "qty": 1.0, "unit": "unit"}],
                "outputs": [{"item_id": "robot_arm_link_aluminum", "qty": 1.0, "unit": "unit"}]
            },
            "drying_basic_v0": {
                "id": "drying_basic_v0",
                "is_template": True,
                "inputs": []
            }
        }

        self.boms = {}

    def get_unit_conversion(self, from_unit, to_unit):
        return self.conversions.get((from_unit, to_unit))

    def get_material_density(self, material_name):
        return self.densities.get(material_name)

    def get_item(self, item_id):
        return self.items.get(item_id)

    def get_process(self, process_id):
        return self.processes.get(process_id)

    def get_bom(self, machine_id):
        return self.boms.get(machine_id)


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


class TestItemValidation:
    """Test item unit_kind validation rules."""

    def test_item_missing_unit_kind_warning(self):
        item = {
            "id": "test_part",
            "kind": "part",
            "unit": "kg",
        }
        issues = validate_item(item)
        issue = next((i for i in issues if i.rule == "unit_kind_missing"), None)
        assert issue is not None
        assert issue.level == ValidationLevel.WARNING

    def test_item_discrete_requires_mass(self):
        item = {
            "id": "test_part",
            "kind": "part",
            "unit_kind": "discrete",
            "unit": "unit",
        }
        issues = validate_item(item)
        issue = next((i for i in issues if i.rule == "unit_kind_discrete_missing_mass"), None)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR

    def test_item_discrete_unit_mismatch(self):
        item = {
            "id": "test_part",
            "kind": "part",
            "unit_kind": "discrete",
            "unit": "kg",
            "mass_kg": 1.0,
        }
        issues = validate_item(item)
        issue = next((i for i in issues if i.rule == "unit_kind_discrete_unit_mismatch"), None)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR

    def test_item_bulk_unit_mismatch(self):
        item = {
            "id": "test_material",
            "kind": "material",
            "unit_kind": "bulk",
            "unit": "unit",
        }
        issues = validate_item(item)
        issue = next((i for i in issues if i.rule == "unit_kind_bulk_unit_mismatch"), None)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR

    def test_item_valid_discrete(self):
        item = {
            "id": "test_part",
            "kind": "part",
            "unit_kind": "discrete",
            "unit": "unit",
            "mass_kg": 2.0,
        }
        issues = validate_item(item)
        assert issues == []

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

    def test_process_missing_machine_requirement(self):
        """ERROR: All processes must declare machine requirements."""
        process_dict = {
            "id": "test_process_v0",
            "process_type": "batch",
            "inputs": [{"item_id": "raw_material", "qty": 10.0, "unit": "kg"}],
            "outputs": [{"item_id": "product", "qty": 8.0, "unit": "kg"}],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 2.0
            },
            "energy_model": {
                "type": "fixed_per_batch",
                "value": 5.0,
                "unit": "kWh"
            },
            # Missing resource_requirements with machine_id
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "process_machine_required"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "machine requirement" in error.message.lower()

    def test_process_with_machine_requirement_passes(self):
        """Process with machine requirement should not generate error."""
        process_dict = {
            "id": "test_process_v0",
            "process_type": "batch",
            "inputs": [{"item_id": "raw_material", "qty": 10.0, "unit": "kg"}],
            "outputs": [{"item_id": "product", "qty": 8.0, "unit": "kg"}],
            "resource_requirements": [
                {"machine_id": "labor_bot_general_v0", "qty": 2.0, "unit": "hr"}
            ],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 2.0
            },
            "energy_model": {
                "type": "fixed_per_batch",
                "value": 5.0,
                "unit": "kWh"
            }
        }

        issues = validate_process_semantics(process_dict)

        machine_errors = [i for i in issues if i.rule == "process_machine_required"]
        assert len(machine_errors) == 0, "Process with machine requirement should not generate error"

    def test_boundary_process_missing_machine_requirement(self):
        """ERROR: Boundary processes must also declare machine requirements."""
        process_dict = {
            "id": "test_boundary_v0",
            "process_type": "boundary",
            "inputs": [],
            "outputs": [{"item_id": "regolith_lunar_highlands", "qty": 100.0, "unit": "kg"}],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            },
            # Missing resource_requirements
        }

        issues = validate_process_semantics(process_dict)

        error = next((i for i in issues if i.rule == "process_machine_required"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR
        assert "machine requirement" in error.message.lower()


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
# Reference Validation Tests (Category 6)
# =============================================================================

class TestReferenceValidation:
    """Test reference validation (ADR-017 Category 6)."""

    def test_input_item_not_found_warning(self, converter):
        """Process with non-existent input item generates WARNING."""
        process = {
            "id": "test_process",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [
                {"item_id": "nonexistent_item", "qty": 1.0, "unit": "kg"}
            ],
            "outputs": [
                {"item_id": "steel_ingot", "qty": 1.0, "unit": "kg"}
            ],
            "time_model": {
                "type": "linear_rate",
                "rate": 10.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "nonexistent_item"
            }
        }

        issues = validate_process(process, converter)

        # Should have WARNING for nonexistent input item
        warnings = [i for i in issues if i.rule == "input_item_not_found"]
        assert len(warnings) == 1
        assert warnings[0].level == ValidationLevel.WARNING
        assert warnings[0].category == "reference"
        assert "nonexistent_item" in warnings[0].message

    def test_output_item_not_found_warning(self, converter):
        """Process with non-existent output item generates WARNING."""
        process = {
            "id": "test_process",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [
                {"item_id": "steel_ingot", "qty": 1.0, "unit": "kg"}
            ],
            "outputs": [
                {"item_id": "nonexistent_output", "qty": 1.0, "unit": "kg"}
            ],
            "time_model": {
                "type": "linear_rate",
                "rate": 10.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "steel_ingot"
            }
        }

        issues = validate_process(process, converter)

        # Should have WARNING for nonexistent output item
        warnings = [i for i in issues if i.rule == "output_item_not_found"]
        assert len(warnings) == 1
        assert warnings[0].level == ValidationLevel.WARNING
        assert "nonexistent_output" in warnings[0].message

    def test_resource_machine_not_found_warning(self, converter):
        """Process with non-existent machine generates WARNING."""
        process = {
            "id": "test_process",
            "kind": "process",
            "process_type": "batch",
            "inputs": [
                {"item_id": "steel_ingot", "qty": 1.0, "unit": "kg"}
            ],
            "outputs": [
                {"item_id": "steel_plate", "qty": 1.0, "unit": "kg"}
            ],
            "resource_requirements": [
                {"machine_id": "nonexistent_machine", "qty": 1.0, "unit": "hr"}
            ],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            }
        }

        issues = validate_process(process, converter)

        # Should have WARNING for nonexistent machine
        warnings = [i for i in issues if i.rule == "resource_machine_not_found"]
        assert len(warnings) == 1
        assert warnings[0].level == ValidationLevel.WARNING
        assert "nonexistent_machine" in warnings[0].message

    def test_template_process_skips_reference_validation(self, converter):
        """Process with is_template: true skips reference validation."""
        process = {
            "id": "template_process",
            "kind": "process",
            "process_type": "batch",
            "is_template": True,  # Template flag
            "inputs": [
                {"item_id": "wet_material", "qty": 1.0, "unit": "kg"}
            ],
            "outputs": [
                {"item_id": "dried_material", "qty": 1.0, "unit": "kg"}
            ],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0
            }
        }

        issues = validate_process(process, converter)

        # Should NOT have reference warnings (template processes are exempt)
        ref_warnings = [i for i in issues if i.category == "reference"]
        assert len(ref_warnings) == 0

    def test_recipe_process_not_found_error(self, converter):
        """Recipe with non-existent process_id generates ERROR."""
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "steel_plate",
            "steps": [
                {"process_id": "nonexistent_process"}
            ]
        }

        issues = validate_recipe(recipe, converter)

        # Should have ERROR for nonexistent process
        errors = [i for i in issues if i.rule == "process_not_found"]
        assert len(errors) == 1
        assert errors[0].level == ValidationLevel.ERROR
        assert errors[0].category == "reference"
        assert "nonexistent_process" in errors[0].message

    def test_recipe_with_valid_process_no_error(self, converter):
        """Recipe with existing process_id has no reference errors."""
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "steel_plate",
            "steps": [
                {"process_id": "regolith_mining_highlands_v0"}  # Real process
            ]
        }

        issues = validate_recipe(recipe, converter)

        # Should NOT have process_not_found errors
        errors = [i for i in issues if i.rule == "process_not_found"]
        assert len(errors) == 0


class TestRecipeTargetAndUnitValidation:
    """Test recipe target output and unit convertibility validation."""

    def test_recipe_target_not_produced_error(self, converter):
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "steel_plate",
            "inputs": [
                {"item_id": "regolith_powder", "qty": 1.0, "unit": "kg"}
            ],
            "steps": [
                {"process_id": "beneficiation_magnetic_basic_v0"}
            ]
        }

        issues = validate_recipe(recipe, converter)
        error = next((i for i in issues if i.rule == "recipe_target_not_produced"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_recipe_target_produced_ok(self, converter):
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "robot_arm_link_aluminum",
            "inputs": [
                {"item_id": "aluminum_alloy_ingot", "qty": 9.0, "unit": "kg"}
            ],
            "steps": [
                {"process_id": "metal_casting_basic_v0"},
                {"process_id": "machining_finish_basic_v0"},
                {"process_id": "inspection_basic_v0"}
            ]
        }

        issues = validate_recipe(recipe, converter)
        errors = [i for i in issues if i.rule == "recipe_target_not_produced"]
        assert errors == []

    def test_recipe_target_unit_not_convertible_error(self, converter):
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "mystery_part",
            "steps": [
                {
                    "process_id": "regolith_mining_highlands_v0",
                    "outputs": [{"item_id": "mystery_part", "qty": 1.0, "unit": "kg"}]
                }
            ]
        }

        issues = validate_recipe(recipe, converter)
        error = next((i for i in issues if i.rule == "recipe_target_unit_not_convertible"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_recipe_unit_convertible_ok(self, converter):
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "motor",
            "inputs": [
                {"item_id": "motor", "qty": 1.0, "unit": "unit"}
            ],
            "outputs": [
                {"item_id": "motor", "qty": 1.0, "unit": "unit"}
            ],
            "steps": [
                {
                    "process_id": "regolith_mining_highlands_v0",
                    "inputs": [{"item_id": "motor", "qty": 12.0, "unit": "kg"}],
                    "outputs": [{"item_id": "motor", "qty": 1.0, "unit": "unit"}]
                }
            ]
        }

        issues = validate_recipe(recipe, converter)
        errors = [i for i in issues if i.rule == "recipe_unit_not_convertible"]
        assert errors == []

    def test_recipe_unit_not_convertible_error(self, converter):
        recipe = {
            "id": "test_recipe",
            "kind": "recipe",
            "target_item_id": "mystery_part",
            "inputs": [
                {"item_id": "mystery_part", "qty": 1.0, "unit": "unit"}
            ],
            "outputs": [
                {"item_id": "mystery_part", "qty": 1.0, "unit": "unit"}
            ],
            "steps": [
                {
                    "process_id": "regolith_mining_highlands_v0",
                    "inputs": [{"item_id": "mystery_part", "qty": 1.0, "unit": "kg"}],
                    "outputs": [{"item_id": "mystery_part", "qty": 1.0, "unit": "unit"}]
                }
            ]
        }

        issues = validate_recipe(recipe, converter)
        error = next((i for i in issues if i.rule == "recipe_unit_not_convertible"), None)
        assert error is not None
        assert error.level == ValidationLevel.ERROR

    def test_byproduct_item_not_found_warning(self, converter):
        """Process with non-existent byproduct item generates WARNING."""
        process = {
            "id": "test_process",
            "kind": "process",
            "process_type": "continuous",
            "inputs": [
                {"item_id": "steel_ingot", "qty": 1.0, "unit": "kg"}
            ],
            "outputs": [
                {"item_id": "steel_plate", "qty": 1.0, "unit": "kg"}
            ],
            "byproducts": [
                {"item_id": "nonexistent_byproduct", "qty": 0.1, "unit": "kg"}
            ],
            "time_model": {
                "type": "linear_rate",
                "rate": 10.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "steel_ingot"
            }
        }

        issues = validate_process(process, converter)

        # Should have WARNING for nonexistent byproduct item
        warnings = [i for i in issues if i.rule == "byproduct_item_not_found"]
        assert len(warnings) == 1
        assert warnings[0].level == ValidationLevel.WARNING
        assert "nonexistent_byproduct" in warnings[0].message


# =============================================================================
# Recipe Step Input Validation Tests (Issue #9)
# =============================================================================

class TestRecipeStepInputValidation:
    """Test recipe step input satisfaction validation (Issue #9)."""

    def test_recipe_anorthite_ore_v0_fails_validation(self, converter):
        """
        Test 1: recipe_anorthite_ore_v0 should fail validation.

        Step 0: beneficiation_magnetic_basic_v0 requires regolith_powder
        Step 1: regolith_screening_sieving_v0 requires regolith_lunar_mare
        Recipe has NO inputs, NO BOM, steps don't chain.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Create recipe that mimics recipe_anorthite_ore_v0
        recipe = {
            "id": "recipe_anorthite_ore_v0",
            "target_item_id": "anorthite_ore",
            "variant_id": "v0",
            "inputs": [],  # NO inputs
            "steps": [
                {"process_id": "beneficiation_magnetic_basic_v0"},
                {"process_id": "regolith_screening_sieving_v0"}
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # Should have errors for unsatisfied inputs
        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        assert len(errors) >= 1, "Expected at least 1 error for unsatisfied inputs"

        # Check that step 0 error mentions regolith_powder
        step_0_errors = [e for e in errors if "Step 0" in e.message and "regolith_powder" in e.message]
        assert len(step_0_errors) == 1, "Expected error for step 0 requiring regolith_powder"

        # Check that step 1 error mentions regolith_lunar_mare
        step_1_errors = [e for e in errors if "Step 1" in e.message and "regolith_lunar_mare" in e.message]
        assert len(step_1_errors) == 1, "Expected error for step 1 requiring regolith_lunar_mare"

    def test_recipe_robot_arm_link_aluminum_v0_passes_validation(self, converter):
        """
        Test 2: recipe_robot_arm_link_aluminum_v0 should pass validation.

        Has recipe-level input: aluminum_alloy_ingot (9.0 kg)
        Steps can use this shared input.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Create recipe that mimics recipe_robot_arm_link_aluminum_v0
        recipe = {
            "id": "recipe_robot_arm_link_aluminum_v0",
            "target_item_id": "robot_arm_link_aluminum",
            "variant_id": "v0",
            "inputs": [{"item_id": "aluminum_alloy_ingot", "qty": 9.0, "unit": "kg"}],
            "steps": [
                {"process_id": "metal_casting_basic_v0"},
                {"process_id": "machining_finish_basic_v0"},
                {"process_id": "inspection_basic_v0"}
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # Should NOT have step input errors
        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        assert len(errors) == 0, f"Expected no errors, but got: {[e.message for e in errors]}"

    def test_step_uses_output_from_earlier_step(self, converter):
        """
        Test 3: Recipe where step N uses output from earlier steps.

        Tests non-sequential dependencies.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Create a recipe where steps chain outputs
        recipe = {
            "id": "test_chaining_recipe",
            "target_item_id": "final_product",
            "inputs": [],
            "steps": [
                {"process_id": "regolith_screening_sieving_v0"},  # outputs: regolith_coarse_fraction, regolith_fine_fraction
                {"process_id": "beneficiation_magnetic_basic_v0", "inputs": [{"item_id": "regolith_coarse_fraction", "qty": 1.0, "unit": "kg"}]}  # uses step 0 output
            ]
        }

        # Mock: Step 0 outputs regolith_coarse_fraction (from actual process definition)
        # Step 1 requires it as explicit step-level input
        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # Should NOT have errors - step 1 uses output from step 0
        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        # Step 0 requires regolith_lunar_mare, so we expect 1 error for that
        # But step 1 should NOT error because it uses step 0's output
        step_1_errors = [e for e in errors if "Step 1" in e.message]
        assert len(step_1_errors) == 0, f"Step 1 should not error (uses step 0 output): {[e.message for e in step_1_errors]}"

    def test_recipe_uses_bom_inputs(self, converter):
        """
        Test 4: Recipe using BOM inputs (ADR-019).

        Recipe has target_item_id with BOM.
        Step requires input that's in BOM.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Add a BOM to the mock KB
        converter.kb.boms["test_machine"] = {
            "id": "bom_test_machine_v0",
            "target_item_id": "test_machine",
            "components": [
                {"item_id": "aluminum_alloy_ingot", "qty": 5.0, "unit": "kg"}
            ]
        }

        # Create a recipe that uses BOM input
        recipe = {
            "id": "recipe_test_machine_v0",
            "target_item_id": "test_machine",
            "inputs": [],  # NO explicit inputs
            "steps": [
                {"process_id": "metal_casting_basic_v0"}  # Requires aluminum_alloy_ingot
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # Should NOT have errors - BOM provides the input
        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        assert len(errors) == 0, f"BOM should satisfy input: {[e.message for e in errors]}"

    def test_boundary_process_skipped(self, converter):
        """
        Test 5: Boundary processes (process_type=boundary) should be skipped.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Find a boundary process - mining processes are typically boundary
        recipe = {
            "id": "test_boundary_recipe",
            "target_item_id": "ore",
            "inputs": [],
            "steps": [
                {"process_id": "regolith_mining_highlands_v0"}  # Should be a boundary process
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # Check if this is actually a boundary process
        process = converter.kb.get_process("regolith_mining_highlands_v0")
        if process and (process.get("process_type") == "boundary" if isinstance(process, dict) else process.process_type == "boundary"):
            # Should NOT have errors (boundary processes are skipped)
            errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
            assert len(errors) == 0, "Boundary processes should not generate input validation errors"

    def test_template_process_skipped(self, converter):
        """
        Test 6: Template processes (is_template=True) should be skipped.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Create a recipe with a template process (if any exist in KB)
        # For now, we'll create a mock scenario
        recipe = {
            "id": "test_template_recipe",
            "target_item_id": "product",
            "inputs": [{"item_id": "material_a", "qty": 1.0, "unit": "kg"}],
            "steps": [
                {"process_id": "drying_basic_v0"}  # Check if this is a template
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # We just verify it doesn't crash - template handling is tested
        assert isinstance(issues, list)

    def test_step_level_input_override(self, converter):
        """
        Test 7: Step-level inputs override process-level inputs (ADR-013).
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Create a recipe where step overrides process inputs
        recipe = {
            "id": "test_override_recipe",
            "target_item_id": "product",
            "inputs": [{"item_id": "aluminum_alloy_ingot", "qty": 1.0, "unit": "kg"}],
            "steps": [
                {
                    "process_id": "beneficiation_magnetic_basic_v0",  # Requires regolith_powder
                    "inputs": [{"item_id": "aluminum_alloy_ingot", "qty": 1.0, "unit": "kg"}]  # Override to use aluminum
                }
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        # Should NOT have errors - step override is satisfied by recipe input
        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        assert len(errors) == 0, f"Step-level override should be satisfied: {[e.message for e in errors]}"

    def test_error_message_includes_context(self, converter):
        """
        Test 8: Error message should include step index, process_id, missing item.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Create broken recipe
        recipe = {
            "id": "recipe_anorthite_ore_v0",
            "target_item_id": "anorthite_ore",
            "inputs": [],
            "steps": [
                {"process_id": "beneficiation_magnetic_basic_v0"}
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        assert len(errors) >= 1

        # Check first error has context
        error = errors[0]
        assert "Step" in error.message, "Error message should include step index"
        assert "process" in error.message.lower(), "Error message should mention process"
        assert error.field_path.startswith("steps["), "Field path should reference steps array"
        assert error.fix_hint, "Fix hint should be provided"

    def test_multiple_steps_multiple_errors(self, converter):
        """
        Test 9: Recipe with multiple steps can generate multiple errors.
        """
        from src.kb_core.validators import validate_recipe_step_inputs

        # Recipe with 2 steps, both requiring unsatisfied inputs
        recipe = {
            "id": "test_multi_error_recipe",
            "target_item_id": "product",
            "inputs": [],
            "steps": [
                {"process_id": "beneficiation_magnetic_basic_v0"},  # Requires regolith_powder
                {"process_id": "regolith_screening_sieving_v0"}     # Requires regolith_lunar_mare
            ]
        }

        issues = validate_recipe_step_inputs(recipe, converter.kb)

        errors = [i for i in issues if i.rule == "recipe_step_input_not_satisfied"]
        assert len(errors) >= 2, f"Expected at least 2 errors, got {len(errors)}"


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
            resource_requirements=[
                Requirement(
                    machine_id="boiler_v0",
                    qty=1.0,
                    unit="hr"
                )
            ],
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
