# Chemical Reactor Basic Runbook

Goal: build `chemical_reactor_basic` while increasing ISRU coverage for the steel vessel and plate stock.

Approach:
1) Baseline import all top-level parts and assemble a unit.
2) Identify the highest-mass subcomponents and replace with local recipes.
3) Assemble a second unit with locally-produced parts where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: chemical_reactor_basic_runbook
- cmd: sim.reset
  args:
    sim-id: chemical_reactor_basic_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting chemical_reactor_basic runbook."
```

## Baseline assembly (imports)

Commentary: baseline assembly with imported plate stock and purchased subsystems.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import plate stock and assemble chemical_reactor_basic."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: steel_plate_or_sheet
    quantity: 300.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: piping_and_fittings_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: insulation_pack_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_heavy
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 50
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Baseline chemical_reactor_basic assembly complete."
```

## Local subcomponents

Commentary: produce steel plate locally from regolith-derived steel ingots.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for local steel plate production."
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
    item: rolling_mill_v0
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
    item: electrical_energy
    quantity: 1000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce local steel_ingot via iron ore reduction and refining."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 80
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 362
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 105
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 700
- cmd: sim.advance-time
  args:
    hours: 800
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 210
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 315
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 300
- cmd: sim.advance-time
  args:
    hours: 800
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: piping_and_fittings_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: insulation_pack_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_heavy
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 50
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Local chemical_reactor_basic assembly complete."
```
