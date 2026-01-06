# Fix Intelligence: recipe_magnesium_chloride_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnesium_chloride_v0.yaml`
- **Target item:** `magnesium_chloride`
  - File: `kb/items/magnesium_chloride.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'magnesium_chloride_from_mgo_v0') requires input 'magnesium_oxide' which is not available

**Location:** Step 0
**Process:** `magnesium_chloride_from_mgo_v0`
  - File: `kb/processes/magnesium_chloride_from_mgo_v0.yaml`

**Current step:**
```yaml
- process_id: magnesium_chloride_from_mgo_v0
  inputs:
  - item_id: magnesium_oxide
    qty: 1.0
    unit: kg
  - item_id: hydrochloric_acid
    qty: 1.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `magnesium_oxide` not found

This item doesn't exist in the KB.

#### Problem: Item `hydrochloric_acid` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnesium_chloride_v0.yaml`
- **BOM available:** No
