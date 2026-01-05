# Fix Intelligence: recipe_stator_wound_v0

## Files

- **Recipe:** `kb/recipes/recipe_stator_wound_v0.yaml`
- **Target item:** `stator_wound`
  - File: `kb/items/stator_wound.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_winding_process_v0') requires input 'steel_lamination_stack' which is not available

**Location:** Step 0
**Process:** `wire_winding_process_v0`
  - File: `kb/processes/wire_winding_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_winding_process_v0
  inputs:
  - item_id: steel_lamination_stack
    qty: 0.8
    unit: kg
  - item_id: wire_copper_magnet
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_lamination_stack` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_magnet` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_stator_wound_v0.yaml`
- **BOM available:** No
