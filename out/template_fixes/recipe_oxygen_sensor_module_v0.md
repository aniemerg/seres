# Fix Intelligence: recipe_oxygen_sensor_module_v0

## Files

- **Recipe:** `kb/recipes/recipe_oxygen_sensor_module_v0.yaml`
- **Target item:** `oxygen_sensor_module`
  - File: `kb/items/oxygen_sensor_module.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_oxygen_sensor_module_import_v0` → oxygen_sensor_module (1 steps)
- `recipe_oxygen_sensor_module_v1` → oxygen_sensor_module (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'oxygen_sensor_module_assembly_v0') requires input 'oxygen_sensor_zirconia_v0' which is not available

**Location:** Step 0
**Process:** `oxygen_sensor_module_assembly_v0`
  - File: `kb/processes/oxygen_sensor_module_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: oxygen_sensor_module_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_oxygen_sensor_module_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
