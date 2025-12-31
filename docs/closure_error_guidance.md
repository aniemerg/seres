# Closure Error Resolution Guide

**Status:** Official Policy
**Version:** 1.0
**Date:** 2024-12-24
**Complements:** [Conservative Mode Guide](conservative_mode_guide.md)

## Overview

This guide provides decision trees for resolving closure analysis errors - material flow problems detected when tracing recipes and processes down to raw materials.

**Core Principle:** Closure errors indicate incomplete or inconsistent material flow definitions. Fix root causes, not symptoms.

---

## Error Types and Decision Trees

### 1. `null_quantity` (Process Inputs/Outputs with Null Quantities)

**Context:** A process has `qty: null` or `qty: 0` for an input or output, breaking material flow tracing.

**Example Error:**
```
Process 'welding_brazing_basic_v0' (in recipe 'recipe_printer_frame_v0')
input 'cast_metal_parts' has null/zero quantity
```

**Decision Tree:**

```
1. Is this a GENERIC process used by multiple recipes?
   (Check: grep "process_id.*{process_name}" kb/recipes/*.yaml)
   ├─ YES → Process should have null quantities
   │         → SOLUTION: Add explicit inputs/outputs to RECIPES that use it
   │         → See "Adding Recipe-Level Inputs" below
   └─ NO → Continue to #2

2. Is there a SIMILAR process with quantities defined?
   (Search: find kb/processes -name "*{function}*.yaml")
   ├─ YES → Copy quantity structure from similar process
   │         → Document: "Based on {similar_process_id}"
   └─ NO → Continue to #3

3. Can quantities be calculated from the TARGET ITEM?
   (If recipe produces X kg of item, inputs ≈ X kg + waste)
   ├─ YES → Calculate quantities based on:
   │         - Target item mass
   │         - Typical material waste (5-20%)
   │         - Material density conversions
   │         → Document assumptions in notes
   └─ NO → Continue to #4

4. Should this process be DELETED?
   (Is it unreferenced, redundant, or obsolete?)
   ├─ YES → Remove process, update referencing recipes
   └─ NO → Continue to #5

5. ESTIMATE quantities conservatively
   - Use 1 kg as default unit quantity
   - Assume 10% waste unless specific process indicates otherwise
   - Document: "Placeholder quantities, refine with research"
   - Add to queue for future refinement
```

**Adding Recipe-Level Inputs (for generic processes):**

```yaml
# BEFORE (generic process with null quantities)
id: recipe_frame_v0
target_item_id: frame_structural
steps:
  - process_id: welding_basic_v0  # Has null quantities

# AFTER (explicit recipe inputs)
id: recipe_frame_v0
target_item_id: frame_structural
inputs:
  - item_id: steel_tube_set
    qty: 5.0
    unit: kg
  - item_id: welding_rod
    qty: 0.5
    unit: kg
outputs:
  - item_id: frame_structural
    qty: 5.0
    unit: kg
steps:
  - process_id: welding_basic_v0
```

---

### 2. `recipe_no_inputs` (Recipes with No Material Flow)

**Context:** A recipe has steps but no material inputs are defined (not at recipe level, not in process steps).

**Example Error:**
```
Recipe 'recipe_motor_assembly_v0' for 'motor_electric_small' has no inputs
```

**Decision Tree:**

```
1. Does this recipe have EXPLICIT inputs/outputs at recipe level?
   (Check: recipe has 'inputs:' and 'outputs:' fields)
   ├─ YES → Check if inputs are empty or have null quantities
   │         → Fix quantities (see null_quantity guidance above)
   └─ NO → Continue to #2

2. Do the process steps have DEFINED inputs?
   (Check each process referenced in steps)
   ├─ YES (all processes have inputs) → Re-index, should resolve automatically
   └─ SOME/NONE → Continue to #3

3. Is there a BOM for the target item that shows components?
   (Check: grep "id.*bom_{target_item}" kb/boms/*.yaml)
   ├─ YES → Convert BOM components to recipe inputs
   │         → Add transformation processes as needed
   └─ NO → Continue to #4

4. Is there a SIMILAR RECIPE for reference?
   (Search for recipes producing similar items)
   ├─ YES → Copy input structure, adapt quantities
   │         → Document: "Based on {similar_recipe_id}"
   └─ NO → Continue to #5

5. Can inputs be INFERRED from the target item?
   ├─ YES → Create inputs based on:
   │         - Target item material_class
   │         - Target item mass
   │         - Typical process inputs for that material
   └─ NO → Continue to #6

6. Should this recipe be DELETED?
   (Is it redundant, obsolete, or import-only?)
   ├─ YES → Mark item as import or use different recipe
   └─ NO → Continue to #7

7. RESEARCH and create minimal inputs
   - Check papers: docs/papers/
   - Use Conservative Mode principles (prefer existing items)
   - Document assumptions clearly
   - Start with major components only
```

