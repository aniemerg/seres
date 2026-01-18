# Cutting Tools General Runbook

Goal: Build `cutting_tools_general` (30 kg toolset) using maximum in-situ resources. This is an assembly of multiple sub-components including hand tools, saws, and shear blades - all of which can be produced from regolith-derived steel.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: cutting_tools_general_runbook
- cmd: sim.reset
  args:
    sim-id: cutting_tools_general_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting cutting_tools_general runbook."
```

## ISRU Build: Cutting Tools from Regolith Steel

Commentary: Extract iron ore and carbon from lunar regolith for all steel needs.
Need significant quantities: ~25 kg tool steel for shear blade, ~5 kg steel for saws, ~3 kg for hand tools.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: Mine regolith and extract materials for steel."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 6
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
- cmd: sim.import
  args:
    item: milling_machine_general_v0
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
    item: cutting_tools_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 1a: Mine mare regolith (need ~200 kg for iron extraction)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Mined 200 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 1b: Extract ilmenite from regolith for iron ore (need ~70 kg iron ore for all steel production)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 120
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Extracted 72 kg iron_ore_or_ilmenite from regolith."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine carbonaceous regolith for carbon extraction (need 320 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 52
- cmd: sim.note
  args:
    style: success
    message: "Mined 350 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract carbon from carbonaceous regolith (need ~9 kg carbon)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 55
- cmd: sim.note
  args:
    style: success
    message: "Extracted 9.6 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Convert carbon_reductant to carbon_reducing_agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 9.5
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Converted 9.5 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: milestone
    message: "Produce tool steel for shear blade."
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
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 3
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
    item: quench_tank
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Producing 11.5 kg tool_steel_high_carbon_v0 from regolith materials."
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_steel_high_carbon_v0
    quantity: 11.5
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Produced 11.5 kg tool_steel_high_carbon_v0 from regolith!"
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel stock and ingots for saws and hand tools."
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
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce 7.5 kg steel_stock for hand_tools_basic (3.0 kg) and fasteners (4.5 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 7.5
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.note
  args:
    style: success
    message: "Produced 7.5 kg steel_stock."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Produce 2.5 kg pig iron for steel_ingot production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 2.5
- cmd: sim.advance-time
  args:
    hours: 25
- cmd: sim.note
  args:
    style: success
    message: "Produced 2.5 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Produce 2.3 kg steel_ingot for saw production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 2.3
- cmd: sim.advance-time
  args:
    hours: 23
- cmd: sim.note
  args:
    style: success
    message: "Produced 2.3 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 3d: Roll steel_ingot into steel_stock_bar_or_billet (need ~2.2 kg for 2 saws)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 2.2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Produced ~2.1 kg steel_stock_bar_or_billet."
- cmd: sim.note
  args:
    style: milestone
    message: "Produce fasteners from regolith steel."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Produced 3 fastener_kit_small from regolith steel."
- cmd: sim.note
  args:
    style: milestone
    message: "Build sub-components from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 5a: Build hand_tools_basic from regolith steel_stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_hand_tools_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "Built 1 hand_tools_basic from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 5b: Build 2 saw_or_cutting_tool from regolith steel_stock_bar_or_billet."
- cmd: sim.run-recipe
  args:
    recipe: recipe_saw_or_cutting_tool_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: success
    message: "Built 2 saw_or_cutting_tool from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 5c: Build shear_blade_or_saw_band from regolith tool steel."
- cmd: sim.run-recipe
  args:
    recipe: recipe_shear_blade_or_saw_band_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Built 1 shear_blade_or_saw_band from regolith tool steel."
- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly with regolith-derived components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_cutting_tools_general_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: cutting_tools_general built with regolith-derived steel components."
- cmd: sim.provenance
  args:
    item: cutting_tools_general
    quantity: 1
    unit: unit
```
