"""
Unit tests for event-driven scheduler (ADR-020).
"""
import pytest

from src.simulation.scheduler import (
    Scheduler,
    EventQueue,
    SchedulerEvent,
    EventType,
    ProcessRun,
)


class TestEventQueue:
    """Test event queue (priority queue)."""

    def test_chronological_ordering(self):
        """Events should be ordered by time."""
        queue = EventQueue()

        queue.push(SchedulerEvent(time=5.0, event_type=EventType.PROCESS_START, event_id='e3'))
        queue.push(SchedulerEvent(time=1.0, event_type=EventType.PROCESS_START, event_id='e1'))
        queue.push(SchedulerEvent(time=3.0, event_type=EventType.PROCESS_START, event_id='e2'))

        assert queue.pop().event_id == 'e1'
        assert queue.pop().event_id == 'e2'
        assert queue.pop().event_id == 'e3'

    def test_priority_ordering(self):
        """Events at same time should be ordered by priority."""
        queue = EventQueue()

        queue.push(SchedulerEvent(
            time=5.0, priority=20,
            event_type=EventType.PROCESS_START, event_id='low_priority'
        ))
        queue.push(SchedulerEvent(
            time=5.0, priority=10,
            event_type=EventType.PROCESS_START, event_id='high_priority'
        ))

        # Lower number = higher priority
        assert queue.pop().event_id == 'high_priority'
        assert queue.pop().event_id == 'low_priority'

    def test_peek(self):
        """Peek should return next event without removing."""
        queue = EventQueue()

        queue.push(SchedulerEvent(time=1.0, event_type=EventType.PROCESS_START, event_id='e1'))
        queue.push(SchedulerEvent(time=2.0, event_type=EventType.PROCESS_START, event_id='e2'))

        assert queue.peek().event_id == 'e1'
        assert len(queue) == 2  # Not removed

        assert queue.pop().event_id == 'e1'
        assert len(queue) == 1

    def test_remove(self):
        """Remove event by ID."""
        queue = EventQueue()

        queue.push(SchedulerEvent(time=1.0, event_type=EventType.PROCESS_START, event_id='e1'))
        queue.push(SchedulerEvent(time=2.0, event_type=EventType.PROCESS_START, event_id='e2'))
        queue.push(SchedulerEvent(time=3.0, event_type=EventType.PROCESS_START, event_id='e3'))

        removed = queue.remove('e2')
        assert removed
        assert len(queue) == 2

        # Remaining events in order
        assert queue.pop().event_id == 'e1'
        assert queue.pop().event_id == 'e3'

    def test_remove_nonexistent(self):
        """Removing nonexistent event returns False."""
        queue = EventQueue()
        queue.push(SchedulerEvent(time=1.0, event_type=EventType.PROCESS_START, event_id='e1'))

        removed = queue.remove('nonexistent')
        assert not removed

    def test_get_events_before(self):
        """Get events before time without removing."""
        queue = EventQueue()

        queue.push(SchedulerEvent(time=1.0, event_type=EventType.PROCESS_START, event_id='e1'))
        queue.push(SchedulerEvent(time=5.0, event_type=EventType.PROCESS_START, event_id='e2'))
        queue.push(SchedulerEvent(time=10.0, event_type=EventType.PROCESS_START, event_id='e3'))

        before_6 = queue.get_events_before(6.0)
        assert len(before_6) == 2
        assert {e.event_id for e in before_6} == {'e1', 'e2'}
        assert len(queue) == 3  # Not removed

    def test_get_events_for_process(self):
        """Get events for specific process."""
        queue = EventQueue()

        queue.push(SchedulerEvent(
            time=1.0,
            event_type=EventType.PROCESS_START,
            event_id='start_proc1',
            data={'process_run_id': 'proc1'}
        ))
        queue.push(SchedulerEvent(
            time=5.0,
            event_type=EventType.PROCESS_COMPLETE,
            event_id='complete_proc1',
            data={'process_run_id': 'proc1'}
        ))
        queue.push(SchedulerEvent(
            time=2.0,
            event_type=EventType.PROCESS_START,
            event_id='start_proc2',
            data={'process_run_id': 'proc2'}
        ))

        proc1_events = queue.get_events_for_process('proc1')
        assert len(proc1_events) == 2

    def test_clear(self):
        """Clear removes all events."""
        queue = EventQueue()

        queue.push(SchedulerEvent(time=1.0, event_type=EventType.PROCESS_START, event_id='e1'))
        queue.push(SchedulerEvent(time=2.0, event_type=EventType.PROCESS_START, event_id='e2'))

        queue.clear()
        assert len(queue) == 0
        assert queue.pop() is None


