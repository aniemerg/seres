# Fix Intelligence: recipe_tube_electrode_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_tube_electrode_set_v0.yaml`
- **Target item:** `tube_electrode_set`
  - File: `kb/items/tube_electrode_set.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_forming_process_v0') requires input 'nickel_wire_fine' which is not available

**Location:** Step 0
**Process:** `wire_forming_process_v0`
  - File: `kb/processes/wire_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_forming_process_v0
  inputs:
  - item_id: nickel_wire_fine
    qty: 0.007
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_wire_fine` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tube_electrode_set_v0.yaml`
- **BOM available:** No
