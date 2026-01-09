"""
Unit tests for dependency graph builder (ADR-020).
"""
import pytest

from src.simulation.dependency_graph import DependencyGraph, StepNode


class TestDependencyGraphConstruction:
    """Test dependency graph construction and validation."""

    def test_simple_linear_chain(self):
        """Test linear dependency chain: 0 -> 1 -> 2."""
        recipe = {
            'id': 'linear_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [1]},
            ]
        }

        graph = DependencyGraph(recipe)

        assert len(graph) == 3
        assert graph.nodes[0].depth == 0
        assert graph.nodes[1].depth == 1
        assert graph.nodes[2].depth == 2

    def test_parallel_steps(self):
        """Test parallel steps with common dependency."""
        recipe = {
            'id': 'parallel_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)

        assert len(graph) == 3
        assert graph.nodes[0].depth == 0
        assert graph.nodes[1].depth == 1
        assert graph.nodes[2].depth == 1

    def test_diamond_dependency(self):
        """Test diamond dependency pattern: 0 -> 1,2 -> 3."""
        recipe = {
            'id': 'diamond_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
                {'process_id': 'step_3', 'dependencies': [1, 2]},
            ]
        }

        graph = DependencyGraph(recipe)

        assert len(graph) == 4
        assert graph.nodes[0].depth == 0
        assert graph.nodes[1].depth == 1
        assert graph.nodes[2].depth == 1
        assert graph.nodes[3].depth == 2

    def test_no_dependencies(self):
        """Test recipe with no dependencies."""
        recipe = {
            'id': 'parallel_only',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': []},
                {'process_id': 'step_2', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)

        assert len(graph) == 3
        assert all(node.depth == 0 for node in graph.nodes)


class TestDependencyGraphValidation:
    """Test dependency graph validation."""

    def test_circular_dependency_detected(self):
        """Circular dependency should raise ValueError."""
        recipe = {
            'id': 'circular_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': [2]},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [1]},
            ]
        }

        with pytest.raises(ValueError, match='circular dependencies'):
            DependencyGraph(recipe)

    def test_self_dependency_detected(self):
        """Self-dependency should raise ValueError."""
        recipe = {
            'id': 'self_dep_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': [0]},
            ]
        }

        with pytest.raises(ValueError, match='circular dependencies'):
            DependencyGraph(recipe)

    def test_invalid_dependency_index_high(self):
        """Dependency index out of range (too high) should raise ValueError."""
        recipe = {
            'id': 'invalid_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [5]},  # Only 2 steps
            ]
        }

        with pytest.raises(ValueError, match='invalid dependency index'):
            DependencyGraph(recipe)

    def test_invalid_dependency_index_negative(self):
        """Negative dependency index should raise ValueError."""
        recipe = {
            'id': 'invalid_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [-1]},
            ]
        }

        with pytest.raises(ValueError, match='invalid dependency index'):
            DependencyGraph(recipe)


class TestTopologicalOrder:
    """Test topological ordering."""

    def test_linear_topological_order(self):
        """Linear chain should give sequential order."""
        recipe = {
            'id': 'linear',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [1]},
            ]
        }

        graph = DependencyGraph(recipe)
        order = graph.topological_order()

        assert order == [0, 1, 2]

    def test_parallel_topological_order(self):
        """Parallel steps should come after their dependency."""
        recipe = {
            'id': 'parallel',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)
        order = graph.topological_order()

        assert order[0] == 0  # step 0 must be first
        assert set(order[1:]) == {1, 2}  # steps 1,2 can be in any order

    def test_complex_topological_order(self):
        """Complex DAG should respect all dependencies."""
        recipe = {
            'id': 'complex',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
                {'process_id': 'step_3', 'dependencies': [1, 2]},
                {'process_id': 'step_4', 'dependencies': [3]},
            ]
        }

        graph = DependencyGraph(recipe)
        order = graph.topological_order()

        # Verify ordering respects dependencies
        position = {idx: pos for pos, idx in enumerate(order)}

        for node in graph.nodes:
            for dep_idx in node.dependencies:
                assert position[dep_idx] < position[node.step_index], \
                    f"Dependency {dep_idx} should come before {node.step_index}"