class TestSchedulerBasics:
    """Test basic scheduler operations."""

    def test_initialization(self):
        """Scheduler initializes correctly."""
        scheduler = Scheduler()

        assert scheduler.current_time == 0.0
        assert len(scheduler.event_queue) == 0
        assert len(scheduler.active_processes) == 0
        assert len(scheduler.completed_processes) == 0

    def test_schedule_event(self):
        """Schedule a basic event."""
        scheduler = Scheduler()

        event = scheduler.schedule_event(
            time=5.0,
            event_type=EventType.PROCESS_START,
            event_id='test_event',
            data={'key': 'value'},
        )

        assert event.time == 5.0
        assert event.event_type == EventType.PROCESS_START
        assert len(scheduler.event_queue) == 1

    def test_schedule_past_event_fails(self):
        """Cannot schedule event in the past."""
        scheduler = Scheduler()
        scheduler.current_time = 10.0

        with pytest.raises(ValueError, match='in the past'):
            scheduler.schedule_event(
                time=5.0,
                event_type=EventType.PROCESS_START,
                event_id='past_event',
            )

    def test_schedule_process_start(self):
        """Schedule process start and completion."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={'ore': 10.0},
            outputs_pending={'metal': 5.0},
            machines_reserved={'furnace': 1.0},
        )

        # Should schedule both start and complete events
        assert len(scheduler.event_queue) == 2

        events = list(scheduler.event_queue._heap)
        event_types = {e.event_type for e in events}
        assert EventType.PROCESS_START in event_types
        assert EventType.PROCESS_COMPLETE in event_types


class TestProcessLifecycle:
    """Test process lifecycle: scheduled → active → completed."""

    def test_process_becomes_active(self):
        """Process becomes active when started."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        # Advance to start time
        scheduler.advance_to(0.0)

        assert len(scheduler.active_processes) == 1
        assert 'proc_1' in scheduler.active_processes

    def test_process_completes(self):
        """Process completes at end time."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        # Advance to completion
        scheduler.advance_to(5.0)

        assert len(scheduler.active_processes) == 0
        assert len(scheduler.completed_processes) == 1
        assert scheduler.completed_processes[0].process_run_id == 'proc_1'

    def test_multiple_processes(self):
        """Multiple processes can run concurrently."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='process_a',
            start_time=0.0,
            duration_hours=10.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        scheduler.schedule_process_start(
            process_run_id='proc_2',
            process_id='process_b',
            start_time=5.0,
            duration_hours=4.0,  # Changed to complete at t=9
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        # At t=6, both should be active
        scheduler.advance_to(6.0)
        assert len(scheduler.active_processes) == 2

        # At t=9, proc_2 completes, proc_1 still active
        scheduler.advance_to(9.0)
        assert len(scheduler.active_processes) == 1
        assert len(scheduler.completed_processes) == 1

        # At t=10, proc_1 completes
        scheduler.advance_to(10.0)
        assert len(scheduler.active_processes) == 0
        assert len(scheduler.completed_processes) == 2

    def test_cancel_scheduled_process(self):
        """Cancel a scheduled process before it starts."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=10.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        # Cancel before start
        cancelled = scheduler.cancel_process('proc_1')
        assert cancelled

        # Advance past start time - nothing should happen
        scheduler.advance_to(15.0)
        assert len(scheduler.active_processes) == 0
        assert len(scheduler.completed_processes) == 0

    def test_cancel_active_process(self):
        """Cancel an active process."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=0.0,
            duration_hours=10.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        # Start process
        scheduler.advance_to(0.0)
        assert len(scheduler.active_processes) == 1

        # Cancel while active
        cancelled = scheduler.cancel_process('proc_1')
        assert cancelled
        assert len(scheduler.active_processes) == 0


class TestTimeAdvancement:
    """Test time advancement."""

    def test_advance_to(self):
        """Advance to specific time."""
        scheduler = Scheduler()

        scheduler.schedule_event(
            time=5.0,
            event_type=EventType.PROCESS_START,
            event_id='event_1',
        )

        events = scheduler.advance_to(10.0)

        assert scheduler.current_time == 10.0
        assert len(events) == 1
        assert events[0].event_id == 'event_1'

    def test_advance_by(self):
        """Advance by time delta."""
        scheduler = Scheduler()
        scheduler.current_time = 5.0

        scheduler.schedule_event(
            time=10.0,
            event_type=EventType.PROCESS_START,
            event_id='event_1',
        )

        events = scheduler.advance_by(10.0)  # Advance to 15.0

        assert scheduler.current_time == 15.0
        assert len(events) == 1

    def test_advance_backwards_fails(self):
        """Cannot advance backwards in time."""
        scheduler = Scheduler()
        scheduler.current_time = 10.0

        with pytest.raises(ValueError, match='backwards'):
            scheduler.advance_to(5.0)

    def test_advance_stops_at_target(self):
        """Advance stops before events after target."""
        scheduler = Scheduler()

        scheduler.schedule_event(
            time=5.0,
            event_type=EventType.PROCESS_START,
            event_id='event_1',
        )

        scheduler.schedule_event(
            time=15.0,
            event_type=EventType.PROCESS_START,
            event_id='event_2',
        )

        events = scheduler.advance_to(10.0)

        assert len(events) == 1  # Only event_1 processed
        assert events[0].event_id == 'event_1'
        assert len(scheduler.event_queue) == 1  # event_2 still queued


class TestEventHandlers:
    """Test event handler callbacks."""

    def test_register_handler(self):
        """Register and call event handler."""
        scheduler = Scheduler()
        called = []

        def handler(event):
            called.append(event.event_id)

        scheduler.register_handler(EventType.PROCESS_START, handler)

        scheduler.schedule_event(
            time=0.0,
            event_type=EventType.PROCESS_START,
            event_id='event_1',
        )

        scheduler.advance_to(0.0)

        assert 'event_1' in called

    def test_multiple_handlers(self):
        """Multiple handlers can be registered."""
        scheduler = Scheduler()
        calls = {'h1': [], 'h2': []}

        def handler1(event):
            calls['h1'].append(event.event_id)

        def handler2(event):
            calls['h2'].append(event.event_id)

        scheduler.register_handler(EventType.PROCESS_START, handler1)
        scheduler.register_handler(EventType.PROCESS_START, handler2)

        scheduler.schedule_event(
            time=0.0,
            event_type=EventType.PROCESS_START,
            event_id='event_1',
        )

        scheduler.advance_to(0.0)

        assert 'event_1' in calls['h1']
        assert 'event_1' in calls['h2']

    def test_handlers_for_specific_type(self):
        """Handlers only called for matching event type."""
        scheduler = Scheduler()
        start_calls = []
        complete_calls = []

        scheduler.register_handler(
            EventType.PROCESS_START,
            lambda e: start_calls.append(e.event_id)
        )
        scheduler.register_handler(
            EventType.PROCESS_COMPLETE,
            lambda e: complete_calls.append(e.event_id)
        )

        scheduler.schedule_event(
            time=0.0,
            event_type=EventType.PROCESS_START,
            event_id='start_1',
        )

        scheduler.advance_to(0.0)

        assert 'start_1' in start_calls
        assert len(complete_calls) == 0


class TestUtilities:
    """Test utility methods."""

    def test_get_active_process(self):
        """Get active process by ID."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        scheduler.advance_to(0.0)

        proc = scheduler.get_active_process('proc_1')
        assert proc is not None
        assert proc.process_run_id == 'proc_1'

    def test_get_active_processes_for_recipe(self):
        """Get all active processes for a recipe."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_1',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id='recipe_1',
        )

        scheduler.schedule_process_start(
            process_run_id='proc_2',
            process_id='step_2',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id='recipe_1',
        )

        scheduler.advance_to(0.0)

        recipe_procs = scheduler.get_active_processes_for_recipe('recipe_1')
        assert len(recipe_procs) == 2

    def test_get_next_event_time(self):
        """Get time of next scheduled event."""
        scheduler = Scheduler()

        scheduler.schedule_event(
            time=5.0,
            event_type=EventType.PROCESS_START,
            event_id='event_1',
        )

        next_time = scheduler.get_next_event_time()
        assert next_time == 5.0

    def test_get_next_event_time_empty(self):
        """Get next event time when queue is empty."""
        scheduler = Scheduler()

        next_time = scheduler.get_next_event_time()
        assert next_time is None

    def test_reset(self):
        """Reset scheduler to initial state."""
        scheduler = Scheduler()

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='test_process',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
        )

        scheduler.advance_to(10.0)

        scheduler.reset()

        assert scheduler.current_time == 0.0
        assert len(scheduler.event_queue) == 0
        assert len(scheduler.active_processes) == 0
        assert len(scheduler.completed_processes) == 0
