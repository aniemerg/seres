# Fix Intelligence: recipe_tailstock_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_tailstock_assembly_v0.yaml`
- **Target item:** `tailstock_assembly`
  - File: `kb/items/tailstock_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tailstock_assembly_basic_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `tailstock_assembly_basic_v0`
  - File: `kb/processes/tailstock_assembly_basic_v0.yaml`

**Current step:**
```yaml
- process_id: tailstock_assembly_basic_v0
  inputs:
  - item_id: steel_plate_or_sheet
    qty: 5.0
    unit: kg
  - item_id: ball_bearing_steel_v0
    qty: 2.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 0.5
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

#### Problem: Item `ball_bearing_steel_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tailstock_assembly_v0.yaml`
- **BOM available:** No
