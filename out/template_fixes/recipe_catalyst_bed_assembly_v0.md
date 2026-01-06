# Fix Intelligence: recipe_catalyst_bed_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_catalyst_bed_assembly_v0.yaml`
- **Target item:** `catalyst_bed_assembly`
  - File: `kb/items/catalyst_bed_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: alumina_powder
    qty: 15.0
    unit: kg
  - item_id: nickel_metal
    qty: 2.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 7.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `nickel_metal` not found

This item doesn't exist in the KB.

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

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_catalyst_bed_assembly_v0.yaml`
- **BOM available:** No
