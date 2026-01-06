# Fix Intelligence: recipe_conveyor_drive_unit_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_conveyor_drive_unit_import_v0.yaml`
- **Target item:** `conveyor_drive_unit`
  - File: `kb/items/conveyor_drive_unit.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_conveyor_drive_unit_v0` → conveyor_drive_unit (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'conveyor_drive_unit_assembly_v0') requires input 'motor_electric_small' which is not available

**Location:** Step 0
**Process:** `conveyor_drive_unit_assembly_v0`
  - File: `kb/processes/conveyor_drive_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: conveyor_drive_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_conveyor_drive_unit_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
