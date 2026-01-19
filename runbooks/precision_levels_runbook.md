# Precision Levels Runbook

Goal: build `precision_levels` with a baseline import path, then iterate toward ISRU.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: precision_levels_runbook
- cmd: sim.reset
  args:
    sim-id: precision_levels_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting precision_levels runbook."
```

## Baseline assembly (imports)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import tooling, stock, and assemble precision_levels."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: precision_lathe
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cnc_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_grinder
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coordinate_measuring_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: precision_tooling_set
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
    item: measurement_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: aluminum_alloy_ingot
    quantity: 4.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cutting_fluid
    quantity: 0.4
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
    recipe: recipe_precision_levels_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: success
    message: "Baseline precision_levels build complete."
```

## ISRU upgrade: local aluminum alloy ingot

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce aluminum_alloy_ingot with local alumina."
- cmd: sim.import
  args:
    item: chemical_reactor_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrolysis_cell_unit_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydrochloric_acid
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_anode
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cryolite_flux
    quantity: 1.0
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
    recipe: recipe_regolith_lunar_highlands_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_alumina_powder_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.import
  args:
    item: cutting_fluid
    quantity: 0.4
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_precision_levels_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: success
    message: "ISRU build with local alumina-derived aluminum complete."
```
