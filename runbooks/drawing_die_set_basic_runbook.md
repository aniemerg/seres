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

## ISRU Build: Drawing Die Set from Regolith Metal

Commentary: Produce machined_part_raw (5 kg) from regolith metal, then fabricate drawing dies.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce drawing die set from regolith metal."
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
    item: saw_or_cutting_tool
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
    item: plate_rolling_mill
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
    item: mre_reactor_v0
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
    item: electrodes
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
    message: "Produce regolith_metal_crude via MRE for machined_part_raw."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 25
- cmd: sim.note
  args:
    style: info
    message: "Import steel plate stock for cut_parts."
- cmd: sim.import
  args:
    item: steel_plate_or_sheet
    quantity: 11
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Cut steel plate into rough stock for machining."
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 1.1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.note
  args:
    style: info
    message: "Produce machined_part_raw from regolith metal (5 kg needed)."
- cmd: sim.import
  args:
    item: induction_forge_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: anvil_or_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_hammer_or_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: info
    message: "Fabricate drawing dies from ISRU machined parts."
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
    message: "ISRU build complete: drawing_die_set_basic from regolith metal."
- cmd: sim.provenance
  args:
    item: drawing_die_set_basic
    quantity: 1
    unit: unit
```
