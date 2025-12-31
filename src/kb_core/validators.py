"""
Validation System for KB Data

Implements ADR-017: Validation and Error Detection Strategy

Provides comprehensive validation with three severity levels:
- ERROR: Hard error, blocks simulation, must be fixed
- WARNING: Soft warning, may affect quality, should be fixed
- INFO: Informational, suggestion for improvement
"""
from __future__ import annotations

from enum import Enum
from typing import List, Optional, Dict, Any

from .schema import Process, Recipe, Item
from .unit_converter import (
    UnitConverter,
    parse_compound_unit,
    is_valid_unit,
)


class ValidationLevel(Enum):
    """Validation severity level."""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class ValidationIssue:
    """Single validation issue."""

    def __init__(
        self,
        level: ValidationLevel,
        category: str,
        rule: str,
        entity_type: str,
        entity_id: str,
        message: str,
        field_path: Optional[str] = None,
        fix_hint: Optional[str] = None
    ):
        self.level = level
        self.category = category
        self.rule = rule
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.message = message
        self.field_path = field_path
        self.fix_hint = fix_hint

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "level": self.level.value,
            "category": self.category,
            "rule": self.rule,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "message": self.message,
            "field_path": self.field_path,
            "fix_hint": self.fix_hint,
        }

    def __repr__(self) -> str:
        return (
            f"ValidationIssue({self.level.value}, {self.entity_id}, "
            f"{self.rule}: {self.message})"
        )


# =============================================================================
# Helper Functions
# =============================================================================

def _get_entity_id(entity: Any) -> str:
    """Extract entity ID from Pydantic model or dict."""
    if hasattr(entity, 'id'):
        return entity.id
    elif isinstance(entity, dict):
        return entity.get('id', 'unknown')
    else:
        return 'unknown'


# =============================================================================
# Schema Validation (Category 1)
# =============================================================================

