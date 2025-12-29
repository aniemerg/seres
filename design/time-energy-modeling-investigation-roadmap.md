# Time & Energy Modeling Investigation Roadmap

**Status:** In Progress
**Date Started:** 2024-12-28
**Goal:** Comprehensive investigation of time and energy modeling architecture leading to ADR-010

## Purpose

This document serves as the master index for a deep architectural investigation into how process time and energy modeling should work across the knowledge base and simulation systems. A fresh Claude Code instance should be able to read this document and understand:

1. What the investigation is about
2. What work has been completed
3. What work remains
4. How to proceed through the investigation
5. How it leads to ADR-010

## Problem Statement

The KB has extensive time and energy modeling infrastructure (`time_model` in ~891 processes, `energy_model` widespread), but the simulation engine doesn't use most of it. Instead, simulations rely on recipe-level duration fields and agent-provided durations. This creates fundamental architectural problems:

1. **Disconnected modeling** - Rich time_model data exists but isn't used
2. **Unit heterogeneity** - Processes use rate_kg_per_hr but inputs may be in liters or units
3. **Undefined override hierarchy** - When recipe steps specify est_time_hr but process has time_model, which wins?
4. **Material dependencies** - Generic processes (polishing) may have different rates for different materials
5. **Multiple consumers** - Indexer, closure analysis, and simulation all need this data differently

These are not simple bugs - they're fundamental architectural questions requiring deep analysis before we can propose solutions in an ADR.

## Investigation Approach

Rather than jumping straight to an ADR, we're creating a series of focused investigation documents that each explore a specific aspect of the problem. These documents serve as "down payments" on ADR-010, exposing the complexity and ensuring any eventual proposal is well-informed.

### Document Series

Each document follows this pattern:
- **Current state** - How things work now
- **Problems identified** - What's broken or unclear
- **Examples** - Real cases from the KB
- **Questions** - What needs to be decided
- **Possible solutions** - Initial exploration (not decisions)

## Investigation Documents

### ✅ Completed

#### 1. `process-time-energy-models-current-state.md`
**Purpose:** Establish baseline understanding of current implementation

**Key findings:**
- TimeModel schema defined with 3 types: linear_rate, fixed_time, boundary
- ~891 processes have time_model (near 100% coverage)
- Simulation ignores time_model, uses agent-provided duration_hours
- Recipe steps can have est_time_hr but relationship to process time_model is unspecified
- Multiple consumers (simulation, indexer, closure) use data differently

**Problems identified:**
- P1: Disconnected modeling (time_model not used)
- P2: Undefined override hierarchy (recipe vs process timing)
- P3: Material-dependent models not supported
- P4: Unit heterogeneity (kg vs L vs units)
- P5: Batch vs continuous unclear
- P6: Parallel resource usage not modeled

**Questions raised:**
- Should time_model be required?
- Should recipe steps override process time_model?
- How should material properties affect time/energy?
- Should simulation calculate duration or accept as parameter?

**References:**
- kbtool/models.py:64-78 (TimeModel schema)
- base_builder/sim_engine.py:164-166 (start_process signature)
- ADR-004 (Base Builder Simulation design)

#### 2. `unit-systems-and-conversions.md`
**Purpose:** Analyze unit heterogeneity and conversion issues

**Key findings:**
- 9 different unit types across 5000+ quantity specifications
- kg dominates (2967 uses) but significant count/volume usage
- UnitConverter exists but doesn't integrate with time_model calculations
- time_model always uses kg-based rates (rate_kg_per_hr, hr_per_kg)

**Problems identified:**
- Fixed units in TimeModel (always kg) but inputs may be L, units, etc.
- No support for compound units (kg/hr, L/min) in converter
- Volume-based inputs with mass-based rates (water: 10L input, 5 kg/hr rate)
- Count-based inputs with mass-based rates (motors: 10 units input, 2 kg/hr rate)
- Multi-unit processes unclear which input drives rate

**Proposed solutions explored:**
- Option 1: Require kg for all rate-based processes
- Option 2: Unit-aware time models (explicit rate_unit: L/hr)
- Option 3: Normalized internal representation
- Option 4: Multiple time models per material type

**References:**
- base_builder/unit_converter.py (current conversion logic)
- Survey: 2967 kg, 1158 unit, 799 hr, 93 each, 22 kWh, 12 count, 8 set, 8 L, 3 kit

#### 3. `time-calculation-real-world-examples.md`
**Purpose:** Walk through actual KB processes to see what works/breaks

**Key findings:**
- Analyzed 10 diverse processes attempting real time calculations
- ✅ 5/10 examples work (simple linear rate, setup+rate, boundary processes)
- ❌ 5/10 examples fail (batch size undefined, unit mismatches, schema violations, conflicts)
- Identified 6 critical issue categories affecting calculation feasibility

