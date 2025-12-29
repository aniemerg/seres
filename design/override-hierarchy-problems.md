# Override Hierarchy Problems

**Status:** In Progress
**Date:** 2024-12-28
**Purpose:** Define precedence rules for time specifications and resolve conflicts

## Overview

The knowledge base has **multiple sources** of time specification that can conflict:

1. **Process `time_model`** - Generic time calculation for any use of the process
2. **Recipe step `est_time_hr`** - Specific time for this recipe's use of the process
3. **Recipe step `machine_hours` and `labor_hours`** - Resource consumption alongside time
4. **Simulation defaults** - Fallback when no timing specified

There is **no documented precedence** for these sources. When they conflict, it's unclear which value should be used. The `time-calculation-real-world-examples.md` investigation found a **15× discrepancy** between recipe and calculated timing, exposing this as a critical design problem.

This document analyzes:
- Current state of timing specifications
- Real conflicts found in the KB
- Semantic meaning of each source
- Possible precedence rules
- Validation and consistency strategies

---

## Current State

### Sources of Time Information

#### 1. Process `time_model`

**Location:** `kb/processes/<process_id>.yaml`

**Structure:**
```yaml
time_model:
  type: linear_rate | fixed_time | boundary
  # For linear_rate:
  hr_per_kg: float
  rate_kg_per_hr: float
  setup_hr: float (optional)
  # For fixed_time:
  hr_per_batch: float
```

**Semantic intent (unclear):**
- Generic time calculation for any use of this process?
- Default when recipe doesn't specify?
- Authoritative calculation that should always be used?
- Informational/documentation only?

**Coverage:** ~891 processes have time_model (near 100%)

**Current usage:**
- Indexer validates presence
- Simulation **ignores** time_model, uses agent-provided duration
- Not used for actual time calculation anywhere

#### 2. Recipe Step `est_time_hr`

**Location:** `kb/recipes/<recipe_id>.yaml`

**Structure:**
```yaml
steps:
  - process_id: some_process_v0
    est_time_hr: 20.0
    inputs: [...]
    outputs: [...]
```

**Semantic intent (unclear):**
- Estimated time for this specific use case?
- Override of process time_model?
- Should match calculated time from time_model?
- Informational/documentation only?

**Coverage:** Minority of recipe steps (exact count unknown, see recipe-step-timing-survey.md)

**Current usage:**
- Not used by simulation (duration is agent parameter)
- May be copied to resolved step but not used for calculation

#### 3. Recipe Step `machine_hours` and `labor_hours`

**Location:** `kb/recipes/<recipe_id>.yaml`

**Structure:**
```yaml
steps:
  - process_id: some_process_v0
    est_time_hr: 20.0
    machine_hours: 20.0
    labor_hours: 5.0
```

**Semantic intent (very unclear):**
- Resource consumption alongside elapsed time?
- Concurrent vs sequential usage?
- Is `labor_hours: 5.0` over 20 hours (intermittent) or 5 workers × 1hr each (concurrent)?
- Relationship to `est_time_hr` - should they be consistent?

**Coverage:** Even smaller minority

**Current usage:** Not used by simulation at all

#### 4. Simulation Agent Parameters

**Location:** Base builder agent code

**Current behavior:**
```python
def start_process(self, process_id: str, scale: float, duration_hours: float):
    # Agent provides duration_hours as arbitrary parameter
    # Ignores all KB timing data
```

**Semantic intent:**
- Agent decides timing based on... what?
- No clear rules or calculation
- Completely disconnected from KB data

---

## Conflicts Found

### Example 1: Crushing Ore (15× Discrepancy!)

**Recipe:** `recipe_crushed_ore_v0`
```yaml
inputs:
  - item_id: regolith_lunar_mare
    qty: 100.0
    unit: kg
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0           # ← Recipe says 2 hours
    machine_hours: 2.0
```

**Process:** `crushing_basic_v0`
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 0.3              # ← 0.3 hr/kg = 3.33 kg/hr throughput
  notes: "primary crushing throughput ~3 kg/hr"
