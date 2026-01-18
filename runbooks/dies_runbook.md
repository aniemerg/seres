# Dies Runbook

Goal: Build `dies` with maximum ISRU using regolith-derived metal.

## Strategy

Dies require only regolith_metal_crude (45 kg input → 40 kg dies output), making this an excellent ISRU candidate.

Expected ISRU: ~100% (only regolith_metal_crude needed)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: dies_runbook
- cmd: sim.reset
  args:
    sim-id: dies_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting dies runbook."
```

## ISRU Build: Dies from Regolith Metal

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce dies from regolith_metal_crude via MRE."
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
    quantity: 1000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce 45 kg regolith_metal_crude via MRE (need ~2 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: info
    message: "Produce dies from regolith_metal_crude (casting + machining)."
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_dies_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: dies produced from regolith metal (40 kg + 5 kg scrap)."
- cmd: sim.provenance
  args:
    item: dies
    quantity: 40
    unit: kg
```
