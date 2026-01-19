# Stamping Press Basic Runbook

Goal: Build `stamping_press_basic` and improve ISRU.

## Machine Details
- **Mass**: TBD
- **Capabilities**: stamping, forming

## Required Components (from recipe)
1. steel_plate_or_sheet (1000 kg)
2. steel_stock (950 kg)
3. filler_wire_basic (50 kg)
4. hydraulic_cylinder_medium (1 unit)
5. hydraulic_pump_small (1 unit)
6. hydraulic_control_valve_set (1 kg)
7. piping_components (1 kg)
8. control_panel_basic (1 unit)
9. assembled_equipment (1 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: stamping_press_basic_runbook
- cmd: sim.reset
  args:
    sim-id: stamping_press_basic_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting stamping_press_basic runbook."
```

## ISRU Components

Commentary: Produce regolith metal locally and replace selected imports (piping, filler wire, hydraulic cylinder, hydraulic pump).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU production run (regolith metal + select subcomponents)."
- cmd: sim.note
  args:
    style: info
    message: "Import equipment and remaining imported components."
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
    item: hydraulic_assembly_tools
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: soldering_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_crimping_tools
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
    item: high_temperature_power_supply_v0
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
    item: electrical_energy
    quantity: 2000
    unit: kWh
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
    item: furnace_basic
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
    item: casting_mold_set
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
    item: steel_plate_or_sheet
    quantity: 1000
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 950
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_rubber_o_ring
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_seals_set
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_cylinder_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_pump_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_control_valve_set
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembled_equipment
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 1: Produce regolith_metal_crude for ISRU metal parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: success
    message: "Produced ~228 kg regolith_metal_crude."
- cmd: sim.note
  args:
    style: info
    message: "Step 2: Roll regolith metal into steel_stock_bar_or_billet and steel_bar_stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 0.35
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 81
- cmd: sim.advance-time
  args:
    hours: 180
- cmd: sim.note
  args:
    style: success
    message: "Produced ~81 kg steel_bar_stock."
- cmd: sim.note
  args:
    style: info
    message: "Step 3: Draw filler_wire_basic from steel_bar_stock (50 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_filler_wire_basic_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Produced 50 kg filler_wire_basic."
- cmd: sim.note
  args:
    style: info
    message: "Step 4: Produce piping_components from regolith metal (2 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_piping_components_regolith_v1
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 kg piping_components."
- cmd: sim.note
  args:
    style: info
    message: "Step 5: Produce bearing_set_small and hydraulic_pump_small."
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_bearing_set_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_pump_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Produced bearing_set_small and hydraulic_pump_small."
- cmd: sim.note
  args:
    style: info
    message: "Step 6: Produce hydraulic_cylinder_medium (regolith metal + imported seals)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_cylinder_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: success
    message: "Produced hydraulic_cylinder_medium."
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble stamping_press_basic with ISRU subcomponents."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_stamping_press_basic_import_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1000
- cmd: sim.note
  args:
    style: success
    message: "ISRU-enhanced stamping_press_basic complete."
```
