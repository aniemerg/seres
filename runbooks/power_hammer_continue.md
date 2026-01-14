# Power Hammer Completion

Continue the power hammer build from where the previous runbook stopped.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: power_hammer_insitu_v0
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.note
  args:
    style: info
    message: "Waiting for all recipes to complete."
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
- cmd: sim.build-machine
  args:
    machine: power_hammer_or_press
    quantity: 1
- cmd: sim.note
  args:
    style: success
    message: "Power hammer build complete!"
- cmd: sim.status
  args: {}
```
