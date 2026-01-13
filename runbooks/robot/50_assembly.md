# Robot Assembly: Delta Robot v0

Purpose: assemble the delta robot from prepared subassemblies.

## Notes

- `recipe_machine_delta_robot_v0` is the current assembly path.
- Motors: we ensure a total of 3 `motor_electric_small` units (imports fill the gap).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble delta robot from subassemblies."

- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: robot_arm_link_aluminum
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electric_parallel_gripper
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: machine_frame_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: harmonic_drive_reducer_medium
    quantity: 3
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_distribution_board
    quantity: 1
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
- cmd: sim.import
  args:
    item: assembled_cable_harness
    quantity: 3
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

- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_delta_robot_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 48
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: note
    message: "Flush remaining assembly, wiring, and test steps."
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
    message: "Delta robot assembly complete."
```
