# Fix Intelligence: recipe_antenna_elements_cut_v0

## Files

- **Recipe:** `kb/recipes/recipe_antenna_elements_cut_v0.yaml`
- **Target item:** `antenna_elements_cut`
  - File: `kb/items/antenna_elements_cut.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_cutting_process_v0') requires input 'aluminum_tube_stock' which is not available

**Location:** Step 0
**Process:** `metal_cutting_process_v0`
  - File: `kb/processes/metal_cutting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_cutting_process_v0
  inputs:
  - item_id: aluminum_tube_stock
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_tube_stock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_antenna_elements_cut_v0.yaml`
- **BOM available:** No
