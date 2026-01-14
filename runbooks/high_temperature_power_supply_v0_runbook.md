# High Temperature Power Supply v0 Runbook

Goal: build `high_temperature_power_supply_v0`, then replace metal-heavy subcomponents
with in-situ production where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: high_temperature_power_supply_v0_runbook
- cmd: sim.reset
  args:
    sim-id: high_temperature_power_supply_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting high_temperature_power_supply_v0 runbook."
```

## Baseline: import equipment

Commentary: import core fabrication and MRE equipment needed for casting, machining,
and metal alloy production.

```sim-runbook
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: hand_tools_basic
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
    item: furnace_high_temp
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
    item: ceramic_press_or_mold_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drying_oven
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: kiln_ceramic
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
    item: vibrating_screen_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: screening_equipment
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
    item: electrodes
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: high_temperature_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
```

## Baseline: import subcomponents and assemble

Commentary: import subcomponents to validate the base recipe.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline build: import subcomponents."
- cmd: sim.import
  args:
    item: high_temp_power_supply_unit
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
    item: power_bus_high_current
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
    item: cooling_loop_basic
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
    recipe: recipe_machine_high_temperature_power_supply_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Baseline high_temperature_power_supply_v0 build complete."
```

## ISRU: produce metal_alloy_bulk via MRE

Commentary: produce metal_alloy_bulk from regolith using molten regolith electrolysis.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce metal_alloy_bulk via MRE."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 4560
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 12
- cmd: sim.advance-time
  args:
    hours: 200
```

## ISRU: fabricate subcomponents and assemble

Commentary: replace metal-heavy subcomponents with in-situ metal alloy; keep compute,
sensors, and small electronics imported for now.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: fabricate subcomponents from local metal alloy."
- cmd: sim.import
  args:
    item: power_supply_components_basic
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_high_temp_power_supply_unit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_conditioning_module_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce ceramic insulators from regolith-derived powders."
- cmd: sim.run-recipe
  args:
    recipe: recipe_coarse_powder_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_powder_mixture_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.import
  args:
    item: water
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_insulators_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_bus_high_current_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.import
  args:
    item: metal_feedstock
    quantity: 57
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: circulation_pump_coolant
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_cooling_loop_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
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
    recipe: recipe_machine_high_temperature_power_supply_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "ISRU high_temperature_power_supply_v0 build complete."
```
