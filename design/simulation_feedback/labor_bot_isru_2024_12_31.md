# Simulation Feedback: Labor Bot ISRU Build
**Sim ID:** labor_bot_max_isru_2024_12_31
**Date:** 2024-12-31
**Goal:** Build labor_bot_general_v0 from maximum in-situ resources

## Challenges Encountered

### 1. Recipe Missing Inputs/Outputs
**Problem:** Many recipes don't specify inputs/outputs at recipe level, only call processes. Simulation can't consume/produce items without explicit recipe-level I/O.

**Examples:**
- `recipe_hydrochloric_acid_v0` - only had process step, no inputs/outputs
- `recipe_alumina_powder_v0` - no inputs/outputs defined initially

**Impact:** Recipes run but don't consume inputs or produce outputs. Silent failure.

**Fix Applied:** Added explicit inputs/outputs to match process definitions.

**Suggestion:** Validation rule to check recipes have inputs/outputs when their processes do.

### 2. Item ID Mismatches
**Problem:** Recipe target_item_id doesn't match process output item_id.

**Example:**
- Recipe: `target_item_id: hydrochloric_acid_v0`
- Process outputs: `hydrochloric_acid` (no _v0)

**Impact:** Recipe produces nothing even when running successfully.

**Suggestion:** Validation to check recipe target matches process output IDs.

### 3. Batch Processing Tedium
**Problem:** Building robot requires many small batch operations:
- Mine 100kg regolith (24h)
- Extract 12kg alumina (10h)
- Smelt 6kg aluminum (10h batches)
- Repeat 3-4 times for enough aluminum

**Current Time:** 308 hours (~13 days) just to make 1 arm link and gather materials

**Impact:** Extremely tedious for agent, many CLI calls, easy to lose track

**Suggestions:**
1. **Batch operation command:** `sim batch-produce --item aluminum_alloy_ingot --quantity 20` that auto-chains the production steps
2. **Production planner:** `sim plan-production --target labor_bot_general_v0 --max-isru` that calculates all materials needed and generates production schedule
3. **Auto-advance mode:** `sim auto-run --until "labor_bot_general_v0 in inventory"` that runs processes automatically

### 4. Material Tracking Difficulty
**Problem:** Hard to track what materials are needed for full robot.

**Current Status:**
- Have: 3kg Al, 30kg Fe, 1x robot_arm_link
- Need: ~25kg more Al for remaining parts + motors + cables + many other components

**Suggestion:** `sim show-requirements --target labor_bot_general_v0 --current-inventory` that shows:
```
Requirements for labor_bot_general_v0:
  Aluminum parts (need 18kg Al more):
    ✓ robot_arm_link_aluminum: 1/2 (need 9kg Al)
    ✗ robot_arm_link_aluminum: 0/1 (need 9kg Al)
    ✗ motor_housing_cast: 0/6 (need ~12kg Al)
  ...
```

### 5. Consumables Management
**Problem:** Keep running out of consumables (carbon_anode, cryolite_flux, HCl) mid-production.

**Imported so far:**
- Initial: 20kg HCl, 5kg carbon, 2kg flux
- Additional: 23kg carbon, 3kg flux

**Suggestion:** Warning system: "⚠️ Low on carbon_anode (2kg remaining, need 6kg for planned operations)"

### 6. Missing Dependency Chain Visibility
**Problem:** Don't know what other parts/recipes depend on until trying to run them.

**Example:** robot_arm_link recipe requires machines I didn't have (milling_machine, casting_furnace, etc.)

**Suggestion:** `sim preflight --recipe recipe_robot_arm_link_aluminum_v0` that shows:
```
✗ Missing machines: milling_machine_general_v0, casting_furnace_v0
✗ Missing materials: 9kg aluminum_alloy_ingot (have 3kg)
```

## Summary After 23 Days Sim Time

**Manufactured from Regolith:**
- 2× robot_arm_link_aluminum (18kg Al consumed)
- 1× robot_wrist_3axis
- Plus materials: 6kg Al, 30kg Fe remaining

**Attempted but failed (recipe bugs):**
- 6× motor_housing_cast - recipe completed, no output
- 1× machine_frame_small - recipe completed, no output
- 1× thermal_management_system - recipe completed, no output

