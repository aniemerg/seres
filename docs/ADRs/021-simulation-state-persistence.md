# 021: Simulation State Persistence and Reconstruction

**Status:** Proposed
**Date:** 2026-01-09
**Decision Makers:** Project team
**Related ADRs:** ADR-004 (Base Builder Simulation), ADR-020 (Recipe Orchestration and Scheduling)

---

## Context

### Current Problem

The ADR-020 simulation engine doesn't persist scheduler state between CLI invocations. When running:

```bash
python -m src.cli sim start-process --sim-id test --process mining_v0 --duration 10
python -m src.cli sim advance-time --sim-id test --hours 10
```

The second command creates a fresh `SimulationEngine` with an empty scheduler, losing all scheduled processes from the first command.

**Result:** The simulation returns "Processes completed: 0" despite having scheduled a 10-hour process.

### Root Cause Analysis

#### 1. Scheduler State is In-Memory Only

The `Scheduler` class (`src/simulation/scheduler.py`) maintains critical state that is never persisted:

```python
class Scheduler:
    current_time: float = 0.0
    event_queue: EventQueue = EventQueue()
    active_processes: Dict[str, ProcessRun] = {}
    completed_processes: List[ProcessRun] = []
```

#### 2. ProcessStartEvent Contains Insufficient Information

Currently logged at line 629 of `src/simulation/engine.py`:

```python
self._log_event(
    ProcessStartEvent(
        process_id=process_id,
        scale=scale,
        ends_at=end_time,
    )
)
```

**Missing critical fields:**
- `process_run_id` - unique instance identifier
- `start_time` - when process starts
- `duration_hours` - how long it runs
- `inputs_consumed` - what was consumed
- `outputs_pending` - what will be produced
- `machines_reserved` - which machines are in use
- `recipe_run_id` / `step_index` - recipe orchestration tracking

#### 3. Load Process Doesn't Reconstruct Scheduler

The `load()` method (`src/simulation/engine.py:1509-1615`) reconstructs:
- ✅ Inventory (from state_snapshot)
- ✅ Machines built (from state_snapshot)
- ✅ Total energy (from state_snapshot)
- ❌ Scheduler event queue (NOT reconstructed)
- ❌ Active processes in scheduler (NOT reconstructed)
- ❌ Scheduler current_time (NOT synced)
- ❌ Machine reservations (NOT reconstructed)
- ❌ Recipe orchestration state (NOT reconstructed)

### Why This Matters

#### Production Use Case Broken
Users expect CLI commands to work incrementally:
```bash
# Day 1: Start long-running processes
sim start-process --sim-id base_001 --process refining_v0 --duration 72

# Day 2: Check progress
sim advance-time --sim-id base_001 --hours 24
sim view-state --sim-id base_001
```

Currently this fails silently - the process vanishes between invocations.

#### ISRU Robot Demonstration Blocked
User requested: "try to create a simulation making a robot from as many in situ resources as possible"

This requires a multi-step workflow:
1. Mine regolith → 2. Extract metals → 3. Manufacture components → 4. Assemble robot

With current state loss, this can only work in a single Python session, not via CLI commands.

---

## What State Must Persist?

### Complete State Inventory

#### 1. Simulation Core State (✅ Already Persisted)

```python
class SimulationState:
    sim_id: str
    current_time_hours: float  # ✅ In state_snapshot
    inventory: Dict[str, InventoryItem]  # ✅ In state_snapshot
    machines_built: List[str]  # ✅ In state_snapshot
    machines_in_use: Dict[str, float]  # ✅ In state_snapshot
    total_energy_kwh: float  # ✅ In state_snapshot (updated on process completion)
    total_imports: Dict[str, InventoryItem]  # ✅ Reconstructed from import events
```

**Status:** WORKING - state_snapshot and import replay handle this. Energy is accumulated at process completion and persisted in each advance-time snapshot, so CLI reloads do not affect totals.

#### 2. Scheduler State (❌ Not Persisted)

```python
class Scheduler:
    current_time: float  # ❌ Starts at 0.0 on every load
    event_queue: EventQueue  # ❌ Empty on load
    active_processes: Dict[str, ProcessRun]  # ❌ Empty on load
    completed_processes: List[ProcessRun]  # ❌ Empty on load
```