```

**Calculated time from time_model:**
- Input: 100 kg
- Rate: 0.3 hr/kg
- Duration: 100 × 0.3 = **30 hours**

**Recipe specifies:** 2 hours

**CONFLICT: 2 hours vs 30 hours (15× discrepancy!)**

**Questions:**
1. Which value is correct?
2. If recipe is correct, why does process have wrong rate?
3. If process is correct, why does recipe have wrong estimate?
4. How should simulation resolve this?

**Possible explanations:**
1. **Recipe is wrong** - Should be 30 hr, not 2 hr
2. **Process rate is wrong** - Should be 0.02 hr/kg (50 kg/hr), not 0.3 hr/kg
3. **Units mismatch** - Recipe assumes different scale or batch size?
4. **Recipe is specific optimization** - This recipe has faster method than generic process
5. **Both are placeholders** - Neither has been properly calibrated

### Example 2: Labor Bot Assembly

**Recipe:** `recipe_labor_bot_basic_v0`
```yaml
steps:
  - process_id: assembly_basic_v0
    est_time_hr: 1.5           # ← Recipe says 1.5 hours
    labor_hours: 1.5
```

**Process:** `assembly_basic_v0`
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 0.5              # ← 0.5 hr/kg = 2 kg/hr
```

**Problem:** Can't calculate time from time_model because:
- Recipe inputs are count-based (1 frame, 2 arms, 4 motors, etc.)
- Process time_model is mass-based (hr_per_kg)
- Items don't have mass_kg defined
- **Calculation is blocked**

**Observation:**
- Recipe provides est_time_hr: 1.5
- This is the **only** source of timing for this step
- Without it, simulation would have no timing info at all

**Implication:** Recipe est_time_hr may be **necessary** when time_model can't calculate.

### Example 3: Thermal Storage System (Partial Specification)

**Recipe:** `recipe_machine_solar_thermal_storage_system_v0`
```yaml
steps:
  - process_id: metal_fabrication_welding_v0
    est_time_hr: 20.0          # ← Has estimate
  - process_id: refractory_casting_v0
    est_time_hr: 8.0           # ← Has estimate
  - process_id: regolith_collection_and_processing_v0
    est_time_hr: 10.0          # ← Has estimate
  - process_id: assembly_process_general_v0
    est_time_hr: 16.0          # ← Has estimate
```

**Observation:**
- Multi-step recipe
- All steps specify est_time_hr
- Clear intention: recipe author wants specific timing

**Question:** Should these override process time_model calculations?

### Example 4: Prepared Material (Appears Consistent)

**Recipe:** `recipe_prepared_material_v0`
```yaml
steps:
  - process_id: material_preparation_basic_v0
    est_time_hr: 0.8
    inputs:
      - item_id: regolith_lunar_mare
        qty: 1.0
        unit: kg
```

**Process:** `material_preparation_basic_v0` (need to check)

**If process has `hr_per_kg: 0.8`:**
- Calculated: 1.0 kg × 0.8 hr/kg = 0.8 hr
- Recipe: 0.8 hr
- **CONSISTENT!**

This is what we'd expect - recipe estimate matches calculation.

---

## Semantic Analysis

### What Does `est_time_hr` Mean?

Three possible interpretations:

#### Interpretation A: Informational Estimate
- `est_time_hr` is documentation/hint only
- Not authoritative
- Simulation should calculate from time_model
- Validation should check they match

**Pros:**
- Single source of truth (time_model)
- Consistent calculations
- Less duplication

**Cons:**
- Why specify it if not used?
- Many recipes have it (effort wasted)
- Doesn't explain 15× conflicts

#### Interpretation B: Override
- `est_time_hr` **overrides** process time_model
- When present, use recipe value
- When absent, calculate from time_model

**Pros:**
- Allows recipe-specific tuning
- Recipe author knows their specific use case
- Explains why conflicts exist (intentional overrides)

**Cons:**
- Two sources of truth
- Can drift out of sync
- Hard to validate
- Why not just fix the process time_model?

#### Interpretation C: Requirement
- `est_time_hr` is **required duration**
- Process must complete in this time (or less)
- Simulation validates it's achievable
- Mismatch is an error