---

### 3. `recipe_not_found` (Referenced Recipe Doesn't Exist)

**Context:** An item references a recipe that doesn't exist in the KB.

**Example Error:**
```
Recipe 'recipe_special_alloy_v0' not found for item 'alloy_special_v0'
```

**Decision Tree:**

```
1. Is this a TYPO in the item's recipe field?
   (Check for similarly-named recipes)
   ├─ YES → Fix item's recipe field to point to correct recipe
   └─ NO → Continue to #2

2. Does the recipe exist under a DIFFERENT NAME?
   (Search: find kb/recipes -name "*{keyword}*.yaml")
   ├─ YES → Update item to reference correct recipe ID
   └─ NO → Continue to #3

3. Does the item NEED a recipe?
   (Is it used anywhere? Is it imported?)
   ├─ NO (unused/imported) → Remove recipe reference or mark as import
   └─ YES → Continue to #4

4. Can an EXISTING recipe be adapted?
   (Search for recipes producing similar items)
   ├─ YES → Create recipe variant or update item to use existing recipe
   └─ NO → Continue to #5

5. Should this be consolidated with an EQUIVALENT item?
   (Check Conservative Mode 5× equivalence rule)
   ├─ YES → Replace with equivalent item, delete this one
   └─ NO → Continue to #6

6. CREATE the recipe
   - Follow existing recipe patterns
   - Use Conservative Mode principles
   - Reference existing processes where possible
   - Document assumptions
```

---

### 4. `process_not_found` (Referenced Process Doesn't Exist)

**Context:** A recipe step references a process that doesn't exist in the KB.

**Example Error:**
```
Process 'special_welding_v0' referenced in recipe 'recipe_frame_v0' not found
```

**Decision Tree:**

```
1. Is this a TYPO in the recipe's process_id?
   (Check for similarly-named processes)
   ├─ YES → Fix recipe step to point to correct process
   └─ NO → Continue to #2

2. Does the process exist under a DIFFERENT NAME?
   (Search: find kb/processes -name "*{keyword}*.yaml")
   ├─ YES → Update recipe to reference correct process ID
   └─ NO → Continue to #3

3. Can an EXISTING process be used instead?
   (Search for processes with similar function)
   ├─ YES → Update recipe to use existing process
   │         → Document: "Using {process_id} for {operation}"
   └─ NO → Continue to #4

4. Can this be replaced with LABOR_BOT + TOOLS?
   (See Conservative Mode: Labor Bot Decision Guide)
   ├─ YES → Update recipe to use labor_bot_general_v0 + tool
   └─ NO → Continue to #5

5. Is this process truly UNIQUE and necessary?
   ├─ NO → Simplify recipe, use generic process
   └─ YES → Continue to #6

6. CREATE the process
   - Follow existing process patterns
   - Define inputs and outputs with quantities
   - Reference required machines/tools
   - Document assumptions
```

---

### 5. `item_not_found` (Item Referenced But Not Defined)

**Context:** A process or recipe references an item that doesn't exist in the KB.

**See:** Conservative Mode Guide - `referenced_only` decision tree

**Additional Closure-Specific Considerations:**

```
If detected through closure analysis:
1. Check WHICH MACHINE needs this item
   → High-priority machines → higher urgency to fix
   → Rarely-used machines → lower priority

2. Check QUANTITY needed
   → Large mass impact → create/define item
   → Small mass impact → consider consolidation/deletion

3. Follow standard referenced_only guidance with priority weighting
```

---

## Common Patterns and Solutions

### Pattern 1: Generic Process with Null Quantities

**Problem:** Process is reused across many recipes, can't have fixed quantities.

**Solution:** Add explicit inputs/outputs to recipes, keep process generic.

```yaml
# Process (generic, null quantities)
id: assembly_basic_v0
inputs: []  # Or inputs with qty: null
outputs: []

# Recipe (explicit inputs/outputs)
id: recipe_motor_v0
inputs:
  - item_id: motor_housing
    qty: 1
  - item_id: motor_rotor
    qty: 1
outputs:
  - item_id: motor_electric_small
    qty: 1
steps:
  - process_id: assembly_basic_v0  # Generic process
```

### Pattern 2: Process Chain with Intermediate Items

**Problem:** Recipe references items that aren't explicitly defined but are intermediate products.

