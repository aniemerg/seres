# Fix Intelligence: recipe_backprop_circuit_hardware_v0

## Files

- **Recipe:** `kb/recipes/recipe_backprop_circuit_hardware_v0.yaml`
- **Target item:** `backprop_circuit_hardware_v0`
  - File: `kb/items/backprop_circuit_hardware_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

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
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'component_placement_process_v0') requires input 'operational_amplifier_ic' which is not available

**Location:** Step 1
**Process:** `component_placement_process_v0`
  - File: `kb/processes/component_placement_process_v0.yaml`

**Current step:**
```yaml
- process_id: component_placement_process_v0
  inputs:
  - item_id: pcb_backprop_bare
    qty: 0.45
    unit: kg
  - item_id: operational_amplifier_ic
    qty: 20.0
    unit: each
  - item_id: analog_multiplier_ic
    qty: 10.0
    unit: each
  - item_id: capacitor_ceramic_generic
    qty: 50.0
    unit: each
  - item_id: resistor_chip_smd
    qty: 100.0
    unit: each
  - item_id: potentiometer_wirewound_v0
    qty: 20.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_backprop_bare` not found

This item doesn't exist in the KB.

#### Problem: Item `operational_amplifier_ic` not found

This item doesn't exist in the KB.

#### Problem: Item `analog_multiplier_ic` not found

This item doesn't exist in the KB.

#### Problem: Item `capacitor_ceramic_generic` not found

This item doesn't exist in the KB.

#### Problem: Item `resistor_chip_smd` not found

This item doesn't exist in the KB.

#### Problem: Item `potentiometer_wirewound_v0` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'soldering_process_wave_v0') requires input 'pcb_populated' which is not available

**Location:** Step 2
**Process:** `soldering_process_wave_v0`
  - File: `kb/processes/soldering_process_wave_v0.yaml`

**Current step:**
```yaml
- process_id: soldering_process_wave_v0
  inputs:
  - item_id: pcb_populated
    qty: 1.5
    unit: kg
  - item_id: solder_tin_lead
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

#### Problem: Item `solder_tin_lead` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'testing_and_calibration_circuit_v0') requires input 'pcb_assembled_board' which is not available

**Location:** Step 3
**Process:** `testing_and_calibration_circuit_v0`
  - File: `kb/processes/testing_and_calibration_circuit_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: testing_and_calibration_circuit_v0
  inputs:
  - item_id: pcb_assembled_board
    qty: 1.55
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_assembled_board` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_backprop_circuit_hardware_v0.yaml`
- **BOM available:** No
