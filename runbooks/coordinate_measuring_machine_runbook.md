# Coordinate Measuring Machine Runbook

Goal: Build `coordinate_measuring_machine` using in-situ resources where possible.

## Machine Details
- **Mass**: 800 kg
- **Capabilities**: Precision 3D coordinate measuring machine (CMM) for dimensional inspection with touch probe and granite base

## Strategy

The coordinate_measuring_machine can achieve moderate ISRU by producing the granite surface plate from regolith-derived rock feedstock. Precision components (linear stages, encoders, motors, computer, air bearings, calibration artifacts) must be imported.

ISRU components:
- granite_surface_plate_large (400 kg) - from regolith_lunar_highlands → rock_feedstock_raw

Imported components:
- linear_stage_xyz_precision (1 unit) - precision motion system
- touch_probe_assembly (1 unit) - measurement probe
- linear_encoder_set (3 units) - position encoders
- stepper_motor_precision (3 units) - axis motors
- computer_workstation (1 unit) - control computer
- air_bearing_assembly (3 units) - precision bearings
- calibration_artifacts (1 unit) - calibration standards

Expected ISRU: ~50% (granite base from regolith)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: coordinate_measuring_machine_runbook
- cmd: sim.reset
  args:
    sim-id: coordinate_measuring_machine_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting coordinate_measuring_machine runbook."
```

## ISRU Build: CMM with Regolith-Derived Granite Base

Commentary: Produce granite_surface_plate_large from regolith-derived rock feedstock. Import all precision components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce granite surface plate from regolith."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: saw_or_cutting_tool
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
    item: inspection_tools_basic
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
    item: electrical_energy
    quantity: 1000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Collect regolith_lunar_highlands for granite production (need 400 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_highlands_v0
    quantity: 400
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: info
    message: "Produce rock_feedstock_raw from highlands regolith (400 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_rock_feedstock_raw_v0
    quantity: 400
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: info
    message: "Produce granite_surface_plate_large from rock feedstock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_granite_surface_plate_large_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: milestone
    message: "Import precision components and assemble CMM."
- cmd: sim.import
  args:
    item: linear_stage_xyz_precision
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: touch_probe_assembly
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: linear_encoder_set
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: stepper_motor_precision
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: computer_workstation
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: air_bearing_assembly
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: calibration_artifacts
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_coordinate_measuring_machine_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: coordinate_measuring_machine with regolith-derived granite base."
- cmd: sim.provenance
  args:
    item: coordinate_measuring_machine
    quantity: 1
    unit: unit
```
