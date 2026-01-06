# Fix Intelligence: recipe_stainless_steel_sheath_v0

## Files

- **Recipe:** `kb/recipes/recipe_stainless_steel_sheath_v0.yaml`
- **Target item:** `stainless_steel_sheath`
  - File: `kb/items/stainless_steel_sheath.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_forming_basic_v0') requires input 'stainless_steel_sheet' which is not available

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  inputs:
  - item_id: stainless_steel_sheet
    qty: 0.009
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `stainless_steel_sheet` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_stainless_steel_sheath_v0.yaml`
- **BOM available:** No
