# Fix Intelligence: recipe_ffc_power_supply_assembled_v0

## Files

- **Recipe:** `kb/recipes/recipe_ffc_power_supply_assembled_v0.yaml`
- **Target item:** `ffc_power_supply_assembled`
  - File: `kb/items/ffc_power_supply_assembled.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_process_general_v0') requires input 'transformer_step_down_high_current' which is not available

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

#### Problem: Item `current_sensing_circuit` not found

This item doesn't exist in the KB.

#### Problem: Item `electrical_cabinet` not found

This item doesn't exist in the KB.

#### Problem: Item `cooling_fan_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `control_circuit_board_power` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ffc_power_supply_assembled_v0.yaml`
- **BOM available:** No
