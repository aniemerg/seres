# Fix Intelligence: recipe_gasket_sheet_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_gasket_sheet_import_v0.yaml`
- **Target item:** `gasket_sheet`
  - File: `kb/items/gasket_sheet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_gasket_sheet_v0` → gasket_sheet (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'plastic_sheet_extrusion_v0') requires input 'plastic_pellets' which is not available

**Location:** Step 0
**Process:** `plastic_sheet_extrusion_v0`
  - File: `kb/processes/plastic_sheet_extrusion_v0.yaml`

**Current step:**
```yaml
- process_id: plastic_sheet_extrusion_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_gasket_sheet_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
