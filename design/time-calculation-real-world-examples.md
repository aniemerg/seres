NOTE: Historical document predating ADR-012+; references deprecated schema. See docs/kb_schema_reference.md for current rules.

# Time Calculation Real-World Examples

**Status:** In Progress
**Date:** 2024-12-28
**Purpose:** Walk through actual KB processes attempting to calculate duration from time_model

## Overview

This document examines 15+ real processes and recipes from the knowledge base, attempting to calculate process duration from `time_model` data. For each example, we:

1. Show the current KB definition
2. Attempt to calculate duration using time_model
3. Document what works, what's ambiguous, what fails
4. Identify missing data needed for calculation
5. Propose how it SHOULD work

The goal is to provide concrete, grounded evidence of what problems exist in practice, not just theoretical analysis.

---

## Example 1: Simple Linear Rate (kg-based)

**Process:** `regolith_crushing_grinding_v0`
**Type:** Linear rate, kg input → kg output
**File:** kb/processes/regolith_crushing_grinding_v0.yaml

### Current Definition

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
  hr_per_kg: 0.1
  notes: "continuous crushing/grinding ~10 kg/hr throughput"
energy_model:
  type: kWh_per_kg
  value: 0.3
```

### Time Calculation Attempt

**Scenario:** Process 100 kg of regolith_coarse_fraction

**Formula:** `duration = input_mass_kg × hr_per_kg`

**Calculation:**
- Input mass: 100 kg
- Rate: 0.1 hr/kg (equivalent to 10 kg/hr throughput)
- Duration: 100 kg × 0.1 hr/kg = **10 hours**

### Analysis

✅ **What works:**
- Clear kg-based input and output
- Unambiguous rate specification (hr_per_kg)
- Simple calculation, no dependencies on other data
- Energy also kg-based, consistent coupling

✅ **This is the IDEAL case** - simple, well-defined, calculable.

### How It Should Work

This example should be the **template** for all rate-based processes:
- Input and output in same units (kg)
- time_model type matches input type (linear_rate for continuous)
- Rate specified clearly (hr_per_kg or rate_kg_per_hr)
- Energy model uses same basis (kWh_per_kg)

---

## Example 2: Linear Rate with Setup Time

**Process:** `ceramic_forming_basic_v0`
**Type:** Linear rate with setup overhead
**File:** kb/processes/ceramic_forming_basic_v0.yaml

### Current Definition

```yaml
inputs:
  - item_id: ceramic_powder_mixture
    qty: 5.0
    unit: kg
outputs:
  - item_id: green_ceramic_parts
    qty: 5.0
    unit: kg
time_model:
  type: linear_rate
  hr_per_kg: 0.5
  setup_hr: 0.2
  notes: "Mold preparation, pressing, demolding"
energy_model:
  type: kWh_per_kg
  value: 0.3
