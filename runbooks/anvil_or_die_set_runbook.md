# Anvil or Die Set Runbook

Goal: Build `anvil_or_die_set` using in-situ steel production from regolith.

## Machine Details
- **Mass**: 25 kg (item spec) / 240 kg (actual from recipe)
- **Material Class**: steel
- **Capabilities**: forging_support, die_set_forming

## Required Components (from recipe)
1. steel_stock_bar_or_billet (270 kg total)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: anvil_or_die_set_runbook
- cmd: sim.reset
  args:
    sim-id: anvil_or_die_set_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting anvil_or_die_set ISRU build with local steel production."
```

## ISRU Build: Local Steel Production

Commentary: Produce steel_stock_bar_or_billet (270 kg) from regolith metal. Need 284 kg regolith_metal_crude total, which is ~13 batches of MRE.

```sim-runbook
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: regolith_lunar_mare
    quantity: 2000
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 10000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce 284 kg regolith_metal_crude from regolith (13 batches)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 130
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel stock from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: milestone
    message: "Forge anvil/die set with locally-produced steel"
- cmd: sim.run-recipe
  args:
    recipe: recipe_anvil_or_die_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "ISRU anvil_or_die_set build complete (35.7% ISRU)."
```
