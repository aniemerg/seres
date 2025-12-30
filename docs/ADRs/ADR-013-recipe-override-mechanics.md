# ADR-013: Recipe Override Mechanics

**Status:** Proposed
**Date:** 2024-12-28
**Decision Makers:** Project team
**Related ADRs:** ADR-012 (Process Types and Time Model), ADR-014 (Energy Model), ADR-016 (Unit Conversion)

## Context

The knowledge base has **multiple sources** for process timing and energy consumption that can conflict. Additionally, the current override mechanism (`est_time_hr`) is underspecified and insufficient for the level of detail required.

### Current State

**Recipe step fields (current):**
```yaml
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0        # Simple float - underspecified
    machine_hours: 2.0       # Relationship unclear
    labor_hours: 0.5         # Concurrent or sequential?
    inputs: [...]
    outputs: [...]
```

**Problems with current approach:**

1. **Underspecified** - `est_time_hr` is just a number with no context
2. **No parametrization** - Can't specify rate changes, setup time, scaling basis
3. **Limited override** - Can only override total time, not the calculation model
4. **No energy override** - No equivalent for energy_model
5. **Ambiguous semantics** - Is it an estimate, requirement, or override?

### Real Conflict Example

Investigation found a **15× discrepancy** in `recipe_crushed_ore_v0`:

**Recipe:**
```yaml
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0  # ← Simple override
    inputs:
      - item_id: regolith_lunar_mare
        qty: 100.0
        unit: kg
```

**Process:**
```yaml
process_id: crushing_basic_v0
time_model:
  type: linear_rate
  rate: 3.33
  rate_unit: kg/hr
  scaling_basis: regolith_lunar_mare
```

**Calculated:** 100 kg / 3.33 kg/hr = **30 hours**
**Recipe says:** **2 hours**

**Current limitations:**
- Can't express "this recipe uses a faster method (50 kg/hr)" with `est_time_hr`
- Can't override energy model at all
- Can't specify different scaling basis
- Can only override the final number

### User Requirements

**From feedback:**
> "we should migrate from 'est_time_hr' to using time_models directly in the recipe step as an override"
> "We will want to migrate away from 'est_time_hr' to providing an actual time model in the override."
> "overrides should be so complete it should be possible to fully re-define the process"
> "a process time model is the default for that process, overrideable by a recipe. When there is a conflict, the recipe will control."

## Decision

We will implement a **Flexible Override Model** where recipe steps can either partially modify or completely redefine process behavior:

### 1. Override Modes: Complete vs Partial

Recipe steps support **two override modes** determined by the presence of the `type` field:

#### Mode 1: Complete Override (type specified)

When `type` is specified, **all required fields must be provided** - this completely replaces the process model:

```yaml
steps:
  - process_id: crushing_basic_v0
    # Complete override (type specified)
    time_model:
      type: linear_rate        # ← Type specified = complete override
      rate: 50.0               # All required fields must be present
      rate_unit: kg/hr
      scaling_basis: regolith_lunar_mare
      notes: "Optimized crushing for this recipe"

    # Complete energy override
    energy_model:
      type: per_unit           # ← Type specified = complete override
      value: 0.2
      unit: kWh/kg
      scaling_basis: regolith_lunar_mare
      notes: "Pre-sorted material requires less energy"
```

**Use when:** Completely redefining the process (different type, different scaling, etc.)

#### Mode 2: Partial Override (type omitted)

When `type` is NOT specified, **only changed fields are provided** - other fields merge from process default:

```yaml
steps:
  - process_id: crushing_basic_v0
    # Partial override (type omitted)
    time_model:
      rate: 50.0               # ← Only override rate
      # type, rate_unit, scaling_basis inherited from process

    # Partial energy override
    energy_model:
      value: 0.2               # ← Only override energy value
      # type, unit, scaling_basis inherited from process
```

**Use when:** Tweaking specific parameters while keeping process structure

**Override rule:** If `type` field is present → complete override (all required fields). If `type` field is absent → partial merge (specified fields override, others inherit).

### 2. Core Precedence Rules

#### For Time

