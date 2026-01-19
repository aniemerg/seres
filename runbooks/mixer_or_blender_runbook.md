# Mixer or Blender Runbook

Goal: Build `mixer_or_blender` with ISRU steel for the drum, frame, and agitator where practical.

## Machine Details
- **Mass**: 80 kg
- **Material Class**: steel
- **Capabilities**: General-purpose mixing/blending for powders or pastes

## Required Components (from recipe)
1. mixer_drum_small (1 unit)
2. mixer_agitator_shaft_and_paddles (1 unit)
3. drive_motor_small (1 unit)
4. gearbox_reducer_small (1 unit)
5. support_frame_small (1 unit)
6. control_panel_basic (1 unit)
7. fastener_kit_small (1 unit)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: mixer_or_blender_runbook
- cmd: sim.reset
  args:
    sim-id: mixer_or_blender_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting mixer_or_blender runbook."
```

## ISRU Phase 1: Import tooling and equipment

Commentary: Import fabrication tooling and equipment needed for steel processing and assembly.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 1: Import tooling and equipment."
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
    item: rolling_mill_v0
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
```

## ISRU Phase 2: Produce steel sheet for mixer drum

Commentary: Produce steel_sheet_3mm from regolith-derived steel ingot for the mixer drum (60 kg needed).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 2: Produce steel sheet for mixer drum."
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

## ISRU Phase 3: Import components without ISRU recipes and produce steel_stock

Commentary: Import steel_bar_stock and filler_wire since no ISRU recipes available. Produce steel_stock and fastener_kit from ISRU iron ore.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 3: Import steel bar stock and produce fasteners."
- cmd: sim.note
  args:
    style: info
    message: "Import steel_bar_stock (26 kg for frame + agitator) and filler_wire (3 kg) - no ISRU recipes available."
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 26
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: filler_wire_basic
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Step 3a: Extract additional iron ore for steel_stock (~6.4 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 10.7
- cmd: sim.advance-time
  args:
    hours: 14
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~6.4 kg iron_ore_or_ilmenite."
- cmd: sim.note
  args:
    style: info
    message: "Step 3b: Mine additional carbonaceous regolith for carbon reducing agent."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 14
- cmd: sim.note
  args:
    style: success
    message: "Mined 100 kg regolith_carbonaceous."
- cmd: sim.note
  args:
    style: info
    message: "Step 3c: Extract carbon_reductant (~1.6 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 5.3
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: success
    message: "Extracted ~1.6 kg carbon_reductant."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 1.6
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Produced 1.6 kg carbon_reducing_agent."
- cmd: sim.note
  args:
    style: info
    message: "Step 3d: Produce steel_stock from regolith iron ore for fasteners (3 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 3.0
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.note
  args:
    style: success
    message: "Produced 3 kg steel_stock from regolith iron ore."
- cmd: sim.note
  args:
    style: info
    message: "Produce fastener_kit_small from regolith steel stock (2 units for frame + assembly)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: success
    message: "Produced 2 fastener_kit_small from regolith steel."
```

## ISRU Phase 4: Build mixer subcomponents

Commentary: Build the mixer drum, agitator, and support frame from ISRU materials. Import drive motor, gearbox, and control panel.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 4: Build mixer subcomponents."
- cmd: sim.note
  args:
    style: info
    message: "Step 4a: Build mixer_drum_small from ISRU steel sheet."
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_drum_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "Built mixer_drum_small from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 4b: Build mixer_agitator_shaft_and_paddles from ISRU steel bar."
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_agitator_shaft_and_paddles_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Built mixer_agitator_shaft_and_paddles from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 4c: Build support_frame_small from ISRU steel bar."
- cmd: sim.run-recipe
  args:
    recipe: recipe_support_frame_small_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "Built support_frame_small from regolith steel."
- cmd: sim.note
  args:
    style: info
    message: "Step 4d: Import drive_motor_small, gearbox_reducer_small, and control_panel_basic."
- cmd: sim.import
  args:
    item: drive_motor_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gearbox_reducer_small
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 1
    unit: unit
    ensure: true
```

## ISRU Phase 5: Final assembly

Commentary: Assemble the mixer_or_blender from ISRU and imported components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU Phase 5: Assemble mixer_or_blender."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_mixer_or_blender_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: milestone
    message: "Mixer or blender assembled from regolith-derived steel!"
- cmd: sim.provenance
  args:
    item: mixer_or_blender
    quantity: 1
    unit: unit
```
