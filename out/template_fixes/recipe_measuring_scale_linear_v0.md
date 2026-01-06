# Fix Intelligence: recipe_measuring_scale_linear_v0

## Files

- **Recipe:** `kb/recipes/recipe_measuring_scale_linear_v0.yaml`
- **Target item:** `measuring_scale_linear`
  - File: `kb/items/measuring_scale_linear.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'precision_scale_fabrication_v0') requires input 'steel_strip_thin' which is not available

**Location:** Step 0
**Process:** `precision_scale_fabrication_v0`
  - File: `kb/processes/precision_scale_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: precision_scale_fabrication_v0
  inputs:
  - item_id: steel_strip_thin
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_strip_thin` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_measuring_scale_linear_v0.yaml`
- **BOM available:** No
