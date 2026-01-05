# Fix Intelligence: recipe_separator_robust_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_separator_robust_import_v0.yaml`
- **Target item:** `separator_robust`
  - File: `kb/items/separator_robust.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_separator_robust_v0` → separator_robust (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'separator_fabrication_basic_v0') requires input 'ceramic_block_small_v0' which is not available

**Location:** Step 0
**Process:** `separator_fabrication_basic_v0`
  - File: `kb/processes/separator_fabrication_basic_v0.yaml`

**Current step:**
```yaml
- process_id: separator_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_separator_robust_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
