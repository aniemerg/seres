"""
Recipe Orchestration System (ADR-020)

Manages recipe execution by scheduling steps based on dependencies.
Integrates dependency graphs, machine reservations, and event-driven scheduling.
"""
from __future__ import annotations

from typing import Dict, Set, Optional, Any, List
from dataclasses import dataclass, field
import uuid

from src.simulation.dependency_graph import DependencyGraph
from src.simulation.scheduler import Scheduler, EventType


@dataclass
class RecipeRun:
    """
    Tracks execution state of a recipe instance.

    Lifecycle:
    - Create with dependency graph
    - Schedule ready steps (dependencies satisfied)
    - Mark steps as started/completed
    - Complete recipe when all steps done
    """

    recipe_run_id: str
    recipe_id: str
    target_item_id: str
    recipe_def: Dict[str, Any]
    dependency_graph: DependencyGraph
    started_at: float

    # Step tracking
    completed_steps: Set[int] = field(default_factory=set)
    active_steps: Dict[int, str] = field(default_factory=dict)  # step_idx -> process_run_id
    scheduled_steps: Dict[int, str] = field(default_factory=dict)  # step_idx -> process_run_id

    # State
    is_completed: bool = False
    completed_at: Optional[float] = None

    def mark_step_scheduled(self, step_index: int, process_run_id: str) -> None:
        """Mark step as scheduled."""
        self.scheduled_steps[step_index] = process_run_id

    def mark_step_started(self, step_index: int, process_run_id: str) -> None:
        """Mark step as started (moved from scheduled to active)."""
        if step_index in self.scheduled_steps:
            del self.scheduled_steps[step_index]
        self.active_steps[step_index] = process_run_id

    def mark_step_completed(self, step_index: int) -> None:
        """Mark step as completed."""
        if step_index in self.active_steps:
            del self.active_steps[step_index]
        self.completed_steps.add(step_index)

        # Check if recipe is complete
        total_steps = len(self.dependency_graph)
        if len(self.completed_steps) == total_steps:
            self.is_completed = True

    def get_ready_steps(self) -> List[int]:
        """
        Get steps ready to schedule.

        Returns:
            List of step indices that can be scheduled now
        """
        # Get steps whose dependencies are satisfied
        ready = self.dependency_graph.ready_steps(self.completed_steps)

        # Filter out already scheduled/active steps
        already_running = set(self.scheduled_steps.keys()) | set(self.active_steps.keys())
        return [idx for idx in ready if idx not in already_running]

    def get_step_process_run_id(self, step_index: int) -> Optional[str]:
        """Get process_run_id for a step (scheduled or active)."""
        if step_index in self.active_steps:
            return self.active_steps[step_index]
        if step_index in self.scheduled_steps:
            return self.scheduled_steps[step_index]
        return None

    def __repr__(self) -> str:
        return (
            f"RecipeRun(id={self.recipe_run_id}, "
            f"recipe={self.recipe_id}, "
            f"completed={len(self.completed_steps)}/{len(self.dependency_graph)}, "
            f"active={len(self.active_steps)})"
        )


