# 017: Validation and Error Detection Strategy

**Status:** Proposed
**Date:** 2024-12-28
**Decision Makers:** Project team
**Related ADRs:** 012 (Process Types), 014 (Energy Model), 016 (Unit Conversion), 013 (Recipe Overrides)

## Context

The knowledge base has grown to ~891 processes, hundreds of recipes, thousands of items, and extensive interconnected data. With the new schemas from 012, 014, and 016, we need a comprehensive validation strategy to:

1. **Catch errors early** - Detect schema violations, missing data, and inconsistencies at index time
2. **Enable agent fixes** - Generate actionable work items for automated fixing
3. **Ensure simulation readiness** - Validate that time_model and energy_model can be calculated
4. **Maintain data quality** - Prevent invalid data from entering the KB
5. **Support incremental improvement** - Allow soft warnings for missing-but-not-critical fields

### Current Validation

The indexer (`src/indexer/indexer.py`) currently validates:
- **Missing fields** - Soft warnings for missing energy_model, time_model, material_class, etc.
- **Null values** - Detects null qty, amount fields
- **Unresolved references** - Tracks requires_text and other unresolved strings
- **Missing recipes** - Items without recipes
- **Recipe inputs** - Recipes with no inputs in any step
- **Orphan resources** - Resource types with no provider machine

### New Validation Needs

With 012, 014, and 016, we now need:
1. **Schema validation** - Enforce new time_model and energy_model schemas
2. **Type consistency** - process_type matches time_model.type
3. **Unit convertibility** - scaling_basis can convert to rate_unit
4. **Field requirements** - Required fields present based on type
5. **Cross-model validation** - Energy-time coupling checks
6. **Override validation** - Recipe overrides are valid and complete/partial correctly

### User Requirements

From `design/time-model-hierarchy-feedback.txt`:
- "We will want the indexer to verify that a time model can be correctly evaluated or needs to be corrected by an agent"
- "changes to the spec will be detected by indexing in the future and enqueue for work to fix"
- "A key principle is fixing definitions, detecting gaps or issues, and creating work for future agents to fix in accordance to specifications"
- "All processes should have a time model"
- "KB should fully be validated and checked against the schema or errors should be emitted (or work enqueued) or simulations should fail"

## Decision

We will implement a **comprehensive, layered validation system** with the following components:

## Updates

**2026-01-01:** Indexer queue generation skips `no_recipe` gaps for items marked `is_scrap: true` so byproducts do not enqueue recipe work.

**2026-01-25:** Mass-balance fixes must not change discrete item outputs to `kg` or
use fractional `unit` quantities for `unit_kind: discrete` items. Prefer bulk
material inputs and explicit scrap/byproduct outputs to close mass, or adjust the
item’s `mass`/`mass_kg` to match the recipe.

### 1. Validation Levels

Define three severity levels for validation issues:

| Level | Name | Meaning | Action |
|-------|------|---------|--------|
| **ERROR** | Hard Error | Schema violation, cannot be used in simulation | Block simulation, emit error, enqueue fix |
| **WARNING** | Soft Warning | Missing recommended field, may affect quality | Emit warning, enqueue fix, allow use |
| **INFO** | Informational | Suggestion for improvement | Log only, no action required |

**Examples:**
- ERROR: `process_type: continuous` but `time_model.type: batch` (inconsistent)
- WARNING: `time_model` missing entirely (recommended but not required yet)
- INFO: Process has no notes field (helpful but optional)

### 2. Validation Categories

Organize validation into logical categories:

#### Category 1: Schema Validation
**Purpose:** Ensure data conforms to defined schemas

**Rules:**
1. **process_type required** (ERROR)
   - Every process must have `process_type: batch | continuous`
   - Missing or invalid value → ERROR

2. **time_model.type consistency** (ERROR)
   - `process_type: continuous` requires `time_model.type: linear_rate`
   - `process_type: batch` requires `time_model.type: batch`
   - Mismatch → ERROR

3. **energy_model.type consistency** (ERROR)
   - Valid types: `per_unit`, `fixed_per_batch`
   - Invalid or unknown type → ERROR

4. **Required fields present** (ERROR)
   - For `time_model.type: linear_rate` → requires `rate`, `rate_unit`, `scaling_basis`
   - For `time_model.type: batch` → requires `hr_per_batch`
   - For `energy_model.type: per_unit` → requires `value`, `unit`, `scaling_basis`
   - Missing required field → ERROR