**Critical issues identified:**
1. **Unit heterogeneity** - L vs kg, count vs kg, no conversion path for many items
2. **Batch size undefined** - hr_per_batch has no specification of what constitutes a batch
3. **Override hierarchy undefined** - Recipe est_time_hr vs process time_model (2hr vs 30hr conflict found!)
4. **Material properties missing** - Items lack mass_kg, density_kg_per_L needed for conversions
5. **Schema validation gaps** - Processes exist with invalid time_model fields (total_time_hr)
6. **Process type mismatches** - Continuous processes marked batch, assembly marked linear_rate

**Examples analyzed:**
- regolith_crushing_grinding_v0 (✅ works perfectly - ideal case)
- ceramic_forming_basic_v0 (⚠️ works but batching ambiguous)
- motor_final_assembly_v0 (❌ batch size undefined)
- pump_housing_machining_v0 (❌ volume input with mass rate)
- water_electrolysis_v0 (❌ type mismatch - says continuous, marked batch)
- environment_source_v0 (✅ boundary type works)
- mixing_and_blending_v0 (❌ invalid schema - uses total_time_hr)
- recipe_crushed_ore_v0 (❌ 15× discrepancy: 2hr vs 30hr)
- recipe_labor_bot_basic_v0 (❌ count inputs, mass-based rate)
- solar_cell_fabrication_v0 (❌ batch output quantity unclear)

**Missing data summary:**
- Item mass_kg for count-based items
- Item density_kg_per_L for volume-based items
- Batch size specifications for fixed_time processes
- Rate basis (which input drives time) for multi-input processes
- Override precedence rules

**Immediate fixes needed:**
- water_electrolysis_v0: Change fixed_time → linear_rate
- mixing_and_blending_v0: Fix invalid schema (total_time_hr)
- recipe_crushed_ore_v0 or crushing_basic_v0: Fix 15× discrepancy
- Add schema validation to indexer

**References:**
- kb/processes/regolith_crushing_grinding_v0.yaml (ideal example)
- kb/processes/pump_housing_machining_v0.yaml (unit mismatch)
- kb/recipes/recipe_crushed_ore_v0.yaml vs kb/processes/crushing_basic_v0.yaml (conflict)

#### 4. `override-hierarchy-problems.md`
**Purpose:** Define precedence rules when recipe and process specify conflicting timing

**Key findings:**
- Analyzed 4 timing sources: process time_model, recipe est_time_hr, machine_hours/labor_hours, simulation defaults
- Examined 4 real examples including 15× discrepancy case (2hr vs 30hr)
- Evaluated 3 semantic interpretations for each source
- Compared to industry standards (ERP systems, simulation software)
- Proposed 4 precedence rule options with tradeoffs

**Critical analysis:**
1. **Recipe override model** (recommended) - est_time_hr wins when present, calculate from time_model otherwise
2. **Strict calculation model** - always calculate, validate est_time_hr matches
3. **Hybrid model** - calculate if possible, fall back to est_time_hr
4. **Required consistency** - both must exist and match

**Semantic clarifications:**
- `est_time_hr` = elapsed wall-clock time (duration)
- `machine_hours` = machine resource consumption (can differ from elapsed)
- `labor_hours` = labor resource consumption (often intermittent/concurrent)

**Conflicts analyzed:**
- recipe_crushed_ore_v0 (2hr) vs crushing_basic_v0 (calculates 30hr) - **15× error!**
- recipe_labor_bot_basic_v0 (1.5hr, est_time_hr necessary - calculation impossible)
- recipe_machine_solar_thermal_storage_system_v0 (multi-step with all est_time_hr specified)
- recipe_prepared_material_v0 (appears consistent - 0.8hr matches)

**Recommended precedence rule:**
- If recipe has est_time_hr: use it (with >50% mismatch warning)
- Else calculate from time_model
- Rationale: Industry standard, handles impossible calculations, allows specialization

**Validation rules proposed:**
- Error: No time_model AND no est_time_hr
- Warning: est_time_hr differs >50% from calculated
- Info: Using est_time_hr because calculation impossible

**Implementation guidance:**
- Provided Python pseudocode for get_process_duration()
- Specified error/warning/info logging
- Defined fallback chain

**Data cleanup needed:**
- Fix 15× discrepancy (recipe_crushed_ore_v0 or crushing_basic_v0)
- Add item mass_kg to enable count-based calculations
- Survey all recipes with est_time_hr to quantify conflicts (see recipe-step-timing-survey.md)

**References:**
- kb/recipes/recipe_crushed_ore_v0.yaml:20 (2hr specification)
- kb/processes/crushing_basic_v0.yaml:21 (0.3 hr/kg rate)
- Manufacturing ERP systems precedence patterns
- base_builder/sim_engine.py:164 (current implementation ignores all timing)

### ⏳ Planned - High Priority

