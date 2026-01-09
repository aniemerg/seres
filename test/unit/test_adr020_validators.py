"""
Unit tests for ADR-020 validation rules.
"""
import pytest

from src.simulation.adr020_validators import (
    validate_full_duration_machine_required,
    validate_machine_reservation_units,
    validate_machine_id_exists,
    validate_no_overlapping_reservations,
    validate_recipe_dependencies,
    validate_recipe_no_circular_deps,
    validate_recipe_has_steps,
    validate_event_ids_consistent,
    validate_process_adr020,
    validate_recipe_adr020,
)
from src.kb_core.validators import ValidationLevel


class TestFullDurationMachineRequired:
    """Test Rule 1: full_duration_machine_required"""

    def test_valid_process_with_count_unit(self):
        """Process with count unit should pass."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'lathe', 'qty': 1.0, 'unit': 'count'}
            ]
        }
        issue = validate_full_duration_machine_required(process)
        assert issue is None

    def test_valid_process_with_unit_unit(self):
        """Process with 'unit' unit should pass."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'press', 'qty': 1.0, 'unit': 'unit'}
            ]
        }
        issue = validate_full_duration_machine_required(process)
        assert issue is None

    def test_invalid_process_only_partial(self):
        """Process with only partial (hr) reservations should fail."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'furnace', 'qty': 2.0, 'unit': 'hr'}
            ]
        }
        issue = validate_full_duration_machine_required(process)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR
        assert issue.rule == "full_duration_machine_required"

    def test_invalid_process_no_requirements(self):
        """Process with no resource_requirements should fail."""
        process = {'id': 'test_process'}
        issue = validate_full_duration_machine_required(process)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR

    def test_valid_process_mixed_reservations(self):
        """Process with both full and partial should pass."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'lathe', 'qty': 1.0, 'unit': 'count'},
                {'machine_id': 'heating', 'qty': 0.5, 'unit': 'hr'}
            ]
        }
        issue = validate_full_duration_machine_required(process)
        assert issue is None


class TestMachineReservationUnits:
    """Test Rule 2: machine_reservation_units_valid"""

    def test_valid_units(self):
        """Valid units should pass."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'a', 'qty': 1.0, 'unit': 'count'},
                {'machine_id': 'b', 'qty': 1.0, 'unit': 'unit'},
                {'machine_id': 'c', 'qty': 2.0, 'unit': 'hr'}
            ]
        }
        issues = validate_machine_reservation_units(process)
        assert len(issues) == 0

    def test_invalid_unit(self):
        """Invalid unit should fail."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'mill', 'qty': 1.0, 'unit': 'kg'}
            ]
        }
        issues = validate_machine_reservation_units(process)
        assert len(issues) == 1
        assert issues[0].level == ValidationLevel.ERROR
        assert 'kg' in issues[0].message

    def test_multiple_invalid_units(self):
        """Multiple invalid units should all be caught."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'a', 'qty': 1.0, 'unit': 'kg'},
                {'machine_id': 'b', 'qty': 1.0, 'unit': 'count'},
                {'machine_id': 'c', 'qty': 1.0, 'unit': 'm'}
            ]
        }
        issues = validate_machine_reservation_units(process)
        assert len(issues) == 2  # kg and m are invalid


class TestMachineIdExists:
    """Test Rule 3: machine_id_exists"""

    def test_all_machines_exist(self):
        """All referenced machines exist."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'lathe_v0', 'qty': 1.0, 'unit': 'count'}
            ]
        }
        kb_items = {'lathe_v0': {}}
        issues = validate_machine_id_exists(process, kb_items)
        assert len(issues) == 0

    def test_missing_machine(self):
        """Missing machine should generate WARNING."""
        process = {
            'id': 'test_process',
            'resource_requirements': [
                {'machine_id': 'nonexistent', 'qty': 1.0, 'unit': 'count'}
            ]
        }
        kb_items = {}
        issues = validate_machine_id_exists(process, kb_items)
        assert len(issues) == 1
        assert issues[0].level == ValidationLevel.WARNING
        assert 'nonexistent' in issues[0].message


class TestNoOverlappingReservations:
    """Test Rule 4: no_overlapping_reservations"""

    def test_no_overlap(self):
        """Sequential reservations should pass."""
        machine_usage = {
            'lathe': [
                (0.0, 2.0, 'proc_1'),
                (2.0, 4.0, 'proc_2'),
                (4.0, 6.0, 'proc_3')
            ]
        }
        issues = validate_no_overlapping_reservations(machine_usage)
        assert len(issues) == 0

    def test_overlap_detected(self):
        """Overlapping reservations should fail."""
        machine_usage = {
            'lathe': [
                (0.0, 3.0, 'proc_1'),
                (2.0, 5.0, 'proc_2')  # Overlaps with proc_1
            ]
        }
        issues = validate_no_overlapping_reservations(machine_usage)
        assert len(issues) == 1
        assert issues[0].level == ValidationLevel.ERROR
        assert 'proc_1' in issues[0].message
        assert 'proc_2' in issues[0].message

    def test_multiple_machines_separate(self):
        """Overlaps on same machine only."""
        machine_usage = {
            'lathe': [(0.0, 3.0, 'proc_1')],
            'mill': [(0.0, 3.0, 'proc_2')]  # Same time, different machine - OK
        }
        issues = validate_no_overlapping_reservations(machine_usage)
        assert len(issues) == 0

    def test_exact_boundary_no_overlap(self):
        """Process ending when another starts is OK."""
        machine_usage = {
            'lathe': [
                (0.0, 2.0, 'proc_1'),
                (2.0, 4.0, 'proc_2')  # Starts exactly when proc_1 ends
            ]
        }
        issues = validate_no_overlapping_reservations(machine_usage)
        assert len(issues) == 0


