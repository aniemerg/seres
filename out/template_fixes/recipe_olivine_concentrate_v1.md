# Fix Intelligence: recipe_olivine_concentrate_v1

## Files

- **Recipe:** `kb/recipes/recipe_olivine_concentrate_v1.yaml`
- **Target item:** `olivine_concentrate`
  - File: `kb/items/olivine_concentrate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_olivine_concentrate_v0` → olivine_concentrate (1 steps)
- `recipe_olivine_concentrate_v2` → olivine_concentrate (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'olivine_beneficiation_v0') requires input 'regolith_powder' which is not available

**Location:** Step 0
**Process:** `olivine_beneficiation_v0`
  - File: `kb/processes/olivine_beneficiation_v0.yaml`

**Current step:**
```yaml
- process_id: olivine_beneficiation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_olivine_concentrate_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
