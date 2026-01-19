# Pyrolysis Chamber v0 Runbook

Goal: Build `pyrolysis_chamber_v0` and replace fasteners with an ISRU chain in-place.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: pyrolysis_chamber_v0_runbook
- cmd: sim.reset
  args:
    sim-id: pyrolysis_chamber_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting pyrolysis_chamber_v0 runbook."
```

## Baseline build (imported inputs)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import tooling and baseline components."
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
    item: metal_shear_or_saw
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
    item: drill_press
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
    item: refractory_brick_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_circuit_board_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_plate_or_sheet
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_material
    quantity: 15
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 6000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble baseline pyrolysis_chamber_v0."
- cmd: sim.run-recipe
  args:
    recipe: recipe_pyrolysis_chamber_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Baseline pyrolysis_chamber_v0 build complete."
```

## ISRU upgrades (in-place)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce ISRU fastener_kit_large from regolith metal."
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
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble a second chamber using ISRU fasteners."
- cmd: sim.note
  args:
    style: info
    message: "Re-import non-ISRU components for the ISRU fastener assembly."
- cmd: sim.import
  args:
    item: refractory_brick_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_circuit_board_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_plate_or_sheet
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_material
    quantity: 15
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_pyrolysis_chamber_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "ISRU-upgraded pyrolysis_chamber_v0 build complete."
- cmd: sim.provenance
  args:
    item: pyrolysis_chamber_v0
    quantity: 1
    unit: unit
```
