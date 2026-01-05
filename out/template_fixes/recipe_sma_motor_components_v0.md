# Fix Intelligence: recipe_sma_motor_components_v0

## Files

- **Recipe:** `kb/recipes/recipe_sma_motor_components_v0.yaml`
- **Target item:** `sma_motor_components`
  - File: `kb/items/sma_motor_components.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'process_3d_print_motor_sma_v0') requires input 'shape_memory_wire_sma' which is not available

**Location:** Step 0
**Process:** `process_3d_print_motor_sma_v0`
  - File: `kb/processes/process_3d_print_motor_sma_v0.yaml`

**Current step:**
```yaml
- process_id: process_3d_print_motor_sma_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sma_motor_components_v0.yaml`
- **BOM available:** No
