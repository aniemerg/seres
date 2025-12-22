"""
Energy calculation for base builder simulation.

Calculates energy consumption for processes based on energy_model definitions in KB.
"""
from __future__ import annotations

from typing import Dict, Any
from base_builder.models import InventoryItem


class EnergyCalculator:
    """
    Calculates energy consumption for processes.

    Supports multiple energy model types from KB process definitions:
    - kWh_per_kg: Energy per kg of material processed
    - kWh_per_kg_input: Energy per kg of input
    - kWh_per_unit / kWh_per_unit_output: Energy per unit of output
    - kWh_per_batch: Fixed energy per batch (scaled)
    - fixed_kWh: Fixed energy consumption
    - total_energy_kwh: Alternative fixed format
    """

    def calculate_process_energy(
        self,
        process_def: Dict[str, Any],
        scale: float,
        inputs_consumed: Dict[str, InventoryItem],
        outputs_produced: Dict[str, InventoryItem]
    ) -> float:
        """
        Calculate energy for a process based on its energy_model.

        Args:
            process_def: Process definition from KB (with energy_model)
            scale: Scale factor applied to process
            inputs_consumed: Input items consumed by process
            outputs_produced: Output items produced by process

        Returns:
            Energy consumption in kWh
            Returns 0.0 if no energy_model defined
        """
        energy_model = process_def.get("energy_model")
        if not energy_model:
            return 0.0

        # Check for total_energy_kwh format (alternative format)
        if "total_energy_kwh" in energy_model:
            return energy_model["total_energy_kwh"] * scale

        model_type = energy_model.get("type")
        value = energy_model.get("value", 0)

        if model_type == "kWh_per_kg":
            # Energy per kg of input or output
            # Sum up all inputs in kg
            total_kg = 0
            for item_id, inv_item in inputs_consumed.items():
                if inv_item.unit == "kg":
                    total_kg += inv_item.quantity

            # If no inputs, try outputs
            if total_kg == 0:
                for item_id, inv_item in outputs_produced.items():
                    if inv_item.unit == "kg":
                        total_kg += inv_item.quantity

            return total_kg * value

        elif model_type == "kWh_per_kg_input":
            # Energy per kg of input
            total_kg = 0
            for item_id, inv_item in inputs_consumed.items():
                if inv_item.unit == "kg":
                    total_kg += inv_item.quantity
            return total_kg * value

        elif model_type == "kWh_per_unit_output" or model_type == "kWh_per_unit":
            # Energy per unit of output
            total_units = 0
            for item_id, inv_item in outputs_produced.items():
                total_units += inv_item.quantity
            return total_units * value

        elif model_type == "kWh_per_batch":
            # Fixed energy per batch, scaled by scale factor
            return value * scale

        elif model_type == "fixed_kWh":
            # Fixed energy consumption
            return value

        else:
            # Unknown model type
            return 0.0
