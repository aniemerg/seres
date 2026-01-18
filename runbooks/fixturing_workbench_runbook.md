# Fixturing Workbench Runbook

Goal: build `fixturing_workbench` with locally produced steel to maximize ISRU.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: fixturing_workbench_runbook
- cmd: sim.reset
  args:
    sim-id: fixturing_workbench_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting fixturing workbench runbook."
```

## Build fixturing workbench with local steel

```sim-runbook
- cmd: sim.note
  args:
    style: info
    message: "Import core equipment for in-situ steel production."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: fixturing_workbench
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
    item: crucible_refractory
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
    item: casting_mold_set
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
    item: furnace_basic
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
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Mine regolith for ilmenite extraction."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 350
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 2300
- cmd: sim.advance-time
  args:
    hours: 2600
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 662
- cmd: sim.advance-time
  args:
    hours: 3000
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 630
- cmd: sim.advance-time
  args:
    hours: 2000
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: info
    message: "Assemble fixturing workbench with local sheet steel."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fixturing_workbench_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 500
- cmd: sim.note
  args:
    style: success
    message: "fixturing_workbench local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
