# Rolling Mill v0 Runbook

Goal: Build `rolling_mill_v0` with maximum ISRU using regolith-derived metal.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: rolling_mill_v0_runbook
- cmd: sim.reset
  args:
    sim-id: rolling_mill_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting rolling mill v0 runbook."
```

## Stage 1: Baseline (import all components)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import equipment and components for baseline assembly."
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
    item: fixturing_workbench
    quantity: 1
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
    item: steel_drum
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: motor_assembly
    quantity: 12
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: grinding_media_steel
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble rolling mill from imported components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_rolling_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Baseline rolling mill v0 complete."
```

## Stage 2: ISRU Production

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for local components."
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
    item: electrical_energy
    quantity: 12000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 350
- cmd: sim.note
  args:
    style: info
    message: "Build bearing_set from local metal_alloy_bulk."
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
    item: forge_or_induction_heater_v0
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
    item: forging_press_v0
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
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_engine_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: precision_lathe
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
    item: steel_bar_stock
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: metal_sheet_or_plate
    quantity: 0.3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: grease_bearing_high_temp
    quantity: 0.1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_rubber_bearing
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: info
    message: "Import remaining steel components."
- cmd: sim.import
  args:
    item: steel_drum
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: grinding_media_steel
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble rolling mill from local components."
- cmd: sim.import
  args:
    item: motor_assembly
    quantity: 12
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_rolling_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Rolling mill v0 with local steel components complete!"
```
