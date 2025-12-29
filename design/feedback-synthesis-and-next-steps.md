# Feedback Synthesis and Next Steps

**Date:** 2024-12-28
**Purpose:** Synthesize user feedback and reorient investigation toward comprehensive KB redesign

## Overview

Based on detailed feedback in `time-model-hierarchy-feedback.txt`, the scope of this investigation is **much larger** than initially understood. This is not just ADR-010 (time/energy modeling) - this is a **fundamental redesign of how the KB works** requiring:

1. **Multiple ADRs** to fully define KB semantics
2. **New unified code base** for indexing, closure analysis, and simulation
3. **Massive schema harmonization** with comprehensive validation
4. **Migration strategy** from current underspecified state to fully validated system
5. **Agent work queue system** for indexer to detect and enqueue fixes

This document synthesizes the feedback and proposes how to proceed.

---

## Major Principles Established

### 1. Full Specification Required

**User directive:**
> "time_models should be fully specified or result in errors. Time_models should be used in simulation and fully accounted for. Energy models should be fully used in simulation and accounted for. Masses and counts should be reconciled across processes and recipes."

**Implications:**
- No more partial/missing data
- Validation must catch all gaps
- Simulation must use all KB data (not agent-arbitrary values)
- Full material flow accounting

### 2. Unified Code Base

**User directive:**
> "To do so, instead of updating those three, the goal will be to build a unified set of code that provides all three of those things from a unified base of tested code."

**Implications:**
- Don't patch indexer, closure, and simulation separately
- Build new unified foundation
- Comprehensive test suite from investigation examples
- Validation, calculation, and simulation share code

### 3. Recipes Override Processes

**User directive:**
> "Recipes override processes."
> "a process time model is the default for that process, overrideable by a recipe. When there is a conflict, the recipe will control."

**Implications:**
- Clear precedence established (my Option 1 recommendation validated)
- But need to migrate from `est_time_hr` to actual `time_model` overrides in recipe steps
- Recipe can completely redefine process if needed

### 4. Implicit Unit Conversion

**User directive:**
> "Units should be implicitly converted where possible, or errors thrown if not possible."
> "known conversions, (L of water to volume as a possible example, kg to tons) should be handled implicitly"

**Implications:**
- System should convert units automatically when unambiguous
- Need conversion database/rules
- Only error when conversion is impossible/ambiguous

### 5. Batch vs Continuous Must Be Explicit

**User directive:**
> "Batching and continuous should be fully specified things."
> "perhaps better would be to explictly specify that a process is a batch process."

**Implications:**
- Not just `type: fixed_time` vs `type: linear_rate`
- Need explicit `process_type: batch | continuous` declaration
- Different semantics and validation for each type

### 6. All Processes Use Machines

**User directive:**
> "All processes should have a time model. The purpose of the time model is to govern time usage of machines."
> "All processes should be associated with a machine that is used for that time (and can't be used for something else during that time)."

**Implications:**
- No processes without time_model (or error if truly needed)
- Every process ties up machine(s) for duration
- Resource accounting is fundamental
- Enables scheduling/capacity analysis

---

## Feedback on Specific Examples

### Example 1: regolith_crushing_grinding_v0 (Simple Linear Rate)

**Feedback:**
> "hr_per_kg", "kWh_per_kg" maybe these should be multiple fields, numerator: hr, denominator: kg, or something like that?

**Implication:**
- Current `hr_per_kg: 0.1` might become:
  ```yaml
  time_model:
    type: linear_rate
    numerator_value: 0.1
    numerator_unit: hr
    denominator_unit: kg
  ```
- Or more structured:
  ```yaml
  time_model:
    type: linear_rate
    rate:
      value: 0.1
      unit: hr/kg
  ```

**Action:** Need document exploring time_model schema redesign options.

### Example 2: ceramic_forming_basic_v0 (Setup Time)