5. **No deprecated fields** (ERROR)
   - Reject `rate_kg_per_hr`, `hr_per_kg`, `kWh_per_kg`, `fixed_time`
   - Presence of deprecated field → ERROR with migration hint

6. **Field types correct** (ERROR)
   - `rate` must be numeric > 0
   - `hr_per_batch` must be numeric > 0
   - `scaling_basis` must be string
   - Type mismatch → ERROR

#### Category 2: Semantic Validation
**Purpose:** Ensure data makes logical sense

**Rules:**
1. **scaling_basis exists** (ERROR)
   - `scaling_basis` must refer to actual input or output `item_id`
   - Not found → ERROR

2. **No setup_hr in continuous** (ERROR)
   - `process_type: continuous` cannot have `setup_hr`
   - Presence → ERROR (suggests batch type)

3. **Positive values** (ERROR)
   - `rate`, `hr_per_batch`, `setup_hr`, `value` must be > 0
   - Zero or negative → ERROR

4. **Compound unit format** (ERROR)
   - `rate_unit` must be "X/Y" format (e.g., "kg/hr")
   - `energy_model.unit` must be "X/Y" format (e.g., "kWh/kg")
   - Invalid format → ERROR

5. **Known units** (ERROR)
   - Numerator and denominator must be recognized units
   - Unknown unit → ERROR

6. **Time denominators** (WARNING)
   - Rate units should use /hr, /min, /day (not /s or uncommon)
   - Non-standard time unit → WARNING (still allowed, flagged for review)

#### Category 3: Unit Conversion Validation
**Purpose:** Ensure unit conversions are possible (016 integration)

**Rules:**
1. **scaling_basis convertibility** (ERROR)
   - Scaling basis item unit must convert to rate_unit numerator
   - Conversion requires: direct factor, density (mass↔volume), or mass_kg (count↔mass)
   - Cannot convert → ERROR

2. **Density available** (ERROR if needed)
   - If scaling_basis is volume and rate_unit is mass (or vice versa), material must have density
   - Missing density → ERROR

3. **mass_kg available** (ERROR if needed)
   - If scaling_basis is count and rate_unit is mass (or vice versa), item must have mass_kg
   - Missing mass_kg → ERROR

4. **Energy scaling_basis convertibility** (ERROR)
   - Same rules as time_model for energy_model scaling_basis
   - Cannot convert → ERROR

#### Category 4: Cross-Model Validation
**Purpose:** Ensure time and energy models are consistent

**Rules:**
1. **Energy-time coupling** (WARNING)
   - If both time_model and energy_model present, should have compatible scaling_basis
   - Different scaling_basis → WARNING (may be intentional)

2. **Power reasonableness** (INFO)
   - If both models present, implicit power = energy / time
   - Unusually high or low power → INFO (flag for review)
   - Example: 1000 kWh for 0.1 hr = 10 MW (very high, flag)

