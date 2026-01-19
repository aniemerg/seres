# Test Bench Electrical Runbook

Goal: Build `test_bench_electrical` using in-situ resources where possible.

## Machine Details
- **Mass**: 200 kg
- **Material Class**: steel
- **Capabilities**: electrical test bench for power delivery and instrument mounting

## Required Components (from recipe)
1. test_bench_frame (1 unit)
2. power_strip_and_protection (1 unit)
3. instrument_mounts_basic (1 unit)
4. power_output_terminals (1 unit)
5. cooling_fan_and_ducting (1 unit)
6. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: test_bench_electrical_runbook
- cmd: sim.reset
  args:
    sim-id: test_bench_electrical_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting test_bench_electrical runbook."
```

## Stage 1: Local steel components (ISRU)

Commentary: Collect regolith locally and produce steel-based parts (frame and mounts). Keep electronics, cooling fan assembly, and fasteners imported for now.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Local steel components (frame, mounts)"
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
    item: surface_grinder
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
    item: heating_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_press
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
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 10000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Extract ilmenite and carbon reductant from regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 550
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 300
- cmd: sim.advance-time
  args:
    hours: 1000
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 82
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel feedstock (pig iron, billet, ingot, bar, sheet, stock)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 160
- cmd: sim.advance-time
  args:
    hours: 800
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_billet_or_slab_v0
    quantity: 140
- cmd: sim.advance-time
  args:
    hours: 800
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_raw_v0
    quantity: 130
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 11
- cmd: sim.advance-time
  args:
    hours: 800
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_sheet_or_plate_v0
    quantity: 11
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 1500
- cmd: sim.note
  args:
    style: milestone
    message: "Fabricate frame and mounts locally."
- cmd: sim.run-recipe
  args:
    recipe: recipe_test_bench_frame_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_instrument_mounts_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining non-steel components and assemble test bench."
- cmd: sim.import
  args:
    item: power_strip_and_protection
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_output_terminals
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cooling_fan_and_ducting
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_test_bench_electrical_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: test_bench_electrical with local steel components."
```
