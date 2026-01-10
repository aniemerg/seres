# Energy Tracking Persistence Fix Plan (REVISED)

**Status**: Proposed (Revised after review)
**Date**: 2026-01-09
**Revision**: 2026-01-09 after review feedback
**Context**: Bug discovered during simulation visualization - energy consumption shows 0.0 kWh despite processes having valid energy models

## Responses to Review Questions

### Q1: Are recipe-step energy overrides currently supported in start_process() scheduling?

**YES** - Recipe overrides ARE supported via `resolve_step()` (engine.py:693-848):

```python
# When running recipes, steps are resolved before scheduling
resolved_process = self.resolve_step(step)
# Then scheduled with the resolved definition
```

**Implication**: Energy must be calculated using the **resolved** process definition (with overrides applied), not the base process. My original plan missed this.

### Q2: Is total_energy_kwh ever incorrect after reload with valid snapshots?

**YES** - Confirmed incorrect in current simulation:

```json
{"type": "state_snapshot", ..., "total_energy_kwh": 0.0}
{"type": "state_snapshot", ..., "total_energy_kwh": 0.0}
{"type": "state_snapshot", ..., "total_energy_kwh": 0.0}
```

All snapshots show 0.0 kWh despite processes having energy models. The reviewer's point #3 was based on incorrect assumption - the bug DOES affect total energy.

**Root cause**: Energy calculation at PROCESS_START (engine.py:1343-1361) happens in-memory but the `_process_energy` dict is lost on reload. When processes are reconstructed, PROCESS_START events don't fire for already-completed processes, so energy is never calculated.

### Q3: Should energy be recalculated for legacy logs without energy_kwh?

**DEFERRED** - For the minimal fix, default to 0.0 for backward compatibility. Could add smart recalculation in a follow-up enhancement, but adds complexity:
- Need to preserve original inputs/outputs in events
- Need to handle cases where process definitions changed
- Risk of inconsistent totals if partial recalculation happens

## Revised Problem Statement

Energy consumption is not being tracked in ADR-020 simulations because:

1. **Per-process energy is lost**: Stored in `_process_energy` in-memory dict, lost between CLI commands
2. **Total energy is wrong**: `total_energy_kwh` shows 0.0 in all state snapshots
3. **Visualization is broken**: Energy charts show flat lines at zero

**Confirmed behavior**: All state snapshots have `"total_energy_kwh": 0.0` despite valid energy models.

## Revised Solution (Minimal, Non-Breaking)

### Core Principle

All data needed to reconstruct state must be in logged events. Energy should be calculated ONCE at scheduling time and persisted.

### Changes Required

#### 1. Add energy_kwh to ProcessScheduledEvent (Non-Breaking)

**File**: `src/simulation/models.py`

```python
class ProcessScheduledEvent(Event):
    """Process scheduled for execution."""
    type: Literal["process_scheduled"] = "process_scheduled"

    process_id: str
    process_run_id: str

    scheduled_start_time: float
    duration_hours: float
    scheduled_end_time: float

    scale: float

    inputs_consumed: Dict[str, Dict[str, Any]]
    outputs_pending: Dict[str, Dict[str, Any]]
    machine_reservations: List[Dict[str, Any]]

    recipe_run_id: Optional[str] = None
    step_index: Optional[int] = None

    # ADD (optional for backward compatibility):
    energy_kwh: Optional[float] = None
```

#### 2. Add energy_kwh to ProcessRun (Minimal Change)

**File**: `src/simulation/scheduler.py`

**KEEP existing field names** (start_time, end_time, machines_reserved as Dict):

```python
@dataclass
class ProcessRun:
    """Represents a running process instance."""

    process_run_id: str
    process_id: str
    start_time: float  # ← Keep as-is (NOT scheduled_start_time)
    duration_hours: float
    end_time: float  # ← Keep as-is (NOT scheduled_end_time)
    scale: float
    inputs_consumed: Dict[str, float]
    outputs_pending: Dict[str, float]
    machines_reserved: Dict[str, float]  # ← Keep as Dict (NOT list)
    recipe_run_id: Optional[str] = None
    step_index: Optional[int] = None

    # ADD ONLY THIS:
    energy_kwh: Optional[float] = None
```

#### 3. Calculate Energy at Scheduling (Handle Recipe Overrides)

