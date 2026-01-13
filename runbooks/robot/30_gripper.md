# Robot Subassembly: Gripper

Purpose: ensure the robot has an end effector. We now assemble the gripper locally,
still importing precision motor and fasteners.

## Notes

- **Current approach:** run `recipe_electric_parallel_gripper_v0`.
- **Remaining imports:** stepper motor + fastener kit + alignment/test tooling.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble robot gripper from local metals."

- cmd: sim.import
  args:
    item: aluminum_alloy_ingot
    quantity: 4.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 0.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: stepper_motor_precision
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_small
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: alignment_tools
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
    item: test_bench_electrical
    quantity: 1
    unit: unit
    ensure: true

- cmd: sim.run-recipe
  args:
    recipe: recipe_electric_parallel_gripper_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: note
    message: "Complete alignment and inspection steps."
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.note
  args:
    style: info
    message: "Gripper ready (locally assembled)."
```