**Critical:** Each `ProcessRun` contains:
```python
@dataclass
class ProcessRun:
    process_run_id: str  # Unique runtime ID
    process_id: str  # Process definition ID
    start_time: float  # When it started
    duration_hours: float  # How long it runs
    end_time: float  # start + duration
    scale: float  # Process scale
    inputs_consumed: Dict[str, float]  # What was consumed
    outputs_pending: Dict[str, float]  # What will be produced
    machines_reserved: Dict[str, float]  # Machines in use
    recipe_run_id: Optional[str]  # Parent recipe
    step_index: Optional[int]  # Recipe step
```

**Problem:** When `start_process()` is called, it creates a `ProcessRun` and adds it to `scheduler.active_processes`, but this is never written to the event log in a recoverable format.

#### 3. Event Queue (❌ Not Persisted)

The scheduler's event queue contains scheduled events:

```python
@dataclass
class SchedulerEvent:
    time: float  # When event fires
    event_type: EventType  # PROCESS_START, PROCESS_COMPLETE, MACHINE_RELEASE
    event_id: str  # Unique ID
    priority: int  # Execution order
    data: Dict[str, Any]  # Event-specific data
```

**Typical contents after start_process():**
- `PROCESS_START` event at t=0.0
- `PROCESS_COMPLETE` event at t=10.0
- Potentially `MACHINE_RELEASE` events for partial reservations

**Problem:** The event queue is a priority queue (heap) that's rebuilt on every scheduler creation, starting empty.

#### 4. Machine Reservations (❌ Not Persisted)

```python
class MachineReservationManager:
    machine_capacities: Dict[str, float]  # ✅ Rebuilt from inventory
    reservations: List[Reservation]  # ❌ Empty on load
    current_time: float  # ❌ Starts at 0.0
```

Each `Reservation`:
```python
@dataclass
class Reservation:
    machine_id: str
    process_run_id: str
    reservation_type: ReservationType  # FULL_DURATION or PARTIAL
    start_time: float
    end_time: float
    qty_reserved: float
    hr_reserved: Optional[float]
    release_time: Optional[float]
```

**Problem:** Created during `start_process()` but never logged to events.

#### 5. Recipe Orchestration State (❌ Not Persisted)

```python
class RecipeOrchestrator:
    recipe_runs: Dict[str, RecipeRun]  # ❌ Empty on load
```

Each `RecipeRun` tracks complex state:
```python
@dataclass
class RecipeRun:
    recipe_run_id: str
    recipe_id: str
    dependency_graph: DependencyGraph
    started_at: float
    completed_steps: Set[int]  # Which steps finished
    active_steps: Dict[int, str]  # step_idx -> process_run_id
    scheduled_steps: Dict[int, str]  # Waiting to start
    is_completed: bool
    completed_at: Optional[float]
```

**Problem:** Mid-flight recipe execution is completely lost on reload.

---

## Decision

We will implement **comprehensive state persistence** by enhancing event logging to capture full scheduler state, then reconstructing it during load.

### Design Principles

1. **Event-Sourced State**: All state changes are logged as events; state is reconstructed by replaying events
2. **Idempotent Reconstruction**: Loading a simulation multiple times produces identical state
3. **Backward Compatible**: Older simulations (without enhanced events) continue to work
4. **Minimal Redundancy**: Avoid duplicating state in multiple events
5. **Audit Trail**: Event log provides complete history of what happened and when
6. **Lifecycle Alignment**: Event types align with ADR-020's three-state lifecycle (scheduled → start → complete)

### Approach: Enhanced Event Model with Lifecycle Separation

#### Key Change: Separate Scheduling from Activation

**ADR-020 defines a three-state process lifecycle:**
1. **Scheduled** - Process reserved but not yet started
2. **Started** - Process actively executing
3. **Completed** - Process finished

**Our event model now reflects this:**
- `ProcessScheduledEvent` - Logged when `start_process()` is called
- `ProcessStartEvent` - Logged when scheduler activates the process (during `advance_time`)
- `ProcessCompleteEvent` - Logged when process finishes

This separation prevents semantic ambiguity and enables correct reconstruction of scheduler state at any point in time.

#### 1. Add ProcessScheduledEvent (NEW)

