# Welding Tools Set Runbook

Goal: Build `welding_tools_set` using in-situ resources where possible.

## Machine Details
- **Mass**: 15 kg
- **Material Class**: steel
- **Capabilities**: welding accessories, gauges, clamps, holders

## Required Components (from recipe)
1. steel_plate_or_sheet (15 kg)
2. fastener_kit_small (0.5 kg)
3. machined_part_raw (13.5 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: welding_tools_set_runbook
- cmd: sim.reset
  args:
    sim-id: welding_tools_set_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting welding_tools_set runbook."
```

## Stage 1: ISRU steel chain (regolith to plate, fasteners, machined parts)

Commentary: Produce steel plate, fasteners, and machined parts from regolith-derived iron and carbon.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: ISRU steel chain for welding tools set."
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
    item: fixturing_workbench
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
    item: milling_machine_cnc
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
    item: calibration_standards
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
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: saw_or_cutting_tool
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
    item: reduction_furnace_v0
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
    item: furnace_basic
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
    item: heating_furnace
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
    item: rolling_mill_or_brake
    quantity: 1
    unit: unit
    ensure: true

- cmd: sim.note
  args:
    style: info
    message: "Mine mare regolith for ilmenite extraction."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 200
- cmd: sim.advance-time
  args:
    hours: 220

- cmd: sim.note
  args:
    style: info
    message: "Collect carbonaceous regolith and extract carbon reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 65
- cmd: sim.advance-time
  args:
    hours: 110
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 18
- cmd: sim.advance-time
  args:
    hours: 40

- cmd: sim.note
  args:
    style: info
    message: "Smelt iron and refine into steel ingots for plate." 
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 34
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 120

- cmd: sim.note
  args:
    style: info
    message: "Roll steel plate for welding tools set and cut parts stock." 
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 1.5
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 12

- cmd: sim.note
  args:
    style: info
    message: "Produce steel stock and fastener kit from regolith steel." 
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 0.5
- cmd: sim.advance-time
  args:
    hours: 2

- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly with ISRU steel components."
- cmd: sim.import
  args:
    item: textile_fabric
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_tools_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.note
  args:
    style: success
    message: "ISRU welding_tools_set complete."
```
