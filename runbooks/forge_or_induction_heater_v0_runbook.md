# Forge or Induction Heater v0 Runbook

Goal: Build `forge_or_induction_heater_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: 1800 kg
- **Material Class**: metal
- **Capabilities**: forging, induction_heating

## Required Components (Mass-Corrected Recipe)
1. metal_alloy_bulk (1720 kg) - structural frame
2. heating_element_set_industrial (1 unit)
3. insulation_pack_high_temp (1 unit)
4. motor_assembly (12 kg)
5. shaft_and_bearing_set (15 kg)
6. bearing_set_heavy (4 kg)
7. fastener_kit_medium (1 kg)
8. power_conditioning_module (1 kg)
9. control_compute_module_imported (2 kg)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: forge_or_induction_heater_v0_runbook
- cmd: sim.reset
  args:
    sim-id: forge_or_induction_heater_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting forge_or_induction_heater_v0 runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all BOM parts and assembly equipment to ensure the forge can be assembled.

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
    item: assembly_tools_basic
    quantity: 1
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
    item: process_power
    quantity: 2000
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: metal_alloy_bulk
    quantity: 1720.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_industrial
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_pack_high_temp
    quantity: 120.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: motor_assembly
    quantity: 12.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: shaft_and_bearing_set
    quantity: 15.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 4.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble forge from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_forge_or_induction_heater_v0_isru
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Baseline forge_or_induction_heater_v0 complete."
```

## Stage 2: Local Metal Production (ISRU)

Commentary: Produce metal_alloy_bulk from regolith using MRE process. Need 1720 kg, which is ~76 batches of recipe_metal_alloy_bulk_v0 (22.8 kg each).

```sim-runbook
- cmd: sim.use
  args:
    sim-id: forge_or_induction_heater_v0_runbook
- cmd: sim.reset
  args:
    sim-id: forge_or_induction_heater_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Local metal production from regolith"
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: assembly_station
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
    item: electrolysis_cell_unit_v0
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
    item: heating_element_set_industrial
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_pack_high_temp
    quantity: 120.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: motor_assembly
    quantity: 12.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: shaft_and_bearing_set
    quantity: 15.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 4.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 10000
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 25000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Produce 1720 kg metal_alloy_bulk from regolith (76 batches)"
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 76
- cmd: sim.advance-time
  args:
    hours: 500
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble forge with locally-produced metal"
- cmd: sim.run-recipe
  args:
    recipe: recipe_forge_or_induction_heater_v0_isru
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Stage 2 complete: Forge with local metal ISRU"
```

## Stage 3: Final Assembly
*To be implemented - optimize remaining components for ISRU*