def validate_process_schema(process: Any) -> List[ValidationIssue]:
    """
    Validate process schema compliance.

    Rules:
    - process_type required (ERROR)
    - time_model.type consistency (ERROR)
    - energy_model.type valid (ERROR)
    - Required fields present (ERROR)
    - No deprecated fields (ERROR)
    """
    issues = []
    process_id = _get_entity_id(process)

    # Get as dict if it's a Pydantic model
    if hasattr(process, 'model_dump'):
        process_dict = process.model_dump()
    else:
        process_dict = process

    # Rule 1: process_type required
    process_type = process_dict.get('process_type')
    if not process_type:
        issues.append(ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id=process_id,
            message="Missing required field 'process_type'",
            field_path="process_type",
            fix_hint="Add 'process_type: batch', 'process_type: continuous', or 'process_type: boundary'"
        ))
        return issues  # Can't validate further without process_type

    # Rule 2: process_type valid
    if process_type not in ["batch", "continuous", "boundary"]:
        issues.append(ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_invalid",
            entity_type="process",
            entity_id=process_id,
            message=(
                f"Invalid process_type '{process_type}'. Must be 'batch', 'continuous', or 'boundary'"
            ),
            field_path="process_type",
            fix_hint="Set to 'batch', 'continuous', or 'boundary'"
        ))

    # Rule 3: time_model.type consistency
    time_model = process_dict.get('time_model')
    if time_model:
        tm_type = time_model.get('type')

        if process_type == "continuous" and tm_type != "linear_rate":
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="time_model_type_mismatch",
                entity_type="process",
                entity_id=process_id,
                message=f"process_type 'continuous' requires time_model.type 'linear_rate', got '{tm_type}'",
                field_path="time_model.type",
                fix_hint="Change time_model.type to 'linear_rate' or change process_type"
            ))

        if process_type == "batch" and tm_type != "batch":
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="time_model_type_mismatch",
                entity_type="process",
                entity_id=process_id,
                message=f"process_type 'batch' requires time_model.type 'batch', got '{tm_type}'",
                field_path="time_model.type",
                fix_hint="Change time_model.type to 'batch' or change process_type"
            ))
        if process_type == "boundary" and tm_type not in ["batch", "linear_rate"]:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="time_model_type_mismatch",
                entity_type="process",
                entity_id=process_id,
                message=(
                    f"process_type 'boundary' requires time_model.type "
                    f"'batch' or 'linear_rate', got '{tm_type}'"
                ),
                field_path="time_model.type",
                fix_hint="Change time_model.type to 'batch' or 'linear_rate'"
            ))
        # Rule 4: Required fields for linear_rate
        if tm_type == "linear_rate":
            for field in ["rate", "rate_unit", "scaling_basis"]:
                if field not in time_model or time_model[field] is None:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="schema",
                        rule="required_field_missing",
                        entity_type="process",
                        entity_id=process_id,
                        message=f"time_model.type 'linear_rate' requires field '{field}'",
                        field_path=f"time_model.{field}",
                        fix_hint=f"Add time_model.{field}"
                    ))

        # Rule 5: Required fields for batch
        if tm_type == "batch":
            if "hr_per_batch" not in time_model or time_model["hr_per_batch"] is None:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="schema",
                    rule="required_field_missing",
                    entity_type="process",
                    entity_id=process_id,
                    message="time_model.type 'batch' requires field 'hr_per_batch'",
                    field_path="time_model.hr_per_batch",
                    fix_hint="Add time_model.hr_per_batch"
                ))

        # Rule 6: No deprecated fields
        deprecated_fields = {
            "rate_kg_per_hr": "Use 'rate: X' and 'rate_unit: kg/hr'",
            "hr_per_kg": "Use 'rate: X' and 'rate_unit: kg/hr' (invert rate)",
        }

        for deprecated, hint in deprecated_fields.items():
            # Check if field exists AND has a non-None value
            if deprecated in time_model and time_model.get(deprecated) is not None:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="schema",
                    rule="deprecated_field",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Deprecated field 'time_model.{deprecated}' used",
                    field_path=f"time_model.{deprecated}",
                    fix_hint=hint
                ))
    elif process_type == "boundary":
        issues.append(ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="required_field_missing",
            entity_type="process",
            entity_id=process_id,
            message="process_type 'boundary' requires time_model",
            field_path="time_model",
            fix_hint="Add time_model with type 'batch' or 'linear_rate'"
        ))

    # Rule 7: energy_model validation
    energy_model = process_dict.get('energy_model')
    if energy_model:
        em_type = energy_model.get('type')

        # Valid types
        if em_type not in ["per_unit", "fixed_per_batch"]:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="energy_model_type_invalid",
                entity_type="process",
                entity_id=process_id,
                message=f"Invalid energy_model.type '{em_type}'. Must be 'per_unit' or 'fixed_per_batch'",
                field_path="energy_model.type",
                fix_hint="Change to 'per_unit' or 'fixed_per_batch'"
            ))

        # Required fields for per_unit
        if em_type == "per_unit":
            for field in ["value", "unit", "scaling_basis"]:
                if field not in energy_model or energy_model[field] is None:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="schema",
                        rule="required_field_missing",
                        entity_type="process",
                        entity_id=process_id,
                        message=f"energy_model.type 'per_unit' requires field '{field}'",
                        field_path=f"energy_model.{field}",
                        fix_hint=f"Add energy_model.{field}"
                    ))

        # Required fields for fixed_per_batch
        if em_type == "fixed_per_batch":
            for field in ["value", "unit"]:
                if field not in energy_model or energy_model[field] is None:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="schema",
                        rule="required_field_missing",
                        entity_type="process",
                        entity_id=process_id,
                        message=f"energy_model.type 'fixed_per_batch' requires field '{field}'",
                        field_path=f"energy_model.{field}",
                        fix_hint=f"Add energy_model.{field}"
                    ))

        # Deprecated energy fields
        deprecated_energy = {
            "kWh_per_kg": "Use 'type: per_unit' with 'unit: kWh/kg'",
            "kWh_per_batch": "Use 'type: fixed_per_batch' with 'unit: kWh'",
        }

        for deprecated, hint in deprecated_energy.items():
            if deprecated in energy_model:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="schema",
                    rule="deprecated_field",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Deprecated field 'energy_model.{deprecated}' used",
                    field_path=f"energy_model.{deprecated}",
                    fix_hint=hint
                ))
    elif process_type == "boundary":
        issues.append(ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="required_field_missing",
            entity_type="process",
            entity_id=process_id,
            message="process_type 'boundary' requires energy_model",
            field_path="energy_model",
            fix_hint="Add energy_model with type 'fixed_per_batch' or 'per_unit'"
        ))

    return issues


