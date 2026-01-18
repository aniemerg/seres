# Lifting Equipment Runbook

Goal: Build `lifting_equipment` using in-situ resources where possible.

## Machine Details
- **Mass**: 150 kg
- **Capabilities**: lifting, material_handling
- **Specifications**: 500 kg load capacity, 3-4m lift height, chain hoist with electric winch

## Required Components (from recipe)
1. structural_frame_large (1 unit) - steel frame for gantry
2. electric_motor_small (1 unit) - winch drive motor
3. worm_gear_set_v0 (1 unit) - gear reduction
4. bearing_set_sealed (2 units) - shaft bearings
5. fastener_kit_medium (1 unit) - bolts and hardware
6. control_circuit_board_basic (1 unit) - motor control

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: lifting_equipment_runbook
- cmd: sim.reset
  args:
    sim-id: lifting_equipment_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting lifting_equipment runbook."
```

## Stage 1: ISRU Phase 1 - Produce regolith materials for structural frame

Commentary: Need 63 kg steel_plate_or_sheet for structural_frame_large (60 kg final + 3 kg scrap). Complete production chain: regolith → iron ore (141 kg) → pig iron (70.5 kg) → steel ingot (67 kg) → steel plate (63 kg).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 1: Produce iron ore and carbon for steel plate."
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
    item: plate_rolling_mill
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
    item: rolling_mill_or_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 1a: Mine mare regolith for iron ore (need ~141 kg for 67 kg steel_ingot)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 24
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Mined 2400 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract 141 kg iron ore from regolith (235 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 235
- cmd: sim.advance-time
  args:
    hours: 294
- cmd: sim.note
  args:
    style: success
    message: "Extracted 141 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith for carbon (need ~36 kg carbon_reducing_agent)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: success
    message: "Mined 1250 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract 36 kg carbon_reducing_agent (122 batches reductant)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 122
- cmd: sim.advance-time
  args:
    hours: 183
- cmd: sim.note
  args:
    style: success
    message: "Extracted 35.4 kg carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 36
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: success
    message: "Produced 36 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce 70.5 kg iron_pig_or_ingot from iron ore and carbon."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 70.5
- cmd: sim.advance-time
  args:
    hours: 847
- cmd: sim.note
  args:
    style: success
    message: "Produced 70.5 kg iron_pig_or_ingot from regolith materials."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Produce 67 kg steel_ingot from pig iron."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 67
- cmd: sim.advance-time
  args:
    hours: 735
- cmd: sim.note
  args:
    style: success
    message: "Produced 67 kg steel_ingot from regolith."
```

## Stage 3: ISRU Phase 2 - Produce regolith steel for fasteners

Commentary: Need 2 kg steel_stock for fastener_kit_medium. Use complete steel production chain from regolith.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 2: Produce steel stock for fasteners from regolith."
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
    item: crucible_refractory
    quantity: 2
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
    item: cutting_tools_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine mare regolith for iron ore (need 6 kg for 2 kg steel_stock)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Mined 200 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract 4.2 kg ilmenite from regolith (need 7 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Extracted 5 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Mine carbonaceous regolith for carbon (need 70 kg for 7 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Mined 100 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Extract 2 kg carbon_reducing_agent (7 batches of reductant for 2 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Extracted 2.03 kg carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 4: Produce 2 kg steel_stock from regolith iron and carbon."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 kg steel_stock from regolith."
```

## Stage 4: ISRU Phase 3 - Manufacture steel components

Commentary: Convert steel_ingot to steel_plate_or_sheet, then manufacture structural_frame_large and fastener_kit_medium.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 3: Manufacture steel components from regolith materials."
- cmd: sim.import
  args:
    item: cnc_mill
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
    item: welding_tools_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_treatment_furnace
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
- cmd: sim.note
  args:
    style: info
    message: "Step 5a: Roll steel_ingot into steel_plate_or_sheet (need 63 kg from 67 kg ingot)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 63
- cmd: sim.advance-time
  args:
    hours: 315
- cmd: sim.note
  args:
    style: success
    message: "Produced 63 kg steel_plate_or_sheet from regolith steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 5b: Manufacture structural_frame_large from regolith steel plate (63 kg → 60 kg + 3 kg scrap)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_frame_large_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Manufactured structural_frame_large (60 kg) from regolith steel with 3 kg scrap losses."
- cmd: sim.note
  args:
    style: info
    message: "Step 5c: Manufacture fastener_kit_medium from regolith steel stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Manufactured fastener_kit_medium from regolith steel."
```

## Stage 5: ISRU Phase 4 - Final assembly with ISRU components

Commentary: Assemble lifting_equipment using regolith-derived steel components (structural_frame_large and fastener_kit_medium) plus imported electronics and motors.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 4: Final assembly with ISRU steel components."
- cmd: sim.import
  args:
    item: electric_motor_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: worm_gear_set_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_sealed
    quantity: 2
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
    recipe: recipe_lifting_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: milestone
    message: "Lifting equipment built with ISRU steel components!"
- cmd: sim.provenance
  args:
    item: lifting_equipment
```
