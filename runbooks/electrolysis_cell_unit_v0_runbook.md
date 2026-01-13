# Electrolysis Cell Unit v0 Build Runbook

Build an electrolysis_cell_unit_v0 machine using as many in situ resources as possible.

## Overview

This runbook builds an electrolysis_cell_unit_v0 by:
1. Importing core equipment and starter materials
2. Mining regolith and extracting metals
3. Producing components from local resources
4. Assembling the final unit

| Phase | Goal |
| --- | --- |
| Setup | Initialize simulation and import equipment |
| Mining | Mine regolith and extract metals |
| Steel Production | Produce steel_sheet_3mm from local iron |
| Nickel Production | Produce nickel components from local nickel |
| Tungsten Components | Produce tungsten components |
| Assembly | Assemble the electrolysis cell unit |
| Check | Verify the build |

## Setup

Commentary: reset the sim so this runbook is repeatable.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: electrolysis_cell_v0_build_v2
- cmd: sim.reset
  args:
    sim-id: electrolysis_cell_v0_build_v2
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting electrolysis cell unit build."
```

Commentary: import core equipment for mining, processing, and assembly.

```sim-runbook
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 10
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
    item: steel_forming_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: rolling_mill_v0
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
    item: drawing_die_set_basic
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
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cnc_mill
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
    item: sintering_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hot_press_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: inert_atmosphere_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: powder_mixer
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
    item: hydraulic_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_ram_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coating_station_v0
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
    item: magnetic_separator_drum_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibratory_feeder_v0
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
    item: crucible_graphite
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_separation_equipment
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
    message: "Imported core equipment."
```

## Mining and Metal Extraction

Commentary: Import regolith as boundary resource for iron and nickel extraction.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Importing regolith for iron and nickel extraction."
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 4100
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: regolith_carbonaceous
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Regolith imported, ready for processing."
```

  args:
    item: hydrochloric_acid
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_heated_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Mining complete, starting local material production."
```

## Local Material Production

Commentary: Produce carbon reductant and iron from locally mined regolith.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Producing carbon reductant and iron from local regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 52
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_metal_pure_from_ilmenite_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.note
  args:
    style: info
    message: "Local material production complete."
```

## Steel Production

Commentary: Produce steel ingot from local iron, then roll into steel_sheet_3mm.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Producing steel sheet from locally produced iron."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_3mm_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: info
    message: "Steel sheet production complete."
```

## Nickel Production

Commentary: Nickel metal can theoretically be extracted from meteoritic fragments in regolith using recipe_nickel_metal_from_regolith_v0, but currently blocked by simulation engine limitation. Importing nickel_metal for now.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Importing nickel for component production."
- cmd: sim.import
  args:
    item: nickel_metal
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Nickel imported, producing nickel components."
- cmd: sim.import
  args:
    item: carbon_monoxide
    quantity: 8
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_nickel_metal_pure_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_nickel_wire_fine_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_tube_electrode_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.import
  args:
    item: raw_metal_block
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_nickel_anode_vacuum_tube_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: info
    message: "Nickel components complete."
```

## Tungsten Components

Commentary: Produce tungsten cathode components. Tungsten powder must be imported as no local recipe exists yet.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Producing tungsten cathode components."
- cmd: sim.import
  args:
    item: tungsten_powder
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: binder_material
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_tungsten_cathode_blank_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.run-recipe
  args:
    recipe: recipe_tungsten_cathode_coated_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: info
    message: "Tungsten components complete."
```

## Assembly

Commentary: Assemble the electrolysis cell unit from locally produced components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assembling electrolysis cell unit from local components."
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrolysis_cell_unit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: info
    message: "Electrolysis cell unit assembly complete."
```

## Checkpoint

Commentary: verify the build.

```sim-runbook
- cmd: sim.status
  args: {}
```