**Pros:**
- Clear constraint semantics
- Validation is meaningful
- Recipe specifies requirements

**Cons:**
- Doesn't match current usage
- Conflicts become hard errors
- What if requirement is unrealistic?

### What Does Process `time_model` Mean?

Three possible interpretations:

#### Interpretation A: Default
- time_model is default when recipe doesn't specify
- Recipe can override with est_time_hr
- Generic fallback for any use

**Pros:**
- Flexible (allows overrides)
- Most processes can have reasonable defaults
- Recipes can specialize

**Cons:**
- Two sources, can diverge
- Which is "correct"?
- Validation is ambiguous

#### Interpretation B: Authoritative Calculation
- time_model is the **calculation formula**
- Always calculate from it
- Recipe est_time_hr should match (documentation only)

**Pros:**
- Single source of truth
- Consistent across all recipes
- Clear validation (est_time_hr should match)

**Cons:**
- Recipe can't specialize
- What if calculation is wrong for specific case?
- Count-based inputs break (can't calculate)

#### Interpretation C: Capacity Constraint
- time_model specifies **minimum possible time**
- Recipe can request longer (e.g., for quality)
- Mismatch where recipe < calculated is error

**Pros:**
- Process defines limits
- Recipe works within constraints
- Clear validation

**Cons:**
- Doesn't match current usage
- Conflicts go the wrong direction (recipe < calculated)

---

## How Other Systems Handle This

### Manufacturing ERP Systems

**Typical approach:**
- **Routing** (like our process): Standard time for operation
- **Work Order** (like our recipe step): Can override standard time
- **Precedence:** Work order wins if specified
- **Validation:** Warning if >50% different from standard

**Implication:** Override model (Interpretation B) is industry standard.

### Simulation Software

**Typical approach:**
- **Process template**: Generic timing formula
- **Instance parameters**: Specific values for this simulation run
- **Precedence:** Instance parameters override template

**Implication:** Override model, instance parameters win.

### Database Systems (Analogy)

**Schema vs Data:**
- Schema defines structure (like time_model)
- Data instances populate it (like recipe est_time_hr)
- You wouldn't "override" schema with data

**Counter-analogy:**
- But process time_model is more like a **function** (calculates time)
- Recipe est_time_hr is like a **cached result** (or override)
- Caches can be stale, overrides can be intentional

---

## Proposed Precedence Rules

### Option 1: Recipe Override (Permissive)

**Rule:**
1. If recipe step has `est_time_hr`, use it
2. Else if process has `time_model`, calculate from it
3. Else error (no timing specified)

**Validation:**
- Warning if `abs(est_time_hr - calculated) / calculated > 0.5` (>50% difference)
- Info log: "Using recipe est_time_hr: 2.0 hr (calculated from time_model would be 30.0 hr)"

**Pros:**
- Allows recipe specialization
- Backward compatible (existing recipes work)
- Handles cases where calculation is impossible (count-based inputs)

**Cons:**
- Two sources can diverge
- No enforcement of consistency
- Hard to know which value is "correct"

### Option 2: Calculate with Validation (Strict)

**Rule:**
1. Always calculate from process `time_model`
2. If recipe has `est_time_hr`, validate it matches (±25% tolerance)
3. If mismatch, error (or warning + use calculated)

**Validation:**
- Error if `abs(est_time_hr - calculated) / calculated > 0.25` (>25% difference)
- Recipe est_time_hr is documentation, must be accurate

**Pros:**
- Single source of truth (time_model)
- Consistent calculations
- Enforces accuracy

**Cons:**
- Breaks recipes with mismatched est_time_hr (found conflicts!)
- Can't handle cases where calculation is impossible
- Less flexible

### Option 3: Hybrid (Recipe If Necessary)

**Rule:**
1. Try to calculate from process `time_model`
2. If calculation succeeds and recipe has `est_time_hr`:
   - Validate they match (±50% tolerance)
   - Use calculated value (ignore est_time_hr)
3. If calculation fails (e.g., count inputs, missing data):
   - Use recipe `est_time_hr` if present
   - Else error

**Validation:**
- Warning if mismatch >50% and calculation possible
- Info if using est_time_hr because calculation impossible

**Pros:**
- Prefers calculation (consistency)
- Falls back to recipe when needed
- Validates when possible

**Cons:**
- Complex logic
- Sometimes uses recipe, sometimes doesn't (confusing)
- Still doesn't fix underlying data issues

### Option 4: Required Consistency (Strictest)

**Rule:**
1. Process `time_model` must be calculable
2. Recipe `est_time_hr` must match calculated (±10% tolerance)
3. Both are required, both must be consistent

**Validation:**
- Error if time_model can't calculate
- Error if est_time_hr mismatches

**Pros:**
- Forces data quality
- No ambiguity
- Clear semantics

**Cons:**
- Breaks existing KB (many processes fail)
- Requires major data cleanup
- Doesn't handle count-based inputs

---

## machine_hours and labor_hours

### Current Usage

```yaml
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0
    machine_hours: 2.0
    labor_hours: 0.5
```

### Questions

1. **What do these mean?**
   - Option A: Resource consumption (2 machine-hours consumed, 0.5 labor-hours consumed)
   - Option B: Resource requirements (need 2 machines for 1 hour, need 0.5 worker for 1 hour)
   - Option C: Concurrent usage (machine runs for 2hr, labor for 0.5hr, but elapsed time is 2hr)

2. **Relationship to est_time_hr?**
   - Should `machine_hours == est_time_hr`? (one machine fully utilized)
   - Should `machine_hours <= est_time_hr`? (machine fraction)
   - Should `machine_hours >= est_time_hr`? (multiple machines)

3. **Real-world interpretation:**
   - Crushing for 2 hours: machine runs continuously (machine_hours = 2.0)
   - Labor checks every 15 min: 8 checks × 4 min = 32 min = 0.5 hr (labor_hours = 0.5)
   - **Elapsed time: 2 hours** (est_time_hr = 2.0)
   - **Concurrent usage:** Machine and labor overlap

### Proposed Semantics

**Define:**
- `est_time_hr`: **Elapsed time** (wall-clock duration)
- `machine_hours`: **Machine utilization** (machine-hours consumed)
- `labor_hours`: **Labor utilization** (labor-hours consumed)

**Relationship:**
- `machine_hours <= est_time_hr × num_machines`
- `labor_hours <= est_time_hr × num_workers`
- Resources can be partial (0.5 worker intermittent) or full (1.0 machine continuous)

**Example:**
```yaml
est_time_hr: 8.0           # 8 hours elapsed
machine_hours: 8.0         # 1 machine × 8 hours (full utilization)
labor_hours: 2.0           # 0.25 worker × 8 hours (intermittent supervision)
```

**Implications for simulation:**
- Advance time by `est_time_hr`
- Consume `machine_hours` from machine capacity
- Consume `labor_hours` from labor capacity
- Scheduling must account for resource availability

---

## Recommendations

### Immediate Actions

1. **Fix the 15× discrepancy in Example 1:**
   - Investigate which value is correct
   - Update either recipe or process to match
   - Add validation to catch future mismatches

2. **Survey all recipe steps with est_time_hr:**
   - Calculate time from time_model where possible
   - Identify mismatches (see recipe-step-timing-survey.md)
   - Quantify problem scope

3. **Fix invalid time_models:**
   - mixing_and_blending_v0 uses `total_time_hr` (invalid)
   - water_electrolysis_v0 should be linear_rate not fixed_time
   - Add schema validation to prevent future errors

### Precedence Rule Decision for ADR-010

**Recommended: Option 1 (Recipe Override Permissive) with strong validation**

**Rationale:**
1. Industry standard (ERP systems use override model)
2. Handles cases where calculation is impossible (count inputs)
3. Allows recipe specialization (some recipes may have optimized methods)
4. Backward compatible with existing KB
5. Strong validation prevents drift (>50% mismatch triggers warning)

**Implementation:**
```python
def get_process_duration(process, recipe_step):
    """Get process duration, preferring recipe override."""

    # 1. If recipe specifies est_time_hr, use it (with validation)
    if recipe_step.est_time_hr is not None:
        estimated = recipe_step.est_time_hr

        # Try to calculate from time_model for validation
        try:
            calculated = calculate_from_time_model(process, recipe_step.inputs)

            # Validate consistency (within 50%)
            if abs(estimated - calculated) / calculated > 0.5:
                logger.warning(
                    f"Recipe est_time_hr ({estimated} hr) differs from "
                    f"calculated time ({calculated} hr) by "
                    f"{abs(estimated - calculated) / calculated * 100:.0f}%"
                )

        except CalculationError as e:
            # Calculation failed (e.g., count inputs), est_time_hr is necessary
            logger.info(
                f"Using recipe est_time_hr ({estimated} hr) - "
                f"calculation from time_model not possible: {e}"
            )

        return estimated

    # 2. Else calculate from process time_model
    if process.time_model:
        try:
            return calculate_from_time_model(process, recipe_step.inputs)
        except CalculationError as e:
            raise ValueError(
                f"Cannot calculate duration from time_model and no "
                f"est_time_hr specified in recipe: {e}"
            )

    # 3. No timing info available
    raise ValueError(
        f"Process {process.id} has no time_model and recipe step "
        f"has no est_time_hr"
    )
```

### Validation Rules

**Error (blocks execution):**
- Process has no time_model AND recipe has no est_time_hr
- Process time_model has invalid schema (fields don't match TimeModel)

**Warning (logged, execution continues):**
- Recipe est_time_hr differs from calculated by >50%
- Recipe has est_time_hr but it matches calculated (redundant documentation)

**Info (logged):**
- Using recipe est_time_hr because calculation impossible (count inputs, missing data)
- Calculated time from time_model (no est_time_hr specified)

### Data Cleanup Required

Based on this analysis:

1. **Fix conflicts:**
   - recipe_crushed_ore_v0 vs crushing_basic_v0 (2hr vs 30hr)
   - Any others found in survey (see recipe-step-timing-survey.md)

2. **Fix invalid schemas:**
   - mixing_and_blending_v0 (total_time_hr → proper time_model)
   - water_electrolysis_v0 (fixed_time → linear_rate)

3. **Add missing data:**
   - Item mass_kg for count-based items (enables calculation)
   - Item density for volume-based items

4. **Document process time_models:**
   - Add clear notes explaining rate basis
   - Specify which input drives time (for multi-input processes)

### For ADR-010

The ADR should specify:

1. **Precedence:** Recipe est_time_hr overrides process time_model when present
2. **Validation:** Warn if >50% mismatch between estimate and calculated
3. **Fallback:** Calculate from time_model if no est_time_hr
4. **Error handling:** Require at least one source (time_model or est_time_hr)
5. **Semantics:**
   - `est_time_hr`: Elapsed wall-clock time
   - `machine_hours`: Machine resource consumption (can differ from elapsed)
   - `labor_hours`: Labor resource consumption (can be intermittent)
6. **Calculation:** Define how to calculate from time_model (see time-calculation-real-world-examples.md)

---

## Cross-References

**Related documents:**
- `process-time-energy-models-current-state.md` - Current time_model schema and usage
- `time-calculation-real-world-examples.md` - Examples 8 and 9 (conflicts found)
- `unit-systems-and-conversions.md` - Why some calculations fail (unit mismatches)
- `scaling-and-batching-behavior.md` - How batch size affects time calculation

**Real conflicts analyzed:**
- kb/recipes/recipe_crushed_ore_v0.yaml:20 (est_time_hr: 2.0)
- kb/processes/crushing_basic_v0.yaml:21 (hr_per_kg: 0.3 → calculates 30hr)

**Code references:**
- base_builder/sim_engine.py:164-166 (start_process signature)
- base_builder/sim_engine.py:510-524 (recipe execution, currently ignores timing)

**Next steps:**
- Create recipe-step-timing-survey.md to quantify scope of conflicts
- Implement validation logic in indexer
- Add calculation helper function for time_model
