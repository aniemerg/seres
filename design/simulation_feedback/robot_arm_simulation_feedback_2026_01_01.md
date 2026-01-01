# Robot Arm Simulation Feedback - 2026-01-01

## Simulation Summary

**Goal**: Create a robot arm component from lunar in-situ resources (ISRU) to test the simulation CLI tools and debug the process.

**Simulation ID**: `robot_arm_link_isru`

**Result**: ✅ **SUCCESS** - Created 1 unit of `robot_arm_link_aluminum` using 2/3 locally-sourced aluminum from regolith mining

**Production Chain Tested**:
```
regolith_lunar_highlands (100 kg, mined locally)
  + hydrochloric_acid (10 kg, imported)
  → alumina_powder (12 kg)
    + carbon_anode (0.5 kg/kg, imported)
    + cryolite_flux (0.15 kg/kg, imported)
    → aluminum_alloy_ingot (6 kg locally-produced + 3 kg imported)
      → robot_arm_link_aluminum (1 unit)
```

**Time**: 19 hours total
**Energy**: 181.1 kWh
**ISRU Ratio**: ~67% (6 kg of 9 kg aluminum from local materials)

---

## CLI Tools Testing Results

### ✅ What Worked Well

1. **`sim scaffold` command** - EXCELLENT
   - Creates simulation and imports bootstrap items in one step
   - Clean syntax: `--bootstrap item_id:qty:unit,item_id2:qty:unit`
   - Saves time vs. separate init + multiple import commands
   - Output is clear and informative

2. **`sim import` command** - WORKS WELL
   - Straightforward syntax
   - Good feedback messages
   - Properly tracks imports separately from local production

3. **`sim preview` command** - VERY USEFUL
   - Non-destructive way to see what will happen
   - Shows exactly what outputs you'll get
   - Essential for planning multi-step operations

4. **`sim advance-time` command** - WORKS WELL
   - Clear output showing completed processes
   - Energy calculation working correctly
   - Shows all outputs produced

5. **`sim view-state` command** - GOOD
   - Comprehensive view of simulation state
   - Separates imports from local production
   - Shows active processes clearly

6. **Resource tracking and validation**
   - Correctly caught insufficient materials error
   - Proper inventory management (consumes inputs, adds outputs)
   - Material balance appears correct

---

## 🐛 Bugs and Issues Found

### 1. **CRITICAL: `sim plan` doesn't help with ISRU decisions**

**Problem**: The `sim plan` command for recipes only shows immediate machine/resource requirements, not the full dependency tree or what can be made locally vs. imported.

**Example**:
```bash
$ python -m src.cli sim plan --recipe recipe_robot_arm_6dof_v0
=== Plan: recipe recipe_robot_arm_6dof_v0 ===
Required machines/resources:
  assembly_station: 1 unit
  assembly_tools_basic: 1 unit
  cutting_tools_general: 1 unit
  labor_bot_general_v0: 1.0 hr
  milling_machine_general_v0: 1 unit
Inputs: none specified (recipe uses step processes)
```

**What's missing**:
- No dependency tree showing what inputs are needed
- No indication of what can be made from local materials
- No path from raw materials (regolith) to final product
- Doesn't help answer: "Can I make this on the Moon?"

**User's Question**: "It doesn't seem like sim plan actually helped with that?"
**Answer**: Correct! It didn't help at all for ISRU planning.

**Recommendation**:
Add a `--show-dependencies` or `--isru-analysis` flag that:
- Traces back through all recipe inputs
- Shows full material tree
- Marks items as:
  - ✓ Locally available (raw materials like regolith)
  - ✓ Has recipe (can be manufactured)
  - ⚠️  Import required (no recipe available)
  - 📊 ISRU % estimate

