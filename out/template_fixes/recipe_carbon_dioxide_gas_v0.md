# Fix Intelligence: recipe_carbon_dioxide_gas_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_dioxide_gas_v0.yaml`
- **Target item:** `carbon_dioxide_gas`
  - File: `kb/items/carbon_dioxide_gas.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbon_dioxide_generation_v0') requires input 'carbon_reductant' which is not available

**Location:** Step 0
**Process:** `carbon_dioxide_generation_v0`
  - File: `kb/processes/carbon_dioxide_generation_v0.yaml`

**Current step:**
```yaml
- process_id: carbon_dioxide_generation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_dioxide_gas_v0.yaml`
- **BOM available:** No
