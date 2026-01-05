# Fix Intelligence: recipe_component_to_seal_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_component_to_seal_import_v0.yaml`
- **Target item:** `component_to_seal`
  - File: `kb/items/component_to_seal.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_component_to_seal_v0` → component_to_seal (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'component_to_seal_from_raw_material_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `component_to_seal_from_raw_material_v0`
  - File: `kb/processes/component_to_seal_from_raw_material_v0.yaml`

**Current step:**
```yaml
- process_id: component_to_seal_from_raw_material_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_component_to_seal_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
