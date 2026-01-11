"""
Time and Energy Calculations

Implements ADR-012 (Time Model) and ADR-014 (Energy Model) calculation logic.

Provides:
- calculate_duration() - Calculate process duration from time_model
- calculate_energy() - Calculate energy consumption from energy_model
"""
from __future__ import annotations

from typing import Dict, Optional

from .schema import Process, Quantity
from .unit_converter import (
    UnitConverter,
    parse_compound_unit,
    normalize_rate_to_hours,
)


class CalculationError(Exception):
    """Raised when time/energy calculation fails."""
    pass


def calculate_duration(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """
    Calculate process duration in hours per ADR-012.

    Args:
        process: Process with time_model
        inputs: Dict of input quantities {item_id: Quantity}
        outputs: Dict of output quantities {item_id: Quantity}
        converter: Unit converter for cross-unit processing

    Returns:
        Duration in hours

    Raises:
        CalculationError: If calculation fails (missing data, unit mismatch, etc.)

    Examples:
        # Linear rate (continuous)
        >>> process.time_model.type == "linear_rate"
        >>> process.time_model.rate == 5.0
        >>> process.time_model.rate_unit == "kg/hr"
        >>> process.time_model.scaling_basis == "ore"
        >>> inputs = {"ore": Quantity(item_id="ore", qty=100.0, unit="kg")}
        >>> calculate_duration(process, inputs, {}, converter)
        20.0  # 100 kg / 5 kg/hr = 20 hours

        # Batch
        >>> process.time_model.type == "batch"
        >>> process.time_model.hr_per_batch == 2.0
        >>> process.time_model.setup_hr == 0.5
        >>> calculate_duration(process, {}, {}, converter)
        2.5  # 0.5 + 2.0 = 2.5 hours
    """
    if process.time_model.type == "linear_rate":
        return _calculate_linear_rate_duration(process, inputs, outputs, converter)
    elif process.time_model.type == "batch":
        return _calculate_batch_duration(process, inputs, outputs, converter)
    else:
        raise CalculationError(
            f"Unknown time_model type: {process.time_model.type}"
        )


def _calculate_linear_rate_duration(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """Calculate duration for linear_rate time_model."""
    # Get scaling basis quantity
    scaling_basis = process.time_model.scaling_basis
    if not scaling_basis:
        raise CalculationError(
            f"Process '{process.id}' has linear_rate but no scaling_basis"
        )

    # Find scaling quantity in inputs or outputs
    scaling_qty = inputs.get(scaling_basis) or outputs.get(scaling_basis)
    if not scaling_qty:
        raise CalculationError(
            f"Process '{process.id}' scaling_basis '{scaling_basis}' "
            f"not found in inputs or outputs"
        )

    # Parse rate_unit (e.g., "kg/hr" -> ("kg", "hr"))
    try:
        rate_numerator, rate_denominator = parse_compound_unit(
            process.time_model.rate_unit
        )
    except ValueError as e:
        raise CalculationError(
            f"Process '{process.id}' has invalid rate_unit "
            f"'{process.time_model.rate_unit}': {e}"
        )

    # Normalize rate to /hr
    rate = process.time_model.rate
    if not rate or rate <= 0:
        raise CalculationError(
            f"Process '{process.id}' has invalid rate: {rate}"
        )

    normalized_rate = normalize_rate_to_hours(rate, rate_denominator)

    # Convert scaling quantity to match rate numerator
    if scaling_qty.unit != rate_numerator:
        # Need unit conversion
        converted_qty = converter.convert(
            scaling_qty.qty,
            scaling_qty.unit,
            rate_numerator,
            scaling_qty.item_id
        )

        if converted_qty is None:
            raise CalculationError(
                f"Process '{process.id}' cannot convert scaling_basis unit "
                f"'{scaling_qty.unit}' to rate_unit numerator '{rate_numerator}' "
                f"for item '{scaling_qty.item_id}'. "
                f"Add density (for mass<->volume) or mass_kg (for count<->mass) to item."
            )
    else:
        converted_qty = scaling_qty.qty

    # Calculate duration: quantity / rate
    duration_hr = converted_qty / normalized_rate

    if duration_hr < 0:
        raise CalculationError(
            f"Process '{process.id}' calculated negative duration: {duration_hr}hr"
        )

    return duration_hr


def _calculate_batch_duration(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """
    Calculate duration for batch time_model.

    If outputs are provided with quantities different from the base process,
    scales the duration by the number of batches required.
    """
    hr_per_batch = process.time_model.hr_per_batch
    if not hr_per_batch or hr_per_batch <= 0:
        raise CalculationError(
            f"Process '{process.id}' has invalid hr_per_batch: {hr_per_batch}"
        )

    setup_hr = process.time_model.setup_hr or 0.0

    # Calculate number of batches if outputs are scaled
    num_batches = 1.0
    if outputs and process.outputs:
        # Find the first output to use as scaling basis
        for process_output in process.outputs:
            output_item_id = process_output.item_id
            if output_item_id in outputs:
                requested_qty = outputs[output_item_id]
                base_qty = process_output.qty if process_output.qty is not None else process_output.quantity

                if base_qty and base_qty > 0:
                    # Convert requested quantity to base unit if needed
                    if requested_qty.unit != process_output.unit:
                        converted_qty = converter.convert(
                            requested_qty.qty,
                            requested_qty.unit,
                            process_output.unit,
                            output_item_id
                        )
                        if converted_qty is None:
                            raise CalculationError(
                                f"Process '{process.id}' cannot convert output unit "
                                f"'{requested_qty.unit}' to '{process_output.unit}' "
                                f"for item '{output_item_id}'"
                            )
                    else:
                        converted_qty = requested_qty.qty

                    num_batches = converted_qty / base_qty
                    break

    return setup_hr + (hr_per_batch * num_batches)


def calculate_energy(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """
    Calculate process energy consumption per ADR-014.

    Args:
        process: Process with energy_model
        inputs: Dict of input quantities {item_id: Quantity}
        outputs: Dict of output quantities {item_id: Quantity}
        converter: Unit converter for cross-unit processing

    Returns:
        Energy in kWh (normalized internally)

    Raises:
        CalculationError: If calculation fails (missing data, unit mismatch, etc.)

    Examples:
        # Per-unit energy
        >>> process.energy_model.type == "per_unit"
        >>> process.energy_model.value == 50.0
        >>> process.energy_model.unit == "kWh/kg"
        >>> process.energy_model.scaling_basis == "water"
        >>> inputs = {"water": Quantity(item_id="water", qty=100.0, unit="kg")}
        >>> calculate_energy(process, inputs, {}, converter)
        5000.0  # 100 kg × 50 kWh/kg = 5000 kWh

        # Fixed per batch
        >>> process.energy_model.type == "fixed_per_batch"
        >>> process.energy_model.value == 100.0
        >>> process.energy_model.unit == "kWh"
        >>> calculate_energy(process, {}, {}, converter)
        100.0
    """
    if not process.energy_model:
        return 0.0  # No energy model = no energy consumption

    if process.energy_model.type == "per_unit":
        return _calculate_per_unit_energy(process, inputs, outputs, converter)
    elif process.energy_model.type == "fixed_per_batch":
        return _calculate_fixed_energy(process, inputs, outputs, converter)
    else:
        raise CalculationError(
            f"Unknown energy_model type: {process.energy_model.type}"
        )


def _calculate_per_unit_energy(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """Calculate energy for per_unit energy_model."""
    # Get scaling basis quantity
    scaling_basis = process.energy_model.scaling_basis
    if not scaling_basis:
        raise CalculationError(
            f"Process '{process.id}' has per_unit energy but no scaling_basis"
        )

    # Find scaling quantity in inputs or outputs
    scaling_qty = inputs.get(scaling_basis) or outputs.get(scaling_basis)
    if not scaling_qty:
        raise CalculationError(
            f"Process '{process.id}' energy scaling_basis '{scaling_basis}' "
            f"not found in inputs or outputs"
        )

    # Parse unit (e.g., "kWh/kg" -> ("kWh", "kg"))
    try:
        energy_unit, per_unit = parse_compound_unit(process.energy_model.unit)
    except ValueError as e:
        raise CalculationError(
            f"Process '{process.id}' has invalid energy unit "
            f"'{process.energy_model.unit}': {e}"
        )

    # Convert scaling quantity to match per_unit
    if scaling_qty.unit != per_unit:
        # Need unit conversion
        converted_qty = converter.convert(
            scaling_qty.qty,
            scaling_qty.unit,
            per_unit,
            scaling_qty.item_id
        )

        if converted_qty is None:
            raise CalculationError(
                f"Process '{process.id}' cannot convert energy scaling_basis unit "
                f"'{scaling_qty.unit}' to energy unit denominator '{per_unit}' "
                f"for item '{scaling_qty.item_id}'. "
                f"Add density (for mass<->volume) or mass_kg (for count<->mass) to item."
            )
    else:
        converted_qty = scaling_qty.qty

    # Calculate energy: quantity × value
    energy_value = process.energy_model.value
    if not energy_value or energy_value < 0:
        raise CalculationError(
            f"Process '{process.id}' has invalid energy value: {energy_value}"
        )

    energy = converted_qty * energy_value

    # TODO: Convert to kWh if energy_unit is not kWh (future enhancement)
    # For now, assume all energy is in kWh

    if energy < 0:
        raise CalculationError(
            f"Process '{process.id}' calculated negative energy: {energy} {energy_unit}"
        )

    return energy


def _calculate_fixed_energy(
    process: Process,
    inputs: Dict[str, Quantity],
    outputs: Dict[str, Quantity],
    converter: UnitConverter
) -> float:
    """
    Calculate energy for fixed_per_batch energy_model.

    If outputs are provided with quantities different from the base process,
    scales the energy by the number of batches required.
    """
    energy_value = process.energy_model.value
    if not energy_value or energy_value < 0:
        raise CalculationError(
            f"Process '{process.id}' has invalid fixed energy value: {energy_value}"
        )

    # Calculate number of batches if outputs are scaled
    num_batches = 1.0
    if outputs and process.outputs:
        # Find the first output to use as scaling basis
        for process_output in process.outputs:
            output_item_id = process_output.item_id
            if output_item_id in outputs:
                requested_qty = outputs[output_item_id]
                base_qty = process_output.qty if process_output.qty is not None else process_output.quantity

                if base_qty and base_qty > 0:
                    # Convert requested quantity to base unit if needed
                    if requested_qty.unit != process_output.unit:
                        converted_qty = converter.convert(
                            requested_qty.qty,
                            requested_qty.unit,
                            process_output.unit,
                            output_item_id
                        )
                        if converted_qty is None:
                            raise CalculationError(
                                f"Process '{process.id}' cannot convert output unit "
                                f"'{requested_qty.unit}' to '{process_output.unit}' "
                                f"for item '{output_item_id}'"
                            )
                    else:
                        converted_qty = requested_qty.qty

                    num_batches = converted_qty / base_qty
                    break

    # TODO: Convert to kWh if unit is not kWh (future enhancement)
    # For now, assume all energy is in kWh

    return energy_value * num_batches
