# Fix Intelligence: recipe_regolith_powder_v0

## Files

- **Recipe:** `kb/recipes/recipe_regolith_powder_v0.yaml`
- **Target item:** `regolith_powder`
  - File: `kb/items/regolith_powder.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'regolith_crushing_grinding_v0') requires input 'regolith_coarse_fraction' which is not available

**Location:** Step 0
**Process:** `regolith_crushing_grinding_v0`
  - File: `kb/processes/regolith_crushing_grinding_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_crushing_grinding_v0
  inputs:
  - item_id: regolith_coarse_fraction
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_coarse_fraction` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_regolith_powder_v0.yaml`
- **BOM available:** No
