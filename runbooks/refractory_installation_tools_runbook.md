# Refractory Installation Tools Runbook

Goal: Build `refractory_installation_tools` (10 kg tool set) using maximum in-situ resources where practical. Current recipe is a light assembly of specialized sub-tools, so this runbook imports the sub-tools and assembles the set.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: refractory_installation_tools_runbook
- cmd: sim.reset
  args:
    sim-id: refractory_installation_tools_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting refractory_installation_tools runbook."
```

## Build tool set (import sub-tools)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce anchor_installation_kit with local tool steel."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
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
    item: blast_furnace_or_smelter
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
    item: casting_mold_set
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
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Mine and refine regolith for tool steel feedstock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 10
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
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 1.5
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_steel_high_carbon_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.import
  args:
    item: drill_bit_carbide
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_anchor_installation_kit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: info
    message: "Import sub-tools and assembly tooling."
- cmd: sim.import
  args:
    item: hot_wire_cutter
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: refractory_trowel_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cement_mixer_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_brush_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Assemble refractory_installation_tools from the tool set."
- cmd: sim.run-recipe
  args:
    recipe: recipe_refractory_installation_tools_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Refractory installation tools assembled."
- cmd: sim.provenance
  args:
    item: refractory_installation_tools
    quantity: 1
    unit: unit
```
