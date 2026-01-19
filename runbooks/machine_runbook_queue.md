# Machine Runbook Queue

Instructions for agents: use a random number generator to pick a machine without a runbook. When working this queue, first create an empty runbook file for the chosen machine to reserve it. Then start a new runbook for it, and iterate toward 50% ISRU if possible. Update the ISRU column as you go.

| Machine | Runbook | ISRU (current, per-item provenance) |
| --- | --- | --- |
| alignment_tools | [runbook](alignment_tools_runbook.md) | 44.3% (ISRU steel for tools+fasteners; +11.5% improvement) |
| anvil_or_die_set | [runbook](anvil_or_die_set_runbook.md) | 35.7% (regolith steel stock for forging) |
| assembly_station | [runbook](assembly_station_runbook.md) | 27.8% |
| assembly_tools_basic | [runbook](assembly_tools_basic_runbook.md) | 84.0% (ISRU steel for frame+tools; 90% with ISRU metal for power module) |
| ball_mill_v0 | [runbook](ball_mill_v0_runbook.md) | TBD |
| casting_furnace_v0 | [runbook](casting_furnace_v0_runbook.md) | TBD |
| casting_mold_set | [runbook](casting_mold_set_runbook.md) | 0% baseline; ~46% estimated ISRU (regolith steel plate + MRE metal) |
| chemical_reactor_basic | [runbook](chemical_reactor_basic_runbook.md) | TBD |
| coil_winding_machine | — | TBD |
| crucible_refractory | [runbook](crucible_refractory_runbook.md) | TBD |
| cutting_tools_general | [runbook](cutting_tools_general_runbook.md) | 50.0% (100% ISRU steel for all components) |
| drilling_equipment_v0 | [runbook](drilling_equipment_v0_runbook.md) | 13.7% (regolith steel for frame+drill string) |
| dust_collection_system | [runbook](dust_collection_system_runbook.md) | 10.1% (regolith steel for sheet metal) |
| electrodes | [runbook](electrodes_runbook.md) | 87.5% (ISRU graphite from regolith carbon) |
| electrolysis_cell_unit_v0 | [runbook](electrolysis_cell_unit_v0_runbook.md) | TBD |
| fixturing_workbench | [runbook](fixturing_workbench_runbook.md) | 60.0% |
| induction_forge_v0 | [runbook](induction_forge_v0_runbook.md) | 39.0% (regolith metal) |
| generic_chemical_reactor_v0 | [runbook](generic_chemical_reactor_v0_runbook.md) | TBD |
| grinding_wheels | [runbook](grinding_wheels_runbook.md) | 93.6% (regolith-derived alumina abrasive + glass bond) |
| hand_tools_basic | [runbook](hand_tools_basic_runbook.md) | 47.8% (ISRU steel for tools+fasteners; +17% improvement) |
| heliostat_array_system_v0 | — | TBD |
| high_temperature_power_supply_v0 | [runbook](high_temperature_power_supply_v0_runbook.md) | 25.7% |
| labor_bot_general_v0 | [runbook](labor_bot_general_v0_runbook.md) | TBD |
| measurement_equipment | [runbook](measurement_equipment_runbook.md) | 3.7% |
| metal_shear_or_saw | [runbook](metal_shear_or_saw_runbook.md) | 20.5% (regolith steel for I-beam) |
| milling_machine_general_v0 | [runbook](milling_machine_general_v0_runbook.md) | 18.7% (local motor + steel chain) |
| mre_reactor_v0 | [runbook](mre_reactor_v0_runbook.md) | 8.9% (reactor_vessel_mre 650kg + power_bus 55kg from regolith_metal_crude; 99% potential with full component production) |
| power_hammer_or_press | [runbook](power_hammer_or_press_runbook.md) | TBD |
| press_brake | [runbook](press_brake_runbook.md) | 42.7% |
| press_brake | [runbook](press_brake_runbook.md) | 100.0% |
| reduction_furnace_v0 | [runbook](reduction_furnace_v0_runbook.md) | 52.4% (regolith metal, optimized) |
| rock_crusher_basic | [runbook](rock_crusher_basic_runbook.md) | 80.0% |
| rolling_mill_v0 | [runbook](rolling_mill_v0_runbook.md) | 0.5% (bearings use regolith_metal_crude but need imported steel_bar_stock; complex steel processing for other components) |
| saw_or_cutting_tool | [runbook](saw_or_cutting_tool_runbook.md) | 86.0% (100% ISRU steel for frame, blade, and fasteners) |
| soldering_station | [runbook](soldering_station_runbook.md) | TBD |
| stamping_press_basic | [runbook](stamping_press_basic_runbook.md) | TBD |
| surface_grinder | [runbook](surface_grinder_runbook.md) | BLOCKED (recipe bug: step 5 expects machine_base_large but steps 3-4 output assembled_equipment) |
| test_bench_electrical | [runbook](test_bench_electrical_runbook.md) | 90.3% (local regolith -> steel for frame+mounts; imports for power/cooling/fasteners) |
| vibrating_screen_v0 | [runbook](vibrating_screen_v0_runbook.md) | 6.3% (regolith steel for frame+screen) |
| welding_consumables | [runbook](welding_consumables_runbook.md) | 80.8% (local aluminum wire + enclosure + steel rods; carbon reductant ISRU) |
| welding_power_supply_v0 | [runbook](welding_power_supply_v0_runbook.md) | 43.1% |
| wire_crimping_tools | [runbook](wire_crimping_tools_runbook.md) | 92.4% (100% ISRU regolith_metal_crude for crimping dies and frames) |
| wire_drawing_die_set | [runbook](wire_drawing_die_set_runbook.md) | 3.8% |
