# Fix Intelligence: recipe_silicon_metal_from_regolith_carbothermic_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_metal_from_regolith_carbothermic_v0.yaml`
- **Target item:** `silicon_metal_v0`
  - File: `kb/items/silicon_metal_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_silicon_metal_v0` → silicon_metal_v0 (1 steps)
- `recipe_silicon_metal_from_regolith_magnesiothermic_v0` → silicon_metal_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'silicon_extraction_from_regolith_carbothermic_v0') requires input 'regolith_lunar_highlands' which is not available

**Location:** Step 0
**Process:** `silicon_extraction_from_regolith_carbothermic_v0`
  - File: `kb/processes/silicon_extraction_from_regolith_carbothermic_v0.yaml`

**Current step:**
```yaml
- process_id: silicon_extraction_from_regolith_carbothermic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicon_metal_from_regolith_carbothermic_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