**Feedback:**
> "The default is that the process should define a 'batch', but perhaps better would be to explictly specify that a process is a batch process."
> "the 'setup_hr' should be ignored or trigger a validation error because it suggests a batch."
> "If multiple batches are being run by a recipe, setup_hr should scale linearly with the number of batches"

**Implications:**
- `setup_hr` only valid in batch processes, error in continuous
- Batch processes pay setup per batch (no economies of scale)
- Continuous processes with setup are modeling error

**Revised understanding:**
```yaml
# Batch process
process_type: batch
time_model:
  type: batch
  setup_hr: 0.2
  hr_per_batch: 2.5

# Continuous process (setup_hr would error)
process_type: continuous
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0
  # setup_hr: 0.2  ← VALIDATION ERROR
```

**Action:** Need batch-vs-continuous-process-types.md document.

### Example 3: motor_final_assembly_v0 (Fixed Batch Time)

**Feedback:**
> "Seems like this should be a batch recipe with an output of 1 motor_electric_small."
> "I don't know if 'fixed_time' should be an actual time model, unless there is a canonical example."
> "If we had a 'batch' time model, would the fixed_time be necessary?"

**Implications:**
- `fixed_time` type might not be needed - just `batch` type
- Batch time_model assumes it relates to 1 batch
- Batch size defined by process outputs

**Revised model:**
```yaml
process_type: batch
outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
time_model:
  type: batch
  hr_per_batch: 1.0  # Time for 1 motor (1 batch)
```

To make 10 motors: 10 batches × 1 hr = 10 hr

**Action:** Incorporate into batch-vs-continuous document.

### Example 4: pump_housing_machining_v0 (Volume Input Mismatch)

**Feedback:**
> "the time model should really be count based, not kg based. So an agent made a mistake here, right?"
> "the time_model should specify the scaling input or output--that's probably a cleaner way to do it."
> "Option 3 looks closest to my thinking."

**Implications:**
- time_model should specify which input/output it scales from
- Not all processes are kg-based - need count-based, volume-based, etc.
- Agent mistakes should be caught by validation

**Revised model:**
```yaml
time_model:
  type: linear_rate
  rate_value: 12.0
  rate_unit: unit/hr  # or hr/unit
  scaling_basis: machined_part_raw  # Which input drives the rate
```

**Action:** Incorporate into time-model-schema-redesign.md.

### Example 5: water_electrolysis_v0 (Type Mismatch)

**Feedback:**
> "This would be improved by having a 'batch' time_model"
> "But, yeah, this is probably a linear_rate process."
> "The energy model looks like it could be better specified. Is it input or output kg? For which output?"

**Implications:**
- Energy model also needs scaling basis specification
- `kWh_per_kg` is ambiguous when multiple inputs/outputs

**Revised model:**
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: 2.0
  rate_unit: hr/kg
  scaling_basis: water  # Input that drives time
energy_model:
  type: per_unit
  value: 15.0
  unit: kWh/kg
  scaling_basis: water  # Input that drives energy
  # Or: scaling_basis: hydrogen_gas (output)
```

**Action:** Energy model also needs redesign (not just time).

### Example 6: environment_source_v0 (Boundary Process)

**Feedback:**
> "environment_source_v0 doesn't really make much sense to me. Read the regolith_organization... file in design/."
> "There should be processes that result in mined regolith of some form. They should include a time model for the mining to consume the time of some mining machine."

**Implications:**
- Boundary processes might not be needed
- Even "free" resources require mining/collection processes
- All processes should have machines and time

**Action:** Read design/regolith_organization*.md and revise understanding.

### Example 7: mixing_and_blending_v0 (Invalid Schema)

**Feedback:**
> "Clear case of something that should be caught by schema and other validation."

**Implications:**
- Schema validation must be strict
- Indexer should catch these

**Action:** Already identified, needs fixing + validation.

### Example 9: labor_bot_basic_v0 (Count-Based Assembly)

**Feedback:**
> "Count based time models would be fine. Assembly using fixed time would also be fine. Assembly specific model would also be fine."

**Implications:**
- Multiple valid approaches for assembly
- Count-based time models are acceptable
- Don't over-constrain

### Example 10: solar_cell_fabrication_v0 (Batch Output Ambiguity)

**Feedback:**
> "I don't like putting batch output in the time model, rather that should be in ouputs."
> "The time model should assume that it relates to 1 batch if in 'batch' mode."
> "You can maybe specify one input or output to scale off of, that might work."
> "But avoid importing the process or recipe into the time model."
> "'units_per_batch' might work, but not 'wafers_per_batch'."

**Key principle:** **time_model should not duplicate process/recipe data.**

**Correct approach:**
- Process outputs define what 1 batch produces
- time_model just says how long 1 batch takes
- Can optionally specify scaling basis

```yaml
outputs:
  - item_id: solar_cell_set
    qty: 1.0
    unit: unit
