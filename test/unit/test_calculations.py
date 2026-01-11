"""
Tests for kb_core.calculations

Tests time and energy calculations per ADR-012 and ADR-014.
"""
import pytest

from src.kb_core.calculations import (
    calculate_duration,
    calculate_energy,
    CalculationError,
)
from src.kb_core.schema import (
    Process,
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
        # Conversion factors
        self.conversions = {
            ("kg", "g"): 1000.0,
            ("m3", "L"): 1000.0,
            ("hr", "min"): 60.0,
            ("day", "hr"): 24.0,
        }

        # Material densities (kg/m³)
        self.densities = {
            "water": 1000.0,
            "aluminum": 2700.0,
        }

        # Item definitions
        self.items = {
            "motor_small": {"mass_kg": 12.0},
            "battery": {"mass_kg": 45.0},
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
# Duration Calculation Tests (Linear Rate)
# =============================================================================

class TestLinearRateDuration:
    """Test calculate_duration for linear_rate processes."""

    def test_simple_linear_rate(self, converter):
        """Calculate duration for simple linear rate process."""
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

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        duration = calculate_duration(process, inputs, outputs, converter)

        # 100 kg / 5 kg/hr = 20 hours
        assert duration == 20.0

    def test_linear_rate_with_output_scaling(self, converter):
        """Calculate duration using output as scaling_basis."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[Quantity(item_id="metal", qty=90.0, unit="kg")],
            time_model=TimeModel(
                type="linear_rate",
                rate=4.5,
                rate_unit="kg/hr",
                scaling_basis="metal"  # Output scaling
            )
        )

        inputs = {}
        outputs = {"metal": Quantity(item_id="metal", qty=90.0, unit="kg")}

        duration = calculate_duration(process, inputs, outputs, converter)

        # 90 kg / 4.5 kg/hr = 20 hours
        assert duration == 20.0

    def test_linear_rate_with_time_normalization(self, converter):
        """Calculate duration with rate in /min (normalized to /hr)."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="liquid", qty=600.0, unit="L")],
            outputs=[Quantity(item_id="processed", qty=600.0, unit="L")],
            time_model=TimeModel(
                type="linear_rate",
                rate=300.0,
                rate_unit="L/min",  # Will be normalized to L/hr
                scaling_basis="liquid"
            )
        )

        inputs = {"liquid": Quantity(item_id="liquid", qty=600.0, unit="L")}
        outputs = {}

        duration = calculate_duration(process, inputs, outputs, converter)

        # 300 L/min = 18000 L/hr
        # 600 L / 18000 L/hr = 0.0333... hours (2 minutes)
        assert duration == pytest.approx(0.0333, abs=0.001)

    def test_linear_rate_with_unit_conversion_volume_to_mass(self, converter):
        """Calculate duration with volume input and mass rate (via density)."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="water", qty=100.0, unit="L")],
            outputs=[Quantity(item_id="steam", qty=100.0, unit="L")],
            time_model=TimeModel(
                type="linear_rate",
                rate=5.0,
                rate_unit="kg/hr",  # Mass rate, input is volume
                scaling_basis="water"
            )
        )

        inputs = {"water": Quantity(item_id="water", qty=100.0, unit="L")}
        outputs = {}

        duration = calculate_duration(process, inputs, outputs, converter)

        # 100 L water = 100 kg (density 1000 kg/m³)
        # 100 kg / 5 kg/hr = 20 hours
        assert duration == 20.0

    def test_linear_rate_count_based(self, converter):
        """Calculate duration for count-based process."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="parts", qty=100.0, unit="unit")],
            outputs=[Quantity(item_id="assemblies", qty=10.0, unit="unit")],
            time_model=TimeModel(
                type="linear_rate",
                rate=12.0,
                rate_unit="unit/hr",
                scaling_basis="assemblies"
            )
        )

        inputs = {}
        outputs = {"assemblies": Quantity(item_id="assemblies", qty=10.0, unit="unit")}

        duration = calculate_duration(process, inputs, outputs, converter)

        # 10 units / 12 unit/hr = 0.833... hours
        assert duration == pytest.approx(0.833, abs=0.001)

    def test_linear_rate_missing_scaling_basis(self, converter):
        """Raise error if scaling_basis not found."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(
                type="linear_rate",
                rate=5.0,
                rate_unit="kg/hr",
                scaling_basis="nonexistent_item"
            )
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        with pytest.raises(CalculationError, match="scaling_basis .* not found"):
            calculate_duration(process, inputs, outputs, converter)

    def test_linear_rate_invalid_rate_unit(self, converter):
        """Raise error for invalid rate_unit format."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(
                type="linear_rate",
                rate=5.0,
                rate_unit="invalid_unit",  # Not compound
                scaling_basis="ore"
            )
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        with pytest.raises(CalculationError, match="invalid rate_unit"):
            calculate_duration(process, inputs, outputs, converter)

    def test_linear_rate_zero_rate(self, converter):
        """Raise error for zero rate."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(
                type="linear_rate",
                rate=0.0,  # Invalid
                rate_unit="kg/hr",
                scaling_basis="ore"
            )
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        with pytest.raises(CalculationError, match="invalid rate"):
            calculate_duration(process, inputs, outputs, converter)

    def test_linear_rate_unit_conversion_not_possible(self, converter):
        """Raise error if unit conversion not possible."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="unknown_item", qty=100.0, unit="L")],
            outputs=[],
            time_model=TimeModel(
                type="linear_rate",
                rate=5.0,
                rate_unit="kg/hr",  # Need L->kg conversion, but no density
                scaling_basis="unknown_item"
            )
        )

        inputs = {"unknown_item": Quantity(item_id="unknown_item", qty=100.0, unit="L")}
        outputs = {}

        with pytest.raises(CalculationError, match="cannot convert"):
            calculate_duration(process, inputs, outputs, converter)


