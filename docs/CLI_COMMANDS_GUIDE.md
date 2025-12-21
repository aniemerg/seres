# Base Builder CLI Commands Guide

Complete reference for interacting with simulations via individual commands.

## Overview

The `cli_commands` module provides a command-line interface for running individual simulation operations. Each command:

1. Loads the simulation from disk
2. Performs the requested action
3. Saves the updated state automatically
4. Exits

This allows you to interact with a simulation step-by-step without maintaining a persistent Python session or running an autonomous agent.

## Quick Start

```bash
# View current state
python -m base_builder.cli_commands view-state --sim-id my_sim

# Import materials
python -m base_builder.cli_commands import --sim-id my_sim --item carbon_anode --quantity 2 --unit kg

# Start a process
python -m base_builder.cli_commands start-process --sim-id my_sim \
  --process alumina_extraction_from_highlands_v0 --scale 1 --duration 10

# Preview what will happen
python -m base_builder.cli_commands preview --sim-id my_sim --hours 10

# Advance time to execute
python -m base_builder.cli_commands advance-time --sim-id my_sim --hours 10
```

## Commands Reference

### view-state

View complete simulation state including inventory, processes, and machines.

```bash
python -m base_builder.cli_commands view-state --sim-id <sim_id>
```

**Output:**
- Current simulation time
- Inventory (all items with quantities and units)
- Active processes (with time remaining)
- Machines built
- Total imports from Earth

**Example:**
```bash
$ python -m base_builder.cli_commands view-state --sim-id claude_base_001

=== Simulation: claude_base_001 ===
Time: 465.4 hours (19.4 days)

Inventory (11 items):
  carbon_anode: 6.00 kg
  cryolite_flux: 1.00 kg
  hydrochloric_acid: 20.00 kg
  iron_metal_pure: 14.40 kg
  regolith_lunar_highlands: 100.00 kg
  ...

Active Processes (0):

Machines Built (1):
  labor_bot_general_v0

Total Imports (9 items):
  carbon_anode: 6.00 kg
  ...
  Total mass: ~27.5 kg
```

---

### import

Import an item from Earth. **Use sparingly** - imports are tracked as a failure metric.

```bash
python -m base_builder.cli_commands import --sim-id <sim_id> \
  --item <item_id> --quantity <number> --unit <unit>
```

**Arguments:**
- `--sim-id`: Simulation identifier
- `--item`: Item ID from KB (e.g., `carbon_anode`, `labor_bot_general_v0`)
- `--quantity`: Amount to import (float)
- `--unit`: Unit of measurement (`kg`, `count`, `m3`, etc.)

**Example:**
```bash
# Import 2 kg of carbon anodes
python -m base_builder.cli_commands import --sim-id claude_base_001 \
  --item carbon_anode --quantity 2 --unit kg

# Import a machine
python -m base_builder.cli_commands import --sim-id claude_base_001 \
  --item lathe_engine_v0 --quantity 1 --unit count
```

**Best Practices:**
- Import only for bootstrapping (initial labor bots, critical machines)
- Prefer ISRU (in-situ resource utilization) production
- Check `total_imports_mass_kg` regularly to minimize Earth dependence

---

### start-process

Start a production process that will complete after a specified duration.

```bash
python -m base_builder.cli_commands start-process --sim-id <sim_id> \
  --process <process_id> --scale <number> --duration <hours>
```

**Arguments:**
- `--sim-id`: Simulation identifier
- `--process`: Process ID from KB (e.g., `alumina_extraction_from_highlands_v0`)
- `--scale`: Scale factor (1.0 = normal, 2.0 = double, etc.) [default: 1.0]
- `--duration`: How long to run the process (hours)

**Example:**
```bash
# Mine highland regolith for 8 hours
python -m base_builder.cli_commands start-process --sim-id claude_base_001 \
  --process regolith_mining_highlands_v0 --scale 1 --duration 8

# Extract alumina at 1.5x scale for 10 hours
python -m base_builder.cli_commands start-process --sim-id claude_base_001 \
  --process alumina_extraction_from_highlands_v0 --scale 1.5 --duration 10
```