```python
class ProcessScheduledEvent(Event):
    """Process scheduled for future execution.

    Logged when start_process() is called. Contains complete scheduling details
    needed to reconstruct Scheduler.active_processes and event queue.
    """
    type: Literal["process_scheduled"] = "process_scheduled"

    # Process identification
    process_id: str  # Process definition ID
    process_run_id: str  # Unique runtime instance ID

    # Timing
    scheduled_start_time: float  # When process is scheduled to start (simulation hours)
    duration_hours: float  # How long it will run
    scheduled_end_time: float  # scheduled_start_time + duration_hours

    # Scaling
    scale: float  # Process scale factor

    # Resource tracking with units
    inputs_consumed: Dict[str, Dict[str, Any]]  # item_id -> {quantity, unit}
    outputs_pending: Dict[str, Dict[str, Any]]  # item_id -> {quantity, unit}

    # Machine reservations (list to support multiple reservations)
    machine_reservations: List[Dict[str, Any]]

    # Recipe orchestration
    recipe_run_id: Optional[str] = None  # Parent recipe (if part of recipe)
    step_index: Optional[int] = None  # Step within recipe
```

**inputs_consumed / outputs_pending structure:**
```python
{
    "aluminum_ingot": {
        "quantity": 10.0,
        "unit": "kg"
    },
    "robot_arm": {
        "quantity": 1.0,
        "unit": "unit"
    }
}
```

**machine_reservations structure** (list to support multiple segments):
```python
[
    {
        "machine_id": "cnc_mill_v0",
        "start_time": 0.0,
        "end_time": 8.0,  # or release_time for PARTIAL
        "qty": 1.0,
        "unit": "count",
        "reservation_type": "FULL_DURATION"
    },
    {
        "machine_id": "heat_furnace_v0",
        "start_time": 0.0,
        "end_time": 6.0,  # Released early
        "qty": 1.0,
        "unit": "count",
        "reservation_type": "PARTIAL",
        "release_time": 6.0  # Explicitly when to release
    }
]
```

**Key improvements over original design:**
- ✅ Units explicitly stored with quantities (addresses ADR-016 compatibility)
- ✅ Reservations as list (supports multiple reservations per machine)
- ✅ Explicit start/end times per reservation (enables correct partial release reconstruction)
- ✅ Lifecycle-aligned event name (scheduled, not started)

#### 2. Keep ProcessStartEvent for Activation

**Updated schema** (unchanged from current, but semantics clarified):
```python
class ProcessStartEvent(Event):
    """Process activated and began execution.

    Logged during advance_time() when scheduler processes PROCESS_START event.
    Indicates process has actually started running (not just scheduled).
    """
    type: Literal["process_start"] = "process_start"
    process_id: str  # Process definition ID
    process_run_id: str  # Runtime instance ID (links to ProcessScheduledEvent)
    actual_start_time: float  # When it actually started (normally == scheduled_start_time)
    scale: float
```

**Note:** In normal operation, `actual_start_time == scheduled_start_time`. Only differs if simulation is loaded mid-execution and times are adjusted.

#### 2. ProcessCompleteEvent (Already Adequate)

Current schema is sufficient:
```python
class ProcessCompleteEvent(Event):
    type: Literal["process_complete"] = "process_complete"
    process_id: str
    process_run_id: Optional[str] = None
    recipe_run_id: Optional[str] = None
    outputs: Dict[str, InventoryItem]
    energy_kwh: Optional[float] = None
    time_hours: Optional[float] = None
```

**Action:** Ensure `time_hours` is always populated (currently optional).

#### 3. Add RecipeRunEvent (New)

```python
class RecipeRunEvent(Event):
    """Recipe execution started.

    Logged when run_recipe() is called. Enables reconstruction of
    RecipeOrchestrator.recipe_runs.
    """
    type: Literal["recipe_run"] = "recipe_run"

    recipe_run_id: str  # Unique runtime ID
    recipe_id: str  # Recipe definition ID
    target_item_id: str  # What's being built
    quantity: int  # How many

    started_at: float  # Start time

    # Dependency graph serialized
    steps: List[Dict[str, Any]]  # Step definitions
    dependencies: Dict[int, List[int]]  # step_idx -> depends_on
```

#### 4. Add RecipeStepEvent (New)

```python
class RecipeStepEvent(Event):
    """Recipe step state change.

    Logged when steps are scheduled, started, or completed.
    """
    type: Literal["recipe_step"] = "recipe_step"

    recipe_run_id: str
    step_index: int
    event: Literal["scheduled", "active", "completed"]
    process_run_id: Optional[str]  # Associated process (if started)
    time_hours: float
```

---

## Implementation Strategy

### Phase 1: Process-Level Persistence (Minimum Viable Fix)

**Goal:** Make CLI process scheduling work across invocations.

**Scope:** Process scheduling only, defer recipe orchestration.

#### Changes Required

**1. Add ProcessScheduledEvent** (`src/simulation/models.py`)
- Add new ProcessScheduledEvent class with fields listed above
- Keep ProcessStartEvent with minimal fields (process_id, process_run_id, actual_start_time, scale)

