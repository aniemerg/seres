# Fix Intelligence: recipe_hydrochloric_acid_v1

## Files

- **Recipe:** `kb/recipes/recipe_hydrochloric_acid_v1.yaml`
- **Target item:** `hydrochloric_acid`
  - File: `kb/items/hydrochloric_acid.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_hcl_recycling_from_salt_waste_v0` → hydrochloric_acid (1 steps)
- `recipe_hydrochloric_acid_v0` → hydrochloric_acid (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hydrochloric_acid_synthesis_v0') requires input 'chlorine_gas' which is not available

**Location:** Step 0
**Process:** `hydrochloric_acid_synthesis_v0`
  - File: `kb/processes/hydrochloric_acid_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: hydrochloric_acid_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hydrochloric_acid_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
