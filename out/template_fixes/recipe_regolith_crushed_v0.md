# Fix Intelligence: recipe_regolith_crushed_v0

## Files

- **Recipe:** `kb/recipes/recipe_regolith_crushed_v0.yaml`
- **Target item:** `regolith_crushed`
  - File: `kb/items/regolith_crushed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'crushing_basic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `crushing_basic_v0`
  - File: `kb/processes/crushing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: crushing_basic_v0
  inputs:
  - item_id: regolith_lunar_mare
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_lunar_mare` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_regolith_crushed_v0.yaml`
- **BOM available:** No