# =============================================================================
# Semantic Validation (Category 2)
# =============================================================================

def validate_process_semantics(process: Any) -> List[ValidationIssue]:
    """
    Validate process semantic correctness.

    Rules:
    - scaling_basis exists in inputs/outputs (ERROR)
    - No setup_hr in continuous (ERROR)
    - Positive values (ERROR)
    - Compound unit format (ERROR)
    - Known units (ERROR)
    """
    issues = []
    process_id = _get_entity_id(process)

    # Get as dict if it's a Pydantic model
    if hasattr(process, 'model_dump'):
        process_dict = process.model_dump()
    else:
        process_dict = process

    process_type = process_dict.get('process_type')
    time_model = process_dict.get('time_model')
    energy_model = process_dict.get('energy_model')

    # Rule 0: Boundary processes must have no inputs and at least one output
    if process_type == "boundary":
        inputs = process_dict.get('inputs', []) or []
        outputs = process_dict.get('outputs', []) or []
        resource_requirements = process_dict.get('resource_requirements', []) or []
        if inputs:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="boundary_inputs_not_allowed",
                entity_type="process",
                entity_id=process_id,
                message="Boundary processes must not declare inputs",
                field_path="inputs",
                fix_hint="Remove inputs or change process_type"
            ))
        if not outputs:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="boundary_outputs_required",
                entity_type="process",
                entity_id=process_id,
                message="Boundary processes must declare at least one output",
                field_path="outputs",
                fix_hint="Add outputs or change process_type"
            ))
        if not resource_requirements:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="semantic",
                rule="boundary_machine_missing",
                entity_type="process",
                entity_id=process_id,
                message="Boundary processes should declare at least one machine requirement",
                field_path="resource_requirements",
                fix_hint="Add resource_requirements for the machine that performs collection"
            ))

    # Collect all input/output item_ids
    all_item_ids = set()
    for inp in process_dict.get('inputs', []) or []:
        if inp.get('item_id'):
            all_item_ids.add(inp['item_id'])
    for out in process_dict.get('outputs', []) or []:
        if out.get('item_id'):
            all_item_ids.add(out['item_id'])

    # Rule 1: time_model scaling_basis exists
    if time_model and time_model.get('type') == 'linear_rate':
        scaling_basis = time_model.get('scaling_basis')
        if scaling_basis and scaling_basis not in all_item_ids:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="scaling_basis_not_found",
                entity_type="process",
                entity_id=process_id,
                message=f"time_model.scaling_basis '{scaling_basis}' not found in inputs or outputs",
                field_path="time_model.scaling_basis",
                fix_hint=f"Add '{scaling_basis}' to inputs or outputs, or change scaling_basis to an existing item_id"
            ))

    # Rule 2: energy_model scaling_basis exists
    if energy_model and energy_model.get('type') == 'per_unit':
        scaling_basis = energy_model.get('scaling_basis')
        if scaling_basis and scaling_basis not in all_item_ids:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="scaling_basis_not_found",
                entity_type="process",
                entity_id=process_id,
                message=f"energy_model.scaling_basis '{scaling_basis}' not found in inputs or outputs",
                field_path="energy_model.scaling_basis",
                fix_hint=f"Add '{scaling_basis}' to inputs or outputs, or change scaling_basis"
            ))

    # Rule 3: No setup_hr in continuous processes
    if process_type == "continuous" and time_model:
        setup_hr = time_model.get("setup_hr")
        if setup_hr is not None and setup_hr > 0:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="setup_hr_in_continuous",
                entity_type="process",
                entity_id=process_id,
                message="Continuous processes cannot have setup_hr (use process_type: batch instead)",
                field_path="time_model.setup_hr",
                fix_hint="Remove setup_hr or change process_type to 'batch'"
            ))

    # Rule 4: Positive values
    if time_model:
        if time_model.get('rate') is not None and time_model['rate'] <= 0:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="non_positive_value",
                entity_type="process",
                entity_id=process_id,
                message=f"time_model.rate must be > 0, got {time_model['rate']}",
                field_path="time_model.rate",
                fix_hint="Set rate to a positive value"
            ))

        if time_model.get('hr_per_batch') is not None and time_model['hr_per_batch'] <= 0:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="non_positive_value",
                entity_type="process",
                entity_id=process_id,
                message=f"time_model.hr_per_batch must be > 0, got {time_model['hr_per_batch']}",
                field_path="time_model.hr_per_batch",
                fix_hint="Set hr_per_batch to a positive value"
            ))

    if energy_model:
        if energy_model.get('value') is not None and energy_model['value'] < 0:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="negative_value",
                entity_type="process",
                entity_id=process_id,
                message=f"energy_model.value must be >= 0, got {energy_model['value']}",
                field_path="energy_model.value",
                fix_hint="Set value to a non-negative value"
            ))

    # Rule 5: Compound unit format
    if time_model and time_model.get('rate_unit'):
        rate_unit = time_model['rate_unit']
        try:
            parse_compound_unit(rate_unit)
        except ValueError as e:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="semantic",
                rule="invalid_compound_unit",
                entity_type="process",
                entity_id=process_id,
                message=f"time_model.rate_unit '{rate_unit}' is not a valid compound unit: {e}",
                field_path="time_model.rate_unit",
                fix_hint="Use format 'numerator/denominator' (e.g., 'kg/hr', 'L/min')"
            ))

    if energy_model and energy_model.get('unit'):
        energy_unit = energy_model['unit']
        em_type = energy_model.get('type')

        # per_unit requires compound unit, fixed_per_batch does not
        if em_type == 'per_unit':
            try:
                parse_compound_unit(energy_unit)
            except ValueError as e:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="semantic",
                    rule="invalid_compound_unit",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"energy_model.unit '{energy_unit}' is not a valid compound unit: {e}",
                    field_path="energy_model.unit",
                    fix_hint="Use format 'energy/scaling' (e.g., 'kWh/kg', 'MJ/unit')"
                ))
        else:
            # fixed_per_batch should be simple energy unit
            if "/" in energy_unit:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="semantic",
                    rule="compound_unit_in_fixed",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"energy_model type 'fixed_per_batch' should use simple unit, got '{energy_unit}'",
                    field_path="energy_model.unit",
                    fix_hint="Use simple energy unit (e.g., 'kWh', 'MJ') for fixed_per_batch"
                ))

    # Rule 6: Known units
    if time_model and time_model.get('rate_unit'):
        try:
            numerator, denominator = parse_compound_unit(time_model['rate_unit'])
            if not is_valid_unit(numerator):
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="semantic",
                    rule="unknown_unit",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Unknown unit in rate_unit numerator: '{numerator}'",
                    field_path="time_model.rate_unit",
                    fix_hint=f"Use a known unit instead of '{numerator}'"
                ))
            if not is_valid_unit(denominator):
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    category="semantic",
                    rule="unknown_unit",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Unknown unit in rate_unit denominator: '{denominator}'",
                    field_path="time_model.rate_unit",
                    fix_hint=f"Use a known time unit instead of '{denominator}'"
                ))
        except ValueError:
            pass  # Already caught by compound unit format check

    return issues