```

### Time Calculation Attempt

**Scenario:** Process 50 kg of ceramic_powder_mixture

**Formula:** `duration = setup_hr + (input_mass_kg × hr_per_kg)`

**Calculation:**
- Setup time: 0.2 hr
- Input mass: 50 kg
- Processing rate: 0.5 hr/kg
- Duration: 0.2 + (50 × 0.5) = **25.2 hours**

### Analysis

✅ **What works:**
- Clear setup + rate structure
- Unambiguous calculation
- Setup time paid once per run

❓ **What's ambiguous:**
- **Batching behavior:** If you have 50 kg but machine capacity is 5 kg per batch, do you pay setup once (25.2 hr total) or 10 times (0.2 + 2.5 = 2.7 hr per batch × 10 = 27 hr total)?
- **Setup scope:** Is setup per run, per batch, or per shift?
- **Scale interaction:** Does setup_hr change with scale parameter?

⚠️ **Missing specification:**
- Batch size not defined in process
- Relationship between recipe quantity and batch size unclear
- When setup applies (per invocation? per batch? per material change?)

### How It Should Work

**Option A: Setup per process invocation (current assumption)**
- Agent calls `start_process(ceramic_forming_basic_v0, scale=1.0, inputs={ceramic_powder_mixture: 50kg})`
- Duration calculated: 0.2 + (50 × 0.5) = 25.2 hr
- Setup paid once for entire run

**Option B: Setup per batch**
- Process defines `batch_size_kg: 5.0`
- 50 kg requires 10 batches
- Duration: 10 × (0.2 + 5 × 0.5) = 10 × 2.7 = 27 hr
- Setup paid per batch

**Recommendation:** Need to specify batch size and setup scope explicitly.

---

## Example 3: Fixed Batch Time (kg input, count output)

**Process:** `motor_final_assembly_v0`
**Type:** Fixed time per batch, unit-based output
**File:** kb/processes/motor_final_assembly_v0.yaml

### Current Definition

```yaml
inputs:
  - item_id: stator_rotor_lamination_set
    qty: 5.0
    unit: kg
  - item_id: motor_coil_wound
    qty: 2.0
    unit: kg
  - item_id: motor_shaft_steel
    qty: 1.0
    unit: kg
  - item_id: bearing_set_small
    qty: 0.5
    unit: kg
  - item_id: motor_housing_steel
    qty: 3.0
    unit: kg
outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
byproducts:
  - item_id: assembly_loss
    qty: 0.5
    unit: kg
time_model:
  type: fixed_time
  hr_per_batch: 1.0
  notes: "Assemble rotor/stator, bearings, housing, and test run"
```

### Time Calculation Attempt

**Scenario:** Assemble 10 motors

**Questions:**
1. Does `hr_per_batch: 1.0` mean 1 hour produces 1 motor?
2. Or does 1 batch produce multiple motors?
3. What defines a "batch"?

**Attempt 1: Assume 1 batch = 1 motor**
- 10 motors = 10 batches
- Duration: 10 × 1.0 = **10 hours** (sequential processing)

**Attempt 2: Assume 1 batch = output qty from process definition**
- Process defines output: 1.0 unit
- So 1 batch = 1 motor (same as Attempt 1)

**Attempt 3: Assume parallel processing**
- If you have 10 assembly stations
- Duration: **1 hour** (parallel batches)

### Analysis

❌ **What fails:**
- **"Batch" is undefined** - no specification of what constitutes a batch
- **Output is count-based but inputs are kg-based** - how do we scale?
- **Parallel vs sequential unclear** - is time per batch or per total run?

❓ **What's ambiguous:**
- If I want 10 motors, I need 10× the inputs (50 kg laminations, 20 kg coils, etc.)
- Do I pay 1 hr or 10 hr?
- Does the answer depend on how many assembly stations I have?

⚠️ **Missing data:**
- Batch size definition
- Relationship between input mass and output count
- Parallelism model (how many batches can run concurrently?)

### How It Should Work

**Proposal 1: Batch = output quantity**
- Process definition says "1 batch produces 1 unit"
- To make 10 motors: 10 batches × 1 hr = 10 hr (sequential)
- Input requirements scale linearly (10× all inputs)

**Proposal 2: Add batch size and parallelism**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 1.0
  batch_output_qty: 1  # Each batch produces 1 motor
  max_parallel_batches: 1  # Sequential processing
```

**Proposal 3: Separate concurrent resource usage**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 1.0
resource_requirements:
  - machine_id: assembly_station
    concurrent: true  # Ties up station for entire duration
    qty: 1.0
    unit: hr
```

Then simulation can decide based on available resources.

---

## Example 4: Volume Input with Mass-Based Rate (UNIT MISMATCH)

**Process:** `pump_housing_machining_v0`
**Type:** Linear rate, mixed units
**File:** kb/processes/pump_housing_machining_v0.yaml

### Current Definition

```yaml
inputs:
  - item_id: machined_part_raw
    qty: 25.0
    unit: kg
  - item_id: cutting_fluid
    qty: 1.8
    unit: L      # ← LITERS!
    notes: "Consumable coolant/lubricant for machining"