**Precedence (highest to lowest):**
1. Recipe step `time_model` (if specified) - **OVERRIDE** (complete or partial based on `type` field)
2. Process `time_model` (if recipe doesn't override)
3. Error if neither available

**Override resolution:**
- If recipe `time_model.type` is specified → **Complete override** (use recipe model entirely)
- If recipe `time_model.type` is NOT specified → **Partial merge** (merge recipe fields into process model)

#### For Energy

**Precedence (highest to lowest):**
1. Recipe step `energy_model` (if specified) - **OVERRIDE** (complete or partial based on `type` field)
2. Process `energy_model` (if recipe doesn't override)
3. Warning if neither available (energy optional)

**Override resolution:**
- If recipe `energy_model.type` is specified → **Complete override** (use recipe model entirely)
- If recipe `energy_model.type` is NOT specified → **Partial merge** (merge recipe fields into process model)

**Rationale:**
- Recipe authors know their specific use case
- **Complete override** when changing fundamental structure (type, scaling basis)
- **Partial override** for simple parameter tweaks (just changing rate)
- Flexible yet explicit (presence of `type` signals intent)
- Industry standard (manufacturing ERP systems use override model)
- User directive: "When there is a conflict, the recipe will control"

### 3. Resource Consumption Semantics

Clarify the meaning of `machine_hours` and `labor_hours`:

**Definitions:**
- `time_model` (process or recipe): **Governs machine time usage** - quantifies duration
- `machine_hours`: **Additional machine resource consumption** beyond process requirements
- `labor_hours`: **Labor resource consumption** concurrent with step execution

**User directive:**
> "We need to bring harmony to these fields and usage. The key is that we are attempting to account for resource usage."
> "labor_hours should be concurrent with the step of the process"
> "any sequential labor should be it's own step"

**Interpretation:**

```yaml
# Process defines base machines
process_id: metal_forming_v0
requires_ids:
  - hydraulic_press_v0
time_model:
  type: batch
  hr_per_batch: 2.0

# Recipe step adds concurrent labor
steps:
  - process_id: metal_forming_v0
    # Uses process time_model (2.0 hr)
    # Already uses: hydraulic_press_v0 (from process)

    # Additional concurrent resources
    labor_hours: 0.5         # 0.25 worker × 2 hr (intermittent)
    labor_machine_id: labor_bot_general_v0  # Which machine provides labor
```

**Accounting:**
- Process uses `hydraulic_press_v0` for 2 hours (from process requirements)
- Recipe adds `labor_bot_general_v0` for 0.5 machine-hours (concurrent, intermittent)
- Total elapsed time: 2 hours
- Total machine-hours: 2.0 (press) + 0.5 (labor) = 2.5

**Sequential labor as separate step:**
```yaml
steps:
  # Setup step (pure labor)
  - process_id: mold_setup_v0
    time_model:
      type: batch
      hr_per_batch: 0.5

  # Forming step (press + concurrent labor)
  - process_id: metal_forming_v0
    labor_hours: 0.5
```

### 4. Override Examples and Use Cases

#### Use Case 1: Recipe-Specific Optimization

**Process (generic):**
```yaml
process_id: crushing_basic_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: regolith
energy_model:
  type: per_unit
  value: 0.5
  unit: kWh/kg
  scaling_basis: regolith
```

**Recipe (optimized method):**
```yaml
steps:
  - process_id: crushing_basic_v0
    # Override: Pre-sorted material crushes faster
    time_model:
      type: linear_rate
      rate: 20.0  # 2× faster than generic
      rate_unit: kg/hr
      scaling_basis: regolith_lunar_mare_presorted
      notes: "Pre-sorted regolith crushes faster"

    # Override: Less energy needed
    energy_model:
      type: per_unit
      value: 0.3  # 40% less energy
      unit: kWh/kg
      scaling_basis: regolith_lunar_mare_presorted
      notes: "Pre-sorting reduces crushing energy"
```

**Why:** This recipe has pre-sorted the regolith, making crushing more efficient.

**Note:** This is a **complete override** (type specified) - all fields must be provided.

#### Use Case 2: Partial Override (Simple Rate Change)

**Process (generic):**
```yaml
process_id: crushing_basic_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: regolith
```

**Recipe (just change rate):**
```yaml
steps:
  - process_id: crushing_basic_v0
    # Partial override: only change rate
    time_model:
      rate: 50.0  # ← No type specified = partial override
      # type, rate_unit, scaling_basis inherited from process
```

**Result after merge:**
```yaml
# Effective time_model for this recipe step
time_model:
  type: linear_rate      # ← From process
  rate: 50.0             # ← From recipe override
  rate_unit: kg/hr       # ← From process
  scaling_basis: regolith  # ← From process
```

**Why:** This recipe only needs a faster rate - everything else stays the same. Partial override is more concise.

**Note:** This is a **partial override** (type omitted) - only changed fields specified.

#### Use Case 3: Different Scaling Basis

**Process (generic):**
```yaml
process_id: water_electrolysis_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 0.5
  rate_unit: kg/hr
  scaling_basis: water  # Scales on water input
```

**Recipe (output-focused):**
```yaml
steps:
  - process_id: water_electrolysis_v0
    # Override: This recipe cares about H2 output rate
    time_model:
      type: linear_rate
      rate: 0.055  # kg H2 per hour
      rate_unit: kg/hr
      scaling_basis: hydrogen_gas  # Scales on H2 output!
      notes: "Process specified in terms of H2 production rate"
```

**Why:** This recipe specifies production in terms of hydrogen output, not water input.

#### Use Case 3: Batch vs Continuous Override

**Process (continuous):**
```yaml
process_id: ceramic_forming_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 5.0
  rate_unit: kg/hr
  scaling_basis: ceramic_powder
```

**Recipe (batch operation):**
```yaml
steps:
  - process_id: ceramic_forming_v0
    # Override: This recipe uses batch operation
    process_type: batch  # Can even override process type!
    time_model:
      type: batch
      setup_hr: 0.5  # Mold setup
      hr_per_batch: 2.0
      notes: "Using batch molds instead of continuous extrusion"

    outputs:
      - item_id: ceramic_part_set
        qty: 10.0  # 1 batch = 10 kg
        unit: kg
```

**Why:** This recipe uses a different manufacturing method (batch molds vs continuous extrusion).

#### Use Case 4: Complex Multi-Parameter Change

**Process (generic):**
```yaml
process_id: aluminum_smelting_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 50.0
  rate_unit: kg/hr
  scaling_basis: aluminum_pure
energy_model:
  type: per_unit
  value: 50.0
  unit: kWh/kg
  scaling_basis: aluminum_pure
```

**Recipe (high-purity variant):**
```yaml
steps:
  - process_id: aluminum_smelting_v0
    # Override: High-purity aluminum requires more time and energy
    time_model:
      type: linear_rate
      rate: 30.0  # Slower rate
      rate_unit: kg/hr
      scaling_basis: aluminum_high_purity
      notes: "High-purity smelting requires longer residence time"

    energy_model:
      type: per_unit
      value: 60.0  # More energy
      unit: kWh/kg
      scaling_basis: aluminum_high_purity
      notes: "High-purity requires higher current density"
```

**Why:** High-purity aluminum requires different process parameters.

### 5. Validation Rules

#### Override Validation

When recipe provides override:

**1. Schema validation:**
- time_model override must match TimeModel schema (from ADR-012)
- energy_model override must match EnergyModel schema (from ADR-014)
- All required fields present (rate, rate_unit, scaling_basis for continuous, etc.)

**2. Consistency validation:**
- scaling_basis must refer to actual input/output in this recipe step
- Units must be convertible
- Type (batch/continuous) must be valid for the process

**3. Comparison to process default (optional warning):**
```python
if recipe.time_model and process.time_model:
    # Calculate both for comparison
    recipe_duration = calculate_time(recipe.time_model, inputs)
    process_duration = calculate_time(process.time_model, inputs)

    if abs(recipe_duration - process_duration) / process_duration > 0.5:
        logger.warning(
            f"Recipe time_model override differs significantly from process: "
            f"{recipe_duration:.1f}hr vs {process_duration:.1f}hr"
        )
```

**Note:** This is a WARNING, not an error. Recipe is allowed to override significantly.

#### Error Conditions

**Error (blocks execution):**
- Process has no time_model AND recipe has no time_model override
- time_model override has invalid schema
- scaling_basis references non-existent item

**Warning (logged, execution continues):**
- Recipe override differs significantly from process default (>50%)
- Energy model missing (if energy tracking enabled)

**Info (logged):**
- Using recipe time_model override
- Using process time_model (no override)

## Consequences

### Positive

1. **Complete flexibility** - Recipe can fully redefine how process works
2. **Clear semantics** - Full model specification, not just a number
3. **Parametric overrides** - Can change rate, scaling basis, even process type
4. **Validation power** - Can validate complete models, catch errors
5. **Handles complexity** - Multi-parameter changes possible
6. **Documentation** - Override model self-documents the change
7. **User requirement** - Implements "overrides should be so complete it should be possible to fully re-define the process"

### Negative

1. **Verbosity** - Override is more verbose than simple `est_time_hr: 2.0`
2. **Migration complexity** - Converting `est_time_hr` to full time_model requires analysis
3. **Duplication risk** - Recipe may duplicate process model unnecessarily
4. **Learning curve** - Recipe authors must understand time_model schema

### Neutral

1. **Migration required** - All `est_time_hr` fields need conversion
2. **Validation critical** - Must validate both process and recipe models
3. **Documentation needed** - When to override vs when to fix process

## When to Use Recipe Overrides

### Use Override When:

1. **Recipe-specific optimization** - This recipe has a faster/better method
   ```yaml
   time_model:  # Override for pre-sorted material
     rate: 20.0  # vs process default 10.0
   ```

2. **Different scaling** - Recipe cares about different input/output
   ```yaml
   time_model:  # Override to scale on output instead of input
     scaling_basis: hydrogen_gas  # vs process default: water
   ```

3. **Different method** - Recipe uses different manufacturing approach
   ```yaml
   process_type: batch  # Override from continuous to batch
   time_model:
     type: batch
     hr_per_batch: 2.0
   ```

4. **Multi-parameter change** - Several process parameters differ
   ```yaml
   time_model:  # Different rate AND scaling
     rate: 30.0
     scaling_basis: aluminum_high_purity
   energy_model:  # Different energy too
     value: 60.0
   ```

### DON'T Use Override When:

1. **Process is generic and works** - Don't override unnecessarily
   ```yaml
   # ✗ BAD: Redundant override
   time_model:  # Identical to process default
     rate: 10.0
     rate_unit: kg/hr
     scaling_basis: regolith

   # ✓ GOOD: Use process default
   # (no time_model field in recipe)
   ```

2. **Process is wrong** - Fix the process, don't override everywhere
   ```yaml
   # ✗ BAD: Overriding to fix wrong process
   time_model:  # Every recipe needs this override
     rate: 30.0  # Process says 2.0 but it's really 30.0

   # ✓ GOOD: Fix the process definition instead
   ```

3. **Simple quantity scaling** - Process model already handles this
   ```yaml
   # ✗ BAD: Overriding just to scale
   inputs:
     - item_id: regolith
       qty: 1000.0  # ← Just change quantity
   time_model:  # Don't need this
     rate: 10.0  # Same as process

   # ✓ GOOD: Process model scales automatically
   inputs:
     - item_id: regolith
       qty: 1000.0
   # time_model calculated: 1000/10 = 100hr
   ```

## Migration Strategy

### Phase 1: Schema Extension

1. **Add override fields to RecipeStep schema:**
```python
class RecipeStep:
    process_id: str
    inputs: list[RecipeStepInput]
    outputs: list[RecipeStepOutput]

    # Model overrides (NEW)
    process_type: Optional[str] = None       # Can override process type
    time_model: Optional[TimeModel] = None   # Full time_model override
    energy_model: Optional[EnergyModel] = None  # Full energy_model override

    # Resource specifications (existing, clarified)
    machine_hours: Optional[float] = None    # Additional machine consumption
    labor_hours: Optional[float] = None      # Labor consumption
    labor_machine_id: Optional[str] = None   # Which machine provides labor (NEW)

    # Legacy field (DEPRECATED)
    est_time_hr: Optional[float] = None      # Will be migrated away

    notes: Optional[str] = None
```

2. **Validate both schemas:**
- Process time_model validated per ADR-012
- Recipe time_model override validated per ADR-012
- Recipe scaling_basis must match recipe inputs/outputs

### Phase 2: Convert est_time_hr to time_model

**Automated conversion (simple cases):**

```yaml
# OLD: Simple time override
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0
    inputs:
      - item_id: regolith
        qty: 100.0
        unit: kg

# Analysis: Process is continuous, 100kg input, 2hr specified
# Process default: 100kg / 10 kg/hr = 10hr
# Recipe: 2hr
# Implied rate: 100kg / 2hr = 50 kg/hr

# NEW: Full time_model override
steps:
  - process_id: crushing_basic_v0
    time_model:  # Auto-converted
      type: linear_rate
      rate: 50.0  # Calculated from est_time_hr
      rate_unit: kg/hr
      scaling_basis: regolith  # Inferred from inputs
      notes: "Migrated from est_time_hr: 2.0"
    inputs:
      - item_id: regolith
        qty: 100.0
        unit: kg
```

**Manual conversion (complex cases):**

Cases requiring human review:
- Multiple possible scaling bases
- Batch vs continuous ambiguity
- Energy model also needs override
- Setup time implications

**Migration script pseudocode:**
```python
def migrate_est_time_hr(recipe_step, process):
    """Convert est_time_hr to time_model override."""

    if recipe_step.est_time_hr is None:
        return None  # No override needed

    # Get process time_model
    process_time_model = process.time_model
    if process_time_model is None:
        # Can't infer, needs manual review
        enqueue_for_manual_review(recipe_step)
        return None

    # Calculate implied rate
    if process_time_model.type == "linear_rate":
        # Find scaling item
        scaling_item = infer_scaling_basis(recipe_step, process)
        if scaling_item is None:
            enqueue_for_manual_review(recipe_step)
            return None

        # Calculate implied rate
        quantity = get_quantity(recipe_step, scaling_item)
        implied_rate = quantity / recipe_step.est_time_hr

        # Create override
        return TimeModel(
            type="linear_rate",
            rate=implied_rate,
            rate_unit=f"{scaling_item.unit}/hr",
            scaling_basis=scaling_item.item_id,
            notes=f"Migrated from est_time_hr: {recipe_step.est_time_hr}"
        )

    elif process_time_model.type == "batch":
        # Batch process: est_time_hr might mean hr_per_batch
        # Or it might be for multiple batches
        # Needs analysis
        enqueue_for_manual_review(recipe_step)
        return None
```

### Phase 3: Deprecation Timeline

**Month 1-2:** Schema extension, dual support
- Support both `est_time_hr` and `time_model` override
- Prefer `time_model` if both present
- Log warnings for `est_time_hr` usage

**Month 3-4:** Migration
- Run automated conversion
- Enqueue manual reviews for complex cases
- Agents fix queued items

**Month 5-6:** Deprecation
- Error if `est_time_hr` used without `time_model`
- Remove `est_time_hr` from schema

### Phase 4: Validation Rollout

1. **Indexer integration** - Validate all time_model and energy_model overrides
2. **Generate work queue** - Enqueue issues for agent fixing
3. **Incremental fixes** - Agents fix recipe steps one by one

## Implementation Details

### Override Resolution Function

```python
def get_time_model(process: Process, recipe_step: RecipeStep) -> TimeModel:
    """Get time_model using override precedence with complete/partial support."""

    # 1. Recipe override takes precedence
    if recipe_step.time_model is not None:
        # Check if complete override (type specified) or partial (type omitted)
        if hasattr(recipe_step.time_model, 'type') and recipe_step.time_model.type is not None:
            # COMPLETE OVERRIDE: type specified
            logger.info(
                f"Using recipe time_model COMPLETE override for {process.id}"
            )

            # Validate as complete model
            validate_time_model(recipe_step.time_model, recipe_step)

            return recipe_step.time_model
        else:
            # PARTIAL OVERRIDE: type omitted, merge with process
            logger.info(
                f"Using recipe time_model PARTIAL override for {process.id}"
            )

            if process.time_model is None:
                raise ValueError(
                    f"Cannot use partial override: process {process.id} has no time_model to merge with"
                )

            # Merge: start with process model, override with recipe fields
            merged_model = copy.deepcopy(process.time_model)

            # Override fields that are specified in recipe
            for field, value in recipe_step.time_model.items():
                if value is not None:  # Only override non-None fields
                    setattr(merged_model, field, value)

            # Validate merged model
            validate_time_model(merged_model, recipe_step)

            return merged_model

    # 2. Process default
    if process.time_model is not None:
        logger.info(
            f"Using process time_model for {process.id}"
        )
        return process.time_model

    # 3. No time model available
    raise ValueError(
        f"Process {process.id} has no time_model and "
        f"recipe step has no time_model override"
    )

def get_energy_model(process: Process, recipe_step: RecipeStep) -> Optional[EnergyModel]:
    """Get energy_model using override precedence with complete/partial support."""

    # 1. Recipe override takes precedence
    if recipe_step.energy_model is not None:
        # Check if complete override (type specified) or partial (type omitted)
        if hasattr(recipe_step.energy_model, 'type') and recipe_step.energy_model.type is not None:
            # COMPLETE OVERRIDE: type specified
            logger.info(
                f"Using recipe energy_model COMPLETE override for {process.id}"
            )

            # Validate as complete model
            validate_energy_model(recipe_step.energy_model, recipe_step)

            return recipe_step.energy_model
        else:
            # PARTIAL OVERRIDE: type omitted, merge with process
            logger.info(
                f"Using recipe energy_model PARTIAL override for {process.id}"
            )

            if process.energy_model is None:
                logger.warning(
                    f"Cannot use partial override: process {process.id} has no energy_model to merge with"
                )
                return None

            # Merge: start with process model, override with recipe fields
            merged_model = copy.deepcopy(process.energy_model)

            # Override fields that are specified in recipe
            for field, value in recipe_step.energy_model.items():
                if value is not None:  # Only override non-None fields
                    setattr(merged_model, field, value)

            # Validate merged model
            validate_energy_model(merged_model, recipe_step)

            return merged_model

    # 2. Process default
    if process.energy_model is not None:
        logger.info(
            f"Using process energy_model for {process.id}"
        )
        return process.energy_model

    # 3. No energy model (optional)
    logger.warning(
        f"Process {process.id} has no energy_model and "
        f"recipe step has no energy_model override"
    )
    return None
```

### Validation Implementation

```python
def validate_recipe_override(
    process: Process,
    recipe_step: RecipeStep
) -> list[ValidationError]:
    """Validate recipe time_model and energy_model overrides."""
    errors = []

    # Validate time_model override if present
    if recipe_step.time_model is not None:
        # Schema validation
        time_errors = validate_time_model_schema(recipe_step.time_model)
        errors.extend(time_errors)

        # Semantic validation (scaling_basis exists in THIS recipe step)
        if recipe_step.time_model.type == "linear_rate":
            all_items = [i.item_id for i in recipe_step.inputs] + \
                       [o.item_id for o in recipe_step.outputs]

            if recipe_step.time_model.scaling_basis not in all_items:
                errors.append(ValidationError(
                    f"Recipe step time_model.scaling_basis "
                    f"'{recipe_step.time_model.scaling_basis}' "
                    f"not found in recipe step inputs or outputs"
                ))

        # Comparison to process (warning only)
        if process.time_model:
            try:
                recipe_dur = calculate_time(recipe_step.time_model, recipe_step.inputs)
                process_dur = calculate_time(process.time_model, recipe_step.inputs)

                if abs(recipe_dur - process_dur) / process_dur > 0.5:
                    errors.append(ValidationError(
                        f"Recipe time_model override differs significantly: "
                        f"{recipe_dur:.1f}hr vs process {process_dur:.1f}hr",
                        severity="warning"
                    ))
            except CalculationError:
                pass  # Can't compare

    # Validate energy_model override if present
    if recipe_step.energy_model is not None:
        # Similar validation as time_model
        energy_errors = validate_energy_model_schema(recipe_step.energy_model)
        errors.extend(energy_errors)

        # Semantic validation
        if recipe_step.energy_model.type == "per_unit":
            all_items = [i.item_id for i in recipe_step.inputs] + \
                       [o.item_id for o in recipe_step.outputs]

            if recipe_step.energy_model.scaling_basis not in all_items:
                errors.append(ValidationError(
                    f"Recipe step energy_model.scaling_basis "
                    f"'{recipe_step.energy_model.scaling_basis}' "
                    f"not found in recipe step inputs or outputs"
                ))

    return errors
```

## Examples

### Example 1: No Override (Use Process Default)

**Recipe:**
```yaml
steps:
  - process_id: regolith_crushing_grinding_v0
    # No time_model - will use process default
    inputs:
      - item_id: regolith_coarse_fraction
        qty: 100.0
        unit: kg
```

**Process:**
```yaml
process_id: regolith_crushing_grinding_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: regolith_coarse_fraction
```

**Result:**
- Use process time_model
- Duration: 100 kg / 10 kg/hr = **10 hours**
- Log: "Using process time_model for regolith_crushing_grinding_v0"

### Example 2: Partial Override (Simple Rate Change)

**Recipe:**
```yaml
steps:
  - process_id: crushing_basic_v0
    # Partial override: only change rate
    time_model:
      rate: 50.0  # ← No type = partial override
      # Other fields inherited from process

    inputs:
      - item_id: regolith_lunar_mare
        qty: 100.0
        unit: kg
```

**Process:**
```yaml
process_id: crushing_basic_v0
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: regolith
```

**Result (merged):**
```yaml
# Effective time_model after merge
time_model:
  type: linear_rate      # ← Inherited from process
  rate: 50.0             # ← Overridden from recipe
  rate_unit: kg/hr       # ← Inherited from process
  scaling_basis: regolith  # ← Inherited from process
```

**Execution:**
- Merge recipe override with process default
- Duration: 100 kg / 50 kg/hr = **2 hours**
- Log: "Using recipe time_model PARTIAL override for crushing_basic_v0"
- Warning: "Recipe time_model differs significantly: 2.0hr vs process 10.0hr"

### Example 3: Complete Redefinition

**Recipe:**
```yaml
steps:
  - process_id: aluminum_smelting_v0
    # Completely redefine for high-purity variant
    time_model:
      type: linear_rate
      rate: 30.0  # Slower
      rate_unit: kg/hr
      scaling_basis: aluminum_high_purity
      notes: "High-purity requires longer residence time"

    energy_model:
      type: per_unit
      value: 60.0  # More energy
      unit: kWh/kg
      scaling_basis: aluminum_high_purity
      notes: "High-purity requires higher current density"

    inputs:
      - item_id: alumina_high_purity
        qty: 50.0
        unit: kg
    outputs:
      - item_id: aluminum_high_purity
        qty: 26.0  # Different yield
        unit: kg
```

**Process (generic smelting):**
```yaml
time_model:
  type: linear_rate
  rate: 50.0
  rate_unit: kg/hr
energy_model:
  type: per_unit
  value: 50.0
  unit: kWh/kg
```

**Result:**
- Use recipe overrides for both time and energy
- Duration: 26 kg / 30 kg/hr = **0.87 hours**
- Energy: 26 kg × 60 kWh/kg = **1560 kWh**
- Completely different from process defaults

### Example 4: Batch Method Override

**Recipe:**
```yaml
steps:
  - process_id: ceramic_forming_v0
    # Override: Use batch molds instead of continuous extrusion
    process_type: batch  # Override process type!
    time_model:
      type: batch
      setup_hr: 0.5
      hr_per_batch: 2.0
      notes: "Using batch molds for precision parts"

    outputs:
      - item_id: ceramic_part_precision
        qty: 10.0  # 1 batch = 10 kg
        unit: kg
```

**Process (continuous extrusion):**
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: 5.0
  rate_unit: kg/hr
```

**Result:**
- Use recipe overrides
- 100 kg needed → 10 batches
- Duration: 10 × (0.5 + 2.0) = **25 hours**
- Completely different method than process default

## References

- User feedback: `design/time-model-hierarchy-feedback.txt`
- Override analysis: `design/override-hierarchy-problems.md`
- Design synthesis: `design/feedback-synthesis-and-next-steps.md`
- Parallel ADRs: ADR-012 (Time Model), ADR-014 (Energy Model)

## Related Decisions

- **ADR-012:** Time model schema - defines what can be overridden
- **ADR-014:** Energy model schema - defines energy override structure
- **ADR-015:** Resource accounting and labor harmonization
- **ADR-016:** Unit conversion system
- **ADR-017:** Validation and error detection

## Approval

- [ ] Architecture review
- [ ] Implementation team review
- [ ] Migration strategy approved
- [ ] est_time_hr deprecation timeline approved
