"""
Unit Converter - Handle unit conversions between mass, volume, count, time, energy

Implements ADR-016: Unit Conversion and Type System

Supports:
1. Direct conversions (kg -> g via conversion factors)
2. Mass <-> Volume conversions (via material densities)
3. Count <-> Mass conversions (via item definitions)
4. Compound unit parsing (kg/hr, kWh/kg)
5. Time unit normalization (min/s/day -> hr)
6. Conversion validation (can_convert checks)
"""
from __future__ import annotations

from typing import Optional, Protocol


class KBLoaderProtocol(Protocol):
    """Protocol for KB loader to avoid circular dependencies."""

    def get_unit_conversion(self, from_unit: str, to_unit: str) -> Optional[float]:
        """Get conversion factor from KB."""
        ...

    def get_material_density(self, material_name: str) -> Optional[float]:
        """Get material density in kg/m³."""
        ...

    def get_item(self, item_id: str) -> Optional[dict]:
        """Get item definition."""
        ...


# Unit categories (per ADR-016)
MASS_UNITS = {"kg", "g", "tonne", "lb"}
VOLUME_UNITS = {"m3", "L", "mL", "liter"}  # Note: m3 and liter are aliases
TIME_UNITS = {"hr", "min", "s", "day"}
ENERGY_UNITS = {"kWh", "MJ", "GJ", "J", "BTU"}
COUNT_UNITS = {"unit", "each", "count", "set", "kit"}
LENGTH_UNITS = {"m", "cm", "mm", "km"}

ALL_UNITS = (
    MASS_UNITS | VOLUME_UNITS | TIME_UNITS |
    ENERGY_UNITS | COUNT_UNITS | LENGTH_UNITS
)

# Standard units per category
STANDARD_UNITS = {
    "mass": "kg",
    "volume": "m3",
    "time": "hr",
    "energy": "kWh",
    "count": "unit",
    "length": "m",
}


def is_valid_unit(unit: str) -> bool:
    """
    Check if unit is a known unit.

    Args:
        unit: Unit string to validate

    Returns:
        True if unit is known, False otherwise
    """
    return unit in ALL_UNITS


def get_unit_category(unit: str) -> Optional[str]:
    """
    Get category for a unit.

    Args:
        unit: Unit string

    Returns:
        Category name ("mass", "volume", "time", etc.) or None if unknown
    """
    if unit in MASS_UNITS:
        return "mass"
    elif unit in VOLUME_UNITS:
        return "volume"
    elif unit in TIME_UNITS:
        return "time"
    elif unit in ENERGY_UNITS:
        return "energy"
    elif unit in COUNT_UNITS:
        return "count"
    elif unit in LENGTH_UNITS:
        return "length"
    else:
        return None


def parse_compound_unit(unit_string: str) -> tuple[str, str]:
    """
    Parse compound unit string into numerator and denominator.

    Per ADR-016, compound units use format "X/Y".

    Args:
        unit_string: Compound unit (e.g., "kg/hr", "L/min", "kWh/kg")

    Returns:
        (numerator_unit, denominator_unit)

    Raises:
        ValueError: If not a compound unit or format is invalid

    Examples:
        >>> parse_compound_unit("kg/hr")
        ("kg", "hr")
        >>> parse_compound_unit("L/min")
        ("L", "min")
        >>> parse_compound_unit("kWh/kg")
        ("kWh", "kg")
        >>> parse_compound_unit("unit/hr")
        ("unit", "hr")
    """
    if "/" not in unit_string:
        raise ValueError(f"Not a compound unit: {unit_string}")

    parts = unit_string.split("/")
    if len(parts) != 2:
        raise ValueError(f"Invalid compound unit format: {unit_string}")

    numerator = parts[0].strip()
    denominator = parts[1].strip()

    # Validate both parts are known units
    if not is_valid_unit(numerator):
        raise ValueError(f"Unknown numerator unit: {numerator}")
    if not is_valid_unit(denominator):
        raise ValueError(f"Unknown denominator unit: {denominator}")

    return (numerator, denominator)


