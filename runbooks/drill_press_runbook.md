# Drill Press Runbook

Goal: build `drill_press` with an import baseline, then rebuild with an ISRU machine column cast from regolith metal.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: drill_press_runbook
- cmd: sim.reset
  args:
    sim-id: drill_press_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting drill_press runbook."
```

## Baseline import build

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline build with imported components to validate recipe."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_mechanical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tension_gauge
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
    item: test_bench_electrical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: measurement_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 10000
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: machine_column_cast
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: spindle_head_basic
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
    item: table_top_t_slot
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: depth_stop_mechanism
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: belt_and_pulley_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_drill_press_v0
    quantity: 1
```

## ISRU machine column casting

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for regolith metal and casting."
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
    item: casting_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sand_casting_flask_set
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
    item: heat_treatment_furnace_v0
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
    item: wood_or_composite_material
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 25000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal, melt to preform, cast ISRU machine column."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_molten_material_or_preform_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_column_cast_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
```

## Final assembly with ISRU column

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining subassemblies and build drill_press with ISRU machine column."
- cmd: sim.import
  args:
    item: spindle_head_basic
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
    item: table_top_t_slot
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: depth_stop_mechanism
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: belt_and_pulley_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_drill_press_v0
    quantity: 1
```