# =============================================================================
# Duration Calculation Tests (Batch)
# =============================================================================

class TestBatchDuration:
    """Test calculate_duration for batch processes."""

    def test_simple_batch(self, converter):
        """Calculate duration for simple batch process."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="parts", qty=10.0, unit="unit")],
            outputs=[Quantity(item_id="assembly", qty=1.0, unit="unit")],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=2.0,
                setup_hr=0.0
            )
        )

        duration = calculate_duration(process, {}, {}, converter)

        # 0 + 2 = 2 hours
        assert duration == 2.0

    def test_batch_with_setup(self, converter):
        """Calculate duration for batch with setup time."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[],
            outputs=[],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=2.0,
                setup_hr=0.5
            )
        )

        duration = calculate_duration(process, {}, {}, converter)

        # 0.5 + 2 = 2.5 hours
        assert duration == 2.5

    def test_batch_zero_hr_per_batch(self, converter):
        """Raise error for zero hr_per_batch."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[],
            outputs=[],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=0.0,  # Invalid
                setup_hr=0.0
            )
        )

        with pytest.raises(CalculationError, match="invalid hr_per_batch"):
            calculate_duration(process, {}, {}, converter)

    def test_batch_with_scaled_output_quantity(self, converter):
        """Calculate duration for batch process with scaled output quantity."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="regolith", qty=10.0, unit="kg")],
            outputs=[Quantity(item_id="carbon", qty=0.3, unit="kg")],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=1.5,
                setup_hr=0.0
            )
        )

        # Request 10 kg output (33.33 batches)
        outputs = {"carbon": Quantity(item_id="carbon", qty=10.0, unit="kg")}

        duration = calculate_duration(process, {}, outputs, converter)

        # 33.33 batches × 1.5 hr/batch = 50 hours
        assert duration == pytest.approx(50.0, abs=0.01)

    def test_batch_with_scaled_output_and_setup(self, converter):
        """Calculate duration for batch with scaled output and setup time."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="material", qty=5.0, unit="kg")],
            outputs=[Quantity(item_id="product", qty=1.0, unit="kg")],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=2.0,
                setup_hr=0.5
            )
        )

        # Request 5 kg output (5 batches)
        outputs = {"product": Quantity(item_id="product", qty=5.0, unit="kg")}

        duration = calculate_duration(process, {}, outputs, converter)

        # 0.5 + (5 batches × 2 hr/batch) = 10.5 hours
        assert duration == 10.5

    def test_batch_with_unit_conversion_in_output(self, converter):
        """Calculate duration for batch with unit conversion."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="ore", qty=1000.0, unit="kg")],
            outputs=[Quantity(item_id="metal", qty=1.0, unit="kg")],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=3.0,
                setup_hr=0.0
            )
        )

        # Request 2000 g output (2 kg = 2 batches)
        outputs = {"metal": Quantity(item_id="metal", qty=2000.0, unit="g")}

        duration = calculate_duration(process, {}, outputs, converter)

        # 2 batches × 3 hr/batch = 6 hours
        assert duration == 6.0

    def test_batch_default_quantity_no_scaling(self, converter):
        """Verify batch without scaled output uses default duration."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="material", qty=10.0, unit="kg")],
            outputs=[Quantity(item_id="product", qty=1.0, unit="kg")],
            time_model=TimeModel(
                type="batch",
                hr_per_batch=2.0,
                setup_hr=0.5
            )
        )

        # No outputs provided - should use default (1 batch)
        duration = calculate_duration(process, {}, {}, converter)

        # 0.5 + 2.0 = 2.5 hours (1 batch)
        assert duration == 2.5


# =============================================================================
# Energy Calculation Tests (Per-Unit)
# =============================================================================

class TestPerUnitEnergy:
    """Test calculate_energy for per_unit energy model."""

    def test_simple_per_unit_energy(self, converter):
        """Calculate energy for simple per-unit process."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[Quantity(item_id="metal", qty=90.0, unit="kg")],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore"),
            energy_model=EnergyModel(
                type="per_unit",
                value=2.0,
                unit="kWh/kg",
                scaling_basis="ore"
            )
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        energy = calculate_energy(process, inputs, outputs, converter)

        # 100 kg × 2 kWh/kg = 200 kWh
        assert energy == 200.0

    def test_per_unit_energy_with_output_scaling(self, converter):
        """Calculate energy using output as scaling_basis."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[Quantity(item_id="metal", qty=90.0, unit="kg")],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore"),
            energy_model=EnergyModel(
                type="per_unit",
                value=3.0,
                unit="kWh/kg",
                scaling_basis="metal"  # Output scaling
            )
        )

        inputs = {}
        outputs = {"metal": Quantity(item_id="metal", qty=90.0, unit="kg")}

        energy = calculate_energy(process, inputs, outputs, converter)

        # 90 kg × 3 kWh/kg = 270 kWh
        assert energy == 270.0

    def test_per_unit_energy_with_unit_conversion(self, converter):
        """Calculate energy with volume input and mass-based energy (via density)."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="water", qty=100.0, unit="L")],
            outputs=[Quantity(item_id="steam", qty=100.0, unit="L")],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="water"),
            energy_model=EnergyModel(
                type="per_unit",
                value=50.0,
                unit="kWh/kg",  # Mass-based energy, input is volume
                scaling_basis="water"
            )
        )

        inputs = {"water": Quantity(item_id="water", qty=100.0, unit="L")}
        outputs = {}

        energy = calculate_energy(process, inputs, outputs, converter)

        # 100 L water = 100 kg (density 1000 kg/m³)
        # 100 kg × 50 kWh/kg = 5000 kWh
        assert energy == 5000.0

    def test_per_unit_energy_count_based(self, converter):
        """Calculate energy for count-based energy model."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="parts", qty=10.0, unit="unit")],
            outputs=[Quantity(item_id="assemblies", qty=10.0, unit="unit")],
            time_model=TimeModel(type="linear_rate", rate=12.0, rate_unit="unit/hr", scaling_basis="assemblies"),
            energy_model=EnergyModel(
                type="per_unit",
                value=5.0,
                unit="kWh/unit",
                scaling_basis="assemblies"
            )
        )

        inputs = {}
        outputs = {"assemblies": Quantity(item_id="assemblies", qty=10.0, unit="unit")}

        energy = calculate_energy(process, inputs, outputs, converter)

        # 10 units × 5 kWh/unit = 50 kWh
        assert energy == 50.0

    def test_per_unit_energy_no_model(self, converter):
        """Return 0 if no energy model."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore"),
            energy_model=None  # No energy model
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        energy = calculate_energy(process, inputs, outputs, converter)

        assert energy == 0.0

    def test_per_unit_energy_missing_scaling_basis(self, converter):
        """Raise error if energy scaling_basis not found."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore"),
            energy_model=EnergyModel(
                type="per_unit",
                value=2.0,
                unit="kWh/kg",
                scaling_basis="nonexistent_item"
            )
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        with pytest.raises(CalculationError, match="energy scaling_basis .* not found"):
            calculate_energy(process, inputs, outputs, converter)

    def test_per_unit_energy_invalid_unit(self, converter):
        """Raise error for invalid energy unit format."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=100.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore"),
            energy_model=EnergyModel(
                type="per_unit",
                value=2.0,
                unit="invalid_unit",  # Not compound
                scaling_basis="ore"
            )
        )

        inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        outputs = {}

        with pytest.raises(CalculationError, match="invalid energy unit"):
            calculate_energy(process, inputs, outputs, converter)