**Example desired output**:
```
=== ISRU Analysis: recipe_robot_arm_link_aluminum_v0 ===

Dependency Tree:
robot_arm_link_aluminum (1 unit)
├─ aluminum_alloy_ingot: 9.00 kg ✓ CAN MAKE
│  ├─ alumina_powder: 18.00 kg ✓ CAN MAKE
│  │  ├─ regolith_lunar_highlands: 150.00 kg ✓ LOCAL RESOURCE
│  │  └─ hydrochloric_acid: 15.00 kg ⚠️  IMPORT REQUIRED
│  ├─ carbon_anode: 4.50 kg ⚠️  IMPORT REQUIRED
│  └─ cryolite_flux: 1.35 kg ⚠️  IMPORT REQUIRED
└─ [manufacturing processes...]

ISRU Summary:
- Local materials: ~150 kg regolith
- Required imports: ~21 kg chemicals
- Estimated ISRU %: ~88% by mass (assuming regolith is mined)
- Blocking imports: hydrochloric_acid, carbon_anode, cryolite_flux
```

---

### 2. **BUG: Auto-duration calculation doesn't work**

**Problem**: Process has a valid `time_model` with all required fields, `sim plan` says "Duration calculation: ok", but `start-process` fails with "Must provide either duration_hours or (output_quantity + output_unit)".

**Steps to reproduce**:
```bash
$ python -m src.cli sim plan --process regolith_mining_highlands_v0
=== Plan: process regolith_mining_highlands_v0 ===
Required machines/resources:
  labor_bot_general_v0: 8.0 hr
Inputs: none
Outputs:
  regolith_lunar_highlands: 100.00 kg
Duration calculation: ok  # <-- Says it's OK!
Energy calculation: ok

$ python -m src.cli sim start-process --sim-id test --process regolith_mining_highlands_v0
✗ Failed to start process: Must provide either duration_hours or (output_quantity + output_unit)
# <-- But it fails!
```

**Process definition** (has valid time_model):
```yaml
id: regolith_mining_highlands_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 12.5
  rate_unit: kg/hr
  scaling_basis: regolith_lunar_highlands
outputs:
  - item_id: regolith_lunar_highlands
    qty: 100.0
    unit: kg
```

**Expected behavior**: Engine should calculate duration as `100 kg / 12.5 kg/hr = 8 hours`

**Workaround**: Manually provide `--duration 8`

**Recommendation**:
- Fix duration calculation for continuous processes with outputs
- OR improve error message to explain WHY it can't calculate
- OR make `sim plan` actually test the calculation instead of just checking if fields exist

---

### 3. **CONFUSING: Recipe output messages are misleading**

**Problem**: When starting a recipe, the output says "Steps: 0" and "Duration: 0.00 hours" even though it clearly has a duration (ends_at > current time).

**Example**:
```bash
$ python -m src.cli sim run-recipe --sim-id test --recipe recipe_alumina_powder_v0 --quantity 1
✓ Started recipe 'recipe_alumina_powder_v0' (quantity: 1)
  Steps: 0          # <-- Says 0 steps?
  Duration: 0.00 hours  # <-- Says 0 duration?
  Ends at: 9.00 hours   # <-- But it clearly runs for 1 hour! (current time was 8.00)
```

**Recipe definition** (has 1 step):
```yaml
id: recipe_alumina_powder_v0
steps:
  - process_id: alumina_extraction_from_highlands_v0
    est_time_hr: 10.0
```

**Impact**: Confusing for users - makes it look like the recipe is broken or didn't work.

**Recommendation**:
- Show actual number of steps from recipe
- Show actual calculated/estimated duration
- OR if steps/duration can't be determined, say "N/A" instead of "0"

---

### 4. **INCONSISTENCY: `sim plan` for process vs. recipe**

**Problem**: `sim plan` output quality differs significantly between processes and recipes.

**Process plan** (GOOD):
```
=== Plan: process regolith_mining_highlands_v0 ===
Required machines/resources:
  labor_bot_general_v0: 8.0 hr
Inputs: none
Outputs:
  regolith_lunar_highlands: 100.00 kg
Duration calculation: ok
Energy calculation: ok
```

