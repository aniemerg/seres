# Bug Fix: Multi-Step Recipe Scheduling Issue

## Root Cause

**Location:** `src/simulation/engine.py` - Dependent recipe step scheduling logic

### The Problem

Multi-step recipes would fail to complete when using large single `advance_time()` calls. The dependent steps were being scheduled at the wrong time.

**Original buggy code flow:**
1. `engine.advance_time(1005)` calls `scheduler.advance_to(1005)`
2. Scheduler processes all events up to time 1005
3. **Scheduler sets `current_time = 1005`** (target time)
4. Scheduler returns processed events to engine
5. Engine post-processes events and schedules dependent recipe steps
6. When scheduling, code used: `schedule_time = max(event.time, scheduler.current_time)`
7. For step completing at time 1.0: `schedule_time = max(1.0, 1005.0) = 1005.0`
8. Dependent step scheduled at 1005.0 instead of 1.0, never executes!

**Why it worked with small advances:**
- `advance_time(150)`: Step 1 completes at 1.0, step 2 scheduled at 150.0
- `advance_time(500)`: Advances to 650, processes step 2 completion at 151.0 ✓

**Why it failed with large advance:**
- `advance_time(1005)`: Step 1 completes at 1.0, step 2 scheduled at 1005.0
- No further advance happens, step 2 never completes ✗

### Root Cause Analysis

The issue was **architectural**: dependent step scheduling happened AFTER `scheduler.advance_to()` completed and set `current_time = target_time`. At that point:
- `scheduler.current_time` was already 1005.0
- `event.time` was the actual completion time (1.0)
- Using `max()` caused scheduling at the wrong time

## The Fix

**Solution:** Move dependent step scheduling into event handlers that run DURING event processing, when `scheduler.current_time` still equals `event.time`. Additionally, add process outputs to inventory during event processing so they're available as inputs for dependent steps.

### Key Insight

The critical issue was that outputs were being added to inventory AFTER all event handlers ran, but dependent step scheduling needed those outputs to be in inventory to validate inputs. The solution required TWO event handlers:
1. First handler: Add outputs to inventory
2. Second handler: Schedule dependent steps (which can now access the outputs)

### Changes Made

**File:** `src/simulation/engine.py`

#### 1. Created output addition handler

```python
def _add_process_outputs(self, event) -> None:
    """
    Event handler to add process outputs to inventory when a process completes.

    This runs during event processing, before dependent recipe steps are scheduled,
    so that outputs are available as inputs for dependent steps.
    """
    # Find completed process and add outputs to inventory
    for item_id, qty in process_run.outputs_pending.items():
        unit = output_units.get(item_id, "kg")
        self.add_to_inventory(item_id, qty, unit)
```

#### 2. Created dependent step scheduling handler

```python
def _schedule_dependent_recipe_steps(self, event) -> None:
    """
    Event handler to schedule dependent recipe steps when a process completes.

    This runs during event processing while scheduler.current_time = event.time,
    which allows us to schedule dependent steps at the correct time without
    "Cannot schedule event in the past" errors.
    """
    # Find process run and check if it's part of a recipe
    # Get ready steps from orchestrator
    # Schedule each ready step at event.time
    schedule_time = event.time  # Scheduled at completion time, not current_time!
```

#### 3. Registered event handlers in order

```python
# In __init__:
# Order matters: handlers are called in registration order
self.scheduler.register_handler(
    EventType.PROCESS_COMPLETE,
    self._add_process_outputs  # FIRST: add outputs to inventory
)
self.scheduler.register_handler(
    EventType.PROCESS_COMPLETE,
    self._schedule_dependent_recipe_steps  # THEN: schedule dependent steps
)

# Same in from_snapshot() for reload support
```

#### 4. Removed old post-processing logic

Removed ~200 lines of:
- Output addition code (moved to `_add_process_outputs` handler)
- Dependent step scheduling code (moved to `_schedule_dependent_recipe_steps` handler)

### Why This Works

When `scheduler._process_event(event)` is called for a PROCESS_COMPLETE event:
1. Sets `scheduler.current_time = event.time` (e.g., 1.0)
2. Moves process from active to completed
3. Calls orchestrator's handler to mark step as completed
4. Calls our `_add_process_outputs` handler:
   - Adds outputs to inventory (e.g., ingot)
5. Calls our `_schedule_dependent_recipe_steps` handler:
   - Checks for ready steps (step 1 is now ready)
   - Calls `start_process` for step 1
   - `start_process` validates inputs - SUCCESS! (ingot is in inventory)
   - Schedules step 1 at `event.time` (1.0)
6. Scheduler validates: `event.time (1.0) >= current_time (1.0)` ✓
7. Step 1 is scheduled correctly!

After all events are processed, `advance_to()` sets `current_time = target_time`, but by then:
- All outputs are in inventory
- All dependent steps are scheduled at correct times

## Testing

### Test Results

**Before Fix:**
- Pytest: PASS (multiple small advances worked around the bug)
- Runbook: FAIL (single large advance exposed the bug)
- Total: 427 passed, 10 failed

**After Fix:**
- Pytest: PASS ✓
- Runbook: PASS ✓
- Total: **437 passed, 0 failed** ✓

### Test Output (Runbook)

```
✓ Advanced time by 1005 hours
  Processes completed: 2

Completed processes:
  - beneficiate_regolith_magnetic_v0 (completed at 1.0h)
      → meteorite_iron: 10.00 kg
  - nickel_extraction_meteorite_v0 (completed at 41.0h)
      → nickel_metal: 1.00 kg
      → iron_metal: 8.00 kg

Recipes: 0 active, 1 completed
```

Both steps complete successfully, with step 2 starting at 1.0h (when step 1 completes) instead of being scheduled at 1005.0h!

### Test Files
- Unit test: `test/test_recipe_bug.py::test_two_step_recipe_completes`
- Integration test: `runbooks/test_nickel_extraction.md`

## Impact

This fix enables multi-step recipes to work correctly in all contexts:
- ✓ Direct API usage with any `advance_time()` increment
- ✓ Runbook execution with any time advancement strategy
- ✓ Recipes with arbitrary numbers of steps and dependencies
- ✓ Proper chronological event ordering maintained
- ✓ No performance impact (cleaner code, fewer lines)

## Files Changed

1. **src/simulation/engine.py**
   - Added `_add_process_outputs()` event handler (~40 lines)
   - Added `_schedule_dependent_recipe_steps()` event handler (~90 lines)
   - Registered both handlers in `__init__()` and `from_snapshot()`
   - Removed old post-processing output addition code (~20 lines)
   - Removed old post-processing scheduling logic (~200 lines)
   - Net: ~90 lines removed, much cleaner architecture

2. **test/test_recipe_bug.py**
   - Updated test to reflect correct (faster) completion times
   - Changed from `advance_time(150)` + `advance_time(500)` to `advance_time(20)` + `advance_time(30)`

3. **test/integration/test_adr020_engine.py**
   - Updated test to check for active step instead of intermediate product in inventory
   - Reflects that step 2 now starts immediately, consuming the intermediate product

4. **test/unit/test_recipe_orchestrator.py**
   - Added `recipe_def` parameter to RecipeRun instantiations (API change)

## Architecture Improvement

This fix improves the system architecture by:
- Moving dependent step scheduling into event handlers (proper event-driven design)
- Scheduling happens at the right time in the event processing lifecycle
- Removes duplicate scheduling logic from post-processing
- Makes the code more maintainable and easier to understand
