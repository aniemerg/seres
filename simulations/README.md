# Simulations Directory

This directory contains historical simulation runs for the base_builder lunar manufacturing system.

## Directory Structure

Each simulation is stored in its own subdirectory:

```
simulations/
├── claude_base_001/
│   └── simulation.jsonl          # Event log (270 events)
├── motor_build_v2/
│   └── simulation.jsonl          # Motor + robot parts test (64 events)
├── test_labor_bot_parts/
│   └── simulation.jsonl          # Labor bot component test (7 events)
└── ...
```

## File Format

Each `simulation.jsonl` is a JSON Lines file where each line is a simulation event:

```json
{"type": "sim_start", "timestamp": "2025-12-21T17:04:54Z", "sim_id": "test_labor_bot_parts"}
{"type": "import", "timestamp": "...", "item_id": "aluminum_alloy_ingot", "quantity": 10.0, "unit": "kg"}
{"type": "recipe_start", "timestamp": "...", "recipe_id": "recipe_robot_arm_link_aluminum_v0", "quantity": 1}
{"type": "state_snapshot", "timestamp": "...", "time_hours": 1.0, "inventory": {...}, "active_processes": []}
```

## Event Types

- `sim_start` - Simulation initialized
- `import` - Item imported from Earth
- `process_start` - Manufacturing process started
- `process_complete` - Process finished, outputs added to inventory
- `recipe_start` - Recipe execution started
- `recipe_complete` - Recipe finished
- `machine_built` - New machine constructed
- `state_snapshot` - Complete state captured
- `error` - Error occurred

## Analysis Tools

### Generate Reports

Analyze all simulations:
```bash
python tools/analyze_simulations.py
```

Analyze specific simulation:
```bash
python tools/analyze_simulations.py motor_build_v2
```

Output:
- `docs/simulation_learnings.md` - Human-readable report
- `docs/simulation_learnings.json` - Machine-readable data

### Manual Inspection

View specific simulation events:
```bash
cat simulations/motor_build_v2/simulation.jsonl | python -m json.tool | less
```

Count events:
```bash
wc -l simulations/*/simulation.jsonl
```

Find simulations that tested specific items:
```bash
grep -r "robot_arm_link_aluminum" simulations/*/simulation.jsonl
```

## Current Simulations

| Name | Events | Duration | Focus |
|------|--------|----------|-------|
| claude_base_001 | 270 | 582.7h | Comprehensive: regolith → parts |
| motor_build_v2 | 64 | 8.0h | Motor + labor bot parts |
| drive_motor_build | 49 | 1.0h | Drive motor assembly |
| motor_robot_build | 42 | 3.0h | Combined motor + robot |
| test_labor_bot_parts | 7 | 0.0h | Single part test |

See `docs/simulation_learnings.md` for detailed analysis.

## Creating New Simulations

**Before creating a new simulation**, read:
1. `docs/simulation_quick_start.md` - Step-by-step guide
2. `docs/simulation_best_practices.md` - Lessons learned
3. `docs/simulation_learnings.json` - Past results database

**Naming convention**: `[purpose]_[variant]` (e.g., `motor_build_v2`, `iron_chain_test`)

**Example**:
```python
from base_builder.interactive import *

init_simulation("my_new_simulation")
# ... your simulation code ...
```

The simulation file will be created at `simulations/my_new_simulation/simulation.jsonl`.

## Key Learnings from Past Simulations

### Tested Supply Chains
- ✓ Regolith → iron → base_metal_parts (claude_base_001)
- ✓ Imported parts → drive_motor_medium (motor_build_v2)
- ✓ Imported aluminum → robot_arm_link (test_labor_bot_parts)

### Common Imports
- labor_bot_general_v0 (required for manufacturing)
- fastener_kit_medium (used in 50% of assemblies)
- electrical_steel_sheet (motor cores)
- bearing_set_heavy (mechanical assemblies)

### Performance Patterns
- Mining regolith: 8 hours per 100 kg
- Iron extraction: ~1 hour per kg input
- Recipe assembly: 0.5-2 hours typical
- Full iron chain (regolith → parts): ~40-60 hours

### Common Bottlenecks
1. Material shortages mid-simulation → Solution: Import 20% buffer
2. Process dependencies → Solution: Map full tree before starting
3. Item ID mismatches → Solution: Verify against KB before importing

## Maintenance

### Cleaning Old Simulations

To remove test simulations:
```bash
rm -rf simulations/test_sim/
rm -rf simulations/old_experiment/
```

Then regenerate analysis:
```bash
python tools/analyze_simulations.py
```

### Archiving Successful Simulations

Important simulations should be documented in `simulation_best_practices.md` before archiving.

## See Also

- `base_builder/INTERACTIVE_MODE.md` - Simulation API reference
- `docs/simulation_quick_start.md` - Quick start guide for new simulations
- `docs/simulation_best_practices.md` - Detailed best practices
- `tools/analyze_simulations.py` - Analysis tool source code
