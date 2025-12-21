# CLI Usage Guide for Claude Code

## ⭐ **ALWAYS Use CLI Commands, Not Python**

When working in Claude Code to build components or run simulations:

### ❌ DO NOT:
- Write Python scripts using `from base_builder.interactive import *`
- Try to manage simulation state in Python
- Call Python functions directly

### ✅ DO:
- Use CLI commands via Bash tool
- Run one command per operation
- Preview before advancing time

---

## Basic Command Pattern

```bash
SIM="my_simulation"

# 1. Check state
python -m base_builder.cli_commands view-state --sim-id $SIM

# 2. Import items (bootstrap only)
python -m base_builder.cli_commands import --sim-id $SIM \
  --item <item_id> --quantity <n> --unit <unit>

# 3. Start process
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process <process_id> --duration <hours>

# 4. ALWAYS preview first
python -m base_builder.cli_commands preview --sim-id $SIM --hours <n>

# 5. Execute time advancement
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours <n>

# 6. Verify results
python -m base_builder.cli_commands view-state --sim-id $SIM
```

---

## Available Commands

### view-state
View current simulation state (time, inventory, processes, machines, imports)

```bash
python -m base_builder.cli_commands view-state --sim-id <sim_id>
```

### import
Import item from Earth (minimize usage!)

```bash
python -m base_builder.cli_commands import --sim-id <sim_id> \
  --item <item_id> --quantity <number> --unit <unit>
```

### start-process
Start a production process

```bash
python -m base_builder.cli_commands start-process --sim-id <sim_id> \
  --process <process_id> --scale <number> --duration <hours>
```

### run-recipe
Execute a recipe to produce items

```bash
python -m base_builder.cli_commands run-recipe --sim-id <sim_id> \
  --recipe <recipe_id> --quantity <number>
```

### build-machine
Build a machine from BOM

```bash
python -m base_builder.cli_commands build-machine --sim-id <sim_id> \
  --machine <machine_id>
```

### preview
Preview time advancement (ALWAYS DO THIS BEFORE ADVANCING)

```bash
python -m base_builder.cli_commands preview --sim-id <sim_id> --hours <number>
```

### advance-time
Execute time step (commits changes)

```bash
python -m base_builder.cli_commands advance-time --sim-id <sim_id> --hours <number>
```

### list
List all simulations

```bash
python -m base_builder.cli_commands list
```

---

## Complete Example: Building drive_motor_medium

```bash
SIM="motor_build"

# Step 1: View initial state (may be empty for new sim)
python -m base_builder.cli_commands view-state --sim-id $SIM

# Step 2: Import bootstrap equipment
python -m base_builder.cli_commands import --sim-id $SIM --item labor_bot_general_v0 --quantity 2 --unit unit
python -m base_builder.cli_commands import --sim-id $SIM --item stamping_press_basic --quantity 1 --unit unit
python -m base_builder.cli_commands import --sim-id $SIM --item coil_winding_machine --quantity 1 --unit unit

# Step 3: Import materials (in production, replace with ISRU)
python -m base_builder.cli_commands import --sim-id $SIM --item electrical_steel_sheet --quantity 40 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item aluminum_wire --quantity 28.4 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item bearing_set_heavy --quantity 4 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item fastener_kit_medium --quantity 1 --unit kg

# Step 4: Build motor
python -m base_builder.cli_commands run-recipe --sim-id $SIM --recipe recipe_drive_motor_medium_v1 --quantity 1

# Step 5: Preview
python -m base_builder.cli_commands preview --sim-id $SIM --hours 19

# Step 6: Execute
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 19

# Step 7: Verify
python -m base_builder.cli_commands view-state --sim-id $SIM | grep drive_motor
```

---

## Why CLI Commands Are Better

| Aspect | CLI Commands | Python API |
|--------|-------------|-----------|
| State management | ✅ Automatic (loads/saves per command) | ❌ Manual (session-based) |
| Error handling | ✅ Simple (exit codes) | ❌ Complex (exceptions) |
| Debugging | ✅ Easy (one command = one action) | ❌ Hard (session state issues) |
| Reliability | ✅ Stateless | ❌ Stateful |
| Use in Claude Code | ✅ Perfect via Bash tool | ❌ Session management problems |

---

## Common Patterns

### Pattern 1: Import and Build
```bash
# Import materials
python -m base_builder.cli_commands import --sim-id $SIM --item <material> --quantity <n> --unit kg

# Build component
python -m base_builder.cli_commands run-recipe --sim-id $SIM --recipe <recipe_id>

# Complete (if recipe uses time)
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours <n>
```

### Pattern 2: Process Materials
```bash
# Start process
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process <process_id> --duration <hours>

# Preview
python -m base_builder.cli_commands preview --sim-id $SIM --hours <hours>

# Execute
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours <hours>
```

### Pattern 3: Parallel Processes
```bash
# Start multiple processes
python -m base_builder.cli_commands start-process --sim-id $SIM --process mining_v0 --duration 8
python -m base_builder.cli_commands start-process --sim-id $SIM --process refining_v0 --duration 6
python -m base_builder.cli_commands start-process --sim-id $SIM --process smelting_v0 --duration 4

# Preview all
python -m base_builder.cli_commands preview --sim-id $SIM --hours 8

# Execute (all complete when time reaches their end points)
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 8
```

---

## Template Script

See `scripts/build_component_template.sh` for a complete template showing the standard workflow.

---

## Complete Documentation

- **`docs/CLI_COMMANDS_GUIDE.md`** - Complete reference with all commands
- **`CLI_QUICK_REFERENCE.md`** - Quick reference card
- **`base_builder/README.md`** - Architecture overview
- **`scripts/build_component_template.sh`** - Working template script

---

## Help

```bash
# General help
python -m base_builder.cli_commands --help

# Command-specific help
python -m base_builder.cli_commands import --help
python -m base_builder.cli_commands start-process --help
python -m base_builder.cli_commands run-recipe --help
```

---

## Remember

1. ✅ **ALWAYS use CLI commands in Claude Code**
2. ✅ **ALWAYS preview before advance-time**
3. ✅ **ONE command = ONE action**
4. ❌ **NEVER use Python API in Claude Code**
5. ❌ **NEVER try to manage simulation state yourself**
