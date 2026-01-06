# Fix Intelligence: recipe_ph_sensor_glass_electrode_v0

## Files

- **Recipe:** `kb/recipes/recipe_ph_sensor_glass_electrode_v0.yaml`
- **Target item:** `ph_sensor_glass_electrode_v0`
  - File: `kb/items/ph_sensor_glass_electrode_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ph_sensor_glass_electrode_fabrication_v0') requires input 'glass_envelope_vacuum_tube_v0' which is not available

**Location:** Step 0
**Process:** `ph_sensor_glass_electrode_fabrication_v0`
  - File: `kb/processes/ph_sensor_glass_electrode_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: ph_sensor_glass_electrode_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ph_sensor_glass_electrode_v0.yaml`
- **BOM available:** No
