"""
Tests for kb_core.unit_converter

Tests compound unit parsing, time normalization, conversion validation,
and all conversion strategies per ADR-016.
"""
import pytest

from src.kb_core.unit_converter import (
    UnitConverter,
    is_valid_unit,
    get_unit_category,
    parse_compound_unit,
    normalize_time_to_hours,
    normalize_rate_to_hours,
    MASS_UNITS,
    VOLUME_UNITS,
    TIME_UNITS,
    COUNT_UNITS,
    ENERGY_UNITS,
)


# =============================================================================
# Mock KB Loader
# =============================================================================

class MockKBLoader:
    """Mock KB loader for testing."""

    def __init__(self):
        # Standard conversion factors (per ADR-016)
        self.conversions = {
            # Mass
            ("kg", "g"): 1000.0,
            ("kg", "tonne"): 0.001,
            # Volume
            ("L", "mL"): 1000.0,
            ("m3", "L"): 1000.0,
            # Time
            ("hr", "min"): 60.0,
            ("hr", "s"): 3600.0,
            ("day", "hr"): 24.0,
            # Energy
            ("kWh", "MJ"): 3.6,
            ("MJ", "GJ"): 0.001,
            # Count synonyms
            ("unit", "each"): 1.0,
            ("unit", "count"): 1.0,
        }

        # Material densities (kg/m³)
        self.densities = {
            "water": 1000.0,
            "aluminum": 2700.0,
            "steel": 7850.0,
        }

        # Item definitions
        self.items = {
            "motor_electric_small": {"id": "motor_electric_small", "mass_kg": 12.0},
            "battery_pack": {"id": "battery_pack", "mass_kg": 45.0},
            "container_tank": {"id": "container_tank", "mass_kg": 100.0},
        }

    def get_unit_conversion(self, from_unit: str, to_unit: str):
        """Get conversion factor."""
        return self.conversions.get((from_unit, to_unit))

    def get_material_density(self, material_name: str):
        """Get material density."""
        return self.densities.get(material_name)

    def get_item(self, item_id: str):
        """Get item definition."""
        return self.items.get(item_id)


@pytest.fixture
def kb_loader():
    """Fixture providing mock KB loader."""
    return MockKBLoader()


@pytest.fixture
def converter(kb_loader):
    """Fixture providing unit converter with mock KB."""
    return UnitConverter(kb_loader)


# =============================================================================
# Unit Validation Tests
# =============================================================================

class TestUnitValidation:
    """Test unit validation functions."""

    def test_is_valid_unit_mass(self):
        """Valid mass units are recognized."""
        assert is_valid_unit("kg")
        assert is_valid_unit("g")
        assert is_valid_unit("tonne")

    def test_is_valid_unit_volume(self):
        """Valid volume units are recognized."""
        assert is_valid_unit("L")
        assert is_valid_unit("m3")
        assert is_valid_unit("mL")
        assert is_valid_unit("liter")

    def test_is_valid_unit_time(self):
        """Valid time units are recognized."""
        assert is_valid_unit("hr")
        assert is_valid_unit("min")
        assert is_valid_unit("s")
        assert is_valid_unit("day")

    def test_is_valid_unit_energy(self):
        """Valid energy units are recognized."""
        assert is_valid_unit("kWh")
        assert is_valid_unit("MJ")
        assert is_valid_unit("GJ")

    def test_is_valid_unit_count(self):
        """Valid count units are recognized."""
        assert is_valid_unit("unit")
        assert is_valid_unit("each")
        assert is_valid_unit("count")

    def test_is_valid_unit_invalid(self):
        """Invalid units are rejected."""
        assert not is_valid_unit("invalid")
        assert not is_valid_unit("kg/hr")  # Compound units not single units
        assert not is_valid_unit("")

    def test_get_unit_category_mass(self):
        """Mass units return correct category."""
        assert get_unit_category("kg") == "mass"
        assert get_unit_category("g") == "mass"

    def test_get_unit_category_volume(self):
        """Volume units return correct category."""
        assert get_unit_category("L") == "volume"
        assert get_unit_category("m3") == "volume"

    def test_get_unit_category_time(self):
        """Time units return correct category."""
        assert get_unit_category("hr") == "time"
        assert get_unit_category("min") == "time"

    def test_get_unit_category_unknown(self):
        """Unknown units return None."""
        assert get_unit_category("invalid") is None


# =============================================================================
# Compound Unit Parsing Tests
# =============================================================================

