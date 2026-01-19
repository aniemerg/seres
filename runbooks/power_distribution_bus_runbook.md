# Power Distribution Bus Runbook

Goal: Build `power_distribution_bus` (200 kg) using available parts; recipe is a simple assembly of bus bars, insulators, brackets, and terminals.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: power_distribution_bus_runbook
- cmd: sim.reset
  args:
    sim-id: power_distribution_bus_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting power_distribution_bus runbook."
```

## Assembly

```sim-runbook
- cmd: sim.note
  args:
    style: info
    message: "Import components and assembly tooling."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 1
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
    item: bus_bar_copper
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: center_insulator_ceramic
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: mounting_bracket_steel
    quantity: 8
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_output_terminals
    quantity: 12
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Assemble power_distribution_bus."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_power_distribution_bus_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Power distribution bus assembled."
- cmd: sim.provenance
  args:
    item: power_distribution_bus
    quantity: 1
    unit: unit
```
