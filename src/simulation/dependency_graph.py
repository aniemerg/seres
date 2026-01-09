"""
Dependency Graph Builder for Recipe Orchestration (ADR-020)

Builds directed acyclic graphs (DAGs) from recipe step dependencies
and provides topological ordering for execution scheduling.
"""
from __future__ import annotations

from typing import List, Dict, Set, Tuple, Any, Optional
from dataclasses import dataclass


@dataclass
class StepNode:
    """Represents a recipe step in the dependency graph."""

    step_index: int
    process_id: str
    dependencies: List[int]
    depth: int = 0  # Level in the DAG (for parallel scheduling)

    def __repr__(self) -> str:
        return f"StepNode(idx={self.step_index}, proc={self.process_id}, deps={self.dependencies})"


class DependencyGraph:
    """
    Builds and analyzes dependency graphs for recipe steps.

    Provides:
    - Topological ordering for sequential execution
    - Parallel execution waves (steps at same depth can run concurrently)
    - Cycle detection
    - Critical path analysis
    """

    def __init__(self, recipe: Dict[str, Any]):
        """
        Build dependency graph from recipe definition.

        Args:
            recipe: Recipe dict with 'steps' list

        Raises:
            ValueError: If recipe has circular dependencies or invalid references
        """
        self.recipe_id = recipe.get('id', 'unknown')
        self.steps = recipe.get('steps', [])
        self.nodes: List[StepNode] = []

        # Build nodes
        for idx, step in enumerate(self.steps):
            node = StepNode(
                step_index=idx,
                process_id=step.get('process_id', f'step_{idx}'),
                dependencies=step.get('dependencies', [])
            )
            self.nodes.append(node)

        # Validate and compute depths
        self._validate()
        self._compute_depths()

    def _validate(self) -> None:
        """
        Validate dependency graph.

        Checks:
        - All dependency indices are valid
        - No circular dependencies

        Raises:
            ValueError: If validation fails
        """
        n_steps = len(self.nodes)

        # Check dependency indices
        for node in self.nodes:
            for dep_idx in node.dependencies:
                if dep_idx < 0 or dep_idx >= n_steps:
                    raise ValueError(
                        f"Recipe '{self.recipe_id}' step {node.step_index} references "
                        f"invalid dependency index {dep_idx} (only {n_steps} steps)"
                    )

        # Check for cycles using DFS
        visited: Set[int] = set()
        rec_stack: Set[int] = set()

        def has_cycle(node_idx: int) -> bool:
            visited.add(node_idx)
            rec_stack.add(node_idx)

            for dep_idx in self.nodes[node_idx].dependencies:
                if dep_idx not in visited:
                    if has_cycle(dep_idx):
                        return True
                elif dep_idx in rec_stack:
                    return True

            rec_stack.remove(node_idx)
            return False

        for idx in range(len(self.nodes)):
            if idx not in visited:
                if has_cycle(idx):
                    raise ValueError(
                        f"Recipe '{self.recipe_id}' has circular dependencies"
                    )

    def _compute_depths(self) -> None:
        """
        Compute depth of each node in the DAG.

        Depth = maximum depth of dependencies + 1
        Depth 0 = no dependencies (can start immediately)
        """
        # Memoization for computed depths
        depths: Dict[int, int] = {}

        def compute_depth(node_idx: int) -> int:
            if node_idx in depths:
                return depths[node_idx]

            node = self.nodes[node_idx]

            if not node.dependencies:
                depths[node_idx] = 0
                return 0

            # Depth = max(dependency depths) + 1
            max_dep_depth = max(
                compute_depth(dep_idx)
                for dep_idx in node.dependencies
            )

            depths[node_idx] = max_dep_depth + 1
            return depths[node_idx]

        # Compute all depths
        for idx in range(len(self.nodes)):
            self.nodes[idx].depth = compute_depth(idx)

    def topological_order(self) -> List[int]:
        """
        Return step indices in topological order.

        Returns:
            List of step indices that respects all dependencies
        """
        # Sort by depth first, then by index (stable ordering)
        sorted_nodes = sorted(self.nodes, key=lambda n: (n.depth, n.step_index))
        return [node.step_index for node in sorted_nodes]

    def execution_waves(self) -> List[List[int]]:
        """
        Group steps into execution waves for parallel scheduling.

        Returns:
            List of waves, where each wave is a list of step indices
            that can execute in parallel (same depth, no dependencies)
        """
        # Group by depth
        waves_dict: Dict[int, List[int]] = {}

        for node in self.nodes:
            if node.depth not in waves_dict:
                waves_dict[node.depth] = []
            waves_dict[node.depth].append(node.step_index)

        # Convert to sorted list of waves
        max_depth = max(node.depth for node in self.nodes) if self.nodes else -1
        waves = []
        for depth in range(max_depth + 1):
            if depth in waves_dict:
                waves.append(sorted(waves_dict[depth]))

        return waves

    def can_start(self, step_index: int, completed_steps: Set[int]) -> bool:
        """
        Check if a step can start given completed steps.

        Args:
            step_index: Index of step to check
            completed_steps: Set of already completed step indices

        Returns:
            True if all dependencies are satisfied
        """
        if step_index < 0 or step_index >= len(self.nodes):
            return False

        node = self.nodes[step_index]
        return all(dep_idx in completed_steps for dep_idx in node.dependencies)

    def ready_steps(self, completed_steps: Set[int]) -> List[int]:
        """
        Get all steps that are ready to start.

        Args:
            completed_steps: Set of already completed step indices

        Returns:
            List of step indices that can start now (dependencies satisfied)
        """
        ready = []

        for node in self.nodes:
            if node.step_index not in completed_steps:
                if self.can_start(node.step_index, completed_steps):
                    ready.append(node.step_index)

        return sorted(ready)

    def critical_path(self) -> Tuple[List[int], int]:
        """
        Find the critical path through the recipe.

        The critical path is the longest chain of dependencies,
        determining the minimum total execution time.

        Returns:
            Tuple of (critical_path_steps, max_depth)
        """
        if not self.nodes:
            return ([], 0)

        # Find node with maximum depth
        max_depth_node = max(self.nodes, key=lambda n: n.depth)
        max_depth = max_depth_node.depth

        # Trace back from max depth node
        path = [max_depth_node.step_index]
        current_idx = max_depth_node.step_index

        while self.nodes[current_idx].dependencies:
            # Find dependency with maximum depth
            deps = self.nodes[current_idx].dependencies
            max_dep = max(deps, key=lambda idx: self.nodes[idx].depth)
            path.append(max_dep)
            current_idx = max_dep

        return (list(reversed(path)), max_depth)

    def get_step(self, step_index: int) -> Optional[StepNode]:
        """Get step node by index."""
        if 0 <= step_index < len(self.nodes):
            return self.nodes[step_index]
        return None

    def __len__(self) -> int:
        """Return number of steps in the graph."""
        return len(self.nodes)

    def __repr__(self) -> str:
        """String representation of the graph."""
        return f"DependencyGraph(recipe={self.recipe_id}, steps={len(self.nodes)})"