class TestCompoundUnitParsing:
    """Test parse_compound_unit per ADR-016."""

    def test_parse_mass_rate(self):
        """Parse mass rate units."""
        assert parse_compound_unit("kg/hr") == ("kg", "hr")
        assert parse_compound_unit("g/min") == ("g", "min")

    def test_parse_volume_rate(self):
        """Parse volume rate units."""
        assert parse_compound_unit("L/min") == ("L", "min")
        assert parse_compound_unit("L/hr") == ("L", "hr")

    def test_parse_count_rate(self):
        """Parse count rate units."""
        assert parse_compound_unit("unit/hr") == ("unit", "hr")
        assert parse_compound_unit("each/min") == ("each", "min")

    def test_parse_energy_intensity(self):
        """Parse energy intensity units."""
        assert parse_compound_unit("kWh/kg") == ("kWh", "kg")
        assert parse_compound_unit("MJ/unit") == ("MJ", "unit")

    def test_parse_with_whitespace(self):
        """Parse compound units with whitespace."""
        assert parse_compound_unit("kg / hr") == ("kg", "hr")
        assert parse_compound_unit("L  /  min") == ("L", "min")

    def test_parse_not_compound_unit(self):
        """Reject non-compound units."""
        with pytest.raises(ValueError, match="Not a compound unit"):
            parse_compound_unit("kg")

    def test_parse_invalid_format(self):
        """Reject invalid compound unit format."""
        with pytest.raises(ValueError, match="Invalid compound unit format"):
            parse_compound_unit("kg/hr/min")

    def test_parse_unknown_numerator(self):
        """Reject unknown numerator unit."""
        with pytest.raises(ValueError, match="Unknown numerator unit"):
            parse_compound_unit("invalid/hr")

    def test_parse_unknown_denominator(self):
        """Reject unknown denominator unit."""
        with pytest.raises(ValueError, match="Unknown denominator unit"):
            parse_compound_unit("kg/invalid")


# =============================================================================
# Time Normalization Tests
# =============================================================================

class TestTimeNormalization:
    """Test normalize_time_to_hours per ADR-016."""

    def test_hours_to_hours(self):
        """Hours remain unchanged."""
        assert normalize_time_to_hours(5.0, "hr") == 5.0

    def test_minutes_to_hours(self):
        """Minutes convert to hours."""
        assert normalize_time_to_hours(60.0, "min") == 1.0
        assert normalize_time_to_hours(30.0, "min") == 0.5

    def test_seconds_to_hours(self):
        """Seconds convert to hours."""
        assert normalize_time_to_hours(3600.0, "s") == 1.0
        assert normalize_time_to_hours(1800.0, "s") == 0.5

    def test_days_to_hours(self):
        """Days convert to hours."""
        assert normalize_time_to_hours(1.0, "day") == 24.0
        assert normalize_time_to_hours(2.0, "day") == 48.0

    def test_invalid_time_unit(self):
        """Reject non-time units."""
        with pytest.raises(ValueError, match="Not a time unit"):
            normalize_time_to_hours(10.0, "kg")


# =============================================================================
# Rate Normalization Tests
# =============================================================================

class TestRateNormalization:
    """Test normalize_rate_to_hours per ADR-016."""

    def test_rate_per_hour_unchanged(self):
        """Rate per hour remains unchanged."""
        assert normalize_rate_to_hours(5.0, "hr") == 5.0

    def test_rate_per_minute_to_hour(self):
        """Rate per minute converts to per hour."""
        assert normalize_rate_to_hours(300.0, "min") == 18000.0
        # 300 L/min = 18000 L/hr

    def test_rate_per_second_to_hour(self):
        """Rate per second converts to per hour."""
        assert normalize_rate_to_hours(1.0, "s") == 3600.0
        # 1 L/s = 3600 L/hr

    def test_rate_per_day_to_hour(self):
        """Rate per day converts to per hour."""
        assert normalize_rate_to_hours(240.0, "day") == 10.0
        # 240 L/day = 10 L/hr

    def test_rate_invalid_time_unit(self):
        """Reject non-time units."""
        with pytest.raises(ValueError, match="Not a time unit"):
            normalize_rate_to_hours(10.0, "kg")


# =============================================================================
# Convertibility Checking Tests
# =============================================================================

