# Controlled Atmosphere Chamber Runbook

Goal: Build `controlled_atmosphere_chamber` and replace the chamber shell feedstock with an ISRU sheet-metal chain.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: controlled_atmosphere_chamber_runbook
- cmd: sim.reset
  args:
    sim-id: controlled_atmosphere_chamber_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting controlled_atmosphere_chamber runbook."
```

## Baseline build (imported inputs)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import assembly tooling and baseline components."
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
    item: fixturing_workbench
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chamber_shell_sealed
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vacuum_pump_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: inert_gas_manifold
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: atmosphere_sensors_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: thermal_controller_basic
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
    item: control_compute_module_imported
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
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 8000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble baseline controlled_atmosphere_chamber."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_controlled_atmosphere_chamber_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "Baseline controlled_atmosphere_chamber build complete."
```

## ISRU upgrades (in-place)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce ISRU sheet metal for a local chamber shell."
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
- cmd: sim.note
  args:
    style: info
    message: "Run MRE batches for regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 11
- cmd: sim.advance-time
  args:
    hours: 55
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_chamber_shell_sealed_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 220
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble a second chamber using ISRU sheet metal."
- cmd: sim.note
  args:
    style: info
    message: "Re-import non-ISRU components for the ISRU shell assembly."
- cmd: sim.import
  args:
    item: vacuum_pump_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: inert_gas_manifold
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: atmosphere_sensors_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: thermal_controller_basic
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
    item: control_compute_module_imported
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
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_controlled_atmosphere_chamber_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "ISRU-upgraded controlled_atmosphere_chamber build complete."
- cmd: sim.provenance
  args:
    item: controlled_atmosphere_chamber
    quantity: 1
    unit: unit
```
