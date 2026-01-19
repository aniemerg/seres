# Machine Runbook Queue (Sequential Simulation)

Instructions for agents: use a random number generator to pick a machine without a runbook. When working this queue, first create an empty runbook file for the chosen machine to reserve it. Then start a new runbook for it, and iterate toward 50% ISRU if possible. Update the ISRU column as you go. This queue reflects machines reserved during the sequential simulation.

| Machine | Runbook | ISRU (current, per-item provenance) |
| --- | --- | --- |
| alignment_tools | [runbook](alignment_tools_runbook.md) | TBD |
| assembly_station | [runbook](assembly_station_runbook.md) | TBD |
| assembly_tools_basic | [runbook](assembly_tools_basic_runbook.md) | TBD |
| balancing_machine | [runbook](balancing_machine_runbook.md) | ~45% (estimated; frame+fasteners from regolith, provenance tracking issue shows 0%) |
| ball_mill_v0 | [runbook](ball_mill_v0_runbook.md) | TBD |
| blast_furnace_or_smelter | [runbook](blast_furnace_or_smelter_runbook.md) | TBD |
| casting_furnace_v0 | [runbook](casting_furnace_v0_runbook.md) | TBD |
| casting_mold_set | [runbook](casting_mold_set_runbook.md) | TBD |
| ceramic_press_or_mold_set | [runbook](ceramic_press_or_mold_set_runbook.md) | TBD |
| chemical_reactor_basic | [runbook](chemical_reactor_basic_runbook.md) | TBD |
| cnc_mill | [runbook](cnc_mill_runbook.md) | TBD |
| coil_winding_machine | [runbook](coil_winding_machine_runbook.md) | TBD |
| controlled_atmosphere_chamber | [runbook](controlled_atmosphere_chamber_runbook.md) | 18.7% (ISRU chamber shell via regolith metal → sheet metal; runbook completes) |
| coordinate_measuring_machine | [runbook](coordinate_measuring_machine_runbook.md) | 89.7% (400 kg granite base from regolith) |
| crucible_refractory | [runbook](crucible_refractory_runbook.md) | TBD |
| cutting_tools_general | [runbook](cutting_tools_general_runbook.md) | TBD |
| drawing_die_set_basic | [runbook](drawing_die_set_basic_runbook.md) | TBD |
| drill_press | [runbook](drill_press_runbook.md) | 0% (ISRU machine_column_cast produced, but per-item provenance shows 0%) |
| drying_oven | [runbook](drying_oven_runbook.md) | TBD |
| dust_collection_system | [runbook](dust_collection_system_runbook.md) | TBD |
| electrodes | [runbook](electrodes_runbook.md) | TBD |
| electrolysis_cell_unit_v0 | [runbook](electrolysis_cell_unit_v0_runbook.md) | TBD |
| fixturing_workbench | [runbook](fixturing_workbench_runbook.md) | TBD |
| forging_press_v0 | [runbook](forging_press_v0_runbook.md) | TBD |
| furnace | [runbook](furnace_runbook.md) | TBD |
| furnace_basic | [runbook](furnace_basic_runbook.md) | TBD |
| furnace_high_temp | [runbook](furnace_high_temp_runbook.md) | TBD |
| generic_chemical_reactor_v0 | [runbook](generic_chemical_reactor_v0_runbook.md) | TBD |
| glass_furnace_v0 | [runbook](glass_furnace_v0_runbook.md) | 78.8% |
| grinding_wheels | [runbook](grinding_wheels_runbook.md) | TBD |
| hand_tools_basic | [runbook](hand_tools_basic_runbook.md) | TBD |
| hand_tools_mechanical | [runbook](hand_tools_mechanical_runbook.md) | TBD |
| heat_treatment_furnace_v0 | [runbook](heat_treatment_furnace_v0_runbook.md) | TBD |
| heating_furnace | [runbook](heating_furnace_runbook.md) | TBD |
| high_temperature_power_supply_v0 | [runbook](high_temperature_power_supply_v0_runbook.md) | TBD |
| hot_press_v0 | [runbook](hot_press_v0_runbook.md) | TBD |
| hydraulic_assembly_tools | [runbook](hydraulic_assembly_tools_runbook.md) | ~7% (estimated; machined parts from regolith, provenance tracking issue shows 0%) |
| hydraulic_press | [runbook](hydraulic_press_runbook.md) | TBD |
| inspection_tools_basic | — | TBD |
| kiln_ceramic | [runbook](kiln_ceramic_runbook.md) | TBD |
| labor_bot_general_v0 | [runbook](labor_bot_general_v0_runbook.md) | TBD |
| lathe_engine_v0 | [runbook](lathe_engine_v0_runbook.md) | TBD |
| lifting_equipment | [runbook](lifting_equipment_runbook.md) | TBD |
| measurement_equipment | [runbook](measurement_equipment_runbook.md) | TBD |
| metal_shear_or_saw | [runbook](metal_shear_or_saw_runbook.md) | TBD |
| milling_machine_general_v0 | [runbook](milling_machine_general_v0_runbook.md) | TBD |
| mixer_or_blender | [runbook](mixer_or_blender_runbook.md) | 36.7% (ISRU steel sheet for drum, ISRU steel bar for agitator/frame, ISRU fasteners) |
| molding_press_basic | [runbook](molding_press_basic_runbook.md) | 43.2% (ISRU steel_stock for frame and fasteners from regolith; KB gaps prevented full steel form conversion) |
| mre_reactor_v0 | [runbook](mre_reactor_v0_runbook.md) | TBD |
| plate_rolling_mill | [runbook](plate_rolling_mill_runbook.md) | ISRU 35.8% |
| powder_mixer | [runbook](powder_mixer_runbook.md) | TBD |
| power_distribution_bus | [runbook](power_distribution_bus_runbook.md) | TBD |
| power_hammer_or_press | [runbook](power_hammer_or_press_runbook.md) | TBD |
| precision_lathe | [runbook](precision_lathe_runbook.md) | TBD |
| precision_levels | [runbook](precision_levels_runbook.md) | 14.2% (local alumina-derived aluminum; cutting fluid, carbon anode, cryolite, acid imported) |
| press_brake | [runbook](press_brake_runbook.md) | TBD |
| pressing_mold_set | [runbook](pressing_mold_set_runbook.md) | TBD |
| pyrolysis_chamber_v0 | [runbook](pyrolysis_chamber_v0_runbook.md) | TBD |
| quench_tank | [runbook](quench_tank_runbook.md) | KB issues prevent completion (recipe uses bulk_material_or_parts placeholder, assembly not completing) |
| reduction_furnace_v0 | [runbook](reduction_furnace_v0_runbook.md) | TBD |
| refractory_installation_tools | [runbook](refractory_installation_tools_runbook.md) | TBD |
| rock_crusher_basic | [runbook](rock_crusher_basic_runbook.md) | TBD |
| rolling_mill_v0 | [runbook](rolling_mill_v0_runbook.md) | TBD |
| saw_or_cutting_tool | [runbook](saw_or_cutting_tool_runbook.md) | TBD |
| screening_equipment | [runbook](screening_equipment_runbook.md) | TBD |
| sintering_furnace_v0 | [runbook](sintering_furnace_v0_runbook.md) | TBD |
| soldering_station | [runbook](soldering_station_runbook.md) | TBD |
| stamping_press_basic | [runbook](stamping_press_basic_runbook.md) | TBD |
| surface_grinder | [runbook](surface_grinder_runbook.md) | TBD |
| surface_treatment_station | [runbook](surface_treatment_station_runbook.md) | TBD |
| test_bench_electrical | [runbook](test_bench_electrical_runbook.md) | TBD |
| vibrating_screen_v0 | [runbook](vibrating_screen_v0_runbook.md) | TBD |
| welding_consumables | [runbook](welding_consumables_runbook.md) | TBD |
| welding_power_supply_v0 | [runbook](welding_power_supply_v0_runbook.md) | TBD |
| welding_tools_set | [runbook](welding_tools_set_runbook.md) | TBD |
| wire_crimping_tools | [runbook](wire_crimping_tools_runbook.md) | TBD |
