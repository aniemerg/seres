# Hydraulic Press Runbook

Goal: Build `hydraulic_press` (600 kg machine) using maximum in-situ resources. Start with imported materials for baseline, then produce frame from regolith-derived steel.

## Machine Details
- **Mass**: 600 kg
- **Purpose**: General-purpose hydraulic press for forming and compaction
- **Components**: Steel frame (150 kg), hydraulic cylinder, hydraulic power unit, controls

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: hydraulic_press_runbook
- cmd: sim.reset
  args:
    sim-id: hydraulic_press_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting hydraulic_press runbook."
```

## ISRU Phase 1: Produce regolith steel for frame

Commentary: Need 150 kg steel plate for frame. Produce from regolith steel via complete steel chain.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel from regolith for frame."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: cutting_tools_general
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
    item: assembly_tools_basic
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
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 1a: Mine mare regolith for iron extraction (need ~332 kg iron ore)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: success
    message: "Mined 600 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract ilmenite from regolith for iron ore (need ~332 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 554
- cmd: sim.advance-time
  args:
    hours: 560
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~332 kg iron_ore_or_ilmenite from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith for carbon extraction (need ~83 kg carbon)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 56
- cmd: sim.advance-time
  args:
    hours: 350
- cmd: sim.note
  args:
    style: success
    message: "Mined 2800 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract carbon from carbonaceous regolith (need ~83 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 277
- cmd: sim.advance-time
  args:
    hours: 420
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~83.1 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Convert carbon_reductant to carbon_reducing_agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 83
- cmd: sim.advance-time
  args:
    hours: 170
- cmd: sim.note
  args:
    style: success
    message: "Converted ~83 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce 166 kg pig iron for steel production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 166
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: success
    message: "Produced 166 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Produce 158 kg steel_ingot for frame."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 158
- cmd: sim.advance-time
  args:
    hours: 500
- cmd: sim.note
  args:
    style: success
    message: "Produced 158 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Cast steel_ingot into steel_plate_raw (need 150 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 150
- cmd: sim.advance-time
  args:
    hours: 130
- cmd: sim.note
  args:
    style: success
    message: "Produced 150 kg steel_plate_raw from regolith steel."
```

## ISRU Phase 2: Produce fasteners from regolith metal

Commentary: Produce fastener_kit_large (1 unit) for the final assembly.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 2: Produce fasteners from regolith metal."
- cmd: sim.note
  args:
    style: info
    message: "Step 4a: Manufacture fastener_kit_large for assembly."
- cmd: sim.import
  args:
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_metal_crude
    quantity: 15
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Produced fastener_kit_large from regolith metal."
```

## ISRU Phase 3: Final assembly with regolith frame

Commentary: Assemble hydraulic_press using regolith-derived steel frame and fasteners. Import hydraulic components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 3: Final assembly with regolith frame."
- cmd: sim.import
  args:
    item: hydraulic_cylinder_large
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_power_unit_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_press_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: milestone
    message: "Hydraulic press built with regolith steel frame!"
- cmd: sim.provenance
  args:
    item: hydraulic_press
    quantity: 1
    unit: unit
```

## Summary

**Target ISRU: ~23% by mass (runbook provenance)** - Good ISRU through regolith steel for frame!

**Regolith-derived materials (in-situ):**
- Mare regolith (600 kg mined) → Iron ore (~332 kg via ilmenite extraction)
- Carbonaceous regolith (2800 kg mined) → Carbon reductant (~83 kg) → Reducing agent (~83 kg)
- Pig iron (166 kg) → Steel ingot (158 kg) → Steel plate (150 kg): For press frame
- Fastener kit (1 unit): For assembly

**Still imported:**
- Hydraulic cylinder large (40 kg) - precision cylinder with seals
- Hydraulic power unit basic (150 kg) - pump, motor, reservoir, valves
- Control compute module - control electronics
- All machines (labor bots, furnaces, machining tools) - one-time Earth imports

**Process flow:**
1. Mare regolith → Iron ore → Pig iron → Steel ingot → Steel plate (150 kg)
2. Carbonaceous regolith → Carbon reducing agent (for steelmaking)
3. Regolith metal → Fastener kit (1 unit)
4. Weld frame + install hydraulic components → Complete press

**Path to higher ISRU:**
- Manufacture hydraulic cylinder from regolith steel tubing and bar stock
- Manufacture hydraulic reservoir from regolith sheet metal
- Develop hydraulic pump manufacturing
- Locally produce electric motors
- Target: 70-80% ISRU achievable with complete hydraulic component manufacturing