# =============================================================================
# Unit Conversion Validation (Category 3)
# =============================================================================

def validate_process_unit_conversion(
    process: Any,
    converter: UnitConverter
) -> List[ValidationIssue]:
    """
    Validate unit conversion requirements.

    Rules:
    - scaling_basis unit convertible to rate_unit numerator (ERROR)
    - Density available when needed (ERROR)
    - mass_kg available when needed (ERROR)
    """
    issues = []
    process_id = _get_entity_id(process)

    # Get as dict if it's a Pydantic model
    if hasattr(process, 'model_dump'):
        process_dict = process.model_dump()
    else:
        process_dict = process

    time_model = process_dict.get('time_model')
    energy_model = process_dict.get('energy_model')

    # Build item_id -> Quantity mapping
    items_map = {}
    for inp in process_dict.get('inputs', []) or []:
        if inp.get('item_id'):
            items_map[inp['item_id']] = inp
    for out in process_dict.get('outputs', []) or []:
        if out.get('item_id'):
            items_map[out['item_id']] = out

    # Rule 1: time_model scaling_basis convertibility
    if time_model and time_model.get('type') == 'linear_rate':
        scaling_basis = time_model.get('scaling_basis')
        rate_unit = time_model.get('rate_unit')

        if scaling_basis and rate_unit and scaling_basis in items_map:
            try:
                rate_numerator, _ = parse_compound_unit(rate_unit)
                scaling_item = items_map[scaling_basis]
                scaling_unit = scaling_item.get('unit')

                if scaling_unit and scaling_unit != rate_numerator:
                    # Check if conversion is possible
                    can_convert = converter.can_convert(
                        scaling_unit,
                        rate_numerator,
                        scaling_basis
                    )

                    if not can_convert:
                        issues.append(ValidationIssue(
                            level=ValidationLevel.ERROR,
                            category="unit_conversion",
                            rule="conversion_not_possible",
                            entity_type="process",
                            entity_id=process_id,
                            message=(
                                f"Cannot convert scaling_basis unit '{scaling_unit}' "
                                f"to rate_unit numerator '{rate_numerator}' for item '{scaling_basis}'"
                            ),
                            field_path="time_model.scaling_basis",
                            fix_hint=(
                                f"Add density (for mass<->volume) or mass_kg (for count<->mass) "
                                f"to item '{scaling_basis}', or change units to match"
                            )
                        ))
            except ValueError:
                pass  # Invalid rate_unit, already caught by semantic validation

    # Rule 2: energy_model scaling_basis convertibility
    if energy_model and energy_model.get('type') == 'per_unit':
        scaling_basis = energy_model.get('scaling_basis')
        energy_unit = energy_model.get('unit')

        if scaling_basis and energy_unit and scaling_basis in items_map:
            try:
                _, per_unit = parse_compound_unit(energy_unit)
                scaling_item = items_map[scaling_basis]
                scaling_unit = scaling_item.get('unit')

                if scaling_unit and scaling_unit != per_unit:
                    # Check if conversion is possible
                    can_convert = converter.can_convert(
                        scaling_unit,
                        per_unit,
                        scaling_basis
                    )

                    if not can_convert:
                        issues.append(ValidationIssue(
                            level=ValidationLevel.ERROR,
                            category="unit_conversion",
                            rule="conversion_not_possible",
                            entity_type="process",
                            entity_id=process_id,
                            message=(
                                f"Cannot convert energy scaling_basis unit '{scaling_unit}' "
                                f"to energy unit denominator '{per_unit}' for item '{scaling_basis}'"
                            ),
                            field_path="energy_model.scaling_basis",
                            fix_hint=(
                                f"Add density (for mass<->volume) or mass_kg (for count<->mass) "
                                f"to item '{scaling_basis}', or change units to match"
                            )
                        ))
            except ValueError:
                pass  # Invalid energy_unit, already caught by semantic validation

    return issues


