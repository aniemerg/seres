# Fix Intelligence: recipe_magnesium_powder_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnesium_powder_v0.yaml`
- **Target item:** `magnesium_powder_v0`
  - File: `kb/items/magnesium_powder_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ball_milling_v0') requires input 'magnesium_metal_v0' which is not available

**Location:** Step 0
**Process:** `ball_milling_v0`
  - File: `kb/processes/ball_milling_v0.yaml`

**Current step:**
```yaml
- process_id: ball_milling_v0
  inputs:
  - item_id: magnesium_metal_v0
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `magnesium_metal_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnesium_powder_v0.yaml`
- **BOM available:** No