outputs:
  - item_id: pump_housing_machined
    qty: 25.0
    unit: kg
time_model:
  type: linear_rate
  setup_hr: 0.2
  rate_kg_per_hr: 12.0  # ← kg/hr rate!
energy_model:
  type: kWh_per_kg
  value: 3.0
```

### Time Calculation Attempt

**Scenario:** Process 1 batch (25 kg raw part, 1.8 L cutting fluid)

**Question:** Which input drives the rate?

**Attempt 1: Rate based on primary material (machined_part_raw)**
- Input: 25 kg
- Rate: 12.0 kg/hr
- Duration: 0.2 + (25 / 12.0) = 0.2 + 2.08 = **2.28 hours**
- Cutting fluid (1.8 L) is consumable, doesn't affect time

**Attempt 2: Rate based on cutting fluid**
- Can't use rate_kg_per_hr with liters!
- Would need to convert: 1.8 L cutting fluid × density
- But we don't have density of cutting_fluid in items DB
- **CALCULATION FAILS**

### Analysis

❌ **What fails:**
- **Unit heterogeneity:** time_model specifies `rate_kg_per_hr` but one input is in liters
- **Missing conversion data:** No density for cutting_fluid to convert L → kg
- **Ambiguous rate basis:** Which input drives the time?

✅ **What works (if we make assumptions):**
- If we assume cutting_fluid is purely consumable and doesn't drive time
- If we use machined_part_raw (kg) as the basis
- Then calculation is straightforward

❓ **What's ambiguous:**
- Is cutting_fluid a consumable or does it affect processing time?
- Should time_model specify which input is the "driver"?
- What if both inputs affect time (e.g., slower machining with less fluid)?

### How It Should Work

**Option 1: Require all inputs in kg for rate-based processes**
- Convert cutting_fluid specification to kg
- Requires adding density to cutting_fluid item definition
- time_model calculation uses primary input only (machined_part_raw)

**Option 2: Unit-aware time models**
```yaml
time_model:
  type: linear_rate
  setup_hr: 0.2
  rate_kg_per_hr: 12.0
  rate_basis_item: machined_part_raw  # ← Specify which input drives time
```

**Option 3: Support multiple rate units**
```yaml
time_model:
  type: linear_rate
  setup_hr: 0.2
  rate: 12.0
  rate_unit: kg/hr  # ← Explicit compound unit
  rate_basis: machined_part_raw
```

**Recommendation:** Option 2 is simplest - explicitly specify which input drives the rate.

---

## Example 5: Multi-Output Process

**Process:** `water_electrolysis_v0`
**Type:** Fixed batch time, multiple outputs
**File:** kb/processes/water_electrolysis_v0.yaml

### Current Definition

```yaml
inputs:
  - item_id: water
    qty: 1.0
    unit: kg
outputs:
  - item_id: hydrogen_gas
    qty: 0.111
    unit: kg
  - item_id: oxygen_gas
    qty: 0.889
    unit: kg
time_model:
  type: fixed_time
  hr_per_batch: 2.0
  notes: "Continuous electrolysis process"
energy_model:
  type: kWh_per_kg
  value: 15.0
  notes: "Electrical energy for electrolysis, ~50 kWh per kg H2 produced"
