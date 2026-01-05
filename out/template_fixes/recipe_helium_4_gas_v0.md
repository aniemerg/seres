# Fix Intelligence: recipe_helium_4_gas_v0

## Files

- **Recipe:** `kb/recipes/recipe_helium_4_gas_v0.yaml`
- **Target item:** `helium_4_gas`
  - File: `kb/items/helium_4_gas.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'regolith_volatile_thermal_extraction_v0') requires input 'regolith_lunar_highlands' which is not available

**Location:** Step 0
**Process:** `regolith_volatile_thermal_extraction_v0`
  - File: `kb/processes/regolith_volatile_thermal_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_volatile_thermal_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_helium_4_gas_v0.yaml`
- **BOM available:** No
