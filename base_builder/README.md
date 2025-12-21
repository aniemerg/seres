# Base Builder Simulation

An autonomous agent simulation for building a lunar base from scratch using the knowledge base as the "tech tree".

## Overview

The Base Builder simulation validates KB completeness and generates mission planning data by having an AI agent attempt to build a self-sustaining lunar base starting from nothing. The agent must:

- Mine local regolith (free/infinite)
- Refine materials using processes
- Produce parts using recipes
- Build machines from BOMs
- **Minimize imports from Earth** (tracked as failure mode)
- Handle KB gaps by delegating to kb_fixer subagent

## Quick Start

### Recommended: CLI Commands (For Manual Control)

**⭐ Use this approach when:**
- Working with Claude Code or other assistants
- Running simulations manually
- Creating shell scripts
- Debugging production sequences

```bash
# Complete guide
cat docs/CLI_COMMANDS_GUIDE.md

# Quick reference
cat CLI_QUICK_REFERENCE.md

# Example workflow
SIM="my_base"

# View state
python -m base_builder.cli_commands view-state --sim-id $SIM

# Import bootstrap
python -m base_builder.cli_commands import --sim-id $SIM --item labor_bot_general_v0 --quantity 1 --unit unit

# Start process
python -m base_builder.cli_commands start-process --sim-id $SIM --process regolith_mining_highlands_v0 --duration 8

# Preview & execute
python -m base_builder.cli_commands preview --sim-id $SIM --hours 8
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 8
```

**Why CLI commands are better:**
- ✅ No state management - loads/saves automatically
- ✅ Simple - one command = one action
- ✅ Reliable - no Python session issues
- ✅ Scriptable - works great with bash

---

### Alternative: Autonomous Agent Mode

**Use this for:**
- Fully autonomous exploration
- Long-running automated builds
- Multi-hour unattended operation

### 1. Run Component Tests

```bash
python test_base_builder.py
```

This verifies:
- KB loader works
- Simulation engine works
- Tools are properly registered

### 2. Start a Simulation

```bash
python -m base_builder.cli start --sim-id my_first_base --model gpt-4
```

This will:
- Load the KB
- Create a new simulation
- Start the agent
- Agent begins exploring and building

### 3. Continue a Simulation

```bash
python -m base_builder.cli continue --sim-id my_first_base
```

### 4. List Simulations

```bash
python -m base_builder.cli list
```

### 5. Analyze Results

```bash
python -m base_builder.cli analyze --sim-id my_first_base
```

Shows:
- Total imports (mass tracked)
- Machines built
- KB gaps discovered
- Event timeline

## Architecture

```
base_builder/
├── __init__.py           # Module init
├── models.py             # Pydantic data models
├── kb_loader.py          # Load/index KB data
├── unit_converter.py     # Unit conversions (kg↔m3, etc.)
├── sim_engine.py         # Core simulation logic
├── sim_tools.py          # Agent tools (@function_tool)
├── agent.py              # Agent runner & instructions
├── cli.py                # Command-line interface
└── README.md             # This file

simulations/              # Simulation storage
└── {sim_id}/
    └── simulation.jsonl  # Event log (append-only)
```

## Agent Tools

The agent has access to:

### Simulation Tools

- **`view_state()`** - View current time, inventory, active processes
- **`start_process(process_id, scale, duration_hours)`** - Start a process
- **`run_recipe(recipe_id, quantity)`** - Run a recipe
- **`build_machine(machine_id)`** - Build machine from BOM
- **`import_item(item_id, quantity, unit)`** - Import from Earth (minimize!)
- **`preview_step(duration_hours)`** - Preview what will happen
- **`advance_time(duration_hours)`** - Execute time step

### KB Tools

- **`rg_search(pattern, path, max_matches)`** - Search KB files
- **`read_file(path)`** - Read KB file
- **`write_file(path, content)`** - Create/update KB file

## Simulation Mechanics

### Time Model

- Granularity: minutes, hours, days (agent chooses)
- Processes run for specified duration
- Multiple processes run in parallel
- Time advances when agent commits with `advance_time()`

### Resource Model

**Local Resources (Free):**
- `regolith_lunar_mare` - Iron-rich
- `regolith_lunar_highlands` - Aluminum-rich
- `regolith_carbonaceous` - Carbon-rich
- `regolith_silicate` - Silicon-rich

**Inventory:**
- Tracked with quantity + unit (kg, count, m3, etc.)
- Unit conversions handled automatically

**Machines:**
- Built from BOMs
- Required by processes (not consumed)

**Imports:**
- Tracked separately
- Counted as failure mode
- Should be minimized

