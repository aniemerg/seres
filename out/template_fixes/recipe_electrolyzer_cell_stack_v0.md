# Fix Intelligence: recipe_electrolyzer_cell_stack_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrolyzer_cell_stack_v0.yaml`
- **Target item:** `electrolyzer_cell_stack`
  - File: `kb/items/electrolyzer_cell_stack.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'stainless_steel_sheet' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: stainless_steel_sheet
    qty: 18.0
    unit: kg
  - item_id: separator_membrane_porous
    qty: 2.0
    unit: kg
  - item_id: gasket_sheet_material_v0
    qty: 1.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 4.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `stainless_steel_sheet` not found

This item doesn't exist in the KB.

#### Problem: Item `separator_membrane_porous` not found

This item doesn't exist in the KB.

#### Problem: Item `gasket_sheet_material_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrolyzer_cell_stack_v0.yaml`
- **BOM available:** No
