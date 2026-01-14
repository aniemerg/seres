# Reduction Furnace v0 Runbook (v2 - Optimized ISRU)

Goal: Build `reduction_furnace_v0` with maximum ISRU percentage by producing major metal components from regolith.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: reduction_furnace_v0_v2
- cmd: sim.reset
  args:
    sim-id: reduction_furnace_v0_v2
- cmd: sim.note
  args:
    style: milestone
    message: "Starting reduction furnace v0 runbook (optimized)."
```

## Stage 1: Import fabrication equipment

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core fabrication equipment."
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

## Stage 2: Produce metal feedstock from regolith

Commentary: Produce 1000 kg of metal_alloy_bulk to supply all major components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce 1000 kg metal_alloy_bulk from regolith."
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
    quantity: 18000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 44
- cmd: sim.advance-time
  args:
    hours: 320
- cmd: sim.note
  args:
    style: success
    message: "Metal feedstock production complete (~1000 kg)."
```

## Stage 3: Reduction furnace shell (local)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build reduction_furnace_shell from local metal."
- cmd: sim.import
  args:
    item: refractory_castable
    quantity: 100
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: thermal_insulation_high_temp
    quantity: 25
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_reduction_furnace_shell_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
```

## Stage 4: Gas handling system (local)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build gas_handling_system from local metal."
- cmd: sim.import
  args:
    item: gas_blower_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_gas_handling_system_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 60
```

## Stage 5: Power bus (local)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build power_bus_high_current from local metal."
- cmd: sim.import
  args:
    item: ceramic_insulators
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 0.5
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_bus_high_current_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 30
```

## Stage 6: Insulation pack (regolith-based)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build insulation_pack_high_temp from regolith materials."
- cmd: sim.import
  args:
    item: thermal_insulation_regolith_based_v0
    quantity: 120
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
```

## Stage 7: Import remaining components

Commentary: Import components that require complex supply chains or electronics.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import remaining components."
- cmd: sim.import
  args:
    item: heating_element_set_high_temp
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
```

## Stage 8: Final assembly

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble reduction_furnace_v0 from local and imported components."
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
    message: "Reduction furnace v0 complete with optimized ISRU."
```
