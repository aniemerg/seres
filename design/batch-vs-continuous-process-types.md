# Batch vs Continuous Process Types

**Status:** In Progress
**Date:** 2024-12-28
**Purpose:** Define explicit batch vs continuous process semantics

## Overview

Based on user feedback, **batch vs continuous must be explicitly specified** as a fundamental process characteristic. This is not just about time_model type - it's about the **physical nature of the production process** and determines:

1. How time scales with quantity
2. Whether setup time applies
3. How parallelism works
4. Validation rules
5. Simulation behavior

This document defines the semantics, validation rules, and implications of batch vs continuous process types.

---

## Core Principle

**User directive:**
> "Batching and continuous should be fully specified things."
> "perhaps better would be to explictly specify that a process is a batch process."

**Implementation:**
- Add explicit `process_type: batch | continuous` field to all processes
- time_model semantics depend on process_type
- Validation enforces consistency between process_type and time_model
- Different scaling rules for each type

---

## Process Type Definitions

### Continuous Processes

**Definition:** Processes that operate on a **continuous flow** of material with **rate-based** production.

**Characteristics:**
1. **Rate-based production** - kg/hr, units/hr, L/hr
2. **Linear scaling** - 2× material = 2× time
3. **No setup time** - or setup is separate startup/shutdown process
4. **Steady-state operation** - material flows continuously
5. **Scale-independent rate** - rate doesn't change with batch size

**Examples:**
- Crushing and grinding (continuous feed, continuous output)
- Water electrolysis (continuous flow)
- Distillation (continuous operation)
- Machining (one part after another)
- Chemical reactions in continuous reactor

**time_model structure:**
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # Or other rate specification
  # setup_hr NOT ALLOWED - validation error
```

**Scaling behavior:**
- To produce 100 kg at 10 kg/hr: 10 hours
- To produce 1000 kg at 10 kg/hr: 100 hours
- Linear relationship

**Setup handling:**
- If startup/shutdown exists, model as separate processes
- Main continuous process has no setup
- Avoids ambiguity about setup frequency

### Batch Processes

**Definition:** Processes that produce **discrete batches** with each batch requiring **setup and processing time**.

**Characteristics:**
1. **Batch-based production** - produces fixed quantity per batch
2. **Setup per batch** - each batch pays setup cost
3. **Linear batch scaling** - 10 batches = 10× (setup + batch time)
4. **Discrete units** - produces 1 batch, 2 batches, 3 batches (not 1.5 batches)
5. **Batch size defined by outputs** - process definition shows 1 batch

**Examples:**
- Motor assembly (assemble 1 motor per batch)
- Ceramic firing (kiln load = 1 batch)
- Heat treatment (furnace load = 1 batch)
- PCB fabrication (panel = 1 batch)
- Injection molding (cavity fill = 1 batch)

**time_model structure:**
```yaml
process_type: batch
time_model:
  type: batch
  setup_hr: 0.5  # Setup required per batch
  hr_per_batch: 2.0  # Processing time per batch
```

**Scaling behavior:**
- Process defines 1 batch = outputs shown (e.g., 1 motor)
- To make 10 motors: 10 batches
- Time: 10 × (0.5 setup + 2.0 process) = 25 hours
- Each batch pays setup cost

**No economies of scale:**
- User directive: setup time "should scale linearly with the number of batches (not worth the complexity to account for economies of scale)"
- 10 batches = 10× setup time
- Simplicity over realism

---

## Validation Rules

### Rule 1: process_type Required

**Validation:**
- Every process MUST specify `process_type: batch | continuous`
- Error if missing

**Rationale:**
- Explicit is better than implicit
- Eliminates ambiguity
- Enables type-specific validation

### Rule 2: Consistent time_model Type

**For continuous processes:**
```yaml
process_type: continuous
time_model:
  type: linear_rate  # MUST be linear_rate
  # type: batch  ← VALIDATION ERROR
```

**For batch processes:**
```yaml
process_type: batch
time_model:
  type: batch  # MUST be batch
  # type: linear_rate  ← VALIDATION ERROR
```

**Validation:**
- `process_type: continuous` REQUIRES `time_model.type: linear_rate`
- `process_type: batch` REQUIRES `time_model.type: batch`
- Mismatch is error

### Rule 3: No setup_hr in Continuous

**User directive:**
> "the 'setup_hr' should be ignored or trigger a validation error because it suggests a batch."

**Validation:**
```yaml
# INVALID - setup_hr in continuous process
process_type: continuous
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0
  setup_hr: 0.5  # ← VALIDATION ERROR
