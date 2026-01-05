# Fix Intelligence: recipe_negative_electrode_pressed_v0

## Files

- **Recipe:** `kb/recipes/recipe_negative_electrode_pressed_v0.yaml`
- **Target item:** `negative_electrode_pressed`
  - File: `kb/items/negative_electrode_pressed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_pressing_process_v0') requires input 'electrode_mix_nife' which is not available

**Location:** Step 0
**Process:** `powder_pressing_process_v0`
  - File: `kb/processes/powder_pressing_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_pressing_process_v0
  inputs:
  - item_id: electrode_mix_nife
    qty: 2.05
    unit: kg
  - item_id: electrode_grid_set
    qty: 0.7
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electrode_mix_nife` not found

This item doesn't exist in the KB.

#### Problem: Item `electrode_grid_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_negative_electrode_pressed_v0.yaml`
- **BOM available:** No
