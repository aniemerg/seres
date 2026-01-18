# Drying Oven Runbook

Goal: Build `drying_oven` using in-situ resources where possible.

## Machine Details
- **Mass**: TBD
- **Capabilities**: drying, low-temperature heat treatment

## Required Components (from recipe)
1. structural_steel_frame (60 kg)
2. insulation_panel_high_temp (30 kg)
3. heating_element_resistive (4 unit)
4. temperature_controller_basic (1 unit)
5. power_electronics_module (1 unit)
6. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: drying_oven_runbook
- cmd: sim.reset
  args:
    sim-id: drying_oven_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting drying_oven runbook."
```

## ISRU Build: Drying Oven with Regolith-Derived Components

Commentary: Produce structural_steel_frame, insulation_panel_high_temp, and fastener_kit_medium from regolith. Import electronics and heating elements.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce structural frame, insulation, and fasteners from regolith."
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
- cmd: sim.import
  args:
    item: heating_furnace
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
    item: cutting_tools_general
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
    item: milling_machine_general_v0
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
    item: ball_mill_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 3000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Mine regolith and produce steel for structural frame (need ~66 kg steel_stock)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 231
- cmd: sim.advance-time
  args:
    hours: 231
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 24
- cmd: sim.advance-time
  args:
    hours: 192
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 117
- cmd: sim.advance-time
  args:
    hours: 176
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 35
- cmd: sim.advance-time
  args:
    hours: 70
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 66
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_metal_crude for steel beams (70 kg via MRE)."
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
    item: generic_chemical_reactor_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 16
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: info
    message: "Produce steel_beam_i_section for structural frame (300 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_beam_i_section_isru_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: info
    message: "Produce steel_plate_or_sheet for structural frame (150 kg)."
- cmd: sim.import
  args:
    item: iron_ore_or_ilmenite
    quantity: 330
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 83
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 165
- cmd: sim.advance-time
  args:
    hours: 1650
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 157
- cmd: sim.advance-time
  args:
    hours: 1570
- cmd: sim.import
  args:
    item: steel_ingot
    quantity: 2
    unit: kg
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 150
- cmd: sim.advance-time
  args:
    hours: 750
- cmd: sim.note
  args:
    style: info
    message: "Produce structural_steel_frame from regolith steel (60 kg)."
- cmd: sim.import
  args:
    item: hydraulic_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 25
    unit: kg
- cmd: sim.import
  args:
    item: welding_rod_steel
    quantity: 15
    unit: kg
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_steel_frame_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith-based insulation for panels (30 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_powder_v0
    quantity: 35
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.import
  args:
    item: regolith_powder
    quantity: 3
    unit: kg
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_regolith_based_v0
    quantity: 35
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: info
    message: "Produce insulation_panel_high_temp from regolith insulation."
- cmd: sim.import
  args:
    item: sintering_furnace_v0
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
    item: pressing_tools
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: kiln_ceramic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ceramic_fiber_slurry
    quantity: 40
    unit: kg
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_panel_high_temp_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 25
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
    style: milestone
    message: "Import electronics and heating elements, then assemble drying oven."
- cmd: sim.import
  args:
    item: heating_element_resistive
    quantity: 4
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
    item: power_electronics_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_drying_oven_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: drying_oven with regolith-derived structural components."
- cmd: sim.provenance
  args:
    item: drying_oven
    quantity: 1
    unit: unit
```
