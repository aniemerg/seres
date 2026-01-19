# Ceramic Press or Mold Set Runbook

## Goal
Build `ceramic_press_or_mold_set` with maximum ISRU using regolith-derived steel.

## Machine Overview
- **Target**: ceramic_press_or_mold_set (20 kg)
- **Purpose**: Tooling for forming green ceramic parts in ceramic_forming_v0 process
- **Material**: Steel construction from regolith_metal_crude
- **Recipe**: recipe_ceramic_press_or_mold_set_v0 (22 kg input → 20 kg output)

## Components Needed
1. Mold base plate and frame (~10 kg)
2. Cavity plates and inserts (~8 kg)
3. Ejector mechanism (~2 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: ceramic_press_or_mold_set_runbook
- cmd: sim.reset
  args:
    sim-id: ceramic_press_or_mold_set_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting ceramic_press_or_mold_set ISRU build."
```

## Stage 1: Import equipment (no materials)

Commentary: Import equipment needed for MRE, casting, machining, and assembly. Do NOT import regolith_metal_crude - we'll produce it locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 1: Import fabrication equipment."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: rock_crusher_basic
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
    item: generic_chemical_reactor_v0
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
    item: high_temperature_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
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
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
```

## Stage 2: Produce regolith_metal_crude via MRE

Commentary: Mine and process regolith to produce 22.8 kg regolith_metal_crude.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Produce regolith_metal_crude via MRE."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: success
    message: "Produced 22.8 kg regolith_metal_crude via MRE."
```

## Stage 3: Build ceramic_press_or_mold_set from ISRU metal

Commentary: Execute recipe to cast, machine, finish, and assemble the mold set.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 3: Build ceramic_press_or_mold_set from ISRU materials."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_press_or_mold_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 11
- cmd: sim.note
  args:
    style: success
    message: "Ceramic press/mold set built with ISRU materials!"
- cmd: sim.provenance
  args:
    item: ceramic_press_or_mold_set
```

## Expected Results
- **Output**: 1 unit ceramic_press_or_mold_set (20 kg)
- **ISRU Material**: 22 kg regolith_metal_crude from MRE (100% ISRU)
- **Target ISRU**: 100% for the mold set material (all metal from regolith)
- **Total Time**: ~18 hours (MRE + fabrication)

## Notes
- Ceramic forming molds don't require hardened tool steel
- Simple steel construction adequate for non-abrasive ceramic powder
- No heat treatment needed
- Fabrication machines are imported but the mold material is 100% ISRU
