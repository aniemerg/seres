# Rock Crusher Basic Runbook

Goal: build `rock_crusher_basic` with >50% ISRU mass by producing all
`steel_plate_raw` locally, then assembling the crusher.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: rock_crusher_basic_runbook
- cmd: sim.reset
  args:
    sim-id: rock_crusher_basic_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting rock crusher basic runbook."
```

## Baseline import + assembly

Commentary: import required tooling and all `steel_plate_raw` to validate the recipe
once, then assemble a baseline rock crusher.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline assembly with imported steel plate."
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
    item: heat_treatment_furnace
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
    item: welding_tools_set
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
    item: test_bench_electrical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_plate_raw
    quantity: 530
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 1200
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_rock_crusher_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2400
- cmd: sim.note
  args:
    style: success
    message: "Baseline rock crusher assembly complete."
- cmd: sim.note
  args:
    style: milestone
    message: "Reset simulation for ISRU-focused build."
- cmd: sim.reset
  args:
    sim-id: rock_crusher_basic_runbook
```

## In-situ equipment + feedstocks

Commentary: import equipment needed to mine regolith and process steel locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for in-situ steel plate production."
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
    item: heat_treatment_furnace
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
    item: welding_tools_set
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
    item: test_bench_electrical
    quantity: 1
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
    item: electrical_energy
    quantity: 4000
    unit: kWh
    ensure: true
```

## In-situ: regolith mining

Commentary: mine enough mare regolith to produce ~530 kg of steel plate locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Mine mare regolith for ilmenite extraction."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 10
```

## In-situ: iron ore, pig iron, steel ingot, steel plate

Commentary: convert mare regolith to ilmenite, smelt to iron, refine to steel, then roll
into raw plate.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Extract ilmenite and produce steel plate stock."
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 300
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 2000
- cmd: sim.advance-time
  args:
    hours: 2200
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 585
- cmd: sim.advance-time
  args:
    hours: 2600
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 557
- cmd: sim.advance-time
  args:
    hours: 2000
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 530
- cmd: sim.advance-time
  args:
    hours: 500
```

## Final assembly (mixed local + imported plate)

Commentary: assemble the crusher using locally produced steel plate.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble rock crusher with locally produced steel plate."
- cmd: sim.run-recipe
  args:
    recipe: recipe_rock_crusher_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2200
- cmd: sim.note
  args:
    style: success
    message: "ISRU-focused rock_crusher_basic assembly complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