```

**Error message:** "setup_hr not allowed in continuous processes. If startup time exists, model as separate batch process."

**Rationale:**
- setup_hr implies batch operation
- Continuous processes shouldn't have setup
- If real startup exists, model explicitly as separate process

### Rule 4: setup_hr Required in Batch (Optional)

**Question:** Should batch processes require setup_hr?

**Option A: Required**
```yaml
process_type: batch
time_model:
  type: batch
  setup_hr: 0.0  # Must specify, even if zero
  hr_per_batch: 2.0
```

**Option B: Optional (default 0)**
```yaml
process_type: batch
time_model:
  type: batch
  hr_per_batch: 2.0
  # setup_hr: 0  (implied if not specified)
```

**Recommendation:** Optional (Option B) - not all batch processes have setup.

### Rule 5: Batch Size Defined by Outputs

**Validation:**
```yaml
# GOOD - batch size clear from outputs
process_type: batch
outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
time_model:
  type: batch
  hr_per_batch: 1.0  # Time for 1 motor (1 batch as defined by outputs)
```

**User directive:**
> "I don't like putting batch output in the time model, rather that should be in ouputs."
> "The time model should assume that it relates to 1 batch if in 'batch' mode."

**Principle:**
- Process outputs define what 1 batch produces
- time_model just specifies time for 1 batch
- Don't duplicate batch size in time_model

---

## Examples Revisited

### Example A: Continuous Crushing

**Before (ambiguous):**
```yaml
inputs:
  - item_id: regolith_coarse_fraction
    qty: 1.0
    unit: kg
outputs:
  - item_id: regolith_powder
    qty: 1.0
    unit: kg
time_model:
  type: linear_rate
  hr_per_kg: 0.1  # Was this continuous? Unclear.
```

**After (explicit):**
```yaml
process_type: continuous  # ← EXPLICIT
inputs:
  - item_id: regolith_coarse_fraction
    qty: 1.0
    unit: kg
outputs:
  - item_id: regolith_powder
    qty: 1.0
    unit: kg
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # 0.1 hr/kg = 10 kg/hr
  # No setup_hr - continuous
```

**Calculation:**
- 100 kg input × (1/10 kg/hr) = 10 hours
- Linear scaling

### Example B: Motor Assembly (Batch)

**Before (used fixed_time):**
```yaml
outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
time_model:
  type: fixed_time
  hr_per_batch: 1.0
```

**After (explicit batch):**
```yaml
process_type: batch  # ← EXPLICIT
outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
time_model:
  type: batch
  setup_hr: 0.1  # Tool setup
  hr_per_batch: 0.9  # Assembly time
```

**Calculation:**
- 1 motor = 1 batch = 0.1 + 0.9 = 1.0 hour
- 10 motors = 10 batches = 10 × (0.1 + 0.9) = 10 hours
- Setup paid per batch

### Example C: Ceramic Forming with Setup

**Before (setup in continuous was ambiguous):**
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 0.5
  setup_hr: 0.2  # What does this mean in continuous context?
```

**After - Option 1 (Continuous, no setup):**
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate_kg_per_hr: 2.0  # 1/0.5
  # No setup - continuous operation
```

**After - Option 2 (Batch with setup):**
```yaml
process_type: batch
inputs:
  - item_id: ceramic_powder_mixture
    qty: 5.0  # Batch size
    unit: kg
outputs:
  - item_id: green_ceramic_parts
    qty: 5.0
    unit: kg
time_model:
  type: batch
  setup_hr: 0.2  # Mold preparation
  hr_per_batch: 2.5  # 5 kg × 0.5 hr/kg
```

**Decision depends on physics:**
- If mold is prepared once then many parts formed: **continuous**
- If mold is prepared per batch: **batch**

### Example D: Water Electrolysis

**Before (type mismatch):**
```yaml
# Notes said "continuous" but used fixed_time
time_model:
  type: fixed_time
  hr_per_batch: 2.0
  notes: "Continuous electrolysis process"  # ← Contradiction!
```

**After (consistent):**
```yaml
process_type: continuous  # ← Matches notes
time_model:
  type: linear_rate
  rate_kg_per_hr: 0.5  # 2 hr/kg = 0.5 kg/hr
```

**Calculation:**
- 100 kg water at 0.5 kg/hr = 200 hours
- Continuous operation

---

## Batch Size Mechanics

### How Batch Size is Determined

**User directive:**
> "The time model should assume that it relates to 1 batch if in 'batch' mode."

**Principle:**
1. **Process outputs define 1 batch**
2. Recipe specifies total desired quantity
3. Simulation calculates number of batches needed
4. Time = num_batches × (setup_hr + hr_per_batch)

**Example:**
```yaml
# Process definition
process_type: batch
outputs:
  - item_id: solar_cell_set
    qty: 1.0  # ← 1 batch produces 1 set
    unit: unit
time_model:
  type: batch
  setup_hr: 1.0
  hr_per_batch: 11.0
