# Simulation Best Practices & Lessons Learned

**Purpose**: This document captures learnings from past simulations to help future Claude Code sessions design better, more efficient simulations.

**Last Updated**: 2025-12-21

---

## Quick Reference: Tested Supply Chains

These supply chains have been successfully tested in simulations:

### Base Material Production (from regolith)
```
regolith_lunar_mare (mining: 8h/100kg)
  ↓ ilmenite_extraction_from_regolith_v0 (1h/kg input)
iron_ore_or_ilmenite (60% yield)
  ↓ iron_pure_production_from_ilmenite_v0 (1h/kg)
iron_metal_pure
  ↓ iron_powder_from_pure_iron_v0 (0.5h/kg)
iron_powder_or_sheet
  ↓ base_metal_parts_from_raw_metal_v0 (0.5h/3kg)
base_metal_parts
```

### Motor Manufacturing
Successfully tested in `motor_build_v2` (8 hours total):
```
Imports: electrical_steel_sheet, aluminum_wire, bearing_set_heavy, coil_insulation_material
  ↓
stator_rotor_lamination_set (recipe_stator_rotor_lamination_set_v0)
motor_coil_wound (recipe_motor_coil_wound_v0)
motor_housing_steel (recipe_motor_housing_steel_v0)
motor_shaft_steel (recipe_motor_shaft_steel_v0)
  ↓
drive_motor_medium (recipe_drive_motor_medium_v1)
```

### Labor Bot Parts Manufacturing
Successfully tested in `motor_build_v2` (8 hours total):
```
robot_arm_link_aluminum (recipe_robot_arm_link_aluminum_v0: 1h, 10kg Al → 1 unit)
robot_wrist_3axis (recipe_robot_wrist_3axis_v0)
thermal_management_system (recipe_thermal_management_system_v0)
protective_cover_set (recipe_protective_cover_set_v0)
electric_parallel_gripper (recipe_electric_parallel_gripper_v0)
```

---

## Import Strategies

### Most Commonly Imported Items (across all simulations)
1. **labor_bot_general_v0** - Standard starting machine
2. **fastener_kit_medium** - Used in ~50% of recipes
3. **coil_insulation_material** - Motor manufacturing
4. **aluminum_wire** - Motor coils
5. **aluminum_alloy_ingot** - Generic metal stock
6. **electrical_steel_sheet** - Motor cores
7. **bearing_set_heavy** - Mechanical assemblies

### Import vs. Manufacture Decision Matrix

| Item Type | Decision | Rationale |
|-----------|----------|-----------|
| Precision bearings | IMPORT | Require precision grinding not yet bootstrapped |
| Electrical steel | IMPORT | Requires specific alloy composition & processing |
| Motors (BLDC) | IMPORT | Requires magnets (NdFeB) not available on Moon |
| Aluminum stock | MANUFACTURE | Can extract from anorthite (highlands regolith) |
| Iron/steel parts | MANUFACTURE | Can extract from ilmenite (mare regolith) |
| Simple fasteners | IMPORT (Phase 1) | Later: manufacture from wire |

---

## Performance Patterns

### Simulation Scale vs. Duration
- **Small tests** (10 events): 0-18 hours sim time
  - Good for testing single supply chains
  - Example: `test_material_class` - 18h, 3 supply chains

- **Medium builds** (40-60 events): 1-8 hours sim time
  - Good for testing complete assemblies
  - Example: `motor_build_v2` - 8h, 10 recipes, 32 final items

- **Comprehensive** (270+ events): 500+ hours sim time
  - Full production chains from regolith to finished goods
  - Example: `claude_base_001` - 582h, 28 supply chains, 29 final items

### Event Density Patterns
- **Process-heavy** simulations: 0.5-1 events/hour
  - Long running processes (mining, extraction, refining)
  - Lower event count but longer duration

- **Recipe-heavy** simulations: 15-50 events/hour
  - Mostly imports + recipe starts/completions
  - Higher event count, shorter duration

---

## Common Bottlenecks

### Material Shortages
**Problem**: Running out of base materials mid-simulation

**Solutions**:
1. Pre-calculate total material needs for all recipes
2. Import 20% buffer beyond calculated needs
3. For regolith-based chains, start multiple mining operations in parallel

**Example**: Building 1 motor requires:
- 10 kg aluminum_alloy_ingot (for housings)
- 5 kg electrical_steel_sheet (for stator/rotor)
- 2 kg aluminum_wire (for coils)
- Fasteners, bearings, insulation (various)

### Process Dependencies
**Problem**: Processes blocking on unavailable inputs

**Solutions**:
1. Map full dependency tree before starting simulation
2. Ensure prerequisite processes complete before dependent ones
3. Use `view_state()` frequently to check inventory