#### 5. `scaling-and-batching-behavior.md`
**Purpose:** Define how time_model behaves with scale and batch size

**Should cover:**
- Linear scaling: 10x material = 10x time?
- Setup time handling: once per run or once per batch?
- Batch vs continuous processes
- Recipe quantity vs process batch size
- Parallel batch processing vs sequential
- How scale parameter interacts with time_model

**Critical examples:**
```yaml
# Example A: Setup + rate
time_model:
  setup_hr: 2.0
  rate_kg_per_hr: 10.0

# Process 1000 kg:
# Option 1: 2 + (1000/10) = 102 hours (one continuous run)
# Option 2: 10 batches × (2 + (100/10)) = 120 hours (ten 100kg batches)
# Which is correct? How does simulation decide?
```

```yaml
# Example B: Fixed batch time
time_model:
  type: fixed_time
  hr_per_batch: 8.0

# Want to produce 100 units:
# Option 1: If batch size is 10, then 10 batches × 8hr = 80 hours sequential
# Option 2: If you have 10 machines, 10 batches × 8hr = 8 hours parallel
# How is batch size defined? How is parallelism modeled?
```

#### 6. `recipe-step-timing-survey.md`
**Purpose:** Quantify current practice with data

**Should provide:**
- Count: Recipe steps with est_time_hr specified
- Count: Recipe steps relying on process time_model only
- Count: Recipe steps with neither
- Count: Recipe steps with conflicts (est_time_hr vs calculated from time_model)
- Distribution: Are conflicts common or rare?
- Pattern analysis: When do recipes specify timing vs rely on process?

**Method:**
```python
# Scan all recipes
for recipe in all_recipes:
    for step in recipe.steps:
        has_est_time = "est_time_hr" in step
        process = get_process(step.process_id)
        has_time_model = process.time_model is not None

        if has_est_time and has_time_model:
            # Calculate what time_model would give
            calculated = calculate_from_time_model(process, step.inputs)
            if abs(calculated - step.est_time_hr) > threshold:
                # Conflict detected!
```

**Goal:** Understand current patterns to inform design decisions.

### ⏳ Planned - Medium Priority

#### 7. `material-dependent-models.md`
**Purpose:** Explore material-specific time/energy characteristics

**Should cover:**
- Use cases requiring material-dependent rates
- Examples: polishing (fast for aluminum, slow for ceramic)
- Examples: chemical reactions (vary by substrate)
- Possible approaches:
  - Multiple time_models per process (selected by material_class)
  - Material-specific scaling factors
  - Separate processes per material type
  - Material properties that affect time (hardness, density, etc.)

**Questions:**
- How common is material dependence in real processes?
- Can we use material_class for selection?
- What if multiple inputs have different materials?
- How to validate/test material-specific models?

#### 8. `validation-strategy.md`
**Purpose:** Define how to validate time/energy models are realistic

**Should cover:**
- What makes a time_model "valid"?
- Sanity checks (time > 0, rates reasonable for process type)
- Cross-validation (est_time_hr vs calculated, energy/time coupling)
- Real-world benchmarks (if available)
- Indexer validation rules
- Testing strategy for new implementations

**Examples of validation rules:**
```python
# Rule 1: Rate must be positive
assert time_model.rate_kg_per_hr > 0

# Rule 2: Setup time must be reasonable
assert time_model.setup_hr < 100  # No 100+ hour setups

# Rule 3: Energy/time coupling makes sense
power = (energy_model.value * mass) / (time_model.rate_kg_per_hr * hours)
assert 0.1 < power < 10000  # Reasonable power range 100W to 10MW

# Rule 4: Consistency with recipe steps
if step.est_time_hr:
    calculated = calculate_from_time_model(process, step.inputs)
    assert abs(calculated - step.est_time_hr) / step.est_time_hr < 0.5  # Within 50%
```

#### 9. `migration-impact-analysis.md`
**Purpose:** Understand what breaks if we change how this works

**Should cover:**
- Current simulations - what breaks if we calculate duration from time_model?
- Processes needing time_model fixes
- Processes with invalid/broken time_models
- Recipe steps needing updates
- Backward compatibility strategy
- Phased migration approach
- Testing strategy

**Key questions:**
- Can we run both modes (calculate vs agent-specified) during transition?
- How to identify high-risk changes?
- What's the rollback plan if problems emerge?
- How to validate migration didn't break things?

#### 10. `parallel-resource-usage-model.md`
**Purpose:** Understand concurrent vs sequential resource usage

**Should analyze:**
```yaml
est_time_hr: 20.0      # Total elapsed time
machine_hours: 20.0    # Machine utilization
labor_hours: 5.0       # Labor utilization
```

