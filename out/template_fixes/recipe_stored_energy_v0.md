# Fix Intelligence: recipe_stored_energy_v0

## Files

- **Recipe:** `kb/recipes/recipe_stored_energy_v0.yaml`
- **Target item:** `stored_energy`
  - File: `kb/items/stored_energy.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'solar_power_generation_basic_v0') requires input 'solar_irradiance' which is not available

**Location:** Step 0
**Process:** `solar_power_generation_basic_v0`
  - File: `kb/processes/solar_power_generation_basic_v0.yaml`

**Current step:**
```yaml
- process_id: solar_power_generation_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_stored_energy_v0.yaml`
- **BOM available:** No