time_model:
  type: batch
  hr_per_batch: 12.0
  # Implicitly: 1 batch = outputs shown above
```

---

## Override Hierarchy - Key Changes

### Migration from est_time_hr

**User directive:**
> "we should migrate from 'est_time_hr' to using time_models directly in the recipe step as an override"
> "We will want to migrate away from 'est_time_hr' to providing an actual time model in the override."

**Implications:**
- `est_time_hr` was useful placeholder but underspecified
- Recipe steps should have full `time_model` override capability
- Migration strategy needed

**Before (current):**
```yaml
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0
```

**After (target):**
```yaml
steps:
  - process_id: crushing_basic_v0
    time_model:  # Override process time_model
      type: linear_rate
      rate_kg_per_hr: 50.0  # Faster than process default
```

### Time Model Purpose Clarified

**User directive:**
> "The time model is to relate time to production. It is meant to quantify the usage of the time resource of machines, to quantify things like amount of machines needed to produce a given quanity of an item in a period of time and so on."

**Purpose of time_model:**
1. Quantify machine time usage
2. Calculate production capacity
3. Determine resource costs
4. Enable scheduling analysis
5. Not to determine "actual" duration (agent decides that)

### Simulation Agent Role

**User directive:**
> "Timing Data should be usable along with duration provided by an agent to calculate machine usage and production."
> "Agent decides timing based on production needs"

**New understanding:**
- Agent specifies: duration OR production quantity
- time_model calculates: the other variable + machine usage

**Example scenarios:**

**Scenario A: Agent specifies duration**
- Agent: "Run crushing for 8 hours"
- time_model (10 kg/hr): Calculates 80 kg produced
- Machine usage: 8 machine-hours consumed

**Scenario B: Agent specifies production**
- Agent: "Produce 100 kg crushed ore"
- time_model (10 kg/hr): Calculates 10 hours needed
- Machine usage: 10 machine-hours consumed

**Scenario C: Agent specifies both (validation)**
- Agent: "Run for 8 hours, expect 80 kg"
- time_model (10 kg/hr): Validates consistency
- Error if mismatch

---

## machine_hours and labor_hours - Major Rethinking

**User directive:**
> "We need to bring harmony to these fields and usage. The key is that we are attempting to account for resource usage and to have a good accounting of the resource costs of producing things."

### Current Understanding Problems

1. **machine_hours** duplicates what process time_model should provide
2. **labor_hours** unclear if concurrent or sequential
3. No specification of which machine provides labor
4. Relationship to process machines unclear

### New Approach Emerging

**Processes:**
- Define machines used (from `requires_ids` and `resource_requirements`)
- Define time_model (governs how long machines are used)
- Process execution consumes machine time

**Recipe Steps:**
- Can add ADDITIONAL concurrent resource usage
- Must specify which machine for labor
- Sequential operations should be separate steps

**Example:**
```yaml
# Process definition
process_id: metal_forming_v0
requires_ids:
  - hydraulic_press_v0
time_model:
  type: batch
  hr_per_batch: 2.0