### KB Gap Handling

When the agent encounters errors like:
- "Process 'xyz' not found"
- "Recipe 'abc' not found"
- "BOM not found"

The simulation logs a `kb_gap` event. The agent should:
1. Analyze what's missing
2. Delegate to kb_fixer subagent (when implemented)
3. Retry after fix

## Event Log Format

Each simulation creates `simulations/{sim_id}/simulation.jsonl` with events:

```jsonl
{"type": "sim_start", "timestamp": "...", "sim_id": "..."}
{"type": "import", "timestamp": "...", "item_id": "labor_bot_general_v0", "quantity": 1, "unit": "count"}
{"type": "process_start", "timestamp": "...", "process_id": "regolith_mining_v0", "ends_at": 8}
{"type": "state_snapshot", "timestamp": "...", "time_hours": 8, "inventory": {...}}
{"type": "kb_gap", "timestamp": "...", "gap_type": "missing_recipe", "details": "..."}
```

## KB Requirements

The simulation requires:

### 1. Unit Definitions (kb/units/units.yaml)
Defines units and conversion factors.

### 2. Material Properties (kb/materials/properties.yaml)
Defines material densities for mass↔volume conversions.

### 3. Process Definitions (kb/processes/*.yaml)
Should include:
```yaml
id: process_id_v0
name: Process Name
base_rate: "100 kg/hour"
inputs:
  - item_id: input_item
    quantity: 10
    unit: kg
outputs:
  - item_id: output_item
    quantity: 5
    unit: kg
required_machines:
  - labor_bot_basic_v0: 1
scalable: true
```

### 4. Recipe Definitions (kb/recipes/*.yaml)
Should include:
```yaml
id: recipe_id_v0
name: Recipe Name
inputs:
  - item_id: input_item
    quantity: 10
    unit: kg
outputs:
  - item_id: output_item
    quantity: 1
    unit: count
duration: 2
duration_unit: hours
required_machines:
  - machine_id: 1
```

### 5. BOM Definitions (kb/boms/*.yaml)
Should include:
```yaml
id: bom_machine_id
components:
  - item_id: component_1
    quantity: 2
    unit: count
  - item_id: component_2
    quantity: 10
    unit: kg
```

## Success Metrics

1. **Primary:** KB completeness (gaps discovered and fixed)
2. **Secondary:** Low import mass (high ISRU usage)
3. **Tertiary:** Build machines from local materials

## Example Workflow

```python
# Agent's typical workflow:

# 1. Explore KB
rg_search("regolith", "kb/processes")
read_file("kb/processes/regolith_mining_v0.yaml")

# 2. Bootstrap
import_item("labor_bot_general_v0", 1, "count")

# 3. Start mining
start_process("regolith_mining_v0", scale=1, duration_hours=8)

# 4. Preview
preview_step(8)  # Check what will happen

# 5. Advance time
advance_time(8)  # Execute

# 6. Check state
view_state()

# 7. Refine materials
start_process("iron_extraction_v0", scale=1, duration_hours=4)
advance_time(4)

# 8. Build parts
run_recipe("recipe_steel_ingot_v0", quantity=10)
advance_time(2)

# 9. Build machine
build_machine("furnace_induction_v0")
```

## Development

### Adding New Tools

1. Add function to `sim_tools.py` with `@function_tool` decorator
2. Add to `__all__` export list
3. Add to agent's tools list in `agent.py`

### Testing

```bash
# Run component tests
python test_base_builder.py

# Start a test simulation
python -m base_builder.cli start --sim-id test_001

# Analyze results
python -m base_builder.cli analyze --sim-id test_001
```

## Troubleshooting

**"Process not found":**
- Check if process exists: `rg 'id: process_name' kb/processes`
- If missing, create it or import alternative

**"Insufficient inputs":**
- Check inventory: `view_state()`
- Mine more regolith or run prerequisite processes

**"Missing machine":**
- Check machines_built: `view_state()`
- Build the machine from BOM or import it

**Import strategy:**
- Bootstrap: Import 1-2 labor_bots initially
- After that: Use ISRU only
- Last resort: Import when no KB alternative exists

## Related Documentation

- [ADR 004: Base Builder Simulation](../docs/ADRs/004-base-builder-simulation.md) - Architecture decision record
- [Queue Agents](../queue_agents/README.md) - Similar agent architecture (KB workers)

## Future Enhancements

- [ ] Subagent delegation for KB fixes
- [ ] Multi-agent collaboration (multiple bases)
- [ ] Resource constraints (storage limits)
- [ ] Transport/logistics simulation
- [ ] Visualization dashboard
- [ ] Mission planning reports
