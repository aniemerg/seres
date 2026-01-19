# High-Temperature Furnace Runbook

Goal: Build `furnace_high_temp` using maximum in-situ resources.

## Machine Details
- **Mass**: 800 kg
- **Material Class**: machine
- **Capabilities**: High-temperature furnace (1600-3000°C) for carbothermal reduction, sintering, tungsten processing

## Required Components (from recipe)
1. furnace_shell_refractory (300 kg) - ISRU from regolith metal + refractory
2. heating_element_set_high_temp (80 kg) - ISRU from regolith metal
3. insulation_pack_high_temp (100 kg) - ISRU from regolith-based insulation
4. chamber_shell_sealed (150 kg) - ISRU from regolith sheet metal
5. gas_handling_system (60 kg) - import (valves, regulators)
6. cooling_loop_basic (50 kg) - partially ISRU (tubing from regolith)
7. temperature_controller_module (12 kg) - import (sensors, electronics)
8. control_panel_basic (20 kg) - import (controls, interface)
9. fastener_kit_medium (10 kg) - ISRU from regolith steel

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: furnace_high_temp_runbook
- cmd: sim.reset
  args:
    sim-id: furnace_high_temp_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting furnace_high_temp runbook."
```

## Build furnace_high_temp with ISRU materials

Commentary: Import machines and non-ISRU components, produce ISRU materials from regolith, then build.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import machines and equipment."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 4
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
    item: sintering_furnace_v0
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
    item: milling_machine_general_v0
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
    item: assembly_tools_basic
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
    item: crucible_refractory
    quantity: 2
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
    item: hand_tools_basic
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
    item: surface_grinder
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
    item: fixturing_workbench
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drying_oven
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: powder_mixer
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hot_press_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: dies
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_ram_set
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
    item: forging_press_v0
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
    item: precision_lathe
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
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_metal_crude via MRE (need ~1150 kg for all metal components including chamber shell)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1150
- cmd: sim.advance-time
  args:
    hours: 5200
- cmd: sim.note
  args:
    style: success
    message: "Produced regolith_metal_crude via MRE."
- cmd: sim.note
  args:
    style: info
    message: "Produce furnace_shell_refractory from regolith (300 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_shell_refractory_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: info
    message: "Produce heating_element_set_high_temp from regolith (80 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_element_set_high_temp_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: info
    message: "Produce more regolith_powder for insulation (need 120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_powder_v0
    quantity: 130
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: info
    message: "Produce thermal_insulation_regolith_based_v0 (120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_regolith_based_v0
    quantity: 120
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.note
  args:
    style: info
    message: "Produce insulation_pack_high_temp from regolith insulation (100 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Produce sheet_metal_or_structural_steel from regolith (for chamber shell)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Produce chamber_shell_sealed from regolith-based sheet metal (150 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_chamber_shell_sealed_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: info
    message: "Produce cooling_loop_basic with regolith tubing."
- cmd: sim.import
  args:
    item: circulation_pump_coolant
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: metal_feedstock
    quantity: 60
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_cooling_loop_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce fastener_kit_medium from regolith steel."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: info
    message: "Import non-ISRU components."
- cmd: sim.import
  args:
    item: gas_handling_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble furnace_high_temp from ISRU and imported components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_high_temp_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.note
  args:
    style: success
    message: "High-temperature furnace built with ISRU materials!"
- cmd: sim.provenance
  args:
    item: furnace_high_temp
```
