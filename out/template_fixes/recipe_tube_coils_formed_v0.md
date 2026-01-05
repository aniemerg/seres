# Fix Intelligence: recipe_tube_coils_formed_v0

## Files

- **Recipe:** `kb/recipes/recipe_tube_coils_formed_v0.yaml`
- **Target item:** `tube_coils_formed`
  - File: `kb/items/tube_coils_formed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_forming_process_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `tube_forming_process_v0`
  - File: `kb/processes/tube_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: tube_forming_process_v0
  inputs:
  - item_id: metal_tubing_stock
    qty: 110.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_tubing_stock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tube_coils_formed_v0.yaml`
- **BOM available:** No