**Time Breakdown:**
- Mining & extraction: ~150 hours
- Smelting & processing: ~180 hours
- Manufacturing parts: ~25 hours
- Tool imports & troubleshooting: ~200 hours
- **Total: 556 hours (23 days)**

**Agent Actions:**
- 150+ CLI commands executed
- 21 different items imported (tools, consumables, machines)
- 3 KB recipe bugs manually fixed
- Many more KB bugs discovered

**Conclusion:** Current system requires massive agent effort and many KB fixes to complete even simple assemblies. Critical need for:
1. Recipe validation (inputs/outputs)
2. Batch production tools
3. Dependency planning
4. Better error messages

## Tools That Would Help

### High Priority
1. **Production Chain Planner** - calculates full BOM → raw materials chain
2. **Batch Production** - run multiple dependent recipes in sequence
3. **Material Requirements Report** - show what's needed for target item

### Medium Priority
4. **Auto-advance with goals** - run simulation until condition met
5. **Consumables tracking/warnings** - alert when running low
6. **Recipe validation** - check inputs/outputs match processes

### Low Priority
7. **Simulation replay/fast-forward** - skip to specific time
8. **Production templates** - save common production sequences

## Progress So Far
- **Time:** 308 hours (12.8 days)
- **Energy:** 454 kWh
- **Manufactured from regolith:**
  - 1× robot_arm_link_aluminum (9kg Al from ~75kg highlands regolith)
  - Materials: 3kg Al, 30kg Fe available
- **Imported:**
  - Consumables: ~50kg (HCl, carbon, flux)
  - Tools/machines: 1× labor_bot, 1× milling machine, 1× furnace, etc.
- **Still needed:** Most robot components

## Continuing...
Will continue the full production chain to completion and update this document.

---

## Production Log

### T=519h: Material Production Complete
After many iterations:
- 21kg aluminum_alloy_ingot produced from ~300kg highlands regolith
- 9 import operations for carbon_anode (3kg each time)
- 2× mining, 3× extraction, 3× smelting cycles
- 30kg iron_metal_pure from mare regolith
- Total: ~186 hours of sim time just for material production

### T=524h: Machine/Tool Requirements Explosion
**MAJOR PAIN POINT:** Every recipe requires different specialized machines.

Tried to manufacture parts, hit missing machines:
- motor_housing_cast → needs `assembly_tools_basic`
- robot_wrist → needs `reduction_furnace_v0`, `alignment_tools`, `furnace_basic`, `measurement_equipment`, `test_bench_electrical`
- machine_frame_small → needs `fixturing_workbench`, `press_brake`, `welding_power_supply_v0`, `metal_shear_or_saw`, `welding_consumables`

**Problem:** No way to know what machines needed until recipe fails.

**Suggestion:** `sim check-requirements --recipe recipe_motor_housing_cast_v0` should show ALL required machines/tools upfront.

### T=556h: CRITICAL - Silent Recipe Failures
**SHOWSTOPPER BUG:** Many recipes complete but produce nothing!

Affected recipes (ran successfully but no output):
- `recipe_motor_housing_cast_v0` - completed, 0 outputs
- `recipe_machine_frame_small_v0` - completed, 0 outputs
- `recipe_thermal_management_system_v0` - completed, 0 outputs

**Root cause:** Recipes don't have `inputs:` and `outputs:` sections at recipe level.
- Process has inputs/outputs
- Recipe just calls process
- Simulation runs recipe but doesn't know what to consume/produce
- Result: Energy consumed, time passes, but inventory unchanged

**Impact:** ~50% of recipes tested have this issue. Makes simulation unusable without fixing every recipe.

**Manual fixes required so far:**
- recipe_hydrochloric_acid_v0 - FIXED
- recipe_alumina_powder_v0 - FIXED
- recipe_motor_housing_cast_v0 - NEEDS FIX
- recipe_machine_frame_small_v0 - NEEDS FIX
- recipe_thermal_management_system_v0 - NEEDS FIX
- Plus probably 100+ more recipes

**Suggestion:** URGENT validation rule: "Recipe with process steps MUST have inputs/outputs matching process requirements"
