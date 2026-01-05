# Fix Intelligence: recipe_hcl_recycling_from_salt_waste_v0

## Files

- **Recipe:** `kb/recipes/recipe_hcl_recycling_from_salt_waste_v0.yaml`
- **Target item:** `hydrochloric_acid`
  - File: `kb/items/hydrochloric_acid.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_hydrochloric_acid_v1` → hydrochloric_acid (1 steps)
- `recipe_hydrochloric_acid_v0` → hydrochloric_acid (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chloride_recycling_to_hcl_v0') requires input 'salt_waste' which is not available

**Location:** Step 0
**Process:** `chloride_recycling_to_hcl_v0`
  - File: `kb/processes/chloride_recycling_to_hcl_v0.yaml`

**Current step:**
```yaml
- process_id: chloride_recycling_to_hcl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hcl_recycling_from_salt_waste_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