```

### Time Calculation Attempt

**Scenario:** Electrolyze 100 kg of water

**Question:** What is a "batch"?

**Attempt 1: Batch = process definition quantities**
- Process defines 1 batch = 1 kg water input
- 100 kg water = 100 batches
- Duration: 100 × 2.0 = **200 hours** (if sequential)

**Attempt 2: Batch = full run**
- 1 batch = entire 100 kg
- Duration: **2 hours**
- But this seems unrealistic - more water should take more time?

**Attempt 3: Fixed time is wrong type**
- This says "continuous electrolysis" in notes
- Should probably be `linear_rate` not `fixed_time`
- If rate: 1 kg water per 2 hr = 0.5 kg/hr
- Duration: 100 kg / 0.5 kg/hr = **200 hours**

### Analysis

❌ **What fails:**
- **Semantic confusion:** Notes say "continuous" but time_model is "fixed_time" (batch)
- **Batch size undefined:** What constitutes one batch?
- **Type mismatch:** fixed_time doesn't make sense for continuous process

✅ **What works:**
- Multi-output doesn't complicate calculation (outputs don't affect time)
- Energy model is per kg input, consistent

❓ **What's ambiguous:**
- Should this be linear_rate instead of fixed_time?
- If fixed_time is correct, what defines batch size?

⚠️ **Inconsistency:**
- Notes describe continuous operation
- time_model specifies batch operation
- These are contradictory!

### How It Should Work

**Option A: Change to linear_rate**
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 2.0  # 2 hours per kg water
  notes: "Continuous electrolysis at 0.5 kg/hr throughput"
```

Then calculation is clear: 100 kg × 2 hr/kg = 200 hr

**Option B: Define batch size explicitly**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 2.0
  batch_size_kg: 10.0  # Each batch processes 10 kg water
  notes: "Batch electrolysis with 10 kg capacity per run"
```

Then: 100 kg / 10 kg per batch = 10 batches × 2 hr = 20 hr

**Recommendation:** Option A - this should be linear_rate based on the description.

---

## Example 6: Boundary Process (No Inputs)

**Process:** `environment_source_v0`
**Type:** Boundary condition
**File:** kb/processes/environment_source_v0.yaml

### Current Definition

```yaml
inputs: []
outputs: []
energy_model:
  type: boundary
  notes: "No energy consumption - freely available environmental resource"
time_model:
  type: boundary
  notes: "No time required - environmental boundary condition"
```

### Time Calculation Attempt

**Scenario:** "Collect" 1000 kg of regolith from environment

**Calculation:**
- type: boundary
- No calculation needed
- Duration: **0 hours** (instantaneous)

### Analysis

✅ **What works:**
- Clear semantic: boundary processes are instantaneous
- No inputs/outputs to track
- No calculation needed

✅ **This is well-defined** - boundary type makes sense for environmental sources.

❓ **Question for simulation:**
- How does simulation handle processes with no inputs?
- Do these need to be invoked, or are outputs just available?
- Should there be a "collection" process with time that uses environment_source as input?

### How It Should Work

Current definition is correct. However:

**Recommendation:** Consider distinguishing:
1. **Source availability** (environment_source_v0) - truly boundary, instant
2. **Collection process** (regolith_collection_v0) - has time_model, uses source as input

Example:
```yaml
# Environment source - no time
id: regolith_source_v0
inputs: []
outputs:
  - item_id: regolith_in_situ  # Unlimited availability
    qty: inf
time_model:
  type: boundary

# Collection process - has time
id: regolith_collection_v0
inputs:
  - item_id: regolith_in_situ
    qty: 1.0
    unit: kg
outputs:
  - item_id: regolith_excavated
    qty: 0.95
    unit: kg
time_model:
  type: linear_rate
  rate_kg_per_hr: 100.0  # Excavation rate
```

This separates availability from collection effort.

---

## Example 7: Invalid time_model Schema

**Process:** `mixing_and_blending_v0`
**Type:** Invalid schema usage
**File:** kb/processes/mixing_and_blending_v0.yaml

### Current Definition

```yaml
inputs:
  - item_id: component_material_a
    qty: 0.5
    unit: kg
  - item_id: binder_simple
    qty: 0.5
    unit: kg
outputs:
  - item_id: blended_mixture
    qty: 1.0
    unit: kg
energy_model:
  total_energy_kwh: 0.3  # ← Invalid field!
time_model:
  total_time_hr: 0.5      # ← Invalid field!