**File**: `src/simulation/engine.py` in `start_process()`

**Location**: Around line 640-660, BEFORE logging ProcessScheduledEvent

**Critical**: Use the process definition that was PASSED IN (which may already have overrides resolved), not the base KB definition:

```python
# Around line 640-660, after inputs/outputs are calculated

# Calculate energy using the process definition (with any overrides applied)
energy_kwh = 0.0

# IMPORTANT: If this was called from run_recipe with resolve_step(),
# the 'process' parameter IS the resolved definition.
# For direct start_process calls, it's the base KB definition.
# Either way, use what we have, don't re-fetch from KB.

if hasattr(process, 'energy_model') and process.energy_model:
    try:
        # Build Quantity objects for calculation
        inputs_dict = {}
        for item_id, inv_item in inputs_consumed.items():
            inputs_dict[item_id] = Quantity(
                item_id=item_id,
                qty=inv_item.quantity,
                unit=inv_item.unit
            )

        outputs_dict = {}
        for item_id, inv_item in outputs_pending.items():
            outputs_dict[item_id] = Quantity(
                item_id=item_id,
                qty=inv_item.quantity,
                unit=inv_item.unit
            )

        energy_kwh = calculate_energy(
            process,  # Use resolved process (with overrides)
            inputs=inputs_dict,
            outputs=outputs_dict,
            converter=self.converter
        )
    except Exception as e:
        # Log warning but continue
        print(f"⚠️ Energy calculation failed for {process_id}: {e}")
        energy_kwh = 0.0

# Log event WITH energy
self._log_event(
    ProcessScheduledEvent(
        process_id=process_id,
        process_run_id=process_run_id,
        scheduled_start_time=start_time,
        duration_hours=duration_hours,
        scheduled_end_time=end_time,
        scale=scale,
        inputs_consumed=inputs_consumed_with_units,
        outputs_pending=outputs_pending_with_units,
        machine_reservations=machine_reservations_list,
        recipe_run_id=recipe_run_id,
        step_index=step_index,
        energy_kwh=energy_kwh,  # ADD THIS
    )
)
```

**Issue to check**: Does `start_process()` receive the resolved process or just process_id? Need to verify call path from `run_recipe()`.

#### 4. Propagate Energy Through Scheduler

**File**: `src/simulation/scheduler.py` in `schedule_process_start()`

Add energy parameter:

```python
def schedule_process_start(
    self,
    process_run_id: str,
    process_id: str,
    start_time: float,
    duration_hours: float,
    end_time: float,
    scale: float,
    inputs_consumed: Dict[str, float],
    outputs_pending: Dict[str, float],
    machines_reserved: Dict[str, float],
    recipe_run_id: Optional[str] = None,
    step_index: Optional[int] = None,
    energy_kwh: Optional[float] = None,  # ADD THIS
) -> SchedulerEvent:
    """Schedule process start and completion events."""

    # Create ProcessRun with energy
    process_run = ProcessRun(
        process_run_id=process_run_id,
        process_id=process_id,
        start_time=start_time,
        duration_hours=duration_hours,
        end_time=end_time,
        scale=scale,
        inputs_consumed=inputs_consumed,
        outputs_pending=outputs_pending,
        machines_reserved=machines_reserved,
        recipe_run_id=recipe_run_id,
        step_index=step_index,
        energy_kwh=energy_kwh,  # ADD THIS
    )

    # Rest of function unchanged...
```

#### 5. Update advance_time() to Use Persisted Energy

**File**: `src/simulation/engine.py` in `advance_time()`

**Location**: Around line 1295-1361, PROCESS_START handler

**REMOVE** energy calculation (lines 1313-1351), use persisted value:

```python
if event.event_type == EventType.PROCESS_START:
    process_run_id = event.data.get("process_run_id")

    # Find process run
    process_run = self.scheduler.active_processes.get(process_run_id)
    if not process_run:
        continue

    # Get energy from ProcessRun (loaded from scheduled event)
    energy_kwh = process_run.energy_kwh or 0.0

    # Accumulate energy into total
    self.state.total_energy_kwh += energy_kwh

    # Store for completion logging
    if not hasattr(self, '_process_energy'):
        self._process_energy = {}
    self._process_energy[process_run_id] = energy_kwh

    # Log activation event (unchanged)
    self._log_event(
        ProcessStartEvent(
            process_id=process_run.process_id,
            process_run_id=process_run_id,
            actual_start_time=event.time,
            scale=process_run.scale,
        )
    )
```

