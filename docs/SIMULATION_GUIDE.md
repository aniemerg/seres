# Simulation Guide

Complete guide to using the simulation engine for validating KB completeness and modeling production chains.

## Overview

The simulation engine allows you to:
- Validate KB completeness by building from scratch
- Model production chains and dependencies
- Calculate time, energy, and resource requirements
- Test recipe overrides and process variations
- Generate audit trails for accountability

**Key Features:**
- ✅ Runtime validation (017)
- ✅ Energy calculation (014)
- ✅ Time calculation (012)
- ✅ Recipe overrides (013)
- ✅ Material class matching
- ✅ JSONL event logging
- ✅ Preflight planning (`sim plan`)
- ✅ Simulation scaffolding (`sim scaffold`)

## Quick Start

### 1. Create a Simulation

```bash
python -m src.cli sim init --sim-id my_simulation
```

This creates:
- `simulations/my_simulation/` directory
- `events.jsonl` event log
- `snapshot.json` state snapshot

### 2. Import Bootstrap Items

Start with items imported from Earth:

```bash
# Import labor bots (general-purpose machines)
python -m src.cli sim import --sim-id my_simulation --item labor_bot_general_v0 --quantity 3 --unit unit

# Import specific tools if needed
python -m src.cli sim import --sim-id my_simulation --item drilling_rig_basic_v0 --quantity 1 --unit unit
```

### 3. Start Production

```bash
# Schedule a process (engine calculates duration OR you provide it)
python -m src.cli sim start-process --sim-id my_simulation --process regolith_mining_highlands_v0 --duration 24

# Or let engine calculate duration from time_model
python -m src.cli sim start-process --sim-id my_simulation --process crushing_basic_v0
```

### 4. Advance Time

```bash
# Preview what will happen
python -m src.cli sim preview --sim-id my_simulation --hours 24

# Advance time (completes processes, adds outputs to inventory)
python -m src.cli sim advance-time --sim-id my_simulation --hours 24
```

### 5. Check State

```bash
python -m src.cli sim view-state --sim-id my_simulation
python -m src.cli sim status --sim-id my_simulation
```

## Commands Reference

### init

Create a new simulation.

```bash
python -m src.cli sim init --sim-id <name>
```

**Arguments:**
- `--sim-id`: Simulation identifier (required)

**Example:**
```bash
python -m src.cli sim init --sim-id lunar_base_001
```

### import

Import items from Earth.

```bash
python -m src.cli sim import --sim-id <name> --item <item_id> --quantity <n> --unit <unit>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--item`: Item ID from KB (required)
- `--quantity`: Amount to import (required)
- `--unit`: Unit (kg, unit, L, etc.) (required)

**Example:**
```bash
python -m src.cli sim import --sim-id lunar_base_001 --item steel_plate --quantity 100 --unit kg
```

**Ensure a minimum quantity:**
```bash
python -m src.cli sim import --sim-id lunar_base_001 --item steel_plate --quantity 100 --unit kg --ensure
```

**Notes:**
- Imports are tracked separately (shown in `total_imports`)
- Use for bootstrap items that can't be manufactured yet
- Avoid over-importing - the goal is local production

### start-process

Schedule a process for execution.

```bash
python -m src.cli sim start-process --sim-id <name> --process <process_id> [--scale <n>] [--duration <hours>]
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--process`: Process ID from KB (required)
- `--scale`: Scale factor for inputs/outputs (default: 1.0)
- `--duration`: Duration in hours (optional - engine will calculate if omitted)

**Duration Modes:**

1. **Agent-provided** (explicit):
   ```bash
   python -m src.cli sim start-process --sim-id test --process mining_v0 --duration 10
   ```

2. **Calculated** (from time_model):
   ```bash
   python -m src.cli sim start-process --sim-id test --process crushing_v0
   # Engine calculates duration from process time_model + inputs
   ```

**Example:**
```bash
# Standard process
python -m src.cli sim start-process --sim-id lunar_base_001 --process regolith_mining_highlands_v0 --duration 24

# Scaled process (2x inputs/outputs)
python -m src.cli sim start-process --sim-id lunar_base_001 --process alumina_extraction_v0 --scale 2.0
```

**Behavior:**
- Logs a `process_scheduled` event with full timing and reservation details
- Actual activation is logged as `process_start` when time advances

**Validation:**
- Process must exist in KB
- Required inputs must be in inventory
- No ERROR-level validation issues

### run-recipe

Execute a recipe (multi-step process).

```bash
python -m src.cli sim run-recipe --sim-id <name> --recipe <recipe_id> [--quantity <n>]
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--recipe`: Recipe ID from KB (required)
- `--quantity`: Number of batches (default: 1)