class TestConvertibilityChecking:
    """Test can_convert per ADR-016."""

    def test_same_unit_convertible(self, converter):
        """Same unit is always convertible."""
        assert converter.can_convert("kg", "kg")
        assert converter.can_convert("L", "L")

    def test_direct_conversion_exists(self, converter):
        """Direct conversions via factors."""
        assert converter.can_convert("kg", "g")
        assert converter.can_convert("L", "mL")

    def test_reverse_conversion_exists(self, converter):
        """Reverse conversions work."""
        assert converter.can_convert("g", "kg")
        assert converter.can_convert("mL", "L")

    def test_mass_volume_with_density(self, converter):
        """Mass <-> volume convertible with density."""
        assert converter.can_convert("kg", "L", item_id="water")
        assert converter.can_convert("L", "kg", item_id="aluminum")

    def test_mass_volume_without_density(self, converter):
        """Mass <-> volume not convertible without density."""
        assert not converter.can_convert("kg", "L", item_id="unknown_material")

    def test_count_mass_with_mass_kg(self, converter):
        """Count <-> mass convertible with mass_kg."""
        assert converter.can_convert("unit", "kg", item_id="motor_electric_small")
        assert converter.can_convert("kg", "unit", item_id="battery_pack")

    def test_count_mass_without_mass_kg(self, converter):
        """Count <-> mass not convertible without mass_kg."""
        assert not converter.can_convert("unit", "kg", item_id="unknown_item")

    def test_incompatible_categories(self, converter):
        """Incompatible categories not convertible."""
        assert not converter.can_convert("kg", "kWh")
        assert not converter.can_convert("L", "hr")


# =============================================================================
# Direct Conversion Tests
# =============================================================================

class TestDirectConversions:
    """Test direct conversions via conversion factors."""

    def test_mass_conversions(self, converter):
        """Mass unit conversions."""
        assert converter.convert(1.0, "kg", "g") == 1000.0
        assert converter.convert(1000.0, "g", "kg") == 1.0

    def test_volume_conversions(self, converter):
        """Volume unit conversions."""
        assert converter.convert(1.0, "L", "mL") == 1000.0
        assert converter.convert(1.0, "m3", "L") == 1000.0

    def test_time_conversions(self, converter):
        """Time unit conversions."""
        assert converter.convert(1.0, "hr", "min") == 60.0
        assert converter.convert(1.0, "day", "hr") == 24.0

    def test_count_synonym_conversions(self, converter):
        """Count synonyms convert 1:1."""
        assert converter.convert(5.0, "unit", "each") == 5.0
        assert converter.convert(10.0, "unit", "count") == 10.0

    def test_same_unit_no_conversion(self, converter):
        """Same unit returns unchanged."""
        assert converter.convert(5.0, "kg", "kg") == 5.0


# =============================================================================
# Mass <-> Volume Conversion Tests
# =============================================================================

class TestMassVolumeConversions:
    """Test mass <-> volume conversions via density."""

    def test_volume_to_mass_water(self, converter):
        """Water: 10 L → 10 kg (density 1000 kg/m³)."""
        # 10 L = 0.01 m³, 0.01 m³ × 1000 kg/m³ = 10 kg
        result = converter.convert(10.0, "L", "kg", item_id="water")
        assert result == pytest.approx(10.0)

    def test_mass_to_volume_water(self, converter):
        """Water: 10 kg → 10 L (density 1000 kg/m³)."""
        # 10 kg / 1000 kg/m³ = 0.01 m³ = 10 L
        result = converter.convert(10.0, "kg", "L", item_id="water")
        assert result == pytest.approx(10.0)

    def test_volume_to_mass_aluminum(self, converter):
        """Aluminum: 1 L → 2.7 kg (density 2700 kg/m³)."""
        # 1 L = 0.001 m³, 0.001 m³ × 2700 kg/m³ = 2.7 kg
        result = converter.convert(1.0, "L", "kg", item_id="aluminum")
        assert result == pytest.approx(2.7)

    def test_mass_to_volume_aluminum(self, converter):
        """Aluminum: 2.7 kg → 1 L (density 2700 kg/m³)."""
        # 2.7 kg / 2700 kg/m³ = 0.001 m³ = 1 L
        result = converter.convert(2.7, "kg", "L", item_id="aluminum")
        assert result == pytest.approx(1.0)

    def test_mass_volume_no_density(self, converter):
        """Conversion fails without density."""
        result = converter.convert(10.0, "L", "kg", item_id="unknown")
        assert result is None


# =============================================================================
# Count <-> Mass Conversion Tests
# =============================================================================

