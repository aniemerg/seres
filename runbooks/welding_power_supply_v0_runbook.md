# Welding Power Supply v0 Runbook

Goal: build `welding_power_supply_v0` with increasing ISRU coverage. Start with a
baseline import assembly, then produce subcomponents locally where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: welding_power_supply_v0_runbook
- cmd: sim.reset
  args:
    sim-id: welding_power_supply_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting welding power supply v0 runbook."
```

## Baseline import + assembly

Commentary: import all top-level inputs to validate the assembly recipe.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import all welding_power_supply_v0 inputs."
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
    item: welding_power_supply_unit
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: torch_assembly
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ground_clamp_and_cables
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_welding_power_supply_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Baseline welding_power_supply_v0 assembly attempt complete."
```

## Local subcomponents (partial ISRU)

Commentary: produce metal-alloy feedstock in-situ, then build torch assembly,
ground clamp, and power conditioning module locally. Electronics are still imported.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce regolith_metal_crude and build local subcomponents."
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
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel_stock for fasteners from regolith."
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
    item: plate_rolling_mill
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
    item: crucible_refractory
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 2
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
- cmd: sim.note
  args:
    style: info
    message: "Mine additional regolith for steel production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.note
  args:
    style: info
    message: "Extract iron ore from mare regolith (~60 batches for ~11 kg steel plus pig iron)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: info
    message: "Mine carbonaceous regolith for carbon extraction."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 56
- cmd: sim.note
  args:
    style: info
    message: "Extract carbon from carbonaceous regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: info
    message: "Convert carbon to reducing agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 9
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.note
  args:
    style: info
    message: "Smelt iron from ore."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: info
    message: "Refine iron into steel ingots."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: info
    message: "Produce 11 kg steel_stock for fasteners."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 11
- cmd: sim.advance-time
  args:
    hours: 120
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
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: winding_drums
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 6
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
    recipe: recipe_aluminum_wire_v0
    quantity: 20
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_torch_assembly_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_ground_clamp_and_cables_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_conditioning_module_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 36
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_power_supply_unit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: info
    message: "Local subcomponents ready (torch, ground clamp, power conditioning)."
```

## Final assembly (mixed local + imports)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Final assembly using local subcomponents and remaining imports."
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_welding_power_supply_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "welding_power_supply_v0 assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
- cmd: sim.provenance
  args: {}
```
