# CNC Mill Runbook

Goal: build `cnc_mill` with baseline imports, then replace frame and shell with
regolith-derived metal to increase ISRU.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: cnc_mill_runbook
- cmd: sim.reset
  args:
    sim-id: cnc_mill_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting CNC mill runbook."
```

## Baseline import + assembly

Commentary: import all inputs and tooling to validate the recipe once.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline assembly with imported inputs."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_station
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
    item: cnc_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: structural_frame_steel
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mill_shell_generic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_medium
    quantity: 1
    unit: unit
    ensure: false
- cmd: sim.import
  args:
    item: gearbox_reducer_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cooling_loop_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coolant_pump_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_medium
    quantity: 0.01
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 1000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_cnc_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Baseline CNC mill assembly complete."
- cmd: sim.note
  args:
    style: milestone
    message: "Reset simulation for ISRU-focused build."
- cmd: sim.reset
  args:
    sim-id: cnc_mill_runbook
```

## ISRU: local frame + mill shell

Commentary: produce regolith_metal_crude, then cast/machine the structural frame and
cast the mill shell locally. Remaining components are imported for now.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import tooling for regolith metal production and casting."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_station
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
    item: cnc_mill
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
    item: crucible_refractory
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
    item: casting_mold_set
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
    item: casting_furnace_v0
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
    item: heating_furnace
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
    item: rolling_mill_v0
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
    item: wire_drawing_die_set
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
    item: stamping_press_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake_v0
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
    item: power_hammer_or_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: anvil_or_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lifting_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 26000
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 120
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: base_grease_stock_v0
    quantity: 1
    unit: kg
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for frame + mill shell."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 220
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_frame_steel_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_mill_shell_generic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Refine steel for gearbox components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_highlands_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 900
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 220
- cmd: sim.advance-time
  args:
    hours: 880
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_billet_or_slab_v0
    quantity: 70
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_raw_v0
    quantity: 65
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 170
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 170
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_metal_pure_v0
    quantity: 58
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_metal_from_regolith_carbothermic_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_steel_sheet_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_housing_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_shaft_steel_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_gearbox_housing_cast_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_gear_set_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_shaft_set_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_heavy_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 90
- cmd: sim.run-recipe
  args:
    recipe: recipe_lubrication_pack_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_gearbox_reducer_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_drive_motor_medium_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
```

## Final assembly (local frame + shell)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble CNC mill with local frame and shell."
- cmd: sim.import
  args:
    item: drive_motor_medium
    quantity: 1
    unit: unit
    ensure: false
- cmd: sim.import
  args:
    item: cooling_loop_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coolant_pump_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_cnc_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "cnc_mill local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
