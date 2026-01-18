# Coil Winding Machine Runbook

Goal: Build `coil_winding_machine` using in-situ resources where possible.

## Machine Details
- **Mass**: 120 kg
- **Capabilities**: winding, tension_control, motor_driven

## Required Components (from recipe)
1. machine_frame_small (1 unit)
2. spindle_drive_motor_small (1 unit)
3. wire_tensioning_mechanism (1 unit)
4. turn_counter_module (1 unit)
5. control_compute_module_imported (1 unit)
6. power_conditioning_module (1 unit)
7. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: coil_winding_machine_runbook
- cmd: sim.reset
  args:
    sim-id: coil_winding_machine_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting coil_winding_machine runbook."
```

## ISRU Build: Machine Frame, Tensioning Mechanism, and Fasteners

Commentary: Need 50 kg sheet_metal_or_structural_steel for machine_frame_small. Production chain: regolith → iron ore (119 kg) → pig iron (59.5 kg) → steel ingot (56 kg) → sheet metal (50.5 kg).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import equipment and produce steel for machine frame."
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
    item: furnace_basic
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
    message: "Step 1a: Mine mare regolith for iron ore (need ~103 kg for 50 kg steel)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 18
- cmd: sim.advance-time
  args:
    hours: 22
- cmd: sim.note
  args:
    style: success
    message: "Mined 1800 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract 119 kg iron ore from regolith (199 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 199
- cmd: sim.advance-time
  args:
    hours: 249
- cmd: sim.note
  args:
    style: success
    message: "Extracted 119.4 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith for carbon (need ~30 kg carbon_reducing_agent)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 21
- cmd: sim.advance-time
  args:
    hours: 168
- cmd: sim.note
  args:
    style: success
    message: "Mined 1050 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract 30 kg carbon_reducing_agent (104 batches reductant)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 104
- cmd: sim.advance-time
  args:
    hours: 156
- cmd: sim.note
  args:
    style: success
    message: "Extracted 30.2 kg carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Produced 30 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce 59.5 kg iron_pig_or_ingot from iron ore and carbon."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 59.5
- cmd: sim.advance-time
  args:
    hours: 714
- cmd: sim.note
  args:
    style: success
    message: "Produced 59.5 kg iron_pig_or_ingot from regolith materials."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Produce 56 kg steel ingot from pig iron (for sheet metal)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 56
- cmd: sim.advance-time
  args:
    hours: 616
- cmd: sim.note
  args:
    style: success
    message: "Produced 56 kg steel_ingot from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Produce sheet metal from steel ingot (50.35 kg output from 55.65 kg ingot)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_v0
    quantity: 0.53
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: success
    message: "Produced 50.35 kg sheet_metal_or_structural_steel from regolith steel ingot."
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for wire tensioning mechanism."
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
    item: generic_chemical_reactor_v0
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
    message: "Run MRE to produce 6+ kg regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: success
    message: "Produced ~23 kg regolith_metal_crude via MRE (need 6 kg)."
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel stock for fasteners."
- cmd: sim.import
  args:
    item: heating_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Mine additional regolith for fastener steel stock."
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
    message: "Extracted 4.2 kg iron ore."
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
    message: "Extracted 2.1 kg carbon_reductant."
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
- cmd: sim.note
  args:
    style: milestone
    message: "Manufacture components from ISRU materials."
- cmd: sim.import
  args:
    item: metal_shear_or_saw
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
    item: furnace_basic
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
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: saw_or_cutting_tool
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 5a: Manufacture machine_frame_small from regolith steel (50 kg → 47.5 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Manufactured machine_frame_small from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 5b: Manufacture wire_tensioning_mechanism from regolith metal (6 kg → 5 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_wire_tensioning_mechanism_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: success
    message: "Manufactured wire_tensioning_mechanism from regolith metal."
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
- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly with ISRU components."
- cmd: sim.import
  args:
    item: spindle_drive_motor_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: turn_counter_module
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
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_coil_winding_machine_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: coil_winding_machine with ISRU components."
- cmd: sim.provenance
  args:
    item: coil_winding_machine_v0
```
