# Inert Atmosphere System Runbook

Goal: Build `inert_atmosphere_system` using in-situ resources where possible.

## Machine Details
- **Mass**: 86.4 kg
- **Material Class**: steel
- **Capabilities**: inert gas control, oxygen monitoring

## Required Components (from recipe)
1. gas_cylinder_argon_or_nitrogen (2 unit)
2. gas_supply_regulator (2 unit)
3. gas_flow_controller (1 unit)
4. oxygen_sensor_module (1 unit)
5. piping_components (1 kg)
6. vacuum_pump_small (1 unit)
7. control_panel_basic (1 unit)
8. enclosure_electrical_medium (1 unit)
9. fastener_kit_small (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: inert_atmosphere_system_runbook
- cmd: sim.reset
  args:
    sim-id: inert_atmosphere_system_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting inert_atmosphere_system runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all components and assembly equipment to confirm the recipe runs.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment and parts for assembly."
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
    item: gas_cylinder_argon_or_nitrogen
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_supply_regulator
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_flow_controller
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: oxygen_sensor_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: piping_components
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: vacuum_pump_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: enclosure_electrical_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Assemble inert_atmosphere_system from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_inert_atmosphere_system_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Baseline inert_atmosphere_system complete."
```

## Stage 2: ISRU gas supply regulators (regolith metal)

Commentary: Produce gas_supply_regulator locally using regolith_metal_crude. Other components remain imported.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: inert_atmosphere_system_runbook
- cmd: sim.reset
  args:
    sim-id: inert_atmosphere_system_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Local gas supply regulators for inert atmosphere system."
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
    item: test_bench_electrical
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

- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_metal_crude for gas regulator castings."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sealing_gaskets
    quantity: 0.5
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_gas_supply_regulator_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: info
    message: "Produce piping components from regolith metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_piping_components_regolith_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Produce an electrical enclosure from regolith metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.run-recipe
  args:
    recipe: recipe_enclosure_electrical_medium_regolith_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20

- cmd: sim.note
  args:
    style: info
    message: "Import remaining components for final assembly."
- cmd: sim.import
  args:
    item: gas_cylinder_argon_or_nitrogen
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_flow_controller
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: oxygen_sensor_module
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
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Final assembly with ISRU regulators, piping, and enclosure."
- cmd: sim.run-recipe
  args:
    recipe: recipe_inert_atmosphere_system_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "ISRU inert_atmosphere_system complete."
```
