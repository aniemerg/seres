# Vibrating Screen v0 Runbook

Goal: Build `vibrating_screen_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: 180 kg
- **Material Class**: (steel/mechanical)
- **Capabilities**: regolith screening and separation

## Required Components (from recipe)
1. screen_deck_basic (1 unit)
2. vibrator_motor_small (1 unit)
3. support_frame_welded (1 unit)
4. control_compute_module_imported (1 unit)
5. sensor_suite_general (1 unit)
6. power_conditioning_module (1 unit)
7. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: vibrating_screen_v0_runbook
- cmd: sim.reset
  args:
    sim-id: vibrating_screen_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting vibrating_screen_v0 runbook."
```

## Stage 1: Local Steel Production (ISRU)

Commentary: Produce support_frame_welded (120 kg) and screen_deck_basic (40 kg) from regolith metal. Need 177 kg regolith_metal_crude total, which is ~8 batches of MRE.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Local steel production from regolith"
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
    item: furnace_basic
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
    item: casting_mold_set
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
    item: vibrating_screen_v0
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
    item: dust_collection_system
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
    item: vibrator_motor_small
    quantity: 1
    unit: unit
    ensure: true
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
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 1500
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce 177 kg regolith_metal_crude from regolith (8 batches)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: milestone
    message: "Produce support frame from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_support_frame_welded_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Produce screen deck from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_screen_deck_basic_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble vibrating screen with locally-produced steel"
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_vibrating_screen_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: Vibrating screen with local steel ISRU"
```

## Stage 3: Final Assembly
*To be implemented - optimize remaining components for ISRU*