```

### Time Calculation Attempt

**Analysis of schema:**

Expected TimeModel schema (from kbtool/models.py:64-78):
```python
class TimeModel(_BaseModel):
    type: str  # linear_rate, fixed_time, boundary
    hr_per_kg: Optional[float] = None
    rate_kg_per_hr: Optional[float] = None
    setup_hr: Optional[float] = None
    hr_per_batch: Optional[float] = None
```

Actual fields in this process:
- `total_time_hr: 0.5` ← NOT IN SCHEMA

### Analysis

❌ **What fails:**
- **Invalid schema:** `total_time_hr` is not a valid TimeModel field
- **Missing type:** No `type` field (required)
- **Parser should reject this** but apparently doesn't (validation gap!)

❓ **What was intended:**
- Probably meant: `type: fixed_time, hr_per_batch: 0.5`
- Or: `type: linear_rate, hr_per_kg: 0.5`

⚠️ **Validation problem:**
- This file exists in KB, suggesting validation is not strict
- Indexer may not enforce schema
- Creates inconsistency across processes

### How It Should Work

**Fix the process definition:**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 0.5
  notes: "Small batch mixing ~1 kg total"
energy_model:
  type: kWh_per_kg
  value: 0.3
```

**Add schema validation:**
- Indexer should validate time_model against TimeModel schema
- Reject processes with invalid fields
- Enforce required fields (type must be present)

---

## Example 8: Recipe Override Conflict

**Recipe:** `recipe_crushed_ore_v0`
**Process:** `crushing_basic_v0`
**Type:** Recipe est_time_hr vs process time_model conflict

### Current Definitions

**Recipe** (kb/recipes/recipe_crushed_ore_v0.yaml):
```yaml
inputs:
  - item_id: regolith_lunar_mare
    qty: 100.0
    unit: kg
outputs:
  - item_id: crushed_ore
    qty: 98.0
    unit: kg
steps:
  - process_id: crushing_basic_v0
    est_time_hr: 2.0        # ← Recipe says 2 hours
    machine_hours: 2.0
```

**Process** (kb/processes/crushing_basic_v0.yaml):
```yaml
inputs: []
outputs: []
time_model:
  type: linear_rate
  hr_per_kg: 0.3           # ← Process says 0.3 hr/kg
  notes: "primary crushing throughput ~3 kg/hr"
```

### Time Calculation Attempt

**From recipe:**
- est_time_hr: 2.0 hours (explicit)

**From process time_model:**
- Input: 100 kg
- Rate: 0.3 hr/kg (= 3.33 kg/hr throughput)
- Duration: 100 kg × 0.3 hr/kg = **30 hours**

**CONFLICT: 2 hours vs 30 hours!**

### Analysis

❌ **What fails:**
- **Massive discrepancy:** 15× difference between recipe and calculated time
- **Undefined precedence:** Which value should simulation use?
- **No validation:** No check that these are consistent

❓ **What's ambiguous:**
- Is `est_time_hr` an estimate (informational) or an override (authoritative)?
- Is `time_model` a default or a requirement?
- Should recipe steps have inputs/outputs or rely on process definition?

⚠️ **Possible explanations:**
1. Recipe is wrong (should be 30 hr)
2. Process rate is wrong (should be 0.02 hr/kg = 50 kg/hr)
3. Recipe represents a specific optimized case
4. Units are mismatched (recipe assumes different scale?)

### How It Should Work

**Option 1: Recipe overrides process**
- If recipe specifies est_time_hr, use it (ignore time_model)
- Recipe timing is specific to this use case
- Process time_model is generic default

**Option 2: Process time_model is authoritative**
- Recipe est_time_hr is informational/documentation only
- Always calculate from time_model
- Validation should check consistency

**Option 3: Hybrid approach**
- If recipe has est_time_hr, validate it's within ±50% of calculated
- If close enough, use recipe value (allows fine-tuning)
- If far off, warn and use calculated (prevents errors)

