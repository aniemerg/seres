NOTE: Historical document predating ADR-012+; references deprecated schema. See docs/kb_schema_reference.md for current rules.

# Process Time & Energy Models: Current State Analysis

**Status:** Investigation
**Date:** 2024-12-28
**Purpose:** Document how time and energy modeling currently works across the KB and simulation systems

## Executive Summary

The KB has **extensive time and energy modeling infrastructure** (time_model in ~891 processes, energy_model widespread), but the **simulation engine doesn't use most of it**. Instead, simulations rely on recipe-level duration fields and agent-provided durations. This creates a disconnect between rich modeling data in processes and actual execution.

## Current Time Modeling Schema

### TimeModel (kbtool/models.py:64-78)

```python
class TimeModel(_BaseModel):
    """
    Time/duration model for a process.

    Types:
    - linear_rate: time = setup_hr + (mass / rate_kg_per_hr)
    - fixed_time: constant time per batch/cycle
    - boundary: terminal node (no time modeled)
    """
    type: str  # linear_rate, fixed_time, boundary
    hr_per_kg: Optional[float] = None  # for linear_rate
    rate_kg_per_hr: Optional[float] = None  # alternative: throughput rate
    setup_hr: Optional[float] = None  # setup time before processing
    hr_per_batch: Optional[float] = None  # for fixed_time
    notes: Optional[str] = None
```

### Coverage

**Processes:**
- ~891 processes have `time_model` field (near 100% coverage)
- Most common pattern: `type: linear_rate` with `rate_kg_per_hr`
- Example:
  ```yaml
  time_model:
    type: linear_rate
    hr_per_kg: 0.3
    notes: "primary crushing throughput ~3 kg/hr"
  ```

**Recipes:**
- Recipe steps CAN have `est_time_hr`, `labor_hours`, `machine_hours`
- But many don't - they rely on underlying process time_model
- Example with timing:
  ```yaml
  - process_id: assembly_basic_v0
    est_time_hr: 3.5
    machine_hours: 3.5
    labor_hours: 3.0
  ```
- Example without timing:
  ```yaml
  - process_id: crushing_basic_v0
    inputs: [...]
    outputs: [...]
    # No timing - relies on process time_model
  ```

## Current Energy Modeling Schema

### EnergyModel (kbtool/models.py:53-61)

```python
class EnergyModel(_BaseModel):
    """
    Energy consumption model for a process.

    Types:
    - kWh_per_kg: energy per unit mass processed
    - kWh_per_batch: energy per batch/cycle
    - kWh_per_unit_output: energy per output unit
    """
    type: str  # kWh_per_kg, kWh_per_batch, kWh_per_unit_output
    value: Optional[float] = None  # numeric value
    notes: Optional[str] = None
```

### Coverage

- Widespread in processes
- Example:
  ```yaml
  energy_model:
    type: kWh_per_kg
    value: 1.5
    notes: "crushing motor power for size reduction to <50mm"
  ```

## How Simulation Currently Works

### Process Execution (base_builder/sim_engine.py:164-166)

```python
def start_process(
    self, process_id: str, scale: float, duration_hours: float
) -> Dict[str, Any]:
```

**Key insight:** Duration is a PARAMETER, not calculated from time_model!

The agent must provide:
1. `process_id` - which process to run
2. `scale` - scaling factor for inputs/outputs
3. `duration_hours` - how long it will take (agent decides!)

**The time_model in the process definition is completely ignored.**

### Recipe Execution (base_builder/sim_engine.py:510-524)

```python
# Get duration
duration = recipe_def.get("duration", 1)
duration_unit = recipe_def.get("duration_unit", "hours")

# Convert duration to hours
if duration_unit == "minutes":
    duration_hours = duration / 60.0
elif duration_unit == "days":
    duration_hours = duration * 24.0
else:  # hours
    duration_hours = float(duration)

# Total duration
total_duration_hours = duration_hours * quantity
```

**Key issues:**
1. Looks for recipe-level `duration` and `duration_unit` fields
2. These fields **don't exist** in most recipes!
3. Falls back to `duration = 1` hour default
4. Doesn't use recipe step `est_time_hr` fields
5. Doesn't use process `time_model` at all

