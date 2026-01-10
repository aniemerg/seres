"""
Simulation Engine - Core simulation logic with ADR-012-017 support.

Handles:
- State management
- Process execution with runtime validation
- Recipe execution with override resolution
- Machine building
- Item imports
- Time advancement
- Event logging
- Duration calculation (agent-provided or calculated)
- Energy calculation using energy models
"""
from __future__ import annotations

import json
import os
import sys
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Any
from copy import deepcopy

from src.simulation.models import (
    SimulationState,
    InventoryItem,
    ActiveProcess,
    SimStartEvent,
    ActionEvent,
    ProcessScheduledEvent,
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
from src.simulation.scheduler import Scheduler, EventType
from src.simulation.machine_reservations import MachineReservationManager
from src.simulation.recipe_orchestrator import RecipeOrchestrator
from src.simulation.adr020_validators import validate_process_adr020, validate_recipe_adr020
from src.kb_core.kb_loader import KBLoader
from src.kb_core.unit_converter import UnitConverter
from src.kb_core.calculations import calculate_duration, calculate_energy
from src.kb_core.schema import Quantity, RawProcess, RawEnergyModel
from src.kb_core.validators import validate_process, ValidationLevel


class SimulationEngine:
    """
    Core simulation engine with ADR-012-017 support.

    Manages state, executes processes/recipes, handles time advancement.

    New features:
    - Runtime validation before process execution
    - Calculated duration from time_model (if not provided by agent)
    - Energy calculation using ADR-014 energy models
    - Override resolution per ADR-013
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

        # ADR-020 components
        self.scheduler = Scheduler()
        self.orchestrator = RecipeOrchestrator(self.scheduler)
        # Reservation manager will be initialized when machines are available
        self.reservation_manager = None
        # Enable ADR-020 mode (event-driven scheduling, machine reservations, recipe orchestration)
        self.adr020_mode = True

        # Register event handler for input validation (must happen during event processing)
        self.scheduler.register_handler(
            EventType.PROCESS_START,
            self._validate_process_inputs
        )

    def _validate_process_inputs(self, event) -> None:
        """
        Event handler to validate inputs when process starts.

        This runs during event processing, after the process is added to active_processes.
        If inputs aren't available, cancel the process.
        """
        process_run_id = event.data.get('process_run_id')
        if not process_run_id:
            return

        # Get process run from active processes
        if process_run_id not in self.scheduler.active_processes:
            return

        process_run = self.scheduler.active_processes[process_run_id]

        # Get process definition to check inputs
        process_model = self.kb.get_process(process_run.process_id)
        if not process_model:
            return

        if hasattr(process_model, 'model_dump'):
            process_def = process_model.model_dump()
        else:
            process_def = process_model

        # Try to consume inputs from inventory
        inputs_available = True
        consumed_inputs = []

        for inp in process_def.get("inputs", []):
            item_id = inp.get("item_id")
            unit = inp.get("unit", "kg")
            if item_id in process_run.inputs_consumed:
                qty = process_run.inputs_consumed[item_id]
                success = self.subtract_from_inventory(item_id, qty, unit)
                if success:
                    consumed_inputs.append((item_id, qty, unit))
                else:
                    inputs_available = False
                    break

        if not inputs_available:
            # Rollback any inputs we already consumed
            for item_id, qty, unit in consumed_inputs:
                self.add_to_inventory(item_id, qty, unit)

            # Cancel this process (removes from active_processes and event queue)
            self.scheduler.cancel_process(process_run_id)

    def _init_reservation_manager(self) -> None:
        """Initialize reservation manager with current machine inventory."""
        if self.reservation_manager is not None:
            return  # Already initialized

        machine_capacities = {}
        for item_id, inv_item in self.state.inventory.items():
            item_model = self.kb.get_item(item_id)
            if item_model:
                item_def = item_model.model_dump() if hasattr(item_model, 'model_dump') else item_model
                if item_def.get('kind') == 'machine':
                    if inv_item.unit in ('count', 'unit'):
                        machine_capacities[item_id] = inv_item.quantity

        self.reservation_manager = MachineReservationManager(machine_capacities)

    def _update_machine_capacities(self) -> None:
        """Update reservation manager with current machine inventory."""
        if self.reservation_manager is None:
            self._init_reservation_manager()
            return

        machine_capacities = {}
        for item_id, inv_item in self.state.inventory.items():
            item_model = self.kb.get_item(item_id)
            if item_model:
                item_def = item_model.model_dump() if hasattr(item_model, 'model_dump') else item_model
                if item_def.get('kind') == 'machine':
                    if inv_item.unit in ('count', 'unit'):
                        machine_capacities[item_id] = inv_item.quantity

        self.reservation_manager.machine_capacities = machine_capacities

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

    def _get_machine_available_count(self, machine_id: str) -> float:
        """Return available count for a machine, accounting for current reservations."""
        in_use = self.state.machines_in_use.get(machine_id, 0)
        total = 0.0

        inv_item = self.state.inventory.get(machine_id)
        if inv_item:
            if inv_item.unit in ("count", "unit"):
                total = inv_item.quantity
            else:
                converted = self.converter.convert(inv_item.quantity, inv_item.unit, "count", machine_id)
                if converted is not None:
                    total = converted
        elif machine_id in self.state.machines_built:
            total = 1.0

        return max(0.0, total - in_use)

    def _collect_required_machines_from_process_def(self, process_def: Dict[str, Any]) -> Dict[str, int]:
        counts: Dict[str, int] = {}

        # Read from resource_requirements (post-migration)
        resource_requirements = process_def.get("resource_requirements", []) or []
        for req in resource_requirements:
            if isinstance(req, dict) and req.get("machine_id"):
                machine_id = req["machine_id"]
                # Count is always 1 for machine availability (duration is from time_model)
                counts[machine_id] = max(counts.get(machine_id, 0), 1)

        # Legacy support: requires_ids (deprecated, for backward compatibility)
        for machine_id in process_def.get("requires_ids", []) or []:
            counts[machine_id] = max(counts.get(machine_id, 0), 1)

        # Legacy support: required_machines (deprecated)
        required_machines = process_def.get("required_machines", []) or []
        for machine_req in required_machines:
            if isinstance(machine_req, dict):
                machine_id = list(machine_req.keys())[0]
                count = int(machine_req[machine_id])
            elif isinstance(machine_req, str):
                machine_id = machine_req
                count = 1
            else:
                continue
            counts[machine_id] = max(counts.get(machine_id, 0), count)

        return counts

    def _collect_required_machines_from_steps(
        self, resolved_steps: List[Dict[str, Any]], recipe_def: Dict[str, Any]
    ) -> Dict[str, int]:
        counts: Dict[str, int] = {}

        # Collect from each step's resource_requirements
        for step in resolved_steps:
            resource_requirements = step.get("resource_requirements", []) or []
            for req in resource_requirements:
                if isinstance(req, dict) and req.get("machine_id"):
                    machine_id = req["machine_id"]
                    counts[machine_id] = max(counts.get(machine_id, 0), 1)

            # Legacy support: requires_ids (deprecated)
            for machine_id in step.get("requires_ids", []) or []:
                counts[machine_id] = max(counts.get(machine_id, 0), 1)

            # Legacy support: required_machines (deprecated)
            for machine_req in step.get("required_machines", []) or []:
                if isinstance(machine_req, dict):
                    machine_id = list(machine_req.keys())[0]
                    count = int(machine_req[machine_id])
                elif isinstance(machine_req, str):
                    machine_id = machine_req
                    count = 1
                else:
                    continue
                counts[machine_id] = max(counts.get(machine_id, 0), count)

        # Legacy support: recipe-level required_machines (deprecated)
        for machine_req in recipe_def.get("required_machines", []) or []:
            if isinstance(machine_req, dict):
                machine_id = list(machine_req.keys())[0]
                count = int(machine_req[machine_id])
            elif isinstance(machine_req, str):
                machine_id = machine_req
                count = 1
            else:
                continue
            counts[machine_id] = max(counts.get(machine_id, 0), count)

        return counts

    def _reserve_machines(self, required: Dict[str, int]) -> None:
        for machine_id, count in required.items():
            if count <= 0:
                continue
            self.state.machines_in_use[machine_id] = self.state.machines_in_use.get(machine_id, 0) + count

    def _release_machines(self, reserved: Dict[str, int]) -> None:
        for machine_id, count in reserved.items():
            if count <= 0:
                continue
            current = self.state.machines_in_use.get(machine_id, 0)
            remaining = current - count
            if remaining > 0:
                self.state.machines_in_use[machine_id] = remaining
            elif machine_id in self.state.machines_in_use:
                del self.state.machines_in_use[machine_id]

    def _rebuild_machines_in_use(self) -> None:
        machines_in_use: Dict[str, int] = {}
        for proc in self.state.active_processes:
            for machine_id, count in proc.machines_reserved.items():
                if count <= 0:
                    continue
                machines_in_use[machine_id] = machines_in_use.get(machine_id, 0) + count
        self.state.machines_in_use = machines_in_use

    # ========================================================================
    # Process execution
    # ========================================================================

    def start_process(
        self,
        process_id: str,
        scale: float = 1.0,
        duration_hours: Optional[float] = None,
        output_quantity: Optional[float] = None,
        output_unit: Optional[str] = None,
        start_time: Optional[float] = None,
        recipe_run_id: Optional[str] = None,
        step_index: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Start a process using ADR-020 event-driven scheduling.

        Args:
            process_id: Process definition ID
            scale: Process scale factor
            duration_hours: Process duration (or calculated from output)
            output_quantity: Requested output quantity (for duration calculation)
            output_unit: Requested output unit (for duration calculation)
            start_time: When to start (default: now)
            recipe_run_id: Parent recipe run ID (if part of recipe)
            step_index: Step index in recipe (if applicable)

        Returns:
            Dict with success, process_run_id, and scheduling info
        """
        # Validate process exists
        process_model = self.kb.get_process(process_id)
        if not process_model:
            return {
                "success": False,
                "error": "kb_gap",
                "message": f"Process '{process_id}' not found in KB",
            }

        process_def = process_model.model_dump() if hasattr(process_model, 'model_dump') else process_model

        # ADR-020 validation
        validation_issues = validate_process_adr020(process_def, self.kb.items)
        errors = [i for i in validation_issues if i.level == ValidationLevel.ERROR]

        if errors:
            return {
                "success": False,
                "error": "validation_error",
                "message": f"Process '{process_id}' failed ADR-020 validation: {errors[0].message}",
                "validation_errors": [
                    {"rule": e.rule, "message": e.message} for e in errors
                ],
            }

        # Generate unique process_run_id
        process_run_id = str(uuid.uuid4())

        # Calculate duration if not provided
        duration_calculated = False
        if duration_hours is None:
            if output_quantity is not None and output_unit is not None:
                try:
                    # Build input quantities dict
                    inputs_dict = {}
                    for inp in process_def.get("inputs", []):
                        inp_id = inp.get("item_id")
                        base_qty = inp.get("quantity") or inp.get("qty", 0)
                        unit = inp.get("unit", "kg")
                        inputs_dict[inp_id] = Quantity(item_id=inp_id, qty=base_qty * scale, unit=unit)

                    # Build output quantities dict
                    outputs = {}
                    for outp in process_def.get("outputs", []):
                        outp_id = outp.get("item_id")
                        outputs[outp_id] = Quantity(item_id=outp_id, qty=output_quantity, unit=output_unit)

                    duration_hours = calculate_duration(
                        process_model,
                        inputs=inputs_dict,
                        outputs=outputs,
                        converter=self.converter
                    )
                    duration_calculated = True

                    # Calculate effective scale from requested output
                    first_output = process_def.get("outputs", [])[0] if process_def.get("outputs") else None
                    if first_output:
                        base_output_qty = first_output.get("quantity") or first_output.get("qty", 1)
                        scale = output_quantity / base_output_qty if base_output_qty > 0 else 1.0

                except Exception as e:
                    return {
                        "success": False,
                        "error": "duration_calculation_failed",
                        "message": f"Failed to calculate duration: {e}",
                    }
            else:
                return {
                    "success": False,
                    "error": "missing_duration",
                    "message": "Must provide either duration_hours or (output_quantity + output_unit)",
                }

        # Calculate inputs needed
        inputs = process_def.get("inputs", [])
        inputs_consumed = {}

        for inp in inputs:
            requested_item_id = inp.get("item_id")
            base_quantity = inp.get("quantity") or inp.get("qty", 0)
            unit = inp.get("unit", "kg")
            needed_quantity = base_quantity * scale

            # Try exact match first
            actual_item_id = None
            if self.has_item(requested_item_id, needed_quantity, unit):
                actual_item_id = requested_item_id
            else:
                # Try material_class matching
                requested_item_model = self.kb.get_item(requested_item_id)
                if requested_item_model:
                    requested_item_def = requested_item_model.model_dump() if hasattr(requested_item_model, 'model_dump') else requested_item_model
                    requested_class = requested_item_def.get("material_class")
                    if requested_class:
                        for inv_item_id in self.state.inventory.keys():
                            inv_item_model = self.kb.get_item(inv_item_id)
                            if inv_item_model:
                                inv_item_def = inv_item_model.model_dump() if hasattr(inv_item_model, 'model_dump') else inv_item_model
                                if inv_item_def.get("material_class") == requested_class:
                                    if self.has_item(inv_item_id, needed_quantity, unit):
                                        actual_item_id = inv_item_id
                                        break

            if actual_item_id is None:
                return {
                    "success": False,
                    "error": "insufficient_inputs",
                    "message": f"Insufficient {requested_item_id}: need {needed_quantity} {unit}",
                }

            inputs_consumed[actual_item_id] = InventoryItem(
                quantity=needed_quantity, unit=unit
            )

        # Calculate outputs
        outputs = process_def.get("outputs", [])
        outputs_pending = {}

        for outp in outputs:
            item_id = outp.get("item_id")
            base_quantity = outp.get("quantity") or outp.get("qty", 0)
            unit = outp.get("unit", "kg")
            output_quantity = base_quantity * scale

            outputs_pending[item_id] = InventoryItem(
                quantity=output_quantity, unit=unit
            )

        # Collect machine requirements
        machines_reserved = {}
        for req in process_def.get('resource_requirements', []):
            machine_id = req.get('machine_id')
            qty = req.get('qty', 1.0)
            if machine_id:
                machines_reserved[machine_id] = qty

        # Update machine capacities from current inventory
        self._update_machine_capacities()

        # Determine start time
        if start_time is None:
            start_time = self.scheduler.current_time

        end_time = start_time + duration_hours

        # Add machine reservations
        for machine_id, qty in machines_reserved.items():
            unit = 'count'  # default
            for req in process_def.get('resource_requirements', []):
                if req.get('machine_id') == machine_id:
                    unit = req.get('unit', 'count')
                    break

            success = self.reservation_manager.add_reservation(
                machine_id=machine_id,
                process_run_id=process_run_id,
                start_time=start_time,
                end_time=end_time,
                qty=qty,
                unit=unit,
            )

            if not success:
                # Cleanup reservations already made
                self.reservation_manager.remove_reservation(process_run_id)
                return {
                    "success": False,
                    "error": "machine_conflict",
                    "message": f"Machine '{machine_id}' not available at time {start_time}-{end_time}h",
                }

            # For partial (unit: hr) reservations, schedule a release event
            if unit == 'hr' and qty < duration_hours:
                release_time = start_time + qty
                self.scheduler.schedule_machine_release(
                    process_run_id=process_run_id,
                    machine_id=machine_id,
                    release_time=release_time,
                    qty=qty,
                )

        # Convert InventoryItem objects to simple dicts for scheduler
        inputs_dict = {
            item_id: inv_item.quantity
            for item_id, inv_item in inputs_consumed.items()
        }
        outputs_dict = {
            item_id: inv_item.quantity
            for item_id, inv_item in outputs_pending.items()
        }

        # Schedule with ADR-020 scheduler
        self.scheduler.schedule_process_start(
            process_run_id=process_run_id,
            process_id=process_id,
            start_time=start_time,
            duration_hours=duration_hours,
            scale=scale,
            inputs_consumed=inputs_dict,
            outputs_pending=outputs_dict,
            machines_reserved=machines_reserved,
            recipe_run_id=recipe_run_id,
            step_index=step_index,
        )

        # Log the process scheduling immediately so it can be reconstructed on load
        inputs_consumed_with_units = {
            item_id: {"quantity": inv_item.quantity, "unit": inv_item.unit}
            for item_id, inv_item in inputs_consumed.items()
        }
        outputs_pending_with_units = {
            item_id: {"quantity": inv_item.quantity, "unit": inv_item.unit}
            for item_id, inv_item in outputs_pending.items()
        }
        machine_reservations_list = []
        for req in process_def.get('resource_requirements', []):
            machine_id = req.get('machine_id')
            if not machine_id:
                continue
            qty = req.get('qty', 1.0)
            unit = req.get('unit', 'count')
            reservation_type = 'FULL_DURATION'
            release_time = None
            reservation_end = end_time
            if unit == 'hr':
                reservation_type = 'PARTIAL'
                release_time = start_time + qty
                reservation_end = release_time

            machine_reservations_list.append({
                "machine_id": machine_id,
                "start_time": start_time,
                "end_time": reservation_end,
                "qty": qty,
                "unit": unit,
                "reservation_type": reservation_type,
                "release_time": release_time,
            })

        self._log_event(
            ProcessScheduledEvent(
                process_id=process_id,
                process_run_id=process_run_id,
                scheduled_start_time=start_time,
                duration_hours=duration_hours,
                scheduled_end_time=end_time,
                scale=scale,
                inputs_consumed=inputs_consumed_with_units,
                outputs_pending=outputs_pending_with_units,
                machine_reservations=machine_reservations_list,
                recipe_run_id=recipe_run_id,
                step_index=step_index,
            )
        )

        return {
            "success": True,
            "process_run_id": process_run_id,
            "process_id": process_id,
            "start_time": start_time,
            "duration_hours": duration_hours,
            "end_time": end_time,
            "ends_at": end_time,  # For backward compatibility
            "duration_calculated": duration_calculated,
            "inputs_consumed": {k: {"quantity": v.quantity, "unit": v.unit} for k, v in inputs_consumed.items()},
            "outputs_pending": {k: {"quantity": v.quantity, "unit": v.unit} for k, v in outputs_pending.items()},
            "machines_reserved": machines_reserved,
        }

    def resolve_step(self, step_def: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve a recipe step to a fully-specified process instance.

        Supports three modes:
        1. Reference: step has process_id, inherits from process definition
        2. Override: step has process_id + override fields (ADR-013)
        3. Inline: step has no process_id, defines everything inline

        Args:
            step_def: Step definition from recipe

        Returns:
            Resolved process definition with all fields populated
        """
        if "process_id" in step_def:
            # Reference mode: Load base process
            process_id = step_def["process_id"]
            base_process_model = self.kb.get_process(process_id)

            if not base_process_model:
                # Process not found - return step as-is with warning
                return {
                    **step_def,
                    "_warning": f"Process '{process_id}' not found in KB",
                }

            # Convert to dict
            base_process = base_process_model.model_dump() if hasattr(base_process_model, 'model_dump') else base_process_model

            # Start with base process
            resolved = dict(base_process)

            # Apply step-level overrides (step fields override process fields)
            # Special handling for certain fields:
            scale = step_def.get("scale", 1.0)

            # Override direct fields
            for key in ["inputs", "outputs", "byproducts", "requires_ids",
                       "resource_requirements", "energy_model"]:
                if key in step_def:
                    resolved[key] = step_def[key]

            # Special handling for time_model per ADR-013: partial vs complete override
            if "time_model" in step_def:
                step_time_model = step_def["time_model"]
                # Check if step has a non-None 'type' field (complete override)
                # or missing/None 'type' field (partial override - merge with base)
                has_type = isinstance(step_time_model, dict) and step_time_model.get("type") is not None

                if not has_type:
                    # Partial override: merge with base process time_model
                    base_time_model = resolved.get("time_model", {})
                    if isinstance(base_time_model, dict):
                        # Start with base, then apply step overrides
                        # Filter out None values from step to preserve base values
                        merged = dict(base_time_model)
                        if isinstance(step_time_model, dict):
                            for key, value in step_time_model.items():
                                if value is not None:
                                    merged[key] = value
                        resolved["time_model"] = merged
                    else:
                        # Base is not a dict (shouldn't happen), use step as-is
                        resolved["time_model"] = step_time_model
                else:
                    # Complete override: step has non-None "type" field
                    resolved["time_model"] = step_time_model

            # Apply scale multiplier if present
            if scale != 1.0:
                for key in ["inputs", "outputs", "byproducts"]:
                    if key in resolved:
                        for item in resolved[key]:
                            if "qty" in item:
                                item["qty"] *= scale
                            elif "quantity" in item:
                                item["quantity"] *= scale

            # Override specific time/labor estimates
            for key in ["est_time_hr", "machine_hours", "labor_hours", "notes"]:
                if key in step_def:
                    resolved[key] = step_def[key]

            return resolved

        else:
            # Inline mode: Step IS the process definition
            return dict(step_def)

    def run_recipe(
        self,
        recipe_id: str,
        quantity: int = 1,
        start_time: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Run a recipe using ADR-020 orchestration.

        Instead of running as a single process, schedules each step
        based on dependencies.

        Args:
            recipe_id: Recipe definition ID
            quantity: Number of recipe instances to run (for backward compatibility, currently ignored)
            start_time: When recipe starts (default: now)

        Returns:
            Dict with success, recipe_run_id, and orchestration info
        """
        # Validate recipe exists
        recipe_model = self.kb.get_recipe(recipe_id)
        if not recipe_model:
            return {
                "success": False,
                "error": "kb_gap",
                "message": f"Recipe '{recipe_id}' not found in KB",
            }

        recipe_def = recipe_model.model_dump() if hasattr(recipe_model, 'model_dump') else recipe_model

        # ADR-020 validation
        validation_issues = validate_recipe_adr020(recipe_def)
        errors = [i for i in validation_issues if i.level == ValidationLevel.ERROR]

        if errors:
            return {
                "success": False,
                "error": "validation_error",
                "message": f"Recipe '{recipe_id}' failed ADR-020 validation: {errors[0].message}",
                "validation_errors": [
                    {"rule": e.rule, "message": e.message} for e in errors
                ],
            }

        if start_time is None:
            start_time = self.scheduler.current_time

        # Start recipe with orchestrator
        recipe_run_id = self.orchestrator.start_recipe(
            recipe_id=recipe_id,
            recipe_dict=recipe_def,
            target_item_id=recipe_def.get('target_item_id', 'unknown'),
            start_time=start_time,
        )

        # Schedule ready steps
        ready_steps = self.orchestrator.get_ready_steps(recipe_run_id)

        scheduled_count = 0
        for step_idx in ready_steps:
            recipe_run = self.orchestrator.get_recipe_run(recipe_run_id)
            step = recipe_def['steps'][step_idx]

            # Resolve step to apply overrides (ADR-013)
            resolved_process = self.resolve_step(step)

            # Get process_id from resolved process
            process_id = resolved_process.get('id') or step.get('process_id')
            if not process_id:
                return {
                    "success": False,
                    "error": "invalid_recipe",
                    "message": f"Step {step_idx} missing process_id",
                    "failed_step": step_idx,
                }

            # Calculate duration from resolved process (respects step overrides)
            # Get default output quantity and unit from first output
            outputs = resolved_process.get('outputs', [])
            output_quantity = None
            output_unit = None
            duration_hours = None
            scale = 1.0

            # Always try to calculate duration_hours from time_model
            time_model = resolved_process.get('time_model', {})
            if time_model.get('type') == 'batch':
                duration_hours = time_model.get('hr_per_batch', 1.0)
            elif time_model.get('type') == 'linear_rate':
                # Need outputs to calculate from rate
                pass

            if outputs:
                first_output = outputs[0]
                output_quantity = first_output.get('qty', first_output.get('quantity', 1.0))
                output_unit = first_output.get('unit', 'kg')

                base_process = self.kb.get_process(process_id)
                if base_process:
                    base_def = base_process.model_dump() if hasattr(base_process, 'model_dump') else base_process
                    base_outputs = base_def.get('outputs', [])
                    if base_outputs:
                        base_output = base_outputs[0]
                        base_qty = base_output.get('qty', base_output.get('quantity', 1.0))
                        if base_qty:
                            scale = output_quantity / base_qty

                # For linear_rate, calculate duration from outputs
                if time_model.get('type') == 'linear_rate' and duration_hours is None:
                    rate = time_model.get('rate', 1.0)
                    scaling_basis = time_model.get('scaling_basis')
                    if scaling_basis and scaling_basis in [o.get('item_id') for o in outputs]:
                        # Find output with this basis
                        for outp in outputs:
                            if outp.get('item_id') == scaling_basis:
                                outp_qty = outp.get('qty', outp.get('quantity', 1.0))
                                duration_hours = outp_qty / rate if rate > 0 else 1.0
                                break

            # Fallback if duration still not set
            if duration_hours is None:
                duration_hours = 1.0

            # Schedule step process with calculated duration
            result = self.start_process(
                process_id=process_id,
                scale=scale,
                start_time=start_time,
                duration_hours=duration_hours,
                output_quantity=output_quantity,
                output_unit=output_unit,
                recipe_run_id=recipe_run_id,
                step_index=step_idx,
            )

            if result['success']:
                self.orchestrator.schedule_step(
                    recipe_run_id,
                    step_idx,
                    result['process_run_id']
                )
                scheduled_count += 1
            elif result.get('error') == 'machine_conflict':
                # Machine conflict - don't fail recipe, just skip this step for now
                # It will be retried later when machines become available
                # Don't mark step as failed, leave it pending
                continue
            else:
                # Other failure - cancel recipe
                self.orchestrator.cancel_recipe(recipe_run_id)
                return {
                    "success": False,
                    "error": "step_scheduling_failed",
                    "message": f"Failed to schedule step {step_idx}: {result.get('message')}",
                    "failed_step": step_idx,
                }

        return {
            "success": True,
            "recipe_run_id": recipe_run_id,
            "recipe_id": recipe_id,
            "start_time": start_time,
            "total_steps": len(recipe_def['steps']),
            "scheduled_steps": scheduled_count,
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
            quantity = comp.get("qty") or comp.get("quantity") or 1
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

    # ========================================================================
    # Recipe Energy Helpers
    # ========================================================================

    def _to_quantity(self, entry: Any, multiplier: float = 1.0) -> Quantity:
        """Normalize raw entries into Quantity for calculations."""
        if isinstance(entry, dict):
            item_id = entry.get("item_id")
            qty = entry.get("qty") if entry.get("qty") is not None else entry.get("quantity")
            unit = entry.get("unit", "kg")
        else:
            item_id = getattr(entry, "item_id", None)
            qty = getattr(entry, "qty", None)
            if qty is None:
                qty = getattr(entry, "quantity", None)
            unit = getattr(entry, "unit", "kg")
        return Quantity(item_id=item_id, qty=float(qty or 0) * multiplier, unit=unit)

    def _merge_energy_model(self, base_model: Any, override: Any) -> Optional[RawEnergyModel]:
        """Merge energy_model overrides per ADR-013 semantics."""
        if override is None:
            if base_model is None:
                return None
            if isinstance(base_model, RawEnergyModel):
                return base_model
            if hasattr(base_model, "model_dump"):
                return RawEnergyModel(**base_model.model_dump())
            if isinstance(base_model, dict):
                return RawEnergyModel(**base_model)
            return None

        override_data = override.model_dump() if hasattr(override, "model_dump") else dict(override)
        if override_data.get("type"):
            return RawEnergyModel(**override_data)

        if base_model is None:
            return RawEnergyModel(**override_data)

        base_data = base_model.model_dump() if hasattr(base_model, "model_dump") else dict(base_model)
        for key, value in override_data.items():
            if value is not None:
                base_data[key] = value
        return RawEnergyModel(**base_data)

    def _calculate_recipe_energy(self, recipe_id: str, multiplier: float) -> float:
        """Calculate total energy for a recipe by summing step energies."""
        recipe_model = self.kb.get_recipe(recipe_id)
        if not recipe_model:
            return 0.0

        recipe_def = recipe_model.model_dump() if hasattr(recipe_model, "model_dump") else recipe_model
        total_energy = 0.0
        warn_zero = os.getenv("SIM_WARN_ZERO_RECIPE_ENERGY", "1") != "0"

        for step in recipe_def.get("steps", []):
            process_id = step.get("process_id")
            process_model = self.kb.get_process(process_id)
            if not process_model:
                continue

            process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
            merged_energy = self._merge_energy_model(process_def.get("energy_model"), step.get("energy_model"))

            process_def["energy_model"] = merged_energy
            step_process = RawProcess(**process_def)

            step_inputs = step.get("inputs") or process_def.get("inputs", [])
            step_outputs = step.get("outputs") or process_def.get("outputs", [])

            inputs_for_calc = {
                q.item_id: q for q in (self._to_quantity(e, multiplier) for e in step_inputs)
                if q.item_id
            }
            outputs_for_calc = {
                q.item_id: q for q in (self._to_quantity(e, multiplier) for e in step_outputs)
                if q.item_id
            }

            if not step_process.energy_model:
                continue

            try:
                step_energy = calculate_energy(
                    step_process,
                    inputs=inputs_for_calc,
                    outputs=outputs_for_calc,
                    converter=self.converter,
                )
                if warn_zero and step_energy == 0.0:
                    print(
                        f"⚠️  Recipe step '{process_id}' used 0 kWh. Bug?",
                        file=sys.stderr,
                    )
                total_energy += step_energy
            except Exception:
                continue

        return total_energy

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
        item_model = self.kb.get_item(item_id)
        if not item_model:
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
            # Try to convert to kg (handle Pydantic models)
            try:
                mass_kg = self.converter.convert(quantity, unit, "kg", item_id)
            except Exception:
                # Conversion failed, that's okay
                pass

        # Log event
        self._log_event(
            ImportEvent(
                item_id=item_id,
                quantity=quantity,
                unit=unit,
                mass_kg=mass_kg,
            )
        )

        # Create state snapshot so import persists
        self._log_event(
            StateSnapshotEvent(
                time_hours=self.state.current_time_hours,
                inventory=self.state.inventory,
                active_processes=self.state.active_processes,
                machines_built=self.state.machines_built,
                machines_in_use=self.state.machines_in_use,
                total_energy_kwh=self.state.total_energy_kwh,
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
        Preview what would happen if time advanced (ADR-020 version).

        Does NOT commit changes.

        Returns:
            {
                "new_time": float,
                "processes_completing": [{process_id, outputs}, ...],
                "errors": [str, ...] if any
            }
        """
        new_time = self.scheduler.current_time + duration_hours

        # Find processes that would complete in ADR-020 scheduler
        completing = []
        for process_run in self.scheduler.active_processes.values():
            if process_run.end_time <= new_time:
                # Get process definition to reconstruct outputs with units
                process_model = self.kb.get_process(process_run.process_id)
                outputs_dict = {}

                if process_model:
                    if hasattr(process_model, 'model_dump'):
                        process_def = process_model.model_dump()
                    else:
                        process_def = process_model

                    for outp in process_def.get("outputs", []):
                        item_id = outp.get("item_id")
                        unit = outp.get("unit", "kg")
                        if item_id in process_run.outputs_pending:
                            outputs_dict[item_id] = {
                                "quantity": process_run.outputs_pending[item_id],
                                "unit": unit
                            }

                completing.append({
                    "process_id": process_run.process_id,
                    "ends_at": process_run.end_time,
                    "outputs": outputs_dict,
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
            "active_processes_count": len(self.scheduler.active_processes),
            "completing_count": len(completing),
        }

    def advance_time(self, duration_hours: float) -> Dict[str, Any]:
        """
        Advance time using ADR-020 event-driven scheduler.

        Processes events chronologically:
        - Process starts (inputs consumed)
        - Process completions (outputs added, machines released)
        - Recipe step dependencies (schedule ready steps)

        Args:
            duration_hours: Time delta to advance

        Returns:
            Dict with completed processes and events
        """
        target_time = self.scheduler.current_time + duration_hours

        # Process all events up to target time
        processed_events = self.scheduler.advance_to(target_time)

        # Track what happened
        completed_processes = []
        started_processes = []

        for event in processed_events:
            if event.event_type == EventType.PROCESS_START:
                # Process started - book energy
                process_run_id = event.data.get("process_run_id")

                # Get process run from active or completed processes
                # (it might have been canceled by input validation, in which case skip it)
                process_run = None
                if process_run_id in self.scheduler.active_processes:
                    process_run = self.scheduler.active_processes[process_run_id]
                elif any(p.process_run_id == process_run_id for p in self.scheduler.completed_processes):
                    # Process completed in the same advance_to call
                    process_run = next(p for p in self.scheduler.completed_processes if p.process_run_id == process_run_id)

                if not process_run:
                    # Process was canceled (e.g., due to insufficient inputs)
                    continue

                # Get process definition for energy calculation
                process_model = self.kb.get_process(process_run.process_id)
                if process_model:
                    if hasattr(process_model, 'model_dump'):
                        process_def = process_model.model_dump()
                    else:
                        process_def = process_model

                    # Calculate and book energy at process start (ADR-014/ADR-016)
                    energy_kwh = 0.0
                    if process_def.get('energy_model'):
                        try:
                            # Build input quantities for energy calculation
                            inputs_dict = {}
                            for inp in process_def.get("inputs", []):
                                inp_id = inp.get("item_id")
                                if inp_id in process_run.inputs_consumed:
                                    qty = process_run.inputs_consumed[inp_id]
                                    unit = inp.get("unit", "kg")
                                    inputs_dict[inp_id] = Quantity(item_id=inp_id, qty=qty, unit=unit)

                            # Build output quantities for energy calculation
                            outputs_dict = {}
                            for outp in process_def.get("outputs", []):
                                outp_id = outp.get("item_id")
                                if outp_id in process_run.outputs_pending:
                                    qty = process_run.outputs_pending[outp_id]
                                    unit = outp.get("unit", "kg")
                                    outputs_dict[outp_id] = Quantity(item_id=outp_id, qty=qty, unit=unit)

                            energy_kwh = calculate_energy(
                                process_model,
                                inputs=inputs_dict,
                                outputs=outputs_dict,
                                converter=self.converter
                            )
                        except Exception as e:
                            # If calculation fails, energy stays at 0.0
                            pass

                    # Accumulate energy into total
                    self.state.total_energy_kwh += energy_kwh

                    # Store energy on process_run for later retrieval
                    # We need to extend ProcessRun or store it separately
                    # For now, store in a dict keyed by process_run_id
                    if not hasattr(self, '_process_energy'):
                        self._process_energy = {}
                    self._process_energy[process_run_id] = energy_kwh

                # Log activation event for lifecycle tracking
                self._log_event(
                    ProcessStartEvent(
                        process_id=process_run.process_id,
                        process_run_id=process_run_id,
                        actual_start_time=event.time,
                        scale=process_run.scale,
                    )
                )

                started_processes.append({
                    "process_run_id": event.data.get("process_run_id"),
                    "process_id": event.data.get("process_id"),
                    "time": event.time,
                })

            elif event.event_type == EventType.PROCESS_COMPLETE:
                # Process completed - add outputs
                process_run_id = event.data.get("process_run_id")

                # Find process in completed list
                process_run = None
                for proc in self.scheduler.completed_processes:
                    if proc.process_run_id == process_run_id:
                        process_run = proc
                        break

                if process_run:
                    # Add outputs to inventory with correct units
                    # Get process definition to look up output units
                    process_model = self.kb.get_process(process_run.process_id)
                    if process_model:
                        if hasattr(process_model, 'model_dump'):
                            process_def = process_model.model_dump()
                        else:
                            process_def = process_model

                        # Build a map of item_id -> unit from process outputs
                        output_units = {}
                        for outp in process_def.get("outputs", []):
                            output_units[outp.get("item_id")] = outp.get("unit", "kg")

                        # Add outputs with their correct units
                        for item_id, qty in process_run.outputs_pending.items():
                            unit = output_units.get(item_id, "kg")
                            self.add_to_inventory(item_id, qty, unit)
                    else:
                        # Fallback if process definition not found
                        for item_id, qty in process_run.outputs_pending.items():
                            self.add_to_inventory(item_id, qty, "kg")

                    # Release machine reservations
                    self.reservation_manager.remove_reservation(process_run_id)

                    # Reconstruct outputs with units for event logging
                    process_model = self.kb.get_process(process_run.process_id)
                    outputs_with_units = {}
                    if process_model:
                        # Convert to dict if it's a Pydantic model
                        if hasattr(process_model, 'model_dump'):
                            process_def = process_model.model_dump()
                        else:
                            process_def = process_model

                        for outp in process_def.get("outputs", []):
                            item_id = outp.get("item_id")
                            unit = outp.get("unit", "kg")
                            if item_id in process_run.outputs_pending:
                                outputs_with_units[item_id] = InventoryItem(
                                    quantity=process_run.outputs_pending[item_id],
                                    unit=unit
                                )

                    # Retrieve stored energy for this process
                    energy_kwh = 0.0
                    if hasattr(self, '_process_energy') and process_run_id in self._process_energy:
                        energy_kwh = self._process_energy[process_run_id]

                    # Log completion event
                    self._log_event(
                        ProcessCompleteEvent(
                            process_id=process_run.process_id,
                            process_run_id=process_run_id,
                            recipe_run_id=process_run.recipe_run_id,
                            time_hours=event.time,
                            outputs=outputs_with_units,
                            energy_kwh=energy_kwh,
                        )
                    )

                    completed_processes.append({
                        "process_run_id": process_run_id,
                        "process_id": process_run.process_id,
                        "time": event.time,
                        "outputs": process_run.outputs_pending,
                        "energy_kwh": energy_kwh,
                    })

                    # Check if this was a recipe step - schedule dependent steps
                    if process_run.recipe_run_id:
                        recipe_run_id = process_run.recipe_run_id
                        ready_steps = self.orchestrator.get_ready_steps(recipe_run_id)

                        for step_idx in ready_steps:
                            recipe_run = self.orchestrator.get_recipe_run(recipe_run_id)
                            if recipe_run:
                                recipe_def = self.kb.get_recipe(recipe_run.recipe_id).model_dump()
                                step = recipe_def['steps'][step_idx]

                                # Get process_id directly from step
                                process_id = step.get('process_id')
                                if not process_id:
                                    continue  # Skip invalid step

                                # Get process definition to extract default output
                                process_def_model = self.kb.get_process(process_id)
                                if not process_def_model:
                                    continue  # Skip if process not found

                                process_dict = process_def_model.model_dump() if hasattr(process_def_model, 'model_dump') else process_def_model

                                # Get default output quantity and unit from first output
                                outputs = process_dict.get('outputs', [])
                                output_quantity = None
                                output_unit = None
                                if outputs:
                                    first_output = outputs[0]
                                    output_quantity = first_output.get('qty', first_output.get('quantity', 1.0))
                                    output_unit = first_output.get('unit', 'kg')

                                # Schedule dependent step
                                result = self.start_process(
                                    process_id=process_id,
                                    scale=1.0,
                                    start_time=event.time,
                                    output_quantity=output_quantity,
                                    output_unit=output_unit,
                                    recipe_run_id=recipe_run_id,
                                    step_index=step_idx,
                                )

                                if result['success']:
                                    self.orchestrator.schedule_step(
                                        recipe_run_id,
                                        step_idx,
                                        result['process_run_id']
                                    )

        # Update engine state time
        self.state.current_time_hours = target_time

        # Log state snapshot
        self._log_event(
            StateSnapshotEvent(
                time_hours=target_time,
                inventory=self.state.inventory,
                active_processes=self.state.active_processes,
                machines_built=self.state.machines_built,
                machines_in_use=self.state.machines_in_use,
                total_energy_kwh=self.state.total_energy_kwh,
            )
        )

        return {
            "new_time": target_time,
            "events_processed": len(processed_events),
            "processes_started": len(started_processes),
            "processes_completed": len(completed_processes),
            "completed_count": len(completed_processes),  # For backward compatibility
            "completed": completed_processes,
            "started": started_processes,
            "total_energy_kwh": self.state.total_energy_kwh,
        }
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
                        self.state.machines_in_use = event.get("machines_in_use", {})

                        # Backfill machine reservations when loading older snapshots
                        for proc in self.state.active_processes:
                            if proc.machines_reserved:
                                continue
                            if proc.process_id.startswith("recipe:"):
                                recipe_id = proc.process_id[7:]
                                recipe_model = self.kb.get_recipe(recipe_id)
                                if recipe_model:
                                    recipe_def = recipe_model.model_dump() if hasattr(recipe_model, "model_dump") else recipe_model
                                    resolved_steps = [self.resolve_step(step) for step in recipe_def.get("steps", [])]
                                    proc.machines_reserved = self._collect_required_machines_from_steps(
                                        resolved_steps, recipe_def
                                    )
                            else:
                                process_model = self.kb.get_process(proc.process_id)
                                if process_model:
                                    process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
                                    proc.machines_reserved = self._collect_required_machines_from_process_def(
                                        process_def
                                    )

                        if not self.state.machines_in_use:
                            self._rebuild_machines_in_use()
                        self.state.total_energy_kwh = event.get("total_energy_kwh", 0.0)

                    # Track imports
                    elif event_type == "import":
                        item_id = event.get("item_id")
                        quantity = event.get("quantity")
                        unit = event.get("unit")
                        if item_id:
                            # Add to inventory (so imports are actually available)
                            self.add_to_inventory(item_id, quantity, unit)

                            # Track in total_imports (for reporting)
                            if item_id in self.state.total_imports:
                                existing = self.state.total_imports[item_id]
                                if existing.unit == unit:
                                    existing.quantity += quantity
                            else:
                                self.state.total_imports[item_id] = InventoryItem(
                                    quantity=quantity, unit=unit
                                )

                    # Replay build events
                    elif event_type == "build":
                        machine_id = event.get("machine_id")
                        components_consumed = event.get("components_consumed", {})
                        if machine_id:
                            # Subtract components from inventory
                            for item_id, inv_data in components_consumed.items():
                                inv_item = InventoryItem(**inv_data)
                                self.subtract_from_inventory(
                                    item_id, inv_item.quantity, inv_item.unit
                                )

                            # Add machine to inventory
                            self.add_to_inventory(machine_id, 1, "count")

                            # Add to machines_built list
                            if machine_id not in self.state.machines_built:
                                self.state.machines_built.append(machine_id)

                except json.JSONDecodeError:
                    continue

        # Reconstruct scheduler and machine reservations from process_scheduled events
        self._update_machine_capacities()
        if self.reservation_manager is None:
            self._init_reservation_manager()

        if self.reservation_manager is not None:
            self.scheduler.current_time = self.state.current_time_hours
            self.reservation_manager.current_time = self.state.current_time_hours

            completed_processes = set()
            with self.log_file.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        event = json.loads(line)
                        if event.get("type") == "process_complete":
                            process_run_id = event.get("process_run_id")
                            if process_run_id:
                                completed_processes.add(process_run_id)
                    except json.JSONDecodeError:
                        continue

            with self.log_file.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        event = json.loads(line)
                        if event.get("type") != "process_scheduled":
                            continue

                        process_run_id = event.get("process_run_id")
                        if not process_run_id or process_run_id in completed_processes:
                            continue

                        scheduled_start_time = event.get("scheduled_start_time", 0.0)
                        scheduled_end_time = event.get("scheduled_end_time", 0.0)

                        if scheduled_end_time <= self.state.current_time_hours:
                            continue

                        inputs_consumed = {}
                        for item_id, item_data in event.get("inputs_consumed", {}).items():
                            if isinstance(item_data, dict):
                                inputs_consumed[item_id] = item_data.get("quantity", 0.0)
                            else:
                                inputs_consumed[item_id] = item_data

                        outputs_pending = {}
                        for item_id, item_data in event.get("outputs_pending", {}).items():
                            if isinstance(item_data, dict):
                                outputs_pending[item_id] = item_data.get("quantity", 0.0)
                            else:
                                outputs_pending[item_id] = item_data

                        machines_reserved = {}
                        for reservation in event.get("machine_reservations", []):
                            machine_id = reservation.get("machine_id")
                            qty = reservation.get("qty", 0.0)
                            if machine_id:
                                machines_reserved[machine_id] = machines_reserved.get(machine_id, 0.0) + qty

                        if scheduled_start_time > self.state.current_time_hours:
                            self.scheduler.schedule_process_start(
                                process_run_id=process_run_id,
                                process_id=event.get("process_id"),
                                start_time=scheduled_start_time,
                                duration_hours=event.get("duration_hours", 0.0),
                                scale=event.get("scale", 1.0),
                                inputs_consumed=inputs_consumed,
                                outputs_pending=outputs_pending,
                                machines_reserved=machines_reserved,
                                recipe_run_id=event.get("recipe_run_id"),
                                step_index=event.get("step_index"),
                            )
                        else:
                            from src.simulation.scheduler import ProcessRun

                            process_run = ProcessRun(
                                process_run_id=process_run_id,
                                process_id=event.get("process_id"),
                                start_time=scheduled_start_time,
                                duration_hours=event.get("duration_hours", 0.0),
                                end_time=scheduled_end_time,
                                scale=event.get("scale", 1.0),
                                inputs_consumed=inputs_consumed,
                                outputs_pending=outputs_pending,
                                machines_reserved=machines_reserved,
                                recipe_run_id=event.get("recipe_run_id"),
                                step_index=event.get("step_index"),
                            )

                            self.scheduler.active_processes[process_run_id] = process_run
                            self.scheduler.schedule_event(
                                time=scheduled_end_time,
                                event_type=EventType.PROCESS_COMPLETE,
                                event_id=f"complete_{process_run_id}",
                                priority=5,
                                data={
                                    'process_run_id': process_run_id,
                                }
                            )

                        for reservation in event.get("machine_reservations", []):
                            machine_id = reservation.get("machine_id")
                            if not machine_id:
                                continue
                            qty = reservation.get("qty", 0.0)
                            unit = reservation.get("unit", "count")
                            reservation_type = reservation.get("reservation_type", "FULL_DURATION")
                            release_time = reservation.get("release_time")
                            start_time = reservation.get("start_time", scheduled_start_time)
                            end_time = reservation.get("end_time", scheduled_end_time)

                            if reservation_type == "PARTIAL" and release_time:
                                if release_time <= self.state.current_time_hours:
                                    continue
                                end_time = release_time

                            success = self.reservation_manager.add_reservation(
                                machine_id=machine_id,
                                process_run_id=process_run_id,
                                start_time=start_time,
                                end_time=end_time,
                                qty=qty,
                                unit=unit,
                            )

                            if not success:
                                print(
                                    f"Warning: Could not restore reservation for {machine_id} "
                                    f"(process {process_run_id})",
                                    file=sys.stderr
                                )

                            if reservation_type == "PARTIAL" and release_time and release_time > self.state.current_time_hours:
                                self.scheduler.schedule_machine_release(
                                    process_run_id=process_run_id,
                                    machine_id=machine_id,
                                    release_time=release_time,
                                    qty=qty,
                                )
                    except json.JSONDecodeError:
                        continue

        return True

    def get_schedule_summary(self) -> Dict[str, Any]:
        """
        Get summary of scheduled and active processes.

        Returns:
            Dict with scheduler state
        """
        return {
            "current_time": self.scheduler.current_time,
            "queued_events": len(self.scheduler.event_queue),
            "active_processes": len(self.scheduler.active_processes),
            "completed_processes": len(self.scheduler.completed_processes),
            "next_event_time": self.scheduler.get_next_event_time(),
            "active_recipes": len(self.orchestrator.get_active_recipe_runs()),
            "completed_recipes": len(self.orchestrator.get_completed_recipe_runs()),
        }

    def get_machine_utilization(
        self,
        machine_id: str,
        time_range: Optional[tuple[float, float]] = None
    ) -> float:
        """
        Get machine utilization over time range.

        Args:
            machine_id: Machine to analyze
            time_range: (start, end) time range (default: 0 to current time)

        Returns:
            Utilization ratio (0.0 to 1.0)
        """
        if time_range is None:
            time_range = (0.0, self.scheduler.current_time)

        return self.reservation_manager.get_utilization(machine_id, time_range)
