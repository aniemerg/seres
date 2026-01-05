# Fix Intelligence: recipe_carbon_anode_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_anode_v0.yaml`
- **Target item:** `carbon_anode`
  - File: `kb/items/carbon_anode.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_carbon_anode_from_material_v0` → carbon_anode (1 steps)
- `recipe_carbon_anode_v1` → carbon_anode (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbon_anode_forming_v0') requires input 'carbon_anode_material' which is not available

**Location:** Step 0
**Process:** `carbon_anode_forming_v0`
  - File: `kb/processes/carbon_anode_forming_v0.yaml`

**Current step:**
```yaml
- process_id: carbon_anode_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_anode_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