# Recipe step (adds labor)
steps:
  - process_id: metal_forming_v0
    concurrent_resources:  # In addition to process machines
      - machine_id: labor_bot_general_v0
        hours: 0.5  # Intermittent supervision
```

**Accounting:**
- Process uses hydraulic_press for 2 hours
- Recipe adds labor_bot for 0.5 hours concurrent
- Total: 2 machine-hours (press), 0.5 machine-hours (labor)
- Elapsed time: 2 hours

### Sequential Labor

**User directive:**
> "any sequential labor should be it's own step"

If setup/teardown requires labor before/after process:

```yaml
steps:
  # Setup step
  - process_id: setup_mold_v0
    # Uses labor, no other machines

  # Forming step
  - process_id: metal_forming_v0
    # Uses press + concurrent labor

  # Teardown step
  - process_id: remove_part_v0
    # Uses labor, no other machines
```

**Action:** Need labor-accounting-harmonization.md document.

---

## Batch vs Continuous - Deep Dive Needed

**User feedback summary:**
- Explicit `process_type: batch | continuous` field
- `setup_hr` only valid in batch processes
- Batch processes pay setup per batch (linear scaling)
- Continuous processes use rates
- time_model type must match process_type

### Batch Process Characteristics

1. **Discrete units of production**
2. **Setup time per batch**
3. **Fixed or variable batch time**
4. **Batch size defined by outputs**
5. **Multiple batches = linear scaling**

### Continuous Process Characteristics

1. **Ongoing production**
2. **Rate-based (kg/hr, units/hr)**
3. **No setup time** (or validation error)
4. **Scale linearly with quantity**
5. **Can have startup/shutdown (separate processes?)**

**Action:** Create batch-vs-continuous-process-types.md document.

---

## Schema Redesign Considerations

### Current time_model Schema Issues

1. `hr_per_kg` - hard-coded units, not flexible
2. `rate_kg_per_hr` - same issue
3. No specification of scaling basis (which input/output)
4. `fixed_time` type unclear vs batch
5. No distinction between batch and continuous

### Proposed Improvements

**Option A: Structured rate with units**
```yaml
time_model:
  process_type: continuous
  type: linear_rate
  rate:
    value: 10.0
    numerator: kg
    denominator: hr
  scaling_basis: primary_input_item_id
```

**Option B: Separate numerator/denominator fields**
```yaml
time_model:
  process_type: continuous
  type: linear_rate
  rate_value: 10.0
  rate_numerator_unit: kg
  rate_denominator_unit: hr
  scaling_basis: primary_input_item_id
```

**Option C: Unit string with parsing**
```yaml
time_model:
  process_type: continuous
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: primary_input_item_id
```

**For batch processes:**
```yaml
time_model:
  process_type: batch
  type: batch
  setup_hr: 0.5
  hr_per_batch: 2.0
  # Batch size implicit from outputs