# =============================================================================
# Energy Calculation Tests (Fixed Per Batch)
# =============================================================================

class TestFixedEnergy:
    """Test calculate_energy for fixed_per_batch energy model."""

    def test_simple_fixed_energy(self, converter):
        """Calculate energy for simple fixed batch process."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[],
            outputs=[],
            time_model=TimeModel(type="batch", hr_per_batch=2.0, setup_hr=0.0),
            energy_model=EnergyModel(
                type="fixed_per_batch",
                value=100.0,
                unit="kWh"
            )
        )

        energy = calculate_energy(process, {}, {}, converter)

        assert energy == 100.0

    def test_fixed_energy_zero_value(self, converter):
        """Raise error for zero fixed energy value."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[],
            outputs=[],
            time_model=TimeModel(type="batch", hr_per_batch=2.0, setup_hr=0.0),
            energy_model=EnergyModel(
                type="fixed_per_batch",
                value=0.0,  # Invalid
                unit="kWh"
            )
        )

        with pytest.raises(CalculationError, match="invalid fixed energy value"):
            calculate_energy(process, {}, {}, converter)

    def test_fixed_energy_with_scaled_output_quantity(self, converter):
        """Calculate energy for batch process with scaled output quantity."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="regolith", qty=10.0, unit="kg")],
            outputs=[Quantity(item_id="carbon", qty=0.3, unit="kg")],
            time_model=TimeModel(type="batch", hr_per_batch=1.5, setup_hr=0.0),
            energy_model=EnergyModel(
                type="fixed_per_batch",
                value=2.0,
                unit="kWh"
            )
        )

        # Request 10 kg output (33.33 batches)
        outputs = {"carbon": Quantity(item_id="carbon", qty=10.0, unit="kg")}

        energy = calculate_energy(process, {}, outputs, converter)

        # 33.33 batches × 2 kWh/batch = 66.67 kWh
        assert energy == pytest.approx(66.67, abs=0.01)

    def test_fixed_energy_with_multiple_batches(self, converter):
        """Calculate energy for multiple batches."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="material", qty=5.0, unit="kg")],
            outputs=[Quantity(item_id="product", qty=1.0, unit="kg")],
            time_model=TimeModel(type="batch", hr_per_batch=2.0, setup_hr=0.0),
            energy_model=EnergyModel(
                type="fixed_per_batch",
                value=10.0,
                unit="kWh"
            )
        )

        # Request 5 kg output (5 batches)
        outputs = {"product": Quantity(item_id="product", qty=5.0, unit="kg")}

        energy = calculate_energy(process, {}, outputs, converter)

        # 5 batches × 10 kWh/batch = 50 kWh
        assert energy == 50.0

    def test_fixed_energy_with_unit_conversion(self, converter):
        """Calculate energy for batch with unit conversion in output."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="ore", qty=1000.0, unit="kg")],
            outputs=[Quantity(item_id="metal", qty=1.0, unit="kg")],
            time_model=TimeModel(type="batch", hr_per_batch=3.0, setup_hr=0.0),
            energy_model=EnergyModel(
                type="fixed_per_batch",
                value=15.0,
                unit="kWh"
            )
        )

        # Request 2000 g output (2 kg = 2 batches)
        outputs = {"metal": Quantity(item_id="metal", qty=2000.0, unit="g")}

        energy = calculate_energy(process, {}, outputs, converter)

        # 2 batches × 15 kWh/batch = 30 kWh
        assert energy == 30.0

    def test_fixed_energy_default_quantity_no_scaling(self, converter):
        """Verify fixed energy without scaled output uses default energy."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="batch",
            inputs=[Quantity(item_id="material", qty=10.0, unit="kg")],
            outputs=[Quantity(item_id="product", qty=1.0, unit="kg")],
            time_model=TimeModel(type="batch", hr_per_batch=2.0, setup_hr=0.0),
            energy_model=EnergyModel(
                type="fixed_per_batch",
                value=20.0,
                unit="kWh"
            )
        )

        # No outputs provided - should use default (1 batch)
        energy = calculate_energy(process, {}, {}, converter)

        # 1 batch × 20 kWh/batch = 20 kWh
        assert energy == 20.0


