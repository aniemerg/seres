# Fixing Template Validation Errors

**Audience:** AI agents and human developers working on recipe fixes
**Context:** 4,609 validation errors related to template processes
**Goal:** Fix recipes so they properly specify inputs for template processes

---

## Table of Contents

1. [Understanding Template Errors](#understanding-template-errors)
2. [Workflow](#workflow)
3. [Using Intelligence Files](#using-intelligence-files)
4. [Decision-Making Guide](#decision-making-guide)
5. [Common Patterns](#common-patterns)
6. [Examples](#examples)
7. [Validation](#validation)

---

## Understanding Template Errors

### What Are Template Processes?

Template processes are generic process definitions marked with `is_template: true`. They have **placeholder inputs** that must be replaced in recipes.

**Example template process:**
```yaml
id: assembly_basic_v0
is_template: true
inputs:
- item_id: assembly_components  # ← Placeholder, not a real item
  qty: 1.0
  unit: kg
```

This says: "I assemble *something* from *some components*" - the recipe must specify what.

### Why Templates Exist

Templates enable **process reuse** across many products:
- One `assembly_basic_v0` process for hundreds of different assemblies
- Each recipe specifies exact components via step-level input overrides
- Alternative would need thousands of specific processes (unmaintainable)

### The Two Error Types

#### Error 1: Missing Step-Level Inputs

**Rule:** `recipe_template_missing_step_inputs`

**Problem:** Recipe uses template process but doesn't provide step-level inputs.

```yaml
steps:
- process_id: assembly_basic_v0  # Template
  # NO inputs field - falls back to placeholder 'assembly_components'
```

**Fix:** Add `inputs:` field with specific items.

#### Error 2: Invalid Step Inputs

**Rule:** `recipe_step_input_not_satisfied`

**Problem:** Step HAS inputs, but they reference items that don't exist or aren't available.

```yaml
steps:
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_plate_or_sheet  # ← Generic placeholder, not real item
    qty: 0.2
    unit: kg
```

**Fix:** Replace with specific item (e.g., `steel_plate_3mm`).

---

## Workflow

### Step 1: Get Work from Queue

```bash
python -m src.cli queue get
```

Returns a work item like:
```
Task: Fix recipe_pump_v0 (validation error: recipe_template_missing_step_inputs)
File: kb/recipes/recipe_pump_v0.yaml
Priority: 100
```

### Step 2: Read Intelligence File

```bash
cat out/template_fixes/recipe_pump_v0.md
```

The intelligence file contains:
- ✅ All file paths (recipe, BOM, processes, items)
- ✅ Error details with step locations
- ✅ Fix suggestions (BOM components, previous outputs, similar recipes)
- ✅ Current YAML showing the problem

### Step 3: Review and Decide

Read the suggestions and **apply judgment**:
- Does this make sense for what the process does?
- Are the quantities appropriate?
- Should ALL suggested items be used, or just some?

### Step 4: Edit Recipe

Use standard editing tools to modify the recipe YAML:
- Add `inputs:` field to the step
- Specify concrete item IDs (not placeholders)
- Set appropriate quantities and units

### Step 5: Validate (Optional)

Re-run validation to verify fix:
```bash
python -m src.cli index
```

Or move to next task and let CI catch any remaining issues.

---

## Using Intelligence Files

### File Structure

Each intelligence file has:

**1. Files Section**
```markdown
## Files
- Recipe: `kb/recipes/recipe_pump_v0.yaml`
- BOM: `kb/boms/bom_pump_v0.yaml` ✓ (3 components)
- Target: `kb/items/pump_v0.yaml`
```

**2. Similar Recipes Section** (if found)
```markdown
## Similar Recipes
- `recipe_pump_v1` → pump_v1 (5 steps)
```

**3. Errors Section** (one per error)
```markdown
### Error 1: Step 1 missing inputs

**Location:** Step 1
**Process:** `assembly_basic_v0` (TEMPLATE)
**Problem:** No step-level inputs

**Option A: Use BOM components**
- aluminum_housing (2.0 kg)
- steel_impeller (1.0 kg)

**Option B: Use previous step output**
- machined_pump_body (1.0 unit)
```

### How to Use Each Section

**Files:** Use these paths when editing - no need to search
**Similar Recipes:** Check how other recipes solved the same problem
**Options:** Consider all, choose the one that makes most sense

---

## Decision-Making Guide

### Question 1: Should I use BOM components?

**Use BOM when:**
- ✅ Step is assembly/integration of final product
- ✅ Recipe has a BOM with relevant components
- ✅ Process needs multiple discrete parts (assembly, wiring, etc.)

**Example:** Assembling a pump from housing + impeller + seal

**Don't use BOM when:**
- ❌ Step is fabrication of raw materials (welding, casting, machining)
- ❌ BOM contains accessories not used in THIS step
- ❌ Process operates on ONE thing (coating, heat treatment, inspection)

**Example:** Welding needs raw steel, not finished components from BOM

### Question 2: Should I use previous step output?

**Use previous output when:**
- ✅ Steps are sequential processing (fabricate → coat → inspect)
- ✅ Previous step produces what this step needs
- ✅ Process operates on output from earlier processing

**Example:** Coating the welded assembly from previous step

**Don't use previous output when:**
- ❌ Previous output is wrong type for this step
- ❌ Step needs additional materials beyond previous output
- ❌ No previous steps exist (step 0)

### Question 3: Should I use ALL suggested items or just some?

**Use ALL items when:**
- ✅ Process is assembly of complete unit
- ✅ Process is final test/calibration of finished product
- ✅ All items are structural/functional components

**Use SUBSET when:**
- ✅ Process only needs specific materials (welding → metals only)
- ✅ BOM includes accessories added in later steps
- ✅ Process operates on 1-2 items, not everything

**Example:** Welding step in reactor recipe:
- BOM has 7 items (vessel, lining, valves, sensors, mixer)
- Only use vessel for welding
- Other items added in later assembly steps

### Question 4: What if suggestions don't make sense?

**Alternative approaches:**

1. **Check similar recipes** (if listed in intelligence file)
   - How did other recipes handle the same process?
   - Copy their pattern if it makes sense

2. **Check process file** (path in intelligence file)
   - Read process inputs/outputs
   - Understand what the process actually does

3. **Look for intermediate outputs**
   - Maybe an earlier step should produce what you need
   - Consider if recipe structure needs changes

4. **Flag for human review** if truly stuck

---

## Common Patterns

### Pattern 1: Final Assembly/Test Steps

**Scenario:** Recipe ends with assembly/calibration/test of final product

**Typical processes:**
- `assembly_basic_v0`
- `integration_test_basic_v0`
- `calibration_and_test_basic_v0`

**Best fix:** Use previous step output (the assembled/processed product)

**Example:**
```yaml
# Step 0: Assembly
- process_id: assembly_basic_v0
  inputs:  # Use BOM components
  - item_id: pump_housing
  - item_id: pump_impeller
  - item_id: pump_seal
  outputs:
  - item_id: pump_v0

# Step 1: Calibration
- process_id: calibration_and_test_basic_v0
  inputs:  # Use previous output
  - item_id: pump_v0  # ← From step 0
```

### Pattern 2: Sequential Processing Chain

**Scenario:** Part goes through multiple processing steps

**Typical sequences:**
- Cut → Weld → Grind → Heat-treat → Coat → Inspect
- Cast → Machine → Polish → Anodize → Test

**Best fix:** Each step uses output from previous step

**Example:**
```yaml
# Step 0: Welding
- process_id: welding_basic_v0
  inputs:
  - item_id: steel_plate_3mm
  outputs:
  - item_id: welded_assembly

# Step 1: Grinding
- process_id: grinding_basic_v0
  inputs:
  - item_id: welded_assembly  # ← From step 0

# Step 2: Coating
- process_id: coating_basic_v0
  inputs:
  - item_id: welded_assembly  # ← Same item, now ground
```

### Pattern 3: Fabrication from Raw Materials

**Scenario:** Early steps fabricate components from raw materials

**Typical processes:**
- `welding_and_fabrication_v0`
- `metal_casting_basic_v0`
- `machining_basic_v0`

**Best fix:** Use raw material inputs (often NOT in BOM)

**Common mistake:** BOM lists finished components, but fabrication needs raw stock

**Example:**
```yaml
# WRONG: BOM has finished components
- process_id: welding_and_fabrication_v0
  inputs:
  - item_id: reactor_agitator_mixer_v0  # ← Can't weld a mixer!
  - item_id: thermocouple_type_s_v0     # ← Can't weld a sensor!

# RIGHT: Use raw materials
- process_id: welding_and_fabrication_v0
  inputs:
  - item_id: stainless_steel_plate_6mm
    qty: 50.0
    unit: kg
```

**Solution:** Check if recipe needs earlier sourcing steps or different inputs.

### Pattern 4: Generic Placeholder Replacement

**Scenario:** Step has inputs but uses generic "or" patterns

**Typical placeholders:**
- `steel_plate_or_sheet`
- `powder_metal_or_ceramic`
- `bulk_material_or_parts`

**Best fix:** Replace with specific item from catalog

**Intelligence file shows:** Specific items matching pattern

**Example:**
```yaml
# BEFORE (generic)
inputs:
- item_id: steel_plate_or_sheet  # ← Not a real item

# AFTER (specific)
inputs:
- item_id: steel_plate_3mm  # ← Real item from catalog
```

### Pattern 5: Multi-Component Assembly

**Scenario:** Assembly requires subset of BOM items

**Typical processes:**
- `assembly_basic_v0` (when step is intermediate, not final)
- `electrical_assembly_basic_v0`

**Best fix:** Select relevant BOM items for THIS step

**Example:**
```yaml
# Recipe makes: acid_reactor_v0
# BOM has: vessel, lining, mixer, valves, sensors, heater

# Step 1: Assemble mechanical components
- process_id: assembly_basic_v0
  inputs:  # Select mechanical items only
  - item_id: reactor_vessel
  - item_id: mixer_assembly
  - item_id: mounting_brackets

# Step 2: Install instrumentation (later)
- process_id: electrical_assembly_basic_v0
  inputs:  # Select electrical items
  - item_id: thermocouple_set
  - item_id: pressure_sensor
```

---

## Examples

### Example 1: Pump Calibration (Simple)

**Intelligence file says:**
```markdown
### Error: Step 1 missing inputs

**Process:** `calibration_and_test_basic_v0` (TEMPLATE)

**Option A: BOM components (5 items)**
- pump_housing, pump_impeller, pump_seal, pump_bearings, pump_shaft

**Option B: Previous output**
- pump_v0 (from step 0)
```

**Analysis:**
- Calibration tests the ASSEMBLED pump, not individual parts
- Previous step assembled the pump
- **Use Option B**

**Fix:**
```yaml
- process_id: calibration_and_test_basic_v0
  inputs:
  - item_id: pump_v0
    qty: 1.0
    unit: unit
```

### Example 2: Reactor Welding (Complex)

**Intelligence file says:**
```markdown
### Error: Step 0 missing inputs

**Process:** `welding_and_fabrication_v0` (TEMPLATE)
**Notes:** "Fabricate stainless steel vessel"

**Option A: BOM components (7 items)**
- chemical_reactor_vessel_v0, acid_resistant_lining,
  reactor_agitator_mixer_v0, valve_set, thermocouple_set
```

**Analysis:**
- Notes say "fabricate vessel" - need to MAKE it, not assemble it
- BOM lists finished components (mixer, valves) - can't weld those!
- Need raw stainless steel, not finished vessel
- **Don't use BOM** - need different inputs

**Fix:**
```yaml
- process_id: welding_and_fabrication_v0
  inputs:
  - item_id: stainless_steel_plate_6mm
    qty: 50.0
    unit: kg
  - item_id: stainless_steel_pipe_50mm
    qty: 10.0
    unit: m
  outputs:
  - item_id: reactor_vessel_welded
    qty: 1.0
    unit: unit
```

### Example 3: Generic Replacement

**Intelligence file says:**
```markdown
### Error: Step 0 has invalid input

**Current input:** `steel_plate_or_sheet` (not a real item)

**Specific items matching pattern:**
- steel_plate_3mm (IN BOM: 5.0 kg)
- steel_plate_6mm
- steel_sheet_18ga
```

**Analysis:**
- `steel_plate_or_sheet` is placeholder
- BOM has `steel_plate_3mm` with exact quantity needed
- **Use BOM match**

**Fix:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_plate_3mm  # ← Replaced placeholder
    qty: 5.0
    unit: kg
```

### Example 4: Sequential Processing

**Intelligence file shows:**
```markdown
Step 0: welding_basic_v0 → produces welded_assembly
Step 1: grinding_basic_v0 → needs inputs (MISSING)
Step 2: coating_basic_v0 → needs inputs (MISSING)
```

**Analysis:**
- Steps are sequential: weld → grind → coat
- Each step processes output from previous
- **Chain them together**

**Fix:**
```yaml
steps:
- process_id: welding_basic_v0
  inputs:
  - item_id: steel_parts_cut
  outputs:
  - item_id: welded_assembly

- process_id: grinding_basic_v0
  inputs:
  - item_id: welded_assembly  # ← From step 0
  outputs:
  - item_id: welded_assembly  # ← Same item, now ground

- process_id: coating_basic_v0
  inputs:
  - item_id: welded_assembly  # ← From step 1
  outputs:
  - item_id: coated_assembly
```

---

## Validation

### After Fixing

You can optionally re-run validation:

```bash
python -m src.cli index
```

Then check for that recipe:
```bash
grep recipe_pump_v0 out/validation_issues.jsonl
```

If no output, the recipe now validates!

### Common New Errors After Fixing

**"Item X not found"**
- You specified an item that doesn't exist in KB
- Check item catalog or use different item

**"Output Y doesn't match process capabilities"**
- Process can't produce the output you specified
- Check process file for allowed outputs

**"Circular dependency"**
- Step N needs output from step M, but M > N
- Reorder steps or fix dependency

---

## Tips and Best Practices

### DO:
- ✅ Read the intelligence file completely before deciding
- ✅ Check process notes for hints about intent
- ✅ Consider what the process actually DOES physically
- ✅ Use specific item IDs, not placeholders
- ✅ Set reasonable quantities based on BOM or similar recipes
- ✅ Chain sequential processing steps together

### DON'T:
- ❌ Blindly use ALL BOM components for every step
- ❌ Add items that can't be processed by that process type
  (e.g., sensors in welding, liquids in grinding)
- ❌ Use placeholders as inputs (steel_or_aluminum, bulk_material, etc.)
- ❌ Ignore process notes that explain intent
- ❌ Add components that should come from later steps

### When in Doubt:
- 📖 Check similar recipes in intelligence file
- 📖 Read the process file to understand what it does
- 📖 Look at recipe structure - does it make logical sense?
- 📖 Conservative is better - if unsure, ask for review

---

## Getting Help

### If Intelligence File is Unhelpful

The intelligence file might not have good suggestions if:
- Recipe has no BOM
- No similar recipes exist
- Process is unusual/specialized

**What to do:**
1. Check the process file directly (`kb/processes/<process_id>.yaml`)
2. Search for other recipes using the same process
3. Review recipe structure for logical flow
4. Flag for human review if genuinely unclear

### If Recipe Seems Fundamentally Broken

Some recipes may need more than input fixes:
- Missing steps (need to add fabrication before assembly)
- Wrong process selection (should use different process)
- BOM is incomplete (missing raw materials)

**What to do:**
1. Note the structural issue
2. Fix what you can (add inputs where obvious)
3. Add comment in recipe noting deeper issues
4. Flag for human review

---

## Summary

**The Goal:** Recipes must specify concrete inputs for template processes

**The Process:**
1. Get work from queue
2. Read intelligence file
3. Apply judgment to suggestions
4. Edit recipe with specific inputs
5. Move to next task

**The Key:** Think about what the process DOES, not just what validates

**Remember:** Validation passing doesn't mean the fix is correct - use semantic reasoning!

---

## Related Documentation

- [ADR-013: Recipe Override Mechanics](../design/adr-013-recipe-override-mechanics.md)
- [ADR-017: Validation System](../design/adr-017-validation-system.md)
- [Template Process Mechanism Explained](../design/template-process-mechanism-explained.md)
- [Work Queue System](./work-queue.md)
