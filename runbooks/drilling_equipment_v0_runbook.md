# Drilling Equipment v0 Runbook

Goal: Build `drilling_equipment_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: 500 kg
- **Material Class**: steel
- **Capabilities**: drilling, boring, subsurface_access

## Required Components (from recipe)
1. motor_electric_medium (2 units, ~80 kg each = 160 kg)
2. structural_frame_steel (150 kg)
3. drill_string_steel (100 kg)
4. hydraulic_power_unit_basic (1 unit, ~150 kg)
5. cutting_tool_set_basic (5 units)
6. bearing_set_heavy (4 units)
7. control_panel_basic (1 unit)
8. fastener_kit_medium (2 units)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: drilling_equipment_v0_runbook
- cmd: sim.reset
  args:
    sim-id: drilling_equipment_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting drilling_equipment_v0 runbook."
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
    item: motor_electric_medium
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: structural_frame_steel
    quantity: 150
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: drill_string_steel
    quantity: 100
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_power_unit_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cutting_tool_set_basic
    quantity: 5
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble drilling equipment from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_drilling_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Baseline drilling_equipment_v0 complete."
```

## Stage 2: Local Steel Production (ISRU)

Commentary: Produce structural_frame_steel (150 kg) and drill_string_steel (100 kg) from regolith metal. Need 275 kg regolith_metal_crude total, which is ~13 batches of MRE.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: drilling_equipment_v0_runbook
- cmd: sim.reset
  args:
    sim-id: drilling_equipment_v0_runbook
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
    item: motor_electric_medium
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_power_unit_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cutting_tool_set_basic
    quantity: 5
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
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
    message: "Produce 275 kg regolith_metal_crude from regolith (13 batches)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: milestone
    message: "Produce structural frame from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_frame_steel_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: milestone
    message: "Produce drill string from local metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_drill_string_steel_isru_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble drilling equipment with locally-produced steel"
- cmd: sim.run-recipe
  args:
    recipe: recipe_drilling_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: Drilling equipment with local steel ISRU"
```

## Stage 3: Final Assembly
*To be implemented - optimize remaining components for ISRU*
