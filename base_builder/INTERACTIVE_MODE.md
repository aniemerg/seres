# Interactive Mode - Claude as Agent

This mode allows Claude (in Claude Code) to directly control the base builder simulation through the conversation.

## Setup

Simply import the interactive module:

```python
from base_builder.interactive import *
```

Then initialize a simulation:

```python
init_simulation("claude_base_001")
```

## Available Functions

### Simulation Control

- **`init_simulation(sim_id)`** - Create or load a simulation
- **`view_state()`** - View current state (time, inventory, processes, imports)
- **`start_process(process_id, scale, duration_hours)`** - Start a process
- **`run_recipe(recipe_id, quantity)`** - Run a recipe
- **`build_machine(machine_id)`** - Build a machine from BOM
- **`import_item(item_id, quantity, unit)`** - Import from Earth (minimize!)
- **`preview_step(duration_hours)`** - Preview what will happen
- **`advance_time(duration_hours)`** - Execute time step
- **`get_kb_stats()`** - View KB statistics

### KB Exploration

Use standard tools:
- **`Grep`** - Search KB files
- **`Read`** - Read KB files
- **`Write`** - Create/update KB files (when fixing gaps)

## Example Workflow

```python
# 1. Initialize simulation
result = init_simulation("my_base")
print(result)

# 2. Check current state
state = view_state()
print(state)

# 3. Search for mining processes
# Use Grep tool to search kb/processes for "regolith"

# 4. Read a process definition
# Use Read tool to read kb/processes/regolith_mining_v0.yaml

# 5. Import a robot to bootstrap
result = import_item("labor_bot_general_v0", 1, "count")
print(result)

# 6. Start mining
result = start_process("regolith_mining_v0", scale=1, duration_hours=8)
print(result)

# 7. Preview what will happen
preview = preview_step(8)
print(preview)

# 8. Advance time
result = advance_time(8)
print(result)

# 9. Check new state
state = view_state()
print(state)
```

## How It Works

The interactive module maintains global state:
- `_current_sim` - Current simulation engine instance
- `_kb` - Loaded knowledge base

Each function call operates on this shared state, allowing Claude to:
1. Explore the KB using standard tools (Grep, Read)
2. Make decisions about what to do
3. Execute simulation actions
4. Check results
5. Iterate

## Advantages

- **Direct control**: Claude decides every action
- **Conversational**: Explain reasoning naturally
- **Flexible**: Can pause, analyze, and continue
- **Transparent**: All state visible in conversation

## Example Session

```
Claude: Let me start by initializing a simulation and exploring what's available.

[Claude calls init_simulation("lunar_base_alpha")]

Claude: Good! Now let me search for regolith mining processes.

[Claude uses Grep to search kb/processes for "regolith"]

Claude: I found several regolith-related processes. Let me read the mining one.

[Claude uses Read to read kb/processes/regolith_mining_v0.yaml]

Claude: This process requires a labor_bot_basic_v0. Since I'm starting from scratch,
I'll need to import one from Earth first. This is acceptable as initial bootstrap.

[Claude calls import_item("labor_bot_basic_v0", 1, "count")]

Claude: Now I'll start mining regolith for 8 hours at scale 1.

[Claude calls start_process("regolith_mining_v0", 1, 8)]

Claude: Let me preview what will happen when I advance time.

[Claude calls preview_step(8)]

Claude: Looks good - I'll get 800kg of regolith. Let me execute it.

[Claude calls advance_time(8)]

Claude: Excellent! Now I have regolith. Let me search for what I can do with it...
```

## Tips for Claude

1. **Always preview before advancing time** - Check for errors
2. **Explain reasoning** - Say why you're making each decision
3. **Track imports** - Check total_imports_mass_kg regularly
4. **Handle KB gaps** - When you find missing processes/recipes, note them
5. **Build incrementally** - Focus on one goal at a time
6. **Save progress** - State is auto-saved after advance_time()

## Goal

Build a self-sustaining lunar base using primarily **in situ resources** (regolith).
Minimize imports from Earth. Discover and report KB gaps.