def normalize_time_to_hours(quantity: float, time_unit: str) -> float:
    """
    Normalize time quantity to hours.

    Per ADR-016, all time units are normalized to hours internally.

    Args:
        quantity: Time quantity
        time_unit: Time unit (hr, min, s, day)

    Returns:
        Quantity in hours

    Raises:
        ValueError: If time_unit is not a valid time unit

    Examples:
        >>> normalize_time_to_hours(60, "min")
        1.0
        >>> normalize_time_to_hours(3600, "s")
        1.0
        >>> normalize_time_to_hours(2, "day")
        48.0
        >>> normalize_time_to_hours(5, "hr")
        5.0
    """
    if time_unit not in TIME_UNITS:
        raise ValueError(f"Not a time unit: {time_unit}")

    # Conversion factors to hours
    if time_unit == "hr":
        return quantity
    elif time_unit == "min":
        return quantity / 60.0
    elif time_unit == "s":
        return quantity / 3600.0
    elif time_unit == "day":
        return quantity * 24.0
    else:
        raise ValueError(f"Unknown time unit: {time_unit}")


def normalize_rate_to_hours(rate: float, time_unit: str) -> float:
    """
    Normalize rate denominator to /hr.

    Per ADR-016, rates with time denominators are normalized to /hr.

    Args:
        rate: Rate value (e.g., 300 in "300 L/min")
        time_unit: Time unit in denominator (min, s, day, hr)

    Returns:
        Rate normalized to /hr

    Raises:
        ValueError: If time_unit is not a valid time unit

    Examples:
        >>> normalize_rate_to_hours(300, "min")
        18000.0  # 300 L/min = 18000 L/hr
        >>> normalize_rate_to_hours(240, "day")
        10.0  # 240 L/day = 10 L/hr
        >>> normalize_rate_to_hours(5, "hr")
        5.0  # Already in /hr
    """
    if time_unit not in TIME_UNITS:
        raise ValueError(f"Not a time unit: {time_unit}")

    # Convert X per <time_unit> to X per hour
    if time_unit == "hr":
        return rate
    elif time_unit == "min":
        return rate * 60.0  # 5/min = 300/hr
    elif time_unit == "s":
        return rate * 3600.0  # 1/s = 3600/hr
    elif time_unit == "day":
        return rate / 24.0  # 240/day = 10/hr
    else:
        raise ValueError(f"Unknown time unit: {time_unit}")