# =============================================================================
# Cross-Model Validation (Category 4)
# =============================================================================

def validate_process_cross_model(process: Any) -> List[ValidationIssue]:
    """
    Validate consistency across time and energy models.

    Rules:
    - Energy-time scaling_basis compatibility (WARNING)
    - Batch process consistency (WARNING)
    """
    issues = []
    process_id = _get_entity_id(process)

    # Get as dict if it's a Pydantic model
    if hasattr(process, 'model_dump'):
        process_dict = process.model_dump()
    else:
        process_dict = process

    process_type = process_dict.get('process_type')
    time_model = process_dict.get('time_model')
    energy_model = process_dict.get('energy_model')

    # Rule 1: Energy-time scaling_basis compatibility
    if time_model and energy_model:
        tm_scaling = time_model.get('scaling_basis')
        em_scaling = energy_model.get('scaling_basis')

        if tm_scaling and em_scaling and tm_scaling != em_scaling:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="cross_model",
                rule="different_scaling_basis",
                entity_type="process",
                entity_id=process_id,
                message=(
                    f"time_model and energy_model use different scaling_basis: "
                    f"'{tm_scaling}' vs '{em_scaling}'"
                ),
                field_path="energy_model.scaling_basis",
                fix_hint="Verify this is intentional, or align scaling_basis for consistency"
            ))

    # Rule 2: Batch process with per-unit energy
    if process_type == "batch" and energy_model:
        if energy_model.get('type') == 'per_unit':
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="cross_model",
                rule="per_unit_energy_with_batch",
                entity_type="process",
                entity_id=process_id,
                message="Batch process uses per-unit energy (expected fixed_per_batch)",
                field_path="energy_model.type",
                fix_hint="Verify this is correct, or change to 'fixed_per_batch' for batch processes"
            ))

    return issues


