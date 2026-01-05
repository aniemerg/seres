# Fix Intelligence: recipe_valve_body_machined_v0

## Files

- **Recipe:** `kb/recipes/recipe_valve_body_machined_v0.yaml`
- **Target item:** `valve_body_machined`
  - File: `kb/items/valve_body_machined.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'valve_body_boring_v0') requires input 'valve_body_cast_rough' which is not available

**Location:** Step 0
**Process:** `valve_body_boring_v0`
  - File: `kb/processes/valve_body_boring_v0.yaml`

**Current step:**
```yaml
- process_id: valve_body_boring_v0
  inputs:
  - item_id: valve_body_cast_rough
    qty: 4.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `valve_body_cast_rough` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_valve_body_machined_v0.yaml`
- **BOM available:** No