**2. Log ProcessScheduledEvent in start_process()** (`src/simulation/engine.py:628-635`)

Current:
```python
self._log_event(
    ProcessStartEvent(
        process_id=process_id,
        scale=scale,
        ends_at=end_time,
    )
)
```

New:
```python
# Prepare inputs_consumed with units
inputs_consumed_with_units = {}
for item_id, qty in inputs_dict.items():
    item = self.kb.get_item(item_id)
    unit = item.unit if hasattr(item, 'unit') else 'kg'
    inputs_consumed_with_units[item_id] = {"quantity": qty, "unit": unit}

# Prepare outputs_pending with units
outputs_pending_with_units = {}
for item_id, qty in outputs_dict.items():
    item = self.kb.get_item(item_id)
    unit = item.unit if hasattr(item, 'unit') else 'kg'
    outputs_pending_with_units[item_id] = {"quantity": qty, "unit": unit}

# Prepare machine_reservations as list with full details
machine_reservations_list = []
for machine_id, qty in machines_reserved.items():
    # Find resource requirement details
    req_unit = 'count'
    req_type = 'FULL_DURATION'
    release_time = None

    process_def = process_model.model_dump() if hasattr(process_model, 'model_dump') else process_model
    for req in process_def.get('resource_requirements', []):
        if req.get('machine_id') == machine_id:
            req_unit = req.get('unit', 'count')
            if req_unit == 'hr' and qty < duration_hours:
                req_type = 'PARTIAL'
                release_time = start_time + qty
            break

    machine_reservations_list.append({
        "machine_id": machine_id,
        "start_time": start_time,
        "end_time": release_time if req_type == 'PARTIAL' else end_time,
        "qty": qty,
        "unit": req_unit,
        "reservation_type": req_type,
        "release_time": release_time,  # Explicit for partial
    })

# Log complete scheduling details
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
    )
)
```

**3. Log ProcessStartEvent in advance_time()** (`src/simulation/engine.py:1313-1320`)

Update the existing ProcessStartEvent logging in advance_time() to use the new minimal schema:
```python
# When processing PROCESS_START event
self._log_event(
    ProcessStartEvent(
        process_id=process_id,
        process_run_id=process_run_id,
        actual_start_time=self.scheduler.current_time,
        scale=scale,
    )
)
```

**4. Add Scheduler Reconstruction** (`src/simulation/engine.py:load()`)

Insert after state_snapshot handling (line 1572):

