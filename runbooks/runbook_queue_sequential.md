# Runbook Queue Sequential Runner

Goal: run each runbook listed in `runbooks/machine_runbook_queue.md` sequentially.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: runbook_queue_sequential
- cmd: sim.reset
  args:
    sim-id: runbook_queue_sequential
- cmd: sim.note
  args:
    style: milestone
    message: "Starting sequential runbook queue execution."
- cmd: sim.note
  args:
    style: note
    message: "Running alignment_tools_runbook.md"
- cmd: sim.runbook
  args:
    file: alignment_tools_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running assembly_station_runbook.md"
- cmd: sim.runbook
  args:
    file: assembly_station_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running crucible_refractory_runbook.md"
- cmd: sim.runbook
  args:
    file: crucible_refractory_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running electrodes_runbook.md"
- cmd: sim.runbook
  args:
    file: electrodes_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running electrolysis_cell_unit_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: electrolysis_cell_unit_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running fixturing_workbench_runbook.md"
- cmd: sim.runbook
  args:
    file: fixturing_workbench_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running hand_tools_basic_runbook.md"
- cmd: sim.runbook
  args:
    file: hand_tools_basic_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running high_temperature_power_supply_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: high_temperature_power_supply_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running milling_machine_general_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: milling_machine_general_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running mre_reactor_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: mre_reactor_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running press_brake_runbook.md"
- cmd: sim.runbook
  args:
    file: press_brake_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running press_brake_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: press_brake_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running reduction_furnace_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: reduction_furnace_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running rock_crusher_basic_runbook.md"
- cmd: sim.runbook
  args:
    file: rock_crusher_basic_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running welding_power_supply_v0_runbook.md"
- cmd: sim.runbook
  args:
    file: welding_power_supply_v0_runbook.md
- cmd: sim.note
  args:
    style: note
    message: "Running wire_drawing_die_set_runbook.md"
- cmd: sim.runbook
  args:
    file: wire_drawing_die_set_runbook.md
- cmd: sim.note
  args:
    style: success
    message: "Sequential runbook queue execution complete."
```
