# CLI Commands Guide

Complete reference for the unified CLI tool (`python -m src.cli`).

## Overview

The CLI provides three main categories of commands:

1. **KB Tools** - Indexing, validation, auto-fix, closure analysis
2. **Simulation** - Create and run simulations
3. **Queue Tools** - Work queue management

## Quick Reference

```bash
# KB Tools
python -m src.cli index                                    # Build KB index
python -m src.cli validate --id process:regolith_mining_highlands_v0  # Validate item
python -m src.cli auto-fix --dry-run                      # Preview auto-fixes
python -m src.cli closure --all                           # Analyze material closure

# Simulation
python -m src.cli sim init --sim-id my_sim                # Create simulation
python -m src.cli sim import --sim-id my_sim --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim start-process --sim-id my_sim --process mining_v0 --duration 24
python -m src.cli sim advance-time --sim-id my_sim --hours 24
python -m src.cli sim view-state --sim-id my_sim          # View state
python -m src.cli sim status --sim-id my_sim              # Status summary
python -m src.cli sim list                                 # List simulations
python -m src.cli sim plan --process crushing_basic_v0      # Preflight a process/recipe
python -m src.cli sim scaffold --sim-id demo --bootstrap labor_bot_general_v0

# Queue Tools
python -m src.cli queue lease --agent <name>                # Lease next queue item
python -m src.cli queue complete --id <gap_type:item_id> --agent <name> [--verify]
python -m src.cli queue release --id <gap_type:item_id> --agent <name>
python -m src.cli queue verify --id <gap_type:item_id>      # Check gap resolution
python -m src.cli queue ls                                  # Queue status counts
```

---

## KB Tools

### index

Build KB index with validation.

```bash
python -m src.cli index [--kb-root KB_ROOT] [--out-dir OUT_DIR]
```

**Arguments:**
- `--kb-root`: KB root directory (default: `kb`)
- `--out-dir`: Output directory (default: `out`)

**Output Files:**
- `out/index.json` - Full dependency graph
- `out/validation_report.md` - Human-readable validation summary
- `out/validation_issues.jsonl` - All validation issues
- `out/work_queue.jsonl` - Work queue items
- `out/missing_fields.jsonl` - Missing required fields
- `out/closure_errors.jsonl` - Material closure errors

**Example:**
```bash
python -m src.cli index
# Loading KB data...
# Loaded: 870 processes, 2016 recipes, 1959 items, 398 BOMs
# Running 017 validation...
# Found 4 validation issues (0 errors, 4 warnings)
# Indexed 5241 entries into out/index.json
```

---

### validate

Validate a specific KB item.

```bash
python -m src.cli validate --id <type:id> [--kb-root KB_ROOT] [--verbose]
```

**Arguments:**
- `--id`: Item identifier in format `type:id` (e.g., `process:regolith_mining_highlands_v0`, `recipe:recipe_steel_plate_v0`)
- `--kb-root`: KB root directory (default: `kb`)
- `--verbose`: Show detailed output

**Supported Types:**
- `process` - Validate a process
- `recipe` - Validate a recipe

**Example:**
```bash
python -m src.cli validate --id process:regolith_mining_highlands_v0

================================================================================
VALIDATION RESULTS: process:regolith_mining_highlands_v0
================================================================================

Found 1 validation issue(s):
  - 1 ERROR(s)
  - 0 WARNING(s)

ERRORS:
1. process_type_required
   Category: schema
   Message: Missing required field 'process_type'
   Field: process_type
```

---

### auto-fix

Automatically fix validation issues.

```bash
python -m src.cli auto-fix [--dry-run] [--max-fixes N] [--rule RULE] [--level LEVEL] [--input FILE]
```

**Arguments:**
- `--dry-run`: Preview fixes without writing (recommended first)
- `--max-fixes`: Maximum fixes to apply (default: unlimited)
- `--rule`: Only fix specific rule (e.g., `process_type_required`)
- `--level`: Only fix specific level (`error`, `warning`)
- `--input`: Input file (default: `out/validation_issues.jsonl`)
- `--kb-root`: KB root directory (default: `kb`)