class TestExecutionWaves:
    """Test execution wave generation."""

    def test_linear_waves(self):
        """Linear chain should have one step per wave."""
        recipe = {
            'id': 'linear',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [1]},
            ]
        }

        graph = DependencyGraph(recipe)
        waves = graph.execution_waves()

        assert waves == [[0], [1], [2]]

    def test_parallel_waves(self):
        """Parallel steps should be in same wave."""
        recipe = {
            'id': 'parallel',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)
        waves = graph.execution_waves()

        assert len(waves) == 2
        assert waves[0] == [0]
        assert set(waves[1]) == {1, 2}

    def test_diamond_waves(self):
        """Diamond pattern should have 3 waves."""
        recipe = {
            'id': 'diamond',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
                {'process_id': 'step_3', 'dependencies': [1, 2]},
            ]
        }

        graph = DependencyGraph(recipe)
        waves = graph.execution_waves()

        assert len(waves) == 3
        assert waves[0] == [0]
        assert set(waves[1]) == {1, 2}
        assert waves[2] == [3]


class TestReadySteps:
    """Test ready step detection."""

    def test_initial_ready_steps(self):
        """Steps with no dependencies should be ready initially."""
        recipe = {
            'id': 'test',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': []},
                {'process_id': 'step_2', 'dependencies': [0, 1]},
            ]
        }

        graph = DependencyGraph(recipe)
        ready = graph.ready_steps(completed_steps=set())

        assert set(ready) == {0, 1}

    def test_ready_after_completion(self):
        """Step becomes ready when dependencies complete."""
        recipe = {
            'id': 'test',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0, 1]},
            ]
        }

        graph = DependencyGraph(recipe)

        # Initially only step 0 is ready
        ready = graph.ready_steps(completed_steps=set())
        assert ready == [0]

        # After step 0 completes, step 1 is ready
        ready = graph.ready_steps(completed_steps={0})
        assert ready == [1]

        # After steps 0,1 complete, step 2 is ready
        ready = graph.ready_steps(completed_steps={0, 1})
        assert ready == [2]

    def test_can_start(self):
        """Test can_start predicate."""
        recipe = {
            'id': 'test',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)

        assert graph.can_start(0, set()) is True
        assert graph.can_start(1, set()) is False
        assert graph.can_start(1, {0}) is True


class TestCriticalPath:
    """Test critical path analysis."""

    def test_linear_critical_path(self):
        """Linear chain critical path is the entire chain."""
        recipe = {
            'id': 'linear',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [1]},
            ]
        }

        graph = DependencyGraph(recipe)
        path, depth = graph.critical_path()

        assert path == [0, 1, 2]
        assert depth == 2

    def test_diamond_critical_path(self):
        """Diamond pattern critical path goes through any branch."""
        recipe = {
            'id': 'diamond',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0]},
                {'process_id': 'step_3', 'dependencies': [1, 2]},
            ]
        }

        graph = DependencyGraph(recipe)
        path, depth = graph.critical_path()

        # Path should be: 0 -> (1 or 2) -> 3
        assert len(path) == 3
        assert path[0] == 0
        assert path[1] in {1, 2}
        assert path[2] == 3
        assert depth == 2

    def test_empty_critical_path(self):
        """Empty recipe has no critical path."""
        recipe = {
            'id': 'empty',
            'steps': []
        }

        graph = DependencyGraph(recipe)
        path, depth = graph.critical_path()

        assert path == []
        assert depth == 0


class TestGraphUtilities:
    """Test utility methods."""

    def test_get_step(self):
        """Test step retrieval by index."""
        recipe = {
            'id': 'test',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
            ]
        }

        graph = DependencyGraph(recipe)

        step = graph.get_step(0)
        assert step is not None
        assert step.step_index == 0
        assert step.process_id == 'step_0'

        step = graph.get_step(1)
        assert step is not None
        assert step.step_index == 1

        step = graph.get_step(99)
        assert step is None

    def test_len(self):
        """Test graph length."""
        recipe = {
            'id': 'test',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': []},
                {'process_id': 'step_2', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)
        assert len(graph) == 3

    def test_repr(self):
        """Test string representation."""
        recipe = {
            'id': 'my_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
            ]
        }

        graph = DependencyGraph(recipe)
        repr_str = repr(graph)

        assert 'DependencyGraph' in repr_str
        assert 'my_recipe' in repr_str
        assert 'steps=1' in repr_str