**Recommendation:**
1. Validation rule: `abs(est_time_hr - calculated) / calculated < 0.5` (within 50%)
2. If recipe specifies est_time_hr and it's consistent, use it
3. Otherwise calculate from time_model
4. This specific case should be fixed (one of the values is clearly wrong)

---

## Example 9: Count-Based Assembly (Multiple Unit Inputs)

**Recipe:** `recipe_labor_bot_basic_v0`
**Process:** `assembly_basic_v0`
**Type:** Count-based inputs, mass-based time_model

### Current Definitions

**Recipe** (kb/recipes/recipe_labor_bot_basic_v0.yaml):
```yaml
inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: count
  - item_id: robot_arm_link_aluminum
    qty: 2
    unit: unit
  - item_id: motor_electric_small
    qty: 4
    unit: unit
  - item_id: harmonic_drive_reducer_medium
    qty: 4
    unit: count
  # ... 8 more count/unit inputs
outputs:
  - item_id: labor_bot_basic_v0
    qty: 1
    unit: count
steps:
  - process_id: assembly_basic_v0
    est_time_hr: 1.5
    labor_hours: 1.5
```

**Process** (kb/processes/assembly_basic_v0.yaml):
```yaml
inputs: []
outputs: []
time_model:
  type: linear_rate
  hr_per_kg: 0.5        # ← Mass-based rate!
  notes: "labor-dominated batch process"
```

### Time Calculation Attempt

**Problem:** How to calculate time from count-based inputs and mass-based rate?

**Need:** Total mass of all input components

**Attempt:**
1. Look up mass_kg for each input item
2. Sum total mass
3. Apply hr_per_kg rate

**Data needed:**
- machine_frame_small: mass_kg = ?
- robot_arm_link_aluminum: mass_kg = ?
- motor_electric_small: mass_kg = 12 kg (from motor item definition)
- ... (need mass for all 12 inputs)

**If we had all masses (example):**
- Total mass: ~80 kg (hypothetical)
- Rate: 0.5 hr/kg
- Calculated duration: 80 × 0.5 = **40 hours**

**Recipe says:** 1.5 hours

**CONFLICT: 1.5 hours vs 40 hours!**

### Analysis

❌ **What fails:**
- **Unit mismatch:** Recipe uses count/unit, process uses kg
- **Missing data:** Most items don't have mass_kg defined
- **Calculation impossible:** Can't convert count to kg without item mass
- **Huge discrepancy:** Even if we could calculate, likely inconsistent with recipe

❓ **What's ambiguous:**
- Is assembly time based on mass or number of parts?
- Should assembly processes use hr_per_unit instead of hr_per_kg?
- Is est_time_hr the right value regardless of calculation?

⚠️ **Fundamental issue:**
- Assembly processes are often not mass-driven
- Time depends on number of parts, complexity, fitment
- Mass-based time_model doesn't match the physics

### How It Should Work

**Option 1: Add count-based time models**
```yaml
time_model:
  type: linear_rate
  hr_per_unit: 0.15  # 0.15 hours per component
  notes: "assembly time scales with part count"
```

