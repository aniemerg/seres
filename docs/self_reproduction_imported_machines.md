# Self-Reproduction Imported Machines

This file lists the machines imported by the current self-reproduction demo output. The demo script filters imports to KB entries whose `kind` is `machine`.

## Sources

- Scenario file: `kb/scenarios/min_seed.yaml`
- Canonical target machine list: `docs/self_reproducing_set.txt`
- Demo summary: `out/self_repro_demo/summary.md`
- Imported-machine output: `out/self_repro_demo/imported_machines.txt`
- Demo script: `scripts/analysis/run_self_reproduction_demo.py`

## Summary

- Imported machine count: 117
- Source simulation: `out/self_repro_demo/summary.md`

Relevant demo checks:

- Requested machines: 135
- Produced machines: 135
- Imported machines: 117
- Requested not produced: 0
- Produced not requested: 0
- Imported not produced: 0
- Produced not imported: 18
- Requested not imported: 18
- In-situ mass: 25554.21 kg
- Imported mass: 437047.94 kg
- Unknown mass: 0.00 kg
- Total mass: 462602.16 kg
- ISRU: 5.52%
Requested == Produced: True
Imports ⊆ Produced: True

## Imported Machines

| # | Machine ID | Name | KB kind | KB item file |
|---:|---|---|---|---|
| 1 | `anvil_or_die_set` | Anvil or die set | `machine` | `kb/items/parts/anvil_or_die_set.yaml` |
| 2 | `assembly_tools_basic` | Basic assembly tools | `machine` | `kb/items/machines/assembly_tools_basic.yaml` |
| 3 | `ball_mill_v0` | Ball mill v0 | `machine` | `kb/items/machines/ball_mill_v0.yaml` |
| 4 | `blast_furnace_or_smelter` | Blast furnace or smelter | `machine` | `kb/items/machines/blast_furnace_or_smelter.yaml` |
| 5 | `casting_furnace_v0` | Casting furnace v0 | `machine` | `kb/items/machines/casting_furnace_v0.yaml` |
| 6 | `casting_mold_set` | Casting mold set | `machine` | `kb/items/machines/casting_mold_set.yaml` |
| 7 | `cement_mixer_small` | Cement mixer (small) | `machine` | `kb/items/machines/cement_mixer_small.yaml` |
| 8 | `chemical_reactor_basic` | Basic chemical reactor | `machine` | `kb/items/machines/chemical_reactor_basic.yaml` |
| 9 | `chemical_reactor_vessel_v0` | Chemical reactor vessel v0 | `machine` | `kb/items/machines/chemical_reactor_vessel_v0.yaml` |
| 10 | `chemical_separation_equipment` | Chemical separation equipment | `machine` | `kb/items/machines/chemical_separation_equipment.yaml` |
| 11 | `cnc_mill` | CNC Milling Machine | `machine` | `kb/items/machines/cnc_mill.yaml` |
| 12 | `coil_winding_machine` | Coil winding machine | `machine` | `kb/items/machines/coil_winding_machine.yaml` |
| 13 | `control_compute_module_imported` | Control compute module (imported) | `machine` | `kb/items/machines/control_compute_module_imported.yaml` |
| 14 | `controlled_atmosphere_chamber` | Controlled atmosphere chamber | `machine` | `kb/items/machines/controlled_atmosphere_chamber.yaml` |
| 15 | `crucible_graphite` | Graphite crucible | `machine` | `kb/items/parts/crucible_graphite.yaml` |
| 16 | `crucible_refractory` | Refractory crucible | `machine` | `kb/items/machines/crucible_refractory.yaml` |
| 17 | `cutting_tools_general` | General cutting tools | `machine` | `kb/items/machines/cutting_tools_general.yaml` |
| 18 | `dies` | Dies and tooling | `machine` | `kb/items/parts/dies.yaml` |
| 19 | `drawing_die_set_basic` | Drawing die set (basic) | `machine` | `kb/items/machines/drawing_die_set_basic.yaml` |
| 20 | `drill_press` | Drill press | `machine` | `kb/items/machines/drill_press.yaml` |
| 21 | `drilling_equipment_v0` | Drilling equipment (field/mining) | `machine` | `kb/items/machines/drilling_equipment_v0.yaml` |
| 22 | `drying_basic_v0` |  | `machine` | `kb/items/machines/drying_basic_v0.yaml` |
| 23 | `drying_oven` | Drying oven | `machine` | `kb/items/machines/drying_oven.yaml` |
| 24 | `dust_collection_system` | Dust collection system | `machine` | `kb/items/machines/dust_collection_system_v0.yaml` |
| 25 | `electrodes` | Electrodes | `machine` | `kb/items/machines/electrodes.yaml` |
| 26 | `electrolysis_cell_unit_v0` | Electrolysis cell module v0 | `machine` | `kb/items/machines/electrolysis_cell_unit_v0.yaml` |
| 27 | `enclosure_small` | Enclosure (small) | `machine` | `kb/items/parts/enclosure_small.yaml` |
| 28 | `epoxy_synthesis_unit` | Epoxy synthesis unit | `machine` | `kb/items/machines/epoxy_synthesis_unit.yaml` |
| 29 | `excavator_basic` | Excavator (basic) | `machine` | `kb/items/machines/excavator_basic.yaml` |
| 30 | `fixturing_workbench` | Fixturing workbench | `machine` | `kb/items/machines/fixturing_workbench.yaml` |
| 31 | `forging_press_v0` | Forging press unit v0 | `machine` | `kb/items/machines/forging_press_v0.yaml` |
| 32 | `furnace_basic` | Basic furnace | `machine` | `kb/items/machines/furnace_basic.yaml` |
| 33 | `furnace_high_temp` | High temperature furnace | `machine` | `kb/items/machines/furnace_high_temp.yaml` |
| 34 | `generic_chemical_reactor_v0` | Generic chemical reactor | `machine` | `kb/items/machines/generic_chemical_reactor_v0.yaml` |
| 35 | `glass_furnace_v0` | Glass furnace v0 | `machine` | `kb/items/machines/glass_furnace_v0.yaml` |
| 36 | `gravity_separator` | Gravity separator | `machine` | `kb/items/machines/gravity_separator.yaml` |
| 37 | `grinding_wheels` | Grinding wheels | `machine` | `kb/items/machines/grinding_wheels.yaml` |
| 38 | `hand_tools_basic` | Hand tools (basic set) | `machine` | `kb/items/machines/hand_tools_basic.yaml` |
| 39 | `hand_tools_electrical` | Electrical hand tools | `machine` | `kb/items/parts/hand_tools_electrical.yaml` |
| 40 | `hand_tools_mechanical` | Mechanical hand tools | `machine` | `kb/items/machines/hand_tools_mechanical.yaml` |
| 41 | `heat_treatment_furnace_v0` | Heat treatment furnace v0 | `machine` | `kb/items/machines/heat_treatment_furnace_v0.yaml` |
| 42 | `heating_furnace` | Heating furnace (general purpose) | `machine` | `kb/items/machines/heating_furnace.yaml` |
| 43 | `heating_plate_induction_heater` | Heating plate induction heater | `machine` | `kb/items/machines/heating_plate_induction_heater.yaml` |
| 44 | `heliostat_array_system_v0` | HelioStat array system v0 | `machine` | `kb/items/machines/heliostat_array_system_v0.yaml` |
| 45 | `high_temperature_power_supply_v0` | High-temperature power supply v0 | `machine` | `kb/items/machines/high_temperature_power_supply_v0.yaml` |
| 46 | `hot_press_v0` | Hot press v0 | `machine` | `kb/items/machines/hot_press_v0.yaml` |
| 47 | `hydraulic_power_unit_basic` | Hydraulic power unit (basic) | `machine` | `kb/items/machines/hydraulic_power_unit_basic.yaml` |
| 48 | `hydraulic_press` | Hydraulic press | `machine` | `kb/items/machines/hydraulic_press.yaml` |
| 49 | `induction_forge_v0` | Induction forge | `machine` | `kb/items/machines/induction_forge_v0.yaml` |
| 50 | `inspection_tools_basic` | Inspection tools (basic) | `machine` | `kb/items/machines/inspection_tools_basic.yaml` |
| 51 | `labor_bot_general_v0` | General labor bot (automation) | `machine` | `kb/items/machines/labor_bot_general_v0.yaml` |
| 52 | `lifting_equipment` | Lifting Equipment (Hoist/Crane) | `machine` | `kb/items/machines/lifting_equipment.yaml` |
| 53 | `measurement_equipment` | Measurement equipment | `machine` | `kb/items/machines/measurement_equipment.yaml` |
| 54 | `metal_forming_basic_v0` |  | `machine` | `kb/items/machines/metal_forming_basic_v0.yaml` |
| 55 | `metal_shear_or_saw` | Metal shear or saw | `machine` | `kb/items/machines/metal_shear_or_saw.yaml` |
| 56 | `milling_machine_general_v0` | Milling machine (general) v0 | `machine` | `kb/items/machines/milling_machine_general_v0.yaml` |
| 57 | `mixer_or_blender` | Mixer or blender | `machine` | `kb/items/machines/mixer_or_blender.yaml` |
| 58 | `molding_press` | Molding press | `machine` | `kb/items/machines/molding_press.yaml` |
| 59 | `molding_press_basic` | Molding press (basic) | `machine` | `kb/items/machines/molding_press_basic.yaml` |
| 60 | `mre_reactor_v0` | MRE reactor v0 | `machine` | `kb/items/machines/mre_reactor_v0.yaml` |
| 61 | `multimeter_set` | Multimeter set | `machine` | `kb/items/machines/multimeter_set.yaml` |
| 62 | `oscilloscope_basic` | Oscilloscope (basic) | `machine` | `kb/items/machines/oscilloscope_basic.yaml` |
| 63 | `pcb_development_station` | PCB development station | `machine` | `kb/items/machines/pcb_development_station.yaml` |
| 64 | `pcb_fab_equipment` | PCB fabrication equipment | `machine` | `kb/items/machines/pcb_fab_equipment.yaml` |
| 65 | `pellet_press` | Pellet press | `machine` | `kb/items/machines/pellet_press.yaml` |
| 66 | `plastic_extruder` | Plastic extruder | `machine` | `kb/items/machines/plastic_extruder.yaml` |
| 67 | `plate_rolling_mill` | Plate rolling mill | `machine` | `kb/items/machines/plate_rolling_mill.yaml` |
| 68 | `powder_mixer` | Powder mixer | `machine` | `kb/items/machines/powder_mixer.yaml` |
| 69 | `power_conditioning_equipment` | Power conditioning equipment | `machine` | `kb/items/machines/power_conditioning_equipment.yaml` |
| 70 | `power_distribution_bus` | Power Distribution Bus | `machine` | `kb/items/machines/power_distribution_bus.yaml` |
| 71 | `power_hammer_or_press` | Power hammer or press | `machine` | `kb/items/machines/power_hammer_or_press.yaml` |
| 72 | `power_supply_benchtop` | Bench-top power supply | `machine` | `kb/items/parts/power_supply_benchtop.yaml` |
| 73 | `precision_lathe` | Precision lathe | `machine` | `kb/items/machines/precision_lathe.yaml` |
| 74 | `precision_levels` | Precision levels | `machine` | `kb/items/machines/precision_levels.yaml` |
| 75 | `precision_tooling_set` | Precision tooling set | `machine` | `kb/items/parts/precision_tooling_set.yaml` |
| 76 | `press_brake` | Press brake | `machine` | `kb/items/machines/press_brake.yaml` |
| 77 | `press_brake_die_set` | Press brake die set | `machine` | `kb/items/parts/press_brake_die_set.yaml` |
| 78 | `press_ram_set` | Press ram set | `machine` | `kb/items/parts/press_ram_set.yaml` |
| 79 | `pressing_mold_set` | Pressing mold set | `machine` | `kb/items/machines/pressing_mold_set.yaml` |
| 80 | `pyrolysis_chamber_v0` | Pyrolysis chamber v0 | `machine` | `kb/items/machines/pyrolysis_chamber_v0.yaml` |
| 81 | `quench_tank` | Quench tank | `machine` | `kb/items/machines/quench_tank.yaml` |
| 82 | `reduction_furnace_v0` | Reduction furnace | `machine` | `kb/items/machines/reduction_furnace_v0.yaml` |
| 83 | `refractory_installation_tools` | Refractory installation tools | `machine` | `kb/items/machines/refractory_installation_tools.yaml` |
| 84 | `resource_3d_printer_cartesian_v0_machine` | Cartesian 3D printer v0 | `machine` | `kb/items/machines/resource_3d_printer_cartesian_v0.yaml` |
| 85 | `rock_crusher_basic` | Rock crusher (basic) | `machine` | `kb/items/machines/rock_crusher_basic.yaml` |
| 86 | `rolling_mill_v0` | Rolling mill v0 | `machine` | `kb/items/machines/rolling_mill_v0.yaml` |
| 87 | `sand_casting_flask_set` | Sand casting flask set | `machine` | `kb/items/machines/sand_casting_flask_set.yaml` |
| 88 | `saw_or_cutting_tool` | Saw or cutting tool | `machine` | `kb/items/machines/saw_or_cutting_tool.yaml` |
| 89 | `screening_equipment` | Screening equipment | `machine` | `kb/items/machines/screening_equipment.yaml` |
| 90 | `sintering_furnace_v0` | Sintering furnace v0 | `machine` | `kb/items/machines/sintering_furnace_v0.yaml` |
| 91 | `solar_array_v0` | Solar array v0 | `machine` | `kb/items/machines/solar_array_v0.yaml` |
| 92 | `solar_tracking_optional` | Solar tracking system (optional) | `machine` | `kb/items/machines/solar_tracking_optional.yaml` |
| 93 | `soldering_station` | Soldering station | `machine` | `kb/items/machines/soldering_station.yaml` |
| 94 | `spinning_machine_v0` | Spinning machine v0 | `machine` | `kb/items/machines/spinning_machine_v0.yaml` |
| 95 | `stamping_press_basic` | Stamping press (basic) | `machine` | `kb/items/machines/stamping_press_basic.yaml` |
| 96 | `steel_forming_press` | Steel forming press | `machine` | `kb/items/machines/steel_forming_press.yaml` |
| 97 | `surface_grinder` | Surface grinder | `machine` | `kb/items/machines/surface_grinder.yaml` |
| 98 | `surface_treatment_station` | Surface treatment station | `machine` | `kb/items/machines/surface_treatment_station.yaml` |
| 99 | `temperature_sensing` | Temperature sensing equipment | `machine` | `kb/items/parts/temperature_sensing.yaml` |
| 100 | `tension_control_system` | Tension control system | `machine` | `kb/items/machines/tension_control_system.yaml` |
| 101 | `tension_gauge` | Tension gauge | `machine` | `kb/items/parts/tension_gauge.yaml` |
| 102 | `test_bench_electrical` | Electrical test bench | `machine` | `kb/items/machines/test_bench_electrical.yaml` |
| 103 | `tube_bender` | Tube bending machine | `machine` | `kb/items/machines/tube_bender.yaml` |
| 104 | `uv_exposure_unit` | UV exposure unit | `machine` | `kb/items/machines/uv_exposure_unit.yaml` |
| 105 | `vacuum_pump_small` | Vacuum pump (small) | `machine` | `kb/items/machines/vacuum_pump_small.yaml` |
| 106 | `vapor_capture_system_v0` | Vapor capture system v0 | `machine` | `kb/items/machines/vapor_capture_system_v0.yaml` |
| 107 | `vibrating_screen_v0` | Vibrating screen v0 | `machine` | `kb/items/machines/vibrating_screen_v0.yaml` |
| 108 | `vibratory_feeder_v0` | Vibratory feeder v0 | `machine` | `kb/items/machines/vibratory_feeder_v0.yaml` |
| 109 | `welding_consumables` | Welding Consumables and Filler Material Set | `machine` | `kb/items/machines/welding_consumables.yaml` |
| 110 | `welding_power_supply_v0` | Welding power supply v0 | `machine` | `kb/items/machines/welding_power_supply_v0.yaml` |
| 111 | `welding_tig_unit_v0` | TIG welding unit v0 | `machine` | `kb/items/machines/welding_tig_unit_v0.yaml` |
| 112 | `welding_tools_set` | Welding tools set | `machine` | `kb/items/machines/welding_tools_set.yaml` |
| 113 | `winding_drums` | Winding drums set | `machine` | `kb/items/parts/winding_drums.yaml` |
| 114 | `wire_crimping_tools` | Wire crimping tools | `machine` | `kb/items/machines/wire_crimping_tools.yaml` |
| 115 | `wire_drawing_die_set` | Wire drawing die set | `machine` | `kb/items/parts/wire_drawing_die_set.yaml` |
| 116 | `wire_stripper_set` | Wire stripper set | `machine` | `kb/items/machines/wire_stripper_set.yaml` |
| 117 | `work_rest_adjustable` | Work rest (adjustable) | `machine` | `kb/items/parts/work_rest_adjustable.yaml` |
