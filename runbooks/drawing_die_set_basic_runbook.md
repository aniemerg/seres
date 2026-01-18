# Drawing Die Set (Basic) Runbook

Goal: Build `drawing_die_set_basic` using in-situ resources where possible.

## Machine Details
- **Mass**: TBD
- **Capabilities**: die fabrication, wire drawing tooling

## Required Components (from recipe)
1. machined_part_raw (5 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: drawing_die_set_basic_runbook
- cmd: sim.reset
  args:
    sim-id: drawing_die_set_basic_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting drawing_die_set_basic runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all components and required machines to test if the recipe runs.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment and parts for assembly."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
- cmd: sim.import
  args:
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_grinder
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: grinding_wheels
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: machined_part_raw
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Fabricate drawing dies from imported blanks."
- cmd: sim.run-recipe
  args:
    recipe: recipe_drawing_die_set_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Baseline drawing_die_set_basic complete."
```

## Stage 2: ISRU Components
*To be implemented - will replace imports with local production*
