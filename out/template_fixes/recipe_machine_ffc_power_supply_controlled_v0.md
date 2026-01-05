# Fix Intelligence: recipe_machine_ffc_power_supply_controlled_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_ffc_power_supply_controlled_v0.yaml`
- **Target item:** `ffc_power_supply_controlled_v0`
  - File: `kb/items/ffc_power_supply_controlled_v0.yaml`
- **BOM:** `kb/boms/bom_ffc_power_supply_controlled_v0.yaml` ✓
  - Components: 10
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_process_general_v0') requires input 'voltage_regulation_circuit_v0' which is not available

**Location:** Step 0
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: transformer_step_down_high_current
    qty: 80.0
    unit: kg
  - item_id: rectifier_bridge_heavy_duty
    qty: 15.0
    unit: kg
  - item_id: capacitor_bank_filter
    qty: 20.0
    unit: kg
  - item_id: voltage_regulation_circuit_v0
    qty: 5.0
    unit: kg
  - item_id: current_sensing_circuit
    qty: 2.0
    unit: kg
  - item_id: electrical_cabinet
    qty: 50.0
    unit: kg
  - item_id: cooling_fan_assembly
    qty: 5.0
    unit: kg
  - item_id: wire_copper_insulated
    qty: 10.0
    unit: kg
  - item_id: control_circuit_board_power
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `transformer_step_down_high_current` not found

This item doesn't exist in the KB.

#### Problem: Item `rectifier_bridge_heavy_duty` not found

This item doesn't exist in the KB.

#### Problem: Item `capacitor_bank_filter` not found

This item doesn't exist in the KB.

#### Problem: Item `voltage_regulation_circuit_v0` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `current_sensing_circuit` not found

This item doesn't exist in the KB.

#### Problem: Item `electrical_cabinet` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `cooling_fan_assembly` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

#### Problem: Item `control_circuit_board_power` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electrical_testing_and_calibration_v0') requires input 'ffc_power_supply_assembled' which is not available

**Location:** Step 1
**Process:** `electrical_testing_and_calibration_v0`
  - File: `kb/processes/electrical_testing_and_calibration_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_testing_and_calibration_v0
  inputs:
  - item_id: ffc_power_supply_assembled
    qty: 180.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `ffc_power_supply_assembled` not found

This item doesn't exist in the KB.

**Suggestions:**
1. Check if item name is misspelled
2. Add item to BOM if it should be a component
3. Replace with an output from a previous step

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_machine_ffc_power_supply_controlled_v0.yaml`
- **BOM available:** Yes (10 components)
