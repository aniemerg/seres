# Machine Runbook Queue (Next Gen)

Instructions for agents: use a random number generator to pick a machine without a runbook. When working this queue, first create an empty runbook file for the chosen machine to reserve it. Then start a new runbook for it, and iterate toward 50% ISRU if possible. Update the ISRU column as you go.

| Machine | Runbook | ISRU (current, per-item provenance) |
| --- | --- | --- |
| anvil_or_die_set | [runbook](anvil_or_die_set_runbook.md) | 35.7% (ISRU steel from regolith via MRE → rolling; fixed plate_rolling_mill + furnace_basic imports) |
| assembly_tools_basic | [runbook](assembly_tools_basic_runbook.md) | 84.0% (ISRU steel for frame+tools; 90% with ISRU metal for power module) |
| ball_mill_v0 | [runbook](ball_mill_v0_runbook.md) | 40.8% (ISRU: mill shell, trunnions, frame, liner, motor, gearbox, fasteners, bearings from regolith; electronics imported) |
| blast_furnace_or_smelter | [runbook](blast_furnace_or_smelter_runbook.md) | 3.5% (runbook completes; produced 570kg regolith refractory bricks + fasteners via MRE, but imported 4500kg structural_steel_sections - missing recipe to convert steel_ingot to structural sections) |
| casting_furnace_v0 | [runbook](casting_furnace_v0_runbook.md) | 49.0% (runbook completes; electronics remain imported) |
| casting_mold_set | [runbook](casting_mold_set_runbook.md) | 19.6% (ISRU steel + silica for permanent molds) |
| ceramic_press_or_mold_set | [runbook](ceramic_press_or_mold_set_runbook.md) | 100.0% (100% ISRU steel from regolith_metal_crude via MRE; simple mold for non-abrasive ceramic forming) |
| chemical_reactor_basic | [runbook](chemical_reactor_basic_runbook.md) | TBD |
| cnc_mill | [runbook](cnc_mill_runbook.md) | 6.2% (local frame + shell + gearbox + bearings; runbook completes) — needs reset removal |
| coating_station_v0 | [runbook](coating_station_v0_runbook.md) | 7.7% (ISRU steel beam + sheet metal + fasteners + spray body; enclosure mass mismatch requires extra unit) |
| coil_winding_machine | [runbook](coil_winding_machine_runbook.md) | 30.4% (ISRU machine_frame_small + wire_tensioning_mechanism (via MRE) + fasteners; MRE bug fixed) |
| crucible_refractory | [runbook](crucible_refractory_runbook.md) | 66.7% (30 kg ISRU from regolith ceramic powder; 100% Stage 2 ISRU) |
| cutting_tools_general | [runbook](cutting_tools_general_runbook.md) | 50.0% (100% ISRU steel for all components) |
| deburring_tools | [runbook](deburring_tools_runbook.md) | 50.0% (100% ISRU steel via regolith_metal_crude → steel_stock_bar_or_billet → deburring_tools) |
| dies | [runbook](dies_runbook.md) | 50.0% (100% ISRU when produced from regolith_metal_crude; pure regolith material) |
| drawing_die_set_basic | [runbook](drawing_die_set_basic_runbook.md) | 0.0% (baseline imports) |
| drying_oven | [runbook](drying_oven_runbook.md) | 0.0% (baseline imports) |
| dust_collection_system | [runbook](dust_collection_system_runbook.md) | 10.1% (regolith steel for sheet metal) |
| electrodes | [runbook](electrodes_runbook.md) | 87.5% (ISRU graphite from regolith carbon) |
| fixturing_workbench | [runbook](fixturing_workbench_runbook.md) | 60.0% |
| induction_forge_v0 | [runbook](induction_forge_v0_runbook.md) | 39.0% (regolith metal) |
| forging_press_v0 | [runbook](forging_press_v0_runbook.md) | 58.5% (900 kg regolith_metal_crude frame + 95 kg for press platens; 995 kg ISRU out of 1700 kg total) |
| furnace | [runbook](furnace_runbook.md) | 65.8% (local steel plate + regolith fasteners + local heating elements; insulation/wiring imported; fixed plate_rolling_mill import) |
| furnace_basic | [runbook](furnace_basic_runbook.md) | 50.1% |
| furnace_high_temp | [runbook](furnace_high_temp_runbook.md) | 84.4% (300kg regolith shell + 100kg regolith insulation + 150kg regolith chamber + 80kg regolith heating elements; critical for tungsten sintering) |
| generic_chemical_reactor_v0 | [runbook](generic_chemical_reactor_v0_runbook.md) | TBD |
| grinding_wheels | [runbook](grinding_wheels_runbook.md) | 93.6% (regolith-derived alumina abrasive + glass bond) |
| hand_tools_basic | [runbook](hand_tools_basic_runbook.md) | 47.8% (ISRU steel for tools+fasteners; +17% improvement) |
| hand_tools_mechanical | [runbook](hand_tools_mechanical_runbook.md) | 0% (baseline complete; produced 22.8kg regolith_metal_crude but recipe needs material substitution to use) |
| heat_treatment_furnace_v0 | [runbook](heat_treatment_furnace_runbook.md) | 54.1% (local quench_rack_and_baskets + furnace_shell_insulated; imported silica + insulation blanket) |
| heat_treatment_furnace_v0 | [runbook](heat_treatment_furnace_v0_runbook.md) | 54.1% (ISRU furnace_shell_insulated + quench_rack_and_baskets; electronics/heaters imported) |
| heating_furnace | [runbook](heating_furnace_runbook.md) | 37.1% (ISRU steel plate for shell; remaining components imported) |
| high_temperature_power_supply_v0 | [runbook](high_temperature_power_supply_v0_runbook.md) | 25.7% |
| hot_press_v0 | [runbook](hot_press_v0_runbook.md) | 86.0% (runbook completes; ISRU steel frame, hydraulics, platens, heaters, insulation; fixed heating_element_set_high_temp mass from 80kg to 74.5kg to match recipe output) |
| hydraulic_press | [runbook](hydraulic_press_runbook.md) | 40.8% (ISRU steel frame + fasteners; hydraulics/electronics imported) |
| inert_atmosphere_system | [runbook](inert_atmosphere_system_runbook.md) | 23.1% (ISRU gas regulators + piping + enclosure via regolith metal) |
| inspection_tools_basic | [runbook](inspection_tools_basic_runbook.md) | 0.0% (KB gaps: missing steel form conversion recipes; demonstrates regolith → steel chain but can't use in final assembly) |
| kiln_ceramic | [runbook](kiln_ceramic_runbook.md) | 4.2% (ISRU alumina + refractory_castable; binder/water/electricals imported) |
| labor_bot_general_v0 | [runbook](labor_bot_general_v0_runbook.md) | 34.8% (ISRU regolith metals + aluminum wire; electronics, sensors, reducers imported) |
| lifting_equipment | [runbook](lifting_equipment_runbook.md) | 37.9% (ISRU steel for structural_frame_large + fasteners; runbook completes) |
| metal_shear_or_saw | [runbook](metal_shear_or_saw_runbook.md) | 20.5% (regolith steel for I-beam) |
| milling_machine_general_v0 | [runbook](milling_machine_general_v0_runbook.md) | 18.7% (local motor + steel chain) |
| molding_press_basic | [runbook](molding_press_basic_runbook.md) | 43.2% (KB gaps: dependent step failures prevent steel_stock completion; 90% target with fixes) |
| mre_reactor_v0 | [runbook](mre_reactor_v0_runbook.md) | 8.9% (reactor_vessel_mre 650kg + power_bus 55kg from regolith_metal_crude; 99% potential with full component production) |
| plate_rolling_mill | [runbook](plate_rolling_mill_runbook.md) | 71.6% (ISRU frame + machined parts; rolls/hydraulics/electronics/fasteners still imported) |
| powder_mixer | [runbook](powder_mixer_runbook.md) | 91.3% (ISRU frame, drum, agitator, motor housing; imported electronics/hardware) |
| power_hammer_or_press | [runbook](power_hammer_or_press_runbook.md) | TBD (runbook completes; built via sim.build-machine so provenance not recorded) |
| precision_lathe | [runbook](precision_lathe_runbook.md) | 46.6% (local bed + spindle assembly + leadscrew/coolant + motor_electric_medium + motor/drive frame/belt + steel_bar_raw; still imports power_electronics_module, control_panel_basic, sealed bearings, cooling_fan_assembly, seals/grease) |
| press_brake | [runbook](press_brake_runbook.md) | 42.7% (Fixed: increased steel_stock from 500→510 kg for fastener consumption; ISRU steel for frame+parts; electronics/hydraulics imported) |
| press_brake | [runbook](press_brake_runbook.md) | 100.0% |
| press_ram_set | [runbook](press_ram_set_runbook.md) | 50.0% (100% ISRU when produced from regolith_metal_crude; pure regolith material) |
| pressing_mold_set | [runbook](pressing_mold_set_runbook.md) | WIP |
| reduction_furnace_v0 | [runbook](reduction_furnace_v0_runbook.md) | 52.4% (regolith metal, optimized) |
| rock_crusher_basic | [runbook](rock_crusher_basic_runbook.md) | 80.0% |
| rolling_mill_v0 | [runbook](rolling_mill_v0_runbook.md) | 0.5% (bearings use regolith_metal_crude but need imported steel_bar_stock; complex steel processing for other components) |
| saw_or_cutting_tool | [runbook](saw_or_cutting_tool_runbook.md) | 86.0% (100% ISRU steel for frame, blade, and fasteners) |
| screening_equipment | [runbook](screening_equipment_runbook.md) | 82.4% (ISRU steel plate + mesh; motor/wiring/fasteners imported) |
| sintering_furnace_v0 | [runbook](sintering_furnace_v0_runbook.md) | 11.2% (ISRU regolith-based insulation pack; shell/elements/electronics imported) |
| stamping_press_basic | [runbook](stamping_press_basic_runbook.md) | 0.0% (ISRU subcomponents added; provenance shows 1 kg machine mass) |
| steel_forming_press | [runbook](steel_forming_press_runbook.md) | 56.7% (ISRU press frame + platens from regolith metal) |
| surface_grinder | [runbook](surface_grinder_runbook.md) | 1.9% (Fixed recipe bugs - removed redundant steps 1-2, fixed step 5 inputs, corrected grinding_spindle_assembly + table_drive_assembly unit outputs) |
| surface_treatment_station | [runbook](surface_treatment_station_runbook.md) | 40.2% (ISRU regolith_metal_crude → steel_plate_or_sheet + support_frame_welded + agitation_system_basic; other subsystems imported) |
| test_bench_electrical | [runbook](test_bench_electrical_runbook.md) | 90.3% (local regolith -> steel for frame+mounts; imports for power/cooling/fasteners) |
| vibrating_screen_v0 | [runbook](vibrating_screen_v0_runbook.md) | 6.3% (regolith steel for frame+screen) |
| welding_consumables | [runbook](welding_consumables_runbook.md) | 80.8% (local aluminum wire + enclosure + steel rods; carbon reductant ISRU) |
| welding_power_supply_v0 | [runbook](welding_power_supply_v0_runbook.md) | 6.5% |
| welding_tools_set | [runbook](welding_tools_set_runbook.md) | 93.3% (ISRU steel chain; 1 kg textile_fabric import for gloves/helmet padding) |
| winding_drums | [runbook](winding_drums_runbook.md) | 100.0% (ISRU steel bar stock from regolith metal) |
| wire_drawing_die_set | [runbook](wire_drawing_die_set_runbook.md) | 3.7% (runbook completes; provenance: 3.7% overall ISRU) |