# =============================================================================
# Reference Validation (Category 6)
# =============================================================================

def validate_process_references(
    process: Any,
    converter: UnitConverter
) -> List[ValidationIssue]:
    """
    Validate that all referenced entities (items, resources, materials) exist in KB.

    Category 6: Reference Validation (ADR-017)

    Args:
        process: Process to validate (Process model or dict)
        converter: UnitConverter (provides access to kb via converter.kb)

    Returns:
        List of validation issues
    """
    issues = []
    process_dict = process if isinstance(process, dict) else process.model_dump()
    process_id = process_dict.get('id', 'unknown')
    kb = converter.kb

    # Check if this is a template process (skip reference validation if so)
    is_template = process_dict.get('is_template', False)
    if is_template:
        # Template processes are allowed to reference undefined items
        return issues

    # Rule 1: Input/output items exist (WARNING)
    # Check all item_id in inputs, outputs, byproducts
    for input_item in process_dict.get('inputs', []) or []:
        item_id = input_item.get('item_id')
        if item_id:
            # Check if item exists in KB
            item = kb.get_item(item_id)
            if not item:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="reference",
                    rule="input_item_not_found",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Input item '{item_id}' not found in KB (may be import or to-be-created)",
                    field_path=f"inputs[item_id={item_id}]",
                    fix_hint=f"Create item definition for '{item_id}' or mark process with is_template: true if this is a template"
                ))

    for output_item in process_dict.get('outputs', []) or []:
        item_id = output_item.get('item_id')
        if item_id:
            item = kb.get_item(item_id)
            if not item:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="reference",
                    rule="output_item_not_found",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Output item '{item_id}' not found in KB (may be import or to-be-created)",
                    field_path=f"outputs[item_id={item_id}]",
                    fix_hint=f"Create item definition for '{item_id}' or mark process with is_template: true if this is a template"
                ))

    for byproduct_item in process_dict.get('byproducts', []) or []:
        item_id = byproduct_item.get('item_id')
        if item_id:
            item = kb.get_item(item_id)
            if not item:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="reference",
                    rule="byproduct_item_not_found",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Byproduct item '{item_id}' not found in KB (may be import or to-be-created)",
                    field_path=f"byproducts[item_id={item_id}]",
                    fix_hint=f"Create item definition for '{item_id}' or mark process with is_template: true if this is a template"
                ))

    # Rule 2: Resource machines exist (WARNING)
    # Check all machine_id in resource_requirements
    for resource_req in process_dict.get('resource_requirements', []) or []:
        machine_id = resource_req.get('machine_id')
        if machine_id:
            # Check if machine exists in KB
            machine = kb.get_item(machine_id)
            if not machine:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="reference",
                    rule="resource_machine_not_found",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"Resource machine '{machine_id}' not found in KB",
                    field_path=f"resource_requirements[machine_id={machine_id}]",
                    fix_hint=f"Create machine definition for '{machine_id}'"
                ))

    return issues


