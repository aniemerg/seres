# Chemical Reactor Heated v0 Runbook

Goal: build `chemical_reactor_heated_v0` while maximizing in-situ production of major subassemblies.

Approach:
1) Import all top-level parts and assemble a baseline unit.
2) Import core fabrication equipment and feedstocks.
3) Produce key parts in-situ (enclosure, manifolds, valve body, fasteners, gas scrubbing, leak test equipment subassemblies).
4) Assemble a second unit using locally-produced components where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: chemical_reactor_heated_v0_runbook
- cmd: sim.reset
  args:
    sim-id: chemical_reactor_heated_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting chemical_reactor_heated_v0 runbook."
```

## Baseline assembly (imported parts)

Commentary: import all BOM parts and assemble a baseline unit to validate the recipe path.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Baseline: import all top-level parts for chemical_reactor_heated_v0."
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
    item: enclosure_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_scrubbing_unit_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_inlet_manifold_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: valve_body_cast_rough
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: leak_test_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_heated_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Baseline chemical_reactor_heated_v0 assembly complete."
```

## Import core equipment

Commentary: bring in the fabrication, casting, and assembly tools needed for in-situ production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment for local fabrication."
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
    item: metal_shear_or_saw
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
    item: punch_press_or_drill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
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
    item: hand_tools_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_bench
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
    item: surface_treatment_station
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
    item: power_hammer_or_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: anvil_or_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_forming_press
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_treatment_furnace
    quantity: 1
    unit: unit
    ensure: true
```

## Local metal feedstock

Commentary: produce a small batch of metal_alloy_bulk for fastener fabrication.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce metal_alloy_bulk from regolith via MRE."
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
    quantity: 500
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
```

## Fastener kit (small) + enclosure (sheet metal)

Commentary: build a small fastener kit and fabricate an enclosure from sheet metal.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build fastener_kit_small and sheet-metal enclosure."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 6.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_enclosure_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
```

## Gas inlet manifold

Commentary: machine gas inlet manifold from steel plate.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Fabricate gas_inlet_manifold_v0."
- cmd: sim.import
  args:
    item: steel_plate_or_sheet
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_gas_inlet_manifold_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
```

## Valve body casting

Commentary: cast a rough valve body from imported metal feedstock.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Cast valve_body_cast_rough."
- cmd: sim.import
  args:
    item: metal_feedstock
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_valve_body_cast_rough_v1
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
```

## Fastener kit (medium)

Commentary: fabricate a medium fastener kit from steel stock and sheet.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce fastener_kit_medium locally."
- cmd: sim.import
  args:
    item: steel_stock_bar_or_billet
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_sheet_3mm
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
```

## Gas scrubbing unit

Commentary: assemble a gas scrubbing unit from steel stock, filter media, and gaskets.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build gas_scrubbing_unit_v0."
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 25.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: filter_cartridges_dust
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: sealing_gaskets
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_gas_scrubbing_unit_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
```

## Local subcomponents (pump/compressor)

Commentary: produce a few pump/compressor subcomponents from in-situ metal where possible.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Build local bearing_set_small and machine_frame_small."
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_bearing_set_small_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 60.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 5
```

## Leak test equipment subassemblies

Commentary: fabricate what we can locally, import the rest.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Prepare leak_test_equipment inputs."
- cmd: sim.import
  args:
    item: raw_metal_block
    quantity: 6.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fused_silica_glass
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_pressure_gauge_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 15.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_rubber_o_ring
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_piping_and_fittings_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
```

## In-situ assembly

Commentary: assemble a second unit using locally-produced components where possible.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble chemical_reactor_heated_v0 from locally-produced parts."
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_heated_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Local chemical_reactor_heated_v0 assembly attempt complete."
```

## Post-run subcomponent build

Commentary: ensure bearing_set_small is produced after other long-running work.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Post-run: build bearing_set_small."
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_bearing_set_small_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "bearing_set_small batches complete."
```

## Leak test equipment assembly (local compressor/pump)

Commentary: assemble compressor and vacuum pump locally, then build leak test equipment.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble air_compressor_small and vacuum_pump_small locally."
- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 24.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_o_ring_rubber
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_air_compressor_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_vacuum_pump_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.import
  args:
    item: control_circuit_board_basic
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
    recipe: recipe_machine_leak_test_equipment_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "Leak test equipment assembled with local compressor and vacuum pump."
```
