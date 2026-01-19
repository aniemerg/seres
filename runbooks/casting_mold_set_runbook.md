# Casting Mold Set Runbook

Goal: Build `casting_mold_set` using in-situ resources where possible.

## Machine Details
- **Mass**: 100 kg
- **Capabilities**: casting, molding

## Required Components (from recipe)
1. sand_casting_flask_set (3 units)
2. permanent_mold_steel_set (2 units)
3. casting_patterns_wooden (5 units)
4. cope_and_drag_boards (2 units)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: casting_mold_set_runbook
- cmd: sim.reset
  args:
    sim-id: casting_mold_set_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting casting_mold_set runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all components and assembly equipment to test if the recipe runs.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment and parts for assembly."
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
    item: welding_tools_set
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
    item: press_brake
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
    item: sand_casting_flask_set
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: permanent_mold_steel_set
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_patterns_wooden
    quantity: 5
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cope_and_drag_boards
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble casting mold set from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_casting_mold_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Baseline casting_mold_set complete."
```

## Stage 2: ISRU Phase 1 - Produce regolith steel for steel plate components

Commentary: Need 180 kg steel plate total (3 sand flasks × 60 kg each). Produce from regolith steel via complete steel chain.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 1: Mine regolith and produce steel for plate components."
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
    item: rolling_mill_v0
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
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 1a: Mine mare regolith for iron extraction (need ~662 kg regolith for ~397 kg ore)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: success
    message: "Mined 700 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract ilmenite from regolith for iron ore (need ~398 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 664
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~398 kg iron_ore_or_ilmenite from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith for carbon extraction (need ~100 kg carbon_reducing_agent)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 69
- cmd: sim.advance-time
  args:
    hours: 500
- cmd: sim.note
  args:
    style: success
    message: "Mined 3450 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract carbon from carbonaceous regolith (need ~100 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 345
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~100 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Convert carbon_reductant to carbon_reducing_agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 100.05
- cmd: sim.advance-time
  args:
    hours: 250
- cmd: sim.note
  args:
    style: success
    message: "Converted ~100 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce ~199 kg pig iron for steel production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 199
- cmd: sim.advance-time
  args:
    hours: 850
- cmd: sim.note
  args:
    style: success
    message: "Produced ~199 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Produce 189 kg steel_ingot for plate rolling."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 189
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: success
    message: "Produced 189 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Roll steel_ingot into steel_plate_or_sheet (need 180 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 180
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.note
  args:
    style: success
    message: "Produced 180 kg steel_plate_or_sheet from regolith steel."
```

## Stage 3: ISRU Phase 2 - Produce regolith metal for permanent molds

Commentary: Need 104 kg regolith_metal_crude for permanent mold set (2 units × 52 kg each). Use MRE process directly.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 2: Produce regolith metal for permanent molds via MRE."
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
    message: "Step 4a: Run MRE to produce regolith_metal_crude (need 104+ kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Produced ~114 kg regolith_metal_crude via MRE."
```

## Stage 4: ISRU Phase 3 - Manufacture all components from ISRU materials

Commentary: Manufacture sand flasks and permanent molds from regolith materials. Import wooden patterns and cope/drag boards (unit mismatch in KB).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 3: Manufacture all components from regolith materials."
- cmd: sim.import
  args:
    item: silica_purified
    quantity: 40
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: binder_material
    quantity: 4
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 5a: Manufacture sand_casting_flask_set (3 units) from regolith steel plate."
- cmd: sim.run-recipe
  args:
    recipe: recipe_sand_casting_flask_set_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Produced 3 sand_casting_flask_set from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 5b: Manufacture permanent_mold_steel_set (2 units) from regolith metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_permanent_mold_steel_set_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 permanent_mold_steel_set from regolith metal."
- cmd: sim.note
  args:
    style: info
    message: "Step 5c: Import wooden patterns (cellulose_raw not available from regolith)."
- cmd: sim.import
  args:
    item: casting_patterns_wooden
    quantity: 5
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 5d: Import cope_and_drag_boards (KB uses unit while recipe outputs kg)."
- cmd: sim.import
  args:
    item: cope_and_drag_boards
    quantity: 2
    unit: unit
    ensure: true
```

## Stage 5: ISRU Phase 4 - Final assembly with ISRU components

Commentary: Assemble complete casting_mold_set from regolith-derived components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 4: Final assembly with ISRU components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_casting_mold_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: milestone
    message: "Casting mold set built with maximum ISRU components!"
- cmd: sim.provenance
  args:
    item: casting_mold_set
    quantity: 1
    unit: unit
```

## Summary

**Target ISRU: TBD** - ISRU paths enabled for steel plate and permanent molds; patterns/boards imported.

**Regolith-derived materials (in-situ):**
- Mare regolith (~700 kg mined total) → Iron ore (~397 kg via ilmenite extraction)
- Carbonaceous regolith (~3450 kg mined) → Carbon reductant (~100 kg) → Reducing agent (~100 kg)
- Pig iron (~198 kg) → Steel ingot (189 kg) → Steel plate (180 kg): For 3 sand flasks
- Mare regolith (MRE) → Regolith metal crude (~114 kg): For 2 permanent mold sets

**Still imported:**
- Wooden patterns (5 units, ~3 kg cellulose_raw) - organic material not available from regolith
- Cope/drag boards (2 units) - KB unit mismatch prevents local build
- Silica purified (40 kg) and binder (4 kg) for permanent mold bonding
- All machines (labor bots, furnaces, rolling mill, MRE reactor) - one-time Earth imports

**Mass breakdown:**
- Total casting_mold_set mass: 100 kg
- In-situ contribution: TBD
- Imported contribution: patterns + boards + silica/binder + tooling

**Process flow:**
1. Mare regolith → Iron ore → Pig iron → Steel ingot → Steel plate (180 kg)
2. Carbonaceous regolith → Carbon reducing agent (for steelmaking)
3. Mare regolith → MRE → Regolith metal crude (~114 kg)
4. Steel plate → Sand flasks + Cope/drag boards (welding/fabrication)
5. Regolith metal → Permanent molds (casting/machining)
6. Assemble → Complete foundry tooling set

**Path to higher ISRU:**
- Develop cellulose substitute or synthetic pattern material from regolith
- Fix cope_and_drag_boards unit mismatch in KB to enable local production
- Locally produce silica and binder from regolith
