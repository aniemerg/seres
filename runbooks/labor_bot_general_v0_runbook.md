# Labor Bot General v0 Runbook

Goal: build `labor_bot_general_v0` using in-situ resources where possible. Start by importing
all final parts for a baseline assembly, then attempt local production of each part
and subassembly.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: labor_bot_general_v0_runbook
- cmd: sim.reset
  args:
    sim-id: labor_bot_general_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting labor_bot_general_v0 runbook."
```

## Baseline import + assembly

Commentary: import all BOM parts to ensure the labor bot can be assembled once, then
run the assembly recipe as a baseline.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment needed for assembly."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Import all BOM parts for baseline labor_bot_general_v0 assembly."

# ===== MECHANICAL STRUCTURE (35 kg) =====
- cmd: sim.import
  args:
    item: machine_frame_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: robot_arm_link_aluminum
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: robot_wrist_3axis
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_housing_cast
    quantity: 6
    unit: unit
    ensure: true

# ===== ACTUATION SYSTEM (30 kg) =====
- cmd: sim.import
  args:
    item: motor_electric_medium
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: harmonic_drive_reducer_medium
    quantity: 6
    unit: unit
    ensure: true

# ===== POWER SYSTEM (8 kg) =====
- cmd: sim.import
  args:
    item: power_supply_small_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_distribution_board
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: battery_backup_small
    quantity: 1
    unit: unit
    ensure: true

# ===== CONTROL SYSTEM (6 kg) =====
- cmd: sim.import
  args:
    item: computer_core_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: servo_drive_controller
    quantity: 6
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: safety_controller_plc
    quantity: 1
    unit: unit
    ensure: true

# ===== SENSING SYSTEM (12 kg) =====
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: force_torque_sensor_6axis
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: touch_sensor_capacitive
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: proximity_sensor_inductive
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: instrument_mounts_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: led_ring_light
    quantity: 2
    unit: unit
    ensure: true

# ===== END EFFECTOR (8 kg) =====
- cmd: sim.import
  args:
    item: electric_parallel_gripper
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: stepper_motor_precision
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: quick_change_tool_interface
    quantity: 1
    unit: unit
    ensure: true

# ===== WIRING AND INTEGRATION (15 kg) =====
- cmd: sim.import
  args:
    item: assembled_cable_harness
    quantity: 7
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cable_drag_chain
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: thermal_management_system
    quantity: 1
    unit: unit
    ensure: true

# ===== SAFETY AND ENCLOSURE (6 kg) =====
- cmd: sim.import
  args:
    item: control_components
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: safety_light_curtain
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: protective_cover_set
    quantity: 1
    unit: unit
    ensure: true

- cmd: sim.note
  args:
    style: info
    message: "Baseline: imported all labor_bot_general_v0 BOM parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_labor_bot_general_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "Baseline labor_bot_general_v0 assembly complete."
```

## In-situ equipment + core feedstocks

Commentary: import the minimum tooling and seed materials to allow local production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment and starter feedstocks for local production."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drilling_equipment_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heliostat_array_system_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: rock_crusher_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibrating_screen_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: dust_collection_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ball_mill_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mre_reactor_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: high_temperature_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrodes
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: reduction_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: metal_shear_or_saw
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fixturing_workbench
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cutting_tools_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrolysis_cell_unit_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_drawing_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: welding_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: welding_consumables
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coil_winding_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Core equipment imported."
```

## In-situ: Regolith mining and alumina extraction

Commentary: mine highland regolith and extract alumina for aluminum production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Mine highland regolith and extract alumina."
- cmd: sim.import
  args:
    item: chemical_reactor_heated_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydrochloric_acid
    quantity: 1500
    unit: kg
    ensure: true
- cmd: sim.start-process
  args:
    process: regolith_mining_highlands_v0
    output_quantity: 500
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.start-process
  args:
    process: alumina_extraction_from_highlands_v0
    output_quantity: 60
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.note
  args:
    style: info
    message: "Alumina extraction complete."
```

## In-situ: Aluminum ingot and wire production

Commentary: produce aluminum ingots and wire from alumina via Hall-Heroult electrolysis.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce aluminum ingots and wire."
- cmd: sim.import
  args:
    item: carbon_anode
    quantity: 60
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cryolite_flux
    quantity: 15
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: info
    message: "Aluminum ingots and wire produced."
```

## In-situ: Metal alloy bulk production from regolith (MRE)

Commentary: produce metal_alloy_bulk from mare regolith via molten regolith electrolysis (MRE).
This is the key to maximizing in situ production - making structural metals from lunar resources.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce metal_alloy_bulk from regolith via MRE."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 14000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Running metal_alloy_bulk production (~35 batches for 800 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 35
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: info
    message: "Waiting for all MRE batches to complete."
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: success
    message: "Metal alloy bulk production complete from lunar regolith."
```

## In-situ: Steel production from regolith

Commentary: produce steel from regolith ilmenite via iron smelting and refining.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel from regolith ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Mining additional mare regolith for steel production (300 kg needed)."
- cmd: sim.import
  args:
    item: carbon_reductant
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    output_quantity: 350
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 210
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 63
- cmd: sim.advance-time
  args:
    hours: 260
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Steel production complete from lunar ilmenite."
```

## In-situ: Mechanical structure parts

Commentary: produce robot arm links, frame, and motor housings from locally-produced aluminum and metal alloys.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce mechanical structure parts from local metals."
- cmd: sim.run-recipe
  args:
    recipe: recipe_robot_arm_link_aluminum_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_housing_cast_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: info
    message: "Mechanical structure parts complete."
```

## In-situ: Motors (partial - needs imported subcomponents)

Commentary: attempt motor production with available materials; will need to import specialized subcomponents.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Attempt motor production (partial in-situ)."
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cooling_fan_assembly
    quantity: 35
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_electric_medium_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 65
- cmd: sim.note
  args:
    style: warning
    message: "Motors produced with imported bearings and cooling fans. Motor_electric_small still needs import."
- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 2
    unit: unit
    ensure: true
```

## In-situ: Remaining imported parts

Commentary: import specialized electronics, sensors, and subassemblies not yet modeled for in-situ production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining specialized components."
- cmd: sim.import
  args:
    item: robot_wrist_3axis
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: harmonic_drive_reducer_medium
    quantity: 6
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_small_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_distribution_board
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: battery_backup_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: computer_core_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: servo_drive_controller
    quantity: 6
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: safety_controller_plc
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: force_torque_sensor_6axis
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: touch_sensor_capacitive
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: proximity_sensor_inductive
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: instrument_mounts_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: led_ring_light
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electric_parallel_gripper
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: stepper_motor_precision
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: quick_change_tool_interface
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembled_cable_harness
    quantity: 7
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cable_drag_chain
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: thermal_management_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_components
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: safety_light_curtain
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: protective_cover_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Specialized components imported."
```

## Final assembly from local + imported parts

Commentary: assemble labor_bot_general_v0 using mix of locally produced and imported parts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble labor_bot_general_v0 from locally produced and imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_labor_bot_general_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "labor_bot_general_v0 assembly complete with partial in-situ production."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
