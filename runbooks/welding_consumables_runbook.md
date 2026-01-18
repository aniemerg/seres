# Welding Consumables Runbook

Goal: build `welding_consumables` with a baseline import, then replace aluminum wire,
storage enclosure, and welding rods with locally produced regolith metal to increase
ISRU.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: welding_consumables_runbook
- cmd: sim.reset
  args:
    sim-id: welding_consumables_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting welding consumables runbook."
```

## ISRU: local regolith metal for aluminum wire + storage enclosure + welding rods

Commentary: produce regolith metal via MRE, use it for aluminum wire and a local
storage enclosure, then refine steel from ilmenite to form welding rods.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import tooling for regolith metal and fabrication."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: wire_drawing_die_set
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
    item: furnace_basic
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
    item: welding_power_supply_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: welding_consumables
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fixturing_workbench
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
    item: hydraulic_press
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
    item: rolling_mill_or_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: reduction_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 6000
    unit: kWh
    ensure: true
```

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith_metal_crude for aluminum wire + storage enclosure."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: milestone
    message: "Extract carbon reductant for local carbon reducing agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 21
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Refine steel from ilmenite for local welding rods."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 11
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_sheet_or_plate_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_storage_enclosure_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_rod_steel_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 20
```

## Final assembly

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble welding consumables with local aluminum wire + enclosure."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_welding_consumables_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "welding_consumables local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