Then: 12 components × 0.15 hr = 1.8 hr (close to recipe's 1.5 hr)

**Option 2: Assembly uses fixed time**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 1.5
  notes: "labor bot assembly is complex but relatively fixed time"
```

**Option 3: Hybrid - base + per-component**
```yaml
time_model:
  type: assembly
  base_hr: 0.5        # Setup and final integration
  hr_per_component: 0.1  # Time per part
  notes: "scales with BOM complexity"
```

**Recommendation:** Assembly processes should use fixed_time or a new assembly-specific model, not mass-based linear_rate.

---

## Example 10: Solar Cell Fabrication (Count Output, Batch Processing)

**Process:** `solar_cell_fabrication_v0`
**File:** kb/processes/solar_cell_fabrication_v0.yaml

### Current Definition

```yaml
inputs:
  - item_id: silicon_single_crystal_ingot
    qty: 9.0
    unit: kg
  - item_id: phosphorus_white
    qty: 0.05
    unit: kg
  - item_id: silver_contact_material
    qty: 0.2
    unit: kg
  - item_id: silicon_nitride_ceramic_v0
    qty: 0.1
    unit: kg
  - item_id: etching_chemicals
    qty: 0.2
    unit: kg
outputs:
  - item_id: solar_cell_set
    qty: 1.0
    unit: unit
time_model:
  type: fixed_time
  hr_per_batch: 12.0
  notes: "Slice wafers, dope junctions, deposit contacts and anti-reflective coating"
energy_model:
  type: kWh_per_kg
  value: 12.0
```

### Time Calculation Attempt

**Scenario:** Produce 50 solar cell sets

**Questions:**
1. How many batches is 50 units?
2. Does each batch produce 1 unit (as process definition shows)?
3. Can batches run in parallel?

**Attempt 1: 1 batch = 1 unit, sequential**
- 50 units = 50 batches
- Duration: 50 × 12.0 hr = **600 hours** (25 days!)

**Attempt 2: Scale inputs**
- Process shows 9.55 kg total input → 1 unit output
- For 50 units: 50 × 9.55 kg = 477.5 kg input
- But time_model is fixed_time, not linear_rate
- Can't calculate from input mass

**Attempt 3: Parallel batching**
- If you have 10 fabrication lines
- 50 batches / 10 lines = 5 batches per line
- Duration: 5 × 12.0 = **60 hours** per line (all finish after 60 hr)

### Analysis

❌ **What fails:**
- **Batch definition unclear:** Does 1 batch = 1 unit?
- **Scalability unknown:** How does this scale to large production?
- **Parallelism not modeled:** Real fab would have multiple process lines

❓ **What's ambiguous:**
- Is hr_per_batch the time for the quantity shown in outputs (1 unit)?
- Or is batch size independent of output quantity?
- How many units does one "batch" produce?

⚠️ **Real-world context:**
- Solar cell fabrication is batch-oriented
- Each batch processes multiple wafers (typically 25-100 wafers per batch)
- A "set" might be dozens of cells
- Current definition doesn't capture this complexity

### How It Should Work

**Option 1: Specify batch output size**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 12.0
  batch_output_qty: 10  # Each batch produces 10 cell sets
  notes: "Batch processes 25 wafers → 10 cell sets"
```

Then: 50 units / 10 per batch = 5 batches × 12 hr = 60 hr

**Option 2: Add capacity and throughput**
```yaml
time_model:
  type: batch_processing
  hr_per_batch: 12.0
  wafers_per_batch: 25
  cells_per_wafer: 4
  notes: "100 cells per batch, packaged as 10 cell sets"
```

More explicit about process physics.

---

## Summary of Findings

### What Works (5/10 examples)

1. ✅ **Simple linear rate (Example 1):** regolith_crushing_grinding - perfect, calculable
2. ✅ **Linear rate with setup (Example 2):** ceramic_forming - calculable with caveats about batching
3. ✅ **Boundary processes (Example 6):** environment_source - well-defined
4. ⚠️ **Multi-output (Example 5):** water_electrolysis - would work if type was corrected

### What Fails (5/10 examples)

5. ❌ **Fixed batch time unclear (Example 3):** motor_final_assembly - batch size undefined
6. ❌ **Unit mismatch (Example 4):** pump_housing_machining - liters vs kg rate
7. ❌ **Invalid schema (Example 7):** mixing_and_blending - using non-existent fields
8. ❌ **Recipe conflict (Example 8):** recipe_crushed_ore - 15× discrepancy
9. ❌ **Count-based assembly (Example 9):** labor_bot - can't calculate from count inputs
10. ❌ **Batch output ambiguous (Example 10):** solar_cell - unclear what batch produces

### Critical Issues Identified

#### 1. Unit Heterogeneity (Examples 4, 9)
- time_model uses kg-based rates
- Inputs may be L (volume), unit/count (discrete), or kg (mass)
- No conversion path from units/count to mass for many items
- **Impact:** Calculation impossible for many processes

#### 2. Batch Size Undefined (Examples 3, 5, 10)
- `hr_per_batch` has no specification of what constitutes a batch
- Unclear if batch = process definition quantities or something else
- No way to calculate how many batches needed for a given quantity
- **Impact:** fixed_time processes are ambiguous

#### 3. Override Hierarchy Undefined (Example 8)
- Recipe `est_time_hr` vs process `time_model` - which wins?
- No validation that they're consistent
- Conflicts exist (2 hr vs 30 hr in Example 8)
- **Impact:** Simulation has no clear rule for which to use

#### 4. Material Properties Missing (Examples 4, 9)
- Items often lack mass_kg, density_kg_per_L
- Can't convert between units without this data
- **Impact:** Calculation blocked even when formula is clear

#### 5. Schema Validation Gaps (Example 7)
- Processes exist with invalid time_model fields
- No enforcement of required fields
- **Impact:** Inconsistency, can't rely on schema

#### 6. Process Type Mismatches (Examples 5, 9)
- Process physics doesn't match time_model type
- Continuous processes marked as batch (Example 5)
- Assembly marked as linear_rate (Example 9)
- **Impact:** Wrong calculations even when technically calculable

### Missing Data Summary

To make time calculation work, need:

1. **Item mass data:**
   - Add `mass_kg` field to all count/unit-based items
   - Add `density_kg_per_L` for all volume-based items

2. **Batch specifications:**
   - Define what "1 batch" means for each fixed_time process
   - Add `batch_size_kg` or `batch_output_qty` fields

3. **Rate basis specification:**
   - For multi-input processes, specify which input drives time
   - Add `rate_basis_item` to time_model

4. **Override rules:**
   - Document precedence: recipe est_time_hr vs process time_model
   - Add validation checks for consistency

5. **Parallelism model:**
   - Specify if processes are inherently sequential or can parallelize
   - Add resource constraints (machine capacity, batch limits)

---

## Recommendations

### Immediate Fixes Needed

1. **Fix Example 5 (water_electrolysis_v0):**
   - Change `type: fixed_time` to `type: linear_rate`
   - Change `hr_per_batch: 2.0` to `hr_per_kg: 2.0`

2. **Fix Example 7 (mixing_and_blending_v0):**
   - Change `total_time_hr: 0.5` to `type: fixed_time, hr_per_batch: 0.5`

3. **Fix Example 8 (recipe_crushed_ore_v0 or crushing_basic_v0):**
   - Either change recipe est_time_hr to 30 hr
   - Or change process hr_per_kg to 0.02 (50 kg/hr rate)

4. **Add schema validation:**
   - Indexer should validate time_model against TimeModel schema
   - Reject processes with invalid/missing fields

### Design Decisions for ADR-010

1. **How to handle unit heterogeneity?**
   - Require item mass/density data?
   - Support unit-aware time models?
   - Restrict to kg-only for rate-based processes?

2. **What is a "batch"?**
   - Always equal to process definition quantities?
   - Separately specified field?
   - Scale-dependent?

3. **Recipe vs process precedence?**
   - Recipe est_time_hr overrides?
   - Always calculate from time_model?
   - Validate consistency?

4. **Assembly processes?**
   - New time_model type for count-based assembly?
   - Fixed time or complexity-based?

5. **Parallelism?**
   - Explicit parallelism model?
   - Resource-constrained scheduling?
   - Simulation-level concern?

---

## Next Steps

Based on these findings:

1. **Create override-hierarchy-problems.md** - Deep dive on precedence rules
2. **Create scaling-and-batching-behavior.md** - Define batch semantics
3. **Survey all processes** - Identify how many have each issue type
4. **Propose schema changes** - Based on real needs discovered here

The real-world examples expose fundamental ambiguities that must be resolved before simulation can reliably calculate process durations.
