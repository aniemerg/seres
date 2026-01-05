# Fix Intelligence: recipe_aluminum_chloride_hydrate_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminum_chloride_hydrate_v0.yaml`
- **Target item:** `aluminum_chloride_hydrate`
  - File: `kb/items/aluminum_chloride_hydrate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aluminum_chloride_hydrate_formation_v0') requires input 'aluminum_chloride' which is not available

**Location:** Step 0
**Process:** `aluminum_chloride_hydrate_formation_v0`
  - File: `kb/processes/aluminum_chloride_hydrate_formation_v0.yaml`

**Current step:**
```yaml
- process_id: aluminum_chloride_hydrate_formation_v0
  inputs:
  - item_id: aluminum_chloride
    qty: 1.0
    unit: kg
  - item_id: water
    qty: 0.8
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_chloride` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminum_chloride_hydrate_v0.yaml`
- **BOM available:** No
