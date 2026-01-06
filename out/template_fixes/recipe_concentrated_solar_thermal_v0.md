# Fix Intelligence: recipe_concentrated_solar_thermal_v0

## Files

- **Recipe:** `kb/recipes/recipe_concentrated_solar_thermal_v0.yaml`
- **Target item:** `concentrated_solar_thermal`
  - File: `kb/items/concentrated_solar_thermal.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'solar_thermal_concentration_v0') requires input 'solar_radiation' which is not available

**Location:** Step 0
**Process:** `solar_thermal_concentration_v0`
  - File: `kb/processes/solar_thermal_concentration_v0.yaml`

**Current step:**
```yaml
- process_id: solar_thermal_concentration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_concentrated_solar_thermal_v0.yaml`
- **BOM available:** No
