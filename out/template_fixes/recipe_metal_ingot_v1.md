# Fix Intelligence: recipe_metal_ingot_v1

## Files

- **Recipe:** `kb/recipes/recipe_metal_ingot_v1.yaml`
- **Target item:** `metal_ingot`
  - File: `kb/items/metal_ingot.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_metal_ingot_v0` → metal_ingot_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_ingot_cast_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `metal_ingot_cast_v0`
  - File: `kb/processes/metal_ingot_cast_v0.yaml`

**Current step:**
```yaml
- process_id: metal_ingot_cast_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metal_ingot_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
