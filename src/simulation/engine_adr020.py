"""
ADR-020 Enhanced Simulation Engine

Extends SimulationEngine with:
- Event-driven scheduling
- Machine reservation system
- Recipe orchestration
- Dependency-based execution

Maintains backward compatibility with existing engine.
"""
from __future__ import annotations

from typing import Dict, List, Optional, Any
from pathlib import Path
import uuid

from src.simulation.engine import SimulationEngine
from src.simulation.scheduler import Scheduler, EventType
from src.simulation.machine_reservations import MachineReservationManager
from src.simulation.recipe_orchestrator import RecipeOrchestrator
from src.simulation.adr020_validators import validate_process_adr020, validate_recipe_adr020
from src.kb_core.kb_loader import KBLoader
from src.kb_core.validators import ValidationLevel


class SimulationEngineADR020(SimulationEngine):
    """
    ADR-020 enhanced simulation engine.

    Adds:
    - Event-driven scheduler for chronological processing
    - Machine reservation system with time-based conflicts
    - Recipe orchestrator for dependency-based step execution
    - ADR-020 validation rules
    """

    def __init__(self, sim_id: str, kb_loader: KBLoader, sim_dir: Optional[Path] = None):
        """Initialize engine with ADR-020 components."""
        # Initialize base engine
        super().__init__(sim_id, kb_loader, sim_dir)

        # ADR-020 components
        self.scheduler = Scheduler()
        self.orchestrator = RecipeOrchestrator(self.scheduler)

        # Build machine capacities from inventory
        machine_capacities = self._build_machine_capacities()
        self.reservation_manager = MachineReservationManager(machine_capacities)

        # Enable ADR-020 mode
        self.adr020_mode = True

    def _build_machine_capacities(self) -> Dict[str, float]:
        """
        Build machine capacity dict from current inventory.

        Returns:
            Dict of machine_id -> capacity (count)
        """
        capacities = {}

        for item_id, inv_item in self.state.inventory.items():
            # Check if item is a machine
            item_model = self.kb.get_item(item_id)
            if item_model:
                item_def = item_model.model_dump() if hasattr(item_model, 'model_dump') else item_model
                if item_def.get('kind') == 'machine':
                    # Get quantity in count units
                    if inv_item.unit == 'count' or inv_item.unit == 'unit':
                        capacities[item_id] = inv_item.quantity

        return capacities

    def _update_machine_capacities(self) -> None:
        """Update reservation manager with current machine inventory."""
        capacities = self._build_machine_capacities()
        self.reservation_manager.machine_capacities = capacities

    def _collect_required_machines_from_process_def(self, process_def: Dict[str, Any]) -> Dict[str, float]:
        """
        Extract machine requirements from process definition.

        Args:
            process_def: Process definition dict

        Returns:
            Dict of machine_id -> qty required
        """
        machines = {}
        for req in process_def.get('resource_requirements', []):
            machine_id = req.get('machine_id')
            qty = req.get('qty', 1.0)
            if machine_id:
                machines[machine_id] = qty
        return machines

    def start_process_adr020(
        self,
        process_id: str,
        scale: float = 1.0,
        start_time: Optional[float] = None,
        duration_hours: Optional[float] = None,
        output_quantity: Optional[float] = None,
        output_unit: Optional[str] = None,
        recipe_run_id: Optional[str] = None,
        step_index: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Start a process using ADR-020 scheduler.

        Args:
            process_id: Process definition ID
            scale: Process scale factor
            start_time: When to start (default: now)
            duration_hours: Process duration (or calculated)
            output_quantity: Requested output quantity
            output_unit: Requested output unit
            recipe_run_id: Parent recipe run ID (if part of recipe)
            step_index: Step index in recipe (if applicable)

        Returns:
            Dict with success, process_run_id, and scheduling info
        """
        # ADR-020 validation
        process_model = self.kb.get_process(process_id)
        if not process_model:
            return {
                "success": False,
                "error": "kb_gap",
                "message": f"Process '{process_id}' not found in KB",
            }

        process_def = process_model.model_dump() if hasattr(process_model, 'model_dump') else process_model

        # Validate with ADR-020 rules
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

        # Generate process_run_id
        process_run_id = str(uuid.uuid4())

        # Use base engine to calculate inputs/outputs and duration
        base_result = super().start_process(
            process_id=process_id,
            scale=scale,
            duration_hours=duration_hours,
            output_quantity=output_quantity,
            output_unit=output_unit,
        )

        if not base_result.get("success"):
            # Add ADR-020 context to error
            base_result["adr020_mode"] = True
            return base_result

        # Get calculated values from base result
        actual_duration = base_result.get("duration_hours")

        # Get the active process that was just added
        if len(self.state.active_processes) > 0:
            active_proc = self.state.active_processes[-1]
            inputs_consumed = active_proc.inputs_consumed
            outputs_pending = active_proc.outputs_pending

            # Revert base engine's changes (we'll apply them via scheduler)
            # Put inputs back
            for item_id, inv_item in inputs_consumed.items():
                self.add_to_inventory(item_id, inv_item.quantity, inv_item.unit)

            # Remove the process from active (we'll schedule it properly)
            self.state.active_processes = []
        else:
            return {
                "success": False,
                "error": "internal_error",
                "message": "Base engine did not create active process",
            }

        # Build machines reserved dict
        machines_reserved = self._collect_required_machines_from_process_def(process_def)

        # Update machine capacities from current inventory
        self._update_machine_capacities()

        # Check and reserve machines using reservation manager
        if start_time is None:
            start_time = self.scheduler.current_time

        end_time = start_time + actual_duration

        # Add machine reservations
        for machine_id, qty in machines_reserved.items():
            # Get unit from resource_requirements
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
            duration_hours=actual_duration,
            scale=scale,
            inputs_consumed=inputs_dict,
            outputs_pending=outputs_dict,
            machines_reserved=machines_reserved,
            recipe_run_id=recipe_run_id,
            step_index=step_index,
        )

        return {
            "success": True,
            "process_run_id": process_run_id,
            "process_id": process_id,
            "start_time": start_time,
            "duration_hours": actual_duration,
            "end_time": end_time,
            "inputs_consumed": {k: {"quantity": v.quantity, "unit": v.unit} for k, v in inputs_consumed.items()},
            "outputs_pending": {k: {"quantity": v.quantity, "unit": v.unit} for k, v in outputs_pending.items()},
            "machines_reserved": machines_reserved,
        }

    def run_recipe_adr020(
        self,
        recipe_id: str,
        start_time: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Run a recipe using ADR-020 orchestration.

        Instead of running as a single process, schedules each step
        based on dependencies.

        Args:
            recipe_id: Recipe definition ID
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

            # Get process_id directly from step
            process_id = step.get('process_id')
            if not process_id:
                return {
                    "success": False,
                    "error": "invalid_recipe",
                    "message": f"Step {step_idx} missing process_id",
                    "failed_step": step_idx,
                }

            # Get process definition to extract default output
            process_def = self.kb.get_process(process_id)
            if not process_def:
                return {
                    "success": False,
                    "error": "kb_gap",
                    "message": f"Process '{process_id}' not found in KB",
                    "failed_step": step_idx,
                }

            process_dict = process_def.model_dump() if hasattr(process_def, 'model_dump') else process_def

            # Get default output quantity and unit from first output
            outputs = process_dict.get('outputs', [])
            output_quantity = None
            output_unit = None
            if outputs:
                first_output = outputs[0]
                output_quantity = first_output.get('qty', first_output.get('quantity', 1.0))
                output_unit = first_output.get('unit', 'kg')

            # Schedule step process (using base process definition, not resolved)
            # TODO: Apply overrides from step
            result = self.start_process_adr020(
                process_id=process_id,
                scale=1.0,
                start_time=start_time,
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
            else:
                # Failed to schedule step - cancel recipe
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

    def advance_time_adr020(self, duration_hours: float) -> Dict[str, Any]:
        """
        Advance time using ADR-020 event-driven scheduler.

        Processes events chronologically:
        - Process starts (inputs consumed, machines reserved)
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
                # Process started - inputs already consumed by scheduler
                started_processes.append({
                    "process_run_id": event.data.get("process_run_id"),
                    "process_id": event.data.get("process_id"),
                    "time": event.time,
                })

            elif event.event_type == EventType.PROCESS_COMPLETE:
                # Process completed - add outputs
                process_run_id = event.data.get("process_run_id")

                # Process is now in completed_processes (moved by scheduler)
                # Find it in the completed list
                process_run = None
                for proc in self.scheduler.completed_processes:
                    if proc.process_run_id == process_run_id:
                        process_run = proc
                        break

                if process_run:
                    # Add outputs to inventory
                    for item_id, qty in process_run.outputs_pending.items():
                        # Get unit from outputs
                        self.add_to_inventory(item_id, qty, "kg")  # TODO: track units properly

                    # Release machine reservations
                    self.reservation_manager.remove_reservation(process_run_id)

                    completed_processes.append({
                        "process_run_id": process_run_id,
                        "process_id": process_run.process_id,
                        "time": event.time,
                        "outputs": process_run.outputs_pending,
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
                                result = self.start_process_adr020(
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

        return {
            "new_time": target_time,
            "events_processed": len(processed_events),
            "processes_started": len(started_processes),
            "processes_completed": len(completed_processes),
            "completed": completed_processes,
            "started": started_processes,
        }

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