**Example:**
```bash
python -m src.cli sim run-recipe --sim-id lunar_base_001 --recipe recipe_steel_plate_v0 --quantity 5
```

**Notes:**
- Recipe steps executed sequentially
- Overrides resolved per 013
- Total duration = sum of step durations

### build-machine

Build a machine from its BOM.

```bash
python -m src.cli sim build-machine --sim-id <name> --machine <machine_id>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--machine`: Machine ID from KB (required)

**Example:**
```bash
python -m src.cli sim build-machine --sim-id lunar_base_001 --machine crusher_basic_v0
```

**Notes:**
- Consumes parts from inventory
- Machine added to `machines_built` list
- No time advancement (instant assembly)

### advance-time

Advance simulation time.

```bash
python -m src.cli sim advance-time --sim-id <name> --hours <n>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--hours`: Hours to advance (required)

**What Happens:**
1. Time advances by specified duration
2. Scheduled processes whose start time is reached become active (`process_start`)
3. Active processes whose end time is reached complete (`process_complete`)
4. Outputs added to inventory
5. Energy consumption calculated (014)
6. Events logged

**Example:**
```bash
python -m src.cli sim advance-time --sim-id lunar_base_001 --hours 24
```

**Output:**
```
✓ Advanced time by 24.0 hours
  New time: 24.00 hours (1.0 days)
  Processes completed: 2
  Total energy consumed: 156.50 kWh

Completed processes:
  - regolith_mining_highlands_v0 (energy: 50.00 kWh)
      → regolith_lunar_highlands: 100.00 kg
  - alumina_extraction_v0 (energy: 106.50 kWh)
      → alumina_powder: 45.00 kg
```

### preview

Preview time advancement without committing.

```bash
python -m src.cli sim preview --sim-id <name> --hours <n>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--hours`: Hours to preview (required)

**Example:**
```bash
python -m src.cli sim preview --sim-id lunar_base_001 --hours 24
```

**Output:**
```
=== Preview: +24.0 hours ===
Current time: 0.00 hours
After advance: 24.00 hours

Processes completing (2):
  - regolith_mining_highlands_v0 (at 8.00h)
      → regolith_lunar_highlands: 100.00 kg
  - crushing_basic_v0 (at 15.00h)
      → crushed_ore: 80.00 kg
```

**Notes:**
- Non-destructive (state not modified)
- Use to plan operations
- Saved to event log for audit trail

### view-state

View current simulation state.

```bash
python -m src.cli sim view-state --sim-id <name>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)

**Example:**
```bash
python -m src.cli sim view-state --sim-id lunar_base_001
```

**Output:**
```
=== Simulation: lunar_base_001 ===
Time: 24.0 hours (1.0 days)
Energy Consumed: 156.50 kWh

Inventory (5 items):
  alumina_powder: 45.00 kg
  labor_bot_general_v0: 3.00 unit
  regolith_lunar_highlands: 100.00 kg
  steel_plate: 25.00 kg
  water: 10.00 L

Active Processes (1):
  iron_smelting_v0 (ends at 48.0h, 24.0h remaining)

Machines Built (2):
  crusher_basic_v0
  furnace_basic_v0

Total Imports (4 items):
  labor_bot_general_v0: 3.00 unit
  steel_plate: 100.00 kg
  ...
  Total imported mass: ~150.0 kg
```

### status

Show a concise metadata summary for a simulation.

```bash
python -m src.cli sim status --sim-id <name>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)

**Example:**
```bash
python -m src.cli sim status --sim-id lunar_base_001
```

**Output:**
```
=== Simulation: lunar_base_001 ===
Time: 24.00 hours (1.00 days)
Energy: 156.50 kWh
Inventory items: 5
Machines built: 2
Imports tracked: 4
Imported mass: ~150.00 kg
Inventory mass: ~220.00 kg
Inventory volume: ~0.010 m3
Inventory count: ~3.00 units
Processes: 1 active, 4 completed
Recipes: 0 active, 1 completed
Events queued: 2
Next event time: 48.00 hours
Snapshot: /path/to/simulations/lunar_base_001/snapshot.json
Events: /path/to/simulations/lunar_base_001/events.jsonl
```

### list

List all simulations.

```bash
python -m src.cli sim list
```

### runbook

Run a Markdown runbook with YAML command cells. See ADR-022 for the spec.

Runbooks live in `runbooks/` and use fenced `sim-runbook` blocks:

```markdown
```sim-runbook
- cmd: sim.use
  args:
    sim-id: demo
- cmd: sim.reset
  args:
    sim-id: demo
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
- cmd: sim.start-process
  args:
    process: regolith_mining_highlands_v0
    duration: 24
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.status
  args: {}
