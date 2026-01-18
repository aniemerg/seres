# Powder Mixer Runbook

Goal: Build `powder_mixer` with ISRU steel for the frame, drum, and agitator where practical.

## Machine Details
- **Mass**: 80 kg
- **Material Class**: steel
- **Capabilities**: Powder mixing for metal or ceramic feedstock preparation.

## Required Components (from recipe)
1. mixer_frame_small (1 unit)
2. mixer_drum_small (1 unit)
3. mixer_motor_small (1 unit)
4. mixer_agitator_shaft_and_paddles (1 unit)
5. mixer_control_basic (1 unit)
6. fastener_kit_medium (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: powder_mixer_runbook
- cmd: sim.reset
  args:
    sim-id: powder_mixer_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting powder_mixer runbook."
```

## Stage 1: Tooling and imports

Commentary: Import fabrication tooling and any non-ISRU electronics.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 1: Import tooling and components."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: rolling_mill_or_brake
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
    item: hydraulic_press
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
    item: welding_tools_set
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
    item: surface_grinder
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
    item: test_bench_electrical
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drawing_die_set_basic
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
    item: furnace_basic
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
    item: high_temperature_power_supply_v0
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
    item: electrodes
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_coil_wound
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bulk_material_or_parts
    quantity: 1
    unit: kg
    ensure: true
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
- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 10
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
```

## Stage 2: ISRU steel for drum sheet

Commentary: Produce steel_sheet_3mm from regolith-derived steel ingot.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 2: ISRU steel sheet for mixer drum."
- cmd: sim.note
  args:
    style: info
    message: "Step 2a: Mine mare regolith for iron ore (~126 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Mined 300 kg regolith_lunar_mare."
- cmd: sim.note
  args:
    style: info
    message: "Step 2b: Extract ilmenite for iron ore."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 210
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~126 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 2c: Mine carbonaceous regolith for reducing agent (~32 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 22
- cmd: sim.advance-time
  args:
    hours: 140
- cmd: sim.note
  args:
    style: success
    message: "Mined 1100 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 2d: Extract carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 110
- cmd: sim.advance-time
  args:
    hours: 180
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~32 kg carbon_reductant."
- cmd: sim.note
  args:
    style: info
    message: "Step 2e: Convert to carbon_reducing_agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 80
- cmd: sim.note
  args:
    style: success
    message: "Produced 32 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 2f: Smelt pig iron for steel (63 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 63
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.note
  args:
    style: success
    message: "Produced 63 kg iron_pig_or_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 2g: Cast steel ingots for sheet (60 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: success
    message: "Produced 60 kg steel_ingot."
- cmd: sim.note
  args:
    style: info
    message: "Step 2h: Roll steel_sheet_3mm (60 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_3mm_v1
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: success
    message: "Produced 60 kg steel_sheet_3mm."
```

## Stage 3: ISRU steel for frame, agitator, and motor housing

Commentary: Produce regolith metal for steel beams, bar stock, and motor housing.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 3: ISRU regolith metal for frame and agitator."
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 1200
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Produce regolith_metal_crude (~68 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 3.0
- cmd: sim.advance-time
  args:
    hours: 70
- cmd: sim.note
  args:
    style: success
    message: "Produced ~68 kg regolith_metal_crude."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Form steel_beam_i_section for frame."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_beam_i_section_isru_v0
    quantity: 0.6
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Produced ~36 kg steel_beam_i_section."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Roll steel_stock_bar_or_billet and steel_bar_stock."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_isru_v0
    quantity: 0.07
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: success
    message: "Produced ~19 kg steel_stock_bar_or_billet."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 17.5
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Produced ~17.5 kg steel_bar_stock."
- cmd: sim.note
  args:
    style: info
    message: "Step 3d: Draw filler_wire_basic for drum welding (3 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_filler_wire_basic_v0
    quantity: 1.5
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Produced 3 kg filler_wire_basic."
```

## Stage 4: Build mixer subcomponents

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 4: Build mixer subcomponents."
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_frame_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_drum_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_agitator_shaft_and_paddles_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_motor_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_control_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
```

## Stage 5: Assemble powder_mixer

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Stage 5: Assemble powder_mixer."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_powder_mixer_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.note
  args:
    style: milestone
    message: "Powder mixer assembled."
- cmd: sim.provenance
  args:
    item: powder_mixer
    quantity: 1
    unit: unit
```