**Questions:**
- Is labor intermittent (5 hours spread over 20) or concurrent (5 workers × 1hr)?
- Do these specify resource requirements or resource consumption?
- How does this affect scheduling?
- Should time_model calculate these separately?
- What's the semantic relationship?

### ⏳ Planned - Lower Priority

#### 11. `consumers-and-use-cases.md`
**Purpose:** Deep dive on how different systems need time/energy data

**Should cover:**
- **Simulation:** Needs actual durations for time advancement
- **Indexer:** Needs validation that time_model is sensible
- **Closure analysis:** Could use time to find bottlenecks
- **Energy planning:** Needs total energy requirements
- **Resource scheduling:** Needs machine/labor hours
- Each consumer's specific requirements
- Conflicts between consumers
- Unified model that serves all?

#### 12. `alternative-architectures.md`
**Purpose:** Explore fundamentally different approaches

**Could explore:**
- Power-based model (specify kW, calculate kWh from time)
- Event-based simulation (process events, not continuous time)
- Discrete-event simulation framework
- Stochastic time models (mean + variance)
- Learning-based time estimation (from execution logs)

## Workflow for Fresh Claude Code Instance

If you're a fresh Claude Code instance working on this investigation:

### 1. Read This Document First
You're reading it now. Good!

### 2. Read Completed Documents
- Read `process-time-energy-models-current-state.md`
- Read `unit-systems-and-conversions.md`
- Understand the current state and core problems

### 3. Check TODO Status
Look at the TODO list in this document to see what's next.

### 4. Pick Next Document
Choose the next planned document based on priority:
- **High priority first:** override-hierarchy, real-world examples, scaling/batching
- Work through them sequentially or in parallel as appropriate

### 5. Create Document
For each investigation document:
- Use similar structure to completed documents
- Focus on current state → problems → examples → questions → possible solutions
- Be thorough but stay focused on that document's specific scope
- Cross-reference other documents where relevant
- Don't make decisions yet (that's for the ADR)

### 6. Update This Roadmap
When you complete a document:
- Move it from "Planned" to "Completed"
- Add key findings summary
- Update cross-references

### 7. Synthesize for ADR
Once all or most documents are complete:
- Read through all investigation documents
- Identify common themes and critical decisions
- Draft ADR-010 based on comprehensive understanding
- ADR should reference investigation documents for details

## Success Criteria

The investigation is ready for ADR-010 when:

1. ✅ Current state is thoroughly documented
2. ✅ Unit systems and conversions analyzed
3. ✅ Real-world examples tested (10 cases analyzed, 6 critical issues identified)
4. ✅ Override hierarchy specified (precedence rule recommended, 4 options analyzed)
5. ⏳ Scaling behavior defined
6. ⏳ Recipe timing practice quantified
7. ⏳ Material dependencies explored
8. ⏳ Validation strategy proposed

Optional (can defer):
- Migration impact understood
- Parallel resource model defined
- Consumer needs documented
- Alternative architectures considered

## ADR-010 Scope

Based on these investigations, ADR-010 should address:

1. **Decision:** Should simulation calculate duration from time_model or accept as parameter?
2. **Decision:** How to handle unit heterogeneity (kg vs L vs units)?
3. **Decision:** Override hierarchy (recipe est_time_hr vs process time_model)
4. **Decision:** Material-dependent time models - support or not?
5. **Decision:** Scaling behavior specification
6. **Decision:** Validation requirements

Each decision should be informed by the investigation documents, not made in a vacuum.

## Current Status

**Date:** 2024-12-28
**Progress:** 4/12+ documents completed (33%)
**Next:** Scaling/batching behavior or recipe timing survey

**Recently completed:**
- ✅ Current state documentation (comprehensive)
- ✅ Unit systems analysis (thorough)
- ✅ Real-world examples walkthrough (10 processes, 50% success, 6 critical issues)
- ✅ Override hierarchy analysis (precedence rule recommended, 4 options evaluated)

**Up next (high priority):**
- ⏳ Scaling and batching behavior (batch size undefined in multiple processes)
- ⏳ Recipe timing practice quantified (survey needed to quantify conflicts)

## Notes for Reviewers

This investigation is intentionally comprehensive and may seem slow. The goal is NOT to quickly write an ADR, but to deeply understand a complex architectural problem before proposing solutions.

Each investigation document serves as:
1. **Documentation** of how things currently work (or don't)
2. **Problem identification** exposing issues that need resolution
3. **Evidence** for eventual ADR decisions
4. **Reference** for future developers

Expect this investigation to take significant time. The alternative (rushing to an ADR without deep understanding) will lead to poor decisions that we'll regret later.

## Questions?

If you're unsure how to proceed:
1. Re-read this roadmap
2. Check the completed documents for examples
3. Pick the highest priority unfinished document
4. Follow the structure of completed documents
5. Focus on understanding and documenting, not deciding

The eventual ADR will make better decisions because of this thorough groundwork.
