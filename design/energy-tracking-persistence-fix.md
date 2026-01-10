# Energy Tracking Persistence Fix Plan

**Status**: Proposed
**Date**: 2026-01-09
**Context**: Bug discovered during simulation visualization - energy consumption shows 0.0 kWh despite processes having valid energy models

## Problem Statement

Energy consumption is not being properly tracked and persisted in ADR-020 simulations. All processes show `energy_kwh: 0.0` in logged events and visualizations despite having valid energy models defined.

### Observed Behavior

1. **Simulation logs show zero energy**: All `process_complete` events have `"energy_kwh": 0.0`
2. **State snapshots show zero total**: `"total_energy_kwh": 0.0` in all state snapshots
3. **Visualizations are empty**: Energy charts show flat lines at zero
4. **Process definitions ARE correct**: Processes have valid `energy_model` fields (e.g., `regolith_mining_simple_v0` has `0.05 kWh/kg`)
5. **Calculation function works**: Direct testing of `calculate_energy()` returns correct values (5.0 kWh for 100 kg)

### Test Case

```python
# Process definition (regolith_mining_simple_v0.yaml)
energy_model:
  type: per_unit
  value: 0.05
  unit: kWh/kg
  scaling_basis: regolith_lunar_mare

# Direct calculation test
outputs = {"regolith_lunar_mare": Quantity(qty=100.0, unit="kg")}
energy = calculate_energy(process, {}, outputs, converter)
# Result: 5.0 kWh ✓ CORRECT

# But in simulation log
{"type": "process_complete", ..., "energy_kwh": 0.0}  # ✗ WRONG
```

## Root Cause Analysis

### The Energy Lifecycle in ADR-020

```
1. start_process() called
   ↓
2. ProcessScheduledEvent logged (no energy field!)
   ↓
3. Scheduler schedules PROCESS_START event at future time
   ↓
4. advance_time() processes events
   ↓
5. PROCESS_START event fires
   ↓
6. Energy calculated and stored in self._process_energy dict
   ↓
7. self.state.total_energy_kwh += energy_kwh
   ↓
8. PROCESS_COMPLETE event fires
   ↓
9. Energy retrieved from self._process_energy dict
   ↓
10. ProcessCompleteEvent logged with energy_kwh
```

### The Three-Part Bug

#### Bug 1: Energy Dictionary Not Persisted

**Location**: `src/simulation/engine.py:1359-1361`

```python
# Store energy on process_run for later retrieval
if not hasattr(self, '_process_energy'):
    self._process_energy = {}
self._process_energy[process_run_id] = energy_kwh
```

**Problem**: `_process_energy` is an in-memory dict, lost between CLI command invocations.

**Impact**: When simulation is reloaded from disk, the dict doesn't exist.

#### Bug 2: Completed Processes Don't Reconstruct Energy

**Location**: `src/simulation/engine.py:1705-1706` (in `load()`)

```python
if scheduled_end_time <= self.state.current_time_hours:
    continue  # Skip completed processes!
```

**Problem**: Processes that have already completed don't get re-added to scheduler, so their `PROCESS_START` events never fire during reconstruction.

**Impact**: Energy calculations never happen during state rebuild from logs.

#### Bug 3: Silent Fallback to Zero

**Location**: `src/simulation/engine.py:1437-1439` (at completion)

```python
energy_kwh = 0.0
if hasattr(self, '_process_energy') and process_run_id in self._process_energy:
    energy_kwh = self._process_energy[process_run_id]
```

**Problem**: If `_process_energy` dict doesn't exist, code silently defaults to 0.0.

**Impact**: No warning/error, just incorrect zero values in logs.

### Why This Happens with ADR-020

ADR-020 introduced event-sourcing architecture where state is reconstructed from JSONL logs. This works well for inventory, machines, and scheduling, but energy tracking wasn't updated to persist through events.

**Before ADR-020** (in-memory only):
- Energy was only tracked during a single Python session
- Fine for long-running simulations
- Not an issue because state was never reloaded

**After ADR-020** (event-sourced):
- Each CLI command loads state from JSONL log
- Energy tracking still uses in-memory dict
- Mismatch between persistence models

## Proposed Solution

### Approach: Store Energy in ProcessScheduledEvent

Calculate energy when scheduling the process and persist it in the event log.

**Key Principle**: All data needed to reconstruct state must be in logged events.

### Implementation Plan

#### 1. Update Data Models

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

    # ADD THIS:
    energy_kwh: Optional[float] = None  # Calculated energy for this process
```

#### 2. Calculate Energy at Scheduling Time

**File**: `src/simulation/engine.py` in `start_process()`

**Location**: Around line 660, before logging `ProcessScheduledEvent`

```python
# Current code (lines ~640-660):
# ... inputs and outputs calculated ...