**Notes:**
- Process must exist in KB (`kb/processes/*.yaml`)
- Required inputs must be in inventory
- Required machines must be built or imported
- Multiple processes can run in parallel
- Use `preview` before `advance-time` to verify outputs

**Common Errors:**
```
✗ Failed to start process: Insufficient hydrochloric_acid: need 10.0 kg
→ Solution: Import or produce the required input first

✗ Failed to start process: Process 'xyz' not found in KB
→ Solution: Check process ID spelling or create the process definition
```

---

### run-recipe

Execute a recipe to produce items (typically for building machines/parts).

```bash
python -m base_builder.cli_commands run-recipe --sim-id <sim_id> \
  --recipe <recipe_id> --quantity <number>
```

**Arguments:**
- `--sim-id`: Simulation identifier
- `--recipe`: Recipe ID from KB (e.g., `recipe_motor_electric_small_v0`)
- `--quantity`: Number of times to run the recipe [default: 1]

**Example:**
```bash
# Build one motor
python -m base_builder.cli_commands run-recipe --sim-id claude_base_001 \
  --recipe recipe_motor_electric_small_v0 --quantity 1

# Produce 10 steel ingots
python -m base_builder.cli_commands run-recipe --sim-id claude_base_001 \
  --recipe recipe_steel_ingot_v0 --quantity 10
```

**Notes:**
- Recipes execute instantly (no time passage)
- All input components must be in inventory
- Recipes often involve multiple process steps
- Check recipe file (`kb/recipes/*.yaml`) to see requirements

---

### build-machine

Build a machine from its BOM (Bill of Materials).

```bash
python -m base_builder.cli_commands build-machine --sim-id <sim_id> \
  --machine <machine_id>
```

**Arguments:**
- `--sim-id`: Simulation identifier
- `--machine`: Machine ID with BOM defined (e.g., `powder_compactor_v0`)

**Example:**
```bash
# Build a powder compactor
python -m base_builder.cli_commands build-machine --sim-id claude_base_001 \
  --machine powder_compactor_v0
```

**Notes:**
- BOM must exist (`kb/boms/bom_<machine>_v0.yaml`)
- All component items must be in inventory with correct quantities
- Machine is added to `machines_built` list
- Building consumes components from inventory

---

### preview

Preview what will happen when time advances, without actually committing changes.

```bash
python -m base_builder.cli_commands preview --sim-id <sim_id> --hours <number>
```

**Arguments:**
- `--sim-id`: Simulation identifier
- `--hours`: Hours to preview (float)

**Example:**
```bash
$ python -m base_builder.cli_commands preview --sim-id claude_base_001 --hours 10

=== Preview: Advance 10 hours ===
Current time: 465.4h
New time: 475.4h

Processes completing: 1

  Process: alumina_extraction_from_highlands_v0
  Ends at: 475.4h
  Outputs:
    alumina_powder: +12.0 kg
    processed_tailings: +98.0 kg
```

**Best Practice:**
- **Always preview before advancing time**
- Verify expected outputs
- Check for errors or insufficient inputs
- Confirm timing is correct

---

### advance-time

Advance simulation time, executing all processes that complete in that period.

```bash
python -m base_builder.cli_commands advance-time --sim-id <sim_id> --hours <number>
```

**Arguments:**
- `--sim-id`: Simulation identifier
- `--hours`: Hours to advance (float)

**Example:**
```bash
$ python -m base_builder.cli_commands advance-time --sim-id claude_base_001 --hours 10

Advancing time by 10.0 hours...
✓ Time advanced
  Old time: 465.4h
  New time: 475.4h
  Completed 1 processes
```

**Notes:**
- State is automatically saved after time advancement
- All processes ending ≤ new_time are completed
- Outputs are added to inventory
- Inputs were already consumed when process started

