# Fix Intelligence: recipe_spinneret_heating_module_v0

## Files

- **Recipe:** `kb/recipes/recipe_spinneret_heating_module_v0.yaml`
- **Target item:** `spinneret_heating_module`
  - File: `kb/items/spinneret_heating_module.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'spool_winding_basic_v0') requires input 'nickel_wire_fine' which is not available

**Location:** Step 0
**Process:** `spool_winding_basic_v0`
  - File: `kb/processes/spool_winding_basic_v0.yaml`

**Current step:**
```yaml
- process_id: spool_winding_basic_v0
  inputs:
  - item_id: nickel_wire_fine
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_wire_fine` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ceramic_coating_v0') requires input 'ceramic_powder' which is not available

**Location:** Step 1
**Process:** `ceramic_coating_v0`
  - File: `kb/processes/ceramic_coating_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_coating_v0
  inputs:
  - item_id: ceramic_powder
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `ceramic_powder` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_finish_basic_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 2
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_plate_or_sheet
    qty: 7.0
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

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_basic_v0') requires input 'temperature_controller_basic' which is not available

**Location:** Step 3
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: temperature_controller_basic
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `temperature_controller_basic` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_spinneret_heating_module_v0.yaml`
- **BOM available:** No
