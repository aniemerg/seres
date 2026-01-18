# Hot Press v0 Runbook

Goal: Build `hot_press_v0` and maximize ISRU by producing local steel, insulation, and heating elements.

## Machine Details
- **Mass**: 950 kg
- **Material Class**: steel
- **Capabilities**: High-temperature hot press for sintering/consolidation.

## Required Components (from recipe)
1. hot_press_frame (1 unit)
2. hydraulic_system_medium (1 unit)
3. heated_platen_set (1 unit)
4. heating_element_set_high_temp (1 unit)
5. insulation_pack_high_temp (1 unit)
6. temperature_sensing (1 unit)
7. control_compute_module_imported (1 unit)
8. sensor_suite_general (1 unit)
9. power_conditioning_module (1 unit)
10. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: hot_press_v0_runbook
- cmd: sim.reset
  args:
    sim-id: hot_press_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting hot_press_v0 runbook."
```

## Stage 1: Import baseline equipment and non-ISRU components

Commentary: Import tooling for mining, casting, machining, rolling, and assembly. Import electronics and specialty components that remain non-ISRU.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 1: Import baseline tooling and non-ISRU components."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: hand_tools_basic
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
    item: saw_or_cutting_tool
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
    item: furnace_basic
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
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: temperature_sensing
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
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_electric
    quantity: 8
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: thermocouple_type_k_v0
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_heavy
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 4
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_seals_set
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: piping_components
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cutting_fluid
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_control_valve_set
    quantity: 2
    unit: kg
    ensure: true
```

## Stage 2: ISRU metal feedstocks (regolith metal + steel ingot chain)

Commentary: Produce regolith metal for heating elements and bar stock, then produce steel ingots for plate and frame.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Produce regolith metal and steel ingots."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Produce regolith_metal_crude (~110 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4.8
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.note
  args:
    style: success
    message: "Produced ~109 kg regolith_metal_crude."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Roll regolith metal into steel_stock_bar_or_billet (~27 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 0.1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Produced ~27 kg steel_stock_bar_or_billet."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Roll bar stock for hydraulic system (25 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Produced 25 kg steel_bar_stock."
- cmd: sim.note
  args:
    style: info
    message: "Step 2d: Mine mare regolith for ilmenite extraction (2300 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 23
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.note
  args:
    style: success
    message: "Mined 2300 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 2e: Extract ilmenite/iron ore (target ~1380 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 2300
- cmd: sim.advance-time
  args:
    hours: 2400
- cmd: sim.note
  args:
    style: success
    message: "Produced ~1380 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 2f: Collect carbonaceous regolith (~12100 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 242
- cmd: sim.advance-time
  args:
    hours: 1500
- cmd: sim.note
  args:
    style: success
    message: "Collected ~12100 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2g: Extract carbon_reductant (~350 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 1207
- cmd: sim.advance-time
  args:
    hours: 2000
- cmd: sim.note
  args:
    style: success
    message: "Produced ~350 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2h: Convert to carbon_reducing_agent (350 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 350
- cmd: sim.advance-time
  args:
    hours: 800
- cmd: sim.note
  args:
    style: success
    message: "Produced 350 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 2i: Smelt iron pig (683 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 683
- cmd: sim.advance-time
  args:
    hours: 3000
- cmd: sim.note
  args:
    style: success
    message: "Produced 683 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 2j: Refine steel ingots (650 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 650
- cmd: sim.advance-time
  args:
    hours: 2100
- cmd: sim.note
  args:
    style: success
    message: "Produced 650 kg steel_ingot."
```

## Stage 3: ISRU steel stock for plates and machined parts

Commentary: Roll plate for frame, platens, and machined parts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 3: Produce steel plate and machined parts stock."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Roll steel_plate_or_sheet (200 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 200
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: success
    message: "Produced 200 kg steel_plate_or_sheet."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Cut steel plate into cut_parts (80 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 8.5
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Produced ~80 kg cut_parts."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Machine cut_parts into machined_part_raw (80 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 90
- cmd: sim.note
  args:
    style: success
    message: "Produced 80 kg machined_part_raw."
```

## Stage 4: ISRU insulation pack (regolith-based)

Commentary: Produce regolith powder and form insulation pack locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 4: Produce insulation_pack_high_temp from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 4a: Mine mare regolith for insulation feedstock (~1000 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Mined 1000 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 4b: Screen regolith to coarse fraction."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_coarse_fraction_v0
    quantity: 1000
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: success
    message: "Produced ~600 kg regolith_coarse_fraction."
- cmd: sim.note
  args:
    style: info
    message: "Step 4c: Grind to regolith_powder (~120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_powder_v0
    quantity: 127
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Produced ~121 kg regolith_powder."
- cmd: sim.note
  args:
    style: info
    message: "Step 4d: Convert to thermal_insulation_regolith_based_v0 (120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_regolith_based_v0
    quantity: 120
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Produced 120 kg thermal_insulation_regolith_based_v0."
- cmd: sim.note
  args:
    style: info
    message: "Step 4e: Assemble insulation_pack_high_temp from regolith insulation."
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 insulation_pack_high_temp."
```

## Stage 5: Build ISRU subcomponents

Commentary: Build hot press frame, hydraulic system, heated platens, and heating elements with local steel inputs.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 5: Build ISRU subcomponents."
- cmd: sim.note
  args:
    style: info
    message: "Step 5a: Build hot_press_frame (steel ingot + fasteners)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_hot_press_frame_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 hot_press_frame."
- cmd: sim.note
  args:
    style: info
    message: "Step 5b: Build heating_element_set_high_temp (regolith metal + machined parts)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_element_set_high_temp_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 heating_element_set_high_temp."
- cmd: sim.note
  args:
    style: info
    message: "Step 5c: Build heated_platen_set (steel plate + imported heaters/sensors)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_heated_platen_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 heated_platen_set."
- cmd: sim.note
  args:
    style: info
    message: "Step 5d: Build hydraulic_system_medium (local steel + imported seals/valves/fluid)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_system_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 hydraulic_system_medium."
```

## Stage 6: Final assembly

Commentary: Assemble hot_press_v0 and verify provenance.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 6: Assemble hot_press_v0."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_hot_press_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: milestone
    message: "Hot press v0 assembled."
- cmd: sim.provenance
  args:
    item: hot_press_v0
    quantity: 1
    unit: unit
```
