# Deburring Tools Runbook

Goal: Build `deburring_tools` with maximum ISRU using regolith-derived metal.

## Strategy

Deburring tools require steel_stock_bar_or_billet (1 kg), which can be produced from regolith_metal_crude using the ISRU recipe.

Production chain: regolith → regolith_metal_crude → steel_stock_bar_or_billet → forged_steel_parts → machined_part_raw → deburring_tools

Expected ISRU: ~100% (full chain from regolith)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: deburring_tools_runbook
- cmd: sim.reset
  args:
    sim-id: deburring_tools_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting deburring tools runbook."
```

## ISRU Build: Deburring Tools from Regolith Metal

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce deburring_tools from regolith_metal_crude via MRE."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce 284 kg regolith_metal_crude via MRE (need ~13 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: info
    message: "Produce 270 kg steel_stock_bar_or_billet from 284 kg regolith_metal_crude using ISRU recipe."
- cmd: sim.import
  args:
    item: rolling_mill_or_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: info
    message: "Produce deburring_tools from steel_stock_bar_or_billet (forge + machine + assemble)."
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
    item: power_hammer_or_press
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
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_deburring_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: deburring_tools produced from regolith metal (1 kit)."
- cmd: sim.provenance
  args:
    item: deburring_tools
    quantity: 1
    unit: kit
```
