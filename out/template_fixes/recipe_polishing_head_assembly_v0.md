# Fix Intelligence: recipe_polishing_head_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_polishing_head_assembly_v0.yaml`
- **Target item:** `polishing_head_assembly`
  - File: `kb/items/polishing_head_assembly.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'assembly_basic_v0') requires input 'formed_metal_part' which is not available

**Location:** Step 1
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: formed_metal_part
    qty: 4.7
    unit: kg
  - item_id: shaft_steel_machined
    qty: 1.0
    unit: kg
  - item_id: bearing_set_small
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `formed_metal_part` not found

This item doesn't exist in the KB.

#### Problem: Item `shaft_steel_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_set_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_polishing_head_assembly_v0.yaml`
- **BOM available:** No
