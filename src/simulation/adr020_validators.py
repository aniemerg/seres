"""
ADR-020 Validation Rules

Validates recipe orchestration, machine reservations, and scheduling constraints.

Ten validation rules per ADR-020 Section 10:

Process Definition Rules:
1. full_duration_machine_required (ERROR)
2. machine_reservation_units_valid (ERROR)
3. machine_id_exists (WARNING)
4. machine_id_is_machine_kind (ERROR)

Scheduling Rules:
4. no_overlapping_reservations (ERROR)
5. duration_calculated_correctly (WARNING)
6. energy_calculated_correctly (WARNING)

Recipe Rules:
7. recipe_dependencies_valid (ERROR)
8. recipe_no_circular_deps (ERROR)
9. recipe_has_steps (ERROR)

Event Rules:
10. event_ids_consistent (ERROR)
"""
from __future__ import annotations

from typing import List, Dict, Any, Set, Optional
from enum import Enum

from src.kb_core.validators import ValidationIssue, ValidationLevel


# =============================================================================
# Process Definition Validation
# =============================================================================

def validate_full_duration_machine_required(process: Dict[str, Any]) -> Optional[ValidationIssue]:
    """
    Rule 1: Every process must have ≥1 full-duration machine reservation.

    Full-duration means unit is "count" or "unit", not "hr".

    Per ADR-020: A process is invalid unless it has at least one
    resource_requirements entry with unit: count/unit and qty >= 1.
    """
    process_id = process.get('id', 'unknown')
    resource_reqs = process.get('resource_requirements', [])

    # Check for at least one full-duration reservation
    has_full_duration = False
    for req in resource_reqs:
        unit = req.get('unit', '')
        qty = req.get('qty', 0)

        if unit in ('count', 'unit') and qty >= 1:
            has_full_duration = True
            break

    if not has_full_duration:
        return ValidationIssue(
            level=ValidationLevel.ERROR,
            category="process_definition",
            rule="full_duration_machine_required",
            entity_type="process",
            entity_id=process_id,
            message=f"Process '{process_id}' must have at least one full-duration machine reservation (unit: count or unit, qty >= 1)",
            field_path="resource_requirements",
            fix_hint="Add a resource_requirements entry with unit='count' or 'unit' and qty >= 1"
        )

    return None


def validate_machine_reservation_units(process: Dict[str, Any]) -> List[ValidationIssue]:
    """
    Rule 2: Validate unit field matches reservation type.

    - Full-duration: unit must be "count" or "unit"
    - Partial: unit must be "hr"
    """
    issues = []
    process_id = process.get('id', 'unknown')
    resource_reqs = process.get('resource_requirements', [])

    valid_units = {'count', 'unit', 'hr'}

    for idx, req in enumerate(resource_reqs):
        unit = req.get('unit', '')

        if unit not in valid_units:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="process_definition",
                rule="machine_reservation_units_valid",
                entity_type="process",
                entity_id=process_id,
                message=f"Invalid unit '{unit}' in resource_requirements[{idx}]. Must be 'count', 'unit', or 'hr'",
                field_path=f"resource_requirements[{idx}].unit",
                fix_hint="Use 'count' or 'unit' for full-duration, 'hr' for partial reservations"
            ))

    return issues


def validate_machine_id_exists(process: Dict[str, Any], kb_items: Dict[str, Any]) -> List[ValidationIssue]:
    """
    Rule 3: Check that machine_id references exist in KB.

    WARNING level - missing machines should be flagged but not block simulation.
    """
    issues = []
    process_id = process.get('id', 'unknown')
    resource_reqs = process.get('resource_requirements', [])

    for idx, req in enumerate(resource_reqs):
        machine_id = req.get('machine_id')

        if machine_id and machine_id not in kb_items:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="reference",
                rule="machine_id_exists",
                entity_type="process",
                entity_id=process_id,
                message=f"Machine '{machine_id}' referenced in resource_requirements[{idx}] not found in KB",
                field_path=f"resource_requirements[{idx}].machine_id",
                fix_hint=f"Define machine '{machine_id}' in kb/items/machines/ or update reference"
            ))

    return issues


