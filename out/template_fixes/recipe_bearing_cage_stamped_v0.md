# Fix Intelligence: recipe_bearing_cage_stamped_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_cage_stamped_v0.yaml`
- **Target item:** `bearing_cage_stamped`
  - File: `kb/items/bearing_cage_stamped.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_stamping_process_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 0
**Process:** `metal_stamping_process_v0`
  - File: `kb/processes/metal_stamping_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_stamping_process_v0
  inputs:
  - item_id: steel_sheet_1mm
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_1mm` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bearing_cage_stamped_v0.yaml`
- **BOM available:** No
