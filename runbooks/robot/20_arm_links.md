# Robot Subassembly: Arm Links (Aluminum)

Purpose: fabricate the delta robot's aluminum arm links using casting + machining.

## Notes

- **Current approach:** import aluminum alloy ingots and machine them into links.
- **Planned improvement:** swap ingot imports for the local aluminum chain (alumina → ingot).
- **Recipe:** `recipe_robot_arm_link_aluminum_v0` (casts + machines + inspects).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build robot arm links (aluminum)."

- cmd: sim.import
  args:
    item: aluminum_alloy_ingot
    quantity: 27
    unit: kg
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

- cmd: sim.run-recipe
  args:
    recipe: recipe_robot_arm_link_aluminum_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: info
    message: "Arm links complete (3x)."
```