class UnitConverter:
    """
    Handles unit conversions for the simulation.

    Uses:
    - Conversion factors from KB (kg -> g, etc.)
    - Material densities (mass -> volume)
    - Item definitions (count -> mass/volume)

    Enhanced per ADR-016 with:
    - Compound unit parsing
    - Time normalization
    - Conversion validation
    """

    def __init__(self, kb_loader: KBLoaderProtocol):
        self.kb = kb_loader

    def convert(
        self,
        quantity: float,
        from_unit: str,
        to_unit: str,
        item_id: Optional[str] = None,
    ) -> Optional[float]:
        """
        Convert quantity from one unit to another.

        Args:
            quantity: Amount to convert
            from_unit: Source unit (e.g., "kg", "m3", "count")
            to_unit: Target unit (e.g., "g", "liter", "kg")
            item_id: Optional item ID for context-specific conversions

        Returns:
            Converted quantity, or None if conversion not possible
        """
        # Same unit - no conversion needed
        if from_unit == to_unit:
            return quantity

        # Try direct conversion via conversion factors
        result = self._try_direct_conversion(quantity, from_unit, to_unit)
        if result is not None:
            return result

        # Try mass <-> volume conversion via material density
        if item_id:
            result = self._try_mass_volume_conversion(
                quantity, from_unit, to_unit, item_id
            )
            if result is not None:
                return result

            # Try count <-> mass/volume conversion via item definition
            result = self._try_count_conversion(quantity, from_unit, to_unit, item_id)
            if result is not None:
                return result

        # No conversion available
        return None

    def can_convert(
        self,
        from_unit: str,
        to_unit: str,
        item_id: Optional[str] = None
    ) -> bool:
        """
        Check if conversion is possible.

        Per ADR-016, validates convertibility before attempting conversion.

        Args:
            from_unit: Source unit
            to_unit: Target unit
            item_id: Optional item ID for context-specific conversions

        Returns:
            True if conversion exists, False otherwise

        Examples:
            >>> converter.can_convert("kg", "g")
            True
            >>> converter.can_convert("kg", "L", item_id="water")
            True  # If water has density
            >>> converter.can_convert("unit", "kg", item_id="motor")
            True  # If motor has mass_kg
            >>> converter.can_convert("kg", "kWh")
            False  # Incompatible categories
        """
        # Same unit always convertible
        if from_unit == to_unit:
            return True

        # Try direct conversion
        if self._has_conversion_factor(from_unit, to_unit):
            return True

        # Try mass <-> volume (requires item_id for density lookup)
        if item_id and self._is_mass_volume_pair(from_unit, to_unit):
            return self._has_material_density(item_id)

        # Try count <-> mass/volume (requires item_id)
        if item_id and self._is_count_conversion(from_unit, to_unit):
            return self._has_item_mass_or_volume(item_id)

        return False

    def _has_conversion_factor(self, from_unit: str, to_unit: str) -> bool:
        """Check if direct conversion factor exists."""
        factor = self.kb.get_unit_conversion(from_unit, to_unit)
        if factor is not None:
            return True

        # Try reverse
        reverse_factor = self.kb.get_unit_conversion(to_unit, from_unit)
        return reverse_factor is not None

    def _is_mass_volume_pair(self, unit1: str, unit2: str) -> bool:
        """Check if units are mass/volume pair."""
        return (
            (unit1 in MASS_UNITS and unit2 in VOLUME_UNITS) or
            (unit1 in VOLUME_UNITS and unit2 in MASS_UNITS)
        )

    def _is_count_conversion(self, from_unit: str, to_unit: str) -> bool:
        """Check if conversion involves count units."""
        return (
            (from_unit in COUNT_UNITS and to_unit in (MASS_UNITS | VOLUME_UNITS)) or
            (from_unit in (MASS_UNITS | VOLUME_UNITS) and to_unit in COUNT_UNITS)
        )

    def _has_material_density(self, item_id: str) -> bool:
        """Check if material has density data."""
        # Try using item_id as material name
        # TODO: Look up item definition to get material_class field
        density = self.kb.get_material_density(item_id)
        return density is not None

    def _has_item_mass_or_volume(self, item_id: str) -> bool:
        """Check if item has mass_kg or volume data."""
        item = self.kb.get_item(item_id)
        if not item:
            return False

        mass_per_unit = item.get("mass_kg") or item.get("mass_per_unit") or item.get("mass")
        return mass_per_unit is not None

    def _try_direct_conversion(
        self, quantity: float, from_unit: str, to_unit: str
    ) -> Optional[float]:
        """Try direct conversion using conversion factors from KB."""
        # Try direct conversion
        factor = self.kb.get_unit_conversion(from_unit, to_unit)
        if factor is not None:
            return quantity * factor

        # Try reverse conversion (from -> to via to -> from)
        reverse_factor = self.kb.get_unit_conversion(to_unit, from_unit)
        if reverse_factor is not None:
            return quantity / reverse_factor

        return None

    def _try_mass_volume_conversion(
        self, quantity: float, from_unit: str, to_unit: str, item_id: str
    ) -> Optional[float]:
        """Try mass <-> volume conversion using material density."""
        # Get material name from item_id
        # For now, try using item_id as material name
        # TODO: Look up item definition to get material_class field
        material_name = item_id

        density = self.kb.get_material_density(material_name)
        if density is None:
            return None

        # kg -> m3
        if from_unit in MASS_UNITS and to_unit in VOLUME_UNITS:
            # Convert to kg first
            mass_kg = self._convert_to_standard_mass(quantity, from_unit)
            if mass_kg is None:
                return None

            # kg to m3 via density
            volume_m3 = mass_kg / density

            # Convert m3 to target volume unit
            return self._convert_from_standard_volume(volume_m3, to_unit)

        # m3 -> kg
        if from_unit in VOLUME_UNITS and to_unit in MASS_UNITS:
            # Convert to m3 first
            volume_m3 = self._convert_to_standard_volume(quantity, from_unit)
            if volume_m3 is None:
                return None

            # m3 to kg via density
            mass_kg = volume_m3 * density

            # Convert kg to target mass unit
            return self._convert_from_standard_mass(mass_kg, to_unit)

        return None

    def _try_count_conversion(
        self, quantity: float, from_unit: str, to_unit: str, item_id: str
    ) -> Optional[float]:
        """Try count <-> mass/volume conversion using item definition."""
        item = self.kb.get_item(item_id)
        if not item:
            return None

        # Check if item has mass_kg, mass_per_unit, or mass
        mass_per_unit = item.get("mass_kg") or item.get("mass_per_unit") or item.get("mass")

        # count <-> unit are synonyms (1:1 conversion)
        if from_unit in COUNT_UNITS and to_unit in COUNT_UNITS:
            return quantity  # Direct 1:1 conversion

        # count -> kg
        if from_unit in COUNT_UNITS and to_unit == "kg":
            if mass_per_unit:
                return quantity * mass_per_unit

        # kg -> count
        if from_unit == "kg" and to_unit in COUNT_UNITS:
            if mass_per_unit:
                return quantity / mass_per_unit

        return None

    def _convert_to_standard_mass(self, quantity: float, unit: str) -> Optional[float]:
        """Convert any mass unit to kg."""
        if unit == "kg":
            return quantity
        factor = self.kb.get_unit_conversion(unit, "kg")
        if factor:
            return quantity * factor

        # Try reverse
        reverse = self.kb.get_unit_conversion("kg", unit)
        if reverse:
            return quantity / reverse

        return None

    def _convert_from_standard_mass(self, kg: float, unit: str) -> Optional[float]:
        """Convert kg to any mass unit."""
        if unit == "kg":
            return kg
        factor = self.kb.get_unit_conversion("kg", unit)
        if factor:
            return kg * factor

        # Try reverse
        reverse = self.kb.get_unit_conversion(unit, "kg")
        if reverse:
            return kg / reverse

        return None

    def _convert_to_standard_volume(
        self, quantity: float, unit: str
    ) -> Optional[float]:
        """Convert any volume unit to m3."""
        # Handle alias: liter -> L
        if unit == "liter":
            unit = "L"

        if unit == "m3":
            return quantity
        factor = self.kb.get_unit_conversion(unit, "m3")
        if factor:
            return quantity * factor

        # Try reverse
        reverse = self.kb.get_unit_conversion("m3", unit)
        if reverse:
            return quantity / reverse

        return None

    def _convert_from_standard_volume(
        self, m3: float, unit: str
    ) -> Optional[float]:
        """Convert m3 to any volume unit."""
        # Handle alias: liter -> L
        if unit == "liter":
            unit = "L"

        if unit == "m3":
            return m3
        factor = self.kb.get_unit_conversion("m3", unit)
        if factor:
            return m3 * factor

        # Try reverse
        reverse = self.kb.get_unit_conversion(unit, "m3")
        if reverse:
            return m3 / reverse

        return None

    def normalize_to_standard_unit(
        self, quantity: float, unit: str, item_id: Optional[str] = None
    ) -> tuple[float, str]:
        """
        Normalize quantity to standard unit (kg for mass, m3 for volume, count for count).

        Returns:
            (normalized_quantity, standard_unit)
        """
        if unit in MASS_UNITS:
            normalized = self._convert_to_standard_mass(quantity, unit)
            return (normalized or quantity, "kg")
        elif unit in VOLUME_UNITS:
            normalized = self._convert_to_standard_volume(quantity, unit)
            return (normalized or quantity, "m3")
        elif unit in COUNT_UNITS:
            return (quantity, "unit")
        elif unit in TIME_UNITS:
            normalized = normalize_time_to_hours(quantity, unit)
            return (normalized, "hr")
        elif unit in ENERGY_UNITS:
            # For now, keep energy as-is (could add normalization to kWh later)
            return (quantity, unit)
        else:
            # Unknown unit, keep as-is
            return (quantity, unit)
