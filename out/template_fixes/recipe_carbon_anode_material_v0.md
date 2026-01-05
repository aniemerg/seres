# Fix Intelligence: recipe_carbon_anode_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_anode_material_v0.yaml`
- **Target item:** `carbon_anode_material`
  - File: `kb/items/carbon_anode_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_carbon_anode_material_from_methane_v0` → carbon_anode_material (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'methane_pyrolysis_v0') requires input 'methane_gas' which is not available

**Location:** Step 0
**Process:** `methane_pyrolysis_v0`
  - File: `kb/processes/methane_pyrolysis_v0.yaml`

**Current step:**
```yaml
- process_id: methane_pyrolysis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_anode_material_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
