# Measurement Equipment Runbook

Goal: build `measurement_equipment` with a baseline import, then replace metal inputs
with locally produced steel and alloys to improve ISRU where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: measurement_equipment_runbook
- cmd: sim.reset
  args:
    sim-id: measurement_equipment_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting measurement equipment runbook."
```

## Baseline import + assembly

Commentary: import all parts and tooling to validate the recipe once.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline assembly with imported parts."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: calibration_artifacts
    quantity: 1
    unit: kit
    ensure: true
- cmd: sim.import
  args:
    item: measurement_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: caliper_set_precision
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: micrometer_set
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: dial_indicator_set
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: gauge_block_set
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: multimeter_digital
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
    item: electrical_wire_and_connectors
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: wired_electrical_system
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: machined_part_raw
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 300
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_measurement_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Baseline measurement equipment assembly complete."
- cmd: sim.note
  args:
    style: milestone
    message: "Reset simulation for ISRU-focused build."
- cmd: sim.reset
  args:
    sim-id: measurement_equipment_runbook
```

## In-situ equipment + feedstocks

Commentary: import tooling and MRE equipment, then produce metal alloy bulk locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for local metal production."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: hand_tools_mechanical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: deburring_tools
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
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: quench_tank
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
    item: crucible_refractory
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: calibration_artifacts
    quantity: 1
    unit: kit
    ensure: true
- cmd: sim.import
  args:
    item: measurement_equipment
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
    item: electrical_energy
    quantity: 1200
    unit: kWh
    ensure: true
```

## In-situ: metal alloy bulk (MRE)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce metal alloy bulk from regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
```

## In-situ: precision component sets

Commentary: use local alloy for gauge blocks and fasteners; machine parts from stock.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce precision component sets."
- cmd: sim.import
  args:
    item: steel_plate_or_sheet
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 8
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: spur_gear_set_v0
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: spring_compression_small
    quantity: 6
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: multimeter_digital
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: wired_electrical_system
    quantity: 60
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 12
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_finished_part_deburred_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_rough_part_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_gauge_block_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_caliper_set_precision_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_micrometer_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_dial_indicator_set_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.advance-time
  args:
    hours: 200
```

## Final assembly (mixed local + imported)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble measurement equipment from locally produced parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_measurement_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "measurement_equipment local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
