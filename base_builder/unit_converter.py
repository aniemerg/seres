"""
Unit Converter - Handle unit conversions between mass, volume, count, etc.

Supports:
1. Direct conversions (kg -> g via conversion factors)
2. Mass <-> Volume conversions (via material densities)
3. Count <-> Mass conversions (via item definitions)
"""
from __future__ import annotations

from typing import Optional, Dict, Any
from base_builder.kb_loader import KBLoader


class UnitConverter:
    """
    Handles unit conversions for the simulation.

    Uses:
    - Conversion factors from KB (kg -> g, etc.)
    - Material densities (mass -> volume)
    - Item definitions (count -> mass/volume)
    """

    def __init__(self, kb_loader: KBLoader):
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

        # Mass units
        mass_units = {"kg", "g", "tonne"}
        # Volume units
        volume_units = {"m3", "liter"}

        # kg -> m3
        if from_unit in mass_units and to_unit in volume_units:
            # Convert to kg first
            mass_kg = self._convert_to_standard_mass(quantity, from_unit)
            if mass_kg is None:
                return None

            # kg to m3 via density
            volume_m3 = mass_kg / density

            # Convert m3 to target volume unit
            return self._convert_from_standard_volume(volume_m3, to_unit)

        # m3 -> kg
        if from_unit in volume_units and to_unit in mass_units:
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

        # Check if item has mass_kg or mass_per_unit
        mass_per_unit = item.get("mass_kg") or item.get("mass_per_unit")

        count_units = {"count", "unit"}

        # count <-> unit are synonyms (1:1 conversion)
        if from_unit in count_units and to_unit in count_units:
            return quantity  # Direct 1:1 conversion

        # count -> kg
        if from_unit in count_units and to_unit == "kg":
            if mass_per_unit:
                return quantity * mass_per_unit

        # kg -> count
        if from_unit == "kg" and to_unit in count_units:
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
        # Determine category
        mass_units = {"kg", "g", "tonne"}
        volume_units = {"m3", "liter"}
        count_units = {"count", "unit"}

        if unit in mass_units:
            normalized = self._convert_to_standard_mass(quantity, unit)
            return (normalized or quantity, "kg")
        elif unit in volume_units:
            normalized = self._convert_to_standard_volume(quantity, unit)
            return (normalized or quantity, "m3")
        elif unit in count_units:
            return (quantity, "count")
        else:
            # Unknown unit, keep as-is
            return (quantity, unit)
