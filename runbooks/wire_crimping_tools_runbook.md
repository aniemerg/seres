# Wire Crimping Tools Runbook

Goal: Build `wire_crimping_tools` with maximum ISRU using regolith-derived materials.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: wire_crimping_tools_runbook
- cmd: sim.reset
  args:
    sim-id: wire_crimping_tools_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting wire_crimping_tools runbook."
```

## Stage 1: Baseline (import all components)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import all components for baseline wire_crimping_tools assembly."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: quench_tank
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_metal_crude
    quantity: 6
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_wire_crimping_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Baseline wire_crimping_tools complete (0% ISRU)."
```

## Stage 2: ISRU Production

Commentary: Produce regolith_metal_crude from local regolith, then manufacture wire_crimping_tools.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith_metal_crude from regolith for wire_crimping_tools."
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
    quantity: 500
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Build wire_crimping_tools from local regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_wire_crimping_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Wire_crimping_tools with 100% ISRU regolith metal complete!"
```
