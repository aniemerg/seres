"""
Event-Driven Scheduler (ADR-020)

Chronological event processing for simulation engine.
Manages process lifecycle: scheduled → active → completed
"""
from __future__ import annotations

from typing import List, Dict, Set, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
import heapq


class EventType(Enum):
    """Types of scheduler events."""

    PROCESS_START = "process_start"  # Process begins execution
    PROCESS_COMPLETE = "process_complete"  # Process finishes
    MACHINE_RELEASE = "machine_release"  # Partial reservation releases
    RECIPE_STEP_READY = "recipe_step_ready"  # Recipe step ready to schedule


@dataclass(order=True)
class SchedulerEvent:
    """
    Event in the simulation timeline.

    Uses dataclass ordering: sorted by time, then priority, then event_id.
    """

    time: float  # Event time (hours)
    event_type: EventType = field(compare=False)
    event_id: str = field(compare=False)
    priority: int = field(default=0)  # Lower number = higher priority
    data: Dict[str, Any] = field(default_factory=dict, compare=False)

    def __repr__(self) -> str:
        return (
            f"SchedulerEvent(time={self.time:.2f}h, "
            f"type={self.event_type.value}, "
            f"id={self.event_id})"
        )


class EventQueue:
    """
    Priority queue for chronological event processing.

    Events are processed in order of:
    1. Time (earliest first)
    2. Priority (lower number = higher priority)
    3. Event ID (for stable ordering)
    """

    def __init__(self):
        """Initialize empty event queue."""
        self._heap: List[SchedulerEvent] = []
        self._event_counter = 0

    def push(self, event: SchedulerEvent) -> None:
        """Add event to queue."""
        heapq.heappush(self._heap, event)

    def pop(self) -> Optional[SchedulerEvent]:
        """Remove and return next event."""
        if self._heap:
            return heapq.heappop(self._heap)
        return None

    def peek(self) -> Optional[SchedulerEvent]:
        """View next event without removing."""
        if self._heap:
            return self._heap[0]
        return None

    def remove(self, event_id: str) -> bool:
        """
        Remove event by ID.

        Returns:
            True if event was found and removed
        """
        for i, event in enumerate(self._heap):
            if event.event_id == event_id:
                self._heap.pop(i)
                heapq.heapify(self._heap)
                return True
        return False

    def get_events_before(self, time: float) -> List[SchedulerEvent]:
        """Get all events scheduled before given time (without removing)."""
        return [e for e in self._heap if e.time < time]

    def get_events_for_process(self, process_run_id: str) -> List[SchedulerEvent]:
        """Get all events for a process run."""
        return [
            e for e in self._heap
            if e.data.get('process_run_id') == process_run_id
        ]

    def __len__(self) -> int:
        """Return number of events in queue."""
        return len(self._heap)

    def __bool__(self) -> bool:
        """Return True if queue has events."""
        return len(self._heap) > 0

    def clear(self) -> None:
        """Remove all events."""
        self._heap.clear()


@dataclass
class ProcessRun:
    """Represents a running process instance."""

    process_run_id: str
    process_id: str
    start_time: float
    duration_hours: float
    end_time: float
    scale: float
    inputs_consumed: Dict[str, float]
    outputs_pending: Dict[str, float]
    machines_reserved: Dict[str, float]
    recipe_run_id: Optional[str] = None
    step_index: Optional[int] = None
    energy_kwh: Optional[float] = None

    def __repr__(self) -> str:
        return (
            f"ProcessRun(id={self.process_run_id}, "
            f"process={self.process_id}, "
            f"time={self.start_time:.2f}-{self.end_time:.2f}h)"
        )


