# Fix Intelligence: recipe_microcontroller_or_embedded_board_v0

## Files

- **Recipe:** `kb/recipes/recipe_microcontroller_or_embedded_board_v0.yaml`
- **Target item:** `microcontroller_or_embedded_board`
  - File: `kb/items/microcontroller_or_embedded_board.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pcb_fabrication_process_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 0
**Process:** `pcb_fabrication_process_v0`
  - File: `kb/processes/pcb_fabrication_process_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_fabrication_process_v0
  inputs:
  - item_id: copper_clad_laminate
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'solder_paste_application_v0') requires input 'pcb_bare_board' which is not available

**Location:** Step 1
**Process:** `solder_paste_application_v0`
  - File: `kb/processes/solder_paste_application_v0.yaml`

**Current step:**
```yaml
- process_id: solder_paste_application_v0
  inputs:
  - item_id: pcb_bare_board
    qty: 0.04
    unit: kg
  - item_id: solder_paste_tin_lead
    qty: 0.005
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_bare_board` not found

This item doesn't exist in the KB.

#### Problem: Item `solder_paste_tin_lead` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'component_placement_process_v0') requires input 'microcontroller_ic_generic' which is not available

**Location:** Step 2
**Process:** `component_placement_process_v0`
  - File: `kb/processes/component_placement_process_v0.yaml`

**Current step:**
```yaml
- process_id: component_placement_process_v0
  inputs:
  - item_id: pcb_paste_applied
    qty: 0.045
    unit: kg
  - item_id: microcontroller_ic_generic
    qty: 1.0
    unit: each
  - item_id: capacitor_ceramic_generic
    qty: 10.0
    unit: each
  - item_id: resistor_chip_smd
    qty: 15.0
    unit: each
  - item_id: voltage_regulator_ic
    qty: 1.0
    unit: each
  - item_id: crystal_oscillator_timing
    qty: 1.0
    unit: each
  - item_id: connector_pin_header
    qty: 4.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_paste_applied` not found

This item doesn't exist in the KB.

#### Problem: Item `microcontroller_ic_generic` not found

This item doesn't exist in the KB.

#### Problem: Item `capacitor_ceramic_generic` not found

This item doesn't exist in the KB.

#### Problem: Item `resistor_chip_smd` not found

This item doesn't exist in the KB.

#### Problem: Item `voltage_regulator_ic` not found

This item doesn't exist in the KB.

#### Problem: Item `crystal_oscillator_timing` not found

This item doesn't exist in the KB.

#### Problem: Item `connector_pin_header` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_microcontroller_or_embedded_board_v0.yaml`
- **BOM available:** No
