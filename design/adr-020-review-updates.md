# ADR-020 Review: Required Updates

## Purpose

Capture required updates to ADR-020 based on review feedback to prevent
scheduling/resource/energy accounting errors and clarify unit handling.

## Required Updates

### 1) Machine reservation lifetime

**Issue:** ADR-020 mixes partial reservation semantics with release on process
completion, which can over- or under-reserve machines.

**Update:**
- A process must reserve **at least one machine for the full process duration**.
- Additional machines may be reserved for partial durations, with the partial
  reservation **front-loaded** at the start of the process and released when
  that partial window ends.
- Machine reservation release rules must be explicit and separate from process
  completion:
  - Full-duration machine(s): release at `process_complete`.
  - Partial-duration machine(s): release at `process_started_at + reserved_hours`.

**Proposed ADR-020 language:**
- Add a rule that a process is invalid unless it has at least one
  `resource_requirements` entry representing a full-duration reservation.

### 2) Resource requirements: units and capacity

**Issue:** `resource_requirements.qty` is ambiguously treated as machine-hours,
but ADR-003 includes `count` or `unit` for quantity of machines.

**Update:**
- Permit `resource_requirements.unit` to be either:
  - `hr` (machine-hours; reservation duration), or
  - `count`/`unit` (number of machine instances required for **full duration**).
- Interpret `count`/`unit` as a **multiplicity** of full-duration reservations.
- Require at least one full-duration reservation entry per process with
  `unit`/`count` and `qty >= 1` (or a dedicated full-duration marker if
  introduced later).
- Indexer and simulation must validate the presence of this full-duration
  reservation; otherwise fail validation or block scheduling.

**Proposed ADR-020 language:**
- Define two reservation types:
  - **Full-duration reservation** (count/unit): reserves `qty` machines for the
    entire process duration.
  - **Partial reservation** (hr): reserves a specific machine for `qty` hours
    at process start.

### 3) Recipe start resource checks

**Issue:** Scheduled steps “reserve” materials but no check guarantees they will
be available when the step activates.

**Update:**
- On `run_recipe(recipe_id)` perform a **per-recipe feasibility check** against
  current inventory for all required inputs across the dependency graph.
- If missing, immediately pause the recipe and emit a blocking issue before any
  steps schedule.
- Consumption still happens at activation time; the pre-check ensures that
  running the recipe alone will not later fail due to missing inputs.

**Note:** Cross-recipe contention can be deferred, but this local guarantee must
be explicit.

### 4) IDs for scheduled/active processes and recipe runs

**Issue:** ADR-020 uses process/recipe references but does not specify stable
IDs for runtime instances.

**Update:**
- Introduce unique runtime IDs:
  - `recipe_run_id` (instance of a recipe execution).
  - `process_run_id` (instance of a process execution).
- All status/control operations and events reference these IDs.
- Maintain linkage fields:
  - `parent_recipe_run_id` and `step_index` on process run records/events.

### 5) advance_time ordering and intermediate completions

**Issue:** The described scheduler completes processes against the old
`current_time`, then updates time, which can miss completions that occur within
`advance_time`.

**Update:**
- Scheduler must process the time interval in order, emitting events at their
  actual completion times.
- Implementation can use an event-queue jump (not fixed step size):
  - Find the next soonest completion time within the interval.
  - Advance to that time, complete processes, activate newly-ready steps.
  - Repeat until reaching the requested target time.
- This preserves correct event timing without a heavy refactor.

### 6) Duration scaling and unit normalization

**Issue:** ADR-020 lacks explicit integration with ADR-016 for compound units and
unit normalization, risking incorrect time and resource scaling.

**Update:**
- Duration calculation must call the ADR-016 unit conversion pipeline:
  - Parse compound units (e.g., `kg/hr`, `L/min`).
  - Normalize time units to hours.
  - Convert between mass/volume/count using density or item mass/volume when
    required.
- Scheduling must support:
  - Running a process for a specified time (derive output qty),
  - Running for a target output qty (derive time),
  - Running for a batch count (derive time/outputs/inputs).
- All derived quantities (time, inputs, outputs, energy) must scale consistently.

### 7) Energy accounting integration

**Issue:** ADR-020 does not specify when or how energy is tallied.

**Update:**
- Energy usage should be booked at **process start** using ADR-014
  `energy_model` and the same scaling basis used for time.
- Book energy at start to avoid double counting later and to preserve a
  consistent accounting point.
- Energy availability constraints remain out of scope, but energy totals must be
  accumulated at both process and recipe run levels.

## Validation Rules to Add

- Reject processes missing a full-duration machine reservation (count/unit).
- Reject `resource_requirements.unit` values outside `hr`, `count`, `unit`.
- Warn or error if unit conversion cannot be performed for duration or energy
  scaling.
- Enforce that `process_run_id` and `recipe_run_id` are present in events.

## Open Implementation Notes

- If partial machine reservations are common, consider adding explicit fields:
  `reservation_kind: full|partial` and `reservation_start_offset_hours` (default
  0). This avoids overloading `unit` semantics.
- If partial reservations are front-loaded, note this explicitly in the ADR and
  treat any other offsets as future work.

