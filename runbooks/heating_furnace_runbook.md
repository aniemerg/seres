# Heating Furnace Runbook

Goal: Build `heating_furnace` using in-situ resources where possible.

## Machine Details
- **Mass**: 512 kg
- **Material Class**: refractory
- **Capabilities**: general-purpose heating

## Required Components (from recipe)
1. steel_plate_or_sheet (200 kg)
2. refractory_brick_set (1 unit)
3. heating_element_electric (4 unit)
4. insulation_thermal_blanket (1 unit)
5. furnace_door_assembly (1 unit)
6. temperature_controller_basic (1 unit)
7. structural_frame_large (1 unit)
8. power_cable_assembly (1 unit)
9. fastener_kit_large (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: heating_furnace_runbook
- cmd: sim.reset
  args:
    sim-id: heating_furnace_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting heating_furnace runbook."
```

## ISRU Production: Build heating furnace with regolith-derived steel plate

Commentary: Produce steel_plate_or_sheet locally for the furnace shell from regolith-derived iron and carbon. Other components remain imported.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: Build heating furnace with local steel plate."
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
    item: press_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake_die_set
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
    item: welding_tools_set
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
    item: high_temperature_power_supply_v0
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
    item: rolling_mill_v0
    quantity: 1
    unit: unit
    ensure: true

- cmd: sim.note
  args:
    style: info
    message: "Mine regolith and extract ilmenite for iron feedstock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 737
- cmd: sim.advance-time
  args:
    hours: 800

- cmd: sim.note
  args:
    style: info
    message: "Collect carbonaceous regolith and extract carbon reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 77
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 385
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 111
- cmd: sim.advance-time
  args:
    hours: 300

- cmd: sim.note
  args:
    style: info
    message: "Smelt iron and refine into steel ingots, then roll plate."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 221
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 210
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 200
- cmd: sim.advance-time
  args:
    hours: 400

- cmd: sim.note
  args:
    style: info
    message: "Import remaining components for final assembly (extra refractory bricks to cover process losses)."
- cmd: sim.import
  args:
    item: refractory_brick_set
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_electric
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: insulation_thermal_blanket
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_door_assembly
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
    item: structural_frame_large
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_cable_assembly
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 1
    unit: unit
    ensure: true

- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly with ISRU steel plate."
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: success
    message: "ISRU heating_furnace complete."
```
