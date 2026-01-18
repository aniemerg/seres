# Assembly Station Runbook

Goal: build `assembly_station` with maximum local production. Start with baseline
imports to validate the recipe, then replace subcomponents with local recipes.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: assembly_station_runbook
- cmd: sim.reset
  args:
    sim-id: assembly_station_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting assembly station runbook."
```

## Baseline import + assembly

Commentary: import all inputs to validate `recipe_assembly_station_v0`.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import assembly station inputs and required tooling."
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
    item: electrical_energy
    quantity: 200
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: regolith_metal_crude
    quantity: 80
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: tool_station_frame
    quantity: 80
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: tool_set_general
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
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
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Baseline: imported all recipe_assembly_station_v0 inputs."
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembly_station_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Baseline assembly_station build attempted."
```

## Local subcomponents (partial ISRU)

Commentary: replace import-only items with local recipes where available. This
still relies on imported feedstocks for metals and electronics.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce local subcomponents for the assembly station."
- cmd: sim.note
  args:
    style: info
    message: "ISRU: produce regolith_metal_crude via MRE for power conditioning."
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
    quantity: 4000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 9
- cmd: sim.advance-time
  args:
    hours: 100
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
    item: metal_shear_or_saw
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_station_frame_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_set_general_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.import
  args:
    item: bolt_hex_medium_steel
    quantity: 0.72
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: nut_hex_medium_steel
    quantity: 0.18
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: washer_flat_medium_steel
    quantity: 0.075
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: washer_lock_medium_steel
    quantity: 0.03
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_assembly_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
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
    item: electronic_components_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_conditioning_module_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: info
    message: "Local subcomponents ready (frame, tool set, fastener kit, power conditioning)."
```

## Final assembly (mixed local + imports)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly using local subcomponents and remaining imports."
- cmd: sim.import
  args:
    item: regolith_metal_crude
    quantity: 80
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
    item: control_compute_module_imported
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembly_station_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "assembly_station build complete (mixed local + imported)."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
