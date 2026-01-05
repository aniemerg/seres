# Fix Intelligence: recipe_strain_gauge_foil_v0

## Files

- **Recipe:** `kb/recipes/recipe_strain_gauge_foil_v0.yaml`
- **Target item:** `strain_gauge_foil_v0`
  - File: `kb/items/strain_gauge_foil_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cutting_basic_v0') requires input 'aluminum_sheet_2mm' which is not available

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  inputs:
  - item_id: aluminum_sheet_2mm
    qty: 0.012
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_sheet_2mm` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_strain_gauge_foil_v0.yaml`
- **BOM available:** No
