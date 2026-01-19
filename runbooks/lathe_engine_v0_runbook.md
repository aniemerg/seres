# Lathe Engine v0 Runbook

Goal: Build `lathe_engine_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: 180 kg
- **Material Class**: steel/iron
- **Capabilities**: Manual engine lathe for basic turning operations. Compact design for small-scale metalworking in seed factory.

## Required Components (from recipe)
1. lathe_bed_simple (1 unit) - cast iron bed with precision ways (needs 45 kg iron_pig_or_ingot)
2. lathe_headstock_simple (1 unit) - headstock assembly
3. lathe_spindle_and_bearings (1 unit) - main spindle assembly
4. tailstock_assembly (1 unit) - tailstock for workpiece support
5. lathe_carriage_simple (1 unit) - carriage with cross-slide
6. lathe_leadscrew_simple (1 unit) - leadscrew for manual feed
7. lathe_tool_post_basic (1 unit) - tool post
8. motor_electric_small (1 unit) - 1-2 kW drive motor
9. gearbox_reducer_small (1 unit) - speed reduction gearbox
10. bearing_set_heavy (4 kg) - bearings for bed ways (can be produced from regolith_metal_crude)
11. control_panel_basic (1 unit) - control panel
12. turning_tools_general (1 unit) - set of turning tools
13. fastener_kit_medium (1 unit) - assembly fasteners
14. safety_guard_steel_mesh (1 unit) - safety guards

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: lathe_engine_v0_runbook
- cmd: sim.reset
  args:
    sim-id: lathe_engine_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting lathe_engine_v0 runbook."
```

## Single-Stage ISRU Build

Commentary: Produce the lathe bed from local iron (via regolith → ilmenite → iron) and bearings from regolith metal. Import remaining components (motor, gearbox, electronics, specialized assemblies).

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Single-stage ISRU build: produce iron bed and bearings locally."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 3
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
    item: electrical_energy
    quantity: 5000
    unit: kWh
    ensure: true
```

## Regolith mining and processing

```sim-runbook
- cmd: sim.note
  args:
    style: info
    message: "Import regolith processing equipment."
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
    style: milestone
    message: "Mine and process regolith for iron and metal production."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 500
- cmd: sim.advance-time
  args:
    hours: 70
```

## Iron production chain

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce iron from regolith via ilmenite extraction and reduction."
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 120
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.note
  args:
    style: info
    message: "Produce carbon reducing agent from regolith."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 25
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.note
  args:
    style: milestone
    message: "Smelt iron from ilmenite using carbon reductant."
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 250
```

## Produce lathe bed from local iron

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce lathe_bed_simple from local iron (45 kg needed)."
- cmd: sim.import
  args:
    item: casting_furnace_v0
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
    item: surface_grinder
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
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_bed_simple_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
```

## Produce bearings from regolith metal

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce bearing_set_heavy from regolith_metal_crude (4 kg needed)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 150
- cmd: sim.import
  args:
    item: lathe_engine_v0
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
    item: bearing_grinding_machine_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: forge_or_induction_heater_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_heavy_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 25
```

## Import remaining components and assemble

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import specialized components (motor, gearbox, electronics, assemblies)."
- cmd: sim.import
  args:
    item: lathe_headstock_simple
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_spindle_and_bearings
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tailstock_assembly
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_carriage_simple
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_leadscrew_simple
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_tool_post_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_electric_small
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
- cmd: sim.import
  args:
    item: turning_tools_general
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: safety_guard_steel_mesh
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: success
    message: "Assemble lathe_engine_v0 with local bed and bearings."
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_engine_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: success
    message: "lathe_engine_v0 assembly complete."
- cmd: sim.provenance
  args:
    item: lathe_engine_v0
```

## Expected ISRU

The primary ISRU components are:
- **lathe_bed_simple** (~45 kg iron from regolith)
- **bearing_set_heavy** (~4 kg from regolith metal)

Total ISRU mass: ~49 kg out of 180 kg = **~27% ISRU**

The remaining mass is in specialized assemblies (headstock, spindle, carriage, leadscrew, motor, gearbox, controls) that would require extensive additional production chains to manufacture locally.
