"""
Concurrent DES runner built on existing simulation engine primitives.
"""
from __future__ import annotations

import uuid
from typing import Any, Callable, Dict, List, Optional, Set

from src.simulation_parallel.intent_queue import DeferredIntentQueue, ProcessIntent
from src.simulation_parallel.session import Sim2Session


TERMINAL_DEFER_ERRORS = {"machine_conflict", "insufficient_inputs"}


class ConcurrentDESRunner:
    """Submit intents upfront and drive scheduler to terminal state."""

    def __init__(self, session: Sim2Session):
        self.session = session

    @property
    def engine(self):
        return self.session.engine

    @property
    def queue(self) -> DeferredIntentQueue:
        return self.session.queue

    def submit_process_intent(
        self,
        *,
        process_id: str,
        scale: float = 1.0,
        duration_hours: Optional[float] = None,
        output_quantity: Optional[float] = None,
        output_unit: Optional[str] = None,
    ) -> Dict[str, Any]:
        effective_duration = duration_hours
        if effective_duration is None:
            effective_duration = self._infer_duration_hours(process_id, scale)
        result = self.engine.start_process(
            process_id=process_id,
            scale=scale,
            duration_hours=effective_duration,
            output_quantity=output_quantity,
            output_unit=output_unit,
            start_time=self.engine.scheduler.current_time,
        )
        if result.get("success"):
            return {"status": "accepted", "detail": result}

        error = result.get("error")
        if error not in TERMINAL_DEFER_ERRORS:
            return {"status": "rejected", "detail": result}

        required_machines = self._required_machines_for_process(process_id)
        intent = ProcessIntent(
            intent_id=str(uuid.uuid4()),
            sequence=self.queue.next_sequence(),
            process_id=process_id,
            scale=scale,
            duration_hours=effective_duration,
            output_quantity=output_quantity,
            output_unit=output_unit,
            required_machines=required_machines,
            submitted_at=self.engine.scheduler.current_time,
            last_error=result.get("message"),
        )
        self.queue.add(intent)
        return {
            "status": "deferred",
            "detail": {
                "intent_id": intent.intent_id,
                "reason": result.get("message"),
                "error": error,
            },
        }

    def _infer_duration_hours(self, process_id: str, scale: float) -> Optional[float]:
        model = self.engine.kb.get_process(process_id)
        if not model:
            return None
        proc = model.model_dump() if hasattr(model, "model_dump") else model
        time_model = proc.get("time_model", {}) or {}
        ttype = time_model.get("type")
        if ttype == "batch":
            return float(time_model.get("hr_per_batch", 1.0)) * float(scale)
        if ttype == "linear_rate":
            rate = float(time_model.get("rate", 0.0) or 0.0)
            if rate <= 0:
                return None
            basis = time_model.get("scaling_basis")
            outputs = proc.get("outputs", []) or []
            if basis:
                for outp in outputs:
                    if outp.get("item_id") == basis:
                        qty = float(outp.get("qty", outp.get("quantity", 0.0)) or 0.0)
                        if qty > 0:
                            return (qty * float(scale)) / rate
            if outputs:
                qty = float(outputs[0].get("qty", outputs[0].get("quantity", 0.0)) or 0.0)
                if qty > 0:
                    return (qty * float(scale)) / rate
        return None

    def _required_machines_for_process(self, process_id: str) -> List[str]:
        model = self.engine.kb.get_process(process_id)
        if not model:
            return []
        proc = model.model_dump() if hasattr(model, "model_dump") else model
        out: List[str] = []
        for req in proc.get("resource_requirements", []) or []:
            machine_id = req.get("machine_id")
            if machine_id:
                out.append(machine_id)
        return sorted(set(out))

    def _promote_deferred(self, changed_machines: Optional[Set[str]] = None) -> int:
        promoted = 0
        while True:
            batch_promoted = 0
            for intent in self.queue.candidate_intents(changed_machines):
                result = self.engine.start_process(
                    process_id=intent.process_id,
                    scale=intent.scale,
                    duration_hours=intent.duration_hours,
                    output_quantity=intent.output_quantity,
                    output_unit=intent.output_unit,
                    start_time=self.engine.scheduler.current_time,
                )
                if result.get("success"):
                    self.queue.remove(intent.intent_id)
                    batch_promoted += 1
                    continue

                if result.get("error") in TERMINAL_DEFER_ERRORS:
                    intent.last_error = result.get("message")
                    continue

                intent.last_error = f"rejected: {result.get('message')}"
                self.queue.remove(intent.intent_id)

            promoted += batch_promoted
            if batch_promoted == 0:
                break
            changed_machines = None
        return promoted

    def _machines_from_completed(self, completed: List[Dict[str, Any]]) -> Set[str]:
        changed: Set[str] = set()
        for row in completed:
            process_id = row.get("process_id")
            if not process_id:
                continue
            changed.update(self._required_machines_for_process(process_id))
        return changed

    def run_to_completion(self, max_no_progress: int = 1000) -> Dict[str, Any]:
        return self._run_to_completion(max_no_progress=max_no_progress, progress_callback=None, progress_every_steps=1000)

    def _run_to_completion(
        self,
        *,
        max_no_progress: int,
        progress_callback: Optional[Callable[[Dict[str, Any]], None]],
        progress_every_steps: int,
    ) -> Dict[str, Any]:
        no_progress = 0
        steps = 0
        while True:
            steps += 1
            scheduler = self.engine.scheduler
            had_events = len(scheduler.event_queue) > 0
            before_time = scheduler.current_time

            if had_events:
                next_event = scheduler.event_queue.peek()
                if next_event is None:
                    break
                delta = max(0.0, next_event.time - scheduler.current_time)
                advance_result = self.engine.advance_time(delta)
                changed_machines = self._machines_from_completed(advance_result.get("completed", []))
                promoted = self._promote_deferred(changed_machines if changed_machines else None)
                progress = (
                    advance_result.get("processes_started", 0) > 0
                    or advance_result.get("processes_completed", 0) > 0
                    or promoted > 0
                )
                # Time advancing while processes are active is meaningful forward motion.
                if (
                    not progress
                    and scheduler.current_time > before_time
                    and len(scheduler.active_processes) > 0
                ):
                    progress = True
            else:
                promoted = self._promote_deferred(None)
                progress = promoted > 0
                if not progress:
                    break

            if progress_callback is not None:
                should_emit = steps == 1
                if progress_every_steps > 0 and steps % progress_every_steps == 0:
                    should_emit = True
                if not progress and not should_emit:
                    stalled_steps = no_progress + 1
                    if progress_every_steps <= 0:
                        should_emit = True
                    elif stalled_steps % progress_every_steps == 0:
                        should_emit = True
                if should_emit:
                    progress_callback(
                        {
                            "step": steps,
                            "time": scheduler.current_time,
                            "queued_events": len(scheduler.event_queue),
                            "active_processes": len(scheduler.active_processes),
                            "completed_processes": len(scheduler.completed_processes),
                            "deferred_intents": len(self.queue),
                            "had_events": had_events,
                            "promoted": promoted,
                            "progress": progress,
                        }
                    )

            if progress:
                no_progress = 0
            else:
                no_progress += 1
                if no_progress >= max_no_progress:
                    return {
                        "status": "blocked",
                        "reason": "no_progress_guard",
                        "steps": steps,
                        "summary": self.status(),
                        "blocked_intents": self._blocked_intents(),
                        "blocked_recipes": self._blocked_recipes(),
                    }

        summary = self.status()
        if summary["queued_events"] == 0 and summary["active_processes"] == 0 and summary["deferred_intents"] == 0:
            return {"status": "completed", "steps": steps, "summary": summary}

        return {
            "status": "blocked",
            "reason": "terminal_blocked",
            "steps": steps,
            "summary": summary,
            "blocked_intents": self._blocked_intents(),
            "blocked_recipes": self._blocked_recipes(),
        }

    def run_to_completion_with_progress(
        self,
        *,
        max_no_progress: int = 1000,
        progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
        progress_every_steps: int = 1000,
    ) -> Dict[str, Any]:
        return self._run_to_completion(
            max_no_progress=max_no_progress,
            progress_callback=progress_callback,
            progress_every_steps=progress_every_steps,
        )

    def _blocked_intents(self) -> List[Dict[str, Any]]:
        out = []
        for intent in self.queue.all_intents():
            out.append(
                {
                    "intent_id": intent.intent_id,
                    "process_id": intent.process_id,
                    "sequence": intent.sequence,
                    "last_error": intent.last_error,
                    "required_machines": intent.required_machines,
                }
            )
        return out

    def _blocked_recipes(self) -> List[Dict[str, Any]]:
        """Best-effort diagnosis for active recipe runs that cannot progress."""
        out: List[Dict[str, Any]] = []
        self.engine._update_machine_capacities()
        now = self.engine.scheduler.current_time

        for recipe_run in self.engine.orchestrator.get_active_recipe_runs():
            ready_steps = recipe_run.get_ready_steps()
            entry: Dict[str, Any] = {
                "recipe_run_id": recipe_run.recipe_run_id,
                "recipe_id": recipe_run.recipe_id,
                "ready_steps": ready_steps,
                "active_steps": sorted(recipe_run.active_steps.keys()),
                "scheduled_steps": sorted(recipe_run.scheduled_steps.keys()),
                "issues": [],
            }
            if not ready_steps:
                entry["issues"].append("no_ready_steps")
                out.append(entry)
                continue

            for step_idx in ready_steps:
                sched = self.engine._resolve_recipe_step_schedule(
                    recipe_run.recipe_run_id,
                    recipe_run.recipe_def,
                    step_idx,
                )
                if not sched:
                    entry["issues"].append(f"step_{step_idx}:cannot_resolve")
                    continue
                proc = sched["process_def_override"]
                process_id = sched["process_id"]

                missing_inputs: List[str] = []
                for inp in proc.get("inputs", []) or []:
                    item_id = inp.get("item_id")
                    qty = float(inp.get("quantity", inp.get("qty", 0.0)) or 0.0) * float(sched.get("scale", 1.0))
                    unit = inp.get("unit", "kg")
                    if item_id and not self.engine.has_item(item_id, qty, unit):
                        missing_inputs.append(f"{item_id} need={qty} {unit}")

                machine_conflicts: List[str] = []
                for req in proc.get("resource_requirements", []) or []:
                    machine_id = req.get("machine_id")
                    qty = float(req.get("qty", 1.0) or 1.0)
                    unit = req.get("unit", "count")
                    if not machine_id:
                        continue
                    if self.engine.reservation_manager is None:
                        machine_conflicts.append(f"{machine_id} unavailable(no_reservation_manager)")
                        continue
                    try:
                        avail = self.engine.reservation_manager.get_availability_at(machine_id, now).available
                    except Exception:
                        avail = 0.0
                    needed = qty if unit in {"count", "unit"} else 1.0
                    if avail < needed:
                        machine_conflicts.append(f"{machine_id} need={needed} avail={avail}")

                if missing_inputs:
                    entry["issues"].append(f"step_{step_idx}:{process_id}:missing_inputs:{'; '.join(missing_inputs)}")
                if machine_conflicts:
                    entry["issues"].append(f"step_{step_idx}:{process_id}:machine_conflict:{'; '.join(machine_conflicts)}")
                if not missing_inputs and not machine_conflicts:
                    entry["issues"].append(f"step_{step_idx}:{process_id}:unknown_blocker")
            out.append(entry)
        return out

    def status(self) -> Dict[str, Any]:
        scheduler = self.engine.scheduler
        return {
            "current_time": scheduler.current_time,
            "queued_events": len(scheduler.event_queue),
            "active_processes": len(scheduler.active_processes),
            "completed_processes": len(scheduler.completed_processes),
            "deferred_intents": len(self.queue),
            "next_event_time": scheduler.get_next_event_time(),
        }
