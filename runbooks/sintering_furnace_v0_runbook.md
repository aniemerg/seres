# Sintering Furnace v0 Runbook

Goal: Build `sintering_furnace_v0` and raise ISRU by producing the insulation pack from regolith.

## Machine Details
- **Mass**: 950 kg
- **Material Class**: steel
- **Capabilities**: High-temperature sintering furnace for ceramics/metal powders.

## Required Components (from recipe)
1. sintering_furnace_shell (1 unit)
2. heating_element_set_high_temp (1 unit)
3. insulation_pack_high_temp (1 unit)
4. temperature_sensing (1 unit)
5. sensor_suite_general (1 unit)
6. control_compute_module_imported (1 unit)
7. power_conditioning_module (1 unit)
8. cooling_loop_basic (1 unit)
9. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: sintering_furnace_v0_runbook
- cmd: sim.reset
  args:
    sim-id: sintering_furnace_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting sintering_furnace_v0 runbook."
```

## ISRU Build: Tooling and Imported Components

Commentary: Import assembly tooling and all non-insulation components needed for the ISRU run.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import tooling and non-insulation components."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: test_bench_electrical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sintering_furnace_shell
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
    item: power_conditioning_module
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
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
```

## Stage 2: ISRU insulation pack (regolith-based)

Commentary: Produce regolith powder and form an insulation pack locally.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: Produce insulation_pack_high_temp from regolith."
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
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine mare regolith for insulation feedstock (~1000 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Mined 1000 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Screen regolith into coarse/fine fractions."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_coarse_fraction_v0
    quantity: 1000
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.note
  args:
    style: success
    message: "Produced ~600 kg regolith_coarse_fraction and ~400 kg regolith_fine_fraction."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Grind coarse fraction to regolith_powder (need ~120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_powder_v0
    quantity: 127
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.note
  args:
    style: success
    message: "Produced ~121 kg regolith_powder."
- cmd: sim.note
  args:
    style: info
    message: "Step 2d: Convert regolith_powder to thermal_insulation_regolith_based_v0."
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_regolith_based_v0
    quantity: 120
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: success
    message: "Produced 120 kg thermal_insulation_regolith_based_v0."
- cmd: sim.note
  args:
    style: info
    message: "Step 2e: Assemble insulation_pack_high_temp from regolith insulation."
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
    message: "Produced 1 insulation_pack_high_temp (regolith-based)."
```

## Stage 3: Final assembly

Commentary: Assemble sintering_furnace_v0 using ISRU insulation pack.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 3: Assemble sintering_furnace_v0."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_sintering_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: milestone
    message: "Sintering furnace v0 assembled."
- cmd: sim.provenance
  args:
    item: sintering_furnace_v0
    quantity: 1
    unit: unit
```