```python
# Track process_scheduled events for reconstruction
completed_processes = set()  # process_run_ids that completed

# First pass: Identify completed processes
with self.log_file.open("r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
            event_type = event.get("type")
            if event_type == "process_complete":
                process_run_id = event.get("process_run_id")
                if process_run_id:
                    completed_processes.add(process_run_id)
        except json.JSONDecodeError:
            continue

# Second pass: Reconstruct active processes from process_scheduled events
with self.log_file.open("r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
            event_type = event.get("type")

            if event_type == "process_scheduled":
                process_run_id = event.get("process_run_id")
                if not process_run_id:
                    # Malformed event - skip
                    continue

                # Only reconstruct if process hasn't completed
                if process_run_id in completed_processes:
                    continue

                # Only reconstruct if process should still be active
                scheduled_end_time = event.get("scheduled_end_time")
                if scheduled_end_time <= self.state.current_time_hours:
                    # Process should have completed by now
                    # (possibly process_complete event missing - data corruption)
                    continue

                # Extract inputs_consumed and outputs_pending (convert from {item_id: {quantity, unit}} to {item_id: quantity})
                inputs_consumed = {}
                for item_id, item_data in event.get("inputs_consumed", {}).items():
                    if isinstance(item_data, dict):
                        inputs_consumed[item_id] = item_data.get("quantity", 0.0)
                    else:
                        # Old format: item_id -> quantity
                        inputs_consumed[item_id] = item_data

                outputs_pending = {}
                for item_id, item_data in event.get("outputs_pending", {}).items():
                    if isinstance(item_data, dict):
                        outputs_pending[item_id] = item_data.get("quantity", 0.0)
                    else:
                        # Old format: item_id -> quantity
                        outputs_pending[item_id] = item_data

                # Extract machines_reserved (convert from list to dict for ProcessRun)
                machines_reserved_dict = {}
                for res in event.get("machine_reservations", []):
                    machine_id = res.get("machine_id")
                    qty = res.get("qty", 0.0)
                    machines_reserved_dict[machine_id] = qty

                # Reconstruct ProcessRun
                from src.simulation.scheduler import ProcessRun

                process_run = ProcessRun(
                    process_run_id=process_run_id,
                    process_id=event.get("process_id"),
                    start_time=event.get("scheduled_start_time", 0.0),
                    duration_hours=event.get("duration_hours", 0.0),
                    end_time=scheduled_end_time,
                    scale=event.get("scale", 1.0),
                    inputs_consumed=inputs_consumed,
                    outputs_pending=outputs_pending,
                    machines_reserved=machines_reserved_dict,
                    recipe_run_id=event.get("recipe_run_id"),
                    step_index=event.get("step_index"),
                )

                # Add to scheduler's active processes
                self.scheduler.active_processes[process_run_id] = process_run

                # Schedule completion event
                from src.simulation.scheduler import EventType
                self.scheduler.schedule_event(
                    time=scheduled_end_time,
                    event_type=EventType.PROCESS_COMPLETE,
                    event_id=f"complete_{process_run_id}",
                    priority=5,
                    data={
                        'process_run_id': process_run_id,
                        'process_id': event.get("process_id"),
                        'recipe_run_id': event.get("recipe_run_id"),
                        'scale': event.get("scale", 1.0),
                    }
                )

                # Reconstruct machine reservations
                for reservation in event.get("machine_reservations", []):
                    machine_id = reservation.get("machine_id")
                    qty = reservation.get("qty", 0.0)
                    unit = reservation.get("unit", "count")
                    reservation_type = reservation.get("reservation_type", "FULL_DURATION")
                    release_time = reservation.get("release_time")
                    start_time = reservation.get("start_time", 0.0)
                    end_time = reservation.get("end_time", scheduled_end_time)

                    # For PARTIAL reservations, use release_time as end_time
                    # Skip if already released (release_time <= current_time)
                    if reservation_type == "PARTIAL" and release_time:
                        if release_time <= self.state.current_time_hours:
                            # Already released, don't restore
                            continue
                        # Use release_time as the reservation end
                        end_time = release_time

                    success = self.reservation_manager.add_reservation(
                        machine_id=machine_id,
                        process_run_id=process_run_id,
                        start_time=start_time,
                        end_time=end_time,
                        qty=qty,
                        unit=unit,
                    )

                    if not success:
                        # Reservation conflict - log warning but continue
                        print(f"Warning: Could not restore reservation for {machine_id} "
                              f"(process {process_run_id})", file=sys.stderr)

        except json.JSONDecodeError:
            continue
```

**5. Sync Scheduler Times** (`src/simulation/engine.py:load()`)

At end of load(), after all reconstruction:

```python
# Sync scheduler's current_time with simulation state
self.scheduler.current_time = self.state.current_time_hours

# Sync reservation manager's current_time
self.reservation_manager.current_time = self.state.current_time_hours
```

#### Success Criteria for Phase 1

1. ✅ CLI process scheduling works across invocations
2. ✅ Active processes persist and complete correctly
3. ✅ Machine reservations are reconstructed
4. ✅ Scheduler current_time syncs with simulation time
5. ✅ Test `test_scheduler_persistence_across_loads` passes
6. ✅ Backward compatible with old event logs

### Phase 2: Recipe Orchestration Persistence (Future)

**Goal:** Preserve recipe execution state across sessions.

**Complexity:** High - recipes have dependency graphs, partial step completion, multi-process coordination.

**Defer to:** Separate ADR or Phase 2 implementation after Phase 1 stabilizes.

**Workaround:** For now, recipes must complete in a single CLI session. Document this limitation.

---

## Testing Strategy

### Unit Tests

**File:** `test/integration/test_adr020_engine.py`

**New test: `test_scheduler_persistence_across_loads`**

