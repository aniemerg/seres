# Fix Intelligence: recipe_safety_guard_steel_mesh_v3

## Files

- **Recipe:** `kb/recipes/recipe_safety_guard_steel_mesh_v3.yaml`
- **Target item:** `safety_guard_steel_mesh`
  - File: `kb/items/safety_guard_steel_mesh.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_safety_guard_steel_mesh_v4` → safety_guard_steel_mesh (1 steps)
- `recipe_safety_guard_steel_mesh_v2` → safety_guard_steel_mesh (1 steps)
- `recipe_safety_guard_steel_mesh_v1` → safety_guard_steel_mesh (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mesh_fabrication_steel_guard_v1') requires input 'steel_mesh_sheet_material' which is not available

**Location:** Step 0
**Process:** `mesh_fabrication_steel_guard_v1`
  - File: `kb/processes/mesh_fabrication_steel_guard_v1.yaml`

**Current step:**
```yaml
- process_id: mesh_fabrication_steel_guard_v1
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_safety_guard_steel_mesh_v3.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
