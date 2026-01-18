# Furnace Basic Runbook

Goal: Build `furnace_basic` using in-situ resources where possible.

## Machine Details
- **Mass**: 300 kg
- **Material Class**: steel
- **Capabilities**: Basic electric or fuel-fired furnace for heating, melting, and heat treatment. Temperature range 200-1200°C.

## Required Components (from recipe)
1. steel_plate_or_sheet (320 kg) - for furnace shell and door
2. steel_stock (300 kg) - structural components
3. refractory_lining_set (1 unit) - for chamber insulation
4. heating_element_set_basic (1 unit) - heating elements
5. temperature_controller_basic (1 unit) - temperature control
6. door_hinge_assembly (1 unit) - furnace door
7. control_circuit_board_basic (1 unit) - control electronics

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: furnace_basic_runbook
- cmd: sim.reset
  args:
    sim-id: furnace_basic_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting furnace_basic runbook."
```

## Single-Stage ISRU Build (max ISRU, no baseline stage)

Commentary: Produce steel plate and stock from regolith (ore + carbon chain), then assemble with imported non-steel components. This keeps a single stage focused on maximum ISRU for bulk materials.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Single-stage ISRU build: produce steel inputs locally, then assemble furnace_basic."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: welding_consumables
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
    item: cutting_tools_general
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
    item: high_temperature_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 2
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
    item: plate_rolling_mill
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
    item: rolling_mill_or_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
    notes: "Bootstrap heat source for steel_plate_or_sheet rolling; replace with ISRU furnace once available."
- cmd: sim.note
  args:
    style: info
    message: "Mine mare regolith and extract ilmenite for iron ore (target ~1336 kg ore)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 23
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 2300
- cmd: sim.advance-time
  args:
    hours: 2300
- cmd: sim.note
  args:
    style: info
    message: "Mine carbonaceous regolith and extract carbon for reducing agent (target ~334 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 223
- cmd: sim.advance-time
  args:
    hours: 1350
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 1114
- cmd: sim.advance-time
  args:
    hours: 1700
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 334
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: info
    message: "Produce steel_stock (300 kg) and steel_plate_or_sheet (320 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 300
- cmd: sim.advance-time
  args:
    hours: 2000
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 353
- cmd: sim.advance-time
  args:
    hours: 1500
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 336
- cmd: sim.advance-time
  args:
    hours: 1100
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 320
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: info
    message: "Import non-steel components and assemble furnace_basic."
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
    item: door_hinge_assembly
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_circuit_board_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.provenance
  args:
    item: furnace_basic
    quantity: 1
    unit: unit
```
