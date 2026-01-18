# Soldering Station Runbook

Goal: build `soldering_station` with baseline imports, then replace sheet metal with
local steel to increase ISRU.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: soldering_station_runbook
- cmd: sim.reset
  args:
    sim-id: soldering_station_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting soldering station runbook."
```

## Baseline import + assembly

Commentary: import recipe inputs and basic tooling to validate the recipe once.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline assembly with imported inputs."
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
    item: soldering_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: nickel_chromium_alloy
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 0.05
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_low_voltage
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tip_holder_and_stand
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 200
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_soldering_station_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Baseline soldering station assembly complete."
- cmd: sim.note
  args:
    style: milestone
    message: "Reset simulation for ISRU-focused build."
- cmd: sim.reset
  args:
    sim-id: soldering_station_runbook
```

## ISRU: local steel for base and holder

Commentary: produce steel from regolith to replace the sheet metal input. The other
inputs remain imported for now.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import tooling for local steel production."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: electrical_energy
    quantity: 2000
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 2
    unit: kg
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Refine steel from ilmenite for local sheet metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 12
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
```

## Final assembly (local sheet metal)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble soldering station with local sheet metal."
- cmd: sim.import
  args:
    item: soldering_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: nickel_chromium_alloy
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 0.05
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_low_voltage
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tip_holder_and_stand
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_soldering_station_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "soldering_station local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