**Workflow Pattern:**
```bash
# 1. Start a process
start-process --sim-id my_sim --process mining_v0 --duration 8

# 2. Preview (verify)
preview --sim-id my_sim --hours 8

# 3. Execute
advance-time --sim-id my_sim --hours 8

# 4. Check results
view-state --sim-id my_sim
```

---

### list

List all simulations with their current status.

```bash
python -m base_builder.cli_commands list
```

**Example:**
```bash
$ python -m base_builder.cli_commands list

=== Simulations ===

claude_base_001:
  Time: 465.4 hours (19.4 days)
  Inventory: 11 items
  Machines: 1

test_motor:
  Time: 120.0 hours (5.0 days)
  Inventory: 5 items
  Machines: 3
```

---

## Complete Workflow Example

### Goal: Produce aluminum from highland regolith

```bash
SIM="claude_base_001"

# 1. Check current state
python -m base_builder.cli_commands view-state --sim-id $SIM

# 2. Import support materials (bootstrap)
python -m base_builder.cli_commands import --sim-id $SIM --item carbon_anode --quantity 2 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item cryolite_flux --quantity 0.5 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item hydrochloric_acid --quantity 10 --unit kg

# 3. Mine highland regolith
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process regolith_mining_highlands_v0 --scale 1 --duration 8

# 4. Preview and advance
python -m base_builder.cli_commands preview --sim-id $SIM --hours 8
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 8

# 5. Extract alumina
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process alumina_extraction_from_highlands_v0 --scale 1 --duration 10

python -m base_builder.cli_commands preview --sim-id $SIM --hours 10
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 10

# 6. Smelt aluminum (Hall-Héroult process)
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process aluminum_smelting_hall_heroult_v0 --scale 1 --duration 8

python -m base_builder.cli_commands preview --sim-id $SIM --hours 8
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 8

# 7. Verify results
python -m base_builder.cli_commands view-state --sim-id $SIM | grep aluminum
```

---

## Command Chaining with Shell Scripts

Create reusable production sequences:

```bash
#!/bin/bash
# produce_aluminum.sh

SIM_ID=$1
SCALE=${2:-1}

echo "=== Producing Aluminum (Scale: $SCALE) ==="

# Mine highland regolith
echo "Step 1: Mining highland regolith..."
python -m base_builder.cli_commands start-process --sim-id $SIM_ID \
  --process regolith_mining_highlands_v0 --scale $SCALE --duration 8
python -m base_builder.cli_commands advance-time --sim-id $SIM_ID --hours 8

# Extract alumina
echo "Step 2: Extracting alumina..."
python -m base_builder.cli_commands start-process --sim-id $SIM_ID \
  --process alumina_extraction_from_highlands_v0 --scale $SCALE --duration 10
python -m base_builder.cli_commands advance-time --sim-id $SIM_ID --hours 10

# Smelt aluminum
echo "Step 3: Smelting aluminum..."
python -m base_builder.cli_commands start-process --sim-id $SIM_ID \
  --process aluminum_smelting_hall_heroult_v0 --scale $SCALE --duration 8
python -m base_builder.cli_commands advance-time --sim-id $SIM_ID --hours 8

echo "✓ Aluminum production complete!"
python -m base_builder.cli_commands view-state --sim-id $SIM_ID | grep aluminum_alloy_ingot
```

Usage: `./produce_aluminum.sh claude_base_001 1.5`

---

## Tips & Best Practices

### 1. Always Preview Before Advancing

```bash
# Good workflow
start-process ...
preview --hours X        # Check what happens
advance-time --hours X   # Execute

# Bad workflow
start-process ...
advance-time --hours X   # Blindly execute (risky!)
```

### 2. Track Simulation Time

Keep track of when processes complete:

```bash
# Start process at t=100h for 8h duration
start-process ... --duration 8
# Process ends at t=108h

# Advance to completion
advance-time --hours 8   # Now at t=108h
```

### 3. Minimize Imports

