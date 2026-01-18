# Steel Forming Press Runbook

Goal: Build `steel_forming_press` using in-situ resources where possible.

## Machine Details
- **Mass**: 2000 kg
- **Capabilities**: steel forming, press operations

## Required Components (from recipe)
1. press_frame_medium (1 unit)
2. hydraulic_cylinder_press (1 unit)
3. hydraulic_system_medium (1 unit)
4. press_platen_set_medium (1 unit)
5. power_conditioning_module (1 unit)
6. control_compute_module_imported (1 unit)
7. sensor_suite_general (1 unit)
8. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: steel_forming_press_runbook
- cmd: sim.reset
  args:
    sim-id: steel_forming_press_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting steel_forming_press runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all components and assembly equipment to test if the recipe runs.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment and parts for assembly."
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
    item: press_frame_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_cylinder_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_system_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_platen_set_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble steel forming press from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_forming_press_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Baseline steel_forming_press complete."
```

## Stage 2: ISRU Components

Commentary: Produce regolith metal for the press frame and platens. Keep hydraulics, power, and controls imported.

```sim-runbook
- cmd: sim.reset
  args:
    sim-id: steel_forming_press_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: ISRU frame + platens from regolith metal."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
- cmd: sim.import
  args:
    item: surface_grinder
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: grinding_wheels
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
    item: mre_reactor_v0
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
    item: electrical_energy
    quantity: 10000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal feedstock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 23
- cmd: sim.advance-time
  args:
    hours: 2000
- cmd: sim.note
  args:
    style: milestone
    message: "Cast and machine press frame + platens."
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_frame_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_platen_set_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining components and assemble press."
- cmd: sim.import
  args:
    item: hydraulic_cylinder_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_system_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_forming_press_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: steel_forming_press with ISRU frame + platens."
```
