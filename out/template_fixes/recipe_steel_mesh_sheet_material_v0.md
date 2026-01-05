# Fix Intelligence: recipe_steel_mesh_sheet_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_mesh_sheet_material_v0.yaml`
- **Target item:** `steel_mesh_sheet_material`
  - File: `kb/items/steel_mesh_sheet_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'steel_mesh_sheet_production_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `steel_mesh_sheet_production_v0`
  - File: `kb/processes/steel_mesh_sheet_production_v0.yaml`

**Current step:**
```yaml
- process_id: steel_mesh_sheet_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_mesh_sheet_material_v0.yaml`
- **BOM available:** No
