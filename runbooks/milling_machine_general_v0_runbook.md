# Milling Machine (General) v0 Runbook

Goal: build `milling_machine_general_v0` using ISRU-produced inputs where possible.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: milling_machine_general_v0_runbook
- cmd: sim.reset
  args:
    sim-id: milling_machine_general_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting milling_machine_general_v0 runbook."
```

## ISRU equipment imports

Commentary: import equipment for ISRU chains and final assembly.

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
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 2000
    unit: kWh
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
    item: blast_furnace_or_smelter
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
    item: wire_drawing_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: stamping_press_basic
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
    item: generic_chemical_reactor_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_unit_v0
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
    item: forging_press_v0
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
    item: cnc_mill
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
    item: rolling_mill_or_brake
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
    item: precision_lathe
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace
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
    item: heat_treatment_furnace_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lifting_equipment
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "ISRU equipment imported."
```

## ISRU: metal alloy bulk + bearings

Commentary: produce local metal alloy via MRE, then cast/machine/grind heavy bearings
and a basic cutting tool set.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce regolith_metal_crude, bearing_set_heavy, and cutting tools."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 4
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_heavy_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_cutting_tool_set_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 84
- cmd: sim.note
  args:
    style: info
    message: "ISRU bearings and cutting tools ready."
```

## ISRU: steel feedstock, ball screws, and fasteners

Commentary: produce steel from regolith and carbonaceous feedstock, then fabricate
ball screw assemblies and fasteners for the milling table.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce steel feedstock, ball screws, and fasteners."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 75
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 16
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 110
- cmd: sim.advance-time
  args:
    hours: 130
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 32
- cmd: sim.advance-time
  args:
    hours: 130
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 90
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 27
- cmd: sim.advance-time
  args:
    hours: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 15
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_ball_steel_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_ball_screw_assembly_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_bolt_hex_medium_steel_v0
    quantity: 216
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_nut_hex_medium_steel_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_1mm_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_washer_flat_medium_steel_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_washer_lock_medium_steel_v0
    quantity: 0.09
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_assembly_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.note
  args:
    style: info
    message: "ISRU ball_screw_assembly and fastener_kit_medium ready."
```

## ISRU: milling table (local iron)

Commentary: produce local iron from regolith, then cast/machine/grind a milling
table using local ball screws and fasteners.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce iron and assemble milling_table."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 84
- cmd: sim.advance-time
  args:
    hours: 84
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_metal_pure_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_milling_table_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.note
  args:
    style: info
    message: "ISRU milling_table assembled with local iron."
```

## ISRU: drive motor medium

Commentary: produce motor materials locally (electrical steel, aluminum wire, coil
insulation, housing, shaft) and assemble the medium drive motor.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: produce and assemble drive_motor_medium."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_highlands_v0
    quantity: 35
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_metal_from_regolith_carbothermic_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_powder_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_precursor_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_polymer_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_coil_insulation_material_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 110
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_metal_pure_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_steel_sheet_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 260
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_housing_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_shaft_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.run-recipe
  args:
    recipe: recipe_stator_rotor_lamination_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_coil_wound_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_drive_motor_medium_assembly_only_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: info
    message: "ISRU drive_motor_medium assembled."
```

## ISRU build (expanded)

Commentary: assemble milling machine with local bearings, cutting tools, and milling table.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU: assemble milling_machine_general_v0 with local subcomponents."
- cmd: sim.import
  args:
    item: spindle_head_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gearbox_reducer_medium
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
    item: control_compute_module_imported
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
    recipe: recipe_machine_milling_machine_general_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.note
  args:
    style: success
    message: "ISRU (expanded) milling_machine_general_v0 build complete."
- cmd: sim.provenance
  args:
    item: milling_machine_general_v0
    quantity: 1
    unit: unit
```

## Next ISRU targets

- Localize `spindle_head_basic` and `gearbox_reducer_medium` subcomponents.
- Replace imported `power_conditioning_module` and `sensor_suite_general` where recipes are available.
