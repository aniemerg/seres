# Press Brake v0 Runbook

Goal: build `press_brake_v0` with a baseline import, then replace the placeholder
bulk input with locally sourced bulk material using solar-derived energy.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: press_brake_v0_runbook
- cmd: sim.reset
  args:
    sim-id: press_brake_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting press_brake_v0 runbook."
```

## Baseline import + assembly

Commentary: import placeholder bulk material and required tools to prove the recipe.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline assembly with imported bulk material."
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
    item: bulk_material_or_parts
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 10
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_brake_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Baseline press_brake_v0 assembly complete."
- cmd: sim.note
  args:
    style: milestone
    message: "Reset simulation for ISRU-focused build."
- cmd: sim.reset
  args:
    sim-id: press_brake_v0_runbook
```

## In-situ energy + bulk material

Commentary: produce bulk material locally using the boundary bulk recipe.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Generate local bulk material via the boundary bulk recipe."
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
    item: electrical_energy
    quantity: 5
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_bulk_material_or_parts_import_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
```

## Final assembly (ISRU attempt)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble press_brake_v0 using locally sourced bulk material."
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_brake_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "press_brake_v0 local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