def validate_machine_id_is_machine_kind(process: Dict[str, Any], kb_items: Dict[str, Any]) -> List[ValidationIssue]:
    """
    Rule 4: Ensure machine_id references items with kind: machine.

    ERROR level - non-machine items cause reservation failures at runtime.
    """
    issues = []
    process_id = process.get('id', 'unknown')
    resource_reqs = process.get('resource_requirements', [])

    for idx, req in enumerate(resource_reqs):
        machine_id = req.get('machine_id')
        if not machine_id:
            continue

        item = kb_items.get(machine_id)
        if not item:
            continue

        item_def = item.model_dump() if hasattr(item, "model_dump") else item
        kind = item_def.get("kind")

        if kind != "machine":
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="reference",
                rule="machine_id_is_machine_kind",
                entity_type="process",
                entity_id=process_id,
                message=(
                    f"Machine '{machine_id}' referenced in resource_requirements[{idx}] "
                    f"has kind '{kind}', expected kind 'machine'"
                ),
                field_path=f"resource_requirements[{idx}].machine_id",
                fix_hint=f"Change item '{machine_id}' to kind: machine or update the process requirement"
            ))

    return issues


# =============================================================================
# Scheduling Validation
# =============================================================================

def validate_no_overlapping_reservations(
    machine_usage: Dict[str, List[tuple[float, float, str]]]
) -> List[ValidationIssue]:
    """
    Rule 4: Detect overlapping machine reservations.

    machine_usage format: machine_id → [(start, end, process_run_id), ...]

    ERROR level - overlapping reservations indicate scheduling conflict.
    """
    issues = []

    for machine_id, reservations in machine_usage.items():
        # Sort by start time
        sorted_res = sorted(reservations, key=lambda x: x[0])

        # Check for overlaps
        for i in range(len(sorted_res) - 1):
            curr_start, curr_end, curr_proc = sorted_res[i]
            next_start, next_end, next_proc = sorted_res[i + 1]

            if next_start < curr_end:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="scheduling",
                    rule="no_overlapping_reservations",
                    entity_type="machine",
                    entity_id=machine_id,
                    message=(
                        f"Machine '{machine_id}' has overlapping reservations: "
                        f"process {curr_proc} ({curr_start}-{curr_end}h) overlaps with "
                        f"process {next_proc} ({next_start}-{next_end}h)"
                    ),
                    fix_hint="Reschedule processes to avoid conflicts or add more machine capacity"
                ))

    return issues


def validate_duration_calculated_correctly(
    process: Dict[str, Any],
    calculated_duration: float,
    actual_duration: float,
    tolerance: float = 0.01
) -> Optional[ValidationIssue]:
    """
    Rule 5: Verify duration matches time_model calculation.

    WARNING level - helps catch calculation errors but doesn't block.
    """
    process_id = process.get('id', 'unknown')

    if abs(calculated_duration - actual_duration) > tolerance:
        return ValidationIssue(
            level=ValidationLevel.WARNING,
            category="calculation",
            rule="duration_calculated_correctly",
            entity_type="process",
            entity_id=process_id,
            message=(
                f"Duration mismatch for process '{process_id}': "
                f"calculated {calculated_duration:.2f}h, actual {actual_duration:.2f}h"
            ),
            fix_hint="Verify time_model parameters and scaling_basis match inputs/outputs"
        )

    return None


def validate_energy_calculated_correctly(
    process: Dict[str, Any],
    calculated_energy: float,
    actual_energy: float,
    tolerance: float = 0.01
) -> Optional[ValidationIssue]:
    """
    Rule 6: Verify energy matches energy_model calculation.

    WARNING level - helps catch calculation errors.
    """
    process_id = process.get('id', 'unknown')

    if abs(calculated_energy - actual_energy) > tolerance:
        return ValidationIssue(
            level=ValidationLevel.WARNING,
            category="calculation",
            rule="energy_calculated_correctly",
            entity_type="process",
            entity_id=process_id,
            message=(
                f"Energy mismatch for process '{process_id}': "
                f"calculated {calculated_energy:.2f} kWh, actual {actual_energy:.2f} kWh"
            ),
            fix_hint="Verify energy_model parameters and scaling_basis match inputs/outputs"
        )

    return None