class TestRecipeDependencies:
    """Test Rule 7: recipe_dependencies_valid"""

    def test_valid_dependencies(self):
        """Valid dependency indices should pass."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [0]},
                {'process_id': 'step_2', 'dependencies': [0, 1]}
            ]
        }
        issues = validate_recipe_dependencies(recipe)
        assert len(issues) == 0

    def test_invalid_dependency_index(self):
        """Out of range dependency should fail."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'process_id': 'step_0', 'dependencies': []},
                {'process_id': 'step_1', 'dependencies': [5]}  # Index 5 doesn't exist
            ]
        }
        issues = validate_recipe_dependencies(recipe)
        assert len(issues) == 1
        assert issues[0].level == ValidationLevel.ERROR
        assert '5' in issues[0].message


class TestRecipeCircularDeps:
    """Test Rule 8: recipe_no_circular_deps"""

    def test_no_circular_deps(self):
        """DAG should pass."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'dependencies': []},
                {'dependencies': [0]},
                {'dependencies': [1]}
            ]
        }
        issue = validate_recipe_no_circular_deps(recipe)
        assert issue is None

    def test_circular_deps_detected(self):
        """Circular dependency should fail."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'dependencies': [2]},  # Depends on step 2
                {'dependencies': [0]},
                {'dependencies': [1]}   # Creates cycle: 0 -> 2 -> 1 -> 0
            ]
        }
        issue = validate_recipe_no_circular_deps(recipe)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR
        assert 'circular' in issue.message.lower()

    def test_self_dependency(self):
        """Self-dependency is a circular dep."""
        recipe = {
            'id': 'test_recipe',
            'steps': [
                {'dependencies': [0]}  # Depends on itself
            ]
        }
        issue = validate_recipe_no_circular_deps(recipe)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR


class TestRecipeHasSteps:
    """Test Rule 9: recipe_has_steps"""

    def test_recipe_with_steps(self):
        """Recipe with steps should pass."""
        recipe = {
            'id': 'test_recipe',
            'steps': [{'process_id': 'step_0'}]
        }
        issue = validate_recipe_has_steps(recipe)
        assert issue is None

    def test_recipe_without_steps(self):
        """Recipe without steps should fail."""
        recipe = {
            'id': 'test_recipe',
            'steps': []
        }
        issue = validate_recipe_has_steps(recipe)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR

    def test_recipe_missing_steps_field(self):
        """Recipe missing steps field should fail."""
        recipe = {'id': 'test_recipe'}
        issue = validate_recipe_has_steps(recipe)
        assert issue is not None
        assert issue.level == ValidationLevel.ERROR


class TestEventIdsConsistent:
    """Test Rule 10: event_ids_consistent"""

    def test_matching_process_ids(self):
        """Matching process IDs should pass."""
        events = [
            {
                'type': 'process_start',
                'process_run_id': 'run_1',
                'process_id': 'welding_v0'
            },
            {
                'type': 'process_complete',
                'process_run_id': 'run_1',
                'process_id': 'welding_v0'
            }
        ]
        issues = validate_event_ids_consistent(events)
        assert len(issues) == 0

    def test_mismatched_process_ids(self):
        """Mismatched process IDs should fail."""
        events = [
            {
                'type': 'process_start',
                'process_run_id': 'run_1',
                'process_id': 'welding_v0'
            },
            {
                'type': 'process_complete',
                'process_run_id': 'run_1',
                'process_id': 'cutting_v0'  # Different!
            }
        ]
        issues = validate_event_ids_consistent(events)
        assert len(issues) == 1
        assert issues[0].level == ValidationLevel.ERROR
        assert 'welding_v0' in issues[0].message
        assert 'cutting_v0' in issues[0].message


class TestConvenienceFunctions:
    """Test convenience validation functions."""

    def test_validate_process_adr020(self):
        """Should run all process validation rules."""
        process = {
            'id': 'test_process',
            'resource_requirements': []  # Missing full-duration
        }
        issues = validate_process_adr020(process, {})
        # Should catch missing full-duration machine
        assert any(i.rule == 'full_duration_machine_required' for i in issues)

    def test_validate_recipe_adr020(self):
        """Should run all recipe validation rules."""
        recipe = {
            'id': 'test_recipe',
            'steps': []  # Empty
        }
        issues = validate_recipe_adr020(recipe)
        # Should catch empty steps
        assert any(i.rule == 'recipe_has_steps' for i in issues)
