#!/usr/bin/env python3
"""
Energy Consumption Calculator

Calculates total energy (kWh) used in a simulation by analyzing
the simulation.jsonl file and looking up energy models from the KB.

Usage:
    python tools/calculate_energy.py <simulation_name>
    python tools/calculate_energy.py isru_advanced
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
import yaml


class EnergyCalculator:
    def __init__(self, kb_path: Path):
        self.kb_path = kb_path
        self.process_cache = {}
        self.recipe_cache = {}

    def load_process(self, process_id: str) -> Optional[Dict[str, Any]]:
        """Load process definition from KB"""
        if process_id in self.process_cache:
            return self.process_cache[process_id]

        # Search for process file
        process_files = list(self.kb_path.glob(f"processes/{process_id}.yaml"))
        if not process_files:
            # Try finding with wildcard
            process_files = list(self.kb_path.glob(f"processes/*{process_id}*.yaml"))

        if not process_files:
            return None

        with open(process_files[0], 'r') as f:
            process_def = yaml.safe_load(f)
            self.process_cache[process_id] = process_def
            return process_def

    def load_recipe(self, recipe_id: str) -> Optional[Dict[str, Any]]:
        """Load recipe definition from KB"""
        if recipe_id in self.recipe_cache:
            return self.recipe_cache[recipe_id]

        # Search for recipe file
        recipe_files = list(self.kb_path.glob(f"recipes/{recipe_id}.yaml"))
        if not recipe_files:
            # Try finding with wildcard
            recipe_files = list(self.kb_path.glob(f"recipes/*{recipe_id}*.yaml"))

        if not recipe_files:
            return None

        with open(recipe_files[0], 'r') as f:
            recipe_def = yaml.safe_load(f)
            self.recipe_cache[recipe_id] = recipe_def
            return recipe_def

    def calculate_process_energy(
        self,
        process_def: Dict[str, Any],
        scale: float,
        inputs_consumed: Dict[str, Any],
        outputs_produced: Dict[str, Any]
    ) -> float:
        """
        Calculate energy for a process based on its energy_model.

        Returns energy in kWh.
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
            for item_id, item_data in inputs_consumed.items():
                qty = item_data.get("quantity", 0)
                unit = item_data.get("unit", "kg")
                if unit == "kg":
                    total_kg += qty

            # If no inputs, try outputs
            if total_kg == 0:
                for item_id, item_data in outputs_produced.items():
                    qty = item_data.get("quantity", 0)
                    unit = item_data.get("unit", "kg")
                    if unit == "kg":
                        total_kg += qty

            return total_kg * value

        elif model_type == "kWh_per_kg_input":
            # Energy per kg of input
            total_kg = 0
            for item_id, item_data in inputs_consumed.items():
                qty = item_data.get("quantity", 0)
                unit = item_data.get("unit", "kg")
                if unit == "kg":
                    total_kg += qty
            return total_kg * value

        elif model_type == "kWh_per_unit_output" or model_type == "kWh_per_unit":
            # Energy per unit of output
            total_units = 0
            for item_id, item_data in outputs_produced.items():
                qty = item_data.get("quantity", 0)
                total_units += qty
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

    def analyze_simulation(self, sim_path: Path) -> Dict[str, Any]:
        """Analyze simulation and calculate total energy"""

        jsonl_file = sim_path / "simulation.jsonl"
        if not jsonl_file.exists():
            return {"error": "simulation.jsonl not found"}

        total_energy = 0.0
        energy_by_process = {}
        process_details = []
        recipe_details = []

        # Track active processes to get scale and inputs information
        active_processes = {}  # keyed by (process_id, ends_at) to track scale and inputs

        # Read all events
        with open(jsonl_file, 'r') as f:
            for line in f:
                if not line.strip():
                    continue

                event = json.loads(line)
                event_type = event.get("type")

                # Track process starts to get scale
                if event_type == "process_start":
                    process_id = event.get("process_id")
                    scale = event.get("scale", 1.0)
                    ends_at = event.get("ends_at")

                    # Store active process with scale
                    key = (process_id, ends_at)
                    active_processes[key] = {"scale": scale, "inputs": {}}

                # Track state snapshots to get inputs_consumed from active processes
                elif event_type == "state_snapshot":
                    for active_proc in event.get("active_processes", []):
                        proc_id = active_proc.get("process_id")
                        ends_at = active_proc.get("ends_at")
                        inputs_consumed = active_proc.get("inputs_consumed", {})

                        key = (proc_id, ends_at)
                        if key in active_processes:
                            active_processes[key]["inputs"] = inputs_consumed

                # Handle process completion
                elif event_type == "process_complete":
                    process_id = event.get("process_id")
                    outputs = event.get("outputs", {})

                    # Skip recipe processes (they're handled separately)
                    if process_id.startswith("recipe:"):
                        continue

                    # Load process definition
                    process_def = self.load_process(process_id)
                    if not process_def:
                        continue

                    # Try to find scale and inputs from active processes
                    # Match by process_id (take the first match and remove it)
                    scale = 1.0
                    inputs_consumed = {}

                    for (pid, ends_at), proc_data in list(active_processes.items()):
                        if pid == process_id:
                            scale = proc_data["scale"]
                            inputs_consumed = proc_data["inputs"]
                            # Remove from active processes
                            del active_processes[(pid, ends_at)]
                            break

                    # Calculate energy
                    energy = self.calculate_process_energy(
                        process_def,
                        scale=scale,
                        inputs_consumed=inputs_consumed,
                        outputs_produced=outputs
                    )

                    total_energy += energy

                    if process_id not in energy_by_process:
                        energy_by_process[process_id] = 0
                    energy_by_process[process_id] += energy

                    process_details.append({
                        "process_id": process_id,
                        "scale": scale,
                        "energy_kwh": energy,
                        "outputs": outputs
                    })

                # Handle recipe completion
                elif event_type == "recipe_start":
                    recipe_id = event.get("recipe_id")
                    quantity = event.get("quantity", 1)

                    # Load recipe definition
                    recipe_def = self.load_recipe(recipe_id)
                    if not recipe_def:
                        continue

                    # Check if recipe has energy model
                    energy_model = recipe_def.get("energy_model")
                    if energy_model:
                        # Calculate based on recipe's energy model
                        inputs = recipe_def.get("inputs", [])
                        outputs = recipe_def.get("outputs", [])

                        # Convert to dict format
                        inputs_dict = {
                            inp.get("item_id"): {"quantity": inp.get("quantity", 0) * quantity, "unit": inp.get("unit", "kg")}
                            for inp in inputs
                        }
                        outputs_dict = {
                            out.get("item_id"): {"quantity": out.get("quantity", 0) * quantity, "unit": out.get("unit", "kg")}
                            for out in outputs
                        }

                        energy = self.calculate_process_energy(
                            recipe_def,
                            scale=quantity,
                            inputs_consumed=inputs_dict,
                            outputs_produced=outputs_dict
                        )

                        total_energy += energy

                        recipe_key = f"recipe:{recipe_id}"
                        if recipe_key not in energy_by_process:
                            energy_by_process[recipe_key] = 0
                        energy_by_process[recipe_key] += energy

                        recipe_details.append({
                            "recipe_id": recipe_id,
                            "quantity": quantity,
                            "energy_kwh": energy
                        })

        return {
            "total_energy_kwh": total_energy,
            "energy_by_process": energy_by_process,
            "process_count": len(process_details),
            "recipe_count": len(recipe_details),
            "process_details": process_details,
            "recipe_details": recipe_details
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/calculate_energy.py <simulation_name>")
        print("Example: python tools/calculate_energy.py isru_advanced")
        sys.exit(1)

    sim_name = sys.argv[1]

    # Locate simulation
    base_path = Path(__file__).parent.parent
    sim_path = base_path / "simulations" / sim_name
    kb_path = base_path / "kb"

    if not sim_path.exists():
        print(f"Error: Simulation '{sim_name}' not found")
        print(f"Available simulations:")
        sims_dir = base_path / "simulations"
        for d in sorted(sims_dir.glob("*/")):
            print(f"  - {d.name}")
        sys.exit(1)

    # Calculate energy
    calculator = EnergyCalculator(kb_path)
    result = calculator.analyze_simulation(sim_path)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    # Display results
    print(f"\n{'='*60}")
    print(f"Energy Analysis: {sim_name}")
    print(f"{'='*60}\n")

    print(f"Total Energy Consumption: {result['total_energy_kwh']:.2f} kWh")
    print(f"Processes analyzed: {result['process_count']}")
    print(f"Recipes analyzed: {result['recipe_count']}\n")

    # Show breakdown by process
    if result['energy_by_process']:
        print("Energy Breakdown by Process:")
        print("-" * 60)
        sorted_processes = sorted(
            result['energy_by_process'].items(),
            key=lambda x: x[1],
            reverse=True
        )
        for process_id, energy in sorted_processes:
            print(f"  {process_id:40s} {energy:10.2f} kWh")

    # Show details if verbose
    if "--verbose" in sys.argv or "-v" in sys.argv:
        print("\n" + "="*60)
        print("Detailed Process Energy:")
        print("="*60)
        for detail in result['process_details']:
            print(f"\n{detail['process_id']}:")
            print(f"  Energy: {detail['energy_kwh']:.2f} kWh")
            print(f"  Outputs: {detail['outputs']}")

        print("\n" + "="*60)
        print("Detailed Recipe Energy:")
        print("="*60)
        for detail in result['recipe_details']:
            print(f"\n{detail['recipe_id']} (x{detail['quantity']}):")
            print(f"  Energy: {detail['energy_kwh']:.2f} kWh")


if __name__ == "__main__":
    main()
