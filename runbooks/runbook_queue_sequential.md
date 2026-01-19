# Runbook Queue Sequential

Runs all machine_runbook_queue_sequential runbooks sequentially. This does not reset between runs; each runbook manages its own sim reset/use.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: runbook_queue_sequential
- cmd: sim.reset
  args:
    sim-id: runbook_queue_sequential
- cmd: sim.runbook
  args:
    file: alignment_tools_runbook.md
- cmd: sim.runbook
  args:
    file: assembly_station_runbook.md
- cmd: sim.runbook
  args:
    file: assembly_tools_basic_runbook.md
- cmd: sim.runbook
  args:
    file: balancing_machine_runbook.md
- cmd: sim.runbook
  args:
    file: ball_mill_v0_runbook.md
- cmd: sim.runbook
  args:
    file: blast_furnace_or_smelter_runbook.md
- cmd: sim.runbook
  args:
    file: casting_furnace_v0_runbook.md
- cmd: sim.runbook
  args:
    file: casting_mold_set_runbook.md
- cmd: sim.runbook
  args:
    file: ceramic_press_or_mold_set_runbook.md
- cmd: sim.runbook
  args:
    file: chemical_reactor_basic_runbook.md
- cmd: sim.runbook
  args:
    file: cnc_mill_runbook.md
- cmd: sim.runbook
  args:
    file: coil_winding_machine_runbook.md
- cmd: sim.runbook
  args:
    file: controlled_atmosphere_chamber_runbook.md
- cmd: sim.runbook
  args:
    file: coordinate_measuring_machine_runbook.md
- cmd: sim.runbook
  args:
    file: crucible_refractory_runbook.md
- cmd: sim.runbook
  args:
    file: cutting_tools_general_runbook.md
- cmd: sim.runbook
  args:
    file: drawing_die_set_basic_runbook.md
- cmd: sim.runbook
  args:
    file: drill_press_runbook.md
- cmd: sim.runbook
  args:
    file: drying_oven_runbook.md
- cmd: sim.runbook
  args:
    file: dust_collection_system_runbook.md
- cmd: sim.runbook
  args:
    file: electrodes_runbook.md
- cmd: sim.runbook
  args:
    file: electrolysis_cell_unit_v0_runbook.md
- cmd: sim.runbook
  args:
    file: fixturing_workbench_runbook.md
- cmd: sim.runbook
  args:
    file: forging_press_v0_runbook.md
- cmd: sim.runbook
  args:
    file: furnace_runbook.md
- cmd: sim.runbook
  args:
    file: furnace_basic_runbook.md
- cmd: sim.runbook
  args:
    file: furnace_high_temp_runbook.md
- cmd: sim.runbook
  args:
    file: generic_chemical_reactor_v0_runbook.md
- cmd: sim.runbook
  args:
    file: glass_furnace_v0_runbook.md
- cmd: sim.runbook
  args:
    file: grinding_wheels_runbook.md
- cmd: sim.runbook
  args:
    file: hand_tools_basic_runbook.md
- cmd: sim.runbook
  args:
    file: hand_tools_mechanical_runbook.md
- cmd: sim.runbook
  args:
    file: heat_treatment_furnace_v0_runbook.md
- cmd: sim.runbook
  args:
    file: heating_furnace_runbook.md
- cmd: sim.runbook
  args:
    file: high_temperature_power_supply_v0_runbook.md
- cmd: sim.runbook
  args:
    file: hot_press_v0_runbook.md
- cmd: sim.runbook
  args:
    file: hydraulic_assembly_tools_runbook.md
- cmd: sim.runbook
  args:
    file: hydraulic_press_runbook.md
- cmd: sim.runbook
  args:
    file: kiln_ceramic_runbook.md
- cmd: sim.runbook
  args:
    file: labor_bot_general_v0_runbook.md
- cmd: sim.runbook
  args:
    file: lathe_engine_v0_runbook.md
- cmd: sim.runbook
  args:
    file: lifting_equipment_runbook.md
- cmd: sim.runbook
  args:
    file: measurement_equipment_runbook.md
- cmd: sim.runbook
  args:
    file: metal_shear_or_saw_runbook.md
- cmd: sim.runbook
  args:
    file: milling_machine_general_v0_runbook.md
- cmd: sim.runbook
  args:
    file: mixer_or_blender_runbook.md
- cmd: sim.runbook
  args:
    file: molding_press_basic_runbook.md
- cmd: sim.runbook
  args:
    file: mre_reactor_v0_runbook.md
- cmd: sim.runbook
  args:
    file: plate_rolling_mill_runbook.md
- cmd: sim.runbook
  args:
    file: powder_mixer_runbook.md
- cmd: sim.runbook
  args:
    file: power_distribution_bus_runbook.md
- cmd: sim.runbook
  args:
    file: power_hammer_or_press_runbook.md
- cmd: sim.runbook
  args:
    file: precision_lathe_runbook.md
- cmd: sim.runbook
  args:
    file: precision_levels_runbook.md
- cmd: sim.runbook
  args:
    file: press_brake_runbook.md
- cmd: sim.runbook
  args:
    file: pressing_mold_set_runbook.md
- cmd: sim.runbook
  args:
    file: pyrolysis_chamber_v0_runbook.md
- cmd: sim.runbook
  args:
    file: quench_tank_runbook.md
- cmd: sim.runbook
  args:
    file: reduction_furnace_v0_runbook.md
- cmd: sim.runbook
  args:
    file: refractory_installation_tools_runbook.md
- cmd: sim.runbook
  args:
    file: rock_crusher_basic_runbook.md
- cmd: sim.runbook
  args:
    file: rolling_mill_v0_runbook.md
- cmd: sim.runbook
  args:
    file: saw_or_cutting_tool_runbook.md
- cmd: sim.runbook
  args:
    file: screening_equipment_runbook.md
- cmd: sim.runbook
  args:
    file: sintering_furnace_v0_runbook.md
- cmd: sim.runbook
  args:
    file: soldering_station_runbook.md
- cmd: sim.runbook
  args:
    file: stamping_press_basic_runbook.md
- cmd: sim.runbook
  args:
    file: surface_grinder_runbook.md
- cmd: sim.runbook
  args:
    file: surface_treatment_station_runbook.md
- cmd: sim.runbook
  args:
    file: test_bench_electrical_runbook.md
- cmd: sim.runbook
  args:
    file: vibrating_screen_v0_runbook.md
- cmd: sim.runbook
  args:
    file: welding_consumables_runbook.md
- cmd: sim.runbook
  args:
    file: welding_power_supply_v0_runbook.md
- cmd: sim.runbook
  args:
    file: welding_tools_set_runbook.md
- cmd: sim.runbook
  args:
    file: wire_crimping_tools_runbook.md
```