## Current Practice: Who Sets Duration?

### In Simulations

The **base builder agent** is responsible for choosing duration when calling `start_process()`. From ADR-004:

> **Duration-based time model** - Agent specifies duration for all processes (hours/days)

Example from agent perspective:
```python
# Agent starts mining for 8 hours
start_process("regolith_mining_v0", scale=1, duration_hours=8)

# Agent previews what would happen
preview_step(duration_hours=8)

# Agent commits
advance_time(duration_hours=8)
```

**Problem:** The agent must somehow know or estimate duration, but the time_model that could help calculate it is not exposed or used.

### In Recipes (Step-Level)

Some recipe steps specify timing:
```yaml
steps:
  - process_id: metal_fabrication_welding_v0
    inputs: [...]
    outputs: [...]
    est_time_hr: 20.0
    machine_hours: 20.0
    labor_hours: 15.0
```

**Questions:**
- How does `est_time_hr` relate to the process's `time_model`?
- Is it an override? An estimate? A constraint?
- What about `machine_hours` and `labor_hours` - are they additive or concurrent?
- How do these interact with process `time_model.hr_per_batch` or `rate_kg_per_hr`?

**No specification exists for these relationships.**

## Use Cases & Consumers

### 1. Base Builder Simulation

**Current behavior:**
- Ignores time_model completely
- Agent provides duration_hours to start_process()
- Recipe execution uses hardcoded defaults

**What it needs:**
- Ability to calculate realistic durations from mass processed and rate
- Respect both setup time and throughput rates
- Handle scaling (10x the material = 10x the time + 1x setup)

### 2. Indexer (kbtool/indexer.py)

**Current behavior:**
- Validates presence of time_model field
- Warns if missing: `{"field": "time_model", "severity": "soft"}`
- Does NOT validate correctness or calculate anything

**What it could do:**
- Validate time_model makes sense (positive rates, etc.)
- Calculate estimated times for closure analysis
- Flag processes with unrealistic rates

### 3. Closure Analysis

**Current behavior:**
- Builds dependency graphs
- Tracks material flows
- Does NOT consider time or energy

**What it could do:**
- Calculate total time to produce an item
- Identify bottleneck processes (slowest rates)
- Estimate energy requirements for closure

### 4. Energy Calculator (base_builder/energy.py)

**Current behavior:**
- Exists but appears minimal
- Not deeply integrated with simulation

**What it could do:**
- Calculate energy from energy_model based on actual mass processed
- Track cumulative energy consumption
- Validate energy closure (enough power generation?)

## Discovered Anomalies

### 1. Unused `base_rate` Field

Found in 3 files:
- kb/processes/regolith_excavation_processing_v0.yaml
- kb/processes/regolith_mining_lunar_highlands_v0.yaml
- kb/processes/regolith_mining_simple_v0.yaml

```yaml
base_rate: "100 kg/hour"  # NOT part of schema, completely unused
```

**Resolution:** Remove (already done, uncommitted)

### 2. Missing Recipe-Level Duration

Most recipes have NO `duration` or `duration_unit` fields, yet simulation code looks for them:
```python
duration = recipe_def.get("duration", 1)  # Defaults to 1 hour!
```

This means every recipe without explicit duration is treated as 1 hour, regardless of complexity.

### 3. Duplicate Time Specifications

Some recipe steps have BOTH:
- Underlying process with `time_model.rate_kg_per_hr: 100`
- Step override with `est_time_hr: 8.0`

Which should win? No specification exists.

## Identified Problems

### P1: Disconnected Modeling

**Problem:** Rich time_model data exists but isn't used by simulation.

**Impact:**
- Simulation durations are arbitrary (agent guesses or 1hr default)
- No connection between material mass and processing time
- Setup times ignored
- Throughput rates ignored

**Example:**
```yaml
# Process says: "I can crush 3 kg/hr after 0.5hr setup"
time_model:
  type: linear_rate
  setup_hr: 0.5
  rate_kg_per_hr: 3.0

# But simulation just uses whatever the agent says, or 1 hour
```

