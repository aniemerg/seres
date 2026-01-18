# Drying Oven Runbook

Goal: Build `drying_oven` using in-situ resources where possible.

## Machine Details
- **Mass**: TBD
- **Capabilities**: drying, low-temperature heat treatment

## Required Components (from recipe)
1. structural_steel_frame (60 kg)
2. insulation_panel_high_temp (30 kg)
3. heating_element_resistive (4 unit)
4. temperature_controller_basic (1 unit)
5. power_electronics_module (1 unit)
6. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: drying_oven_runbook
- cmd: sim.reset
  args:
    sim-id: drying_oven_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting drying_oven runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all components and assembly equipment to test if the recipe runs.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment and parts for assembly."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_station
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
    item: structural_steel_frame
    quantity: 60
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_panel_high_temp
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_resistive
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_electronics_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble drying oven from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_drying_oven_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Baseline drying_oven complete."
```

## Stage 2: ISRU Components
*To be implemented - will replace imports with local production*
