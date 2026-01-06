# Fix Intelligence: recipe_tensioner_frame_welded_v0

## Files

- **Recipe:** `kb/recipes/recipe_tensioner_frame_welded_v0.yaml`
- **Target item:** `tensioner_frame_welded`
  - File: `kb/items/tensioner_frame_welded.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_fabrication_welding_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 1.5
    unit: kg
  - item_id: steel_sheet_3mm
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

#### Problem: Item `steel_sheet_3mm` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tensioner_frame_welded_v0.yaml`
- **BOM available:** No
