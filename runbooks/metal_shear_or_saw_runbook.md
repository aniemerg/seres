# Metal Shear or Saw Runbook

Goal: Build `metal_shear_or_saw` using in-situ resources where possible.

## Machine Details
- **Mass**: 350 kg
- **Material Class**: steel
- **Capabilities**: metal cutting, sheet metal shearing

## Required Components (from recipe)
1. steel_beam_i_section (60 kg)
2. motor_electric_small (1 unit)
3. fastener_kit_large (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: metal_shear_or_saw_runbook
- cmd: sim.reset
  args:
    sim-id: metal_shear_or_saw_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting metal_shear_or_saw runbook."
```

## Stage 1: Local Steel Production (ISRU)

Commentary: Produce steel_beam_i_section (60 kg) from regolith metal. Need 70 kg regolith_metal_crude total, which is ~3 batches of MRE.

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
    item: welding_tools_set
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
    item: plate_rolling_mill
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
    item: motor_electric_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 1000
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
    message: "Produce 70 kg regolith_metal_crude from regolith (4 batches)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel beam from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_beam_i_section_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble metal shear/saw with locally-produced steel"
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_shear_or_saw_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: Metal shear/saw with local steel ISRU"
```
