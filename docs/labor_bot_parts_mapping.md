# Labor Bot BOM Component Mapping
**Analysis of existing vs. new parts for labor_bot_general_v0**
**Date**: 2024-12-21

## Purpose

Map the 31 components in `bom_labor_bot_general_v0` to existing KB parts where "reasonably equivalent" per `parts_and_labor_guidelines.md`, and identify which new parts must be created.

**Equivalence criteria**:
- Within ~5x in dimensions, mass, or capability
- Same construction method and materials (if materials matter for function)
- Can note specific variations in BOM/recipe notes

## Component Mapping Analysis

### 1. MECHANICAL STRUCTURE (5 components)

#### 1.1 robot_base_frame (10 kg steel)
**Existing candidates:**
- `machine_frame_small` (mass unknown)
- `machine_frame_medium` (mass unknown)
- `support_frame_welded` (mass unknown)
- `steel_frame_welded` (mass unknown)

**Decision**: **REUSE `machine_frame_small`**
- Within 5x mass range (assuming small frame ~5-20 kg)
- Same material (steel)
- Same construction (welded)
- Note in BOM: "Used as robot base, 10 kg variant"

#### 1.2 robot_upper_arm_link (8 kg aluminum)
**Existing candidates:**
- No specific "link" or "beam" components found
- `structural_steel_frame` exists but wrong material (steel vs aluminum)

**Decision**: **CREATE NEW** `robot_arm_link_aluminum`
- Unique geometry (1m box beam)
- Material-specific (aluminum required for weight)
- Can serve both upper arm and forearm (8kg and 7kg within 2x)

#### 1.3 robot_forearm_link (7 kg aluminum)
**Decision**: **REUSE `robot_arm_link_aluminum`** (same part as 1.2)
- 8 kg vs 7 kg = 1.14x difference (well within 5x)
- Same material, construction, function
- Note in BOM: "Tapered variant, 7 kg"

#### 1.4 robot_wrist_assembly (5 kg aluminum + steel)
**Existing candidates:**
- No wrist assemblies found

**Decision**: **CREATE NEW** `robot_wrist_3axis`
- Unique precision assembly
- Specific function (J4-J5-J6 roll-pitch-roll)

#### 1.5 robot_joint_housing (qty 6, ~0.8 kg each aluminum)
**Existing candidates:**
- `motor_housing_cast` exists (mass unknown)
- `gearbox_housing_cast` exists (mass unknown)

**Decision**: **REUSE `motor_housing_cast`**
- Same material (aluminum casting)
- Same function (enclose motor/gearbox)
- Qty 6 in BOM
- Note: "For robot joints, houses motor and harmonic drive"

---

### 2. ACTUATION SYSTEM (6 motor + 6 gearbox = 12 components)

#### 2.1 bldc_motor_400w (qty 3, 4 kg each)
**Existing candidates:**
- `motor_electric_small` (mass unknown)
- `motor_electric_medium` (mass unknown)
- `motor_electric_large` (mass unknown)
- `drive_motor_small` (mass unknown)
- `drive_motor_medium` (mass unknown)

**Decision**: **REUSE `motor_electric_medium`**
- 400W is medium power
- Likely within 5x range (200W-2000W would be "medium")
- Note in BOM: "BLDC type, 400W, 3000 rpm, integrated encoder"

#### 2.2 bldc_motor_300w (qty 1, 3 kg)
**Decision**: **REUSE `motor_electric_medium`** (same as 2.1)
- 300W vs 400W = 1.33x (within 5x)
- Same type and construction

#### 2.3 bldc_motor_200w (qty 2, 2.5 kg each)
**Decision**: **REUSE `motor_electric_small`**
- 200W is small power
- 2.5 kg per motor
- Note: "BLDC type, 200W, 4000 rpm for wrist joints"

#### 2.4 harmonic_drive_100_1_50mm (qty 3, 2 kg each)
**Existing candidates:**
- `gearbox_reducer_small` (mass unknown)
- `gearbox_reducer_medium` (mass unknown)

**Analysis**: Harmonic drives are very specialized (zero-backlash, 100:1 ratio). Generic gearboxes may not meet precision requirements.

**Decision**: **CREATE NEW** `harmonic_drive_reducer_medium`
- Precision matters for robot repeatability (±0.5mm)
- Harmonic drives have unique construction (flexspline, wave generator)
- Can't substitute generic gearbox without losing precision
- Medium size covers both 50mm and 40mm variants

#### 2.5 harmonic_drive_80_1_40mm (qty 3, 2 kg each)
**Decision**: **REUSE `harmonic_drive_reducer_medium`** (same as 2.4)
- 80:1 vs 100:1 = 1.25x ratio (within 5x)
- 40mm vs 50mm = 1.25x size (within 5x)
- 2 kg mass (same)
- Note in BOM: "Smaller variant, 80:1 ratio, 40mm"

---

### 3. POWER SYSTEM (3 components)