```
```

Execute a runbook:

```bash
python -m src.cli sim runbook --file runbooks/lunar_base_demo.md
```

Notes:
- Only `sim.*` commands are allowed.
- `sim.use` sets the default `sim-id` for later steps.
- `sim.reset` clears an existing sim directory and re-initializes it.
- `sim.note` prints a runbook-friendly message with `style` (info, milestone, warning, success, note, dim).
- `sim.runbook` runs another runbook; child runbooks ignore `sim.use` and `sim.reset`.

**Reference:** `docs/ADRs/022-simulation-runbooks.md`

**Output:**
```
Found 3 simulation(s):

  lunar_base_001
    Created: 2025-12-30T10:00:00.000000Z
    Path: /path/to/simulations/lunar_base_001

  test_production
    Created: 2025-12-30T11:30:00.000000Z
    Path: /path/to/simulations/test_production

  ...
```

## Common Workflows

### Bootstrap From Scratch

Build a production facility from minimal Earth imports:

```bash
# 1. Create simulation
python -m src.cli sim init --sim-id bootstrap_test

# 2. Import minimal bootstrap
python -m src.cli sim import --sim-id bootstrap_test --item labor_bot_general_v0 --quantity 2 --unit unit
python -m src.cli sim import --sim-id bootstrap_test --item power_supply_basic_v0 --quantity 1 --unit unit

# 3. Start resource extraction
python -m src.cli sim start-process --sim-id bootstrap_test --process regolith_mining_highlands_v0 --duration 24

# 4. Advance and check
python -m src.cli sim advance-time --sim-id bootstrap_test --hours 24
python -m src.cli sim view-state --sim-id bootstrap_test

# 5. Process raw materials
python -m src.cli sim start-process --sim-id bootstrap_test --process alumina_extraction_v0 --duration 48
python -m src.cli sim advance-time --sim-id bootstrap_test --hours 48

# 6. Continue production chain...
```

### Test Recipe Variations

Compare different production methods:

```bash
# Simulation A: Standard method
python -m src.cli sim init --sim-id method_a
python -m src.cli sim import --sim-id method_a --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim run-recipe --sim-id method_a --recipe recipe_steel_plate_standard_v0
python -m src.cli sim view-state --sim-id method_a

# Simulation B: Alternative method
python -m src.cli sim init --sim-id method_b
python -m src.cli sim import --sim-id method_b --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim run-recipe --sim-id method_b --recipe recipe_steel_plate_additive_v0
python -m src.cli sim view-state --sim-id method_b

# Compare energy, time, yield
```

### Validate Machine BOM

Ensure a machine can be built from available resources:

```bash
# 1. Create simulation
python -m src.cli sim init --sim-id bom_test

# 2. Import expected parts
python -m src.cli sim import --sim-id bom_test --item steel_plate --quantity 50 --unit kg
python -m src.cli sim import --sim-id bom_test --item electric_motor_small --quantity 2 --unit unit
# ... (all BOM parts)

# 3. Try to build
python -m src.cli sim build-machine --sim-id bom_test --machine crusher_basic_v0

# Success: Machine built
# Failure: Shows missing parts
```

## Advanced Features

### Duration Calculation

The engine can calculate process duration from `time_model`:

**Continuous processes (linear_rate):**
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: input_material
```

Duration = `input_qty / rate` (e.g., 100 kg / 10 kg/hr = 10 hours)

**Batch processes:**
```yaml
process_type: batch
time_model:
  type: batch
  hr_per_batch: 2.0
  setup_hr: 0.5  # Optional
```

Duration = `setup_hr + hr_per_batch` (e.g., 0.5 + 2.0 = 2.5 hours)

### Energy Calculation

Energy automatically calculated per 014:

**Per-unit energy:**
```yaml
energy_model:
  type: per_unit
  value: 0.5
  unit: kWh/kg
  scaling_basis: input_material
```

Energy = `input_qty * value` (e.g., 100 kg * 0.5 kWh/kg = 50 kWh)

**Fixed per batch:**
```yaml
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
```

Energy = `120.0 kWh` per batch

### Recipe Overrides

Recipes can override process time/energy models per 013:

**Complete override** (step has `type` field):
```yaml
steps:
  - process_id: crushing_basic_v0
    time_model:
      type: linear_rate  # ← Complete override
      rate: 50.0
      rate_unit: kg/hr
      scaling_basis: ore
```

**Partial override** (step lacks `type` field):
```yaml
steps:
  - process_id: crushing_basic_v0
    time_model:
      rate: 50.0  # ← Merges with process time_model