**Solution:** Either:
- Define intermediate items as parts
- OR Inline the process chain and skip intermediate items

```yaml
# Option A: Define intermediate
id: recipe_wire_v0
inputs:
  - item_id: copper_rod
    qty: 1.0
outputs:
  - item_id: copper_wire
    qty: 0.95
steps:
  - process_id: wire_drawing_v0

# Option B: Inline (if intermediate not reused)
id: recipe_wire_v0
inputs:
  - item_id: copper_scrap
    qty: 1.1
outputs:
  - item_id: copper_wire
    qty: 0.95
steps:
  - process_id: copper_refining_v0  # scrap → rod (inlined)
  - process_id: wire_drawing_v0     # rod → wire
```

### Pattern 3: Mass Balance Issues

**Problem:** Recipe inputs total mass doesn't match outputs.

**Solution:** Add waste/loss items or adjust quantities.

```yaml
id: recipe_part_machined_v0
inputs:
  - item_id: steel_bar
    qty: 2.0
    unit: kg
outputs:
  - item_id: part_machined
    qty: 1.5
    unit: kg
  - item_id: metal_swarf  # Waste from machining
    qty: 0.5
    unit: kg
```

---

## Conservative Mode Integration

All closure error fixes MUST follow Conservative Mode principles:

1. **Check for equivalents** before creating new items/processes/recipes
2. **Prefer reuse** over creation
3. **Document assumptions** in notes fields
4. **Use 5× magnitude rule** for equivalence
5. **Minimize KB growth** - consolidate when possible

## Research Resources

When quantities or process details are unknown:

1. **Check existing KB patterns**
   ```bash
   grep -r "similar_process" kb/processes/
   ```

2. **Review papers directory**
   ```bash
   ls docs/papers/ | grep -i {topic}
   ```

3. **Use parts and labor guidelines**
   - Mass estimation guidelines
   - Material class system
   - Equivalence criteria

4. **Conservative estimates**
   - Heavier rather than lighter
   - More energy rather than less
   - More waste rather than less

---

## Validation

After fixing closure errors:

1. **Run indexer**
   ```bash
   python -m src.cli index
   ```

2. **Check if error resolved**
   ```bash
   grep "{item_id}" out/closure_errors.jsonl
   ```

3. **Verify material flow**
   ```bash
   .venv/bin/python -m kbtool mat-closure --machine {machine_id}
   ```

4. **Check for new gaps**
   - Expect some new gaps when filling closure errors
   - Each fix should resolve more than it creates

---

## Agent Workflow

For autonomous queue agents processing closure errors:

```
1. Lease closure error from queue
2. Read error context (machine, recipe, process, item)
3. Apply decision tree for error type
4. Make minimal necessary changes
5. Run indexer to validate
6. Check closure error resolved
7. Complete if resolved, iterate if not
```

## Questions to Ask Yourself

Before fixing a closure error, ask:

- [ ] Have I checked for existing equivalents?
- [ ] Is this error a symptom of a deeper issue?
- [ ] Am I creating new items unnecessarily?
- [ ] Are my quantity estimates conservative?
- [ ] Have I documented my assumptions?
- [ ] Does this fix follow Conservative Mode?
- [ ] Will this create circular dependencies?

---

## Examples

### Example 1: Fixing Null Quantity

**Error:**
```
Process 'welding_basic_v0' input 'metal_parts' has null quantity
```

**Investigation:**
```bash
# Check how many recipes use this process
grep "welding_basic_v0" kb/recipes/*.yaml | wc -l
# Output: 45 recipes

# This is a generic process - don't fix the process, fix recipes
```

**Fix:** Add inputs to specific recipes that use this process

### Example 2: Fixing Recipe No Inputs

**Error:**
```
Recipe 'recipe_bracket_v0' has no inputs
```

**Investigation:**
```bash
# Read the recipe
cat kb/recipes/recipe_bracket_v0.yaml
# Shows: Only has steps, no inputs

# Check if BOM exists
grep "bracket" kb/boms/*.yaml
# Found: bom_bracket_v0 shows steel_plate component
```

**Fix:** Add inputs based on BOM
```yaml
inputs:
  - item_id: steel_plate
    qty: 0.5
    unit: kg
```

---

## Summary

**Key Takeaways:**

1. Closure errors indicate **incomplete material flow definitions**
2. Fix **root causes**, not symptoms
3. Follow **Conservative Mode** principles
4. **Document assumptions** clearly
5. **Validate** with indexer and closure analysis
6. Expect **some new gaps** - each fix should net positive

Closure errors are normal and expected. They help us systematically complete the material flow graph.
