# Fix Intelligence: recipe_stainless_steel_sheet_v1

## Files

- **Recipe:** `kb/recipes/recipe_stainless_steel_sheet_v1.yaml`
- **Target item:** `stainless_steel_sheet`
  - File: `kb/items/stainless_steel_sheet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_stainless_steel_sheet_v0` → stainless_steel_sheet (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_making_from_ingot_stainless_v0') requires input 'stainless_steel_ingot' which is not available

**Location:** Step 0
**Process:** `sheet_making_from_ingot_stainless_v0`
  - File: `kb/processes/sheet_making_from_ingot_stainless_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_making_from_ingot_stainless_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_stainless_steel_sheet_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
