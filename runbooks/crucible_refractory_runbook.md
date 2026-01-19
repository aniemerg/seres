# Crucible Refractory Runbook

Goal: Build `crucible_refractory` with maximum ISRU using regolith-derived ceramic materials.

## Strategy

Crucible refractory requires ceramic_powder_mixture (16 kg), which can be produced from regolith_coarse_fraction via coarse_powder.

Production chain: regolith_lunar_mare → regolith_coarse_fraction (screening) → coarse_powder → ceramic_powder_mixture (ball milling + drying + screening) → crucible_refractory (forming + drying + firing + finishing)

Expected ISRU: ~100% (full chain from regolith)

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
    message: "Starting crucible refractory runbook."
```

## ISRU Build: Crucible Refractory from Regolith Ceramics

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce crucible_refractory from regolith via ceramic powder route."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 1
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
    item: furnace_high_temp
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
    item: screening_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ceramic_press_or_mold_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: kiln_ceramic
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
    message: "Produce ~60 kg regolith, screen to get ~36 kg coarse fraction."
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
- cmd: sim.note
  args:
    style: info
    message: "Produce ~36 kg coarse_powder from regolith_coarse_fraction."
- cmd: sim.run-recipe
  args:
    recipe: recipe_coarse_powder_v0
    quantity: 36
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: info
    message: "Produce ~34 kg ceramic_powder_mixture from coarse_powder (ball mill + dry + screen)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_powder_mixture_v0
    quantity: 36
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: info
    message: "Produce 2 crucible_refractory units (30 kg total) from ceramic_powder_mixture (form + dry + fire + finish)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_crucible_refractory_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: crucible_refractory produced from regolith ceramics (30 kg, 2 units)."
- cmd: sim.provenance
  args:
    item: crucible_refractory
    quantity: 2
    unit: unit
```
