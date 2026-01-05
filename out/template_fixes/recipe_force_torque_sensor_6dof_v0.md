# Fix Intelligence: recipe_force_torque_sensor_6dof_v0

## Files

- **Recipe:** `kb/recipes/recipe_force_torque_sensor_6dof_v0.yaml`
- **Target item:** `force_torque_sensor_6dof_v0`
  - File: `kb/items/force_torque_sensor_6dof_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_milling_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `machining_process_milling_v0`
  - File: `kb/processes/machining_process_milling_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_milling_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'strain_gauge_bonding_process_v0') requires input 'compliant_element_machined' which is not available

**Location:** Step 1
**Process:** `strain_gauge_bonding_process_v0`
  - File: `kb/processes/strain_gauge_bonding_process_v0.yaml`

**Current step:**
```yaml
- process_id: strain_gauge_bonding_process_v0
  inputs:
  - item_id: compliant_element_machined
    qty: 1.0
    unit: kg
  - item_id: strain_gauge_foil_v0
    qty: 24.0
    unit: each
  - item_id: adhesive_cyanoacrylate
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `compliant_element_machined` not found

This item doesn't exist in the KB.

#### Problem: Item `strain_gauge_foil_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `adhesive_cyanoacrylate` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'electrical_wiring_assembly_v0') requires input 'sensor_element_with_gauges' which is not available

**Location:** Step 2
**Process:** `electrical_wiring_assembly_v0`
  - File: `kb/processes/electrical_wiring_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_assembly_v0
  inputs:
  - item_id: sensor_element_with_gauges
    qty: 1.1
    unit: kg
  - item_id: wire_copper_insulated
    qty: 0.1
    unit: kg
  - item_id: connector_electrical_multi_pin
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `sensor_element_with_gauges` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `connector_electrical_multi_pin` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_force_torque_sensor_6dof_v0.yaml`
- **BOM available:** No
