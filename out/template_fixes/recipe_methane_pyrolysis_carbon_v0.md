# Fix Intelligence: recipe_methane_pyrolysis_carbon_v0

## Files

- **Recipe:** `kb/recipes/recipe_methane_pyrolysis_carbon_v0.yaml`
- **Target item:** `methane_pyrolysis_carbon_v0`
  - File: `kb/items/methane_pyrolysis_carbon_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'methane_pyrolysis_basic_v0') requires input 'methane_gas_v0' which is not available

**Location:** Step 0
**Process:** `methane_pyrolysis_basic_v0`
  - File: `kb/processes/methane_pyrolysis_basic_v0.yaml`

**Current step:**
```yaml
- process_id: methane_pyrolysis_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_methane_pyrolysis_carbon_v0.yaml`
- **BOM available:** No