# =============================================================================
# Main Validator
# =============================================================================

def validate_process(
    process: Any,
    converter: Optional[UnitConverter] = None
) -> List[ValidationIssue]:
    """
    Validate a process with all validation rules.

    Args:
        process: Process to validate (Process model or dict)
        converter: Optional UnitConverter for unit conversion validation

    Returns:
        List of validation issues
    """
    issues = []

    # Schema validation (always run)
    issues.extend(validate_process_schema(process))

    # Semantic validation (always run)
    issues.extend(validate_process_semantics(process))

    # Unit conversion validation (requires converter)
    if converter:
        issues.extend(validate_process_unit_conversion(process, converter))

    # Cross-model validation (always run)
    issues.extend(validate_process_cross_model(process))

    # Reference validation (requires converter for KB access)
    if converter:
        issues.extend(validate_process_references(process, converter))

    return issues


def validate_recipe_inputs_outputs(
    recipe: Any,
    kb: Any
) -> List[ValidationIssue]:
    """
    Validate recipe inputs/outputs are resolvable (ADR-018).

    Checks if recipe has explicit inputs/outputs OR can infer them from
    process steps. Generates ERROR if neither is available.

    Args:
        recipe: Recipe to validate (Recipe model or dict)
        kb: KB loader with access to processes

    Returns:
        List of validation issues
    """
    issues = []
    recipe_id = _get_entity_id(recipe)

    # Get as dict if it's a Pydantic model
    if hasattr(recipe, 'model_dump'):
        recipe_dict = recipe.model_dump()
    else:
        recipe_dict = recipe

    recipe_inputs = recipe_dict.get("inputs", [])
    recipe_outputs = recipe_dict.get("outputs", [])
    steps = recipe_dict.get("steps", [])

    # Check if inputs resolvable
    if not recipe_inputs:
        # Check if ANY step has inputs (explicit or from process)
        has_step_inputs = False
        for step in steps:
            # Check step-level inputs first
            step_inputs = step.get("inputs", [])
            if step_inputs:
                has_step_inputs = True
                break

            # Check if process has inputs
            process_id = step.get("process_id")
            if process_id:
                process = kb.get_process(process_id)
                if process:
                    # Get as dict if Pydantic model
                    if hasattr(process, 'model_dump'):
                        process_dict = process.model_dump()
                    else:
                        process_dict = process

                    # Boundary processes are allowed to have no inputs (extract from environment)
                    if process_dict.get("process_type") == "boundary":
                        has_step_inputs = True
                        break

                    # Template processes are allowed to have no inputs (inputs defined in recipe)
                    if process_dict.get("is_template"):
                        has_step_inputs = True
                        break

                    if process_dict.get("inputs", []):
                        has_step_inputs = True
                        break

        if not has_step_inputs:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="recipe",
                rule="recipe_inputs_not_resolvable",
                entity_type="recipe",
                entity_id=recipe_id,
                message="Recipe has no resolvable inputs (neither explicit at recipe level nor from steps/processes)",
                field_path="inputs",
                fix_hint="Add inputs: [...] to recipe, or ensure referenced processes have inputs defined"
            ))

    # Check if outputs resolvable
    if not recipe_outputs:
        has_step_outputs = False
        for step in steps:
            # Check step-level outputs first
            step_outputs = step.get("outputs", [])
            if step_outputs:
                has_step_outputs = True
                break

            # Check if process has outputs
            process_id = step.get("process_id")
            if process_id:
                process = kb.get_process(process_id)
                if process:
                    # Get as dict if Pydantic model
                    if hasattr(process, 'model_dump'):
                        process_dict = process.model_dump()
                    else:
                        process_dict = process

                    # Boundary processes must have outputs (checked in process validation)
                    if process_dict.get("process_type") == "boundary":
                        has_step_outputs = True
                        break

                    # Template processes are allowed to have no outputs (outputs defined in recipe)
                    if process_dict.get("is_template"):
                        has_step_outputs = True
                        break

                    if process_dict.get("outputs", []):
                        has_step_outputs = True
                        break

        if not has_step_outputs:
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="recipe",
                rule="recipe_outputs_not_resolvable",
                entity_type="recipe",
                entity_id=recipe_id,
                message="Recipe has no resolvable outputs (neither explicit at recipe level nor from steps/processes)",
                field_path="outputs",
                fix_hint="Add outputs: [...] to recipe, or ensure referenced processes have outputs defined"
            ))

    # Check target_item_id in outputs (WARNING)
    target_item_id = recipe_dict.get("target_item_id")
    if target_item_id and recipe_outputs:
        target_found = any(
            out.get("item_id") == target_item_id
            for out in recipe_outputs
        )

        if not target_found:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="recipe",
                rule="recipe_outputs_missing_target",
                entity_type="recipe",
                entity_id=recipe_id,
                message=f"Recipe outputs don't include target_item_id '{target_item_id}'",
                field_path="outputs",
                fix_hint=f"Add output with item_id: {target_item_id}"
            ))

    return issues


