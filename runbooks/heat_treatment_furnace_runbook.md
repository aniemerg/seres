# Heat Treatment Furnace v0 Runbook

Goal: Build `heat_treatment_furnace_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: 600 kg
- **Material Class**: steel
- **Capabilities**: heat treating metals with controlled cycles

## Required Components (from recipe)
1. bulk_material_or_parts (1 kg)
2. furnace_shell_insulated (1 unit)
3. refractory_lining_set (1 unit)
4. heating_element_set_basic (1 unit)
5. temperature_controller_basic (1 unit)
6. level_sensor_basic (1 unit)
7. sensor_suite_general (1 unit)
8. control_compute_module_imported (1 unit)
9. power_conditioning_module (1 unit)
10. quench_rack_and_baskets (1 unit)
11. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: heat_treatment_furnace_runbook
- cmd: sim.reset
  args:
    sim-id: heat_treatment_furnace_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting heat_treatment_furnace_v0 runbook."
```

## ISRU Production: Build heat treatment furnace with regolith materials

Commentary: Produce quench_rack_and_baskets and furnace_shell_insulated from regolith_metal_crude, import remaining components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: Build heat_treatment_furnace_v0 with regolith materials."
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
    item: refractory_installation_tools
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
    item: electrical_energy
    quantity: 6500
    unit: kWh
    ensure: true

- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_metal_crude for quench rack + furnace shell casting."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 15.0
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_quench_rack_and_baskets_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.note
  args:
    style: info
    message: "Import silica_purified for furnace shell mold prep."
- cmd: sim.import
  args:
    item: silica_purified
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_thermal_blanket
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_shell_insulated_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.note
  args:
    style: info
    message: "Import remaining components for final assembly."
- cmd: sim.import
  args:
    item: bulk_material_or_parts
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: refractory_lining_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_basic
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
    item: level_sensor_basic
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

- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly with ISRU quench rack."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_heat_treatment_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "ISRU heat_treatment_furnace_v0 complete."
```