```

**Action:** Create time-model-schema-redesign.md document with full proposal.

---

## Validation Strategy - Comprehensive

Based on user feedback, validation must:

1. **Schema validation** - catch invalid fields, types
2. **Semantic validation** - catch logical errors
3. **Cross-reference validation** - verify data consistency
4. **Calculation validation** - ensure time_model can be evaluated

### Examples of Validation Rules

**Schema:**
- All fields match TimeModel definition
- No unknown fields (total_time_hr error)
- Required fields present

**Semantic:**
- `setup_hr` only in batch processes
- `process_type` matches `time_model.type`
- `scaling_basis` refers to actual input/output

**Cross-reference:**
- Items referenced exist
- Machines referenced exist
- Units can be converted

**Calculation:**
- time_model can be evaluated with process inputs/outputs
- No missing data (mass_kg, density) when needed
- Unit conversions possible

**Action:** Expand validation-strategy.md document significantly.

---

## Impact on Remaining Planned Documents

### Originally Planned (from roadmap):

1. ⏳ scaling-and-batching-behavior.md
2. ⏳ recipe-step-timing-survey.md
3. ⏳ material-dependent-models.md
4. ⏳ validation-strategy.md
5. ⏳ migration-impact-analysis.md
6. ⏳ parallel-resource-usage-model.md
7. ⏳ consumers-and-use-cases.md
8. ⏳ alternative-architectures.md

### Revised Priority and Scope:

#### CRITICAL (Do Next):

1. **batch-vs-continuous-process-types.md** (NEW)
   - Define explicit batch vs continuous semantics
   - Validation rules
   - Examples of each type
   - Migration implications

2. **time-model-schema-redesign.md** (NEW)
   - Propose new time_model structure
   - Handle multiple units (not just kg)
   - Scaling basis specification
   - Backward compatibility considerations

3. **labor-accounting-harmonization.md** (NEW)
   - Reconcile machine_hours, labor_hours, process machines
   - Concurrent vs sequential labor
   - Full resource accounting model
   - Recipe override mechanics

4. **validation-strategy.md** (EXPAND)
   - Comprehensive validation rules
   - Schema, semantic, cross-reference, calculation
   - Error vs warning vs info
   - Work queue integration

#### HIGH PRIORITY:

5. **recipe-process-override-mechanics.md** (NEW)
   - How recipe steps override processes
   - Migration from est_time_hr to time_model overrides
   - Complete override capability
   - Validation of overrides

6. **unified-kb-code-architecture.md** (NEW)
   - Design for unified indexer/closure/simulation code
   - Shared calculation engine
   - Validation integration
   - Test strategy

7. **scaling-and-batching-behavior.md** (REFOCUS)
   - Focus on batch scaling (setup per batch)
   - Continuous scaling (linear)
   - Recipe quantity vs process batch size

8. **implicit-unit-conversion.md** (NEW)
   - Known conversions (L water, kg/tons)
   - Conversion rules and database
   - When to convert vs when to error
   - Integration with time_model calculations

#### MEDIUM PRIORITY:

9. **migration-impact-analysis.md** (EXPAND)
   - Migration from est_time_hr to time_model overrides
   - Schema changes impact
   - Validation rollout strategy
   - Agent work queue for fixes

10. **energy-model-redesign.md** (NEW)
    - Parallel to time_model redesign
    - Scaling basis for energy
    - kWh_per_kg → structured approach

11. **material-flow-accounting.md** (NEW)
    - Full mass/count reconciliation
    - Material must exist before use
    - Transformation tracking
    - Validation rules

#### LOWER PRIORITY (Can Defer):

12. material-dependent-models.md
13. parallel-resource-usage-model.md (partially covered by labor harmonization)
14. consumers-and-use-cases.md
15. alternative-architectures.md
16. recipe-step-timing-survey.md (less important now - focus on design)

---

## Multiple ADRs Likely Needed

**User directive:**
> "We may need to have multiple ADRs that fully define how the KB files work and provide the basis for a fully testable implementation."

### Proposed ADR Structure:

**ADR-010: Time Model Redesign**
- New time_model schema
- Batch vs continuous process types
- Scaling basis specification
- Validation rules

**ADR-011: Recipe Override Mechanics**
- How recipes override processes
- Migration from est_time_hr
- time_model overrides in recipe steps
- Complete override capability

**ADR-012: Resource Accounting and Labor Harmonization**
- machine_hours, labor_hours semantics
- Concurrent vs sequential resources
- Process machines vs recipe resources
- Full accounting model

**ADR-013: Unit Conversion and Type System**
- Implicit unit conversion rules
- Conversion database
- Type-aware calculations
- Error handling

**ADR-014: Validation and Error Detection**
- Comprehensive validation strategy
- Schema, semantic, calculation validation
- Work queue for agent fixes
- Indexer integration

**ADR-015: Unified KB Code Architecture**
- Shared calculation engine
- Validation integration
- Indexer, closure, simulation from common base
- Test strategy

**ADR-016: Material Flow Accounting**
- Mass/count reconciliation
- Material provenance tracking
- Transformation validation

---

## Immediate Next Steps

### 1. Read Referenced Documents

**User directive:**
> "Read the regolith_organization... file in design/"

**Action:** Read design/regolith_organization*.md to understand latest regolith approach.

### 2. Create Critical New Documents

In priority order:

1. **batch-vs-continuous-process-types.md** - Foundational distinction
2. **time-model-schema-redesign.md** - Concrete schema proposal
3. **labor-accounting-harmonization.md** - Resource accounting model

### 3. Update Roadmap

- Add new documents
- Reprioritize existing planned documents
- Update to reflect multiple ADRs
- Indicate unified code base goal

### 4. Use Examples as Test Cases

**User directive:**
> "These examples are incredible examples that would be good to use as parts of planned tests and these examples would be great in the ADR as suggested cases (with an eye towards good tests)."

**Action:**
- Extract examples into test case format
- Document expected behavior under new schema
- Use for validation of proposals

---

## Key Insights from Feedback

### What I Got Right:

1. ✅ Examples are valuable (will become tests)
2. ✅ Recipe override model (Option 1) was correct direction
3. ✅ Identified real conflicts and issues
4. ✅ Schema validation gaps
5. ✅ Unit heterogeneity problems

### What Needs Major Revision:

1. ❌ Scope - this is not just ADR-010, it's a KB redesign
2. ❌ Code approach - need unified base, not patch three systems
3. ❌ time_model schema - needs complete redesign (scaling basis, units)
4. ❌ Batch vs continuous - needs to be explicit process type
5. ❌ est_time_hr - migration target is time_model overrides, not keeping est_time_hr
6. ❌ Labor/resource accounting - needs complete rethinking
7. ❌ Simulation role - agent specifies duration OR quantity, not arbitrary

### What's Now Clear:

1. **Full specification** - no partial data, validation catches all gaps
2. **Implicit conversion** - system handles known conversions automatically
3. **Machine accounting** - all processes use machines, time_model governs usage
4. **Recipe power** - can completely override process
5. **Work queues** - indexer detects issues, enqueues for agent fixing
6. **Test-driven** - examples become tests for new implementation

---

## Questions for Clarification

### 1. Regolith Organization
Need to read design/regolith_organization*.md - what files exist?

### 2. Batch Time Model Details
If batch processes have `hr_per_batch`, how do variable-time batches work?
- Example: Firing kiln - time depends on temperature and load
- Still 1 batch definition but time varies?

### 3. Count-Based Time Models
How should count-based rates be specified?
```yaml
# Option A: Natural rate
time_model:
  rate: 10.0
  rate_unit: unit/hr

