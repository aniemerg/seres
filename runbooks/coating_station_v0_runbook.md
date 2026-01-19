# Coating Station v0 Runbook

Goal: Build `coating_station_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: TBD
- **Capabilities**: coating, spraying, drying

## Required Components (from recipe)
1. steel_beam_i_section (40 kg)
2. coating_booth_enclosure (1 unit)
3. control_panel_basic (1 unit)
4. electronic_components_set (1 unit)
5. coating_spray_gun_and_pump (1 unit)
6. coating_drying_oven (1 unit)
7. chemical_bath_ventilation (1 unit)
8. fastener_kit_medium (1 unit)
9. enclosure_electrical_medium (1 unit)
10. assembled_electrical_system (1 unit)
11. assembled_equipment (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: coating_station_v0_runbook
- cmd: sim.reset
  args:
    sim-id: coating_station_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting coating_station_v0 runbook."
```

## ISRU Build: Enclosures, Fasteners, and Spray Body

Commentary: Produce sheet metal and fasteners from regolith-derived steel, plus raw metal blocks for the spray gun body. Keep electronics and specialty components imported.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: sheet metal, fasteners, and spray body from regolith."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 4
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
    item: test_bench_electrical
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
    item: plate_rolling_mill
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
- cmd: sim.import
  args:
    item: heat_treatment_furnace
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
- cmd: sim.note
  args:
    style: milestone
    message: "Collect regolith feedstock locally."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 8000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce ilmenite and carbon reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 400
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 200
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.note
  args:
    style: milestone
    message: "Smelt iron and produce steel ingots for sheet metal."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 111
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 105
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel stock for fasteners."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for beam and spray body."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_beam_i_section_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.run-recipe
  args:
    recipe: recipe_raw_metal_block_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: milestone
    message: "Fabricate ISRU enclosure and ventilation."
- cmd: sim.import
  args:
    item: sealing_gaskets
    quantity: 4
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_coating_booth_enclosure_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_bath_ventilation_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble spray gun with ISRU metal body."
- cmd: sim.import
  args:
    item: compressor_pump_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: applicator_nozzle
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_hose_assembly
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_coating_spray_gun_and_pump_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining controls and assemble coating station."
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coating_booth_enclosure
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coating_drying_oven
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: enclosure_electrical_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembled_electrical_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembled_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_coating_station_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: coating_station_v0 with ISRU enclosures and spray body."
- cmd: sim.provenance
  args:
    item: coating_station_v0
    quantity: 1
    unit: unit
```
