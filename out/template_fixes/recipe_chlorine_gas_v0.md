# Fix Intelligence: recipe_chlorine_gas_v0

## Files

- **Recipe:** `kb/recipes/recipe_chlorine_gas_v0.yaml`
- **Target item:** `chlorine_gas`
  - File: `kb/items/chlorine_gas.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_chloralkali_gas_v0` → chlorine_gas (1 steps)

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chloralkali_electrolysis_v0') requires input 'sodium_chloride' which is not available

**Location:** Step 0
**Process:** `chloralkali_electrolysis_v0`
  - File: `kb/processes/chloralkali_electrolysis_v0.yaml`

**Current step:**
```yaml
- process_id: chloralkali_electrolysis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'chloralkali_electrolysis_v0') requires input 'sodium_chloride' which is not available

**Location:** Step 1
**Process:** `chloralkali_electrolysis_v0`
  - File: `kb/processes/chloralkali_electrolysis_v0.yaml`

**Current step:**
```yaml
- process_id: chloralkali_electrolysis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_chlorine_gas_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
