# Glass Furnace v0 Runbook

Goal: Build `glass_furnace_v0` using in-situ resources where possible.

## Machine Details
- **Mass**: 1400 kg
- **Capabilities**: Batch/continuous glass melting furnace for glass production

## Strategy

The glass_furnace_v0 can achieve moderate-high ISRU by producing the furnace shell, insulation, cooling loop tubing, and fasteners from regolith-derived materials. Heating elements, electrical components, sensors, pump, and valves must be imported.

ISRU components:
- furnace_shell_refractory (~560 kg) - from regolith_metal_crude + regolith_fine_fraction
- insulation_pack_high_temp (~120 kg) - from regolith-based thermal insulation
- cooling_loop_basic metal parts (~52 kg) - from regolith_metal_crude
- fastener_kit_medium (~1 kg) - from regolith-derived steel

Imported components:
- heating_element_set_high_temp (electrical heating)
- power_bus_high_current (electrical distribution)
- temperature_sensing, sensor_suite_general (sensors/controls)
- control_compute_module_imported (computer)
- circulation_pump_coolant, fittings_and_valves (cooling loop components)

Expected ISRU: ~52% (structural/thermal components from regolith)

## Setup

```sim-runbook
- cmd: sim.use
  args:
    sim-id: glass_furnace_v0_runbook
- cmd: sim.reset
  args:
    sim-id: glass_furnace_v0_runbook
- cmd: sim.note
  args:
    style: milestone
    message: "Simulation reset. Starting glass_furnace_v0 runbook."
```

## ISRU Build: Glass Furnace with Regolith-Derived Components

Commentary: Produce furnace shell, insulation pack, cooling loop metal, and fasteners from regolith. Import electrical/electronic components.

```sim-runbook
- cmd: sim.note
  args:
    style: milestone
    message: "ISRU build: produce furnace shell, insulation, cooling loop, and fasteners from regolith."
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
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
    item: sintering_furnace_v0
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
    item: assembly_station
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
    item: fixturing_workbench
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
    item: heating_furnace
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
    item: plate_rolling_mill
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
    item: electrical_energy
    quantity: 10000
    unit: kWh
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_metal_crude for furnace shell and cooling loop (~28 batches for 607 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 28
- cmd: sim.advance-time
  args:
    hours: 700
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_fine_fraction for refractory lining (60 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_fine_fraction_v0
    quantity: 60
- cmd: sim.advance-time
  args:
    hours: 10
- cmd: sim.note
  args:
    style: info
    message: "Produce furnace_shell_refractory from regolith metal and fine fraction."
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_shell_refractory_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 13
- cmd: sim.note
  args:
    style: info
    message: "Produce regolith_powder for thermal insulation (need ~126 kg to get 120 kg)."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_powder_v0
    quantity: 127
- cmd: sim.advance-time
  args:
    hours: 18
- cmd: sim.note
  args:
    style: info
    message: "Produce thermal_insulation_regolith_based_v0 from regolith powder."
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_regolith_based_v0
    quantity: 120
- cmd: sim.advance-time
  args:
    hours: 120
- cmd: sim.note
  args:
    style: info
    message: "Produce insulation_pack_high_temp from regolith-based insulation."
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_regolith_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: info
    message: "Produce cooling_loop_basic (import metal_feedstock, pump, and valves)."
- cmd: sim.import
  args:
    item: metal_feedstock
    quantity: 57
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: circulation_pump_coolant
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.run-recipe
  args:
    recipe: recipe_cooling_loop_basic_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.note
  args:
    style: info
    message: "Produce fastener_kit_medium from regolith-derived steel."
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 70
- cmd: sim.advance-time
  args:
    hours: 70
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 16
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 10
- cmd: sim.advance-time
  args:
    hours: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 3
- cmd: sim.advance-time
  args:
    hours: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 2
- cmd: sim.advance-time
  args:
    hours: 20
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 8
- cmd: sim.note
  args:
    style: milestone
    message: "Import electrical components, heating elements, sensors, and controls, then assemble glass furnace."
- cmd: sim.import
  args:
    item: heating_element_set_high_temp
    quantity: 1
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_bus_high_current
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
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_glass_furnace_v0
    quantity: 1
- cmd: sim.advance-time
  args:
    hours: 3
- cmd: sim.note
  args:
    style: success
    message: "ISRU build complete: glass_furnace_v0 with regolith-derived shell, insulation, cooling loop, and fasteners."
- cmd: sim.provenance
  args:
    item: glass_furnace_v0
    quantity: 1
    unit: unit
```