#### 6. Load Energy During State Reconstruction

**File**: `src/simulation/engine.py` in `load()`

**Location**: Around line 1695-1730

**DO NOT accumulate energy to total_energy_kwh** (reviewer's point #1 - would double-count):

```python
if event.get("type") != "process_scheduled":
    continue

process_run_id = event.get("process_run_id")
# ... existing code ...

# Read energy from event (NEW)
energy_kwh = event.get("energy_kwh")

# Create ProcessRun with energy
process_run = ProcessRun(
    process_run_id=process_run_id,
    process_id=process_id,
    start_time=scheduled_start_time,  # Keep existing name
    duration_hours=duration_hours,
    end_time=scheduled_end_time,      # Keep existing name
    scale=scale,
    inputs_consumed=inputs_consumed,
    outputs_pending=outputs_pending,
    machines_reserved=reservations,   # Keep as Dict
    recipe_run_id=recipe_run_id,
    step_index=step_index,
    energy_kwh=energy_kwh,  # ADD THIS
)

# For in-flight processes, re-add to scheduler
if scheduled_end_time > self.state.current_time_hours:
    self.scheduler.schedule_process_start(
        process_run_id=process_run_id,
        process_id=process_id,
        start_time=scheduled_start_time,
        duration_hours=duration_hours,
        end_time=scheduled_end_time,
        scale=scale,
        inputs_consumed=inputs_consumed,
        outputs_pending=outputs_pending,
        machines_reserved=reservations,
        recipe_run_id=recipe_run_id,
        step_index=step_index,
        energy_kwh=energy_kwh,  # ADD THIS
    )
```

**DO NOT** add energy for completed processes - the authoritative `total_energy_kwh` comes from the latest state_snapshot.

#### 7. Trust State Snapshots for Total Energy

**File**: `src/simulation/engine.py` in `load()`

**Location**: Around line 1621

**NO CHANGE NEEDED** - total_energy_kwh is already loaded from state_snapshot:

```python
elif event_type == "state_snapshot":
    # ... existing inventory/machines loading ...

    self.state.total_energy_kwh = event.get("total_energy_kwh", 0.0)
    # ↑ This is authoritative - do NOT add scheduled energy on top
```

The state snapshot already includes all energy accumulated up to that point. Adding scheduled energy would double-count.

## Recipe Override Handling

**Critical Issue**: When `run_recipe()` schedules steps, it must pass the RESOLVED process to energy calculation.

**Current flow** (needs verification):
```python
# In run_recipe()
resolved_process = self.resolve_step(step)
# Then what? Does it:
# A) Call start_process() with resolved_process? OR
# B) Call start_process() with process_id only?
```

**TODO**: Check if `start_process()` receives:
- Full resolved process definition (GOOD - can calculate energy with overrides)
- Just process_id (BAD - would fetch base process, missing overrides)

**If B**, we need to:
1. Pass resolved process to `start_process()`, OR
2. Calculate energy BEFORE calling `start_process()` and pass it as parameter

## Testing Plan

### 1. Unit Tests

**File**: `test/unit/test_energy_persistence.py` (new)

```python
def test_energy_in_scheduled_event():
    """Energy should appear in ProcessScheduledEvent."""
    # Verify logged event has energy_kwh field

def test_energy_in_process_run():
    """Energy should be stored in ProcessRun."""
    # Verify ProcessRun object has energy_kwh

def test_energy_accumulated_at_start():
    """total_energy_kwh should increase when process starts."""
    # Not at schedule, at START event

def test_energy_in_complete_event():
    """process_complete should log energy_kwh."""
    # Retrieved from _process_energy dict

def test_energy_survives_reload():
    """Energy persists across load/save cycle."""
    # Schedule process with energy
    # Save
    # Reload
    # Verify ProcessRun has energy
    # Advance time
    # Verify total_energy_kwh correct
```

### 2. Integration Test

**File**: `test/integration/test_energy_cli_persistence.py` (new)

```python
def test_energy_across_cli_commands(tmp_path):
    """Energy survives CLI command boundaries."""
    sim_id = "energy_test"

    # Command 1: Init + import + schedule
    engine1 = SimulationEngine(sim_id, kb_loader, tmp_path)
    engine1.import_item("labor_bot_general_v0", 1.0, "unit")
    engine1.start_process("regolith_mining_simple_v0", duration_hours=10)
    engine1.save()

    # Command 2: Load + advance
    engine2 = SimulationEngine(sim_id, kb_loader, tmp_path)
    engine2.load()
    result = engine2.advance_time(10.0)

    # Verify energy is correct (5 kWh for 100 kg at 0.05 kWh/kg)
    # Calculated from 100 kg output (not input) scaled by scale factor
    expected_energy = 100 * 0.05  # 5.0 kWh
    assert engine2.state.total_energy_kwh == expected_energy

    # Verify it's in process_complete event
    # (check last event in log)
```

### 3. Recipe Override Test

```python
def test_recipe_energy_override():
    """Recipe step energy overrides should be used."""
    # Create recipe with energy_model override
    # Run recipe
    # Verify scheduled event uses overridden energy, not base
```

### 4. Regression Test

```bash
# Should show non-zero energy after fix
python -m src.cli sim visualize --sim-id robot_build_max_isru_2026_01_09
```

## Migration Strategy

### Backward Compatibility

**Old logs** (missing energy_kwh):
- `ProcessScheduledEvent.energy_kwh` is `Optional[float] = None`
- Code checks `if energy_kwh is not None` or uses `energy_kwh or 0.0`
- Old simulations load without errors
- Old simulations show 0 energy (can't retroactively calculate)

**New logs** (with energy_kwh):
- Energy is calculated and stored
- Persists across reloads
- Visualizations work correctly

### Deployment Steps

1. ✅ Add optional field to ProcessScheduledEvent
2. ✅ Add optional field to ProcessRun
3. ✅ Calculate energy at scheduling time
4. ✅ Propagate through scheduler
5. ✅ Use persisted energy in advance_time()
6. ✅ Load energy during reconstruction
7. ✅ Write tests
8. ✅ Verify recipe overrides work
9. ✅ Update documentation

## Open Issues

### Issue 1: How is resolved process passed to start_process()?

**Need to verify**: When `run_recipe()` resolves a step, does it pass the resolved process definition to `start_process()` or just the process_id?

**If just process_id**: Need to refactor to pass resolved process or pre-calculate energy.

### Issue 2: Scale factor application

Energy should respect scale factor. Need to verify:
- Is scale applied to outputs BEFORE energy calculation?
- Or do we need to multiply energy by scale?

**Current code** suggests outputs are scaled before calculation (inputs_consumed/outputs_pending already include scale), so energy should be correct.

## Success Criteria

1. ✅ `process_scheduled` events include `energy_kwh`
2. ✅ `ProcessRun` objects store `energy_kwh`
3. ✅ `total_energy_kwh` increases when processes start
4. ✅ Energy persists across CLI command boundaries
5. ✅ `process_complete` events include correct `energy_kwh`
6. ✅ Visualizations show non-zero energy
7. ✅ Recipe overrides apply to energy calculation
8. ✅ Old simulations load without errors
9. ✅ ProcessRun schema unchanged (except energy field)
10. ✅ No double-counting of energy from snapshots

## Summary of Changes vs Original Plan

**Reviewer corrections applied**:
1. ❌ REMOVED: Adding scheduled energy to total during load (would double-count)
2. ✅ FIXED: ProcessRun schema - kept existing field names (start_time/end_time, machines_reserved as Dict)
3. ✅ CLARIFIED: Problem scope - total_energy_kwh IS wrong (confirmed 0.0 in all snapshots)
4. ✅ ADDED: Recipe override handling (must use resolved process for energy)
5. ✅ ADDED: Energy propagation through scheduler's schedule_process_start()
6. ✅ CLARIFIED: Backward compatibility strategy

**Remaining questions**:
- How is resolved process passed from run_recipe to energy calculation?
- Should we support smart recalculation for old logs?

## References

- Original plan: `design/energy-tracking-persistence-fix.md`
- Review notes: `design/energy-tracking-persistence-fix-review.md`
- ADR-014: Energy Model Redesign
- ADR-020: Simulation Persistence and Scheduling
- ADR-013: Recipe Override Mechanics