# ADD: Calculate energy before scheduling
energy_kwh = 0.0
process_model = self.kb.get_process(process_id)

if process_model and process_model.energy_model:
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
            process_model,
            inputs=inputs_dict,
            outputs=outputs_dict,
            converter=self.converter
        )
    except Exception as e:
        # Log warning but continue
        print(f"Warning: Energy calculation failed for {process_id}: {e}")
        energy_kwh = 0.0

# Then log event with energy
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

#### 3. Accumulate Energy When Process Starts

**File**: `src/simulation/engine.py` in `advance_time()`

**Location**: Around line 1295-1361, in `PROCESS_START` handler

Replace the current energy calculation with event lookup:

```python
if event.event_type == EventType.PROCESS_START:
    process_run_id = event.data.get("process_run_id")

    # Find the process run in scheduler
    process_run = self.scheduler.active_processes.get(process_run_id)
    if not process_run:
        continue

    # Get energy from the original scheduled event
    energy_kwh = 0.0

    # Look up energy from process_run (which was loaded from scheduled event)
    if hasattr(process_run, 'energy_kwh'):
        energy_kwh = process_run.energy_kwh

    # Accumulate energy into total
    self.state.total_energy_kwh += energy_kwh

    # Store for later retrieval at completion
    if not hasattr(self, '_process_energy'):
        self._process_energy = {}
    self._process_energy[process_run_id] = energy_kwh

    # Log activation event (no changes needed)
    self._log_event(
        ProcessStartEvent(
            process_id=process_run.process_id,
            process_run_id=process_run_id,
            actual_start_time=event.time,
            scale=process_run.scale,
        )
    )
```

#### 4. Update ProcessRun to Store Energy

**File**: `src/simulation/scheduler.py`

Add energy field to `ProcessRun` dataclass:

```python
@dataclass
class ProcessRun:
    """Process execution instance."""
    process_run_id: str
    process_id: str

    scheduled_start_time: float
    scheduled_end_time: float
    duration_hours: float

    scale: float
    inputs_consumed: Dict[str, float]
    outputs_pending: Dict[str, float]

    machine_reservations: List[MachineReservation]

    recipe_run_id: Optional[str] = None
    step_index: Optional[int] = None

    # ADD THIS:
    energy_kwh: Optional[float] = None
```

#### 5. Load Energy When Reconstructing State

**File**: `src/simulation/engine.py` in `load()`

**Location**: Around line 1695-1730, where `process_scheduled` events are read

```python
if event.get("type") != "process_scheduled":
    continue

process_run_id = event.get("process_run_id")
# ... existing code ...

# ADD: Read energy from event
energy_kwh = event.get("energy_kwh", 0.0)

# Create ProcessRun with energy
process_run = ProcessRun(
    process_run_id=process_run_id,
    process_id=process_id,
    scheduled_start_time=scheduled_start_time,
    scheduled_end_time=scheduled_end_time,
    duration_hours=duration_hours,
    scale=scale,
    inputs_consumed=inputs_consumed,
    outputs_pending=outputs_pending,
    machine_reservations=reservations,
    recipe_run_id=recipe_run_id,
    step_index=step_index,
    energy_kwh=energy_kwh,  # ADD THIS
)
```

#### 6. Handle Completed Processes During Load

**File**: `src/simulation/engine.py` in `load()`

For processes that already completed, we need to add their energy to the total:

```python
# Around line 1705
if scheduled_end_time <= self.state.current_time_hours:
    # Process already completed - add its energy to total
    energy_kwh = event.get("energy_kwh", 0.0)
    self.state.total_energy_kwh += energy_kwh
    continue
```

### Testing Plan

#### 1. Unit Tests

**File**: `test/unit/test_energy_persistence.py` (new)

```python
def test_energy_persisted_in_scheduled_event():
    """Energy should be in ProcessScheduledEvent."""
    # Start process with energy model
    # Check logged event has energy_kwh field

def test_energy_accumulated_on_completion():
    """Total energy should increase when process completes."""
    # Schedule process with known energy
    # Advance time to completion
    # Assert total_energy_kwh matches expected

def test_energy_survives_reload():
    """Energy should persist across simulation reload."""
    # Run simulation with energy-consuming processes
    # Save state
    # Reload simulation
    # Assert total_energy_kwh is preserved
```

#### 2. Integration Tests

**File**: `test/integration/test_energy_tracking.py` (new)

```python
def test_multi_process_energy_tracking():
    """Multiple processes should accumulate energy correctly."""
    # Start 3 processes with different energy models
    # Complete all
    # Assert total = sum of individual energies

def test_energy_persistence_across_cli_commands():
    """Energy should survive CLI command boundaries."""
    # Init simulation via CLI
    # Start process via CLI
    # Advance time via CLI (separate command)
    # View state via CLI
    # Assert energy is correct
```

