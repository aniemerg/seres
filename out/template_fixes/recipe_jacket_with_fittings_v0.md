# Fix Intelligence: recipe_jacket_with_fittings_v0

## Files

- **Recipe:** `kb/recipes/recipe_jacket_with_fittings_v0.yaml`
- **Target item:** `jacket_with_fittings`
  - File: `kb/items/jacket_with_fittings.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_forming_process_v0') requires input 'copper_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `sheet_metal_forming_process_v0`
  - File: `kb/processes/sheet_metal_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_forming_process_v0
  inputs:
  - item_id: copper_plate_or_sheet
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `copper_plate_or_sheet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `gasket_sheet_material_v0`
- `gasket_sheet`
- `steel_plate_or_sheet`
- `iron_powder_or_sheet`
- `sheet_metal_or_structural_steel`
- `brass_sheet`
- `nickel_sheet_rolling_forming_v0`
- `steel_sheet_1mm`
- `steel_sheet_3mm`
- `nickel_mesh_sheet_material`

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_process_tig_v0') requires input 'jacket_panels_formed' which is not available

**Location:** Step 1
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: jacket_panels_formed
    qty: 2.8
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `jacket_panels_formed` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'brazing_process_v0') requires input 'jacket_shell_welded' which is not available

**Location:** Step 2
**Process:** `brazing_process_v0`
  - File: `kb/processes/brazing_process_v0.yaml`

**Current step:**
```yaml
- process_id: brazing_process_v0
  inputs:
  - item_id: jacket_shell_welded
    qty: 2.7
    unit: kg
  - item_id: fittings_and_valves
    qty: 0.3
    unit: kg
  - item_id: brazing_alloy_generic
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `jacket_shell_welded` not found

This item doesn't exist in the KB.

#### Problem: Item `fittings_and_valves` not found

This item doesn't exist in the KB.

#### Problem: Item `brazing_alloy_generic` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_jacket_with_fittings_v0.yaml`
- **BOM available:** No
