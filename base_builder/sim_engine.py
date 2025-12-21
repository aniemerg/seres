"""
Simulation Engine - Core simulation logic.

Handles:
- State management
- Process execution
- Recipe execution
- Machine building
- Item imports
- Time advancement
- Event logging
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from copy import deepcopy

from base_builder.models import (
    SimulationState,
    InventoryItem,
    ActiveProcess,
    SimStartEvent,
    ActionEvent,
    ProcessStartEvent,
    ProcessCompleteEvent,
    RecipeStartEvent,
    RecipeCompleteEvent,
    BuildEvent,
    ImportEvent,
    PreviewEvent,
    StateSnapshotEvent,
    ErrorEvent,
    KBGapEvent,
)
from base_builder.kb_loader import KBLoader
from base_builder.unit_converter import UnitConverter


class SimulationEngine:
    """
    Core simulation engine.

    Manages state, executes processes/recipes, handles time advancement.
    """

    def __init__(self, sim_id: str, kb_loader: KBLoader, sim_dir: Optional[Path] = None):
        self.sim_id = sim_id
        self.kb = kb_loader
        self.converter = UnitConverter(kb_loader)

        # Simulation state
        self.state = SimulationState(sim_id=sim_id)

        # Event buffer (will be written to JSONL)
        self.event_buffer: List[Any] = []

        # Simulation directory
        if sim_dir is None:
            sim_dir = Path("simulations") / sim_id
        self.sim_dir = sim_dir
        self.sim_dir.mkdir(parents=True, exist_ok=True)

        self.log_file = self.sim_dir / "simulation.jsonl"

        # Only log sim start for NEW simulations
        # (load() will skip this if loading existing)
        self._is_new_sim = not self.log_file.exists()

    # ========================================================================
    # State queries
    # ========================================================================

    def get_state_dict(self) -> dict:
        """Get current state as dictionary."""
        return self.state.model_dump()

    def get_inventory_summary(self) -> Dict[str, Any]:
        """Get human-readable inventory summary."""
        summary = {}
        for item_id, inv_item in self.state.inventory.items():
            summary[item_id] = f"{inv_item.quantity} {inv_item.unit}"
        return summary

    # ========================================================================
    # Inventory management
    # ========================================================================

    def add_to_inventory(self, item_id: str, quantity: float, unit: str) -> None:
        """Add item to inventory."""
        if item_id in self.state.inventory:
            # Item exists - need to convert units if different
            existing = self.state.inventory[item_id]
            if existing.unit == unit:
                existing.quantity += quantity
            else:
                # Try to convert to existing unit
                converted = self.converter.convert(quantity, unit, existing.unit, item_id)
                if converted is not None:
                    existing.quantity += converted
                else:
                    # Can't convert - error
                    raise ValueError(
                        f"Cannot add {item_id}: incompatible units {unit} and {existing.unit}"
                    )
        else:
            # New item
            self.state.inventory[item_id] = InventoryItem(quantity=quantity, unit=unit)

    def subtract_from_inventory(
        self, item_id: str, quantity: float, unit: str
    ) -> bool:
        """
        Subtract item from inventory.

        Returns True if successful, False if insufficient quantity.
        """
        if item_id not in self.state.inventory:
            return False

        existing = self.state.inventory[item_id]

        # Convert to existing unit if needed
        if existing.unit != unit:
            quantity = self.converter.convert(quantity, unit, existing.unit, item_id)
            if quantity is None:
                return False

        # Check if enough
        if existing.quantity < quantity:
            return False

        # Subtract
        existing.quantity -= quantity

        # Remove if empty
        if existing.quantity <= 0:
            del self.state.inventory[item_id]

        return True

    def has_item(self, item_id: str, quantity: float, unit: str) -> bool:
        """Check if inventory has sufficient quantity of item."""
        if item_id not in self.state.inventory:
            return False

        existing = self.state.inventory[item_id]

        # Convert to existing unit if needed
        if existing.unit != unit:
            quantity = self.converter.convert(quantity, unit, existing.unit, item_id)
            if quantity is None:
                return False

        return existing.quantity >= quantity

    # ========================================================================
    # Process execution
    # ========================================================================

    def start_process(
        self, process_id: str, scale: float, duration_hours: float
    ) -> Dict[str, Any]:
        """
        Start a process.

        Steps:
        1. Validate process exists in KB
        2. Check required machines exist
        3. Calculate inputs needed (base × scale)
        4. Validate inputs available
        5. Reserve inputs (subtract from inventory)
        6. Schedule completion
        7. Log event

        Returns:
            {"success": bool, "message": str, ...}
        """
        # Validate process exists
        process_def = self.kb.get_process(process_id)
        if not process_def:
            return {
                "success": False,
                "error": "kb_gap",
                "gap_type": "missing_process",
                "message": f"Process '{process_id}' not found in KB",
            }

        # Check required machines
        required_machines = process_def.get("required_machines", [])
        for machine_req in required_machines:
            if isinstance(machine_req, dict):
                machine_id = list(machine_req.keys())[0]
                count = machine_req[machine_id]
            elif isinstance(machine_req, str):
                machine_id = machine_req
                count = 1
            else:
                continue

            # Check if machine exists in inventory or built
            if machine_id not in self.state.machines_built:
                if not self.has_item(machine_id, count, "count"):
                    return {
                        "success": False,
                        "error": "missing_machine",
                        "message": f"Required machine '{machine_id}' not available (need {count})",
                    }

        # Calculate inputs needed
        inputs = process_def.get("inputs", [])
        inputs_consumed = {}

        for inp in inputs:
            requested_item_id = inp.get("item_id")
            # Handle both 'quantity' and 'qty' fields
            base_quantity = inp.get("quantity") or inp.get("qty", 0)
            unit = inp.get("unit", "kg")

            # Scale quantity
            needed_quantity = base_quantity * scale

            # Try to find matching item in inventory
            # First try exact match, then try material_class match
            actual_item_id = None

            if self.has_item(requested_item_id, needed_quantity, unit):
                # Exact match found
                actual_item_id = requested_item_id
            else:
                # Try material_class matching
                requested_item_def = self.kb.get_item(requested_item_id)
                if requested_item_def:
                    requested_class = requested_item_def.get("material_class")
                    if requested_class:
                        # Search inventory for items with matching material_class
                        for inv_item_id in self.state.inventory.keys():
                            inv_item_def = self.kb.get_item(inv_item_id)
                            if inv_item_def and inv_item_def.get("material_class") == requested_class:
                                if self.has_item(inv_item_id, needed_quantity, unit):
                                    actual_item_id = inv_item_id
                                    break

            # Check if we found a suitable item
            if actual_item_id is None:
                return {
                    "success": False,
                    "error": "insufficient_inputs",
                    "message": f"Insufficient {requested_item_id}: need {needed_quantity} {unit}",
                }

            inputs_consumed[actual_item_id] = InventoryItem(
                quantity=needed_quantity, unit=unit
            )

        # Subtract inputs from inventory
        for item_id, inv_item in inputs_consumed.items():
            self.subtract_from_inventory(item_id, inv_item.quantity, inv_item.unit)

        # Calculate outputs
        outputs = process_def.get("outputs", [])
        outputs_pending = {}

        for outp in outputs:
            item_id = outp.get("item_id")
            # Handle both 'quantity' and 'qty' fields
            base_quantity = outp.get("quantity") or outp.get("qty", 0)
            unit = outp.get("unit", "kg")

            # Scale quantity
            output_quantity = base_quantity * scale

            outputs_pending[item_id] = InventoryItem(
                quantity=output_quantity, unit=unit
            )

        # Create active process
        ends_at = self.state.current_time_hours + duration_hours
        active_proc = ActiveProcess(
            process_id=process_id,
            scale=scale,
            started_at=self.state.current_time_hours,
            ends_at=ends_at,
            inputs_consumed=inputs_consumed,
            outputs_pending=outputs_pending,
        )

        self.state.active_processes.append(active_proc)

        # Log event
        self._log_event(
            ProcessStartEvent(
                process_id=process_id,
                scale=scale,
                ends_at=ends_at,
            )
        )

        # Save state snapshot so active process persists
        self._log_event(
            StateSnapshotEvent(
                time_hours=self.state.current_time_hours,
                inventory=self.state.inventory,
                active_processes=self.state.active_processes,
                machines_built=self.state.machines_built,
            )
        )

        return {
            "success": True,
            "message": f"Started process '{process_id}' (scale={scale}, ends at t={ends_at}h)",
            "ends_at": ends_at,
        }

    def run_recipe(self, recipe_id: str, quantity: int) -> Dict[str, Any]:
        """
        Run a recipe to produce items.

        Similar to process but based on batch quantity.
        Recipes define inputs/outputs per batch and duration.

        Returns:
            {"success": bool, "message": str, "duration_hours": float, ...}
        """
        # Validate recipe exists
        recipe_def = self.kb.get_recipe(recipe_id)
        if not recipe_def:
            return {
                "success": False,
                "error": "kb_gap",
                "gap_type": "missing_recipe",
                "message": f"Recipe '{recipe_id}' not found in KB",
            }

        # Check required machines
        required_machines = recipe_def.get("required_machines", [])
        for machine_req in required_machines:
            if isinstance(machine_req, dict):
                machine_id = list(machine_req.keys())[0]
                count = machine_req[machine_id]
            elif isinstance(machine_req, str):
                machine_id = machine_req
                count = 1
            else:
                continue

            if machine_id not in self.state.machines_built:
                if not self.has_item(machine_id, count, "count"):
                    return {
                        "success": False,
                        "error": "missing_machine",
                        "message": f"Required machine '{machine_id}' not available",
                    }

        # Calculate total inputs needed (per batch × quantity)
        inputs = recipe_def.get("inputs", [])
        total_inputs = {}

        for inp in inputs:
            requested_item_id = inp.get("item_id")
            # Handle both 'quantity' and 'qty' fields
            per_batch = inp.get("quantity") or inp.get("qty", 0)
            unit = inp.get("unit", "kg")
            total_needed = per_batch * quantity

            # Try to find matching item in inventory
            # First try exact match, then try material_class match
            actual_item_id = None

            if self.has_item(requested_item_id, total_needed, unit):
                # Exact match found
                actual_item_id = requested_item_id
            else:
                # Try material_class matching
                requested_item_def = self.kb.get_item(requested_item_id)
                if requested_item_def:
                    requested_class = requested_item_def.get("material_class")
                    if requested_class:
                        # Search inventory for items with matching material_class
                        for inv_item_id in self.state.inventory.keys():
                            inv_item_def = self.kb.get_item(inv_item_id)
                            if inv_item_def and inv_item_def.get("material_class") == requested_class:
                                if self.has_item(inv_item_id, total_needed, unit):
                                    actual_item_id = inv_item_id
                                    break

            if actual_item_id is None:
                return {
                    "success": False,
                    "error": "insufficient_inputs",
                    "message": f"Insufficient {requested_item_id}: need {total_needed} {unit}",
                }

            total_inputs[actual_item_id] = InventoryItem(quantity=total_needed, unit=unit)

        # Subtract inputs
        for item_id, inv_item in total_inputs.items():
            self.subtract_from_inventory(item_id, inv_item.quantity, inv_item.unit)

        # Calculate total outputs
        outputs = recipe_def.get("outputs", [])
        total_outputs = {}

        for outp in outputs:
            item_id = outp.get("item_id")
            # Handle both 'quantity' and 'qty' fields
            per_batch = outp.get("quantity") or outp.get("qty", 0)
            unit = outp.get("unit", "kg")
            total_output = per_batch * quantity

            total_outputs[item_id] = InventoryItem(quantity=total_output, unit=unit)

        # Get duration
        duration = recipe_def.get("duration", 1)
        duration_unit = recipe_def.get("duration_unit", "hours")

        # Convert duration to hours
        if duration_unit == "minutes":
            duration_hours = duration / 60.0
        elif duration_unit == "days":
            duration_hours = duration * 24.0
        else:  # hours
            duration_hours = float(duration)

        # Total duration (assuming batches run sequentially for now)
        # TODO: Could parallelize if multiple machines available
        total_duration_hours = duration_hours * quantity

        # Create active process for recipe
        ends_at = self.state.current_time_hours + total_duration_hours
        active_proc = ActiveProcess(
            process_id=f"recipe:{recipe_id}",
            scale=quantity,
            started_at=self.state.current_time_hours,
            ends_at=ends_at,
            inputs_consumed=total_inputs,
            outputs_pending=total_outputs,
        )

        self.state.active_processes.append(active_proc)

        # Log event
        self._log_event(
            RecipeStartEvent(
                recipe_id=recipe_id,
                quantity=quantity,
                duration_hours=total_duration_hours,
            )
        )

        # Save state snapshot so active process persists
        self._log_event(
            StateSnapshotEvent(
                time_hours=self.state.current_time_hours,
                inventory=self.state.inventory,
                active_processes=self.state.active_processes,
                machines_built=self.state.machines_built,
            )
        )

        return {
            "success": True,
            "message": f"Started recipe '{recipe_id}' × {quantity} (ends at t={ends_at}h)",
            "duration_hours": total_duration_hours,
            "ends_at": ends_at,
        }

    def build_machine(self, machine_id: str) -> Dict[str, Any]:
        """
        Build a machine from BOM components.

        Steps:
        1. Get BOM
        2. Check all components available
        3. Consume components
        4. Add machine to inventory and machines_built
        5. Log event

        Returns:
            {"success": bool, "message": str, ...}
        """
        # Get BOM
        bom = self.kb.get_bom(machine_id)
        if not bom:
            return {
                "success": False,
                "error": "kb_gap",
                "gap_type": "missing_bom",
                "message": f"BOM for machine '{machine_id}' not found in KB",
            }

        # Get components
        components = bom.get("components", [])
        if not components:
            return {
                "success": False,
                "error": "invalid_bom",
                "message": f"BOM for '{machine_id}' has no components",
            }

        # Check all components available
        components_consumed = {}
        for comp in components:
            item_id = comp.get("item_id") or comp.get("id")
            quantity = comp.get("quantity", 1)
            unit = comp.get("unit", "count")

            if not self.has_item(item_id, quantity, unit):
                return {
                    "success": False,
                    "error": "insufficient_components",
                    "message": f"Insufficient component '{item_id}': need {quantity} {unit}",
                }

            components_consumed[item_id] = InventoryItem(quantity=quantity, unit=unit)

        # Consume components
        for item_id, inv_item in components_consumed.items():
            self.subtract_from_inventory(item_id, inv_item.quantity, inv_item.unit)

        # Add machine to inventory
        self.add_to_inventory(machine_id, 1, "count")

        # Add to machines_built list
        if machine_id not in self.state.machines_built:
            self.state.machines_built.append(machine_id)

        # Log event
        self._log_event(
            BuildEvent(
                machine_id=machine_id,
                components_consumed=components_consumed,
            )
        )

        return {
            "success": True,
            "message": f"Built machine '{machine_id}'",
            "components_consumed": {
                k: f"{v.quantity} {v.unit}" for k, v in components_consumed.items()
            },
        }

    def import_item(
        self, item_id: str, quantity: float, unit: str
    ) -> Dict[str, Any]:
        """
        Import an item from Earth.

        Adds to inventory and tracks in total_imports.

        Returns:
            {"success": bool, "imported": {...}, ...}
        """
        # Validate item exists in KB
        item_def = self.kb.get_item(item_id)
        if not item_def:
            return {
                "success": False,
                "error": "kb_gap",
                "gap_type": "missing_item",
                "message": f"Item '{item_id}' not found in KB",
            }

        # Add to inventory
        self.add_to_inventory(item_id, quantity, unit)

        # Track in imports
        if item_id in self.state.total_imports:
            existing = self.state.total_imports[item_id]
            # Convert and add
            if existing.unit == unit:
                existing.quantity += quantity
            else:
                converted = self.converter.convert(quantity, unit, existing.unit, item_id)
                if converted:
                    existing.quantity += converted
        else:
            self.state.total_imports[item_id] = InventoryItem(
                quantity=quantity, unit=unit
            )

        # Estimate mass for tracking
        mass_kg = None
        if unit == "kg":
            mass_kg = quantity
        else:
            # Try to convert to kg
            mass_kg = self.converter.convert(quantity, unit, "kg", item_id)

        # Log event
        self._log_event(
            ImportEvent(
                item_id=item_id,
                quantity=quantity,
                unit=unit,
                mass_kg=mass_kg,
            )
        )

        return {
            "success": True,
            "message": f"Imported {quantity} {unit} of '{item_id}' from Earth",
            "imported": {
                "item_id": item_id,
                "quantity": quantity,
                "unit": unit,
                "mass_kg": mass_kg,
            },
        }

    # ========================================================================
    # Time management
    # ========================================================================

    def preview_step(self, duration_hours: float) -> Dict[str, Any]:
        """
        Preview what would happen if time advanced.

        Does NOT commit changes.

        Returns:
            {
                "new_time": float,
                "processes_completing": [{process_id, outputs}, ...],
                "errors": [str, ...] if any
            }
        """
        new_time = self.state.current_time_hours + duration_hours

        # Find processes that would complete
        completing = []
        for proc in self.state.active_processes:
            if proc.ends_at <= new_time:
                completing.append({
                    "process_id": proc.process_id,
                    "ends_at": proc.ends_at,
                    "outputs": {
                        k: {"quantity": v.quantity, "unit": v.unit}
                        for k, v in proc.outputs_pending.items()
                    },
                })

        # Log preview event
        self._log_event(
            PreviewEvent(
                new_time=new_time,
                processes_completing=completing,
            )
        )

        return {
            "new_time": new_time,
            "processes_completing": completing,
            "active_processes_count": len(self.state.active_processes),
            "completing_count": len(completing),
        }

    def advance_time(self, duration_hours: float) -> Dict[str, Any]:
        """
        Advance simulation time.

        Steps:
        1. Calculate new time
        2. Find all processes ending <= new_time
        3. Complete processes (add outputs, remove from active)
        4. Update current time
        5. Log events

        Returns:
            {
                "new_time": float,
                "completed": [{process_id, outputs}, ...],
                "new_inventory": {...}
            }
        """
        new_time = self.state.current_time_hours + duration_hours

        # Find and complete processes
        completed = []
        remaining = []

        for proc in self.state.active_processes:
            if proc.ends_at <= new_time:
                # Process completes
                # Add outputs to inventory
                for item_id, inv_item in proc.outputs_pending.items():
                    self.add_to_inventory(item_id, inv_item.quantity, inv_item.unit)

                # Log completion
                self._log_event(
                    ProcessCompleteEvent(
                        process_id=proc.process_id,
                        outputs=proc.outputs_pending,
                    )
                )

                completed.append({
                    "process_id": proc.process_id,
                    "ended_at": proc.ends_at,
                    "outputs": {
                        k: {"quantity": v.quantity, "unit": v.unit}
                        for k, v in proc.outputs_pending.items()
                    },
                })
            else:
                # Process still running
                remaining.append(proc)

        # Update active processes
        self.state.active_processes = remaining

        # Update time
        self.state.current_time_hours = new_time

        # Log state snapshot
        self._log_event(
            StateSnapshotEvent(
                time_hours=new_time,
                inventory=self.state.inventory,
                active_processes=self.state.active_processes,
                machines_built=self.state.machines_built,
            )
        )

        # Flush events to disk
        self.save()

        return {
            "new_time": new_time,
            "completed": completed,
            "completed_count": len(completed),
            "active_processes_remaining": len(remaining),
            "new_inventory": self.get_inventory_summary(),
        }

    # ========================================================================
    # Event logging
    # ========================================================================

    def _log_event(self, event: Any) -> None:
        """Add event to buffer."""
        self.event_buffer.append(event)

    def save(self) -> None:
        """Flush event buffer to JSONL file."""
        if not self.event_buffer:
            return

        with self.log_file.open("a", encoding="utf-8") as f:
            for event in self.event_buffer:
                # Convert Pydantic model to dict
                if hasattr(event, "model_dump"):
                    event_dict = event.model_dump()
                else:
                    event_dict = event

                f.write(json.dumps(event_dict) + "\n")

        # Clear buffer
        self.event_buffer.clear()

    def load(self) -> bool:
        """
        Load simulation state from JSONL file.

        Reconstructs state from events.

        Returns:
            True if loaded successfully, False if no save file exists
        """
        if not self.log_file.exists():
            # New simulation - log sim start
            self._log_event(SimStartEvent(sim_id=self.sim_id))
            self.save()
            return False

        # Read all events
        with self.log_file.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    event = json.loads(line)
                    event_type = event.get("type")

                    # Reconstruct state from state_snapshot events
                    if event_type == "state_snapshot":
                        self.state.current_time_hours = event.get("time_hours", 0)
                        self.state.inventory = {
                            k: InventoryItem(**v)
                            for k, v in event.get("inventory", {}).items()
                        }
                        self.state.active_processes = [
                            ActiveProcess(**p)
                            for p in event.get("active_processes", [])
                        ]
                        self.state.machines_built = event.get("machines_built", [])

                    # Track imports
                    elif event_type == "import":
                        item_id = event.get("item_id")
                        quantity = event.get("quantity")
                        unit = event.get("unit")
                        if item_id:
                            if item_id in self.state.total_imports:
                                existing = self.state.total_imports[item_id]
                                if existing.unit == unit:
                                    existing.quantity += quantity
                            else:
                                self.state.total_imports[item_id] = InventoryItem(
                                    quantity=quantity, unit=unit
                                )

                except json.JSONDecodeError:
                    continue

        return True
