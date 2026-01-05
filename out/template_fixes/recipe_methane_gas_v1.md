# Fix Intelligence: recipe_methane_gas_v1

## Files

- **Recipe:** `kb/recipes/recipe_methane_gas_v1.yaml`
- **Target item:** `methane_gas`
  - File: `kb/items/methane_gas.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_methane_gas_v0` → methane_gas_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'methanation_basic_v0') requires input 'carbon_dioxide_gas' which is not available

**Location:** Step 0
**Process:** `methanation_basic_v0`
  - File: `kb/processes/methanation_basic_v0.yaml`

**Current step:**
```yaml
- process_id: methanation_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_methane_gas_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
