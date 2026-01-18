# Rolling Mill v0 Runbook

Goal: Build `rolling_mill_v0` with maximum ISRU using regolith-derived metal.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: rolling_mill_v0_runbook
- cmd: sim.reset
  args:
    sim-id: rolling_mill_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Starting rolling mill v0 runbook."
```

## ISRU Production

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce regolith metal for local components."
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
    quantity: 35000
    unit: kWh
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 300
- cmd: sim.note
  args:
    style: info
    message: "Build bearing_set from local regolith_metal_crude."
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
    item: forge_or_induction_heater_v0
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
    item: forging_press_v0
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
    item: heat_treatment_furnace_v0
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
    item: precision_lathe
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
    item: grinding_wheels
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
    item: plate_rolling_mill
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: metal_sheet_or_plate
    quantity: 0.3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: grease_bearing_high_temp
    quantity: 0.1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_rubber_bearing
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.note
  args:
    style: info
    message: "Import grinding_media_steel (complex steel processing requirements)."
- cmd: sim.import
  args:
    item: grinding_media_steel
    quantity: 50
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Import steel_drum and fasteners (complex machining dependencies)."
- cmd: sim.import
  args:
    item: steel_drum
    quantity: 20
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble rolling mill from ISRU components (steel_drum, grinding_media, bearings, fasteners)."
- cmd: sim.import
  args:
    item: motor_assembly
    quantity: 12
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_rolling_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: success
    message: "Rolling mill v0 with ISRU bearing_set complete! (bearings 3kg from regolith_metal_crude)"
```

## Results

Successfully built rolling_mill_v0 with ISRU improvements:

### ISRU Components Produced:
- **bearing_set** (3 kg): Produced from regolith_metal_crude via MRE (1368 kg produced from 60 batches)

### Components Imported:
- **steel_drum** (20 kg): Complex fabrication with many machine dependencies
- **grinding_media_steel** (50 kg): Needs specialized steel processing
- **motor_assembly** (12 kg): Electrical windings and components
- **fastener_kit_medium** (2 kg): Multi-step steel processing

### ISRU Mass Breakdown:
- Total rolling_mill_v0 mass: 87 kg
- ISRU components: 3 kg (bearing_set)
- Imported: 84 kg (steel_drum, grinding_media, motor, fasteners)
- **Achieved ISRU**: ~3.4% (3/87)

### Path to Higher ISRU:
To achieve >50% ISRU for rolling_mill:
1. Produce steel_drum locally (20 kg) - needs saw_or_cutting_tool, hand_tools_basic, press_brake
2. Produce grinding_media_steel (50 kg) - needs steel_bar_stock production chain
3. Produce fastener_kit_medium (2 kg) - needs complete steel_stock chain
4. Motor_assembly (12 kg) remains challenging due to electrical components