#### 3. Regression Tests

Use existing simulation:
```bash
# Should now show correct energy values
python -m src.cli sim visualize --sim-id robot_build_max_isru_2026_01_09
```

Expected results:
- `regolith_mining_simple_v0` (5100 kg): 255 kWh
- `alumina_extraction_from_highlands_v0` (5 batches): 180 kWh
- `ilmenite_extraction_from_regolith_v0` (50 kg): energy TBD based on model
- `iron_pure_production_from_ilmenite_v0` (30 kg): energy TBD based on model
- **Total**: ~500+ kWh (not 0!)

## Migration Strategy

### Backward Compatibility

**Issue**: Existing simulations have `process_scheduled` events without `energy_kwh` field.

**Solution**: Make field optional, default to 0.0:
- Field is `Optional[float] = None` in model
- Code checks `if energy_kwh is not None` before using
- Old events will be missing the field, calculation will use 0.0
- New events will have the field

**Impact**:
- ✅ Old simulations load without errors
- ⚠️ Old simulations show 0 energy (expected - can't retroactively calculate)
- ✅ New simulations track energy correctly

### Deployment Steps

1. **Update models** (no breaking changes - field is optional)
2. **Update engine** to calculate and store energy at scheduling
3. **Update tests** to verify energy persistence
4. **Run regression tests** on existing simulations
5. **Update documentation** (ADR-020, simulation guide)
6. **Regenerate visualizations** for demonstration simulations

## Alternative Approaches Considered

### Alternative 1: Recalculate Energy at Completion

**Approach**: Read process definition at completion time and recalculate energy.

**Pros**:
- Simpler initial implementation
- No schema changes needed

**Cons**:
- Duplicates calculation logic
- Can't handle recipe overrides (which might modify energy model)
- Energy not available during process execution (for power budgeting)
- Less efficient (calculate twice)

**Decision**: ❌ Rejected - violates event-sourcing principle

### Alternative 2: Add PROCESS_ENERGY Event

**Approach**: Log a separate `process_energy` event when energy is calculated.

**Pros**:
- Separates concerns
- Could support dynamic energy adjustments

**Cons**:
- More complex (extra event type)
- Energy split across multiple events
- Harder to reconstruct state

**Decision**: ❌ Rejected - over-engineered for current needs

### Alternative 3: Store in ProcessStartEvent

**Approach**: Calculate and log energy when process starts.

**Pros**:
- Closer to current implementation
- Energy calculated with actual inventory state

**Cons**:
- Completed processes don't fire START events during reload
- Would still need special handling in load()
- Violates "calculate once" principle

**Decision**: ❌ Rejected - doesn't solve completed process issue

## Success Criteria

1. ✅ Energy values appear in logged events (`process_scheduled`, `process_complete`)
2. ✅ `total_energy_kwh` increases correctly during simulation
3. ✅ Energy persists across CLI command boundaries
4. ✅ Visualizations show non-zero energy consumption
5. ✅ Existing simulations load without errors (backward compatible)
6. ✅ Direct calculation values match logged values
7. ✅ Multiple processes accumulate energy correctly
8. ✅ Recipe steps inherit/override energy models correctly

## Implementation Checklist

- [ ] Update `ProcessScheduledEvent` model with `energy_kwh` field
- [ ] Update `ProcessRun` dataclass with `energy_kwh` field
- [ ] Calculate energy in `start_process()` before logging event
- [ ] Include energy in `ProcessScheduledEvent` instantiation
- [ ] Update `advance_time()` to read energy from process run
- [ ] Update `load()` to read energy from scheduled events
- [ ] Handle completed processes energy accumulation in `load()`
- [ ] Write unit tests for energy calculation persistence
- [ ] Write integration tests for CLI command boundaries
- [ ] Update ADR-020 documentation
- [ ] Update simulation guide with energy tracking explanation
- [ ] Regenerate visualizations for demo simulations
- [ ] Verify energy values in `robot_build_max_isru_2026_01_09`

## References

- **ADR-014**: Energy Model Redesign
- **ADR-020**: Simulation Persistence and Scheduling
- **Issue Location**: `src/simulation/engine.py:1343-1361, 1437-1439, 1705-1706`
- **Test Case**: `robot_build_max_isru_2026_01_09` simulation
- **Related**: Process timeline visualization showing zero energy

## Notes

- This fix is a **critical bug** - energy is a fundamental simulation metric
- The bug was introduced during ADR-020 migration (event-sourcing refactor)
- Energy calculation itself is correct (verified via direct testing)
- Only the persistence mechanism is broken
- Fix aligns with event-sourcing architecture principles
