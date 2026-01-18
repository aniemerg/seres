# Heat Treatment Furnace v0 Runbook

Goal: Build `heat_treatment_furnace_v0` with ISRU furnace shell and quench rack while importing electronics and heating elements.

## Machine Details
- **Mass**: 537 kg
- **Material Class**: steel
- **Capabilities**: heat treating metals with controlled cycles

## Required Components (from recipe)
1. furnace_shell_insulated (1 unit)
2. refractory_lining_set (1 unit)
3. heating_element_set_basic (1 unit)
4. temperature_controller_basic (1 unit)
5. level_sensor_basic (1 unit)
6. sensor_suite_general (1 unit)
7. control_compute_module_imported (1 unit)
8. power_conditioning_module (1 unit)
9. quench_rack_and_baskets (1 unit)
10. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: heat_treatment_furnace_v0_runbook
- cmd: sim.reset
  args:
    sim-id: heat_treatment_furnace_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting heat_treatment_furnace_v0 runbook."
```

## ISRU Phase 1: Import equipment and materials

Commentary: Import mining/casting/machining tooling plus electronics and materials that are not ISRU.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import equipment for ISRU production."
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
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: refractory_installation_tools
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
    item: coil_winding_machine
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
- cmd: sim.import
  args:
    item: silica_purified
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_thermal_blanket
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: refractory_lining_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: level_sensor_basic
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
    item: power_conditioning_module
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

## ISRU Phase 2: Produce regolith metal and cast components

Commentary: Produce regolith_metal_crude and cast the furnace shell plus quench rack.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal and cast shell + quench rack."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Produce regolith_metal_crude (~320 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 14
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.note
  args:
    style: success
    message: "Produced ~319 kg regolith_metal_crude."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Cast furnace_shell_insulated."
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_shell_insulated_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 furnace_shell_insulated."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Cast quench_rack_and_baskets."
- cmd: sim.run-recipe
  args:
    recipe: recipe_quench_rack_and_baskets_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Produced 1 quench_rack_and_baskets."
```

## ISRU Phase 3: Final assembly

Commentary: Assemble heat_treatment_furnace_v0 and verify provenance.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble heat_treatment_furnace_v0."
- cmd: sim.run-recipe
  args:
    recipe: recipe_heat_treatment_furnace_v0_target_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 600
- cmd: sim.note
  args:
    style: milestone
    message: "Heat treatment furnace v0 assembled."
- cmd: sim.provenance
  args:
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
```
