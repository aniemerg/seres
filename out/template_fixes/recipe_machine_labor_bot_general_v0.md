# Fix Intelligence: recipe_machine_labor_bot_general_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_labor_bot_general_v0.yaml`
- **Target item:** `labor_bot_general_v0`
  - File: `kb/items/labor_bot_general_v0.yaml`
- **BOM:** `kb/boms/bom_labor_bot_general_v0.yaml` ✓
  - Components: 33
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 33 components:

- `machine_frame_small` (qty: 1 None)
- `robot_arm_link_aluminum` (qty: 1 None)
- `robot_arm_link_aluminum` (qty: 1 None)
- `robot_wrist_3axis` (qty: 1 None)
- `motor_housing_cast` (qty: 6 None)
- `motor_electric_medium` (qty: 3 None)
- `motor_electric_medium` (qty: 1 None)
- `motor_electric_small` (qty: 2 None)
- `harmonic_drive_reducer_medium` (qty: 3 None)
- `harmonic_drive_reducer_medium` (qty: 3 None)
- `power_supply_small_imported` (qty: 1 None)
- `power_distribution_board` (qty: 1 None)
- `battery_backup_small` (qty: 1 None)
- `computer_core_imported` (qty: 1 None)
- `servo_drive_controller` (qty: 6 None)
- `safety_controller_plc` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `force_torque_sensor_6axis` (qty: 1 None)
- `touch_sensor_capacitive` (qty: 2 None)
- `proximity_sensor_inductive` (qty: 4 None)
- `instrument_mounts_basic` (qty: 1 None)
- `led_ring_light` (qty: 2 None)
- `electric_parallel_gripper` (qty: 1 None)
- `stepper_motor_precision` (qty: 1 None)
- `quick_change_tool_interface` (qty: 1 None)
- `assembled_cable_harness` (qty: 6 None)
- `assembled_cable_harness` (qty: 1 None)
- `cable_drag_chain` (qty: 2 None)
- `electrical_wire_and_connectors` (qty: 1 None)
- `thermal_management_system` (qty: 1 None)
- `control_components` (qty: 1 None)
- `safety_light_curtain` (qty: 1 None)
- `protective_cover_set` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: robot_arm_link_aluminum
    qty: 1
    unit: None
  - item_id: robot_arm_link_aluminum
    qty: 1
    unit: None
  - item_id: robot_wrist_3axis
    qty: 1
    unit: None
  - item_id: motor_housing_cast
    qty: 6
    unit: None
  - item_id: motor_electric_medium
    qty: 3
    unit: None
  - item_id: motor_electric_medium
    qty: 1
    unit: None
  - item_id: motor_electric_small
    qty: 2
    unit: None
  - item_id: harmonic_drive_reducer_medium
    qty: 3
    unit: None
  - item_id: harmonic_drive_reducer_medium
    qty: 3
    unit: None
  - item_id: power_supply_small_imported
    qty: 1
    unit: None
  - item_id: power_distribution_board
    qty: 1
    unit: None
  - item_id: battery_backup_small
    qty: 1
    unit: None
  - item_id: computer_core_imported
    qty: 1
    unit: None
  - item_id: servo_drive_controller
    qty: 6
    unit: None
  - item_id: safety_controller_plc
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: force_torque_sensor_6axis
    qty: 1
    unit: None
  - item_id: touch_sensor_capacitive
    qty: 2
    unit: None
  - item_id: proximity_sensor_inductive
    qty: 4
    unit: None
  - item_id: instrument_mounts_basic
    qty: 1
    unit: None
  - item_id: led_ring_light
    qty: 2
    unit: None
  - item_id: electric_parallel_gripper
    qty: 1
    unit: None
  - item_id: stepper_motor_precision
    qty: 1
    unit: None
  - item_id: quick_change_tool_interface
    qty: 1
    unit: None
  - item_id: assembled_cable_harness
    qty: 6
    unit: None
  - item_id: assembled_cable_harness
    qty: 1
    unit: None
  - item_id: cable_drag_chain
    qty: 2
    unit: None
  - item_id: electrical_wire_and_connectors
    qty: 1
    unit: None
  - item_id: thermal_management_system
    qty: 1
    unit: None
  - item_id: control_components
    qty: 1
    unit: None
  - item_id: safety_light_curtain
    qty: 1
    unit: None
  - item_id: protective_cover_set
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machine_labor_bot_general_v0.yaml`
- **BOM available:** Yes (33 components)
