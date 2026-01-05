# Fix Intelligence: recipe_coating_compound_v0

## Files

- **Recipe:** `kb/recipes/recipe_coating_compound_v0.yaml`
- **Target item:** `coating_compound`
  - File: `kb/items/coating_compound.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'coating_compound_production_v0') requires input 'barium_oxide' which is not available

**Location:** Step 0
**Process:** `coating_compound_production_v0`
  - File: `kb/processes/coating_compound_production_v0.yaml`

**Current step:**
```yaml
- process_id: coating_compound_production_v0
  inputs:
  - item_id: barium_oxide
    qty: 0.8
    unit: kg
  - item_id: binder_material
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `barium_oxide` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coating_compound_v0.yaml`
- **BOM available:** No
