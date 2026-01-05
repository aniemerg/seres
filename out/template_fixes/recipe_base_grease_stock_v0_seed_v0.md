# Fix Intelligence: recipe_base_grease_stock_v0_seed_v0

## Files

- **Recipe:** `kb/recipes/recipe_base_grease_stock_v0_seed_v0.yaml`
- **Target item:** `base_grease_stock_v0`
  - File: `kb/items/base_grease_stock_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_base_grease_stock_v0` → base_grease_stock_v0 (1 steps)
- `recipe_base_grease_stock_import_v0` → base_grease_stock (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'grease_stock_v0_conversion_v0') requires input 'base_grease_stock' which is not available

**Location:** Step 0
**Process:** `grease_stock_v0_conversion_v0`
  - File: `kb/processes/grease_stock_v0_conversion_v0.yaml`

**Current step:**
```yaml
- process_id: grease_stock_v0_conversion_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_base_grease_stock_v0_seed_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
