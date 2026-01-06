# Fix Intelligence: recipe_electrode_grid_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrode_grid_set_v0.yaml`
- **Target item:** `electrode_grid_set`
  - File: `kb/items/electrode_grid_set.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: sheet_metal_or_structural_steel
    qty: 1.4
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `sheet_metal_or_structural_steel`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `sheet_metal_or_structural_steel`
- `steel_chassis_sheet_metal`
- `formed_sheet_metal_parts`
- `structural_steel_frame`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrode_grid_set_v0.yaml`
- **BOM available:** No
