# Fix Intelligence: recipe_lox_storage_tank_cryogenic_v0

## Files

- **Recipe:** `kb/recipes/recipe_lox_storage_tank_cryogenic_v0.yaml`
- **Target item:** `lox_storage_tank_cryogenic_v0`
  - File: `kb/items/lox_storage_tank_cryogenic_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

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

**Message:** Step 1 (process 'sealing_and_assembly_basic_v0') requires input 'insulation_pack_high_temp' which is not available

**Location:** Step 1
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: tank_shell_spun
    qty: 1.0
    unit: unit
  - item_id: insulation_pack_high_temp
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tank_shell_spun` not found

This item doesn't exist in the KB.

#### Problem: Item `insulation_pack_high_temp` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_lox_storage_tank_cryogenic_v0.yaml`
- **BOM available:** No
