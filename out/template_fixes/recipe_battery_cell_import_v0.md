# Fix Intelligence: recipe_battery_cell_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_battery_cell_import_v0.yaml`
- **Target item:** `battery_cell`
  - File: `kb/items/battery_cell.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_battery_cell_v0` → battery_cell (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'battery_cell_assembly_v0') requires input 'electrode_materials' which is not available

**Location:** Step 0
**Process:** `battery_cell_assembly_v0`
  - File: `kb/processes/battery_cell_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: battery_cell_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_battery_cell_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
