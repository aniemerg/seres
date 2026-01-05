# Fix Intelligence: recipe_aluminum_sheet_2mm_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminum_sheet_2mm_v0.yaml`
- **Target item:** `aluminum_sheet_2mm`
  - File: `kb/items/aluminum_sheet_2mm.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'rolling_basic_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `rolling_basic_v0`
  - File: `kb/processes/rolling_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: rolling_basic_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 1.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminum_sheet_2mm_v0.yaml`
- **BOM available:** No
