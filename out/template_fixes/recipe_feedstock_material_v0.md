# Fix Intelligence: recipe_feedstock_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_feedstock_material_v0.yaml`
- **Target item:** `feedstock_material`
  - File: `kb/items/feedstock_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'material_preparation_basic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `material_preparation_basic_v0`
  - File: `kb/processes/material_preparation_basic_v0.yaml`

**Current step:**
```yaml
- process_id: material_preparation_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_feedstock_material_v0.yaml`
- **BOM available:** No
