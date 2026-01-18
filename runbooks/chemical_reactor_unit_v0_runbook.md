# Chemical Reactor Unit v0 Runbook

Goal: build `chemical_reactor_unit_v0` while increasing ISRU coverage for major subassemblies.

Approach:
1) Baseline import all top-level parts and assemble a unit.
2) Identify the highest-mass subcomponents and replace with local recipes.
3) Assemble a second unit with locally-produced parts where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: chemical_reactor_unit_v0_runbook
- cmd: sim.reset
  args:
    sim-id: chemical_reactor_unit_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting chemical_reactor_unit_v0 runbook."
```

## Baseline assembly (imports)

Commentary: the current recipe is a placeholder and only requires ingots plus assembly capacity.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import ingots and assemble chemical_reactor_unit_v0."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: steel_ingot
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: metal_ingot
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 50
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_unit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Baseline chemical_reactor_unit_v0 assembly complete."
```

## Local subcomponents

Commentary: the current recipe only consumes ingots, so focus on local ingot production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for local ingot production."
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
    item: ball_mill_v0
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
    item: reduction_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 1000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce local metal_ingot via regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_ingot_v1
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 10
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce local steel_ingot via iron ore reduction and refining."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 36.21
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 10.5
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 70
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 21
- cmd: sim.advance-time
  args:
    hours: 90
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 20
- cmd: sim.advance-time
  args:
    hours: 70
```

## In-situ assembly

Commentary: assemble a second unit using locally-produced ingots.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble chemical_reactor_unit_v0 with locally-produced ingots."
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_unit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Local chemical_reactor_unit_v0 assembly complete."
```

## Additional ISRU units

Commentary: scale local ingot production and assemble two more units to raise overall ISRU share.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import extra energy for scaled local ingot production."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 2000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce additional local metal_ingot."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_ingot_v1
    quantity: 20
- cmd: sim.advance-time
  args:
    hours: 20
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce additional local steel_ingot."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 72.5
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 21
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 140
- cmd: sim.advance-time
  args:
    hours: 160
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 42
- cmd: sim.advance-time
  args:
    hours: 180
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 130
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble two additional chemical_reactor_unit_v0 units from local ingots."
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_unit_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Two additional local chemical_reactor_unit_v0 units complete."
```
