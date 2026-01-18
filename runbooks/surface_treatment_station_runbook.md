# Surface Treatment Station Runbook

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: surface_treatment_station_runbook
- cmd: sim.reset
  args:
    sim-id: surface_treatment_station_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting surface_treatment_station runbook."
```

## Baseline assembly

Commentary: import all subassemblies and assemble a baseline surface_treatment_station.

```sim-runbook
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: chemical_bath_tank_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: agitation_system_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_bath_ventilation
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: circulation_pump_coolant
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
    item: support_frame_welded
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_surface_treatment_station_base_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

## Local ISRU assembly

Commentary: localize steel frame, agitation system, pump, and tank set using regolith metal and local steel plate. Import remaining controls/ventilation.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for regolith metal and steel plate production."
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
    item: metal_shear_or_saw
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: punch_press_or_drill
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
    item: fixturing_workbench
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 12000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for frame, agitation system, and pump housings."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 8
- cmd: sim.advance-time
  args:
    hours: 400
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce ilmenite and steel plate for chemical bath tanks."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 334
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 500
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 95
- cmd: sim.advance-time
  args:
    hours: 350
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 90
- cmd: sim.advance-time
  args:
    hours: 200
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce local frame, agitation system, pump, and tank set."
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_support_frame_welded_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 11
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_agitation_system_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_circulation_pump_coolant_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_bath_tank_set_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble surface_treatment_station with local subassemblies."
- cmd: sim.import
  args:
    item: chemical_bath_ventilation
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_surface_treatment_station_base_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```