```python
def test_scheduler_persistence_across_loads(self, kb_root, sim_dir):
    """Verify scheduler state persists across save/load cycles."""
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_id = "persistence_test"
    full_sim_dir = sim_dir / sim_id

    # Phase 1: Create, schedule process, save
    engine1 = SimulationEngine(sim_id, kb, full_sim_dir)
    engine1.import_item("ore", 10.0, "kg")
    engine1.import_item("furnace", 1.0, "count")

    result = engine1.start_process(
        process_id="test_process_v0",
        scale=1.0,
        duration_hours=5.0,
    )
    assert result["success"]
    process_run_id = result["process_run_id"]

    # Verify scheduled in engine1
    assert len(engine1.scheduler.active_processes) == 1
    assert process_run_id in engine1.scheduler.active_processes

    engine1.save()

    # Phase 2: Fresh engine, load, verify reconstruction
    engine2 = SimulationEngine(sim_id, kb, full_sim_dir)
    success = engine2.load()
    assert success

    # Critical assertions
    assert engine2.scheduler.current_time == 0.0
    assert len(engine2.scheduler.active_processes) == 1
    assert process_run_id in engine2.scheduler.active_processes

    process_run = engine2.scheduler.active_processes[process_run_id]
    assert process_run.process_id == "test_process_v0"
    assert process_run.duration_hours == 5.0
    assert process_run.end_time == 5.0

    # Phase 3: Advance time, verify completion
    advance_result = engine2.advance_time(5.0)
    assert advance_result["processes_completed"] == 1
    assert engine2.has_item("metal", 1.0, "kg")
```

**Additional test: `test_machine_reservations_persist`**

```python
def test_machine_reservations_persist(self, kb_root, sim_dir):
    """Verify machine reservations are reconstructed correctly."""
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_id = "reservation_test"
    full_sim_dir = sim_dir / sim_id

    # Schedule process using a machine
    engine1 = SimulationEngine(sim_id, kb, full_sim_dir)
    engine1.import_item("ore", 10.0, "kg")
    engine1.import_item("furnace", 1.0, "count")

    engine1.start_process("test_process_v0", scale=1.0, duration_hours=5.0)

    # Verify reservation exists
    furnace_reserved = engine1.reservation_manager.get_reserved_qty(
        machine_id="furnace",
        start_time=0.0,
        end_time=5.0
    )
    assert furnace_reserved == 1.0

    engine1.save()

    # Load fresh engine
    engine2 = SimulationEngine(sim_id, kb, full_sim_dir)
    engine2.load()

    # Verify reservation reconstructed
    furnace_reserved = engine2.reservation_manager.get_reserved_qty(
        machine_id="furnace",
        start_time=0.0,
        end_time=5.0
    )
    assert furnace_reserved == 1.0
```

### Integration Tests (Manual CLI)

```bash
# Test 1: Basic process persistence
python -m src.cli sim init --sim-id cli_test_001
python -m src.cli sim import --sim-id cli_test_001 --item labor_bot_general_v0 --quantity 2 --unit unit
python -m src.cli sim start-process --sim-id cli_test_001 --process regolith_mining_lunar_highlands_v0 --output-quantity 1000 --output-unit kg
python -m src.cli sim view-state --sim-id cli_test_001
# Should show process scheduled

python -m src.cli sim advance-time --sim-id cli_test_001 --hours 10
python -m src.cli sim view-state --sim-id cli_test_001
# Should show regolith in inventory

# Test 2: Multiple processes
python -m src.cli sim init --sim-id cli_test_002
python -m src.cli sim import --sim-id cli_test_002 --item labor_bot_general_v0 --quantity 3 --unit unit
python -m src.cli sim start-process --sim-id cli_test_002 --process regolith_mining_lunar_highlands_v0 --duration 10
python -m src.cli sim start-process --sim-id cli_test_002 --process regolith_mining_simple_v0 --duration 8
python -m src.cli sim advance-time --sim-id cli_test_002 --hours 10
python -m src.cli sim view-state --sim-id cli_test_002
# Should show both regolith types

# Test 3: Partial time advancement
python -m src.cli sim init --sim-id cli_test_003
python -m src.cli sim import --sim-id cli_test_003 --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim start-process --sim-id cli_test_003 --process regolith_mining_lunar_highlands_v0 --duration 20
python -m src.cli sim advance-time --sim-id cli_test_003 --hours 10
# Process should still be active
python -m src.cli sim view-state --sim-id cli_test_003
# No regolith yet
python -m src.cli sim advance-time --sim-id cli_test_003 --hours 10
python -m src.cli sim view-state --sim-id cli_test_003
# Now regolith appears
```

---

## Migration and Backward Compatibility

### Handling Old Event Logs

**Scenario:** User has existing simulations created before this ADR.

**Solution:** Graceful degradation

```python
# In reconstruction logic
if event_type == "process_scheduled":
    # New format - proceed with reconstruction
    process_run_id = event.get("process_run_id")
    if not process_run_id:
        # Malformed event - skip
        continue
    # ... reconstruction logic ...

elif event_type == "process_start":
    # Old format (pre-ADR-021)
    # These don't have sufficient info for reconstruction
    # Skip silently - can't rebuild without ProcessScheduledEvent
    continue
```

