# Casting Furnace v0 Runbook

Goal: build `casting_furnace_v0` while maximizing in-situ production of major subassemblies.

Approach:
1) Import all top-level parts and assemble a baseline unit.
2) Produce in-situ inputs where feasible (regolith -> metal_alloy_bulk -> shell).
3) Assemble a second unit using locally-produced components where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: casting_furnace_v0_runbook
- cmd: sim.reset
  args:
    sim-id: casting_furnace_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting casting_furnace_v0 runbook."
```

## Import baseline equipment

Commentary: bring in the core production machines and tools needed for mining, processing, casting, welding, and assembly.

```sim-runbook
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
    item: forge_or_induction_heater_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_engine_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake_v0
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
- cmd: sim.note
  args:
    style: info
    message: "Baseline production equipment imported."
```

## Baseline assembly (imported parts)

Commentary: import all top-level parts and assemble a first unit to validate the recipe path.

```sim-runbook
- cmd: sim.import
  args:
    item: casting_furnace_shell
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: burner_or_heater_casting
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
    item: power_conditioning_module
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
    item: cooling_loop_basic
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
    recipe: recipe_machine_casting_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: info
    message: "Baseline casting furnace assembled from imported parts."
```

## In-situ production attempt

Commentary: produce metal_alloy_bulk from regolith, then run the shell fabrication steps that can be executed directly.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce metal_alloy_bulk from regolith and prep shell subcomponents."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 13000
    unit: kWh
    ensure: true

- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    output_quantity: 2200
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 22

- cmd: sim.start-process
  args:
    process: regolith_screening_sieving_v0
    output_quantity: 1320
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 110

- cmd: sim.start-process
  args:
    process: regolith_crushing_grinding_v0
    output_quantity: 1320
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 132

- cmd: sim.start-process
  args:
    process: regolith_based_thermal_insulation_v0
    output_quantity: 120
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 120

- cmd: sim.start-process
  args:
    process: oxygen_extraction_molten_regolith_electrolysis_v0
    output_quantity: 480
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 3800

- cmd: sim.start-process
  args:
    process: metal_casting_basic_v0
    output_quantity: 470
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 800

- cmd: sim.start-process
  args:
    process: welding_brazing_basic_v0
    output_quantity: 460
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 200

- cmd: sim.start-process
  args:
    process: sintering_and_hot_pressing_v0
    output_quantity: 55
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 140

- cmd: sim.start-process
  args:
    process: casting_furnace_shell_assembly_v0
    output_quantity: 1
    output_unit: unit
    duration: null
- cmd: sim.advance-time
  args:
    hours: 4
```

Commentary: produce insulation pack from regolith-based insulation where feasible; import electronics and other specialized assemblies.

```sim-runbook
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 4
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8

- cmd: sim.start-process
  args:
    process: fastener_kit_medium_production_v0
    output_quantity: 2
    output_unit: kg
    duration: null
- cmd: sim.advance-time
  args:
    hours: 4

- cmd: sim.start-process
  args:
    process: fastener_kit_small_fabrication_v0
    output_quantity: 1
    output_unit: unit
    duration: null
- cmd: sim.advance-time
  args:
    hours: 4

- cmd: sim.start-process
  args:
    process: power_conditioning_module_fabrication_v0
    output_quantity: 1
    output_unit: unit
    duration: null
- cmd: sim.advance-time
  args:
    hours: 10

- cmd: sim.start-process
  args:
    process: burner_or_heater_casting_fabrication_v0
    output_quantity: 1
    output_unit: unit
    duration: null
- cmd: sim.advance-time
  args:
    hours: 12

- cmd: sim.start-process
  args:
    process: cooling_loop_basic_fabrication_v0
    output_quantity: 1
    output_unit: unit
    duration: null
- cmd: sim.advance-time
  args:
    hours: 12

- cmd: sim.note
  args:
    style: info
    message: "Local subassemblies completed; electronics and some materials remain imported."
```

## Final assembly (local parts where possible)

```sim-runbook
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_casting_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Second casting furnace assembled using in-situ shell and locally produced subassemblies."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
