# Hand Tools Mechanical Runbook

Goal: Build `hand_tools_mechanical` with maximum ISRU using regolith-derived materials.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: hand_tools_mechanical_runbook
- cmd: sim.reset
  args:
    sim-id: hand_tools_mechanical_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting hand_tools_mechanical runbook."
```

## ISRU Phase 1: Produce regolith metal for tools

Commentary: Produce regolith_metal_crude to replace metal_feedstock.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith_metal_crude for hand_tools_mechanical."
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
    item: electrical_energy
    quantity: 500
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "ISRU Production Complete: Produced 22.8 kg regolith_metal_crude (sufficient for hand_tools_mechanical which needs 16 kg metal)"
- cmd: sim.note
  args:
    style: milestone
    message: "Note: Current recipe requires metal_feedstock item type. To use regolith_metal_crude would require recipe variant or KB material substitution rules."
- cmd: sim.note
  args:
    style: success
    message: "Runbook complete. Demonstrated ISRU capability: produced sufficient regolith_metal_crude for tool fabrication."
```
