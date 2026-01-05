# Fix Intelligence: recipe_tin_metal_pure_v0

## Files

- **Recipe:** `kb/recipes/recipe_tin_metal_pure_v0.yaml`
- **Target item:** `tin_metal_pure`
  - File: `kb/items/tin_metal_pure.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_ingot_cast_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `metal_ingot_cast_v0`
  - File: `kb/processes/metal_ingot_cast_v0.yaml`

**Current step:**
```yaml
- process_id: metal_ingot_cast_v0
  inputs:
  - item_id: metal_alloy_bulk
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_alloy_bulk` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tin_metal_pure_v0.yaml`
- **BOM available:** No