# =============================================================================
# Recipe Validation
# =============================================================================

def validate_recipe_dependencies(recipe: Dict[str, Any]) -> List[ValidationIssue]:
    """
    Rule 7: All dependencies reference valid steps.

    ERROR level - invalid dependencies will cause runtime failures.
    """
    issues = []
    recipe_id = recipe.get('id', 'unknown')
    steps = recipe.get('steps', [])

    # Build set of valid step indices
    valid_indices = set(range(len(steps)))

    for step_idx, step in enumerate(steps):
        dependencies = step.get('dependencies', [])

        for dep_idx in dependencies:
            if dep_idx not in valid_indices:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="recipe",
                    rule="recipe_dependencies_valid",
                    entity_type="recipe",
                    entity_id=recipe_id,
                    message=(
                        f"Recipe '{recipe_id}' step {step_idx} references "
                        f"invalid dependency index {dep_idx} (only {len(steps)} steps)"
                    ),
                    field_path=f"steps[{step_idx}].dependencies",
                    fix_hint=f"Use dependency index in range 0-{len(steps)-1}"
                ))

    return issues


def validate_recipe_no_circular_deps(recipe: Dict[str, Any]) -> Optional[ValidationIssue]:
    """
    Rule 8: Dependency graph must be acyclic (no circular dependencies).

    ERROR level - circular deps prevent scheduling.
    """
    recipe_id = recipe.get('id', 'unknown')
    steps = recipe.get('steps', [])

    # Build adjacency list
    graph: Dict[int, List[int]] = {}
    for step_idx, step in enumerate(steps):
        graph[step_idx] = step.get('dependencies', [])

    # Detect cycles using DFS
    visited = set()
    rec_stack = set()

    def has_cycle(node: int) -> bool:
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    # Check all nodes
    for node in graph:
        if node not in visited:
            if has_cycle(node):
                return ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="recipe",
                    rule="recipe_no_circular_deps",
                    entity_type="recipe",
                    entity_id=recipe_id,
                    message=f"Recipe '{recipe_id}' has circular dependencies in step graph",
                    field_path="steps[*].dependencies",
                    fix_hint="Remove circular dependencies to create a valid DAG"
                )

    return None


def validate_recipe_has_steps(recipe: Dict[str, Any]) -> Optional[ValidationIssue]:
    """
    Rule 9: Recipe must have at least one step.

    ERROR level - empty recipe cannot execute.
    """
    recipe_id = recipe.get('id', 'unknown')
    steps = recipe.get('steps', [])

    if not steps or len(steps) == 0:
        return ValidationIssue(
            level=ValidationLevel.ERROR,
            category="recipe",
            rule="recipe_has_steps",
            entity_type="recipe",
            entity_id=recipe_id,
            message=f"Recipe '{recipe_id}' has no steps",
            field_path="steps",
            fix_hint="Add at least one step with process_id"
        )

    return None


# =============================================================================
# Event Validation
# =============================================================================

