# Fix Intelligence: recipe_position_sensor_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_position_sensor_set_v0.yaml`
- **Target item:** `position_sensor_set`
  - File: `kb/items/position_sensor_set.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'position_sensor_set_assembly_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 0
**Process:** `position_sensor_set_assembly_v0`
  - File: `kb/processes/position_sensor_set_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: position_sensor_set_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_position_sensor_set_v0.yaml`
- **BOM available:** No
