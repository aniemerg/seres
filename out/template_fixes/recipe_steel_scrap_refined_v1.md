# Fix Intelligence: recipe_steel_scrap_refined_v1

## Files

- **Recipe:** `kb/recipes/recipe_steel_scrap_refined_v1.yaml`
- **Target item:** `steel_scrap_refined`
  - File: `kb/items/steel_scrap_refined.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_steel_scrap_refined_v0` → steel_scrap_refined_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'steel_scrap_refining_v0') requires input 'steel_scrap_v0' which is not available

**Location:** Step 0
**Process:** `steel_scrap_refining_v0`
  - File: `kb/processes/steel_scrap_refining_v0.yaml`

**Current step:**
```yaml
- process_id: steel_scrap_refining_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_scrap_refined_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
