# Fix Intelligence: recipe_gas_flow_controller_v0

## Files

- **Recipe:** `kb/recipes/recipe_gas_flow_controller_v0.yaml`
- **Target item:** `gas_flow_controller`
  - File: `kb/items/gas_flow_controller.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sealing_and_assembly_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 1
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 5.0
    unit: kg
  - item_id: valve_solenoid
    qty: 1.0
    unit: unit
  - item_id: valve_needle_precision
    qty: 1.0
    unit: unit
  - item_id: sensor_suite_general
    qty: 1.0
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1.0
    unit: unit
  - item_id: fittings_and_valves
    qty: 1.0
    unit: unit
  - item_id: power_output_terminals
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_solenoid` not found

This item doesn't exist in the KB.

#### Problem: Item `valve_needle_precision` not found

This item doesn't exist in the KB.

#### Problem: Item `sensor_suite_general` not found

This item doesn't exist in the KB.

#### Problem: Item `control_compute_module_imported` not found

This item doesn't exist in the KB.

#### Problem: Item `fittings_and_valves` not found

This item doesn't exist in the KB.

#### Problem: Item `power_output_terminals` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'calibration_and_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `calibration_and_test_basic_v0`
  - File: `kb/processes/calibration_and_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_and_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `gas_flow_controller` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_gas_flow_controller_v0.yaml`
- **BOM available:** No