### P2: Undefined Override Hierarchy

**Problem:** Multiple sources of timing information with no precedence rules.

**Sources (in order of specificity):**
1. Recipe step `est_time_hr` (most specific - this exact step in this recipe)
2. Process `time_model` (generic - applies to all uses of this process)
3. Simulation default (1 hour if nothing else found)

**Questions:**
- Should recipe step timing override process time_model?
- Should they be additive? Multiplicative?
- What if step specifies `est_time_hr` but process has `rate_kg_per_hr`?

### P3: Material-Dependent Models

**Problem:** Generic processes may have different characteristics for different materials.

**Example:** `polishing_basic_v0` might have:
- Fast rate for soft aluminum (10 kg/hr)
- Slow rate for hard ceramic (2 kg/hr)

**Current model:** Single `rate_kg_per_hr` per process, can't vary by material.

**Possible solutions:**
- Material-class-specific rates in time_model?
- Separate processes per material type?
- Scaling factors based on material properties?

### P4: Unit Heterogeneity

**Problem:** Inputs/outputs use different units (kg, m³, unit, L) but time_model uses fixed units (hr_per_kg, rate_kg_per_hr).

**Example:**
```yaml
inputs:
  - item_id: water
    qty: 10
    unit: L  # Liters!
outputs:
  - item_id: steam
    qty: 8
    unit: m³  # Cubic meters!
time_model:
  rate_kg_per_hr: 5.0  # kg per hour - but inputs are in liters!
```

**Current handling:** Unit conversion exists (UnitConverter) but may not integrate with time calculation.

### P5: Batch vs Continuous

**Problem:** Some processes are inherently batch (fixed cycle time), others continuous (throughput rate).

**Current model:** Two types (`fixed_time`, `linear_rate`) but unclear how they interact with different batch sizes.

**Questions:**
- If process has `hr_per_batch: 2.0` and you want to run 10 batches, is it 20 hours or 2 hours (parallel)?
- How does `rate_kg_per_hr` handle very small batches (sub-kg amounts)?

### P6: Parallel Resource Usage

**Problem:** `machine_hours` and `labor_hours` in recipe steps suggest parallelism, but no model for it.

**Example:**
```yaml
est_time_hr: 20.0      # Total time
machine_hours: 20.0    # Machine running whole time
labor_hours: 5.0       # Labor only 5 hours (intermittent?)
```

**Interpretation:**
- Total elapsed time: 20 hours
- Machine utilization: 100% (20/20)
- Labor utilization: 25% (5/20)

**Current handling:** None - these fields are logged but not used in calculations.

## Questions for Further Investigation

1. **Should time_model be required?** Currently "soft" warning if missing. Should it be hard requirement?

2. **Should recipe steps be able to override process time_model?** If yes, what's the semantic?

3. **How should material properties affect time/energy?** Need material-dependent modeling?

4. **What about multi-output processes?** If crushing produces both coarse and fine fractions, does time depend on total mass or specific output?

5. **How to model setup time for batch operations?** Is it per batch, or amortized across continuous operation?

6. **Should energy_model and time_model be coupled?** More time = more energy for most processes.

7. **How to validate time_model realism?** What checks should indexer perform?

8. **Should simulation calculate duration or accept it as parameter?** Current: accepts. Alternative: calculate from time_model.

## Next Steps

1. **Unit Systems Analysis** → Separate document analyzing all unit types and conversion logic
2. **Override Hierarchy Specification** → Define precedence rules for time sources
3. **Material Dependencies** → Explore material-specific modeling approaches
4. **Consumer Analysis** → Deep dive on how each system (simulation, indexer, closure) needs to use this data
5. **Prototype Implementation** → Test different approaches to see what works

## References

- kbtool/models.py:64-78 (TimeModel schema)
- kbtool/models.py:53-61 (EnergyModel schema)
- base_builder/sim_engine.py:164-166 (start_process signature)
- base_builder/sim_engine.py:510-524 (recipe duration handling)
- kb/processes/*.yaml (~891 files with time_model)
- ADR-004 (Base Builder Simulation design)
