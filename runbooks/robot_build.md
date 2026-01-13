# Delta Robot Build (Composed Runbooks)

Goal: build a **delta robot v0** using composable runbooks. We intentionally start with
imports for high‑complexity parts, then replace them with local builds over time.

## Structure

This runbook composes child runbooks in order:

1. **Bootstrap**: regolith → metals, aluminum wire, and at least one local motor.
2. **Arm links**: cast + machine aluminum links (3x).
3. **Gripper**: import for now; later replace with local build.
4. **Frame + electronics**: import baseline kit.
5. **Assembly**: put it all together with `recipe_machine_delta_robot_v0`.

## Plan Notes

- **Motor coverage:** the bootstrap runbook produces one local `motor_electric_small`.
  Assembly ensures a total of 3 by importing the missing motors.
- **WIP:** move gripper, electronics, and frame parts into local production runbooks
  once their dependency chains stabilize.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: delta_robot_build_v0
- cmd: sim.reset
  args:
    sim-id: delta_robot_build_v0
- cmd: sim.note
  args:
    style: milestone
    message: "Begin delta robot build (composed runbooks)."

- cmd: sim.runbook
  args:
    file: robot/00_bootstrap.md

- cmd: sim.runbook
  args:
    file: robot/20_arm_links.md

- cmd: sim.runbook
  args:
    file: robot/30_gripper.md

- cmd: sim.runbook
  args:
    file: robot/40_frame_and_electronics.md

- cmd: sim.runbook
  args:
    file: robot/50_assembly.md

- cmd: sim.status
  args: {}
```
