# Surface Grinder Runbook

Goal: Build `surface_grinder` with maximum ISRU using regolith-derived materials.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: surface_grinder_runbook
- cmd: sim.reset
  args:
    sim-id: surface_grinder_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting surface_grinder runbook."
```

## ISRU Production

Commentary: Produce ~1000 kg of regolith_metal_crude to build major components locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith_metal_crude for surface_grinder components."
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
    item: crucible_refractory
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
    item: coil_winding_machine
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
    item: grinding_wheels
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
    item: surface_grinder
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
    item: electrical_energy
    quantity: 20000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 45
- cmd: sim.advance-time
  args:
    hours: 350
- cmd: sim.note
  args:
    style: info
    message: "Build machine_base_large from local regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_base_large_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 35
- cmd: sim.note
  args:
    style: info
    message: "Build grinding_spindle_assembly from local regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_grinding_spindle_assembly_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: info
    message: "Build table_drive_assembly from local regolith_metal_crude."
- cmd: sim.run-recipe
  args:
    recipe: recipe_table_drive_assembly_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: info
    message: "Build magnetic_chuck_surface_grinder from local regolith_metal_crude."
- cmd: sim.import
  args:
    item: aluminum_wire
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 0.1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_magnetic_chuck_surface_grinder_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: info
    message: "Import remaining components and assemble surface_grinder."
- cmd: sim.import
  args:
    item: coolant_system_basic
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
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_surface_grinder_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Surface_grinder with maximum ISRU complete!"
```