**Recipe plan** (LESS USEFUL):
```
=== Plan: recipe recipe_robot_arm_6dof_v0 ===
Required machines/resources:
  assembly_station: 1 unit
  ...
Inputs: none specified (recipe uses step processes)
Duration/Energy calculation: not evaluated for recipes (step overrides possible)
```

**Why is recipe plan less useful?**
- Doesn't show recipe-level inputs even when defined
- Doesn't attempt to calculate duration/energy
- Doesn't show step count or step details

**Recommendation**:
- For recipes with defined inputs/outputs, show them
- Calculate total duration by summing step durations
- Show step count and brief step summary
- Show total energy estimate

---

## 💡 Feature Requests

### 1. **Add `sim plan --full-chain` flag**

Show the complete production chain from raw materials to final product, including all intermediate steps.

**Example**:
```bash
$ python -m src.cli sim plan --recipe recipe_robot_arm_link_aluminum_v0 --full-chain

=== Full Production Chain ===

Step 1: Mine regolith
  Process: regolith_mining_highlands_v0
  Output: 100 kg regolith_lunar_highlands
  Time: 8 hours | Energy: 50 kWh

Step 2: Extract alumina
  Recipe: recipe_alumina_powder_v0
  Input: 100 kg regolith + 10 kg HCl
  Output: 12 kg alumina_powder
  Time: 10 hours | Energy: 36 kWh

Step 3: Smelt aluminum (x6 batches)
  Recipe: recipe_aluminum_alloy_ingot_v0
  Input: 12 kg alumina + 3 kg carbon + 0.9 kg flux
  Output: 6 kg aluminum
  Time: 6 hours | Energy: 90 kWh

Step 4: Fabricate arm link
  Recipe: recipe_robot_arm_link_aluminum_v0
  Input: 9 kg aluminum
  Output: 1 unit robot_arm_link_aluminum
  Time: 1 hour | Energy: 5 kWh

TOTALS:
  Time: ~25 hours
  Energy: 181 kWh
  Required imports: 13 kg chemicals
  Local resources: 100 kg regolith
```

### 2. **Add `sim estimate` command**

Calculate material requirements and time/energy before starting simulation.

**Example**:
```bash
$ python -m src.cli sim estimate --goal robot_arm_link_aluminum:1 --isru-mode

=== Production Estimate ===

Goal: 1 unit robot_arm_link_aluminum

Required inputs:
  From local resources (mining):
    - regolith_lunar_highlands: 150 kg (12 hours mining)

  Required imports:
    - hydrochloric_acid: 15 kg
    - carbon_anode: 4.5 kg
    - cryolite_flux: 1.35 kg
    - Processing machines: 4 units
    - Tools: 3 sets

  Estimated totals:
    - Time: 25-30 hours
    - Energy: 180-200 kWh
    - Import mass: ~21 kg + machines

  ISRU ratio: 88% by mass
```

### 3. **Add `sim batch` command**

Run multiple recipes in sequence from a script file.

**Example**:
```yaml
# production_plan.yaml
simulation_id: robot_arm_batch
steps:
  - action: mine
    process: regolith_mining_highlands_v0
    duration: 8
  - action: recipe
    recipe: recipe_alumina_powder_v0
    quantity: 1
  - action: recipe
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 6
  - action: recipe
    recipe: recipe_robot_arm_link_aluminum_v0
    quantity: 1
```

```bash
$ python -m src.cli sim batch --plan production_plan.yaml
```

### 4. **Add `sim replay` command**

Replay a simulation from its JSONL log for debugging or presentation.

### 5. **Improve `sim view-state` grouping**

Group inventory by category:
- Raw materials
- Intermediate products
- Final products
- Machines/Tools
- Byproducts

---

## 🎯 Answers to User's Questions

### 1. "It's kind of important that we try to make the robot out of local in situ resources"