3. **Batch consistency** (ERROR)
   - If `process_type: batch`, energy_model should be `fixed_per_batch` or scale appropriately
   - Per-unit energy with batch time → WARNING (ensure it's correct)

#### Category 5: Recipe Override Validation
**Purpose:** Ensure recipe overrides are valid (013 integration)

**Rules:**
1. **Complete override valid** (ERROR)
   - If recipe step has `time_model.type`, must have all required fields for that type
   - Missing required field → ERROR

2. **Partial override valid** (ERROR)
   - If recipe step has time_model fields but no `type`, process must have time_model to merge with
   - Process missing time_model → ERROR

3. **Override fields recognized** (ERROR)
   - All fields in recipe time_model/energy_model must be valid schema fields
   - Unknown field → ERROR

4. **Override process exists** (ERROR)
   - Recipe step `process_id` must exist in KB
   - Missing process → ERROR

#### Category 6: Reference Validation
**Purpose:** Ensure all referenced entities exist

**Rules:**
1. **Input/output items exist** (WARNING)
   - All `item_id` in inputs, outputs, byproducts should exist in KB
   - Missing → WARNING (may be import or to-be-created)

2. **Resource types exist** (WARNING)
   - All `resource_type` in resource_requirements should exist
   - Missing → WARNING

3. **Process references exist** (ERROR)
   - Recipe step `process_id` must exist
   - Missing → ERROR

4. **Material class exists** (WARNING)
   - Items with `material_class` should reference known material
   - Unknown → WARNING

### 3. Validation Implementation

**Architecture:**

```
Indexer (src/indexer/indexer.py)
    ↓
Validator (new: src/kb_core/validators.py)
    ↓
Validation Rules (modular)
    - schema_validator.py
    - semantic_validator.py
    - unit_validator.py
    - cross_model_validator.py
    - override_validator.py
    ↓
Validation Report (out/validation_report.json)
    ↓
Work Queue (out/work_queue.jsonl)
```

**Core Validator Interface:**

```python
from typing import List, Dict, Optional
from enum import Enum

class ValidationLevel(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

class ValidationError:
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

class Validator:
    """Main validation coordinator."""

    def __init__(self, kb_loader, unit_converter):
        self.kb = kb_loader
        self.converter = unit_converter
        self.validators = [
            SchemaValidator(kb_loader),
            SemanticValidator(kb_loader),
            UnitValidator(kb_loader, unit_converter),
            CrossModelValidator(kb_loader),
            OverrideValidator(kb_loader),
        ]

    def validate_process(self, process: dict) -> List[ValidationError]:
        """Validate a single process."""
        errors = []
        for validator in self.validators:
            errors.extend(validator.validate_process(process))
        return errors

    def validate_recipe(self, recipe: dict) -> List[ValidationError]:
        """Validate a single recipe."""
        errors = []
        for validator in self.validators:
            errors.extend(validator.validate_recipe(recipe))
        return errors

    def validate_all(self, entries: Dict[str, dict]) -> Dict[str, List[ValidationError]]:
        """Validate all KB entries."""
        results = {}
        for entry_id, entry in entries.items():
            kind = entry.get("kind")
            if kind == "process":
                errors = self.validate_process(entry)
            elif kind == "recipe":
                errors = self.validate_recipe(entry)
            else:
                errors = []

            if errors:
                results[entry_id] = errors

        return results
```

**Schema Validator Example:**

```python
class SchemaValidator:
    """Validates schema compliance."""

    def __init__(self, kb_loader):
        self.kb = kb_loader

    def validate_process(self, process: dict) -> List[ValidationError]:
        errors = []
        process_id = process.get("id", "unknown")

        # Rule 1: process_type required
        process_type = process.get("process_type")
        if not process_type:
            errors.append(ValidationError(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="process_type_required",
                entity_type="process",
                entity_id=process_id,
                message="Missing required field 'process_type'",
                field_path="process_type",
                fix_hint="Add 'process_type: batch' or 'process_type: continuous'"
            ))
            return errors  # Can't validate further

        if process_type not in ["batch", "continuous"]:
            errors.append(ValidationError(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="process_type_invalid",
                entity_type="process",
                entity_id=process_id,
                message=f"Invalid process_type '{process_type}'. Must be 'batch' or 'continuous'",
                field_path="process_type",
                fix_hint="Set to 'batch' or 'continuous'"
            ))

        # Rule 2: time_model.type consistency
        time_model = process.get("time_model")
        if time_model:
            tm_type = time_model.get("type")

            if process_type == "continuous" and tm_type != "linear_rate":
                errors.append(ValidationError(
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
                errors.append(ValidationError(
                    level=ValidationLevel.ERROR,
                    category="schema",
                    rule="time_model_type_mismatch",
                    entity_type="process",
                    entity_id=process_id,
                    message=f"process_type 'batch' requires time_model.type 'batch', got '{tm_type}'",
                    field_path="time_model.type",
                    fix_hint="Change time_model.type to 'batch' or change process_type"
                ))

        # Rule 3: Required fields for time_model
        if time_model and tm_type == "linear_rate":
            for field in ["rate", "rate_unit", "scaling_basis"]:
                if field not in time_model or time_model[field] is None:
                    errors.append(ValidationError(
                        level=ValidationLevel.ERROR,
                        category="schema",
                        rule="required_field_missing",
                        entity_type="process",
                        entity_id=process_id,
                        message=f"time_model.type 'linear_rate' requires field '{field}'",
                        field_path=f"time_model.{field}",
                        fix_hint=f"Add time_model.{field}"
                    ))

        # Rule 5: No deprecated fields
        deprecated_fields = {
            "rate_kg_per_hr": "Use 'rate: X' and 'rate_unit: kg/hr'",
            "hr_per_kg": "Use 'rate: X' and 'rate_unit: kg/hr' (invert rate)",
            "kWh_per_kg": "Use energy_model with 'unit: kWh/kg'",
            "fixed_time": "Use 'type: batch' with 'hr_per_batch'"
        }

        if time_model:
            for deprecated, hint in deprecated_fields.items():
                if deprecated in time_model:
                    errors.append(ValidationError(
                        level=ValidationLevel.ERROR,
                        category="schema",
                        rule="deprecated_field",
                        entity_type="process",
                        entity_id=process_id,
                        message=f"Deprecated field 'time_model.{deprecated}' used",
                        field_path=f"time_model.{deprecated}",
                        fix_hint=hint
                    ))

        return errors
```

### 4. Validation Outputs

**Output 1: Validation Report (JSON)**

```json
{
  "summary": {
    "total_entities": 1500,
    "entities_validated": 1500,
    "total_errors": 45,
    "total_warnings": 120,
    "total_info": 30,
    "error_entities": 32,
    "warning_entities": 98
  },
  "errors_by_category": {
    "schema": 20,
    "semantic": 10,
    "unit_conversion": 8,
    "cross_model": 5,
    "override": 2
  },
  "errors_by_rule": {
    "process_type_required": 5,
    "time_model_type_mismatch": 8,
    "scaling_basis_not_found": 7,
    "conversion_not_possible": 8,
    "deprecated_field": 12
  },
  "issues": [
    {
      "level": "error",
      "category": "schema",
      "rule": "time_model_type_mismatch",
      "entity_type": "process",
      "entity_id": "crushing_basic_v0",
      "message": "process_type 'continuous' requires time_model.type 'linear_rate', got 'batch'",
      "field_path": "time_model.type",
      "fix_hint": "Change time_model.type to 'linear_rate' or change process_type"
    }
  ]
}
```

**Output 2: Work Queue Items**

For each ERROR-level validation issue, generate work queue item:

```json
{
  "id": "validation_error_crushing_basic_v0_001",
  "priority": "schema_error",
  "type": "validation_fix",
  "entity_type": "process",
  "entity_id": "crushing_basic_v0",
  "file": "kb/processes/crushing_basic_v0.yaml",
  "validation_error": {
    "rule": "time_model_type_mismatch",
    "message": "process_type 'continuous' requires time_model.type 'linear_rate', got 'batch'",
    "field_path": "time_model.type",
    "fix_hint": "Change time_model.type to 'linear_rate' or change process_type"
  },
  "suggested_fix": {
    "field": "time_model.type",
    "old_value": "batch",
    "new_value": "linear_rate"
  },
  "created_at": "2024-12-28T10:30:00Z"
}
```

### 5. Integration with Indexer

**Modified indexer flow:**

```python
def build_index() -> Dict[str, dict]:
    """Build KB index with validation."""
    # 1. Load all KB files
    entries = load_all_kb_files()

    # 2. Initialize validator
    kb_loader = KBLoader()
    unit_converter = UnitConverter(kb_loader)
    validator = Validator(kb_loader, unit_converter)

    # 3. Validate all entries
    validation_results = validator.validate_all(entries)

    # 4. Generate validation report
    report = generate_validation_report(validation_results)
    write_json(OUT_DIR / "validation_report.json", report)

    # 5. Generate work queue items for errors
    work_items = generate_work_queue_items(validation_results)
    append_to_work_queue(work_items)

    # 6. Return index (include validation status)
    for entry_id, errors in validation_results.items():
        entry = entries[entry_id]
        entry["validation_status"] = "invalid" if has_errors(errors) else "valid"
        entry["validation_errors"] = len([e for e in errors if e.level == ValidationLevel.ERROR])
        entry["validation_warnings"] = len([e for e in errors if e.level == ValidationLevel.WARNING])

    return entries
```

### 6. Runtime Validation (Simulation)

**Simulation should validate before execution:**

```python
def execute_process(process_id: str, inputs: dict) -> ProcessResult:
    """Execute a process with runtime validation."""
    process = kb.get_process(process_id)

    # Runtime validation
    errors = validator.validate_process(process)

    # Check for errors
    error_list = [e for e in errors if e.level == ValidationLevel.ERROR]
    if error_list:
        raise ValidationException(
            f"Process {process_id} has validation errors and cannot be executed",
            errors=error_list
        )

    # Validate inputs can be converted
    if process.time_model and process.time_model.type == "linear_rate":
        scaling_item = inputs.get(process.time_model.scaling_basis)
        if not scaling_item:
            raise ValidationException(
                f"scaling_basis '{process.time_model.scaling_basis}' not in inputs"
            )

        # Check conversion possible
        rate_num, _ = parse_compound_unit(process.time_model.rate_unit)
        if not converter.can_convert(scaling_item.unit, rate_num, scaling_item.item_id):
            raise ValidationException(
                f"Cannot convert {scaling_item.unit} to {rate_num} for time calculation. "
                f"Add density or mass_kg to item definition."
            )

    # Proceed with execution
    return execute_process_internal(process, inputs)
```

## Consequences

### Positive

1. **Early error detection** - Issues found at index time, not runtime
2. **Clear error messages** - Specific, actionable feedback with fix hints
3. **Automated fixes** - Work queue enables agent-driven corrections
4. **Incremental improvement** - Warnings allow gradual quality improvements
5. **Simulation reliability** - Runtime validation prevents execution errors
6. **Comprehensive coverage** - All new schema features validated
7. **Modular design** - Easy to add new validation rules
8. **Quality metrics** - Validation report tracks KB quality over time

### Negative

1. **Indexing overhead** - Validation adds processing time
2. **Complexity** - More code to maintain
3. **Work queue volume** - May generate many items initially
4. **False positives** - Some warnings may not be actual issues
5. **Migration burden** - Existing KB will have many errors initially

### Neutral

1. **Validation strictness** - Can tune ERROR vs WARNING levels
2. **Performance** - May need caching for large KBs
3. **User feedback** - Error messages need user testing

## Migration Strategy

### Phase 1: Implement Validators (Week 1)

1. **Create validator infrastructure**
   - `src/kb_core/validators.py` - Core validator
   - `ValidationError` class
   - `ValidationLevel` enum

2. **Implement rule validators**
   - `SchemaValidator` - Schema compliance
   - `SemanticValidator` - Logical consistency
   - `UnitValidator` - Unit conversion checks
   - `CrossModelValidator` - Time-energy coupling
   - `OverrideValidator` - Recipe override validation

3. **Add tests**
   - Unit tests for each validator
   - Integration tests with sample KB data

### Phase 2: Integrate with Indexer (Week 1-2)

1. **Modify indexer**
   - Call validator after loading
   - Generate validation report
   - Append work queue items

2. **Update outputs**
   - `out/validation_report.json`
   - `out/work_queue.jsonl` (append validation items)

### Phase 3: Initial Validation Run (Week 2)

1. **Run indexer on full KB**
   - Generate initial validation report
   - Identify error/warning counts
   - Categorize issues

2. **Tune validation levels**
   - Review ERROR vs WARNING assignments
   - Adjust for false positives
   - Add exceptions if needed

### Phase 4: Agent Fixes (Weeks 3-6)

1. **Process work queue**
   - Agents consume validation_fix items
   - Fix schema errors
   - Add missing data

2. **Incremental improvement**
   - Run indexer periodically
   - Track error reduction
   - Adjust rules based on findings

### Phase 5: Runtime Validation (Week 7)

1. **Add to simulation**
   - Validate processes before execution
   - Validate recipes before use
   - Clear error messages on failure

2. **Testing**
   - Test with valid and invalid data
   - Verify error messages helpful
   - Ensure no false positives

## Examples

### Example 1: Process Type Mismatch

**Invalid YAML:**
```yaml
id: crushing_basic_v0
process_type: continuous  # ← Says continuous
time_model:
  type: batch             # ← But has batch time model!
  hr_per_batch: 2.0
```

**Validation Error:**
```json
{
  "level": "error",
  "category": "schema",
  "rule": "time_model_type_mismatch",
  "entity_type": "process",
  "entity_id": "crushing_basic_v0",
  "message": "process_type 'continuous' requires time_model.type 'linear_rate', got 'batch'",
  "field_path": "time_model.type",
  "fix_hint": "Change time_model.type to 'linear_rate' or change process_type to 'batch'"
}
```

### Example 2: Missing scaling_basis

**Invalid YAML:**
```yaml
id: water_processing_v0
process_type: continuous
inputs:
  - item_id: water
    qty: 10.0
    unit: L
time_model:
  type: linear_rate
  rate: 5.0
  rate_unit: kg/hr
  # ← Missing scaling_basis!
```

**Validation Error:**
```json
{
  "level": "error",
  "category": "schema",
  "rule": "required_field_missing",
  "entity_type": "process",
  "entity_id": "water_processing_v0",
  "message": "time_model.type 'linear_rate' requires field 'scaling_basis'",
  "field_path": "time_model.scaling_basis",
  "fix_hint": "Add time_model.scaling_basis (e.g., 'water')"
}
```

### Example 3: Unit Conversion Impossible

**Invalid YAML:**
```yaml
id: assembly_v0
process_type: continuous
inputs:
  - item_id: widget  # widget has no mass_kg defined!
    qty: 10.0
    unit: unit
time_model:
  type: linear_rate
  rate: 50.0
  rate_unit: kg/hr  # ← Needs to convert unit → kg
  scaling_basis: widget
```

**Validation Error:**
```json
{
  "level": "error",
  "category": "unit_conversion",
  "rule": "conversion_not_possible",
  "entity_type": "process",
  "entity_id": "assembly_v0",
  "message": "Cannot convert scaling_basis unit 'unit' to rate_unit numerator 'kg'. Item 'widget' has no mass_kg field.",
  "field_path": "time_model.scaling_basis",
  "fix_hint": "Add 'mass_kg' field to item 'widget' or change rate_unit to 'unit/hr'"
}
```

### Example 4: Deprecated Field

**Invalid YAML:**
```yaml
id: old_process_v0
process_type: continuous
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # ← Deprecated!
```

**Validation Error:**
```json
{
  "level": "error",
  "category": "schema",
  "rule": "deprecated_field",
  "entity_type": "process",
  "entity_id": "old_process_v0",
  "message": "Deprecated field 'time_model.rate_kg_per_hr' used",
  "field_path": "time_model.rate_kg_per_hr",
  "fix_hint": "Use 'rate: 10.0' and 'rate_unit: kg/hr'"
}
```

## Validation Rules Summary

| Category | Rule | Level | Description |
|----------|------|-------|-------------|
| Schema | process_type_required | ERROR | process_type field must exist |
| Schema | process_type_invalid | ERROR | process_type must be batch or continuous |
| Schema | time_model_type_mismatch | ERROR | time_model.type must match process_type |
| Schema | required_field_missing | ERROR | Required fields for type must be present |
| Schema | deprecated_field | ERROR | Old schema fields not allowed |
| Schema | field_type_invalid | ERROR | Field value has wrong type |
| Semantic | scaling_basis_not_found | ERROR | scaling_basis not in inputs/outputs |
| Semantic | setup_hr_in_continuous | ERROR | Continuous processes can't have setup_hr |
| Semantic | negative_value | ERROR | Rates, times must be positive |
| Semantic | invalid_compound_unit | ERROR | rate_unit format must be "X/Y" |
| Semantic | unknown_unit | ERROR | Unit not recognized |
| Semantic | nonstandard_time_unit | WARNING | Uncommon time denominator |
| Unit | conversion_not_possible | ERROR | scaling_basis unit can't convert to rate_unit |
| Unit | density_missing | ERROR | Mass↔volume conversion needs density |
| Unit | mass_kg_missing | ERROR | Count↔mass conversion needs mass_kg |
| Cross-model | energy_time_scaling_mismatch | WARNING | Different scaling_basis in time/energy |
| Cross-model | power_unreasonable | INFO | Calculated power very high/low |
| Cross-model | batch_energy_type_mismatch | WARNING | Batch process with per-unit energy |
| Override | complete_override_incomplete | ERROR | Complete override missing required fields |
| Override | partial_override_no_base | ERROR | Partial override but process has no base model |
| Override | override_unknown_field | ERROR | Override field not in schema |
| Override | override_process_missing | ERROR | Recipe references non-existent process |

## References

- 012: Process types and time model (validation rules lines 93-113)
- 014: Energy model redesign (validation rules)
- 016: Unit conversion system (conversion validation)
- 013: Recipe override mechanics (override validation)
- Current indexer: `src/indexer/indexer.py`
- User feedback: `design/time-model-hierarchy-feedback.txt`

## Related Decisions

- **012:** Time model schema defines validation rules
- **014:** Energy model schema defines validation rules
- **016:** Unit conversion defines convertibility validation
- **013:** Recipe overrides define override validation

## Approval

- [ ] Architecture review
- [ ] Implementation team review
- [ ] Migration strategy approved
- [ ] Test plan approved