**Consequence:** Old simulations (without ProcessScheduledEvent) won't reconstruct active processes, but won't error. On first load, user will see info message: "Loaded simulation with old event format (pre-ADR-021) - scheduled processes will not be reconstructed."

**Migration Path:** Users must re-run old simulations from scratch to generate new event format.

### Event Log Format Version

**Optional enhancement:** Add version field to sim_start event

```python
class SimStartEvent(Event):
    type: Literal["sim_start"] = "sim_start"
    sim_id: str
    event_format_version: str = "2.0"  # NEW
```

**Version semantics:**
- `1.0`: Original format (ADR-004)
- `2.0`: Enhanced persistence (ADR-021)

**Usage:**
```python
def load(self):
    # Detect format version
    event_format_version = "1.0"  # default

    with self.log_file.open("r") as f:
        first_line = f.readline()
        first_event = json.loads(first_line)
        if first_event.get("type") == "sim_start":
            event_format_version = first_event.get("event_format_version", "1.0")

    if event_format_version == "1.0":
        print("Warning: Old event format detected. Scheduled processes may not persist.",
              file=sys.stderr)

    # Proceed with reconstruction...
```

---

## Files Modified

### 1. Event Models (`src/simulation/models.py`)
- **Add ProcessScheduledEvent class** after line 65 (before ProcessStartEvent)
- **Lines 66-72:** Update ProcessStartEvent to minimal schema (process_id, process_run_id, actual_start_time, scale)
- **Lines 74-82:** Ensure ProcessCompleteEvent has time_hours (make it required, not optional)

### 2. Simulation Engine (`src/simulation/engine.py`)
- **Lines 628-635:** Log ProcessScheduledEvent (not ProcessStartEvent) in start_process()
- **Lines 1313-1320:** Update ProcessStartEvent logging in advance_time() to use minimal schema
- **After line 1572:** Add scheduler reconstruction logic in load() (reconstruct from process_scheduled events)
- **After line 1614:** Add scheduler/reservation manager time sync in load()
- **Line 1483:** Add total_energy_kwh to advance_time() return value (already done)

### 3. Tests (`test/integration/test_adr020_engine.py`)
- Add `test_scheduler_persistence_across_loads()`
- Add `test_machine_reservations_persist()`
- Add `test_backward_compatible_old_events()`

### 4. Documentation (`docs/SIMULATION_GUIDE.md`)
- Update "State Persistence" section
- Add "Limitations" section documenting recipe orchestration deferral

---

## Resolution of Review Concerns

This section addresses the critical concerns raised in `design/adr-021-review-notes.md`:

### 1. Event Semantics Mismatch with ADR-020 ✅ RESOLVED
**Concern:** Original design conflated scheduling with activation by logging ProcessStartEvent at schedule time.

**Resolution:**
- Introduced `ProcessScheduledEvent` logged when `start_process()` is called
- Kept `ProcessStartEvent` for actual activation during `advance_time()`
- Clear lifecycle: Scheduled → Started → Completed

### 2. Partial Reservation Reconstruction ✅ RESOLVED
**Concern:** Original design used `end_time=end_time` for all reservations, incorrectly handling partial releases.

**Resolution:**
- For PARTIAL reservations, use `release_time` as the reservation `end_time` during reconstruction
- Skip restoring if `release_time <= current_time` (already released)
- Code in reconstruction logic (lines 626-633 of implementation section)

### 3. Machine Reservation Schema Fidelity ✅ RESOLVED
**Concern:** Dict structure lost information for multiple reservations on same machine.

**Resolution:**
- Changed `machine_reservations` from dict to list in ProcessScheduledEvent
- Each reservation has explicit `start_time`, `end_time`, `qty`, `unit`, `reservation_type`
- Supports multiple reservation segments per machine

### 4. Material Quantity Units ✅ RESOLVED
**Concern:** `inputs_consumed` and `outputs_pending` were `Dict[str, float]` with no units.

**Resolution:**
- Changed to `Dict[str, Dict[str, Any]]` with structure: `{item_id: {quantity, unit}}`
- Units explicitly persisted alongside quantities
- Compatible with ADR-016 conversions

### 5. Recipe Persistence Deferred ⚠️ ACKNOWLEDGED
**Concern:** CLI workflow requires recipe state persistence, not just active processes.

**Resolution:**
- Phase 1 focuses on process-level persistence (achieves minimum viable CLI fix)
- Recipe persistence explicitly deferred to Phase 2 or separate ADR
- Documented limitation: recipes must complete in single CLI session for now
- Added RecipeRunEvent and RecipeStepEvent schemas for future implementation

