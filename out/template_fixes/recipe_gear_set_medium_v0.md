# Fix Intelligence: recipe_gear_set_medium_v0

## Files

- **Recipe:** `kb/recipes/recipe_gear_set_medium_v0.yaml`
- **Target item:** `gear_set_medium`
  - File: `kb/items/gear_set_medium.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'gear_cutting_basic_v0') requires input 'steel_bar_raw' which is not available

**Location:** Step 0
**Process:** `gear_cutting_basic_v0`
  - File: `kb/processes/gear_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: gear_cutting_basic_v0
  inputs:
  - item_id: steel_bar_raw
    qty: 65.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_raw` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_gear_set_medium_v0.yaml`
- **BOM available:** No
