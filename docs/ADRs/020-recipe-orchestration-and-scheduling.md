# ADR 020: Recipe Orchestration, Resource Accounting, and Process Scheduling

**Status:** Proposed
**Date:** 2026-01-08 (Initial), 2026-01-09 (Revised)
**Supersedes:** ADR-005 (Recipe Step Processing)
**Related:** ADR-003 (Process-Machine Refactor), ADR-004 (Base Builder Simulation), ADR-012 (Process Types and Time Model), ADR-013 (Recipe Override Mechanics), ADR-014 (Energy Models), ADR-016 (Unit Conversion), ADR-018 (Recipe Inputs/Outputs Validation), ADR-019 (BOM-Recipe Relationship)

---

## Context

### What Exists Today

The simulation system has several well-functioning components:

- **Recipe validation system** (ADR-018, ADR-019): Recipes define multi-step manufacturing sequences with validated inputs and outputs
- **Material class matching** (ADR-004): Flexible material substitution allows processes to accept equivalent materials
- **Process definitions with time models** (ADR-012): Processes specify how to calculate execution duration
- **Resource requirements** (ADR-003): Processes declare machine needs with concrete machine_id references
- **Recipe override mechanics** (ADR-013): Recipe steps can override process time and energy models

### Implementation Status of ADR-005

ADR-005 (Recipe Step Processing) defined a three-phase implementation plan:

- **Phase 1**: ✅ Machine existence validation - IMPLEMENTED
- **Phase 2**: ⏳ Machine-hour tracking, energy accounting - NOT IMPLEMENTED
- **Phase 3**: ⏳ Sequential step execution, intermediate materials - NOT IMPLEMENTED

Result: Recipes validate correctly but execute as opaque black boxes.

### Current Simulation Model

The current simulation operates as follows:

1. Agent calls `start_process(process_id, scale, duration_hours)`
2. System creates single `ActiveProcess` with `ends_at` timestamp
3. A recipe with N steps creates ONE ActiveProcess representing the entire recipe
4. No visibility into intermediate steps or materials
5. No machine utilization tracking
6. Duration provided by agent, not calculated from time_model

## Problem Statement

### Problem 1: Recipes as Black Boxes

When executing a recipe with multiple steps, the system creates a single opaque ActiveProcess:

- **Intermediate materials invisible**: A recipe with steps producing materials at step 3, 5, and 7 only shows final output
- **Per-step resource consumption hidden**: Can't determine which step used which machine for how long
- **No parallelization**: Steps that could run concurrently (independent dependencies) execute sequentially
- **Event log incomplete**: Shows recipe_start and recipe_complete but not individual step execution
- **Visualization broken**: Discovered during implementation - `process_timeline.png` couldn't display recipe internals because recipe events are separate from process events

Example: Recipe to build robot arm link has 3 steps (casting → machining → inspection). Current system shows only "recipe_robot_arm_link_aluminum_v0 started" and "completed." The 8.7kg of cast_metal_parts produced at step 1 never appears in inventory or events.

### Problem 2: No Resource Accounting

Machines are validated for existence (ADR-005 Phase 1) but never tracked:

- **No conflict detection**: Two recipes can "use" the same CNC mill at the same time without detection
- **No utilization measurement**: Can't answer "how many machine-hours did this recipe consume?"
- **No availability checking**: Can't determine "is cnc_mill_v0 available at t=5.0?"
- **No double-booking prevention**: System allows scheduling conflicting uses of single machines

The simulation performs careful accounting of materials (consumed/produced) and energy (kWh consumed) but completely ignores machine utilization.

### Problem 3: Time Models Ignored

ADR-012 defines how to calculate process duration from time_model (linear_rate, batch, fixed_time), but this specification is never used:

- Agent manually provides `duration_hours` parameter
- time_model field exists in process definitions but is never read
- No connection between KB specification and simulation behavior
- Calculations defined but not implemented

Example: A process defines `time_model: {type: "linear_rate", rate: 2.0, rate_unit: "kg/hr", scaling_basis: "output_qty"}`. The system should calculate duration = output_qty / rate. Instead, agent provides duration directly.

### Problem 4: Machine-Hours vs Elapsed Time Confusion

The system conflates two distinct measurements:

- **Elapsed time**: How long the process takes (from time_model)
- **Machine utilization**: How long machines are occupied (from resource_requirements)

These are often different. Example:

```yaml
time_model:
  type: batch
  hr_per_batch: 8.0  # Process takes 8 hours total

resource_requirements:
  - machine_id: heat_treatment_furnace_v0
    qty: 6.0  # Furnace used for 6 hours (heating + soaking)
    unit: hr
  # 2 hours of cooling doesn't require the furnace
```

The process takes 8 hours but only reserves the furnace for 6 hours. Current model can't represent this distinction.

### Problem 5: No Automatic Orchestration

Agent must manually start every process:

- No scheduler to progress through recipe steps
- Agent workflow: start step 1 → advance time → check completion → start step 2 → advance time → ...
- Agent forced to micromanage timing
- Can't simply "start recipe and advance time to completion"