```

### Event Logging

All actions logged to `simulation.jsonl`:

```json
{"type": "sim_start", "timestamp": "2025-12-30T10:00:00Z", "sim_id": "lunar_base_001"}
{"type": "import", "item_id": "labor_bot_general_v0", "quantity": 3.0, "unit": "unit"}
{"type": "process_scheduled", "process_id": "regolith_mining_highlands_v0", "scheduled_start_time": 0.0, "scheduled_end_time": 24.0}
{"type": "process_start", "process_id": "regolith_mining_highlands_v0", "actual_start_time": 0.0}
{"type": "process_complete", "process_id": "regolith_mining_highlands_v0", "time_hours": 24.0, "energy_kwh": 50.0, "outputs": {...}}
```

Use for:
- Audit trail
- Replay simulations
- Debug issues
- Export to other tools

## State Persistence and Lifecycle

- CLI commands load and save simulation state on every invocation.
- `start-process` records a `process_scheduled` event so the scheduler can be rebuilt across commands.
- `advance-time` activates scheduled work (`process_start`) and completes work (`process_complete`).
- Phase 1 persistence covers scheduled/active processes; recipe orchestration persistence is still deferred and recipes should complete within one CLI session.

## Troubleshooting

### Process Start Fails

**Error:** "Input item 'X' not found in inventory"

**Solution:** Import or produce the required input first.

```bash
python -m src.cli sim import --sim-id test --item X --quantity 10 --unit kg
```

**Error:** "Validation errors: process_type_required"

**Solution:** The process has validation errors in the KB. Fix the process YAML first.

```bash
python -m src.cli validate --id process:process_id
# Fix issues in kb/processes/process_id.yaml
python -m src.cli index  # Rebuild index
```

### Machine Build Fails

**Error:** "Missing parts: steel_plate (need 50.0 kg)"

**Solution:** Produce or import missing parts.

```bash
# Option 1: Import
python -m src.cli sim import --sim-id test --item steel_plate --quantity 50 --unit kg

# Option 2: Produce via recipe
python -m src.cli sim run-recipe --sim-id test --recipe recipe_steel_plate_v0
python -m src.cli sim advance-time --sim-id test --hours 10
```

### Energy Calculation Warning

**Warning:** "⚠️ Energy calculation failed for process_id: missing energy_model"

**Solution:** The process is missing an `energy_model`. Add one to the process YAML:

```yaml
energy_model:
  type: per_unit
  value: 0.5
  unit: kWh/kg
  scaling_basis: input_material
```

### Duration Calculation Error

**Error:** "Must provide either duration_hours or (output_quantity + output_unit)"

**Solution:** Either:
1. Provide explicit duration: `--duration 10`
2. Add `time_model` to the process so engine can calculate

## Best Practices

### 1. Start Small

Begin with a simple production chain:
```
regolith → crushing → ore → smelting → metal → parts → machine
```

### 2. Validate Incrementally

After each step:
```bash
python -m src.cli sim view-state --sim-id test
# Check inventory, energy, time
```

### 3. Use Preview

Before committing to time advancement:
```bash
python -m src.cli sim preview --sim-id test --hours 24
# Verify expected outputs
python -m src.cli sim advance-time --sim-id test --hours 24
```

### 4. Track Import Ratio

Goal: Maximize local production, minimize imports.

```
ISRU% = (local_production_mass / total_mass) * 100
```

Target: >90% ISRU for mature base.

### 5. Monitor Energy

Energy is a constraint on lunar operations:
```bash
python -m src.cli sim view-state --sim-id test | grep "Energy Consumed"
```

Compare to available solar/nuclear power capacity.

## See Also

- `docs/CLI_COMMANDS_GUIDE.md` - Complete CLI reference
- `docs/ADRs/012-process-types-and-time-model.md` - Time model specification
- `docs/ADRs/013-recipe-override-mechanics.md` - Override resolution rules
- `docs/ADRs/014-energy-model-redesign.md` - Energy calculation specification
- `docs/ADRs/017-validation-and-error-detection.md` - Validation rules
- `src/simulation/engine.py` - Engine implementation
- `src/simulation/cli.py` - CLI implementation
### plan

Preflight a process or recipe to see required machines, inputs, and calculation readiness.

```bash
python -m src.cli sim plan --process crushing_basic_v0
python -m src.cli sim plan --recipe recipe_labor_bot_basic_v0
```

**Output:**
- Required machines/resources
- Inputs and outputs (when specified)
- Duration/energy calculation readiness (process only)

### scaffold

Create a simulation and optionally import bootstrap items in one step.

```bash
python -m src.cli sim scaffold --sim-id labor_bot_basic_isru --bootstrap labor_bot_general_v0,assembly_tools_basic
```

**Bootstrap format:** `item_id[:qty[:unit]]` (defaults: `1 unit`)
