# Reduction Furnace v0 Runbook

Goal: Build `reduction_furnace_v0` using in-situ resources where possible. Start by importing
all final parts for a baseline assembly, then produce major components locally.

## Machine Details
- **Mass**: 1300 kg
- **Material Class**: refractory
- **Capabilities**: reduction_furnace, carbothermal_reduction, metal_oxide_reduction, high_temp_processing
- **Temperature Range**: 1200-1600°C

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: reduction_furnace_v0_runbook
- cmd: sim.reset
  args:
    sim-id: reduction_furnace_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting reduction furnace v0 runbook."
```

## Stage 1: Baseline (import all components)

Commentary: Import all BOM parts and assembly equipment to ensure the furnace can be assembled.

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
    item: process_power
    quantity: 1000
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: reduction_furnace_shell
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: insulation_pack_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_handling_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: offgas_manifold
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cooling_loop_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_bus_high_current
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_sensing
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
    item: control_compute_module_imported
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
    message: "Assemble reduction furnace from imported parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_reduction_furnace_v0
    quantity: 1
- cmd: sim.note
  args:
    style: success
    message: "Baseline reduction furnace v0 complete."
```

## Stage 2: Import core equipment

Commentary: bring in the fabrication, welding, machining, and casting tools for local production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for local fabrication."
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
    item: welding_tools_set
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
    item: hot_press_v0
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
    item: dies
    quantity: 1
    unit: unit
    ensure: true
```

## Stage 3: Local metal feedstock

Commentary: produce metal_alloy_bulk from regolith via processing chain.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce metal_alloy_bulk from regolith."
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
    quantity: 8500
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 22
- cmd: sim.advance-time
  args:
    hours: 160
- cmd: sim.note
  args:
    style: success
    message: "Metal feedstock production complete."
```

## Stage 4: Skip shell production (KB issue)

Commentary: Skipping shell production due to mass mismatch in KB. Would produce locally in future iteration.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Skipping shell production due to KB mass mismatch."
```

## Stage 5: Heating element set

Commentary: fabricate high-temperature heating elements from local metal.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Fabricate heating_element_set_high_temp locally."
- cmd: sim.import
  args:
    item: machined_part_raw
    quantity: 80.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_element_set_high_temp_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Heating elements complete."
```

## Stage 6: Insulation pack (regolith-based)

Commentary: produce high-temp insulation from local regolith materials.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce insulation_pack_high_temp from regolith."
- cmd: sim.import
  args:
    item: thermal_insulation_regolith_based_v0
    quantity: 120.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Insulation pack complete."
```

## Stage 7: Wait for in-progress recipes

Commentary: advance time to ensure all recipes complete.

```sim-runbook
- cmd: sim.advance-time
  args:
    hours: 20
```

## Stage 8: Import remaining components

Commentary: Import the remaining smaller components that we're not producing locally in this iteration.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining components for second furnace."
- cmd: sim.import
  args:
    item: reduction_furnace_shell
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_handling_system
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: offgas_manifold
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cooling_loop_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_bus_high_current
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
    unit: unit
    ensure: true
```

## Stage 9: Final ISRU assembly

Commentary: assemble a second reduction furnace using locally-produced major components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble reduction_furnace_v0 from locally-produced parts."
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_sensing
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_reduction_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: success
    message: "Local reduction_furnace_v0 assembly complete with partial ISRU."
```