**Response**: Absolutely correct! This simulation successfully demonstrated:
- Mining local regolith (100 kg)
- Processing to alumina (12 kg)
- Smelting to aluminum (6 kg locally-produced)
- Fabricating robot arm component (67% local content)

**What we still need to import**:
- Chemicals: HCl, carbon anodes, cryolite (can't make these yet on the Moon)
- Processing machines (but these are reusable capital equipment)

**What we proved we CAN make locally**:
- Aluminum metal from regolith (the bulk material for the robot arm)
- The fabricated component itself

### 2. "It doesn't seem like sim plan actually helped with that?"

**Response**: You're 100% right. The `sim plan` command in its current form:
- ✅ Shows immediate machine requirements (helpful)
- ✅ Shows direct inputs for processes (helpful)
- ❌ Doesn't show dependency trees (not helpful)
- ❌ Doesn't distinguish local vs. import materials (not helpful for ISRU)
- ❌ Doesn't help answer "can I make this on the Moon?" (the key question!)

**What I had to do instead**:
1. Manually read recipe files
2. Manually trace dependencies (alumina ← regolith)
3. Manually search for intermediate recipes
4. Trial and error to figure out what to import

**This should be automated!** See recommendations above.

---

## 📊 Simulation Statistics

**Resources Imported** (bootstrap):
- labor_bot_general_v0: 3 units
- hydrochloric_acid: 10 kg
- carbon_anode: 5 kg
- cryolite_flux: 1 kg
- aluminum_alloy_ingot: 3 kg (supplemental)
- Machines: 4 units (chemical_reactor, electrolysis_cell, casting_furnace, milling_machine)
- Tools: 3 sets
- **Total import mass**: ~22 kg + machines

**Local Production**:
- regolith_lunar_highlands: 100 kg (mined)
- alumina_powder: 12 kg (processed)
- aluminum_alloy_ingot: 6 kg (smelted)
- robot_arm_link_aluminum: 1 unit (fabricated)

**Time Breakdown**:
- Mining: 8 hours
- Alumina extraction: 1 hour (actual recipe time)
- Aluminum smelting: 6 hours
- Arm link fabrication: 1 hour
- Idle time: 3 hours
- **Total**: 19 hours

**Energy**:
- Mining: 50 kWh
- Processing: 131.1 kWh
- **Total**: 181.1 kWh

---

## 🔄 Recommendations Summary

**High Priority**:
1. Fix auto-duration calculation or improve error messages
2. Add ISRU dependency analysis to `sim plan`
3. Fix misleading recipe output messages

**Medium Priority**:
4. Add `sim estimate` command for planning
5. Add `sim plan --full-chain` for complete production chains
6. Improve consistency between process and recipe planning

**Nice to Have**:
7. Add `sim batch` for scripted multi-step production
8. Add `sim replay` for debugging
9. Improve `sim view-state` grouping

---

## ✅ Overall Assessment

**Simulation Engine**: Solid and working well!
- Material tracking is correct
- Energy calculations work
- Time advancement works
- Validation catches errors appropriately

**CLI Tools**: Good foundation, needs polish
- Core commands work well
- Planning tools need significant improvement for ISRU workflows
- Some confusing messages and inconsistencies
- Missing convenience features for complex simulations

**For ISRU modeling**: Additional tooling needed
- Current tools don't help answer "can I make this locally?"
- Manual dependency tracing is tedious and error-prone
- Need better support for planning from raw materials to final product

**Rating**: 7/10
- Would be 9/10 with ISRU planning features
- Would be 10/10 with all recommended features

---

## 📝 Notes

- The simulation successfully demonstrated a realistic ISRU production chain
- The engine correctly handles multi-step recipes and material flow
- The main gap is in planning/analysis tools, not the core simulation
- These issues would be especially noticeable for users new to the KB who don't know what recipes exist or how they connect

**Test environment**:
- Date: 2026-01-01
- Model: Claude Sonnet 4.5
- KB state: Current (with ADR-012/014/017 schemas)