def validate_event_ids_consistent(events: List[Dict[str, Any]]) -> List[ValidationIssue]:
    """
    Rule 10: Runtime IDs must be consistent between related events.

    ERROR level - inconsistent IDs indicate data corruption.

    Checks:
    - process_scheduled -> process_start -> process_complete: same process_run_id
    - recipe_start -> recipe_complete: same recipe_run_id
    """
    issues = []

    # Track runtime IDs
    process_scheduled: Dict[str, Dict[str, Any]] = {}  # process_run_id → event
    process_starts: Dict[str, Dict[str, Any]] = {}  # process_run_id → event
    recipe_starts: Dict[str, Dict[str, Any]] = {}  # recipe_run_id → event

    for event in events:
        event_type = event.get('type')

        if event_type == 'process_scheduled':
            process_run_id = event.get('process_run_id')
            if process_run_id:
                process_scheduled[process_run_id] = event

        if event_type == 'process_start':
            process_run_id = event.get('process_run_id')
            if process_run_id:
                process_starts[process_run_id] = event
                if process_run_id in process_scheduled:
                    scheduled_event = process_scheduled[process_run_id]
                    if scheduled_event.get('process_id') != event.get('process_id'):
                        issues.append(ValidationIssue(
                            level=ValidationLevel.ERROR,
                            category="event",
                            rule="event_ids_consistent",
                            entity_type="process_run",
                            entity_id=process_run_id,
                            message=(
                                f"Process ID mismatch for process_run_id={process_run_id}: "
                                f"scheduled as '{scheduled_event.get('process_id')}', "
                                f"started as '{event.get('process_id')}'"
                            )
                        ))

        elif event_type == 'process_complete':
            process_run_id = event.get('process_run_id')
            if process_run_id and process_run_id in process_starts:
                start_event = process_starts[process_run_id]

                # Verify process_id matches
                if start_event.get('process_id') != event.get('process_id'):
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="event",
                        rule="event_ids_consistent",
                        entity_type="process_run",
                        entity_id=process_run_id,
                        message=(
                            f"Process ID mismatch for process_run_id={process_run_id}: "
                            f"started as '{start_event.get('process_id')}', "
                            f"completed as '{event.get('process_id')}'"
                        )
                    ))
            elif process_run_id and process_run_id in process_scheduled:
                scheduled_event = process_scheduled[process_run_id]
                if scheduled_event.get('process_id') != event.get('process_id'):
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="event",
                        rule="event_ids_consistent",
                        entity_type="process_run",
                        entity_id=process_run_id,
                        message=(
                            f"Process ID mismatch for process_run_id={process_run_id}: "
                            f"scheduled as '{scheduled_event.get('process_id')}', "
                            f"completed as '{event.get('process_id')}'"
                        )
                    ))

        elif event_type == 'recipe_start':
            recipe_run_id = event.get('recipe_run_id')
            if recipe_run_id:
                recipe_starts[recipe_run_id] = event

        elif event_type == 'recipe_complete':
            recipe_run_id = event.get('recipe_run_id')
            if recipe_run_id and recipe_run_id in recipe_starts:
                start_event = recipe_starts[recipe_run_id]

                # Verify recipe_id matches
                if start_event.get('recipe_id') != event.get('recipe_id'):
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="event",
                        rule="event_ids_consistent",
                        entity_type="recipe_run",
                        entity_id=recipe_run_id,
                        message=(
                            f"Recipe ID mismatch for recipe_run_id={recipe_run_id}: "
                            f"started as '{start_event.get('recipe_id')}', "
                            f"completed as '{event.get('recipe_id')}'"
                        )
                    ))

    return issues


# =============================================================================
# Convenience Functions
# =============================================================================

def validate_process_adr020(process: Dict[str, Any], kb_items: Dict[str, Any]) -> List[ValidationIssue]:
    """
    Run all ADR-020 process validation rules.

    Args:
        process: Process definition dict
        kb_items: KB items dict for reference validation

    Returns:
        List of validation issues
    """
    issues = []

    # Rule 1: Full-duration machine required
    issue = validate_full_duration_machine_required(process)
    if issue:
        issues.append(issue)

    # Rule 2: Machine reservation units valid
    issues.extend(validate_machine_reservation_units(process))

    # Rule 3: Machine ID exists
    issues.extend(validate_machine_id_exists(process, kb_items))

    # Rule 4: Machine ID references machine kind
    issues.extend(validate_machine_id_is_machine_kind(process, kb_items))

    return issues


def validate_recipe_adr020(recipe: Dict[str, Any]) -> List[ValidationIssue]:
    """
    Run all ADR-020 recipe validation rules.

    Args:
        recipe: Recipe definition dict

    Returns:
        List of validation issues
    """
    issues = []

    # Rule 7: Dependencies valid
    issues.extend(validate_recipe_dependencies(recipe))

    # Rule 8: No circular dependencies
    issue = validate_recipe_no_circular_deps(recipe)
    if issue:
        issues.append(issue)

    # Rule 9: Has steps
    issue = validate_recipe_has_steps(recipe)
    if issue:
        issues.append(issue)

    return issues
