# Fix Intelligence: recipe_thermionic_topping_cycle_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermionic_topping_cycle_v0.yaml`
- **Target item:** `thermionic_topping_cycle_v0`
  - File: `kb/items/thermionic_topping_cycle_v0.yaml`
- **BOM:** `kb/boms/bom_thermionic_topping_cycle_v0.yaml` ✓
  - Components: 6
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'thermionic_power_generation_v0') requires input 'concentrated_solar_thermal' which is not available

**Location:** Step 0
**Process:** `thermionic_power_generation_v0`
  - File: `kb/processes/thermionic_power_generation_v0.yaml`

**Current step:**
```yaml
- process_id: thermionic_power_generation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_thermionic_topping_cycle_v0.yaml`
- **BOM available:** Yes (6 components)
