# Bug Report: Multi-Step Recipe Second Step Keeps Getting Rescheduled

## Summary

Multi-step recipes in the simulation engine have a bug where the second step (and subsequent steps) get continuously rescheduled to start at the current time, preventing them from ever completing.

## Severity

**HIGH** - Blocks all multi-step recipe execution in runbooks, making it impossible to use recipes with dependencies.

## Reproduction

### Minimal Failing Test Case

**Test File:** `test/test_recipe_bug.py`

The test `test_two_step_recipe_completes()` demonstrates the bug when run via runbook but passes when run via pytest. This indicates the issue is specific to how runbooks advance time or handle events.

### Steps to Reproduce via Runbook

1. Create a simulation with a 2-step recipe (e.g., `recipe_nickel_metal_from_regolith_v0`)
2. Import required resources
3. Run the recipe with `sim.run-recipe`
4. Advance time by a large amount (e.g., 1000 hours)
5. Check the simulation status

**Expected Behavior:**
- Both steps should complete
- Recipe should be marked as complete
- Output items should be in inventory

**Actual Behavior:**
- Step 1 completes successfully
- Step 2 gets scheduled but never completes
- Status shows "Processes: 1 active, 1 completed"
- Event queue shows process_start scheduled at current_time, process_complete at current_time+1
- Each time you check or advance, the start time moves forward to match current_time

### Evidence

```bash
# At time=1000 hours
$ cat simulations/test_nickel/snapshot.json | python3 -c "..."
Time: 1000.0
Event queue:
  1000.0: process_start
  1001.0: process_complete

# After advancing to time=1005 hours
$ cat simulations/test_nickel/snapshot.json | python3 -c "..."
Time: 1005.0
Event queue:
  1005.0: process_start  # <-- Rescheduled!
  1006.0: process_complete  # <-- Keeps moving forward
```

## Root Cause Analysis

### Key Observation

The bug does **NOT** occur when using the SimulationEngine directly via pytest:
- Test advances time in two separate calls: `advance_time(150)` then `advance_time(500)`
- Both steps complete successfully
- nickel_metal appears in inventory

The bug **DOES** occur when using runbooks:
- Runbook advances time in a single large increment: `advance_time(1000)`
- Step 2 gets continuously rescheduled
- Recipe never completes

### Hypothesis

The issue appears to be in the event processing logic in `src/simulation/engine.py` around lines 1455-1539:

```python
# Check if this was a recipe step - schedule dependent steps
if process_run.recipe_run_id:
    recipe_run_id = process_run.recipe_run_id
    ready_steps = self.orchestrator.get_ready_steps(recipe_run_id)

    for step_idx in ready_steps:
        # ... schedule step ...
        schedule_time = max(event.time, self.scheduler.current_time)
        result = self.start_process(
            ...
            start_time=schedule_time,
            ...
        )
```

The line `schedule_time = max(event.time, self.scheduler.current_time)` may be causing the issue. If this code runs multiple times during a single `advance_time()` call (e.g., during event processing), it could keep rescheduling the process to the current time.

### Possible Causes

1. **Event Processing Loop Issue**: The code that schedules subsequent steps may be running in a loop or getting triggered multiple times during a single advance_time call
2. **State Inconsistency**: The process may be getting added to the scheduler multiple times with different IDs
3. **Scheduler State Issue**: The scheduler may be resetting or recreating events incorrectly

## Investigation Path

To identify the exact cause, we need to:

1. Add debug logging to track when `orchestrator.get_ready_steps()` is called
2. Add debug logging to track when `start_process()` is called for recipe steps
3. Trace the event processing loop in `advance_time()` to see if it's iterating multiple times over the same events
4. Check if there's a difference in how pytest vs runbook execution handles the scheduler state

## Affected Code

- **Primary**: `src/simulation/engine.py:1455-1539` (subsequent step scheduling in advance_time)
- **Secondary**: `src/simulation/recipe_orchestrator.py` (recipe run tracking)
- **Secondary**: `src/simulation/scheduler.py` (event queue management)

## Workaround

Currently, NO effective workaround exists for runbooks. Multi-step recipes cannot be used in runbooks until this bug is fixed.

For direct API usage, calling `advance_time()` multiple times in smaller increments appears to work correctly (as demonstrated by the pytest test).

## Test Status

- **Pytest test** (`test/test_recipe_bug.py::test_two_step_recipe_completes`): **PASSES** ✅
- **Runbook test** (`runbooks/test_nickel_extraction.md`): **FAILS** ❌

This confirms the bug is reproducible and related to runbook execution specifically.

## Next Steps

1. Add comprehensive debug logging to trace event processing
2. Identify why runbook execution behaves differently than pytest execution
3. Fix the rescheduling logic to prevent continuous rescheduling
4. Add regression test to prevent this issue from recurring
5. Update affected runbooks once fix is implemented

## Related Files

- Test: `/Users/allanniemerg/dev2/self-replicating-system-modeling/test/test_recipe_bug.py`
- Runbook: `/Users/allanniemerg/dev2/self-replicating-system-modeling/runbooks/test_nickel_extraction.md`
- Recipe: `/Users/allanniemerg/dev2/self-replicating-system-modeling/kb/recipes/recipe_nickel_metal_from_regolith_v0.yaml`
- Main runbook affected: `/Users/allanniemerg/dev2/self-replicating-system-modeling/runbooks/electrolysis_cell_unit_v0_runbook.md`
