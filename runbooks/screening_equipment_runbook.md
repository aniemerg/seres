# Screening Equipment Runbook

Goal: Build `screening_equipment` with maximum ISRU.

## Machine Details
- **Mass**: 60 kg
- **Material Class**: steel
- **Capabilities**: Vibrating screen for particle size separation.

## Required Components (from recipe)
1. steel_plate_raw (45 kg)
2. steel_mesh_sheet_material (5 kg)
3. vibrator_motor_small (8 kg)
4. electrical_wiring_kit (1 kg)
5. fastener_kit_medium (1 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: screening_equipment_runbook
- cmd: sim.reset
  args:
    sim-id: screening_equipment_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting screening_equipment runbook."
```

## ISRU steel plate and mesh

Commentary: Produce steel plate and mesh stock in-situ for the frame and screen.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU steel plate and mesh stock (tooling + imports for non-steel parts)."
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
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: rolling_mill_v0
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
    item: soldering_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_crimping_tools
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
    item: heating_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibrator_motor_small
    quantity: 8
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wiring_kit
    quantity: 1
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
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine mare regolith for iron ore (~120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Mined 200 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract ilmenite for iron ore."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 200
- cmd: sim.advance-time
  args:
    hours: 220
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~120 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Mine carbonaceous regolith for reducing agent (~26 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 18
- cmd: sim.advance-time
  args:
    hours: 110
- cmd: sim.note
  args:
    style: success
    message: "Mined 900 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2d: Extract carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 90
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~26 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2e: Convert to carbon_reducing_agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 26
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: success
    message: "Produced 26 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 2f: Smelt pig iron for steel (52 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 52
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.note
  args:
    style: success
    message: "Produced 52 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 2g: Cast steel ingots for plate (48 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 48
- cmd: sim.advance-time
  args:
    hours: 520
- cmd: sim.note
  args:
    style: success
    message: "Produced 48 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 2h: Roll steel_plate_raw (45 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 45
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Produced 45 kg steel_plate_raw."
- cmd: sim.note
  args:
    style: info
    message: "Step 2i: Produce regolith_metal_crude for mesh stock."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 120
    unit: kWh
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
    item: electrodes
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 0.3
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Produced ~6.8 kg regolith_metal_crude."
- cmd: sim.note
  args:
    style: info
    message: "Step 2j: Roll steel_stock_bar_or_billet and steel_bar_stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 0.024
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: success
    message: "Produced ~6.5 kg steel_stock_bar_or_billet."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Produced 6 kg steel_bar_stock."
- cmd: sim.note
  args:
    style: info
    message: "Step 2k: Produce steel_mesh_sheet_material (5 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_mesh_sheet_material_v0
    quantity: 34
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Produced ~5.1 kg steel_mesh_sheet_material."
```

## Assemble screening_equipment

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble screening_equipment."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_screening_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: milestone
    message: "Screening equipment assembled."
- cmd: sim.provenance
  args:
    item: screening_equipment
    quantity: 1
    unit: unit
```