class TestCountMassConversions:
    """Test count <-> mass conversions via item mass_kg."""

    def test_count_to_mass_motor(self, converter):
        """Motor: 1 unit → 12 kg (mass_kg: 12)."""
        result = converter.convert(1.0, "unit", "kg", item_id="motor_electric_small")
        assert result == 12.0

    def test_count_to_mass_multiple_motors(self, converter):
        """Motor: 5 units → 60 kg."""
        result = converter.convert(5.0, "unit", "kg", item_id="motor_electric_small")
        assert result == 60.0

    def test_mass_to_count_battery(self, converter):
        """Battery: 90 kg → 2 units (mass_kg: 45)."""
        result = converter.convert(90.0, "kg", "unit", item_id="battery_pack")
        assert result == 2.0

    def test_count_synonym_to_mass(self, converter):
        """Count synonyms work for mass conversion."""
        result = converter.convert(1.0, "each", "kg", item_id="motor_electric_small")
        assert result == 12.0

    def test_count_mass_no_mass_kg(self, converter):
        """Conversion fails without mass_kg."""
        result = converter.convert(1.0, "unit", "kg", item_id="unknown")
        assert result is None


# =============================================================================
# Normalization Tests
# =============================================================================

class TestNormalization:
    """Test normalize_to_standard_unit."""

    def test_normalize_mass(self, converter):
        """Normalize mass to kg."""
        qty, unit = converter.normalize_to_standard_unit(1000.0, "g")
        assert qty == 1.0
        assert unit == "kg"

    def test_normalize_volume(self, converter):
        """Normalize volume to m3."""
        qty, unit = converter.normalize_to_standard_unit(1000.0, "L")
        assert qty == 1.0
        assert unit == "m3"

    def test_normalize_count(self, converter):
        """Normalize count to unit."""
        qty, unit = converter.normalize_to_standard_unit(5.0, "each")
        assert qty == 5.0
        assert unit == "unit"

    def test_normalize_time(self, converter):
        """Normalize time to hr."""
        qty, unit = converter.normalize_to_standard_unit(60.0, "min")
        assert qty == 1.0
        assert unit == "hr"

    def test_normalize_already_standard(self, converter):
        """Already standard units unchanged."""
        qty, unit = converter.normalize_to_standard_unit(5.0, "kg")
        assert qty == 5.0
        assert unit == "kg"


# =============================================================================
# Integration Tests
# =============================================================================

class TestIntegration:
    """Integration tests for complex conversion scenarios."""

    def test_compound_unit_with_time_normalization(self):
        """Parse and normalize compound unit with time."""
        # Parse "L/min"
        numerator, denominator = parse_compound_unit("L/min")
        assert numerator == "L"
        assert denominator == "min"

        # Normalize rate to /hr
        rate = normalize_rate_to_hours(300.0, denominator)
        assert rate == 18000.0  # 300 L/min = 18000 L/hr

    def test_cross_unit_conversion_chain(self, converter):
        """Water: L → kg conversion (volume to mass)."""
        # 100 L water → 100 kg
        result = converter.convert(100.0, "L", "kg", item_id="water")
        assert result == pytest.approx(100.0)

    def test_count_to_mass_to_volume(self, converter):
        """Cannot chain conversions without explicit data."""
        # Motors don't have density, so can't convert count → volume directly
        result = converter.convert(1.0, "unit", "L", item_id="motor_electric_small")
        assert result is None  # No chained conversions

    def test_validate_then_convert(self, converter):
        """Validate before converting (per ADR-016)."""
        # Check convertibility first
        assert converter.can_convert("kg", "g")

        # Then convert
        result = converter.convert(1.0, "kg", "g")
        assert result == 1000.0


# =============================================================================
# Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_zero_quantity(self, converter):
        """Zero quantities convert correctly."""
        assert converter.convert(0.0, "kg", "g") == 0.0

    def test_very_small_quantity(self, converter):
        """Very small quantities preserve precision."""
        result = converter.convert(0.001, "kg", "g")
        assert result == pytest.approx(1.0)

    def test_very_large_quantity(self, converter):
        """Very large quantities convert correctly."""
        result = converter.convert(1000000.0, "kg", "g")
        assert result == 1000000000.0

    def test_conversion_not_possible(self, converter):
        """Returns None when conversion not possible."""
        result = converter.convert(10.0, "kg", "unknown_unit")
        assert result is None

    def test_parse_empty_string(self):
        """Empty string raises error."""
        with pytest.raises(ValueError):
            parse_compound_unit("")

    def test_normalize_zero_time(self):
        """Zero time normalizes to zero."""
        assert normalize_time_to_hours(0.0, "min") == 0.0
