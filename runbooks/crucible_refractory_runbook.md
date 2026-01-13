# Crucible Refractory Runbook

Goal: build `crucible_refractory` using in-situ resources where possible. Start by
importing all required equipment and feedstocks for a baseline build, then replace
feedstocks with locally produced inputs.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: crucible_refractory_runbook
- cmd: sim.reset
  args:
    sim-id: crucible_refractory_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting crucible refractory runbook."
```

## Baseline import (equipment only)

Commentary: import the machines needed for forming and firing. Feedstock will be
produced in-situ from regolith to increase local resource usage.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import equipment for ceramic processing."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: furnace_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: screening_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: pressing_mold_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_press
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
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 500
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Baseline: equipment imported; feedstocks will be produced in-situ."
```

## In-situ: regolith feedstock to ceramic powder mixture

Commentary: mine regolith, screen to coarse fraction, convert to coarse powder,
then ball mill and screen into ceramic_powder_mixture.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "In-situ: produce ceramic_powder_mixture from regolith."
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_coarse_fraction_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_coarse_powder_v0
    quantity: 36
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_powder_mixture_v0
    quantity: 36
- cmd: sim.advance-time
  args:
    hours: 320
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "In-situ ceramic_powder_mixture complete."
```

## In-situ: crucible refractory builds

Commentary: build two crucibles using the locally produced ceramic powder mixture.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "In-situ: form, dry, fire, and finish two crucible_refractory units."
- cmd: sim.run-recipe
  args:
    recipe: recipe_crucible_refractory_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.advance-time
  args:
    hours: 280
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "In-situ crucible_refractory builds complete."
```