**Tested Chain** (from `claude_base_001`):
```
1. Start: regolith_mining_simple_v0 (8h)
2. Wait for completion
3. Start: ilmenite_extraction_from_regolith_v0 (10h)
4. Wait for completion
5. Start: iron_pure_production_from_ilmenite_v0 (12h)
... and so on
```

---

## Recipe Validation Checklist

Before running a recipe in simulation:

- [ ] All input items exist in KB
- [ ] All input items have valid mass/qty/unit
- [ ] Recipe target_item exists in KB
- [ ] All processes in recipe steps exist
- [ ] No circular dependencies
- [ ] Input quantities are realistic (check similar recipes)

**Common Issues**:
- ❌ `bearing_set_industrial` (8kg) used where `bearing_set_small` (0.3kg) needed
- ❌ `copper_metal` instead of `copper_rod_ingot`
- ❌ `water_deionized` instead of `deionized_water`

---

## Successful Simulation Patterns

### Pattern 1: Component Testing
**Use case**: Verify a single recipe works
**Structure**:
```python
init_simulation("test_component_X")
import_item("input1", qty, unit)
import_item("input2", qty, unit)
run_recipe("recipe_X_v0", quantity=1)
advance_time(duration)
view_state()  # Verify output in inventory
```

**Example**: `test_labor_bot_parts` - tested single robot arm link recipe

### Pattern 2: Assembly Testing
**Use case**: Build complete machine from imported parts
**Structure**:
```python
init_simulation("test_assembly_X")
# Import ALL components from BOM
for component in bom:
    import_item(component, qty, unit)
# Run assembly recipes in dependency order
run_recipe("recipe_subassembly1_v0", 1)
run_recipe("recipe_subassembly2_v0", 1)
run_recipe("recipe_final_assembly_v0", 1)
```

**Example**: `motor_build_v2` - built complete motor + robot parts

### Pattern 3: Full Supply Chain
**Use case**: Test production from raw materials to finished goods
**Structure**:
```python
init_simulation("test_full_chain_X")
# Import only initial seed items (labor_bot, initial machines)
import_item("labor_bot_general_v0", 1, "unit")

# Run base material production
run_process("regolith_mining_simple_v0", scale=1.0)
advance_time(8)  # Wait for mining

# Extract resources
run_process("ilmenite_extraction_from_regolith_v0", scale=10.0)
advance_time(10)

# Continue through refinement and manufacturing...
```

**Example**: `claude_base_001` - regolith → iron → parts (582 hours)

---

## Recommended Starting Configurations

### Minimal Viable Simulation
**Goal**: Test a single recipe
**Initial imports**:
- `labor_bot_general_v0` × 1
- Recipe inputs (from recipe YAML)

### Standard Manufacturing Test
**Goal**: Build a machine from parts
**Initial imports**:
- `labor_bot_general_v0` × 1
- All BOM components
- Common consumables: `fastener_kit_medium`, `aluminum_alloy_ingot`

### Bootstrap Simulation
**Goal**: Demonstrate self-sufficiency from regolith
**Initial imports**:
- `labor_bot_general_v0` × 1
- Critical machines: `press_brake_v0`, `stamping_press_basic`, etc.
- Minimal consumables for first-generation parts

---

## Future Improvements

Based on simulation analysis, these are high-priority improvements:

1. **Aluminum production chain**: Tested iron extensively, but aluminum (from anorthite) less tested
2. **Parallel processing**: Most simulations run processes sequentially; test parallel execution
3. **Machine building**: Only `labor_bot_general_v0` built in simulations; test building other machines
4. **Waste/byproduct tracking**: Tailings accumulate but aren't reused; test recycling processes
5. **Energy modeling**: No power consumption tracked yet; add power budget constraints

---

## Quick Tips for New Simulations

1. **Always start with** `init_simulation("descriptive_name")`
2. **Name your simulation** descriptively (e.g., `motor_assembly_test_dec21` not `test_sim_5`)
3. **Import in bulk** before starting recipes (reduces events)
4. **Check inventory** with `view_state()` after each major milestone
5. **Use advance_time()** to fast-forward through long processes
6. **Calculate total materials** needed before importing (avoid shortages)
7. **Test recipes individually** before chaining them together
8. **Document intent** in simulation name and initial comments

---

## Appendix: Simulation Replay

To replay/analyze an existing simulation:

```bash
# View simulation summary
python tools/analyze_simulations.py claude_base_001

# Generate full report for all simulations
python tools/analyze_simulations.py

# View simulation events
cat simulations/claude_base_001/simulation.jsonl | python -m json.tool
```

---

## Related Documentation

- `base_builder/INTERACTIVE_MODE.md` - How to use interactive simulation
- `docs/labor_bot_design_memo.md` - Labor bot specifications
- `docs/parts_and_labor_guidelines.md` - Parts, BOMs, and labor modeling policy
- `docs/simulation_learnings.md` - Auto-generated analysis report (detailed)
