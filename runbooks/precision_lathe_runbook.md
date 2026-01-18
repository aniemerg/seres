# Precision Lathe Runbook

Goal: build `precision_lathe` while increasing ISRU coverage for heavy metal components.

Approach:
1) Baseline import all top-level parts to validate the recipe path.
2) Produce regolith metal and fasteners locally.
3) Assemble a second unit with locally-produced inputs where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: precision_lathe_runbook
- cmd: sim.reset
  args:
    sim-id: precision_lathe_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting precision_lathe runbook."
```

## Baseline assembly (imports)

Commentary: import all top-level recipe inputs and assemble a baseline lathe.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import top-level parts for precision_lathe."
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
    item: casting_furnace_v0
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
    item: inspection_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_bed_and_headstock
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_leadscrew_and_feed_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coolant_system_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_spindle_and_bearings
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_motor_and_drive
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_metal_crude
    quantity: 200
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 200
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_precision_lathe_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Baseline precision_lathe assembly complete."
```

## Local regolith metal + fasteners

Commentary: produce regolith-derived metal and fasteners for a second assembly.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for regolith metal production and fasteners."
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
    item: heat_treatment_furnace
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
    item: electrical_energy
    quantity: 30000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith_metal_crude for carriage/cross-slide, bed, and fasteners."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 1200
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

## Local steel stock + subassemblies

Commentary: build local steel stock, leadscrew/feed system, and coolant subassemblies.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import steelmaking + rolling equipment for local steel stock."
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
    item: heating_furnace
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
    item: cnc_mill
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
    item: electrical_energy
    quantity: 6000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce carbon reducing agent and ilmenite feedstock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 7
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 76
- cmd: sim.advance-time
  args:
    hours: 460
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 380
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 110
- cmd: sim.advance-time
  args:
    hours: 250
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 690
- cmd: sim.advance-time
  args:
    hours: 720
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce iron/steel intermediates for stock, plate, and billet."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 135
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_billet_or_slab_v0
    quantity: 80
- cmd: sim.advance-time
  args:
    hours: 420
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_raw_v0
    quantity: 70
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 41
- cmd: sim.advance-time
  args:
    hours: 600
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel stock, plate, and fastener kits."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 65
- cmd: sim.advance-time
  args:
    hours: 420
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 20
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce bearing_set_heavy and pipe fittings."
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_heavy_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_pipe_and_fittings_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce spindle assembly and lathe spindle/bearings."
- cmd: sim.import
  args:
    item: hydraulic_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_plate_or_induction_heater
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_sealed
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: assembly_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: balancing_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_spindle_assembly_precision_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_spindle_and_bearings_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce lathe_bed_and_headstock locally."
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
    item: welding_consumables
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: milling_machine_cnc
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coordinate_measuring_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: precision_tooling_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: alignment_tools
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: precision_levels
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_bed_and_headstock_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 400
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Top up regolith_metal_crude for final lathe assembly."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 30
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble lathe leadscrew/feed system and coolant system."
- cmd: sim.import
  args:
    item: spur_gear_set_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: pump_water_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_leadscrew_and_feed_system_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_coolant_system_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce lathe motor/drive subassembly with local frame and belt drive."
- cmd: sim.import
  args:
    item: test_bench_electrical
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
    item: drill_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drill_press_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_treatment_station
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_installed_belt_drive_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_frame_welded_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: milestone
    message: "Produce motor components and local motor_electric_medium."
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 0.1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cooling_fan_assembly
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 1.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: grease_bearing_high_temp
    quantity: 0.05
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_rubber_bearing
    quantity: 0.1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_sheet_or_plate_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_electric_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.import
  args:
    item: power_electronics_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_motor_and_drive_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
```

## In-situ assembly

Commentary: assemble a second lathe with local regolith metal and fasteners.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble precision_lathe with local regolith_metal_crude and fasteners."
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_precision_lathe_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: success
    message: "Local precision_lathe assembly complete."
```