**Example:**
```bash
# Preview fixes
python -m src.cli auto-fix --dry-run

# Apply fixes
python -m src.cli auto-fix

# Fix only specific rule
python -m src.cli auto-fix --rule process_type_required
```

**Note:** Auto-fix has limited coverage. Most issues require manual fixes or agent work.

---

### closure

Analyze material closure for machines.

```bash
python -m src.cli closure {--machine MACHINE_ID | --all} [--output FILE]
```

**Arguments:**
- `--machine`: Analyze specific machine
- `--all`: Analyze all machines
- `--output`: Output file (default: stdout)

**Example:**
```bash
# Analyze specific machine
python -m src.cli closure --machine crusher_basic_v0

# Analyze all machines
python -m src.cli closure --all --output out/closure_report.txt
```

**Output:**
- Raw materials (mined/collected locally)
- Imported items (from Earth)
- Unresolved items (missing recipes)
- ISRU percentage

---

## Queue Tools

Work queue operations for leasing, completing, and verifying gaps.

### queue lease

Lease the next available queue item.

```bash
python -m src.cli queue lease --agent <name> [--ttl 900] [--priority gap1,gap2]
```

### queue complete

Mark a leased item complete (optional verify runs indexer first).

```bash
python -m src.cli queue complete --id <gap_type:item_id> --agent <name> [--verify]
```

### queue release

Release a leased item back to pending.

```bash
python -m src.cli queue release --id <gap_type:item_id> --agent <name>
```

### queue verify

Rebuild queue and verify one or more gaps are resolved.

```bash
python -m src.cli queue verify --id <gap_type:item_id> [--id <gap_type:item_id>] [--no-index]
```

### queue ls

Show queue counts by status.

```bash
python -m src.cli queue ls
```

### queue add

Add a manual gap to the queue (single or batch).

```bash
python -m src.cli queue add --gap-type quality_concern --item-id steel_melting_v0 --description "..."
python -m src.cli queue add --file queue_tasks/discovered_issues.jsonl
```

### queue gap-types

List registered gap types.

```bash
python -m src.cli queue gap-types
```

---

## Simulation Commands

### sim init

Create a new simulation.

```bash
python -m src.cli sim init --sim-id <name>
```

**Arguments:**
- `--sim-id`: Simulation identifier (required)

**Example:**
```bash
python -m src.cli sim init --sim-id lunar_base_001
# ✓ Created simulation 'lunar_base_001'
#   Location: simulations/lunar_base_001
#   Log file: simulations/lunar_base_001/simulation.jsonl
```

---

### sim import

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
python -m src.cli sim import --sim-id lunar_base_001 --item labor_bot_general_v0 --quantity 3 --unit unit
# ✓ Imported 3.0 unit of 'labor_bot_general_v0'
```

**Notes:**
- Imports tracked separately in `total_imports`
- Use sparingly - goal is local production
- Shown in `view-state` output

---

### sim start-process

Schedule a process for execution.

```bash
python -m src.cli sim start-process --sim-id <name> --process <process_id> [--scale <n>] [--duration <hours>]
```

**Arguments:**
- `--sim-id`: Simulation ID (required)
- `--process`: Process ID from KB (required)
- `--scale`: Scale factor for inputs/outputs (default: 1.0)
- `--duration`: Duration in hours (optional - calculated if omitted)

**Duration Modes:**

**1. Agent-provided (explicit):**
```bash
python -m src.cli sim start-process --sim-id test --process mining_v0 --duration 10
```

**2. Calculated (from time_model):**
```bash
python -m src.cli sim start-process --sim-id test --process crushing_v0
# Engine calculates duration from process time_model + inputs
```

**Example:**
```bash
python -m src.cli sim start-process --sim-id lunar_base_001 --process regolith_mining_highlands_v0 --duration 24
# ✓ Scheduled process 'regolith_mining_highlands_v0'
#   Duration: 24.00 hours (provided)
#   Scheduled end: 24.00 hours
```

**Notes:**
- Logs `process_scheduled` immediately (used to reconstruct scheduler state across CLI commands)
- Actual activation is logged as `process_start` during `advance-time`

---

### sim run-recipe

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
# ✓ Started recipe 'recipe_steel_plate_v0' (quantity: 5)
#   Steps: 3
#   Duration: 15.50 hours
#   Ends at: 15.50 hours
```

