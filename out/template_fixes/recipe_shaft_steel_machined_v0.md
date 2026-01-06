# Fix Intelligence: recipe_shaft_steel_machined_v0

## Files

- **Recipe:** `kb/recipes/recipe_shaft_steel_machined_v0.yaml`
- **Target item:** `shaft_steel_machined`
  - File: `kb/items/shaft_steel_machined.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'steel_shaft_machining_v0') requires input 'steel_bar_raw' which is not available

**Location:** Step 0
**Process:** `steel_shaft_machining_v0`
  - File: `kb/processes/steel_shaft_machining_v0.yaml`

**Current step:**
```yaml
- process_id: steel_shaft_machining_v0
  inputs:
  - item_id: steel_bar_raw
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_raw` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_shaft_steel_machined_v0.yaml`
- **BOM available:** No
