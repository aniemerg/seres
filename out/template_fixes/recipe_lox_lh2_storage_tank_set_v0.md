# Fix Intelligence: recipe_lox_lh2_storage_tank_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_lox_lh2_storage_tank_set_v0.yaml`
- **Target item:** `lox_lh2_storage_tank_set`
  - File: `kb/items/lox_lh2_storage_tank_set.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_spinning_process_v0') requires input 'aluminum_sheet_2mm' which is not available

**Location:** Step 0
**Process:** `metal_spinning_process_v0`
  - File: `kb/processes/metal_spinning_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_spinning_process_v0
  inputs:
  - item_id: aluminum_sheet_2mm
    qty: 150.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_sheet_2mm` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_process_tig_v0') requires input 'aluminum_sheet_2mm' which is not available

**Location:** Step 1
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: tank_shell_spun
    qty: 140.0
    unit: kg
  - item_id: aluminum_sheet_2mm
    qty: 200.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_spun` not found

This item doesn't exist in the KB.

#### Problem: Item `aluminum_sheet_2mm` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'welding_process_tig_v0') requires input 'aluminum_sheet_2mm' which is not available

**Location:** Step 2
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: tank_shell_spun
    qty: 320.0
    unit: kg
  - item_id: aluminum_sheet_2mm
    qty: 150.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_spun` not found

This item doesn't exist in the KB.

#### Problem: Item `aluminum_sheet_2mm` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'machining_process_milling_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 3
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 30.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_process_general_v0') requires input 'tank_valve_and_fitting_set' which is not available

**Location:** Step 4
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: tank_shell_spun
    qty: 450.0
    unit: kg
  - item_id: tank_valve_and_fitting_set
    qty: 25.0
    unit: kg
  - item_id: insulation_thermal_blanket
    qty: 15.0
    unit: kg
  - item_id: valve_set_gas_handling
    qty: 4.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_spun` not found

This item doesn't exist in the KB.

#### Problem: Item `tank_valve_and_fitting_set` not found

This item doesn't exist in the KB.

#### Problem: Item `insulation_thermal_blanket` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_set_gas_handling` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_lox_lh2_storage_tank_set_v0.yaml`
- **BOM available:** No
