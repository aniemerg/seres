# Regolith Bootstrap Runbook

Minimal first runbook: import basic equipment, mine multiple regolith types, then run a few starter processing steps.

## Overview

This is a small, fast cycle intended to surface missing items or processes early.

| Phase | Goal |
| --- | --- |
| Setup | Create a clean sim and import basic equipment + reagents |
| Mining | Produce multiple regolith types in one pass |
| Processing | Run a couple starter conversion steps |
| Check | Summarize state and stop |

## Setup

Commentary: reset the sim so this runbook is repeatable.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: regolith_bootstrap_v0
- cmd: sim.reset
  args:
    sim-id: regolith_bootstrap_v0
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting regolith bootstrap runbook."
```

Commentary: import minimal equipment and one reagent to allow early processing.

```sim-runbook
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drilling_equipment_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heliostat_array_system_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydrochloric_acid
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Imported mining equipment and reagents."
```

## Mining

Commentary: kick off multiple regolith mining processes, then advance time once.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Begin regolith mining."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 4
- cmd: sim.start-process
  args:
    process: regolith_mining_highlands_v0
    duration: 4
- cmd: sim.advance-time
  args:
    hours: 4

- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.start-process
  args:
    process: regolith_mining_polar_psc_v0
    duration: 8
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: info
    message: "All regolith mining complete."
```

## Processing

Commentary: try a couple of simple conversions, then advance time once.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Begin starter processing (ilmenite, carbon reductant, alumina)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.start-process
  args:
    process: alumina_extraction_from_highlands_v0
    duration: 10
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: info
    message: "Starter processing complete."
```

## Aluminum wire

Commentary: smelt alumina into an aluminum ingot, then draw wire.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Smelt alumina into aluminum ingots, then draw wire."
- cmd: sim.import
  args:
    item: carbon_anode
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cryolite_flux
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrolysis_cell_unit_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_drawing_die_set
    quantity: 1
    unit: unit

    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.note
  args:
    style: info
    message: "Aluminum wire batches complete."
```

## Motor dependencies: electrical steel sheet

Commentary: produce electrical steel sheet locally from iron + silicon.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce electrical steel sheet for motor laminations."
- cmd: sim.import
  args:
    item: iron_metal_pure
    quantity: 5.76
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: silicon_purified
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: reduction_furnace_v0
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
    item: induction_forge_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: rolling_mill_v0
    quantity: 1
    unit: unit

    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_metal_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_metal_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2

- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_steel_sheet_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 36
```

## Motor dependencies: motor housing

Commentary: form the steel housing locally from iron stock.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Form motor housing from iron."
- cmd: sim.import
  args:
    item: iron_metal_pure
    quantity: 19.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 1
    unit: unit

    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_housing_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.advance-time
  args:
    hours: 2
```

## Motor dependencies: bearing set

Commentary: produce regolith_metal_crude locally, then cast and finish a small bearing set.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce metal alloy for bearings."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 380
    unit: kWh
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.advance-time
  args:
    hours: 6

- cmd: sim.note
  args:
    style: milestone
    message: "Cast and finish bearing set."
- cmd: sim.import
  args:
    item: crucible_refractory
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_bearing_set_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
```

## Motor dependencies: coil insulation

Commentary: produce coil insulation material locally from silicone polymer.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce coil insulation material."
- cmd: sim.import
  args:
    item: generic_chemical_reactor_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_basic
    quantity: 1
    unit: unit

    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_powder_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_precursor_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_polymer_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_coil_insulation_material_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
```

## Motor dependencies: motor shaft

Commentary: forge, machine, and grind a steel motor shaft.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce motor shaft from steel stock."
- cmd: sim.import
  args:
    item: steel_stock_bar_or_billet
    quantity: 5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_hammer_or_press
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_shaft_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
```

## Motor assembly

Commentary: import remaining materials/tools, then build a small electric motor.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble motor using local components and aluminum wire."
- cmd: sim.import
  args:
    item: stamping_press_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coil_winding_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 1
    unit: unit

    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_electric_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: info
    message: "Motor build complete."
```

## Checkpoint

Commentary: end with a quick status summary.

```sim-runbook
- cmd: sim.status
  args: {}
```
