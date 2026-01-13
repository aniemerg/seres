"""
Unit tests for recipe orchestration system (ADR-020).
"""
import pytest

from src.simulation.recipe_orchestrator import RecipeOrchestrator, RecipeRun
from src.simulation.scheduler import Scheduler
from src.simulation.dependency_graph import DependencyGraph


class TestRecipeRun:
    """Test RecipeRun dataclass."""

    def test_initialization(self):
        """Recipe run initializes correctly."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        assert run.recipe_run_id == 'run_1'
        assert len(run.completed_steps) == 0
        assert not run.is_completed

    def test_get_ready_steps_initial(self):
        """Initially, steps with no dependencies are ready."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        ready = run.get_ready_steps()
        assert ready == [0]  # Only step 0 has no dependencies

    def test_mark_step_scheduled(self):
        """Mark step as scheduled."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        run.mark_step_scheduled(0, 'proc_1')

        assert 0 in run.scheduled_steps
        assert run.scheduled_steps[0] == 'proc_1'

        # Scheduled steps are not ready anymore
        ready = run.get_ready_steps()
        assert 0 not in ready

    def test_mark_step_started(self):
        """Mark step as started (moves from scheduled to active)."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        run.mark_step_scheduled(0, 'proc_1')
        run.mark_step_started(0, 'proc_1')

        assert 0 not in run.scheduled_steps
        assert 0 in run.active_steps
        assert run.active_steps[0] == 'proc_1'

    def test_mark_step_completed(self):
        """Mark step as completed."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        run.mark_step_scheduled(0, 'proc_1')
        run.mark_step_started(0, 'proc_1')
        run.mark_step_completed(0)

        assert 0 not in run.active_steps
        assert 0 in run.completed_steps

    def test_recipe_completes_when_all_steps_done(self):
        """Recipe marks as completed when all steps are done."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        run.mark_step_completed(0)
        assert not run.is_completed

        run.mark_step_completed(1)
        assert run.is_completed

    def test_get_ready_steps_after_completion(self):
        """Dependent steps become ready after dependencies complete."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)
        run = RecipeRun(
            recipe_run_id='run_1',
            recipe_id='test_recipe',
            target_item_id='metal',
            recipe_def=recipe,
            dependency_graph=graph,
            started_at=0.0,
        )

        # Initially only step 0 ready
        assert run.get_ready_steps() == [0]

        # After step 0 completes, steps 1 and 2 ready
        run.mark_step_completed(0)
        ready = run.get_ready_steps()
        assert set(ready) == {1, 2}


class TestRecipeOrchestrator:
    """Test RecipeOrchestrator."""

    def test_initialization(self):
        """Orchestrator initializes with scheduler."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        assert orchestrator.scheduler is scheduler
        assert len(orchestrator.recipe_runs) == 0

    def test_start_recipe(self):
        """Start a recipe execution."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        assert recipe_run_id is not None
        assert recipe_run_id in orchestrator.recipe_runs

    def test_get_ready_steps(self):
        """Get ready steps for a recipe run."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        ready = orchestrator.get_ready_steps(recipe_run_id)
        assert ready == [0]

    def test_schedule_step(self):
        """Schedule a step."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')

        recipe_run = orchestrator.recipe_runs[recipe_run_id]
        assert 0 in recipe_run.scheduled_steps

    def test_process_start_event_marks_active(self):
        """Process start event marks step as active."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')

        # Schedule process start
        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_0',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=recipe_run_id,
            step_index=0,
        )

        # Advance to start time
        scheduler.advance_to(0.0)

        recipe_run = orchestrator.recipe_runs[recipe_run_id]
        assert 0 in recipe_run.active_steps

    def test_process_complete_event_marks_completed(self):
        """Process completion event marks step as completed."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')

        # Schedule process
        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_0',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=recipe_run_id,
            step_index=0,
        )

        # Advance to completion
        scheduler.advance_to(5.0)

        recipe_run = orchestrator.recipe_runs[recipe_run_id]
        assert 0 in recipe_run.completed_steps

    def test_recipe_completes_automatically(self):
        """Recipe marks as completed when last step finishes."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_0',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=recipe_run_id,
            step_index=0,
        )

        scheduler.advance_to(5.0)

        assert orchestrator.is_recipe_complete(recipe_run_id)

    def test_multi_step_recipe(self):
        """Multi-step recipe with dependencies."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        # Initially only step 0 ready
        ready = orchestrator.get_ready_steps(recipe_run_id)
        assert ready == [0]

        # Schedule and run step 0
        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')
        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_0',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=recipe_run_id,
            step_index=0,
        )

        scheduler.advance_to(5.0)

        # Now step 1 should be ready
        ready = orchestrator.get_ready_steps(recipe_run_id)
        assert ready == [1]

        # Schedule and run step 1
        orchestrator.schedule_step(recipe_run_id, 1, 'proc_2')
        scheduler.schedule_process_start(
            process_run_id='proc_2',
            process_id='step_1',
            start_time=5.0,
            duration_hours=3.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=recipe_run_id,
            step_index=1,
        )

        scheduler.advance_to(8.0)

        # Recipe should be complete
        assert orchestrator.is_recipe_complete(recipe_run_id)

    def test_cancel_recipe(self):
        """Cancel a recipe run."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')

        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_0',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=recipe_run_id,
            step_index=0,
        )

        # Cancel before process starts
        cancelled = orchestrator.cancel_recipe(recipe_run_id)
        assert cancelled
        assert recipe_run_id not in orchestrator.recipe_runs

    def test_get_step_status(self):
        """Get status of recipe steps."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        # Step 0 is ready, step 1 is pending
        assert orchestrator.get_step_status(recipe_run_id, 0) == 'ready'
        assert orchestrator.get_step_status(recipe_run_id, 1) == 'pending'

        # Schedule step 0
        orchestrator.schedule_step(recipe_run_id, 0, 'proc_1')
        assert orchestrator.get_step_status(recipe_run_id, 0) == 'scheduled'

    def test_get_recipe_progress(self):
        """Get recipe progress summary."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        recipe_run_id = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        progress = orchestrator.get_recipe_progress(recipe_run_id)

        assert progress['recipe_id'] == 'test_recipe'
        assert progress['total_steps'] == 2
        assert progress['completed_steps'] == 0
        assert progress['progress_percent'] == 0.0

    def test_get_active_and_completed_recipes(self):
        """Get active and completed recipe runs."""
        scheduler = Scheduler()
        orchestrator = RecipeOrchestrator(scheduler)

        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        # Start first recipe
        run_id_1 = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        # Start second recipe
        run_id_2 = orchestrator.start_recipe(
            recipe_id='test_recipe',
            recipe_dict=recipe,
            target_item_id='metal',
            start_time=0.0,
        )

        # Both should be active
        active = orchestrator.get_active_recipe_runs()
        assert len(active) == 2

        # Complete first recipe
        orchestrator.schedule_step(run_id_1, 0, 'proc_1')
        scheduler.schedule_process_start(
            process_run_id='proc_1',
            process_id='step_0',
            start_time=0.0,
            duration_hours=5.0,
            scale=1.0,
            inputs_consumed={},
            outputs_pending={},
            machines_reserved={},
            recipe_run_id=run_id_1,
            step_index=0,
        )
        scheduler.advance_to(5.0)

        # One active, one completed
        active = orchestrator.get_active_recipe_runs()
        completed = orchestrator.get_completed_recipe_runs()
        assert len(active) == 1
        assert len(completed) == 1
