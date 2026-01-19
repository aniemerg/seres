# Kiln Ceramic Runbook

Goal: Build `kiln_ceramic` using in-situ resources where possible.

## Machine Details
- **Mass**: TBD
- **Capabilities**: ceramic firing, annealing

## Required Components (from recipe)
1. refractory_castable (50 kg)
2. furnace_chamber_unequipped (1 unit)
3. heating_element_resistive (1 unit)
4. electrical_wire_and_connectors (2 kg)
5. control_circuit_board_basic (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: kiln_ceramic_runbook
- cmd: sim.reset
  args:
    sim-id: kiln_ceramic_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting kiln_ceramic runbook."
```

## ISRU Production: Build kiln with regolith-derived components

Commentary: Produce alumina and refractory castable in-situ from regolith, while importing binder, water, and electrical parts.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce refractory_castable from local alumina."
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
    item: refractory_installation_tools
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mixer_or_blender
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Mine highlands regolith for alumina extraction."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_highlands_v0
    quantity: 300
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.import
  args:
    item: hydrochloric_acid
    quantity: 30
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Extract alumina from highlands regolith (3 batches)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_alumina_powder_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.import
  args:
    item: ceramic_binder
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: water
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Mix refractory_castable for kiln shell."
- cmd: sim.run-recipe
  args:
    recipe: recipe_refractory_castable_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.import
  args:
    item: heating_element_resistive
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_circuit_board_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble kiln with ISRU refractory and imported electricals."
- cmd: sim.run-recipe
  args:
    recipe: recipe_kiln_ceramic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 kiln_ceramic complete."
```
