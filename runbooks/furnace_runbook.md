# Furnace Runbook

Goal: Build `furnace` using in-situ resources where possible.

## Machine Details
- **Mass**: 900 kg
- **Material Class**: steel
- **Capabilities**: generic furnace for heating and melting operations

## Required Components (from recipe)
1. steel_plate_raw (100 kg)
2. insulation_ceramic (50 kg)
3. heating_elements_basic (5 kg)
4. electrical_wire_and_connectors (3 kg)
5. fastener_kit_large (2 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: furnace_runbook
- cmd: sim.reset
  args:
    sim-id: furnace_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting furnace runbook."
```

## Build furnace with local components (ISRU)

```sim-runbook
- cmd: sim.note
  args:
    style: info
    message: "Import machines for local production."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: assembly_station
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
    item: hand_tools_electrical
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
    item: furnace_high_temp
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
    quantity: 6
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
    quantity: 12000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel ingot feedstock for plate."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 370
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 190
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 56
- cmd: sim.advance-time
  args:
    hours: 150
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
    recipe: recipe_steel_plate_raw_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for large fasteners."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining non-steel components and assemble furnace."
- cmd: sim.import
  args:
    item: insulation_ceramic
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: heating_elements_basic
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_v0
    quantity: 1
- cmd: sim.import
  args:
    item: drawing_die_set_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_drawing_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coil_winding_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ceramic_press_or_mold_set
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
    item: water
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: screening_equipment
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
    quantity: 15000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel ingot feedstock for plate."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 370
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 190
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 56
- cmd: sim.advance-time
  args:
    hours: 150
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
    recipe: recipe_steel_plate_raw_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal and wire feedstock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.run-recipe
  args:
    recipe: recipe_raw_metal_block_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.import
  args:
    item: drawing_die_set_basic
    quantity: 1
    unit: unit
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_wire_feed_v0
    quantity: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 22
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: milestone
    message: "Prepare ceramic powder for heater supports."
- cmd: sim.run-recipe
  args:
    recipe: recipe_coarse_powder_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_powder_mixture_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble heating elements with local wire and ceramic supports."
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_elements_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble furnace with local steel, fasteners, and heating elements."
- cmd: sim.import
  args:
    item: insulation_ceramic
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Furnace built with local steel plate, fasteners, and heating elements."
- cmd: sim.provenance
  args:
    item: furnace
```
