# Fix Intelligence: recipe_current_collector_nickel_or_steel_mesh_v0

## Files

- **Recipe:** `kb/recipes/recipe_current_collector_nickel_or_steel_mesh_v0.yaml`
- **Target item:** `current_collector_nickel_or_steel_mesh`
  - File: `kb/items/current_collector_nickel_or_steel_mesh.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_current_collector_nickel_or_steel_mesh_import_v0` → current_collector_nickel_or_steel_mesh (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mesh_fabrication_v0') requires input 'nickel_mesh_sheet_material' which is not available

**Location:** Step 0
**Process:** `mesh_fabrication_v0`
  - File: `kb/processes/mesh_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: mesh_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_current_collector_nickel_or_steel_mesh_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