# =============================================================================
# Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_duration_with_very_small_quantity(self, converter):
        """Calculate duration with very small quantity."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=0.001, unit="kg")],
            outputs=[],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore")
        )

        inputs = {"ore": Quantity(item_id="ore", qty=0.001, unit="kg")}
        outputs = {}

        duration = calculate_duration(process, inputs, outputs, converter)

        # 0.001 kg / 5 kg/hr = 0.0002 hours
        assert duration == pytest.approx(0.0002)

    def test_energy_with_very_large_quantity(self, converter):
        """Calculate energy with very large quantity."""
        process = Process(
            id="test_v0",
            kind="process",
            process_type="continuous",
            inputs=[Quantity(item_id="ore", qty=1000000.0, unit="kg")],
            outputs=[],
            time_model=TimeModel(type="linear_rate", rate=5.0, rate_unit="kg/hr", scaling_basis="ore"),
            energy_model=EnergyModel(type="per_unit", value=2.0, unit="kWh/kg", scaling_basis="ore")
        )

        inputs = {"ore": Quantity(item_id="ore", qty=1000000.0, unit="kg")}
        outputs = {}

        energy = calculate_energy(process, inputs, outputs, converter)

        # 1,000,000 kg × 2 kWh/kg = 2,000,000 kWh
        assert energy == 2000000.0
