# Plate Rolling Mill Runbook

Goal: Build `plate_rolling_mill` (1500 kg heavy machinery) using maximum in-situ resources from regolith-derived steel and metal.

## Machine Details
- **Mass**: 1500 kg
- **Purpose**: Rolling mill for producing metal plate from ingots or billets
- **Capabilities**: copper_strip_thin_production_v0, steel_bar_stock_rolling_v0, steel_strip_thin_production_v0

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: plate_rolling_mill_runbook
- cmd: sim.reset
  args:
    sim-id: plate_rolling_mill_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting plate_rolling_mill runbook."
```

## Stage 1: Import tooling and assembly equipment

Commentary: Import fabrication tooling used throughout the ISRU build.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 1: Import tooling and assembly equipment."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 4
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
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
    ensure: true
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
    item: surface_grinder
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: grinding_wheels
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
    item: hand_tools_basic
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
    item: heat_treatment_furnace
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
    item: roll_grinding_lathe_or_cylindrical_grinder_v0
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
    item: dynamic_balancing_stand_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: forge_or_induction_heater_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_hammer_or_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: anvil_or_die_set
    quantity: 1
    unit: unit
    ensure: true
```

## Stage 2: ISRU Phase 1 - Produce regolith steel for machined parts

Commentary: Need steel billet for machined parts and steel plate/stock for the frame. Produce from regolith steel via the steel chain.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 1: Mine regolith and produce steel for machined parts."
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
- cmd: sim.import
  args:
    item: heating_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 1a: Mine mare regolith for iron extraction (need ~1240 kg iron ore)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 21
- cmd: sim.advance-time
  args:
    hours: 26
- cmd: sim.note
  args:
    style: success
    message: "Mined 2100 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract ilmenite from regolith for iron ore (need ~1240 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 2100
- cmd: sim.advance-time
  args:
    hours: 2300
- cmd: sim.note
  args:
    style: success
    message: "Extracted 1260 kg iron_ore_or_ilmenite from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith for carbon extraction (need ~320 kg carbon)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 220
- cmd: sim.advance-time
  args:
    hours: 1360
- cmd: sim.note
  args:
    style: success
    message: "Mined 11000 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract carbon from carbonaceous regolith (need ~320 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 1100
- cmd: sim.advance-time
  args:
    hours: 1700
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~320 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Convert carbon_reductant to carbon_reducing_agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 320
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: success
    message: "Converted 320 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce 620 kg pig iron for steel production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 620
- cmd: sim.advance-time
  args:
    hours: 2700
- cmd: sim.note
  args:
    style: success
    message: "Produced 620 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Produce 260 kg steel_billet_or_slab for precision machining."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_billet_or_slab_v0
    quantity: 260
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.note
  args:
    style: success
    message: "Produced 260 kg steel_billet_or_slab."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Produce 322 kg steel_ingot for frame plate and welding rod."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 322
- cmd: sim.advance-time
  args:
    hours: 3500
- cmd: sim.note
  args:
    style: success
    message: "Produced 322 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3d: Roll steel_plate_or_sheet for frame gussets (need 280 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 280
- cmd: sim.advance-time
  args:
    hours: 210
- cmd: sim.note
  args:
    style: success
    message: "Produced 280 kg steel_plate_or_sheet."
- cmd: sim.note
  args:
    style: info
    message: "Step 3e: Produce metal_sheet_or_plate for welding rod (need 28 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_sheet_or_plate_v0
    quantity: 28
- cmd: sim.advance-time
  args:
    hours: 85
- cmd: sim.note
  args:
    style: success
    message: "Produced 28 kg metal_sheet_or_plate."
- cmd: sim.note
  args:
    style: info
    message: "Step 3f: Form welding_rod_steel from sheet stock (need 28 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_rod_steel_v0
    quantity: 28
- cmd: sim.advance-time
  args:
    hours: 125
- cmd: sim.note
  args:
    style: success
    message: "Produced 28 kg welding_rod_steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 3i: Produce 200 kg machined_steel_part_precision from local steel."
- cmd: sim.import
  args:
    item: cutting_fluid
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: coating_compound
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_steel_part_precision_v0
    quantity: 200
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: success
    message: "Produced 200 kg machined_steel_part_precision."