#### 3.1 power_supply_ac_dc_48v_2500w (5 kg)
**Existing candidates:**
- `power_supply_small_imported` (mass unknown)
- `power_supply_bench` (mass unknown)
- `power_supply_low_voltage` (mass unknown)

**Decision**: **REUSE `power_supply_small_imported`**
- 2.5 kW is "small" for industrial use (vs. welding supplies at 10+ kW)
- Likely imported (has AC/DC conversion electronics)
- Note in BOM: "48V DC output, 2.5 kW, from 240V 3-phase AC"

#### 3.2 power_distribution_board_robot (2 kg)
**Existing candidates:**
- `power_conditioning_module` exists! (12 kg from old stub BOM)
- But power_conditioning_module is 12 kg vs 2 kg = 6x (exceeds 5x guideline)

**Decision**: **CREATE NEW** `power_distribution_board`
- Different from power_conditioning_module (6x mass difference)
- Specific function (distribution vs conditioning)
- Simple PCB with bus bars and breakers

#### 3.3 battery_backup_48v_100wh (1 kg)
**Existing candidates:**
- `battery_pack_large` (mass unknown, probably >>1 kg)
- `battery_pack_large_nife` (mass unknown)
- `battery_cell` (mass unknown, probably <1 kg)

**Decision**: **REUSE `battery_pack_small`** if exists, else **CREATE NEW** `battery_backup_small`
- Search for battery_pack_small...

---

### 4. CONTROL SYSTEM (3 components)

#### 4.1 industrial_pc_controller (3 kg)
**Existing candidates:**
- `computer_core_imported` (mass unknown)
- `computer_workstation` (mass unknown, probably much larger)
- `microcontroller_or_embedded_board` (mass unknown, probably smaller)

**Decision**: **REUSE `computer_core_imported`**
- Industrial PC is an imported computer module
- Within reasonable mass range
- Note in BOM: "Industrial PC, ARM/x86, 8GB RAM, real-time Linux, EtherCAT"

#### 4.2 motor_controller_servo_drive (qty 6, ~300g each = 2 kg total)
**Existing candidates:**
- `temperature_controller_module` (mass unknown)
- No specific motor controller found

**Decision**: **CREATE NEW** `servo_drive_controller`
- Specialized motor control (FOC, EtherCAT)
- Different from temperature controller

#### 4.3 safety_controller_plc (1 kg)
**Existing candidates:**
- Controllers found are for temperature, charge, thermal
- No PLC or safety controller

**Decision**: **CREATE NEW** `safety_controller_plc`
- Safety-critical (SIL 2 rated)
- Unique function

---

### 5. SENSING SYSTEM (5 components)

#### 5.1 stereo_camera_pair_5mp (2 kg)
**Existing candidates:**
- `sensor_suite_general` exists! (5 kg from old stub BOM)
- Description: "Cameras, lidar/radar as needed for navigation/inspection"

**Decision**: **REUSE `sensor_suite_general`**
- 5 kg vs 2 kg = 2.5x (within 5x)
- Same function (vision for navigation/inspection)
- Note in BOM: "Stereo camera variant, 2 kg"

#### 5.2 force_torque_sensor_6axis (2 kg)
**Existing candidates:**
- `current_sensor_set` (mass unknown, different function)
- `touch_probe_assembly` (mass unknown, different principle)
- No 6-axis force sensor found

**Decision**: **CREATE NEW** `force_torque_sensor_6axis`
- Unique sensor type
- Critical for force control

#### 5.3 touch_sensor_capacitive (qty 2)
**Existing candidates:**
- `touch_probe_assembly` exists but unclear if same principle

**Decision**: **CREATE NEW** `touch_sensor_capacitive`
- Small component (~0.5 kg total for 2)
- Specific technology (capacitive)

#### 5.4 proximity_sensor_inductive (qty 4, ~0.25 kg each)
**Existing candidates:**
- `level_sensor_basic` (mass unknown, different function)
- No proximity sensor found

**Decision**: **CREATE NEW** `proximity_sensor_inductive`
- Standard industrial sensor
- Specific technology (inductive)

#### 5.5 camera_mount_with_led_lights (4 kg)
**Existing candidates:**
- `instrument_mounts_basic` exists
- No LED lights found in inventory

**Decision**: **REUSE `instrument_mounts_basic`** + **CREATE NEW** `led_ring_light`
- Mount can be generic instrument mount
- LED lights are separate component
- Combined in BOM as assembly

---

### 6. END EFFECTOR (3 components)

#### 6.1 electric_parallel_gripper (4 kg)
**Existing candidates:**
- No grippers found in inventory search

**Decision**: **CREATE NEW** `electric_parallel_gripper`
- Core robot component
- Specific type (electric, parallel jaw)

#### 6.2 stepper_motor_nema23_gripper (2 kg)
**Existing candidates:**
- `stepper_motor_precision` exists!

