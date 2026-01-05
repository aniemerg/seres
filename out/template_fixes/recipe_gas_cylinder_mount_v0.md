# Fix Intelligence: recipe_gas_cylinder_mount_v0

## Files

- **Recipe:** `kb/recipes/recipe_gas_cylinder_mount_v0.yaml`
- **Target item:** `gas_cylinder_mount`
  - File: `kb/items/gas_cylinder_mount.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'gas_cylinder_mount_basic_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `gas_cylinder_mount_basic_v0`
  - File: `kb/processes/gas_cylinder_mount_basic_v0.yaml`

**Current step:**
```yaml
- process_id: gas_cylinder_mount_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_gas_cylinder_mount_v0.yaml`
- **BOM available:** No
