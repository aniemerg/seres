# Fix Intelligence: recipe_electrical_energy_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrical_energy_v0.yaml`
- **Target item:** `electrical_energy`
  - File: `kb/items/electrical_energy.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_electrical_energy_basic_v0` → electrical_energy (3 steps)
- `recipe_electrical_energy_thermionic_v0` → electrical_energy (3 steps)

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
- **Recipe file:** `kb/recipes/recipe_electrical_energy_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