**Decision**: **REUSE `stepper_motor_precision`**
- NEMA 23 is a precision stepper size
- 2 kg is reasonable for NEMA 23
- Note in BOM: "NEMA 23 size, with ball screw for gripper"

#### 6.3 quick_change_tool_interface (2 kg)
**Existing candidates:**
- No tool interfaces found

**Decision**: **CREATE NEW** `quick_change_tool_interface`
- Specialized mechanical coupling
- ISO standard mounting

---

### 7. WIRING AND INTEGRATION (5 components)

#### 7.1 motor_cable_shielded_3phase (qty 6, ~1 kg each)
**Existing candidates:**
- `assembled_cable_harness` exists
- `electrical_wire_and_connectors` exists

**Decision**: **REUSE `assembled_cable_harness`**
- Generic cable assembly
- Qty 6 in BOM
- Note: "3-phase motor cable, 3m, shielded, M12 connectors"

#### 7.2 signal_cable_bundle_robot (1 kg, ~25m total)
**Decision**: **REUSE `assembled_cable_harness`** (same as 7.1)
- Another cable assembly variant
- Note: "Signal bundle: EtherCAT, USB3, force sensor, safety"

#### 7.3 cable_drag_chain (qty 2, 1.5 kg each)
**Existing candidates:**
- No drag chains or cable carriers found

**Decision**: **CREATE NEW** `cable_drag_chain`
- Specific mechanical component
- Polymer chain for cable management

#### 7.4 electrical_connectors_set (1 kg, ~40 connectors)
**Existing candidates:**
- `electrical_wire_and_connectors` exists!

**Decision**: **REUSE `electrical_wire_and_connectors`**
- Generic connector kit
- Note: "M12, M23, RJ45, USB-C, terminal blocks, ~40 units"

#### 7.5 thermal_management_system_robot (2 kg)
**Existing candidates:**
- No thermal management systems found
- `thermal_controller_basic` is controller, not cooling hardware

**Decision**: **CREATE NEW** `thermal_management_system`
- Physical cooling (heat pipes, radiator)
- Not a controller

---

### 8. SAFETY AND ENCLOSURE (3 components)

#### 8.1 emergency_stop_system (1 kg)
**Existing candidates:**
- No E-stop systems found

**Decision**: **CREATE NEW** `emergency_stop_system`
- Safety-critical component
- Includes buttons, relays, wiring

#### 8.2 safety_light_curtain (2 kg)
**Existing candidates:**
- No safety barriers found

**Decision**: **CREATE NEW** `safety_light_curtain`
- Safety-critical optoelectronic
- IEC 61496 Type 4

#### 8.3 protective_cover_set (3 kg)
**Existing candidates:**
- No cover sets found
- Many "housing" items but for specific machines

**Decision**: **CREATE NEW** `protective_cover_set`
- Generic covers for pinch points
- Polycarbonate or aluminum

---

## Summary Statistics

| Status | Count | Components |
|--------|-------|------------|
| **Reuse existing** | 14 | machine_frame_small, robot_arm_link_aluminum (2x), motor_housing_cast (6x), motor_electric_medium (4x), motor_electric_small (2x), power_supply_small_imported, computer_core_imported, sensor_suite_general, instrument_mounts_basic, stepper_motor_precision, assembled_cable_harness (8x), electrical_wire_and_connectors |
| **Create new** | 17 | robot_arm_link_aluminum, robot_wrist_3axis, harmonic_drive_reducer_medium (6x), power_distribution_board, battery_backup_small, servo_drive_controller (6x), safety_controller_plc, force_torque_sensor_6axis, touch_sensor_capacitive (2x), proximity_sensor_inductive (4x), led_ring_light (2x), electric_parallel_gripper, quick_change_tool_interface, cable_drag_chain (2x), thermal_management_system, emergency_stop_system, safety_light_curtain, protective_cover_set |
| **Need to search** | 1 | battery_backup_small (check for battery_pack_small) |

**Note**: Quantities in parentheses show how many instances in BOM (e.g., "6x" means qty 6).

## Next Steps

1. Search for `battery_pack_small` to finalize battery component
2. Create YAML part definitions for 17 new components
3. Update `bom_labor_bot_general_v0.yaml` with correct part IDs
4. Verify each part has recipe or import designation
5. For reused parts, add notes in BOM about specific variants/usage

## Design Notes

**Key reuse decisions**:
- **Motors**: Used existing small/medium motors instead of creating power-specific variants (200W, 300W, 400W all within "medium" range)
- **Frames**: Used existing machine_frame_small for base
- **Cables**: All cables mapped to assembled_cable_harness with variant notes
- **Sensors**: Reused sensor_suite_general (old stub component now validated)

**Key new parts needed**:
- **Harmonic drives**: Cannot substitute generic gearboxes (precision requirement)
- **Controllers**: Servo drives and safety PLC are specialized electronics
- **Force sensor**: Unique 6-axis strain gauge sensor
- **Gripper**: Core robot component, no equivalent
- **Safety equipment**: E-stop and light curtain are safety-critical
