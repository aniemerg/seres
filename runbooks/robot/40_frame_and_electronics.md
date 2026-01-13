# Robot Subassembly: Frame + Electronics

Purpose: gather structural frame parts and control electronics for the delta robot.

## Notes

- **Current approach:** build frame locally, import core control modules.
- **Planned improvement:** continue replacing imported power/control electronics.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Provision frame and control modules (imports)."

- cmd: sim.import
  args:
    item: harmonic_drive_reducer_medium
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: computer_core_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true

- cmd: sim.note
  args:
    style: info
    message: "Frame and control modules provisioned."
```

## Frame (Local Fabrication)

Goal: fabricate the machine frame from sheet steel and weld/fabricate in situ.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Fabricate machine frame locally."

- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: welding_power_supply_v0
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
    item: press_brake
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

- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.note
  args:
    style: info
    message: "Machine frame fabricated."
```

## Wiring Harnesses (Local Assembly)

Goal: replace imported harnesses with in situ assembly while still importing wire stock and connectors.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble cable harnesses locally."

- cmd: sim.import
  args:
    item: wire_stripper_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: crimping_tool_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: magnet_wire_copper
    quantity: 3.1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 0.7
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cable_ties_and_sleeving
    quantity: 0.7
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembled_cable_harness_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.note
  args:
    style: info
    message: "Cable harnesses assembled (3x)."
```

## Power Distribution (Local Assembly)

Goal: assemble the power distribution board from imported subcomponents.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble power distribution board locally."

- cmd: sim.import
  args:
    item: assembly_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bus_bar_copper
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: circuit_breaker_thermal_v0
    quantity: 6
    unit: each
    ensure: true
- cmd: sim.import
  args:
    item: terminal_block_set
    quantity: 1
    unit: set
    ensure: true
- cmd: sim.import
  args:
    item: indicator_light_set
    quantity: 1
    unit: set
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_distribution_board_import_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.advance-time
  args:
    hours: 2

- cmd: sim.note
  args:
    style: info
    message: "Power distribution board assembled."
```