class RecipeOrchestrator:
    """
    Orchestrates recipe execution.

    Responsibilities:
    - Create and track recipe runs
    - Schedule steps based on dependencies
    - Monitor step completion
    - Trigger dependent steps when ready
    """

    def __init__(self, scheduler: Scheduler):
        """
        Initialize orchestrator.

        Args:
            scheduler: Event-driven scheduler
        """
        self.scheduler = scheduler
        self.recipe_runs: Dict[str, RecipeRun] = {}

        # Register event handlers
        self.scheduler.register_handler(
            EventType.PROCESS_START,
            self._on_process_start
        )
        self.scheduler.register_handler(
            EventType.PROCESS_COMPLETE,
            self._on_process_complete
        )

    def start_recipe(
        self,
        recipe_id: str,
        recipe_dict: Dict[str, Any],
        target_item_id: str,
        start_time: float,
    ) -> str:
        """
        Start a recipe execution.

        Args:
            recipe_id: Recipe definition ID
            recipe_dict: Recipe dict with steps
            target_item_id: Target item being produced
            start_time: When recipe starts

        Returns:
            recipe_run_id for this execution instance
        """
        # Generate runtime ID
        recipe_run_id = str(uuid.uuid4())

        # Build dependency graph
        dependency_graph = DependencyGraph(recipe_dict)

        # Create recipe run
        recipe_run = RecipeRun(
            recipe_run_id=recipe_run_id,
            recipe_id=recipe_id,
            target_item_id=target_item_id,
            recipe_def=recipe_dict,
            dependency_graph=dependency_graph,
            started_at=start_time,
        )

        # Track recipe run
        self.recipe_runs[recipe_run_id] = recipe_run

        return recipe_run_id

    def get_ready_steps(self, recipe_run_id: str) -> List[int]:
        """
        Get steps ready to schedule for a recipe run.

        Args:
            recipe_run_id: Recipe run to query

        Returns:
            List of step indices ready to schedule
        """
        if recipe_run_id not in self.recipe_runs:
            return []

        recipe_run = self.recipe_runs[recipe_run_id]
        return recipe_run.get_ready_steps()

    def schedule_step(
        self,
        recipe_run_id: str,
        step_index: int,
        process_run_id: str,
    ) -> None:
        """
        Mark a step as scheduled.

        Args:
            recipe_run_id: Recipe run
            step_index: Step index
            process_run_id: Process run ID that was scheduled
        """
        if recipe_run_id not in self.recipe_runs:
            raise ValueError(f"Recipe run {recipe_run_id} not found")

        recipe_run = self.recipe_runs[recipe_run_id]
        recipe_run.mark_step_scheduled(step_index, process_run_id)

    def _on_process_start(self, event) -> None:
        """Handle process start event."""
        process_run_id = event.data.get('process_run_id')
        recipe_run_id = event.data.get('recipe_run_id')
        step_index = event.data.get('step_index')

        if not recipe_run_id or step_index is None:
            return  # Not a recipe step

        if recipe_run_id not in self.recipe_runs:
            return

        recipe_run = self.recipe_runs[recipe_run_id]
        recipe_run.mark_step_started(step_index, process_run_id)

    def _on_process_complete(self, event) -> None:
        """Handle process completion event."""
        process_run_id = event.data.get('process_run_id')

        # Find which recipe run this belongs to
        recipe_run_id = None
        step_index = None

        for run_id, recipe_run in self.recipe_runs.items():
            for idx, proc_id in recipe_run.active_steps.items():
                if proc_id == process_run_id:
                    recipe_run_id = run_id
                    step_index = idx
                    break
            if recipe_run_id:
                break

        if not recipe_run_id or step_index is None:
            return  # Not a recipe step

        # Mark step as completed
        recipe_run = self.recipe_runs[recipe_run_id]
        recipe_run.mark_step_completed(step_index)

        # Check if recipe is complete
        if recipe_run.is_completed:
            recipe_run.completed_at = self.scheduler.current_time

    def is_recipe_complete(self, recipe_run_id: str) -> bool:
        """Check if recipe has completed."""
        if recipe_run_id not in self.recipe_runs:
            return False
        return self.recipe_runs[recipe_run_id].is_completed

    def get_recipe_run(self, recipe_run_id: str) -> Optional[RecipeRun]:
        """Get recipe run by ID."""
        return self.recipe_runs.get(recipe_run_id)

    def get_active_recipe_runs(self) -> List[RecipeRun]:
        """Get all active (not completed) recipe runs."""
        return [
            run for run in self.recipe_runs.values()
            if not run.is_completed
        ]

    def get_completed_recipe_runs(self) -> List[RecipeRun]:
        """Get all completed recipe runs."""
        return [
            run for run in self.recipe_runs.values()
            if run.is_completed
        ]

    def cancel_recipe(self, recipe_run_id: str) -> bool:
        """
        Cancel a recipe run.

        Cancels all scheduled and active processes for the recipe.

        Args:
            recipe_run_id: Recipe run to cancel

        Returns:
            True if recipe was found and cancelled
        """
        if recipe_run_id not in self.recipe_runs:
            return False

        recipe_run = self.recipe_runs[recipe_run_id]

        # Cancel all scheduled and active processes
        all_process_ids = (
            list(recipe_run.scheduled_steps.values()) +
            list(recipe_run.active_steps.values())
        )

        for process_run_id in all_process_ids:
            self.scheduler.cancel_process(process_run_id)

        # Remove recipe run
        del self.recipe_runs[recipe_run_id]
        return True

    def get_step_status(
        self,
        recipe_run_id: str,
        step_index: int
    ) -> Optional[str]:
        """
        Get status of a step.

        Returns:
            'pending', 'scheduled', 'active', 'completed', or None if not found
        """
        if recipe_run_id not in self.recipe_runs:
            return None

        recipe_run = self.recipe_runs[recipe_run_id]

        if step_index in recipe_run.completed_steps:
            return 'completed'
        if step_index in recipe_run.active_steps:
            return 'active'
        if step_index in recipe_run.scheduled_steps:
            return 'scheduled'

        # Check if dependencies are satisfied
        if recipe_run.dependency_graph.can_start(step_index, recipe_run.completed_steps):
            return 'ready'

        return 'pending'

    def get_recipe_progress(self, recipe_run_id: str) -> Dict[str, Any]:
        """
        Get progress summary for a recipe run.

        Returns:
            Dict with progress information
        """
        if recipe_run_id not in self.recipe_runs:
            return {}

        recipe_run = self.recipe_runs[recipe_run_id]
        total_steps = len(recipe_run.dependency_graph)

        return {
            'recipe_run_id': recipe_run_id,
            'recipe_id': recipe_run.recipe_id,
            'total_steps': total_steps,
            'completed_steps': len(recipe_run.completed_steps),
            'active_steps': len(recipe_run.active_steps),
            'scheduled_steps': len(recipe_run.scheduled_steps),
            'is_completed': recipe_run.is_completed,
            'started_at': recipe_run.started_at,
            'completed_at': recipe_run.completed_at,
            'progress_percent': (len(recipe_run.completed_steps) / total_steps * 100)
                if total_steps > 0 else 0,
        }

    def __repr__(self) -> str:
        active = len([r for r in self.recipe_runs.values() if not r.is_completed])
        completed = len([r for r in self.recipe_runs.values() if r.is_completed])
        return f"RecipeOrchestrator(active={active}, completed={completed})"
