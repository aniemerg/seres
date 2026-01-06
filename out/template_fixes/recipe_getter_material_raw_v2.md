# Fix Intelligence: recipe_getter_material_raw_v2

## Files

- **Recipe:** `kb/recipes/recipe_getter_material_raw_v2.yaml`
- **Target item:** `getter_material_raw`
  - File: `kb/items/getter_material_raw.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'getter_material_raw_generation_v0') requires input 'barium_oxide' which is not available

**Location:** Step 0
**Process:** `getter_material_raw_generation_v0`
  - File: `kb/processes/getter_material_raw_generation_v0.yaml`

**Current step:**
```yaml
- process_id: getter_material_raw_generation_v0
  inputs:
  - item_id: barium_oxide
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `barium_oxide` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_getter_material_raw_v2.yaml`
- **BOM available:** No
