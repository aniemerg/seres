# Fix Intelligence: recipe_traction_control_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_traction_control_system_v0.yaml`
- **Target item:** `traction_control_system_v0`
  - File: `kb/items/traction_control_system_v0.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'software_development_programming_v0') requires input 'computing_time_development' which is not available

**Location:** Step 0
**Process:** `software_development_programming_v0`
  - File: `kb/processes/software_development_programming_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: software_development_programming_v0
  inputs:
  - item_id: computing_time_development
    qty: 80.0
    unit: hr
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `computing_time_development` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'pcb_fabrication_process_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 1
**Process:** `pcb_fabrication_process_v0`
  - File: `kb/processes/pcb_fabrication_process_v0.yaml`

**Current step:**
```yaml
- process_id: pcb_fabrication_process_v0
  inputs:
  - item_id: copper_clad_laminate
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `copper_clad_laminate` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'component_placement_process_v0') requires input 'control_board_bare' which is not available

**Location:** Step 2
**Process:** `component_placement_process_v0`
  - File: `kb/processes/component_placement_process_v0.yaml`

**Current step:**
```yaml
- process_id: component_placement_process_v0
  inputs:
  - item_id: control_board_bare
    qty: 0.18
    unit: kg
  - item_id: microcontroller_ic_generic
    qty: 1.0
    unit: each
  - item_id: motor_driver_ic_high_current
    qty: 4.0
    unit: each
  - item_id: current_sensor_set
    qty: 1.0
    unit: each
  - item_id: capacitor_ceramic_generic
    qty: 20.0
    unit: each
  - item_id: resistor_chip_smd
    qty: 30.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `control_board_bare` not found

This item doesn't exist in the KB.

#### Problem: Item `microcontroller_ic_generic` not found

This item doesn't exist in the KB.

#### Problem: Item `motor_driver_ic_high_current` not found

This item doesn't exist in the KB.

#### Problem: Item `current_sensor_set` not found

This item doesn't exist in the KB.

#### Problem: Item `capacitor_ceramic_generic` not found

This item doesn't exist in the KB.

#### Problem: Item `resistor_chip_smd` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'reflow_soldering_process_v0') requires input 'pcb_populated' which is not available

**Location:** Step 3
**Process:** `reflow_soldering_process_v0`
  - File: `kb/processes/reflow_soldering_process_v0.yaml`

**Current step:**
```yaml
- process_id: reflow_soldering_process_v0
  inputs:
  - item_id: pcb_populated
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'assembly_process_general_v0') requires input 'pcb_populated' which is not available

**Location:** Step 4
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: pcb_populated
    qty: 0.95
    unit: kg
  - item_id: traction_control_software
    qty: 1.0
    unit: each
  - item_id: encoder_optical_simple_v0
    qty: 4.0
    unit: each
  - item_id: power_cable_assembly
    qty: 2.0
    unit: kg
  - item_id: enclosure_steel_small
    qty: 1.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

#### Problem: Item `traction_control_software` not found

This item doesn't exist in the KB.

#### Problem: Item `encoder_optical_simple_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `power_cable_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `enclosure_steel_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_traction_control_system_v0.yaml`
- **BOM available:** No