# Option B: Inverted
time_model:
  rate: 0.1
  rate_unit: hr/unit
```

### 4. Energy Model Scope
Should energy_model redesign happen in parallel with time_model?
- Same issues (scaling basis, units)
- Should be consistent

### 5. Multiple Outputs
If process has multiple outputs, how does scaling basis work?
```yaml
outputs:
  - item_id: hydrogen_gas
    qty: 0.111
    unit: kg
  - item_id: oxygen_gas
    qty: 0.889
    unit: kg

time_model:
  scaling_basis: water  # Input
  # Or: scaling_basis: hydrogen_gas  # Primary output
```

---

## Conclusion

This feedback fundamentally changes the investigation scope:

**Before:** Write ADR-010 for time/energy modeling fixes

**After:** Design comprehensive KB redesign with:
- Multiple ADRs
- New unified code base
- Complete schema overhaul
- Full validation strategy
- Migration path for existing KB
- Agent work queue system

The investigation documents created so far (current state, unit systems, real-world examples, override hierarchy) provide **excellent foundation** for this larger effort. The examples will become test cases.

Next step: Create the three critical new documents (batch-vs-continuous, time-model-schema-redesign, labor-accounting-harmonization) before proceeding further.

The investigation is now properly scoped to match the actual complexity of the problem.