This creates unnecessary complexity in agent logic and makes the simulation feel like a low-level API rather than a simulation engine.

### Problem 6: Sequential Blocking Model

The `ActiveProcess.ends_at` field implies processes block until completion:

- Prevents pipelining (starting step 2 while step 1 finishing)
- Prevents parallelism (steps with independent dependencies must serialize)
- Can't model realistic factory operations where multiple processes run simultaneously
- Forces sequential execution even when not required by dependencies

### Problem 7: Inconsistent ADR Implementation

ADR-005's vision was never fully realized:

- Phase 1 implemented, Phases 2-3 deferred indefinitely
- System ossified around the Phase 1 "temporary" solution
- Unclear how to progress from Phase 1 to complete implementation
- Original architecture (recipes as processes) conflicts with needs (recipes orchestrating processes)

## Investigation & Root Causes

### Root Cause 1: Conceptual Model Confusion

The original design treated recipes as a special kind of process (inheritance relationship). Reality: recipes coordinate multiple processes (composition relationship). This conceptual mismatch led to treating complex multi-step procedures as atomic operations.

### Root Cause 2: Deferred Implementation

ADR-005 Phase 1 was implemented as "for now, just validate machines exist." Phases 2-3 were never prioritized. The system stabilized around the Phase 1 model. Technical debt accumulated as other features built on the incomplete foundation.

### Root Cause 3: Agent Responsibility Unclear

Ambiguity about division of responsibility:

- Who calculates duration? Agent or system?
- Who schedules the next step? Agent or system?
- Who tracks machine utilization? Agent or system?

Resulted in system doing minimal work and agent performing manual scheduling.

### Root Cause 4: Resource Tracking Complexity Underestimated

Machine reservation requires:

- Time-based conflict detection (overlap checking)
- Distinguishing machine-hours from elapsed time
- Managing reservations across parallel executions

This was more complex than initially apparent. Easier to skip tracking than implement correctly. But "we'll add it later" never happened.

## Decision

### Core Principle

**Recipes are orchestrators, not processes.**

A recipe defines a dependency graph of process executions. Each step executes as an individual process with full transparency, resource accounting, and automatic scheduling.

### Key Design Principles

#### 1. Transparency

Every recipe step is a visible process instance:

- Intermediate materials appear in inventory after each step
- Per-step resource consumption tracked separately
- Events emitted for each step start and completion
- Parallel steps visible as simultaneously active processes
- Event log captures complete execution history

This enables detailed analysis, debugging, and visualization of manufacturing sequences.

#### 2. Proper Time Modeling

Duration calculated from time_model per ADR-012:

- System calculates duration, not agent
- Respects time_model type (linear_rate, batch, fixed_time)
- Step overrides respected per ADR-013
- Agent controls clock (advance_time) but not individual durations

This enforces consistency between KB specification and simulation behavior.

#### 3. Resource Accounting

Track machines properly with time-based reservations:

- Machine reservations with explicit start and end times
- Conflict detection prevents double-booking
- Distinguish machine-hours (utilization) from elapsed time (duration)
- Multiple processes can use different machines simultaneously
- Enables "is machine available?" queries

Example: An 8-hour heat treatment process reserves furnace for 6 hours (heating + soaking). The 2-hour cooling phase doesn't require the furnace, which becomes available for other processes.

#### 4. Automatic Orchestration

Scheduler manages process lifecycle:

- Agent controls simulation clock via `advance_time(hours)`
- Scheduler automatically activates processes when their scheduled time arrives
- Dependencies resolved automatically
- Agent doesn't micromanage happy-path execution

This simplifies agent logic and makes the simulation engine feel like an engine rather than a low-level API.

#### 5. Agent Control

Observability and intervention levers when issues arise:

- Query detailed status (what's running, what's scheduled, what's blocked)
- Detect blocking issues (material shortages, machine conflicts)
- Intervene when needed (pause, cancel, reschedule, reassign machines)
- Emergency operations (force stop, declare machine unavailable)

Agent has full control without requiring micromanagement.

### Clean Break

This ADR supersedes ADR-005's approach. There is no backward compatibility mode. Existing simulations require migration. This clean break simplifies implementation and reduces long-term confusion.

## Architecture

### 1. Process Lifecycle (Three States)

Processes move through three distinct states:

**Scheduled**: Process planned for future execution
- Start time determined by dependencies and machine availability
- Materials not yet consumed (but reserved)
- Machines not yet occupied (but reserved)
- Waiting for: time to arrive AND dependencies to complete AND materials available

**Active**: Process currently executing
- Started at specific simulation time
- Materials consumed from inventory
- Machines occupied and unavailable for other processes
- Will complete at `started_at + duration_hours`

**Completed**: Process finished
- Outputs added to inventory
- Machines released (available for other processes)
- Historical record for tracking and analysis
- Immutable (completed processes never change)

This three-state model provides clear lifecycle semantics and enables proper resource management.

### 2. Recipe Execution Model

When agent calls `run_recipe(recipe_id)`, the following occurs:

#### Step 0: Create Recipe Run Instance and Feasibility Check

Before any scheduling:

1. Generate unique `recipe_run_id` for this execution instance
2. **Perform feasibility check** against current inventory:
   - Calculate total material requirements across all steps
   - Verify all required inputs are currently available
   - If any materials missing: immediately pause recipe, emit blocking issue, return without scheduling
3. Create RecipeExecution tracking record linking recipe_id to recipe_run_id

This pre-flight check ensures that running this recipe alone will not fail due to missing inputs. Cross-recipe material contention is handled later during step activation, but this local guarantee prevents obvious failures.

**Rationale**: Without this check, a recipe could schedule all steps successfully, then fail at step 5 when materials are missing. The failure mode would be delayed and harder to diagnose. Checking upfront provides immediate feedback.

#### Step 1: Parse Recipe into Dependency Graph

Analyze recipe steps to determine:
- Which steps depend on which (sequential relationships)
- Which steps are independent (parallel opportunities)
- Earliest possible start time for each step

Example: Recipe with steps A → B → C (sequential) and D → E (parallel branch) produces dependency graph showing B waits for A, C waits for B, E waits for D, but D can start immediately if resources available.

#### Step 2: Calculate Duration and Scale Quantities for Each Step

For each step:
- Retrieve process definition from KB
- Use time_model to calculate duration per ADR-012
- Apply step overrides if present (ADR-013)
- **Use ADR-016 unit conversion pipeline**:
  - Parse compound units (e.g., `kg/hr`, `L/min`)
  - Normalize time units to hours
  - Convert between mass/volume/count using density or item mass/volume when required
- Scale inputs, outputs, and energy consistently based on:
  - Specified duration (derive output qty from time)
  - Target output qty (derive time from output)
  - Batch count (derive time, inputs, outputs from batches)

All derived quantities must scale consistently to maintain material and energy balance.

Example: Process has `time_model: {type: "linear_rate", rate: 5.0, rate_unit: "kg/hr", scaling_basis: "output_qty"}`. Recipe step specifies output of 15kg. Unit conversion normalizes rate to hours. Duration = 15kg / 5.0 kg/hr = 3.0 hours. Inputs and energy scale proportionally.

#### Step 3: Check Machine Availability

For each step's resource_requirements:
- Query machine_usage table for each required machine
- Find time windows when ALL required machines are free
- If conflict detected, delay step start until machines available

Example: Step needs cnc_mill_v0 for 2 hours starting at t=5.0. If cnc_mill_v0 is reserved 4.0-6.5, step delayed to start at t=6.5.

#### Step 4: Create Scheduled Processes

Create one ScheduledProcess per recipe step containing:
- **process_run_id**: Unique ID for this process execution instance (generated)
- **process_id**: Which process definition to run (from recipe step)
- **scheduled_start**: When to start (based on dependencies and machine availability)
- **duration_hours**: How long it runs (calculated from time_model)
- **inputs_reserved**: What it will consume (from step or recipe inputs)
- **outputs_expected**: What it will produce (from step or recipe outputs)
- **energy_kwh**: Energy consumption (calculated at scheduling time from ADR-014 energy_model)
- **machine_reservations**: Which machines it needs (see Machine Reservation System section)
- **parent_recipe_run_id**: Link back to this recipe execution instance
- **parent_recipe_id**: Link back to recipe definition (for reference)
- **step_index**: Position in recipe sequence
- **dependencies**: List of process_run_ids that must complete first

These scheduled processes are not yet active - they're planned for future execution. Each has a unique process_run_id that distinguishes this execution from other runs of the same process definition.

#### Step 5: Activate Immediately Ready Steps

For steps with:
- No dependencies (or all dependencies already satisfied)
- Start time equals current time
- Materials available now

Move from scheduled to active immediately. For most recipes, this is the first step.

### 3. Machine Reservation System

Machines are tracked via time-based reservations with explicit full-duration and partial-duration semantics.

**Data Structure**: `machine_usage` table maps machine_id → list of (start_time, end_time, process_run_id) tuples

**Reservation Types**:

Every process must have **at least one full-duration reservation** - a machine that remains reserved for the entire process execution. Additional machines may have partial reservations.

1. **Full-Duration Reservation** (unit: `count` or `unit`):
   - Reserves `qty` machine instances for entire process duration
   - Released only at `process_complete` event
   - Specified with `unit: count` or `unit: unit` in resource_requirements
   - Reservation window: `[started_at, started_at + duration_hours]`
   - Example: `qty: 2, unit: count` reserves 2 instances of the machine for full duration

2. **Partial Reservation** (unit: `hr`):
   - Reserves machine for specific number of hours less than process duration
   - **Front-loaded**: Reservation starts at process start
   - Released at `process_started_at + qty` (not at process completion)
   - Specified with `unit: hr` in resource_requirements
   - Reservation window: `[started_at, started_at + qty]`
   - Example: `qty: 6.0, unit: hr` reserves machine for first 6 hours only

**Validation Rule**: A process is invalid unless it has at least one resource_requirements entry with `unit: count` or `unit: unit` and `qty >= 1`. This ensures at least one machine is reserved for the full duration.

**Rationale**: Processes must use machines. A process with only partial reservations would have periods where no machines are reserved, which doesn't match manufacturing reality. At minimum, a process requires operator attention, workspace, or oversight for its full duration.

**Conflict Detection**: New reservation conflicts if it overlaps any existing reservation for that machine. Two reservations overlap if: `NOT (new_end <= existing_start OR new_start >= existing_end)`

**Machine-Hours vs Elapsed Time**:
- time_model duration = **elapsed time** (how long process takes)
- resource_requirements with `unit: hr` = **machine-hours** (how long machine occupied)
- resource_requirements with `unit: count/unit` = **full-duration** (entire process)

Example showing both types:

```yaml
# Process takes 8 hours total
time_model:
  type: fixed_time
  hr_per_batch: 8.0

resource_requirements:
  # Full-duration reservation: operator required entire time
  - machine_id: labor_bot_general_v0
    qty: 1
    unit: count

  # Partial reservation: furnace only needed for 6 hours
  - machine_id: heat_treatment_furnace_v0
    qty: 6.0
    unit: hr

# Reservations created:
# - labor_bot_general_v0: [t, t+8] (full duration)
# - heat_treatment_furnace_v0: [t, t+6] (partial, front-loaded)
# After 6 hours, furnace available for other processes
# Process continues 2 more hours (cooling phase with operator oversight)
```

### 4. Scheduler Operation

The scheduler activates when agent calls `advance_time(hours)`. To ensure accurate event timing, the scheduler processes events **in chronological order** rather than batch processing.

#### Algorithm: Event-Driven Time Advancement

When agent calls `advance_time(delta_hours)`:

```
target_time = current_time + delta_hours

while current_time < target_time:
    # Find next event in time interval
    next_event_time = min(
        min(p.started_at + p.duration_hours for p in active_processes),
        min(p.started_at + res.qty for p in active_processes for res in p.partial_reservations),
        min(p.scheduled_start for p in scheduled_processes)
    )

    if next_event_time > target_time:
        # No more events in interval
        current_time = target_time
        break

    # Advance to next event time
    current_time = next_event_time

    # Process all events at this time
    process_completions(current_time)
    release_partial_reservations(current_time)
    activate_scheduled_processes(current_time)
    check_for_blocking_issues(current_time)

emit_event("time_advanced", from=old_time, to=target_time)
```

This approach ensures:
- Events emitted at their actual occurrence time (not batched at end)
- Processes can complete and release resources mid-interval
- Those released resources can be used by processes starting later in same interval
- Event log has accurate chronological ordering

#### Process Completions

When `current_time` reaches `process.started_at + process.duration_hours`:

1. Add outputs to inventory
2. Release **all** machine reservations (full-duration and any remaining partial)
3. Move from active list to completed list
4. Emit `process_complete` event with current_time as completion time
5. Update parent recipe completion tracking

#### Partial Reservation Releases

When `current_time` reaches `process.started_at + partial_reservation.qty`:

1. Find all active processes with partial reservations ending at current_time
2. For each, release that specific machine reservation
3. Keep process in active list (still running, just released one machine)
4. Machine becomes available for other processes to reserve

This enables resource sharing: furnace freed after 6 hours can be used by another process while original process continues cooling.

#### Scheduled Process Activation

When `current_time` reaches `scheduled_process.scheduled_start`:

1. Verify all dependencies satisfied (prerequisite process_run_ids in completed list)
2. Verify materials available in inventory
3. If ready:
   - Consume inputs from inventory
   - Book energy consumption (using ADR-014 energy_model)
   - Move from scheduled list to active list
   - Emit `process_start` event with current_time
4. If not ready (materials missing):
   - Flag as blocking issue
   - Pause parent recipe run
   - Keep in scheduled list for retry

This enables automatic progression through recipe steps while handling resource contention.

#### Blocking Issue Detection

After processing all events at current_time, check for problems:

- Scheduled processes past their start time but couldn't activate
- Material shortages (inputs not in inventory)
- Unresolved dependencies (shouldn't happen, but detect)
- Machine conflicts (shouldn't happen if scheduled correctly)

For each blocking issue:
- Emit `blocking_issue` event with details and resolution options
- Automatically pause affected recipe run
- Keep processes in scheduled list for potential retry after resolution

### 5. Event Model

Events emitted at two levels:

#### Recipe-Level Events

- **recipe_start**: Recipe execution initiated, dependency graph built, all steps scheduled
- **recipe_paused**: Recipe execution paused (manually by agent or automatically due to blocking issue)
- **recipe_resumed**: Paused recipe execution resumed, pending steps rescheduled
- **recipe_complete**: All steps completed successfully
- **recipe_cancelled**: Recipe execution cancelled by agent

#### Process-Level Events

- **process_scheduled**: Process scheduled for future execution (includes scheduled_start time)
- **process_start**: Process activated (materials consumed, machines occupied)
- **process_complete**: Process finished (outputs produced, machines released)
- **process_failed**: Process failed (materials lost or returned depending on failure mode)

#### Event Hierarchy and Instance IDs

All events include runtime instance IDs:

**Recipe-level events** include:
- `recipe_run_id`: Unique ID for this execution of the recipe
- `recipe_id`: Recipe definition being executed (for reference)

**Process-level events** include:
- `process_run_id`: Unique ID for this execution of the process
- `process_id`: Process definition being executed (for reference)
- `parent_recipe_run_id`: Link to parent recipe execution (if part of recipe)
- `parent_recipe_id`: Recipe definition (for reference)
- `step_index`: Position in recipe sequence (if part of recipe)

This creates a parent-child relationship without unifying event types. Recipe events provide high-level orchestration context. Process events provide detailed execution tracking. The runtime IDs distinguish multiple executions of the same definition.

This separation enables:
- Recipe-focused analysis (total time, resource consumption)
- Process-focused analysis (per-step performance, bottlenecks)
- Visualization at both levels (recipe bars and process bars)
- Tracking multiple concurrent executions of same recipe/process

### 6. Agent Control Operations

The agent has three categories of operations.

**Interface Note**: These operations are described as conceptual functions for clarity, but agents interact with the simulation through the **CLI interface**. The simulation CLI provides commands that map to these operations. For example, `get_recipe_status(recipe_run_id)` might be invoked via a CLI command like `sim status recipe <recipe_run_id>` or similar. The exact CLI syntax is an implementation detail. This ADR specifies *what operations exist* and *what they do*, not the specific CLI command structure.

The agent has three categories of operations:

#### Observability Operations (Read-Only)

Query state without modifying execution:

- **get_recipe_status(recipe_run_id)**: Overall progress, completion estimate, blocking issues for specific recipe execution
- **get_step_status(recipe_run_id, step_index)**: Detailed single-step state and resource usage
- **get_scheduled_processes()**: List of all processes queued to run (across all recipes)
- **get_active_processes()**: List of all processes currently running (across all recipes)
- **get_blocking_issues(recipe_run_id)**: Material shortages, conflicts, failures for specific recipe execution
- **simulate_recipe_completion(recipe_id)**: Project forward for NEW run of recipe: resource needs, completion time, feasibility

Note: Most operations use `recipe_run_id` (specific execution instance) not `recipe_id` (definition). The `simulate_recipe_completion` is an exception - it projects a hypothetical new run.

These operations enable agents to understand system state and make informed decisions.

#### Control Operations (Modify Execution)

Modify recipe execution when issues arise:

- **pause_recipe(recipe_run_id)**: Hold execution - active processes continue to completion, scheduled processes won't activate
- **resume_recipe(recipe_run_id)**: Continue paused recipe - reschedule pending steps from current time
- **cancel_recipe(recipe_run_id, return_materials)**: Abort execution - remove scheduled processes, optionally return unconsumed materials
- **reschedule_step(recipe_run_id, step_index, new_start_time)**: Manually change when scheduled step will start (for conflict resolution)
- **reassign_machine(recipe_run_id, step_index, old_machine_id, new_machine_id)**: Swap which machine a scheduled step uses (for handling unavailability)
- **insert_step(recipe_run_id, after_step_index, process_id, inputs, outputs)**: Add new step mid-recipe (for inspection, rework, cleaning)

All control operations act on specific recipe execution instances (recipe_run_id), not recipe definitions.

These operations give agents precise control over recipe execution without requiring micromanagement.

#### Emergency Operations

Handle exceptional situations:

- **force_stop_process(process_run_id, return_materials)**: Immediately halt active process instance, optionally return materials
- **set_machine_unavailable(machine_id, from_time, to_time, reason)**: Mark machine unavailable for maintenance or failure, automatically reschedule affected processes

### 7. Typical Agent Workflow

**Normal Recipe Execution:**

```
Agent: run_recipe("recipe_robot_arm_link_aluminum_v0")
  → System schedules 3 processes (casting, machining, inspection)
  → System activates step 0 (casting) immediately
  → Returns RecipeExecution object

Agent: advance_time(5.0)
  → System completes casting (step 0)
  → System activates machining (step 1)
  → System continues machining

Agent: advance_time(5.0)
  → System completes machining (step 1)
  → System activates inspection (step 2)
  → System completes inspection (step 2)
  → Recipe complete

Agent: get_recipe_status("recipe_robot_arm_link_aluminum_v0")
  → Returns: {status: "completed", steps_completed: 3, total_time: 10.0}
```

**Handling Material Shortage:**

```
Agent: run_recipe("recipe_X")
  → System schedules all steps
  → Step 0 activates

Agent: advance_time(2.0)
  → System completes step 0
  → System attempts to activate step 1
  → Step 1 needs material Y: 5kg
  → Inventory has only 2kg
  → System pauses recipe automatically
  → Emits blocking_issue event

Agent: get_blocking_issues("recipe_X")
  → Returns: [BlockingIssue(type="insufficient_materials",
               step_index=1, needed="material_Y: 5kg",
               available="material_Y: 2kg")]

Agent: run_recipe("recipe_produce_material_Y")
  → Produces 10kg of material Y

Agent: resume_recipe("recipe_X")
  → System reschedules pending steps
  → Step 1 activates (now has materials)
  → Recipe continues
```

**Handling Machine Conflict:**

```
Agent: run_recipe("recipe_A")
  → Schedules step 3 using cnc_mill_v0 at t=5.0

Agent: run_recipe("recipe_B")
  → Attempts to schedule step 2 using cnc_mill_v0 at t=5.0
  → Conflict detected (cnc_mill_v0 already reserved)
  → Step scheduled for t=7.0 instead (after recipe_A step completes)

Alternative: Agent intervenes
Agent: reschedule_step("recipe_A", step_index=3, new_start_time=10.0)
  → Frees cnc_mill_v0 at t=5.0

Agent: run_recipe("recipe_B")
  → Now schedules successfully at t=5.0
```

### 8. Energy Accounting

Energy consumption is calculated and booked at **process start** (activation time) using ADR-014 energy models.

**Why Book at Start**:
- Prevents double-counting if process is force-stopped or fails
- Provides consistent accounting point across all processes
- Energy requirements known at scheduling time (from energy_model and scaled quantities)
- Simplifies accounting: one booking event per process

**Energy Calculation**:

During scheduling (Step 2 of Recipe Execution Model):
1. Retrieve process energy_model from KB
2. Apply step overrides if present (ADR-013)
3. Scale energy based on same scaling_basis used for time_model
4. Use ADR-016 unit conversion for energy units
5. Store calculated `energy_kwh` in ScheduledProcess

During activation:
1. Book `energy_kwh` to process run record
2. Accumulate to parent recipe run (if applicable)
3. Include in `process_start` event for tracking

**Energy Availability**:

Energy availability constraints are **out of scope** for this ADR. The system:
- Tracks total energy consumption
- Books energy at process start
- Does NOT check battery capacity or power limits
- Does NOT prevent processes from starting due to insufficient energy

Future work may add energy availability checking similar to material availability checking.

**Accumulation Levels**:

Energy is accumulated at multiple levels for analysis:
- **Process run**: Individual process execution
- **Recipe run**: Sum of all steps in recipe execution
- **Simulation**: Total across all processes

This enables answering questions like:
- "How much energy did this recipe consume?"
- "What's the most energy-intensive step?"
- "What's total energy consumption over 100 simulation hours?"

### 9. Unit Conversion and Scaling Integration

All quantity calculations integrate with ADR-016 unit conversion system.

**Duration Calculation**:

When calculating process duration from time_model:
1. Parse compound units in rate (e.g., `kg/hr` → numerator: kg, denominator: hr)
2. Normalize time unit to hours (e.g., `min` → `hr`, `sec` → `hr`)
3. Convert scaling_basis quantity to match rate units:
   - If rate is `kg/hr` and output is in `g`, convert g → kg
   - If rate is `L/hr` and output is mass, use density to convert mass → volume
   - If rate is `unit/hr` and output is in batches, resolve batch size

**Energy Calculation**:

When calculating energy from energy_model:
1. Parse energy units (e.g., `kWh`, `MJ`, `BTU`)
2. Normalize to kWh
3. Scale based on same basis as time_model
4. Convert if needed (e.g., mass-based energy with volume output)

**Input/Output Scaling**:

When scaling process inputs/outputs:
1. Determine scale factor from time or output quantity
2. Scale all inputs/outputs proportionally
3. Preserve unit types (kg stays kg, L stays L)
4. Validate mass/volume balance if conserved

**Validation**:

If unit conversion cannot be performed (missing density, incompatible units, etc.):
- Emit warning or error during scheduling
- Include details about what conversion failed
- Prevent process from scheduling if critical conversion failed

This ensures consistent, accurate scaling across time, materials, and energy.

## Impact on Existing ADRs

### ADR-005 (Recipe Step Processing)

**Status Change**: Mark as "Superseded by ADR-020"

**What Remains Valid**: Phase 1 (machine existence validation) continues to work correctly.

**What Changes**: Phases 2-3 replaced by this ADR's architecture. The original vision of tracking machine-hours and executing steps sequentially is realized, but with a different architectural approach (orchestration rather than inheritance).

**Migration**: All unimplemented parts of ADR-005 are now specified in ADR-020.

### ADR-003 (Process-Machine Refactor)

**Completes Outstanding Work**:
- Implementation now uses `resource_requirements.machine_id` for machine reservations
- The `processes_supported` field can now be populated by scanning which processes list each machine
- Machine tracking fully realized

**Clarifies Machine-Hours**:
- Distinction between `resource_requirements.qty` (machine utilization) and time_model duration (elapsed time) is now explicit and implemented
- Example usage documented

**No Changes Needed**: ADR-003 structure already correct, just needed proper usage.

### ADR-012 (Process Types and Time Model)

**Now Enforced**:
- Duration calculated from time_model, not manually specified
- All time_model types (linear_rate, batch, fixed_time) properly used
- Scaling based on actual inputs/outputs as specified

**No Changes Needed**: Specification already correct and complete.

### ADR-013 (Recipe Override Mechanics)

**Clarification**:
- Overrides apply at step level during scheduling
- Step specifies override → used during duration calculation
- Works seamlessly with orchestration model

**Step-Level Only**:
- No recipe-level overrides supported
- Each step individually overrides if needed
- Recipe-level convenience syntax deferred until evidence of need

**No Changes Needed**: Works as designed with orchestration.

### ADR-018 & ADR-019 (Recipe Validation)

**Still Valid**:
- Validation happens before scheduling
- All input/output inference rules unchanged
- BOM-based inference continues to work

**Enhanced**:
- Can now validate machine availability across time
- Can detect potential conflicts during planning

**No Changes Needed**: Validation layer unchanged.

### ADR-004 (Base Builder Simulation)

**Breaking Changes Required**:

**Remove from ActiveProcess**:
- `ends_at` field (replaced by calculation: started_at + duration_hours)
- Duration parameter from `start_process()` (calculated from time_model instead)

**Add to SimulationState**:
- `scheduled_processes: List[ScheduledProcess]` - processes planned for future
- `machine_usage: Dict[str, List[Tuple[float, float, str]]]` - reservation tracking

**Modify in ActiveProcess**:
- Add `duration_hours: float` (calculated value, not provided)
- Add `machine_reservations: Dict[str, MachineReservation]` (which machines reserved)
- Add `parent_recipe_id: Optional[str]` (link to parent recipe if any)
- Add `step_index: Optional[int]` (position in recipe if any)
- Add `dependencies: List[str]` (prerequisite process IDs)

## Migration Strategy

### Dependencies Between Work

This work requires implementation in a specific order:

1. **Schema Updates** (blocking all other work)
   - Update ActiveProcess model
   - Add ScheduledProcess model
   - Add RecipeExecution tracking model
   - Update SimulationState

2. **Core Implementation** (depends on #1)
   - Implement dependency graph builder
   - Implement duration calculator using ADR-012 logic
   - Implement machine reservation system
   - Implement scheduler (advance_time logic)

3. **Control Interface** (depends on #2)
   - Implement observability operations
   - Implement control operations
   - Implement emergency operations

4. **Event System** (depends on #2)
   - Update event emission for new lifecycle
   - Ensure process events link to parent recipe
   - Update visualization to consume new events

5. **Testing** (depends on #2, #3, #4)
   - Unit tests for dependency resolution
   - Unit tests for machine reservation conflicts
   - Integration tests for full recipe execution
   - Time-dependent behavior tests

6. **Migration** (depends on all above)
   - Create migration utility for old event logs (if needed)
   - Update example simulations to new model
   - Archive old implementation

**No Backward Compatibility**: Clean break simplifies implementation. No need to maintain two parallel execution models.

### Estimated Effort

Based on the complexity analysis:

- Schema updates: ~100 lines
- Core implementation: ~300 lines
- Control interface: ~200 lines
- Event system updates: ~100 lines
- Testing: ~300 lines
- **Total: ~1000 lines of code**

Estimated calendar time: 3-4 days implementation + 2 days testing = approximately 1 week.

## Consequences

### Positive

- ✅ **True resource accounting**: Machines, energy, and time properly tracked
- ✅ **Full visibility**: Every step of recipe execution observable
- ✅ **Automatic parallelization**: Independent steps can run concurrently
- ✅ **Agent simplification**: Control clock without micromanaging processes
- ✅ **Time models enforced**: ADR-012 specification actually used
- ✅ **Visualization fixed**: Process events exposed for rendering
- ✅ **ADR-005 completed**: Original vision realized with better architecture
- ✅ **Clear semantics**: Machine-hours vs elapsed time distinction explicit
- ✅ **Conflict prevention**: Double-booking detected and prevented
- ✅ **Intermediate materials usable**: Recipe failure doesn't lose partial progress

### Negative

- ❌ **Breaking change**: Requires migration of existing simulations
- ❌ **Complexity increase**: Three process states vs one
- ❌ **Testing complexity**: Time-dependent behavior harder to test
- ❌ **Migration effort**: Existing simulations need updating
- ❌ **Implementation cost**: ~1 week of development effort

### Neutral

- ⚪ **Different execution model**: Orchestration vs black box (different, not better/worse)
- ⚪ **More explicit**: What recipes are is now clearer
- ⚪ **Event log changes**: Structure different but not incompatible
- ⚪ **Learning curve**: Agent authors need to understand new model

## Validation Rules

The indexer and simulation must enforce these validation rules:

### Process Definition Validation

**Rule 1: Full-Duration Machine Requirement**
- Every process must have at least one `resource_requirements` entry with:
  - `unit: count` or `unit: unit`
  - `qty >= 1`
- **Severity**: ERROR - process invalid without this
- **Rationale**: Processes must use at least one machine for their full duration

**Rule 2: Valid Resource Requirement Units**
- `resource_requirements.unit` must be one of: `hr`, `count`, `unit`
- **Severity**: ERROR - invalid unit
- **Rationale**: Only these units have defined semantics in reservation system

**Rule 3: Partial Reservation Validity**
- If `unit: hr`, then `qty` must be <= process duration (when calculable)
- **Severity**: WARNING - may indicate error
- **Rationale**: Partial reservation exceeding duration doesn't make sense

### Scheduling Validation

**Rule 4: Runtime Instance IDs Required**
- All `process_run_id` and `recipe_run_id` fields must be populated
- **Severity**: ERROR - events without IDs are invalid
- **Rationale**: Tracking requires unique instance identification

**Rule 5: Unit Conversion Feasibility**
- Time, energy, and material scaling must be calculable with available unit data
- **Severity**: ERROR if critical conversion missing, WARNING if optional
- **Rationale**: Can't schedule process if duration or energy incalculable

**Rule 6: Parent Linkage Consistency**
- Process with `parent_recipe_run_id` must reference valid recipe run
- `step_index` must be within recipe step count
- **Severity**: ERROR - invalid linkage
- **Rationale**: Maintains parent-child relationship integrity

### Recipe Validation

**Rule 7: Feasibility Check Completeness**
- Recipe feasibility check must verify all step inputs against current inventory
- If insufficient, immediate pause with blocking issue
- **Severity**: ERROR - can't schedule unfeasible recipe
- **Rationale**: Prevents delayed failures deep in recipe execution

**Rule 8: Dependency Graph Acyclic**
- Recipe step dependencies must not create cycles
- **Severity**: ERROR - cyclic dependencies unresolvable
- **Rationale**: Scheduler can't order steps if dependencies are cyclic

### Event Validation

**Rule 9: Event Instance ID Presence**
- All events must include appropriate runtime IDs:
  - Recipe events: `recipe_run_id`, `recipe_id`
  - Process events: `process_run_id`, `process_id`, plus parent IDs if applicable
- **Severity**: ERROR - invalid event
- **Rationale**: Events must be traceable to specific execution instances

**Rule 10: Event Timestamp Consistency**
- `process_complete` time must be >= `process_start` time
- `process_start` time must be >= `process_scheduled` time
- **Severity**: ERROR - timestamp violation
- **Rationale**: Events must occur in logical chronological order

## Open Questions

These questions are explicitly deferred (not blocking this ADR):

1. **Failure mode details**: When step fails, exactly which materials should be returned? Is partial progress salvageable? Should there be a "rollback" mechanism?

2. **Machine substitution**: Should system auto-suggest alternative machines when conflicts detected? Or is this entirely agent responsibility?

3. **Recipe-level overrides**: Currently not supported. If pattern emerges where every step in multiple recipes needs same override (e.g., "production line version is 2x faster"), consider convenience syntax.

4. **Optimization**: Should scheduler optimize for total time, resource utilization, energy efficiency, or other metrics? Or just execute as scheduled?

5. **Parallel execution limits**: Should there be a maximum concurrent processes limit (simulating limited factory parallelism)? Or allow unlimited parallelism?

6. **Machine capability verification**: Should `reassign_machine()` verify new machine has same capabilities as old? Or trust agent to make valid assignments?

7. **Event log compaction**: With many more events (per-step instead of per-recipe), does log need compression or summarization for long simulations?

8. **Visualization priority**: Should visualization show recipe bars in addition to process bars, or replace them? Should there be a toggle between views?

9. **Material handoff semantics**: Are intermediate materials just inventory entries, or should there be explicit "handoff" events between steps for tracking material flow?

10. **Partial time advancement**: When agent advances 3 hours into 10-hour recipe, should all completeable steps finish instantly (batch processing) or simulate sequentially with events at proper times (accurate timeline)?

## Key Decisions Summary

| Decision | Rationale |
|----------|-----------|
| Clean break, no backward compatibility | Simpler than maintaining two models; reduces long-term confusion |
| Recipe as orchestrator, not process | Matches reality: recipes coordinate processes, not are processes |
| Three-state lifecycle (scheduled/active/completed) | Clear distinction between planned, running, and finished |
| Automatic scheduling via advance_time() | Agent controls clock, system handles progression |
| Agent control operations (pause/resume/reschedule) | Observability and intervention for issues |
| Step-level overrides only | No evidence yet for recipe-level convenience |
| Automatic pause on failure | Agent decides resolution, not system |
| Intermediate materials in inventory | Enables recovery from partial completion |
| Process events as children of recipe | Maintains hierarchy without unifying event types |
| Simulate completion at proper times | Event log accuracy over instant batch completion |
| Machine-hours ≠ elapsed time | Explicit distinction enables partial machine usage |
| Duration calculated from time_model | Enforces consistency between KB and simulation |

## Related Documents

- ADR-003: Process-Machine Schema Harmonization
- ADR-004: Base Builder Simulation
- ADR-005: Recipe Step Processing (superseded)
- ADR-012: Process Types and Time Model
- ADR-013: Recipe Override Mechanics
- ADR-018: Recipe Inputs/Outputs Validation
- ADR-019: BOM-Recipe Relationship and Inference
