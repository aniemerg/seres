# Output Showcase Runbook

Goal: demonstrate rich, story-driven CLI output (headings, notes, tables, task lists).

!!! info "Runbook intent"
    This file is a showcase. It is safe to run and is designed to produce varied CLI output.

## Storyboard

- [x] Setup and reset
- [ ] Baseline imports
- [ ] Baseline build
- [ ] Structured notes and callouts
- [ ] Checkpoint summary

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: output_showcase
- cmd: sim.reset
  args:
    sim-id: output_showcase
- cmd: sim.note
  args:
    style: milestone
    message: "Starting output showcase runbook."
```

## Stage 1: Baseline imports

Commentary: import the minimal toolchain for a simple build.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import tools and materials."
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
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tool_steel_high_carbon_v0
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Baseline imports complete."
```

## Stage 2: Baseline build

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Run baseline recipe to generate process output."
- cmd: sim.run-recipe
  args:
    recipe: recipe_alignment_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Baseline build complete."
```

## Stage 3: Structured callouts

!!! warning "Demonstration warning"
    This is a markdown callout only. It demonstrates how warnings could render in the CLI.

```sim-runbook
- cmd: sim.note
  args:
    style: warning
    message: "Optional warning note: imports still required for electronics."
- cmd: sim.note
  args:
    style: note
    message: "Note: this runbook is a UX showcase, not an ISRU optimization."
- cmd: sim.note
  args:
    style: dim
    message: "Debug: staged output controls can hide low-signal events."
```

## Stage 4: Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```

## Optional: story block (future extension)

```sim-story
title: "Alignment tools baseline"
focus: item:alignment_tools
show: [isru, energy, imports, provenance]
table:
  - step: machining_finish_basic_v0
    output: machined_part_raw
    delta: "+4.5 kg"
  - step: precision_grinding_basic_v0
    output: finished_part_deburred
    delta: "+4.3 kg"
  - step: assembly_basic_v0
    output: alignment_tools
    delta: "+1 unit"
```
