# Fix Intelligence: recipe_metal_sheet_v0

## Files

- **Recipe:** `kb/recipes/recipe_metal_sheet_v0.yaml`
- **Target item:** `metal_sheet`
  - File: `kb/items/metal_sheet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_metal_sheet_v1` → metal_sheet (1 steps)
- `recipe_metal_sheet_import_v0` → metal_sheet (1 steps)

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'rolling_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `rolling_basic_v0`
  - File: `kb/processes/rolling_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: rolling_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metal_sheet_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
