# Fix Intelligence: recipe_powder_metal_or_ceramic_v0

## Files

- **Recipe:** `kb/recipes/recipe_powder_metal_or_ceramic_v0.yaml`
- **Target item:** `powder_metal_or_ceramic`
  - File: `kb/items/powder_metal_or_ceramic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sizing_grinding_basic_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `sizing_grinding_basic_v0`
  - File: `kb/processes/sizing_grinding_basic_v0.yaml`

**Current step:**
```yaml
- process_id: sizing_grinding_basic_v0
  inputs:
  - item_id: metal_alloy_bulk
    qty: 10.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_alloy_bulk` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_powder_metal_or_ceramic_v0.yaml`
- **BOM available:** No