```

## Stage 3: ISRU Phase 2 - Produce regolith metal for fasteners and frame stock

Commentary: Need regolith_metal_crude for fasteners, beams, and bar stock. Use MRE process.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 2: Produce regolith metal for fasteners and frame stock."
- cmd: sim.import
  args:
    item: mre_reactor_v0
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
    item: electrodes
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 4a: Run MRE to produce regolith_metal_crude (need ~710 kg total)."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 12160
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: success
    message: "Produced ~730 kg regolith_metal_crude via MRE."
- cmd: sim.note
  args:
    style: info
    message: "Step 4b: Form steel_beam_i_section for frame (need 552 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_beam_i_section_isru_v0
    quantity: 9.2
- cmd: sim.advance-time
  args:
    hours: 55
- cmd: sim.note
  args:
    style: success
    message: "Produced 552 kg steel_beam_i_section."
- cmd: sim.note
  args:
    style: info
    message: "Step 4c: Produce steel_stock_bar_or_billet from regolith metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 0.18
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: success
    message: "Produced ~49 kg steel_stock_bar_or_billet."
- cmd: sim.note
  args:
    style: info
    message: "Step 4d: Roll steel_bar_stock for frame reinforcements (need 46 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 46
- cmd: sim.advance-time
  args:
    hours: 125
- cmd: sim.note
  args:
    style: success
    message: "Produced 46 kg steel_bar_stock."
```

## Stage 4: ISRU Phase 3 - Manufacture fasteners from ISRU materials

Commentary: Manufacture fastener_kit_large from regolith metal.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 3: Manufacture fasteners from regolith materials."
- cmd: sim.note
  args:
    style: info
    message: "Step 6a: Manufacture fastener_kit_large from regolith metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 70
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 fastener_kit_large from regolith metal."
```

## Stage 5: ISRU Phase 4 - Build structural steel frame

Commentary: Fabricate the heavy frame from ISRU beams, plate, bar stock, and welding rod.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 4: Build structural steel frame from ISRU stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_steel_frame_v0
    quantity: 1.84
- cmd: sim.advance-time
  args:
    hours: 320
- cmd: sim.note
  args:
    style: success
    message: "Produced ~902 kg structural_steel_frame."
```

## Stage 6: ISRU Phase 5 - Final assembly with ISRU components

Commentary: Assemble plate_rolling_mill using regolith-derived frame and machined steel parts. Import precision components (rolls, motor, electronics, fasteners).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 5: Final assembly with ISRU components."
- cmd: sim.import
  args:
    item: rolling_mill_rolls_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_system_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_electronics_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: kit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_plate_rolling_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: milestone
    message: "Plate rolling mill built with maximum ISRU components!"
- cmd: sim.provenance
  args:
    item: plate_rolling_mill
    quantity: 1
    unit: unit
```

## Summary

**Current ISRU:** 71.6% for plate_rolling_mill; overall runbook ISRU 42.9%.

**Regolith-derived materials (in-situ):**
- Mare regolith → Iron ore → Pig iron → Steel billet (260 kg) → Machined steel parts (200 kg)
- Mare regolith → Iron ore → Pig iron → Steel ingot (322 kg) → Plate/sheet + welding rod
- Carbonaceous regolith → Carbon reductant → Reducing agent (320 kg)
- Mare regolith → MRE → Regolith metal crude (~730 kg) → Beams + bar stock + fasteners
- ISRU steel stock → Structural steel frame (~902 kg)

**Still imported for assembly:**
- Hydraulic system medium and power electronics module
- Rolling mill rolls set (200 kg)
- Fastener kit medium (recipe requirement)
- Note: fastener_kit_large ISRU output is not consumed by the current machine recipe

**Mass breakdown (provenance):**
- Total plate_rolling_mill mass: 1501 kg
- In-situ contribution: 1074.46 kg (71.6% current run)
- Imported contribution: 426.54 kg (28.4% current run)

**Process flow:**
1. Mare regolith → Iron ore → Pig iron → Steel billet (260 kg)
2. Carbonaceous regolith → Carbon reducing agent (for steelmaking)
3. Steel billet → Machined steel parts (200 kg)
4. Steel ingot → Plate/sheet + welding rod
5. Regolith metal → Beams + bar stock → Structural steel frame (~902 kg)
6. Regolith metal → Fasteners (2 units)
7. Import rolls, hydraulics, electronics, fasteners
8. Assemble → Integrate → Test → Complete rolling mill

**Path to higher ISRU:**
- Develop precision roll manufacturing from regolith steel
- Locally manufacture electric motors
- Develop wire drawing for electrical conductors
- Target: 70-80% ISRU achievable with complete component manufacturing