### 6. Duplicate Event Logging ✅ RESOLVED
**Concern:** ProcessStartEvent logged in both `start_process()` and `advance_time()`.

**Resolution:**
- `ProcessScheduledEvent` logged in `start_process()` (scheduling)
- `ProcessStartEvent` logged in `advance_time()` (activation)
- No duplication - each event has distinct semantics and timing

---

## Consequences

### Positive

1. **CLI Usability:** Users can incrementally build simulations across multiple commands
2. **Production Readiness:** Simulation state can be saved and resumed reliably
3. **Audit Trail:** Event log becomes complete record of all scheduling decisions
4. **Debugging:** Full process state visible in event log for troubleshooting
5. **ISRU Demo:** Enables multi-step ISRU robot manufacturing simulation

### Negative

1. **Event Log Size:** Enhanced events are larger (~5x) due to complete state capture
2. **Complexity:** Load() method becomes more complex with reconstruction logic
3. **Performance:** Two-pass reconstruction (find completed, rebuild active) adds load time
4. **Recipe Limitation:** Recipe orchestration doesn't persist (Phase 2 needed)

### Neutral

1. **Breaking Change:** Old simulations work but don't reconstruct active processes
2. **Testing Burden:** Requires comprehensive integration tests for state reconstruction
3. **Migration Path:** Users need to re-run old simulations to get new format

---

## Alternative Approaches Considered

### Alternative 1: Scheduler Snapshot Event

**Idea:** Create dedicated `SchedulerSnapshotEvent` logged periodically.

```python
class SchedulerSnapshotEvent(Event):
    type: Literal["scheduler_snapshot"] = "scheduler_snapshot"
    current_time: float
    active_processes: List[Dict[str, Any]]  # Serialized ProcessRuns
    queued_events: List[Dict[str, Any]]  # Serialized SchedulerEvents
```

**Pros:**
- Clean separation of concerns
- Single source of truth for scheduler state
- Easy to extend

**Cons:**
- Redundant with ProcessStartEvent data
- Timing issues - when to snapshot?
- Large events with duplicated information
- Doesn't provide audit trail of individual scheduling decisions

**Decision:** Rejected - enhancing ProcessStartEvent is more elegant.

### Alternative 2: Database-Backed State

**Idea:** Replace JSONL with SQLite database for state persistence.

**Pros:**
- Transactional consistency
- Easy querying
- No two-pass reconstruction

**Cons:**
- Major architecture change
- Loses append-only log benefits
- Harder to debug (binary format)
- Migration path complex

**Decision:** Rejected - too invasive for current problem.

### Alternative 3: Implicit Reconstruction

**Idea:** Don't log process_run_id, regenerate it deterministically during load.

**Pros:**
- Smaller events
- No explicit IDs to track

**Cons:**
- Fragile - requires deterministic ID generation
- Hard to debug
- Breaks with any non-determinism in scheduling

**Decision:** Rejected - explicit is better than implicit.

---

## References

- **ADR-004 (Base Builder Simulation):** Original simulation architecture
- **ADR-020 (Recipe Orchestration and Scheduling):** Scheduler design
- **ProcessRun dataclass:** `src/simulation/scheduler.py:115-137`
- **Scheduler class:** `src/simulation/scheduler.py:139-477`
- **MachineReservationManager:** `src/simulation/machine_reservations.py:126-348`
- **Current load() implementation:** `src/simulation/engine.py:1509-1615`
- **ProcessStartEvent current:** `src/simulation/models.py:66-72`

---

## Implementation Timeline

**Estimated Effort:** 3-4 hours

1. **Event Model Changes** (30 min)
   - Update ProcessStartEvent schema
   - Add validation

2. **Logging Updates** (30 min)
   - Enhance start_process() logging
   - Remove duplicate logging in advance_time()

3. **Reconstruction Logic** (90 min)
   - Implement two-pass reconstruction
   - Handle machine reservations
   - Sync times

4. **Testing** (60 min)
   - Write unit tests
   - Run integration tests
   - Manual CLI verification

5. **Documentation** (30 min)
   - Update SIMULATION_GUIDE.md
   - Add inline comments

---

## Status

**Decision:** PROPOSED

**Next Steps:**
1. Review this ADR with team
2. Get approval on approach
3. Implement Phase 1 (process persistence)
4. Validate with ISRU robot simulation
5. Plan Phase 2 (recipe persistence) in separate ADR if needed
