# Fix Intelligence: recipe_control_circuit_stepper_driver_v0

## Files

- **Recipe:** `kb/recipes/recipe_control_circuit_stepper_driver_v0.yaml`
- **Target item:** `control_circuit_stepper_driver`
  - File: `kb/items/control_circuit_stepper_driver.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'control_circuit_stepper_driver_assembly_v0') requires input 'assembled_electronics' which is not available

**Location:** Step 0
**Process:** `control_circuit_stepper_driver_assembly_v0`
  - File: `kb/processes/control_circuit_stepper_driver_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: control_circuit_stepper_driver_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_control_circuit_stepper_driver_v0.yaml`
- **BOM available:** No
