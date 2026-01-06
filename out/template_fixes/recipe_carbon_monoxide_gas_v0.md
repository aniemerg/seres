# Fix Intelligence: recipe_carbon_monoxide_gas_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_monoxide_gas_v0.yaml`
- **Target item:** `carbon_monoxide_gas_v0`
  - File: `kb/items/carbon_monoxide_gas_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_carbon_monoxide_gas_v1` → carbon_monoxide_gas (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbon_monoxide_generation_v0') requires input 'carbon_reductant' which is not available

**Location:** Step 0
**Process:** `carbon_monoxide_generation_v0`
  - File: `kb/processes/carbon_monoxide_generation_v0.yaml`

**Current step:**
```yaml
- process_id: carbon_monoxide_generation_v0
  inputs:
  - item_id: carbon_reductant
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `carbon_reductant` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_monoxide_gas_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
