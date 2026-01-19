# Balancing Machine Runbook

Goal: Build `balancing_machine` using in-situ resources where possible.

## Machine Details
- **Mass**: 450 kg
- **Capabilities**: Dynamic balancing for rotating assemblies, vibration sensing, measurement

## Strategy

The balancing_machine can achieve moderate ISRU by producing the structural frame and fasteners from regolith-derived metal. Electronics (sensors, control modules, drive motors) must be imported.

ISRU components:
- machine_frame_medium (200 kg) - from regolith_metal_crude
- fastener_kit_medium (1 kg) - from regolith-derived steel_stock

Imported components:
- spindle_drive_motor_small
- vibration_sensor_set
- control_compute_module_imported
- sensor_suite_general
- power_conditioning_module
- mounting_fixtures_adjustable (steel_bar_stock)

Expected ISRU: ~45% (structural components from regolith)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: balancing_machine_runbook
- cmd: sim.reset
  args:
    sim-id: balancing_machine_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting balancing_machine runbook."
```

## ISRU Build: Balancing Machine with Regolith-Derived Frame

Commentary: Produce machine_frame_medium and fastener_kit_medium from regolith. Import electronics, sensors, motors, and mounting fixtures.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce structural frame and fasteners from regolith."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: heating_furnace
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
    item: heat_treatment_furnace_v0
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
    item: measurement_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_metal_crude for machine frame (need ~10 batches for 210+ kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 250
- cmd: sim.note
  args:
    style: info
    message: "Produce machine_frame_medium from regolith_metal_crude (200 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: info
    message: "Produce steel_stock from regolith for fasteners (need iron ore and carbon)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 70
- cmd: sim.advance-time
  args:
    hours: 70
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: info
    message: "Produce fastener_kit_medium from regolith-derived steel_stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: milestone
    message: "Import electronics, sensors, motors, and mounting fixtures, then assemble balancing machine."
- cmd: sim.import
  args:
    item: spindle_drive_motor_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibration_sensor_set
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mounting_fixtures_adjustable
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_balancing_machine_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: balancing_machine with regolith-derived structural frame and fasteners."
- cmd: sim.provenance
  args:
    item: balancing_machine
    quantity: 1
    unit: unit
```