```

```yaml
# Recipe requesting 50 sets
steps:
  - process_id: solar_cell_fabrication_v0
    outputs:
      - item_id: solar_cell_set
        qty: 50.0  # Want 50 sets
        unit: unit
```

**Calculation:**
- 1 batch = 1 set (from process)
- Want 50 sets → need 50 batches
- Time: 50 × (1 + 11) = 600 hours

### Variable Batch Sizes

**Question:** What if batch size varies?

**Example:** Kiln can hold 10-50 kg depending on part size

**Option A: Fixed batch (simpler)**
```yaml
# Define standard batch
outputs:
  - item_id: fired_ceramic
    qty: 30.0  # Standard batch size
    unit: kg
time_model:
  type: batch
  hr_per_batch: 8.0  # Firing time
```

**Option B: Recipe overrides batch size**
```yaml
# Recipe specifies different batch size
steps:
  - process_id: ceramic_firing_v0
    outputs:
      - item_id: fired_ceramic
        qty: 50.0  # Override: 50 kg per batch
        unit: kg
    time_model:  # Override time model if batch size affects time
      type: batch
      hr_per_batch: 8.0  # Still 8 hours (firing is time-based, not mass-based)
```

**Recommendation:** Option A (fixed) for simplicity. Recipe overrides if really needed.

---

## Parallelism

### Sequential vs Parallel Batches

**User feedback on parallel processing:**
> "I'm uncertain about the suggestion for a 'concurrent' field, seems like we just count the qty and unit for the machine_id."

**Principle:**
- Parallelism is about **resource availability**, not process definition
- If you have 10 assembly stations, 10 batches can run in parallel
- Simulation handles this via resource scheduling

**Process definition (no parallelism info):**
```yaml
process_type: batch
requires_ids:
  - assembly_station_v0  # Requires 1 station
time_model:
  type: batch
  hr_per_batch: 1.0
```

**Simulation with resource availability:**
- 1 assembly station: 10 batches sequential = 10 hours
- 10 assembly stations: 10 batches parallel = 1 hour
- Resource scheduler determines actual parallelism

**No need for:**
- `max_parallel_batches` field
- `concurrent: true/false` field
- Complex parallelism modeling

**Just need:**
- Clear resource requirements (which machines)
- Resource availability in simulation
- Scheduler assigns work to available resources

---

## Setup Time Semantics

### Setup Scope

**Question:** What does setup_hr represent?

**Answer:** Setup for **one batch** execution.

**Examples:**
- **Assembly:** Tool retrieval, fixture setup, test equipment connection
- **Firing:** Load kiln, close door, set temperature profile
- **Machining:** Mount workpiece, tool selection, zero offsets
- **Molding:** Mold installation, parameter setting

### Setup Frequency

**User directive:**
> "If multiple batches are being run by a recipe, setup_hr should scale linearly with the number of batches"

**Interpretation:**
- No setup amortization across batches
- Each batch pays full setup cost
- Economies of scale not modeled (complexity not worth it)

**Example:**
```yaml
time_model:
  type: batch
  setup_hr: 0.5
  hr_per_batch: 2.0

# 1 batch: 0.5 + 2.0 = 2.5 hours
# 5 batches: 5 × (0.5 + 2.0) = 12.5 hours (NOT 0.5 + 5×2.0 = 10.5)
```

**Rationale:**
- Simplicity
- Conservative estimate (better to overestimate time)
- Avoids questions about when setup can be amortized

### When Setup Should Be Zero

**Cases where setup_hr = 0:**
1. Truly continuous processes (modeled as continuous, not batch)
2. Batch processes where setup is negligible
3. Setup already completed in previous step

**Example:**
```yaml
steps:
  - process_id: mold_setup_v0  # Separate setup step
    time_model:
      type: batch
      hr_per_batch: 0.5  # Just setup

  - process_id: injection_molding_v0  # No setup needed
    time_model:
      type: batch
      setup_hr: 0  # Already set up
      hr_per_batch: 0.1  # Just molding
```

---

## Migration from Current State

### Processes Currently Using linear_rate

**Likely continuous:**
- Crushing, grinding, milling
- Distillation, electrolysis
- Mixing (continuous mixer)
- Pumping, conveying

**Action:**
```yaml
# Add to each
process_type: continuous
time_model:
  type: linear_rate
  # Keep existing rate specification
```

### Processes Currently Using fixed_time

**Likely batch:**
- Assembly operations
- Heat treatment (furnace loads)
- Firing (kiln loads)
- Discrete manufacturing

**Action:**
```yaml
# Replace fixed_time with batch
process_type: batch
time_model:
  type: batch
  setup_hr: 0  # Or estimate if setup exists
  hr_per_batch: <previous hr_per_batch value>
```

### Processes with setup_hr in linear_rate

**Current (ambiguous):**
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 0.5
  setup_hr: 0.2
```