def validate_recipe(
    recipe: Any,
    converter: Optional[UnitConverter] = None
) -> List[ValidationIssue]:
    """
    Validate a recipe.

    Args:
        recipe: Recipe to validate (Recipe model or dict)
        converter: Optional UnitConverter for reference validation (KB access)

    Returns:
        List of validation issues
    """
    issues = []
    recipe_id = _get_entity_id(recipe)

    # Get as dict if it's a Pydantic model
    if hasattr(recipe, 'model_dump'):
        recipe_dict = recipe.model_dump()
    else:
        recipe_dict = recipe

    # Rule: target_item_id required
    if not recipe_dict.get('target_item_id'):
        issues.append(ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="target_item_id_required",
            entity_type="recipe",
            entity_id=recipe_id,
            message="Missing required field 'target_item_id'",
            field_path="target_item_id",
            fix_hint="Add target_item_id"
        ))

    # Rule: steps must be non-empty
    steps = recipe_dict.get('steps', []) or []
    if not steps:
        issues.append(ValidationIssue(
            level=ValidationLevel.WARNING,
            category="schema",
            rule="empty_steps",
            entity_type="recipe",
            entity_id=recipe_id,
            message="Recipe has no steps",
            field_path="steps",
            fix_hint="Add process steps to recipe"
        ))

    # Rule: Each step must have process_id
    for i, step in enumerate(steps):
        if not step.get('process_id'):
            issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="missing_process_id",
                entity_type="recipe",
                entity_id=recipe_id,
                message=f"Step {i} missing required field 'process_id'",
                field_path=f"steps[{i}].process_id",
                fix_hint="Add process_id to step"
            ))

    # Reference validation: process_id must exist (ERROR - ADR-017 Category 6 Rule 3)
    if converter:
        kb = converter.kb
        for i, step in enumerate(steps):
            process_id = step.get('process_id')
            if process_id:
                # Check if process exists in KB
                process = kb.get_process(process_id)
                if not process:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        category="reference",
                        rule="process_not_found",
                        entity_type="recipe",
                        entity_id=recipe_id,
                        message=f"Step {i} references process '{process_id}' which does not exist in KB",
                        field_path=f"steps[{i}].process_id",
                        fix_hint=f"Create process definition for '{process_id}' or correct the process_id"
                    ))

        # ADR-018: Validate recipe inputs/outputs are resolvable
        inputs_outputs_issues = validate_recipe_inputs_outputs(recipe, kb)
        issues.extend(inputs_outputs_issues)

    return issues
