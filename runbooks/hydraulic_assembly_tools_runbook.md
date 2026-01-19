# Hydraulic Assembly Tools Runbook

Goal: Build `hydraulic_assembly_tools` using in-situ resources where possible.

## Machine Details
- **Mass**: 15 kg
- **Capabilities**: Specialized tools for hydraulic systems - torque wrenches, flare tools, hose crimpers, pressure test equipment, bleeding kits

## Strategy

The hydraulic_assembly_tools can achieve limited ISRU by producing machined_part_raw from regolith-derived steel. Electrical and electronic components must be imported.

ISRU components:
- machined_part_raw (1 kg) - from regolith-derived steel_plate_or_sheet

Imported components:
- electrical_wire_and_connectors (1 kg) - copper wire
- electronic_components_set (1 kg) - pressure sensors, electronics

Expected ISRU: ~7% (machined metal parts from regolith)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: hydraulic_assembly_tools_runbook
- cmd: sim.reset
  args:
    sim-id: hydraulic_assembly_tools_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting hydraulic_assembly_tools runbook."
```

## ISRU Build: Hydraulic Assembly Tools with Regolith-Derived Metal Parts

Commentary: Produce machined_part_raw from regolith-derived steel. Import electrical/electronic components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce machined metal parts from regolith."
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
    item: blast_furnace_or_smelter
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
    item: heating_furnace
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
    item: plate_rolling_mill
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
    item: saw_or_cutting_tool
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
    item: hand_tools_basic
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
    item: assembly_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: soldering_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_crimping_tools
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 1000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce steel_plate_or_sheet from regolith (need ~1.2 kg for 1 kg machined parts)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 14
- cmd: sim.advance-time
  args:
    hours: 14
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 11
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Cut steel plate into rough parts for machining."
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 0.2
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.note
  args:
    style: info
    message: "Machine cut parts into machined_part_raw (1 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 0.5
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.note
  args:
    style: milestone
    message: "Import electrical and electronic components, then assemble hydraulic tools."
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_assembly_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: hydraulic_assembly_tools with regolith-derived machined parts."
- cmd: sim.provenance
  args:
    item: hydraulic_assembly_tools
    quantity: 1
    unit: unit
```
