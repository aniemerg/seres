# Fix Intelligence: recipe_plastic_housing_molded_v0

## Files

- **Recipe:** `kb/recipes/recipe_plastic_housing_molded_v0.yaml`
- **Target item:** `plastic_housing_molded`
  - File: `kb/items/plastic_housing_molded.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'plastic_housing_molding_v0') requires input 'plastic_pellets' which is not available

**Location:** Step 0
**Process:** `plastic_housing_molding_v0`
  - File: `kb/processes/plastic_housing_molding_v0.yaml`

**Current step:**
```yaml
- process_id: plastic_housing_molding_v0
  inputs:
  - item_id: plastic_pellets
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `plastic_pellets` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_plastic_housing_molded_v0.yaml`
- **BOM available:** No
