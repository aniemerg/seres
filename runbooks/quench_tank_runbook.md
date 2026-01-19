# Quench Tank Runbook

Goal: Build `quench_tank` with ISRU steel for the tank shell, pump, lid/basket, and fasteners where practical.

## Machine Details
- **Mass**: 200 kg
- **Material Class**: steel (tank body), electronics (sensors/controls)
- **Capabilities**: Rapid cooling of heat-treated parts with optional agitation

## Required Components (from recipe)
1. tank_shell_steel (150 kg)
2. agitation_pump_small (15 kg)
3. tank_lid_and_basket (6 kg)
4. level_sensor_basic (5 kg)
5. power_conditioning_module (1 kg)
6. sensor_suite_general (1 kg)
7. control_compute_module_imported (2 kg)
8. fastener_kit_small (1.3 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: quench_tank_runbook
- cmd: sim.reset
  args:
    sim-id: quench_tank_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting quench_tank runbook."
```

## ISRU Phase 1: Import tooling and equipment

Commentary: Import fabrication tooling and equipment needed for steel processing and assembly.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 1: Import tooling and equipment."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: surface_grinder
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
    item: dust_collection_system
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
```

## ISRU Phase 2: Produce regolith_metal_crude for tank shell and pump

Commentary: Produce regolith_metal_crude via MRE for tank shell (177 kg needed) and pump (16 kg needed).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 2: Produce regolith_metal_crude for tank shell and pump."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 4000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Produce regolith_metal_crude for tank shell (177 kg) and pump (16 kg) = 193 kg total."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 8.6
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: success
    message: "Produced ~193 kg regolith_metal_crude via MRE."
```

## ISRU Phase 3: Produce steel materials for lid/basket and fasteners

Commentary: Produce steel ingot and steel_stock from regolith for tank lid/basket components and fasteners.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 3: Produce steel for lid/basket and fasteners."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Mine mare regolith for iron ore (~25 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 0.9
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Mined 90 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Extract ilmenite for iron ore."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 42
- cmd: sim.advance-time
  args:
    hours: 48
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~25 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Mine carbonaceous regolith for reducing agent (~10 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Mined 350 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 3d: Extract carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 33.5
- cmd: sim.advance-time
  args:
    hours: 65
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~10 kg carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 10.0
- cmd: sim.advance-time
  args:
    hours: 25
- cmd: sim.note
  args:
    style: success
    message: "Produced 10 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3e: Smelt pig iron and produce steel ingot for metal_sheet (3.4 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 3.4
- cmd: sim.advance-time
  args:
    hours: 18
- cmd: sim.note
  args:
    style: success
    message: "Produced 3.4 kg iron_pig_or_ingot."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 3.2
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Produced 3.2 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3f: Import metal_sheet (3 kg - no direct ISRU recipe from steel_ingot)."
- cmd: sim.import
  args:
    item: metal_sheet
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 3g: Produce steel_stock for basket bars and fasteners (6.5 kg total)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 6.5
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Produced 4.5 kg steel_stock."
```

## ISRU Phase 4: Build ISRU components

Commentary: Build tank shell, pump, lid/basket, and fasteners from ISRU materials.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 4: Build ISRU components."
- cmd: sim.note
  args:
    style: info
    message: "Step 4a: Build tank_shell_steel from regolith metal (160 kg sheet metal needed)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_isru_v0
    quantity: 0.73
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Produced ~160 kg sheet_metal_or_structural_steel."
- cmd: sim.run-recipe
  args:
    recipe: recipe_tank_shell_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Built 150 kg tank_shell_steel from regolith metal."
- cmd: sim.note
  args:
    style: info
    message: "Step 4b: Build agitation_pump_small from regolith metal (15 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_agitation_pump_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Built 15 kg agitation_pump_small from regolith metal."
- cmd: sim.note
  args:
    style: info
    message: "Step 4c: Produce fastener_kit_small from ISRU steel_stock (2 units = 2.6 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 fastener_kit_small from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 4d: Build tank_lid_and_basket from ISRU materials."
- cmd: sim.run-recipe
  args:
    recipe: recipe_tank_lid_and_basket_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Built tank_lid_and_basket from regolith steel."
```

## ISRU Phase 5: Import electronics and assemble

Commentary: Import sensors and control modules (no ISRU recipes available). Assemble quench_tank.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 5: Import electronics and assemble quench_tank."
- cmd: sim.import
  args:
    item: level_sensor_basic
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bulk_material_or_parts
    quantity: 200
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Assemble quench_tank from ISRU and imported components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_quench_tank_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Quench tank assembled with high ISRU content!"
- cmd: sim.provenance
  args:
    item: quench_tank
    quantity: 1
    unit: unit
```
