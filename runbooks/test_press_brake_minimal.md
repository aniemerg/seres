# Test Press Brake Minimal

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: test_press_brake_minimal
- cmd: sim.reset
  args:
    sim-id: test_press_brake_minimal
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: success
    message: "Test complete"
```
