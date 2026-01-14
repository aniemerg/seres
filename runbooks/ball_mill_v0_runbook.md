# Ball Mill v0 Runbook

Goal: build `ball_mill_v0` using in-situ resources where possible. Start by importing
all final parts for a baseline assembly, then attempt local production of each part
and subassembly.

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: ball_mill_v0_runbook
- cmd: sim.reset
  args:
    sim-id: ball_mill_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting ball mill v0 runbook."
```

## Baseline import + assembly

Commentary: import all BOM parts to ensure the ball mill can be assembled once, then
run the assembly recipe as a baseline.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import baseline equipment needed for assembly."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 2
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
    item: assembly_station
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mill_shell_generic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: liner_set_abrasion_resistant
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: trunnion_supports
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_medium
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
    item: support_frame_welded
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Baseline: imported all ball_mill_v0 BOM parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_ball_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 400
- cmd: sim.note
  args:
    style: success
    message: "Baseline ball_mill_v0 assembly complete."
```

## In-situ equipment + core feedstocks

Commentary: import the minimum tooling and seed materials to allow local production.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Import core equipment and starter feedstocks for local production."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drilling_equipment_v0
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
    item: dust_collection_system
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
    item: electrolysis_cell_unit_v0
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
    item: casting_furnace_v0
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
    item: chemical_reactor_heated_v0
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_basic
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_distribution_bus
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
    item: pyrolysis_chamber_v0
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
    item: crucible_refractory
    quantity: 2
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
    item: stamping_press_basic
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
    item: wire_drawing_die_set
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: winding_drums
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
    item: coil_winding_machine
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lifting_equipment
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
    item: steel_forming_press
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
    item: heat_treatment_furnace
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
    item: heating_furnace
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
- cmd: sim.import
  args:
    item: electrical_energy
    quantity: 13000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Core equipment imported."
```

## In-situ: regolith feedstocks + metal alloy bulk (MRE)

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Mine regolith feedstocks and produce metal_alloy_bulk via MRE."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_carbonaceous_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.start-process
  args:
    process: regolith_mining_lunar_highlands_v0
    duration: 6
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_alloy_bulk_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 240
```

## In-situ: casting parts for mill shell + trunnions + frame

Commentary: make core structural parts that depend on metal_alloy_bulk.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Cast mill shell, trunnions, and support frame."
- cmd: sim.note
  args:
    style: info
    message: "Prepare casting molds from regolith fines."
- cmd: sim.import
  args:
    item: binder_simple
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_fine_fraction_v0
    quantity: 50
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_prepared_mold_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_mill_shell_generic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_trunnion_supports_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_support_frame_welded_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
```

## In-situ: liner set from regolith fines

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce abrasion-resistant liner set."
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_liner_set_abrasion_resistant_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
```

## In-situ: steel stock for fasteners + motor shaft

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce steel stock and sheet for fasteners and motor shaft."
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 24
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 7
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 44
- cmd: sim.advance-time
  args:
    hours: 55
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 13
- cmd: sim.advance-time
  args:
    hours: 55
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 12
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 9
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_3mm_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 2
```

## In-situ: bearing set + fastener kit

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce bearing set and fastener kit."
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_heavy_v0
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 20
```

## In-situ: iron and silicon feedstocks

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce iron and silicon feedstocks."
- cmd: sim.start-process
  args:
    process: regolith_mining_simple_v0
    duration: 2
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 20
- cmd: sim.advance-time
  args:
    hours: 32
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 100
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_metal_pure_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 60
- cmd: sim.import
  args:
    item: regolith_lunar_highlands
    quantity: 650
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_metal_from_regolith_carbothermic_v0
    quantity: 5
- cmd: sim.advance-time
  args:
    hours: 5
```

## In-situ: aluminum + insulation materials

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce aluminum wire and coil insulation materials."
- cmd: sim.import
  args:
    item: sodium_chloride
    quantity: 120
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: water
    quantity: 120
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fluorite
    quantity: 2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_dioxide_gas
    quantity: 22
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_sodium_hydroxide_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 36
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydrochloric_acid_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 62
- cmd: sim.run-recipe
  args:
    recipe: recipe_methane_gas_v1
    quantity: 22
- cmd: sim.advance-time
  args:
    hours: 12
- cmd: sim.run-recipe
  args:
    recipe: recipe_alumina_powder_v0
    quantity: 6
- cmd: sim.advance-time
  args:
    hours: 62
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_anode_material_v0
    quantity: 22
- cmd: sim.advance-time
  args:
    hours: 18
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_anode_v0
    quantity: 16
- cmd: sim.advance-time
  args:
    hours: 25
- cmd: sim.run-recipe
  args:
    recipe: recipe_cryolite_flux_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 30
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_powder_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 1
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
    hours: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_coil_wound_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 50
```

## In-situ: drive motor medium

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce medium drive motor locally."
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_steel_sheet_v0
    quantity: 40
- cmd: sim.advance-time
  args:
    hours: 240
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_housing_steel_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_shaft_steel_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_stator_rotor_lamination_set_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.start-process
  args:
    process: drive_motor_medium_assembly_v0
    duration: 4
- cmd: sim.advance-time
  args:
    hours: 6
```

## In-situ: gearbox reducer medium

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Produce medium gearbox reducer locally."
- cmd: sim.import
  args:
    item: base_grease_stock_v0
    quantity: 1
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_raw
    quantity: 70
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 40
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: iron_pig_or_ingot
    quantity: 80
    unit: kg
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_shaft_set_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_lubrication_pack_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.run-recipe
  args:
    recipe: recipe_gearbox_housing_cast_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_gear_set_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 40
- cmd: sim.run-recipe
  args:
    recipe: recipe_gearbox_reducer_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 12
```

## Final assembly from local parts

```sim-runbook
- cmd: sim.note
  args:
    style: info
    message: "Advance time to drain remaining queued processes before final assembly."
- cmd: sim.advance-time
  args:
    hours: 200
- cmd: sim.note
  args:
    style: info
    message: "Final buffer advance to close out short batch steps."
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.note
  args:
    style: info
    message: "Second buffer to flush any trailing assembly steps."
- cmd: sim.advance-time
  args:
    hours: 5
- cmd: sim.note
  args:
    style: milestone
    message: "Assemble ball_mill_v0 from locally produced parts."
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_ball_mill_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.note
  args:
    style: success
    message: "ball_mill_v0 local assembly attempt complete."
```

## Checkpoint

```sim-runbook
- cmd: sim.status
  args: {}
```
