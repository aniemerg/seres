# Fix Intelligence: recipe_nickel_grid_electrode_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_grid_electrode_v0.yaml`
- **Target item:** `nickel_grid_electrode_v0`
  - File: `kb/items/nickel_grid_electrode_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'nickel_grid_electrode_assembly_v0') requires input 'nickel_wire_fine' which is not available

**Location:** Step 0
**Process:** `nickel_grid_electrode_assembly_v0`
  - File: `kb/processes/nickel_grid_electrode_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: nickel_grid_electrode_assembly_v0
  inputs:
  - item_id: nickel_wire_fine
    qty: 0.4
    unit: kg
  - item_id: nickel_mesh_sheet_material
    qty: 0.6
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_wire_fine` not found

This item doesn't exist in the KB.

#### Problem: Item `nickel_mesh_sheet_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nickel_grid_electrode_v0.yaml`
- **BOM available:** No