class Scheduler:
    """
    Event-driven scheduler for simulation engine.

    Manages:
    - Event queue (chronological processing)
    - Active processes (currently running)
    - Completed processes (finished)
    - Event handlers (callbacks)
    """

    def __init__(self):
        """Initialize scheduler."""
        self.current_time: float = 0.0
        self.event_queue = EventQueue()
        self.active_processes: Dict[str, ProcessRun] = {}
        self.completed_processes: List[ProcessRun] = []

        # Event handlers
        self._handlers: Dict[EventType, List[Callable]] = {
            EventType.PROCESS_START: [],
            EventType.PROCESS_COMPLETE: [],
            EventType.MACHINE_RELEASE: [],
            EventType.RECIPE_STEP_READY: [],
        }

        # Statistics
        self.total_events_processed = 0

    def register_handler(
        self,
        event_type: EventType,
        handler: Callable[[SchedulerEvent], None]
    ) -> None:
        """
        Register event handler callback.

        Args:
            event_type: Type of event to handle
            handler: Callback function(event) -> None
        """
        self._handlers[event_type].append(handler)

    def schedule_event(
        self,
        time: float,
        event_type: EventType,
        event_id: str,
        data: Optional[Dict[str, Any]] = None,
        priority: int = 0,
    ) -> SchedulerEvent:
        """
        Schedule an event.

        Args:
            time: Event time (hours)
            event_type: Type of event
            event_id: Unique event identifier
            data: Event data dict
            priority: Event priority (lower = earlier)

        Returns:
            The scheduled event
        """
        if time < self.current_time:
            raise ValueError(
                f"Cannot schedule event in the past: "
                f"time={time}, current={self.current_time}"
            )

        event = SchedulerEvent(
            time=time,
            priority=priority,
            event_type=event_type,
            event_id=event_id,
            data=data or {},
        )

        self.event_queue.push(event)
        return event

    def schedule_process_start(
        self,
        process_run_id: str,
        process_id: str,
        start_time: float,
        duration_hours: float,
        scale: float,
        inputs_consumed: Dict[str, float],
        outputs_pending: Dict[str, float],
        machines_reserved: Dict[str, float],
        recipe_run_id: Optional[str] = None,
        step_index: Optional[int] = None,
        energy_kwh: Optional[float] = None,
    ) -> SchedulerEvent:
        """
        Schedule a process to start.

        Args:
            process_run_id: Unique run instance ID
            process_id: Process definition ID
            start_time: When to start (hours)
            duration_hours: How long to run
            scale: Process scale factor
            inputs_consumed: Input items consumed
            outputs_pending: Output items to produce
            machines_reserved: Machines reserved
            recipe_run_id: Parent recipe run ID (if part of recipe)
            step_index: Step index in recipe (if applicable)

        Returns:
            The scheduled start event
        """
        # Schedule start event
        start_event = self.schedule_event(
            time=start_time,
            event_type=EventType.PROCESS_START,
            event_id=f"start_{process_run_id}",
            priority=10,  # Starts have lower priority than completions
            data={
                'process_run_id': process_run_id,
                'process_id': process_id,
                'duration_hours': duration_hours,
                'scale': scale,
                'inputs_consumed': inputs_consumed,
                'outputs_pending': outputs_pending,
                'machines_reserved': machines_reserved,
                'recipe_run_id': recipe_run_id,
                'step_index': step_index,
                'energy_kwh': energy_kwh,
            }
        )

        # Schedule completion event
        end_time = start_time + duration_hours
        self.schedule_event(
            time=end_time,
            event_type=EventType.PROCESS_COMPLETE,
            event_id=f"complete_{process_run_id}",
            priority=5,  # Completions have higher priority
            data={
                'process_run_id': process_run_id,
            }
        )

        return start_event

    def schedule_machine_release(
        self,
        process_run_id: str,
        machine_id: str,
        release_time: float,
        qty: float,
    ) -> SchedulerEvent:
        """
        Schedule a machine release event for partial reservations.

        Args:
            process_run_id: Process instance ID
            machine_id: Machine to release
            release_time: When to release (hours)
            qty: Quantity being released

        Returns:
            The scheduled event
        """
        return self.schedule_event(
            time=release_time,
            event_type=EventType.MACHINE_RELEASE,
            event_id=f"release_{process_run_id}_{machine_id}",
            priority=6,  # Higher priority than completion
            data={
                'process_run_id': process_run_id,
                'machine_id': machine_id,
                'qty': qty,
            }
        )

    def cancel_process(self, process_run_id: str) -> bool:
        """
        Cancel a scheduled or active process.

        Args:
            process_run_id: Process instance to cancel

        Returns:
            True if process was found and cancelled
        """
        # Remove from active processes
        if process_run_id in self.active_processes:
            del self.active_processes[process_run_id]

        # Remove scheduled events
        removed_start = self.event_queue.remove(f"start_{process_run_id}")
        removed_complete = self.event_queue.remove(f"complete_{process_run_id}")

        return removed_start or removed_complete

    def advance_to(self, target_time: float) -> List[SchedulerEvent]:
        """
        Advance simulation to target time, processing all events.

        Args:
            target_time: Time to advance to (hours)

        Returns:
            List of events that were processed
        """
        if target_time < self.current_time:
            raise ValueError(
                f"Cannot go backwards in time: "
                f"target={target_time}, current={self.current_time}"
            )

        processed_events = []

        while self.event_queue:
            event = self.event_queue.peek()

            if event.time > target_time:
                break  # Stop before target

            # Process event
            event = self.event_queue.pop()
            self._process_event(event)
            processed_events.append(event)
            self.total_events_processed += 1

        # Update current time
        self.current_time = target_time

        return processed_events

    def advance_by(self, hours: float) -> List[SchedulerEvent]:
        """
        Advance simulation by hours.

        Args:
            hours: Time delta (hours)

        Returns:
            List of events that were processed
        """
        return self.advance_to(self.current_time + hours)

    def _process_event(self, event: SchedulerEvent) -> None:
        """
        Process a single event.

        Args:
            event: Event to process
        """
        self.current_time = event.time

        # Handle event type
        if event.event_type == EventType.PROCESS_START:
            self._handle_process_start(event)
        elif event.event_type == EventType.PROCESS_COMPLETE:
            self._handle_process_complete(event)
        elif event.event_type == EventType.MACHINE_RELEASE:
            self._handle_machine_release(event)
        elif event.event_type == EventType.RECIPE_STEP_READY:
            self._handle_recipe_step_ready(event)

        # Call registered handlers
        for handler in self._handlers[event.event_type]:
            handler(event)

    def _handle_process_start(self, event: SchedulerEvent) -> None:
        """Handle process start event."""
        data = event.data

        # Generic events may not have full process data
        if 'process_run_id' not in data:
            return

        process_run_id = data['process_run_id']

        # Create ProcessRun
        process_run = ProcessRun(
            process_run_id=process_run_id,
            process_id=data['process_id'],
            start_time=event.time,
            duration_hours=data['duration_hours'],
            end_time=event.time + data['duration_hours'],
            scale=data['scale'],
            inputs_consumed=data['inputs_consumed'],
            outputs_pending=data['outputs_pending'],
            machines_reserved=data['machines_reserved'],
            recipe_run_id=data.get('recipe_run_id'),
            step_index=data.get('step_index'),
            energy_kwh=data.get('energy_kwh'),
        )

        # Add to active processes
        self.active_processes[process_run_id] = process_run

    def _handle_process_complete(self, event: SchedulerEvent) -> None:
        """Handle process completion event."""
        process_run_id = event.data['process_run_id']

        # Move from active to completed
        if process_run_id in self.active_processes:
            process_run = self.active_processes.pop(process_run_id)
            self.completed_processes.append(process_run)

    def _handle_machine_release(self, event: SchedulerEvent) -> None:
        """Handle machine release event (for partial reservations)."""
        # Machine release is handled by reservation manager
        # This is a notification event for logging
        pass

    def _handle_recipe_step_ready(self, event: SchedulerEvent) -> None:
        """Handle recipe step ready event."""
        # Recipe step ready is handled by orchestrator
        # This is a notification event for dependency resolution
        pass

    def get_active_process(self, process_run_id: str) -> Optional[ProcessRun]:
        """Get active process by ID."""
        return self.active_processes.get(process_run_id)

    def get_active_processes_for_recipe(self, recipe_run_id: str) -> List[ProcessRun]:
        """Get all active processes for a recipe run."""
        return [
            p for p in self.active_processes.values()
            if p.recipe_run_id == recipe_run_id
        ]

    def get_next_event_time(self) -> Optional[float]:
        """Get time of next scheduled event."""
        event = self.event_queue.peek()
        return event.time if event else None

    def reset(self) -> None:
        """Reset scheduler to initial state."""
        self.current_time = 0.0
        self.event_queue.clear()
        self.active_processes.clear()
        self.completed_processes.clear()
        self.total_events_processed = 0

    def __repr__(self) -> str:
        return (
            f"Scheduler(time={self.current_time:.2f}h, "
            f"queued={len(self.event_queue)}, "
            f"active={len(self.active_processes)}, "
            f"completed={len(self.completed_processes)})"
        )
