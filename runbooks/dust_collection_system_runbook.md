# Dust Collection System Runbook

Goal: Build `dust_collection_system` using in-situ resources where possible.

## Machine Details
- **Mass**: 200 kg
- **Capabilities**: Industrial dust collection for regolith processing

## Required Components (from recipe)
1. sheet_metal_or_structural_steel (220 kg) - main steel structure
2. cyclone_separator_body (1 unit)
3. filter_cartridges_dust (4 units)
4. vacuum_blower_industrial (1 unit)
5. drive_motor_medium (1 unit)
6. ductwork_and_fittings (1 unit)
7. collection_hopper_drum (1 unit)
8. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: dust_collection_system_runbook
- cmd: sim.reset
  args:
    sim-id: dust_collection_system_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting dust_collection_system runbook."
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
    item: metal_shear_or_saw
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
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: punch_press_or_drill
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
    item: sheet_metal_or_structural_steel
    quantity: 220
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cyclone_separator_body
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: filter_cartridges_dust
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vacuum_blower_industrial
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ductwork_and_fittings
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: collection_hopper_drum
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
    message: "Assemble dust collection system from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_dust_collection_system_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 65
- cmd: sim.note
  args:
    style: success
    message: "Baseline dust_collection_system complete."
```

## Stage 2: Local Steel Production (ISRU)

Commentary: Produce sheet_metal_or_structural_steel (220 kg) from regolith metal. Need 244 kg regolith_metal_crude total, which is ~11 batches of MRE.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: dust_collection_system_runbook
- cmd: sim.reset
  args:
    sim-id: dust_collection_system_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Local steel production from regolith"
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
    item: metal_shear_or_saw
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
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: punch_press_or_drill
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
    item: vibrating_screen_v0
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
    item: dust_collection_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cyclone_separator_body
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: filter_cartridges_dust
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vacuum_blower_industrial
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ductwork_and_fittings
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: collection_hopper_drum
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 2000
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 10000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce 244 kg regolith_metal_crude from regolith (11 batches)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 11
- cmd: sim.advance-time
  args:
    hours: 110
- cmd: sim.note
  args:
    style: milestone
    message: "Produce sheet metal from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble dust collection system with locally-produced steel"
- cmd: sim.run-recipe
  args:
    recipe: recipe_dust_collection_system_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 65
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: Dust collection system with local steel ISRU"
```

## Stage 3: Final Assembly
*To be implemented - final build with maximum ISRU*
