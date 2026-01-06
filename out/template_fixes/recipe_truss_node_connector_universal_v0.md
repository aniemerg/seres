# Fix Intelligence: recipe_truss_node_connector_universal_v0

## Files

- **Recipe:** `kb/recipes/recipe_truss_node_connector_universal_v0.yaml`
- **Target item:** `truss_node_connector_universal_v0`
  - File: `kb/items/truss_node_connector_universal_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_cutting_process_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `metal_cutting_process_v0`
  - File: `kb/processes/metal_cutting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_cutting_process_v0
  inputs:
  - item_id: steel_plate_or_sheet
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_plate_or_sheet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `gasket_sheet_material_v0`
- `gasket_sheet`
- `steel_plate_raw`
- `steel_plate_or_sheet`
- `iron_powder_or_sheet`
- `sheet_metal_or_structural_steel`
- `brass_sheet`
- `nickel_sheet_rolling_forming_v0`
- `steel_sheet_1mm`
- `steel_sheet_3mm`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_truss_node_connector_universal_v0.yaml`
- **BOM available:** No
