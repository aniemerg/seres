# Fix Intelligence: recipe_ceramic_zirconia_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_zirconia_v0.yaml`
- **Target item:** `zirconia_ceramic_v0`
  - File: `kb/items/zirconia_ceramic_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ceramic_sintering_v0') requires input 'powder_feedstock' which is not available

**Location:** Step 0
**Process:** `ceramic_sintering_v0`
  - File: `kb/processes/ceramic_sintering_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_sintering_v0
  inputs:
  - item_id: powder_feedstock
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `powder_feedstock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ceramic_zirconia_v0.yaml`
- **BOM available:** No
