# Fix Intelligence: recipe_grease_bearing_high_temp_v0

## Files

- **Recipe:** `kb/recipes/recipe_grease_bearing_high_temp_v0.yaml`
- **Target item:** `grease_bearing_high_temp`
  - File: `kb/items/grease_bearing_high_temp.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_grease_bearing_high_temp_import_v0` → grease_bearing_high_temp (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lubricant_compounding_high_temp_v0') requires input 'base_grease_stock_v0' which is not available

**Location:** Step 0
**Process:** `lubricant_compounding_high_temp_v0`
  - File: `kb/processes/lubricant_compounding_high_temp_v0.yaml`

**Current step:**
```yaml
- process_id: lubricant_compounding_high_temp_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_grease_bearing_high_temp_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
