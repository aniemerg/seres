# Power Hammer or Press Runbook

This runbook builds a power_hammer_or_press using as many in situ resources as possible.

## Overview

| Phase | Goal |
| --- | --- |
| Setup | Create a clean sim and import basic equipment |
| Bootstrap | Mine regolith and produce basic metals |
| Steel Production | Produce steel materials for structural components |
| Motor Components | Build aluminum wire and motor components |
| Fasteners | Manufacture fastener kit from steel stock |
| Hammer Components | Build frame, head, and anvil from metals |
| Final Assembly | Import electronics and assemble power hammer |
| Check | Verify the build succeeded |

## Setup

Commentary: reset the sim and import basic mining/processing equipment.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: power_hammer_insitu_v0
- cmd: sim.reset
  args:
    sim-id: power_hammer_insitu_v0
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting in situ power hammer build."
```

Commentary: import basic equipment for mining and processing.

```sim-runbook
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: reduction_furnace_v0
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
    item: casting_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sand_casting_flask_set
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
    item: rock_crusher_basic
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
    item: mre_reactor_v0
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
    item: high_temperature_power_supply_v0
    quantity: 1
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
    item: forge_or_induction_heater_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_furnace
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
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: quench_tank
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_grinder
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: grinding_wheels
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
    item: rolling_mill_v0
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
    item: rolling_mill_or_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 500
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Basic equipment imported."
```

## Bootstrap: Regolith Mining and Metal Production

Commentary: mine regolith for iron extraction and metal alloy bulk for components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Mining regolith for iron extraction and metals."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 40
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: info
    message: "Regolith mining complete."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 28
- cmd: sim.note
  args:
    style: info
    message: "Metal alloy bulk produced."
```

## Steel Production

Commentary: mine additional regolith and produce steel materials for frame using in situ iron ore from regolith.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Mining additional regolith for iron extraction."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: info
    message: "Extracting ilmenite from regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 480
- cmd: sim.advance-time
  args:
    hours: 560
- cmd: sim.note
  args:
    style: info
    message: "Ilmenite extracted. Producing carbon reducing agent."
- cmd: sim.import
  args:
    item: carbon_reductant
    quantity: 72
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 72
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Producing iron pig ingot from ilmenite."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 144
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: info
    message: "Producing steel ingot from iron pig."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 137
- cmd: sim.advance-time
  args:
    hours: 430
- cmd: sim.note
  args:
    style: info
    message: "Producing steel plate for frame."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 130
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: info
    message: "Steel plate ready."
```

## Motor Components: Aluminum Wire

Commentary: produce aluminum wire for motor windings.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Producing aluminum wire for motor."
- cmd: sim.import
  args:
    item: alumina_powder
    quantity: 6
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_anode
    quantity: 1.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cryolite_flux
    quantity: 0.5
    unit: kg
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: info
    message: "Aluminum wire produced."
```

## Motor Components: Coil Insulation

Commentary: produce coil insulation material from silicon.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Producing coil insulation."
- cmd: sim.import
  args:
    item: silicon_purified
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: silicon_metal_v0
    quantity: 1.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: generic_chemical_reactor_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_unit_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_powder_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_precursor_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_polymer_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_coil_insulation_material_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
```

## Motor Components: Bearings

Commentary: produce bearing set from metal alloy.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Producing bearings for motor."
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_bearing_set_small_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 8
```

## Fasteners

Commentary: import fasteners since they require forging (circular dependency).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Importing fasteners (circular dependency - they require power hammer to forge)."
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Fasteners imported."
```

## Hammer Components

Commentary: build frame, head, and anvil sequentially to avoid machine conflicts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Building hammer frame."
- cmd: sim.run-recipe
  args:
    recipe: recipe_hammer_frame_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: milestone
    message: "Producing additional regolith_metal_crude for hammer head."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 28
- cmd: sim.note
  args:
    style: milestone
    message: "Building hammer head."
- cmd: sim.run-recipe
  args:
    recipe: recipe_hammer_head_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: milestone
    message: "Building anvil block."
- cmd: sim.note
  args:
    style: milestone
    message: "Producing additional regolith_metal_crude for anvil block."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 56
- cmd: sim.run-recipe
  args:
    recipe: recipe_anvil_block_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
```

## Motor Assembly

Commentary: assemble the hammer drive motor.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assembling hammer drive motor."
- cmd: sim.import
  args:
    item: assembled_equipment
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_hammer_drive_motor_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
```

## Final Assembly

Commentary: import electronics that can't be made locally and assemble the power hammer.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Importing electronics and assembling power hammer."
- cmd: sim.import
  args:
    item: control_compute_module_imported
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
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Waiting for all recipes to complete."
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.build-machine
  args:
    machine: power_hammer_or_press
    quantity: 1
- cmd: sim.note
  args:
    style: success
    message: "Power hammer build complete!"
```

## Checkpoint

Commentary: verify the final state.

```sim-runbook
- cmd: sim.status
  args: {}
```
