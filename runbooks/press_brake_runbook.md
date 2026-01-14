# Press Brake Runbook

Goal: build `press_brake` using in-situ steel production where possible. Start with
baseline imports to validate the recipe, then replace the bulk steel feedstock with
regolith-derived steel stock.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: press_brake_runbook
- cmd: sim.reset
  args:
    sim-id: press_brake_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting press_brake runbook."
```

## Baseline: import equipment

Commentary: import the core fabrication equipment needed for welding, machining,
cutting, forging, heat treating, and assembly.

```sim-runbook
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
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drawing_die_set_basic
    quantity: 1
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
    item: steel_forming_press
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
    item: high_temperature_power_supply_v0
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
```

## Baseline: import feedstocks and modules

Commentary: import feedstocks and modules to validate the press_brake recipe.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline build: import feedstocks and modules."
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 500
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: filler_wire_basic
    quantity: 25
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: machined_part_raw
    quantity: 120
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_system_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_electronics_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_assembly_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: kit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_press_brake_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Baseline press_brake build complete."
```

## ISRU: steel stock from regolith

Commentary: produce steel_stock from regolith-derived ilmenite and carbonaceous
regolith. Also roll steel into plate/sheet and bar stock for downstream parts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU steel: mine regolith and extract ilmenite."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 3000
- cmd: sim.advance-time
  args:
    hours: 3000
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 300
- cmd: sim.advance-time
  args:
    hours: 1810
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 1500
- cmd: sim.advance-time
  args:
    hours: 2250
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 450
- cmd: sim.advance-time
  args:
    hours: 900
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 352
- cmd: sim.advance-time
  args:
    hours: 1420
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 500
- cmd: sim.advance-time
  args:
    hours: 3200
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 335
- cmd: sim.advance-time
  args:
    hours: 1020
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 160
- cmd: sim.advance-time
  args:
    hours: 320
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 70
- cmd: sim.advance-time
  args:
    hours: 105
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_3mm_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 55
- cmd: sim.advance-time
  args:
    hours: 130
```

## ISRU: fabricate filler wire and machined parts

Commentary: use locally fabricated intermediates to reduce imports for filler wire
and machined parts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: fabricate filler wire and machined parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_filler_wire_basic_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 7
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 200
```

## ISRU: fasteners and hydraulic system

Commentary: use locally produced steel stock and sheet to assemble fasteners and
build a medium hydraulic system with imported seals, valves, and fluid.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce fasteners and hydraulic system."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_seals_set
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: piping_components
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cutting_fluid
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_control_valve_set
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_system_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 120
```

## ISRU: press_brake build with local steel

Commentary: assemble a second press_brake using locally produced steel_stock while
keeping electronics and hydraulics imported.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: assemble press_brake using local steel stock."
- cmd: sim.import
  args:
    item: power_electronics_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_assembly_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_press_brake_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "ISRU press_brake build complete."
```