---

### sim build-machine

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
# ✓ Built machine 'crusher_basic_v0'
#   Parts consumed: 5
```

**Notes:**
- Consumes parts from inventory
- Machine added to `machines_built` list
- No time advancement (instant)

---

### sim advance-time

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
5. Energy calculated (014)
6. Events logged

**Example:**
```bash
python -m src.cli sim advance-time --sim-id lunar_base_001 --hours 24
# ✓ Advanced time by 24.0 hours
#   New time: 24.00 hours (1.0 days)
#   Processes completed: 1
#   Total energy consumed: 50.00 kWh
#
# Completed processes:
#   - regolith_mining_highlands_v0 (energy: 50.00 kWh)
#       → regolith_lunar_highlands: 100.00 kg
```

---

### sim preview

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
# === Preview: +24.0 hours ===
# Current time: 0.00 hours
# After advance: 24.00 hours
#
# Processes completing (1):
#   - regolith_mining_highlands_v0 (at 24.00h)
#       → regolith_lunar_highlands: 100.00 kg
```

**Notes:**
- Non-destructive (no state changes)
- Use to plan operations
- Logged to event file

---

### sim view-state

View current simulation state.

```bash
python -m src.cli sim view-state --sim-id <name>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)

**Example:**
```bash
python -m src.cli sim view-state --sim-id lunar_base_001
# === Simulation: lunar_base_001 ===
# Time: 24.0 hours (1.0 days)
# Energy Consumed: 50.00 kWh
#
# Inventory (2 items):
#   labor_bot_general_v0: 3.00 unit
#   regolith_lunar_highlands: 100.00 kg
#
# Active Processes (0):
#
# Machines Built (0):
#
# Total Imports (1 items):
#   labor_bot_general_v0: 3.00 unit
#   Total imported mass: ~0.0 kg
```

---

### sim status

Show a concise metadata summary for a simulation.

```bash
python -m src.cli sim status --sim-id <name>
```

**Arguments:**
- `--sim-id`: Simulation ID (required)

**Example:**
```bash
python -m src.cli sim status --sim-id lunar_base_001
# === Simulation: lunar_base_001 ===
# Time: 24.00 hours (1.00 days)
# Energy: 50.00 kWh
# Inventory items: 2
# Machines built: 0
# Imports tracked: 1
# Imported mass: ~0.00 kg
# Inventory mass: ~100.00 kg
# Inventory count: ~3.00 units
# Processes: 0 active, 1 completed
# Recipes: 0 active, 0 completed
# Events queued: 0
# Next event time: none
# Snapshot: /path/to/simulations/lunar_base_001/snapshot.json
# Events: /path/to/simulations/lunar_base_001/events.jsonl
```

---

### sim list

List all simulations.

```bash
python -m src.cli sim list
```

**Example:**
```bash
python -m src.cli sim list
# Found 3 simulation(s):
#
#   lunar_base_001
#     Created: 2025-12-30T10:00:00.000000Z
#     Path: /path/to/simulations/lunar_base_001
#
#   test_production
#     Created: 2025-12-30T11:30:00.000000Z
#     Path: /path/to/simulations/test_production
```

---

## Legacy Commands (Removed)

The old `base_builder` CLI has been removed. Use `python -m src.cli sim` instead.

---

## See Also

- **`docs/SIMULATION_GUIDE.md`** - Comprehensive simulation guide
- **`docs/README.md`** - KB schema reference
- **`docs/ADRs/`** - Architecture decision records
- **`src/cli.py`** - CLI implementation
- **`src/simulation/cli.py`** - Simulation CLI implementation
### sim plan

Preflight a process or recipe and show immediate blockers.

```bash
python -m src.cli sim plan --process crushing_basic_v0
python -m src.cli sim plan --recipe recipe_labor_bot_basic_v0
```

**Output:**
- Required machines/resources
- Inputs and outputs (when specified)
- Duration/energy calculation readiness (process only)

### sim scaffold

Create a simulation with optional bootstrap imports.

```bash
python -m src.cli sim scaffold --sim-id labor_bot_basic_isru --bootstrap labor_bot_general_v0,assembly_tools_basic
```

**Bootstrap format:** `item_id[:qty[:unit]]`