**Need to decide:**
- Is this really batch? → Convert to batch
- Or is setup a separate startup process? → Split into two processes

**Example split:**
```yaml
# Startup process (batch)
process_id: ceramic_press_startup_v0
process_type: batch
time_model:
  type: batch
  hr_per_batch: 0.2  # Startup time

# Main process (continuous)
process_id: ceramic_forming_v0
process_type: continuous
time_model:
  type: linear_rate
  rate_kg_per_hr: 2.0
```

---

## Validation Error Messages

### Error: Missing process_type

```
ValidationError: Process 'crushing_basic_v0' missing required field 'process_type'.
  Must specify: process_type: batch | continuous
```

### Error: Type mismatch

```
ValidationError: Process 'water_electrolysis_v0' has process_type: continuous
  but time_model.type: fixed_time.
  Continuous processes must use time_model.type: linear_rate
```

### Error: setup_hr in continuous

```
ValidationError: Process 'ceramic_forming_v0' has process_type: continuous
  but specifies time_model.setup_hr: 0.2
  Setup time not allowed in continuous processes.
  Suggestion: Model as separate batch process or remove setup_hr.
```

### Error: Wrong time_model type

```
ValidationError: Process 'motor_assembly_v0' has process_type: batch
  but time_model.type: linear_rate.
  Batch processes must use time_model.type: batch
```

---

## Open Questions

### 1. Batch Processes with Variable Time

**RESOLVED:** Avoid variable time modeling that doesn't scale with inputs/outputs.

**Scenario:** Batch time depends on load, temperature, etc.

**Example:** Kiln firing - time depends on peak temperature
- Low temp (900°C): 4 hours
- High temp (1200°C): 8 hours

**Decision:**
- If time doesn't scale with inputs/outputs (kg, count), **just estimate**
- Don't try to model non-scaling variability
- Create separate processes for significantly different variants

**Options:**
A. Multiple processes (ceramic_firing_low_temp_v0, ceramic_firing_high_temp_v0) ✓
B. Recipe overrides with estimated time_model ✓
C. Complex parameter modeling ✗ (don't do this)

**Recommendation:** Option A (multiple processes) or B (recipe estimate).

### 2. Semi-Continuous Processes

**RESOLVED:** No mixed continuous/batch - split or pick dominant.

**Scenario:** Process that's continuous but has periodic batch operations

**Example:** Continuous casting with periodic mold change

**Decision:**
- **No mixed process types** - process is either batch OR continuous
- If both exist, split into two separate processes
- Or pick the dominant type and ignore the minor component

**Options:**
A. Split into two processes (continuous casting + batch mold change) ✓
B. Model as dominant type only (continuous, ignore mold change) ✓
C. Mixed continuous/batch type ✗ (not supported)

**Recommendation:** Option A (split) if both are significant, Option B (dominant) if one is minor.

### 3. Boundary Processes

**RESOLVED:** Boundary processes can have a process_type.

**Question:** Do boundary processes need process_type?

**Answer:**
- Yes, boundary processes **can** have process_type
- Even "free" environmental resources require extraction processes
- Mining/collection processes should be:
  - process_type: continuous (for excavation)
  - With time_model (machine time usage)
  - With machines (excavators, drills)

**Example:**
```yaml
# Mining regolith (free resource, but extraction takes time)
process_id: regolith_mining_lunar_mare_v0
process_type: continuous  # ← Boundary can have type
inputs: []  # Free resource
outputs:
  - item_id: regolith_lunar_mare
    qty: 100.0
    unit: kg
requires_ids:
  - excavator_v0
time_model:
  type: linear_rate
  rate_kg_per_hr: 100.0  # Mining rate
energy_model:
  type: kWh_per_kg
  value: 0.5  # Excavation energy
```

**Key principle:** All processes should have time_model and machines, even boundary processes.

---

## Summary

### Key Decisions

1. **Explicit process_type field** - batch or continuous, required
2. **Type determines time_model** - batch uses batch, continuous uses linear_rate
3. **No setup in continuous** - validation error if present
4. **Setup scales linearly** - no economies of scale
5. **Batch size from outputs** - don't duplicate in time_model
6. **Parallelism via resources** - not in process definition

### Validation Rules

1. process_type required
2. process_type matches time_model.type
3. setup_hr only in batch processes
4. Batch size defined by outputs

### Migration Path

1. Add process_type to all processes
2. Convert fixed_time → batch
3. Split processes with setup_hr in continuous
4. Update validation in indexer

### Benefits

1. **Clarity** - explicit is better than implicit
2. **Validation** - catch semantic errors
3. **Simulation** - unambiguous behavior
4. **Documentation** - process type self-documents

This explicit batch vs continuous distinction is foundational for the entire KB redesign.
