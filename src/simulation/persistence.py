"""
Snapshot persistence for simulation state.

Canonical, snapshot-only storage for engine + scheduler + orchestrator state.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from src.simulation.models import SimulationState
from src.simulation.scheduler import Scheduler, SchedulerEvent, EventType, ProcessRun
from src.simulation.recipe_orchestrator import RecipeOrchestrator, RecipeRun
from src.simulation.dependency_graph import DependencyGraph
from src.simulation.machine_reservations import (
    MachineReservationManager,
    Reservation,
    ReservationType,
)


class SchedulerEventSnapshot(BaseModel):
    time: float
    event_type: str
    event_id: str
    priority: int = 0
    data: Dict[str, Any] = Field(default_factory=dict)


class ProcessRunSnapshot(BaseModel):
    process_run_id: str
    process_id: str
    start_time: float
    duration_hours: float
    end_time: float
    scale: float
    inputs_consumed: Dict[str, float]
    outputs_pending: Dict[str, float]
    outputs_pending_units: Dict[str, str] = Field(default_factory=dict)
    machines_reserved: Dict[str, float]
    recipe_run_id: Optional[str] = None
    step_index: Optional[int] = None
    energy_kwh: Optional[float] = None


class SchedulerSnapshot(BaseModel):
    current_time: float
    event_queue: List[SchedulerEventSnapshot] = Field(default_factory=list)
    active_processes: Dict[str, ProcessRunSnapshot] = Field(default_factory=dict)
    completed_processes: List[ProcessRunSnapshot] = Field(default_factory=list)
    total_events_processed: int = 0


class RecipeRunSnapshot(BaseModel):
    recipe_run_id: str
    recipe_id: str
    target_item_id: str
    recipe_def: Dict[str, Any]
    started_at: float
    completed_steps: List[int] = Field(default_factory=list)
    active_steps: Dict[int, str] = Field(default_factory=dict)
    scheduled_steps: Dict[int, str] = Field(default_factory=dict)
    is_completed: bool = False
    completed_at: Optional[float] = None


class OrchestratorSnapshot(BaseModel):
    recipe_runs: Dict[str, RecipeRunSnapshot] = Field(default_factory=dict)


class ReservationSnapshot(BaseModel):
    machine_id: str
    process_run_id: str
    reservation_type: str
    start_time: float
    end_time: float
    qty_reserved: float
    hr_reserved: Optional[float] = None


class ReservationManagerSnapshot(BaseModel):
    machine_capacities: Dict[str, float] = Field(default_factory=dict)
    reservations: List[ReservationSnapshot] = Field(default_factory=list)
    current_time: float = 0.0


class SimulationSnapshot(BaseModel):
    sim_id: str
    state: SimulationState
    scheduler: SchedulerSnapshot
    orchestrator: OrchestratorSnapshot
    reservation_manager: ReservationManagerSnapshot


def _process_run_to_snapshot(proc: ProcessRun) -> ProcessRunSnapshot:
    return ProcessRunSnapshot(
        process_run_id=proc.process_run_id,
        process_id=proc.process_id,
        start_time=proc.start_time,
        duration_hours=proc.duration_hours,
        end_time=proc.end_time,
        scale=proc.scale,
        inputs_consumed=dict(proc.inputs_consumed),
        outputs_pending=dict(proc.outputs_pending),
        outputs_pending_units=dict(proc.outputs_pending_units),
        machines_reserved=dict(proc.machines_reserved),
        recipe_run_id=proc.recipe_run_id,
        step_index=proc.step_index,
        energy_kwh=proc.energy_kwh,
    )


def _snapshot_to_process_run(snapshot: ProcessRunSnapshot) -> ProcessRun:
    return ProcessRun(
        process_run_id=snapshot.process_run_id,
        process_id=snapshot.process_id,
        start_time=snapshot.start_time,
        duration_hours=snapshot.duration_hours,
        end_time=snapshot.end_time,
        scale=snapshot.scale,
        inputs_consumed=dict(snapshot.inputs_consumed),
        outputs_pending=dict(snapshot.outputs_pending),
        outputs_pending_units=dict(snapshot.outputs_pending_units),
        machines_reserved=dict(snapshot.machines_reserved),
        recipe_run_id=snapshot.recipe_run_id,
        step_index=snapshot.step_index,
        energy_kwh=snapshot.energy_kwh,
    )


def build_snapshot(engine) -> SimulationSnapshot:
    scheduler = engine.scheduler
    event_snapshots = [
        SchedulerEventSnapshot(
            time=event.time,
            event_type=event.event_type.value,
            event_id=event.event_id,
            priority=event.priority,
            data=dict(event.data),
        )
        for event in scheduler.event_queue.to_list()
    ]
    active = {
        proc_id: _process_run_to_snapshot(proc)
        for proc_id, proc in scheduler.active_processes.items()
    }
    completed = [
        _process_run_to_snapshot(proc)
        for proc in scheduler.completed_processes
    ]
    scheduler_snapshot = SchedulerSnapshot(
        current_time=scheduler.current_time,
        event_queue=event_snapshots,
        active_processes=active,
        completed_processes=completed,
        total_events_processed=scheduler.total_events_processed,
    )

    recipe_runs: Dict[str, RecipeRunSnapshot] = {}
    for run_id, run in engine.orchestrator.recipe_runs.items():
        recipe_def = run.recipe_def or {}
        recipe_runs[run_id] = RecipeRunSnapshot(
            recipe_run_id=run.recipe_run_id,
            recipe_id=run.recipe_id,
            target_item_id=run.target_item_id,
            recipe_def=recipe_def,
            started_at=run.started_at,
            completed_steps=sorted(run.completed_steps),
            active_steps=dict(run.active_steps),
            scheduled_steps=dict(run.scheduled_steps),
            is_completed=run.is_completed,
            completed_at=run.completed_at,
        )
    orchestrator_snapshot = OrchestratorSnapshot(recipe_runs=recipe_runs)

    reservations = []
    if engine.reservation_manager is not None:
        for res in engine.reservation_manager.reservations:
            reservations.append(
                ReservationSnapshot(
                    machine_id=res.machine_id,
                    process_run_id=res.process_run_id,
                    reservation_type=res.reservation_type.value,
                    start_time=res.start_time,
                    end_time=res.end_time,
                    qty_reserved=res.qty_reserved,
                    hr_reserved=res.hr_reserved,
                )
            )
        reservation_snapshot = ReservationManagerSnapshot(
            machine_capacities=dict(engine.reservation_manager.machine_capacities),
            reservations=reservations,
            current_time=engine.reservation_manager.current_time,
        )
    else:
        reservation_snapshot = ReservationManagerSnapshot()

    return SimulationSnapshot(
        sim_id=engine.sim_id,
        state=engine.state,
        scheduler=scheduler_snapshot,
        orchestrator=orchestrator_snapshot,
        reservation_manager=reservation_snapshot,
    )


def restore_scheduler(snapshot: SchedulerSnapshot) -> Scheduler:
    scheduler = Scheduler()
    scheduler.current_time = snapshot.current_time
    scheduler.total_events_processed = snapshot.total_events_processed
    events: List[SchedulerEvent] = []
    for event in snapshot.event_queue:
        events.append(
            SchedulerEvent(
                time=event.time,
                event_type=EventType(event.event_type),
                event_id=event.event_id,
                priority=event.priority,
                data=dict(event.data),
            )
        )
    scheduler.event_queue.load_from_list(events)
    scheduler.active_processes = {
        proc_id: _snapshot_to_process_run(proc)
        for proc_id, proc in snapshot.active_processes.items()
    }
    scheduler.completed_processes = [
        _snapshot_to_process_run(proc)
        for proc in snapshot.completed_processes
    ]
    return scheduler


def restore_orchestrator(
    snapshot: OrchestratorSnapshot,
    scheduler: Scheduler,
) -> RecipeOrchestrator:
    orchestrator = RecipeOrchestrator(scheduler)
    for run_id, run in snapshot.recipe_runs.items():
        dependency_graph = DependencyGraph(run.recipe_def or {"steps": []})
        recipe_run = RecipeRun(
            recipe_run_id=run.recipe_run_id,
            recipe_id=run.recipe_id,
            target_item_id=run.target_item_id,
            recipe_def=run.recipe_def or {},
            dependency_graph=dependency_graph,
            started_at=run.started_at,
            completed_steps=set(run.completed_steps),
            active_steps=dict(run.active_steps),
            scheduled_steps=dict(run.scheduled_steps),
            is_completed=run.is_completed,
            completed_at=run.completed_at,
        )
        orchestrator.recipe_runs[run_id] = recipe_run
    return orchestrator


def restore_reservation_manager(
    snapshot: ReservationManagerSnapshot,
) -> MachineReservationManager:
    manager = MachineReservationManager(snapshot.machine_capacities)
    manager.current_time = snapshot.current_time
    for res in snapshot.reservations:
        reservation = Reservation(
            machine_id=res.machine_id,
            process_run_id=res.process_run_id,
            reservation_type=ReservationType(res.reservation_type),
            start_time=res.start_time,
            end_time=res.end_time,
            qty_reserved=res.qty_reserved,
            hr_reserved=res.hr_reserved,
        )
        manager.reservations.append(reservation)
    return manager
