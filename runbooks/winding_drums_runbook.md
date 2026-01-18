# Winding Drums Runbook

Goal: Build `winding_drums` with ISRU steel bar stock where possible.

## Machine Details
- **Mass**: 50 kg
- **Material Class**: steel
- **Capabilities**: Winding support and spool rotation.

## Required Components (from recipe)
1. steel_bar_stock (55 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: winding_drums_runbook
- cmd: sim.reset
  args:
    sim-id: winding_drums_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting winding_drums runbook."
```

## Stage 1: Tooling and baseline imports

Commentary: Import machining and assembly tooling, plus supporting equipment for ISRU steel.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 1: Import tooling and support equipment."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: assembly_tools_basic
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
    item: high_temperature_power_supply_v0
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
    item: electrodes
    quantity: 1
    unit: unit
    ensure: true
```

## Stage 2: ISRU steel bar stock

Commentary: Produce steel bar stock from regolith metal for drum and shaft machining.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: ISRU steel bar stock."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 1100
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Produce regolith_metal_crude for steel stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 2.8
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: success
    message: "Produced ~64 kg regolith_metal_crude."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Roll steel_stock_bar_or_billet from regolith metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 0.22
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Produced ~59 kg steel_stock_bar_or_billet."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Roll steel_bar_stock for winding drums (55 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 55
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "Produced 55 kg steel_bar_stock."
```

## Stage 3: Assemble winding_drums

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 3: Assemble winding_drums."
- cmd: sim.run-recipe
  args:
    recipe: recipe_winding_drums_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: milestone
    message: "Winding drums assembled."
- cmd: sim.provenance
  args:
    item: winding_drums
    quantity: 1
    unit: unit
```