```bash
# Check import mass regularly
view-state --sim-id my_sim | grep "Total mass"

# Goal: < 100 kg for bootstrapping
# Anything beyond initial labor bots should be ISRU
```

### 4. Parallel Processes

Multiple processes can run simultaneously:

```bash
# Start multiple processes
start-process --process mining_v0 --duration 8
start-process --process refining_v0 --duration 6
start-process --process smelting_v0 --duration 4

# Advance to when all complete
advance-time --hours 8
```

### 5. Error Handling

If a command fails, check:

```bash
# 1. Verify item exists
grep -r "id: item_name" kb/items/

# 2. Check inventory
view-state --sim-id my_sim | grep item_name

# 3. Verify process exists
grep -r "id: process_name" kb/processes/

# 4. Read process requirements
cat kb/processes/process_name_v0.yaml
```

---

## Troubleshooting

### "Insufficient inputs" Error

```
✗ Failed to start process: Insufficient hydrochloric_acid: need 10.0 kg
```

**Solutions:**
1. Check inventory: `view-state --sim-id my_sim | grep hydrochloric_acid`
2. Import if needed: `import --item hydrochloric_acid --quantity 10 --unit kg`
3. Or produce via process: `start-process --process hcl_production_v0 ...`

### "Process not found" Error

```
✗ Failed to start process: Process 'xyz_v0' not found in KB
```

**Solutions:**
1. Verify process exists: `ls kb/processes/ | grep xyz`
2. Check spelling and version (v0, v1, etc.)
3. Create process definition if missing

### State Not Persisting

If changes don't persist between commands:

- ✓ Commands automatically save state when they modify it
- ✓ Each command loads from disk, performs action, saves, exits
- If issues persist, check file permissions on `simulations/<sim_id>/simulation.jsonl`

### Import Not Working

```
✗ Failed to import: Item 'xyz' not found in KB
```

**Solutions:**
1. Verify item exists: `grep -r "id: xyz" kb/items/`
2. Check if it's a machine: `grep -r "id: xyz" kb/items/machines/`
3. Check if it's a material: `grep -r "id: xyz" kb/items/materials/`

---

## Related Documentation

- [Base Builder README](../base_builder/README.md) - Architecture and autonomous agent mode
- [Interactive Mode Guide](../base_builder/INTERACTIVE_MODE.md) - Python REPL usage
- [Knowledge Base Schema](../kb/schema/README.md) - KB structure and file formats

---

## Advanced Usage

### JSON Output for Scripting

Parse command output for automation:

```bash
# Extract specific inventory item
python -m base_builder.cli_commands view-state --sim-id my_sim 2>/dev/null | \
  grep "aluminum_alloy_ingot:" | \
  awk '{print $2}'
```

### Conditional Execution

```bash
# Only import if not enough material
IRON=$(python -m base_builder.cli_commands view-state --sim-id my_sim 2>/dev/null | \
  grep "iron_metal_pure:" | awk '{print $2}')

if (( $(echo "$IRON < 10" | bc -l) )); then
  python -m base_builder.cli_commands import --sim-id my_sim \
    --item iron_metal_pure --quantity 10 --unit kg
fi
```

### Parallel Simulations

Run multiple simulations with different strategies:

```bash
# Strategy A: Maximum imports
./run_strategy_a.sh sim_a

# Strategy B: Minimum imports
./run_strategy_b.sh sim_b

# Compare results
python -m base_builder.cli_commands view-state --sim-id sim_a | grep "Total mass"
python -m base_builder.cli_commands view-state --sim-id sim_b | grep "Total mass"
```

---

## Getting Help

```bash
# General help
python -m base_builder.cli_commands --help

# Command-specific help
python -m base_builder.cli_commands import --help
python -m base_builder.cli_commands start-process --help
```

For issues or questions:
- Check the [Knowledge Base](../kb/) for process/item definitions
- Review [simulation logs](../simulations/<sim_id>/simulation.jsonl) for detailed events
- File issues at https://github.com/anthropics/claude-code/issues
