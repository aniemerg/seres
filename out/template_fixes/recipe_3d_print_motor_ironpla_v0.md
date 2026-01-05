# Fix Intelligence: recipe_3d_print_motor_ironpla_v0

## Files

- **Recipe:** `kb/recipes/recipe_3d_print_motor_ironpla_v0.yaml`
- **Target item:** `3d_printed_motor_ironpla_v0`
  - File: `kb/items/3d_printed_motor_ironpla_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_3d_printed_motor_ironpla_v0` → 3d_printed_motor_ironpla_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'process_3d_print_motor_ironpla_v0') requires input 'printing_material_v0' which is not available

**Location:** Step 0
**Process:** `process_3d_print_motor_ironpla_v0`
  - File: `kb/processes/process_3d_print_motor_ironpla_v0.yaml`

**Current step:**
```yaml
- process_id: process_3d_print_motor_ironpla_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_3d_print_motor_ironpla_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
