# multi_machine_plan SimPlan Runbook

Generated from a SimPlan.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: simplan_minimal_self_repro
- cmd: sim.reset
  args:
    sim-id: simplan_minimal_self_repro
- cmd: sim.note
  args:
    style: milestone
    message: Simulation reset. Starting combined build.
- cmd: sim.import
  args:
    item: agitation_pump_small
    quantity: 30.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: agitation_system_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: air_bearing_assembly
    quantity: 6.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: air_compressor_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: air_manifold_and_nozzles
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: alignment_tools
    quantity: 5.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: aluminum_ingot
    quantity: 15.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: aluminum_wire
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: anvil_block_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: anvil_or_die_set
    quantity: 33.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: assembled_cable_harness
    quantity: 7.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: assembled_electrical_equipment
    quantity: 465.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: assembled_electronics
    quantity: 8.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: assembled_equipment
    quantity: 50.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: assembly_station
    quantity: 15.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: assembly_tools_basic
    quantity: 291.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: atmosphere_sensors_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: balancing_machine
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: ball_mill_v0
    quantity: 125.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: ball_screw_assembly
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: base_grease_stock_v0
    quantity: 5.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: basic_fabrication_station
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: basic_fabrication_station_v0
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: battery_backup_small
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_heavy
    quantity: 5.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bearing_set_sealed
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: belt_and_pulley_set
    quantity: 3.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: bending_machine_v0
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: biocide_additive
    quantity: 1.7000000000000002
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: blast_furnace_or_smelter
    quantity: 278.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: bulk_material_or_parts
    quantity: 628.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: burner_or_heater_casting
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: bus_bar_copper
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cable_drag_chain
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: calibration_artifacts
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: caliper_set_precision
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: capacitor_bank_power
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: carbon_dioxide_gas
    quantity: 79.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_monoxide
    quantity: 125.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_reducing_agent
    quantity: 367.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: carbon_reductant
    quantity: 397.21999999999997
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: casting_furnace_v0
    quantity: 526.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: casting_mold_set
    quantity: 433.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: casting_patterns_wooden
    quantity: 5.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cellulose_raw
    quantity: 310.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cement_mixer_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: center_insulator_ceramic
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: ceramic_fiber_bulk
    quantity: 19.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: ceramic_fiber_raw
    quantity: 468.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: chemical_bath_agitation_system
    quantity: 25.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: chemical_bath_heaters
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: chemical_bath_station
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: chemical_bath_ventilation
    quantity: 6.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_basic
    quantity: 56.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: chemical_reactor_vessel_v0
    quantity: 32.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: chemical_separation_equipment
    quantity: 352.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: chlorine_gas
    quantity: 98.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: chromium_metal_pure
    quantity: 6.7
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: circulation_pump_coolant
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cnc_mill
    quantity: 16.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: coil_insulation_material
    quantity: 0.05
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: coil_winding_machine
    quantity: 17.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: cold_trap_module_v0
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: collection_hopper_drum
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: computer_core_imported
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_circuit_board_basic
    quantity: 8.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_circuit_board_power
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_components
    quantity: 4.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_compute_module_imported
    quantity: 52.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_assembly_v0
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: control_panel_basic
    quantity: 16.4
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: controlled_atmosphere_chamber
    quantity: 5.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: coolant_loop_basic
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: coolant_system_basic
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cooling_fan_and_ducting
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cooling_loop_basic
    quantity: 7.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: coordinate_measuring_machine
    quantity: 7.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: cope_and_drag_boards
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: copper_rod_ingot
    quantity: 52.58
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: copper_wire_magnet
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: corrosion_inhibitor
    quantity: 2.55
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: crucible_graphite
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: crucible_refractory
    quantity: 414.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: cut_parts
    quantity: 410.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cutting_fluid
    quantity: 10.4
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: cutting_tool_set_basic
    quantity: 6.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: cutting_tools_general
    quantity: 278.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: depth_stop_mechanism
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: dial_indicator_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: dies
    quantity: 8.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: display_screen_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: door_hinge_assembly
    quantity: 1.0
    unit: each
    ensure: true
- cmd: sim.import
  args:
    item: draft_roller_set
    quantity: 25.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: drawing_die_set_basic
    quantity: 8.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: drill_bit_carbide
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: drill_press
    quantity: 15.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: drill_string_steel
    quantity: 100.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: drilling_equipment_v0
    quantity: 110.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_medium
    quantity: 9.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drive_motor_small
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: drying_basic_v0
    quantity: 5.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: drying_oven
    quantity: 16.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: ductwork_and_fittings
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: dust_collection_system
    quantity: 245.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: electric_parallel_gripper
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wire_and_connectors
    quantity: 117.9
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrical_wiring_kit
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: electrode_set_mre
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: electrodes
    quantity: 113.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: electrolysis_cell_unit_v0
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: electronic_components_set
    quantity: 48.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: emulsifying_oil
    quantity: 8.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: enclosure_electrical_medium
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: enclosure_small
    quantity: 2.16
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: epoxy_monomer_v0
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: epoxy_processing_unit
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: epoxy_synthesis_unit
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: equipment_imported
    quantity: 3.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: etching_chemicals
    quantity: 0.4
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: excavator_basic
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: extruder_head_basic
    quantity: 16.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_heavy
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_large
    quantity: 4.5
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_medium
    quantity: 53.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fastener_kit_small
    quantity: 7.607692307692307
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fiber_drawing_tower
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: filler_wire_basic
    quantity: 117.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: filter_cartridges_dust
    quantity: 5.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: filtration_unit
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: finished_part
    quantity: 48.25
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: finished_part_deburred
    quantity: 46.8
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fittings_and_valves
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fixture_mounting_plate_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: fixturing_workbench
    quantity: 73.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: flier_and_bobbin_set
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: fluorite
    quantity: 3.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: force_torque_sensor_6axis
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: forging_press_v0
    quantity: 19.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: frame_and_supports_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: furnace_basic
    quantity: 455.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: furnace_door_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: furnace_high_temp
    quantity: 21.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: gantry_axes_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_cylinder_argon_or_nitrogen
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_flow_controller
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gas_handling_system
    quantity: 140.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: gas_inlet_manifold
    quantity: 3.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: gas_supply_regulator
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gauge_block_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gearbox_reducer_medium
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: gearbox_reducer_small
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: generic_chemical_reactor_v0
    quantity: 77.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: glass_furnace_v0
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: glass_to_metal_seal_v0
    quantity: 0.75
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: graphite_powder
    quantity: 24.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: gravity_separator
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: grinder_cylindrical_v0
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: grinding_media_steel
    quantity: 50.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: grinding_spindle_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: grinding_wheels
    quantity: 33.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: ground_clamp_and_cables
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_basic
    quantity: 54.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_electrical
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: hand_tools_mechanical
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: harmonic_drive_reducer_medium
    quantity: 6.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: heat_exchanger_compact
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_transport_loop_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heat_treatment_furnace_v0
    quantity: 40.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: heated_platen_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_electric
    quantity: 4.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_industrial
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_resistive
    quantity: 12.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_basic
    quantity: 240.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: heating_element_set_high_temp
    quantity: 6.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heating_elements_basic
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: heating_furnace
    quantity: 118.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: heating_plate_induction_heater
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: heliostat_array_system_v0
    quantity: 226.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: heliostat_control_electronics_v0
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heliostat_mirror_panel_v0
    quantity: 6.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: heliostat_mounting_bracket_v0
    quantity: 4.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: high_temperature_power_supply_v0
    quantity: 395.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: hopper_feed_steel
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hot_press_v0
    quantity: 8.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_control_valve_set
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_cylinder_industrial
    quantity: 4.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_cylinder_large
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_cylinder_press
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_power_unit_basic
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_press
    quantity: 45.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_pump_basic
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_pump_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydraulic_system_medium
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: hydrochloric_acid
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: hydrogen_gas
    quantity: 19.874999999999996
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: import_misc_components_set
    quantity: 75.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: induction_forge_v0
    quantity: 42.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: inert_gas_manifold
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: inspection_tools_basic
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: instrument_mounts_basic
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: insulation_ceramic
    quantity: 50.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_material
    quantity: 17.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_pack_high_temp
    quantity: 5.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: insulation_panel_high_temp
    quantity: 130.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: insulation_thermal_blanket
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: inverter_module_imported
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: iron_metal_pure
    quantity: 800.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: iron_ore_or_ilmenite
    quantity: 164.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: iron_pig_or_ingot
    quantity: 22.05
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: kiln_ceramic
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: lab_v0
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 4830.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: lamination_stack_clamped
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_bed_simple
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_carriage_simple
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_headstock_simple
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_leadscrew_and_feed_system
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_leadscrew_simple
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_motor_and_drive
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_spindle_and_bearings
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: lathe_tool_post_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: leak_test_equipment
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: led_ring_light
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: level_sensor_basic
    quantity: 15.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: lifting_equipment
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: linear_encoder_set
    quantity: 9.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: linear_guide_rails
    quantity: 7.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: linear_stage_xyz_precision
    quantity: 6.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: machine_frame_heavy
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: machine_frame_small
    quantity: 48.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: machined_part_raw
    quantity: 203.25
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: machined_steel_part_precision
    quantity: 335.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: magnet_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: magnetic_chuck_surface_grinder
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: magnetic_separator_drum_v0
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: manual_labour
    quantity: 11.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: measurement_equipment
    quantity: 7.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: metal_feedstock
    quantity: 965.8
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: metal_forming_basic_v0
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: metal_shear_or_saw
    quantity: 29.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: methane_gas
    quantity: 30.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: methanol_liquid
    quantity: 21.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: micrometer_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: milling_machine_general_v0
    quantity: 227.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: milling_table
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mixer_agitator_shaft_and_paddles
    quantity: 2.25
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mixer_control_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mixer_frame_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mixer_motor_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mixer_or_blender
    quantity: 13.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: mixing_tank_medium
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: molding_control_unit
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: molding_press
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: molding_press_basic
    quantity: 11.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: molding_press_cylinder
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: molding_press_platen_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: monochloroacetic_acid
    quantity: 124.00000000000003
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: mos2_precursor_v0
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: motor_assembly
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: motor_electric_medium
    quantity: 7.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_electric_small
    quantity: 58.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: motor_general_5kw
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: motor_housing_cast
    quantity: 6.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: mounting_bracket_steel
    quantity: 8.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: mounting_fixtures_adjustable
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: mre_reactor_v0
    quantity: 113.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: multimeter_set
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: nickel_chromium_alloy
    quantity: 0.3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: offgas_manifold
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: oscilloscope_basic
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: oxygen_gas
    quantity: 48.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: pcb_development_station
    quantity: 200.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: pcb_etching_tank_set
    quantity: 40.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: pcb_fab_equipment
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: pcb_tinning_plating_bath
    quantity: 25.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: pellet_press
    quantity: 26.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: pelletizer_v0
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: permanent_magnet_array
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: piping_and_fittings_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: piping_and_valves_set
    quantity: 8.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: piping_assembly_small
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: piping_components
    quantity: 11.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: plastic_extruder
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: plate_rolling_mill
    quantity: 155.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: plumbing_system_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: polymer_printing_feedstock
    quantity: 5.45
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: position_sensor_set
    quantity: 0.5
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: powder_mixer
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: power_bus_high_current
    quantity: 200.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_cable_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_equipment
    quantity: 7.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: power_conditioning_module
    quantity: 206.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_distribution_board
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: power_distribution_bus
    quantity: 92.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: power_electronics_module
    quantity: 7.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_hammer_or_press
    quantity: 33.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: power_output_terminals
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: power_strip_and_protection
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_benchtop
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_components_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_low_voltage
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: power_supply_small_imported
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: precision_lathe
    quantity: 16.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: precision_levels
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: precision_tooling_set
    quantity: 7.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: press_brake
    quantity: 46.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: press_brake_die_set
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_frame_medium
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_platen_set_medium
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: press_ram_set
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: pressing_mold_set
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: pressure_gauge_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: pressure_test_gauge_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: printer_control_module
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: printer_frame_generic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: protective_cover_set
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: proximity_sensor_inductive
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: pv_module_imported
    quantity: 8.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: pyrolysis_chamber_v0
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: quench_rack_and_baskets
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: quench_tank
    quantity: 8.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: quick_change_tool_interface
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: reduction_furnace_v0
    quantity: 282.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: refractory_castable
    quantity: 400.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: refractory_installation_tools
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: refractory_lining_set
    quantity: 1.0
    unit: each
    ensure: true
- cmd: sim.import
  args:
    item: refractory_trowel_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: regolith_carbonaceous
    quantity: 13960.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: regolith_lunar_highlands
    quantity: 257.06
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: regolith_lunar_mare
    quantity: 922.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: regolith_polar_psc
    quantity: 268.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: relay_electromagnetic_v0
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: resource_3d_printer_cartesian_v0_machine
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: robot_arm_link_aluminum
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: robot_wrist_3axis
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: rock_crusher_basic
    quantity: 118.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: roller_set_forming
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: rolling_mill_rolls_set
    quantity: 1.0
    unit: set
    ensure: true
- cmd: sim.import
  args:
    item: rolling_mill_v0
    quantity: 161.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: rough_part
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: safety_controller_plc
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: safety_guard_steel_mesh
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: safety_light_curtain
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: salt_waste
    quantity: 29580.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: sand_casting_flask_set
    quantity: 5.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: saw_or_cutting_tool
    quantity: 51.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: screening_equipment
    quantity: 10.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: screening_equipment_v0
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: seal_mechanical_rotary
    quantity: 0.2
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: seal_rubber_o_ring
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: sensor_suite_general
    quantity: 138.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: servo_drive_controller
    quantity: 6.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: shaft_and_bearing_set
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: sheet_metal_or_structural_steel
    quantity: 3211.55
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: silicon_metal_v0
    quantity: 3.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: sintering_furnace_v0
    quantity: 8.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: sodium_chloride
    quantity: 50.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: solar_array_v0
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: solar_irradiance
    quantity: 100.0
    unit: kWh
    ensure: true
- cmd: sim.import
  args:
    item: solar_tracking_optional
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: soldering_station
    quantity: 14.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: spindle_assembly_spinning
    quantity: 30.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: spindle_drive_motor_small
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: spindle_head_basic
    quantity: 80.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: spinning_drive_motor
    quantity: 40.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: spinning_frame_basic
    quantity: 120.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: spinning_machine_v0
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: spring_compression_small
    quantity: 0.01
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: stamping_press_basic
    quantity: 10.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: steel_bar_stock
    quantity: 3.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_beam_i_section
    quantity: 2215.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_drum
    quantity: 20.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_forming_press
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: steel_frame_welded
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_mesh_sheet_material
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_plate_or_sheet
    quantity: 198.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_sheet_22ga
    quantity: 1.3
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: steel_sheet_3mm
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_shell_thick
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: steel_stock
    quantity: 547.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: stepper_motor_precision
    quantity: 12.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: structural_steel_frame
    quantity: 1900.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: structural_steel_sections
    quantity: 4500.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: support_frame_small
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: support_frame_welded
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: surface_grinder
    quantity: 49.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: surface_treatment_station
    quantity: 4.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: table_drive_assembly
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tailstock_assembly
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tank_lid_and_basket
    quantity: 40.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_basic
    quantity: 96.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: temperature_controller_module
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: temperature_sensing
    quantity: 6.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tension_control_system
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: tension_gauge
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: test_bench_electrical
    quantity: 19.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: test_equipment_basic
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: textile_fabric
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: thermal_controller_basic
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: thermal_management_system
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: tip_holder_and_stand
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tool_set_general
    quantity: 40.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: torch_assembly
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: touch_probe_assembly
    quantity: 2.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: touch_sensor_capacitive
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: tracking_control_unit
    quantity: 8.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: tracking_drive_assembly
    quantity: 40.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: trunnion_supports
    quantity: 6.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: tube_bender
    quantity: 2.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: turn_counter_module
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: turning_tools_general
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: unfinished_part
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: uv_exposure_unit
    quantity: 100.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: vacuum_blower_industrial
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vacuum_pump_small
    quantity: 2.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: valve_ball_stainless
    quantity: 1.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: vapor_capture_system_v0
    quantity: 120.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: vibrating_screen_v0
    quantity: 133.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: vibration_drive_module
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibration_motor_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibration_sensor_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: vibrator_motor_small
    quantity: 15.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: vibratory_feeder_v0
    quantity: 3.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: voltage_regulator_module
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: water
    quantity: 48.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: welded_fabrications
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: welding_consumables
    quantity: 62.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: welding_power_supply_unit
    quantity: 65.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: welding_power_supply_v0
    quantity: 79.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: welding_rod_steel
    quantity: 10.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: welding_tig_unit_v0
    quantity: 3.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: welding_tools_set
    quantity: 23.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: winding_drums
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: wire_brush_set
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wire_crimping_tools
    quantity: 14.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: wire_drawing_die_set
    quantity: 16.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: wire_stripper_set
    quantity: 11.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: wire_tensioning_mechanism
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.import
  args:
    item: wood_or_composite_material
    quantity: 5.0
    unit: kg
    ensure: true
- cmd: sim.import
  args:
    item: work_rest_adjustable
    quantity: 1.0
    unit: count
    ensure: true
- cmd: sim.import
  args:
    item: worm_gear_set_v0
    quantity: 1.0
    unit: unit
    ensure: true
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for alignment_tools
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for anvil_or_die_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for assembly_station
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for assembly_tools_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for balancing_machine
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for ball_mill_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for basic_fabrication_station
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for basic_fabrication_station_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for bending_machine_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for blast_furnace_or_smelter
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for casting_furnace_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for casting_mold_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for chemical_bath_station
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for chemical_reactor_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for chemical_reactor_vessel_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for chemical_separation_equipment
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for cnc_mill
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for coil_winding_machine
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for controlled_atmosphere_chamber
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for coordinate_measuring_machine
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for crucible_graphite
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for crucible_refractory
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for cutting_tools_general
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for dies
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for drawing_die_set_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for drill_press
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for drilling_equipment_v0
- cmd: sim.note
  args:
    style: warning
    message: Import-only machine 'drying_basic_v0' has no recipe target.
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for drying_basic_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for drying_oven
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for dust_collection_system
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for electrodes
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for electrolysis_cell_unit_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for enclosure_small
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for epoxy_processing_unit
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for epoxy_synthesis_unit
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for excavator_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for fiber_drawing_tower
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for filtration_unit
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for fixturing_workbench
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for forging_press_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for furnace
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for furnace_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for furnace_high_temp
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for generic_chemical_reactor_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for glass_furnace_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for gravity_separator
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for grinder_cylindrical_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for grinding_wheels
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for hand_tools_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for hand_tools_electrical
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for hand_tools_mechanical
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for heat_treatment_furnace_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for heating_furnace
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for heating_plate_induction_heater
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for heliostat_array_system_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for high_temperature_power_supply_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for hot_press_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for hydraulic_assembly_tools
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for hydraulic_press
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for induction_forge_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for inspection_tools_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for kiln_ceramic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for lab_v0
- cmd: sim.note
  args:
    style: warning
    message: Import-only machine 'labor_bot_general_v0' has no recipe target.
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for labor_bot_general_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for lathe_engine_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for leak_test_equipment
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for lifting_equipment
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for magnetic_separator_drum_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for manual_labour
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for measurement_equipment
- cmd: sim.note
  args:
    style: warning
    message: Import-only machine 'metal_forming_basic_v0' has no recipe target.
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for metal_forming_basic_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for metal_shear_or_saw
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for milling_machine_general_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for mixer_or_blender
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for mixing_tank_medium
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for molding_press
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for molding_press_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for mre_reactor_v0
- cmd: sim.note
  args:
    style: warning
    message: Import-only machine 'multimeter_set' has no recipe target.
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for multimeter_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for oscilloscope_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for pcb_fab_equipment
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for pellet_press
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for pelletizer_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for plastic_extruder
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for plate_rolling_mill
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for powder_mixer
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for power_conditioning_equipment
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for power_distribution_bus
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for power_hammer_or_press
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for power_supply_benchtop
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for precision_lathe
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for precision_levels
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for precision_tooling_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for press_brake
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for press_brake_die_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for press_ram_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for pressing_mold_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for pyrolysis_chamber_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for quench_tank
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for reduction_furnace_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for refractory_installation_tools
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for resource_3d_printer_cartesian_v0_machine
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for rock_crusher_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for rolling_mill_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for sand_casting_flask_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for saw_or_cutting_tool
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for screening_equipment
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for screening_equipment_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for sintering_furnace_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for solar_array_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for solar_tracking_optional
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for soldering_station
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for spinning_machine_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for stamping_press_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for steel_forming_press
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for surface_grinder
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for surface_treatment_station
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for tension_control_system
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for tension_gauge
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for test_bench_electrical
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for test_equipment_basic
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for tube_bender
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for vapor_capture_system_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for vibrating_screen_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for vibratory_feeder_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for welding_consumables
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for welding_power_supply_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for welding_tig_unit_v0
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for welding_tools_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for winding_drums
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for wire_crimping_tools
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for wire_drawing_die_set
- cmd: sim.note
  args:
    style: warning
    message: Import-only machine 'wire_stripper_set' has no recipe target.
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for wire_stripper_set
- cmd: sim.note
  args:
    style: info
    message: Import-only plan for work_rest_adjustable
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 9078
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_carbonaceous_collection_v0
    quantity: 9500
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_highlands_v0
    quantity: 15306
- cmd: sim.run-recipe
  args:
    recipe: recipe_recovered_salt_v0
    quantity: 2958
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_polar_psc_v0
    quantity: 1717
- cmd: sim.run-recipe
  args:
    recipe: recipe_solar_irradiance_v0
    quantity: 1750
- cmd: sim.run-recipe
  args:
    recipe: recipe_bulk_material_or_parts_import_v0
    quantity: 726
- cmd: sim.run-recipe
  args:
    recipe: recipe_mos2_solid_lubricant_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_plastic_pellets_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_magnet_wire_copper_v1
    quantity: 44
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_supply_components_basic_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_valve_body_cast_rough_v1
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_copper_plate_or_sheet_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_manual_labour_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_copper_wire_magnet_v1
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_bus_bar_copper_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_epoxy_precursor_block_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_test_equipment_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_basalt_aggregate_v0
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_ilmenite_from_regolith_v0
    quantity: 89203
- cmd: sim.run-recipe
  args:
    recipe: recipe_meteorite_iron_v0
    quantity: 120
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_coarse_fraction_v0
    quantity: 702790
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_fine_fraction_v0
    quantity: 4975
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_metal_crude_v0
    quantity: 711
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reductant_v0
    quantity: 46697
- cmd: sim.run-recipe
  args:
    recipe: recipe_rock_feedstock_raw_v0
    quantity: 400
- cmd: sim.run-recipe
  args:
    recipe: recipe_uncoated_substrate_material_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_water_v0
    quantity: 82587
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_energy_thermionic_v0
    quantity: 1850
- cmd: sim.run-recipe
  args:
    recipe: recipe_grinding_wheels_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_epoxy_synthesis_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_wet_material_import_v0
    quantity: 351
- cmd: sim.run-recipe
  args:
    recipe: recipe_high_temp_additive_v0
    quantity: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_plastic_housing_molded_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_wire_lengths_v0
    quantity: 16
- cmd: sim.run-recipe
  args:
    recipe: recipe_valve_body_machined_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_copper_strip_thin_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_epoxy_resin_base_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_basalt_molten_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_metal_pure_v0
    quantity: 374
- cmd: sim.run-recipe
  args:
    recipe: recipe_nickel_metal_import_v0
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_coarse_powder_v0
    quantity: 421
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_liner_set_abrasion_resistant_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_powder_v0
    quantity: 421250
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_reducing_agent_v0
    quantity: 13383
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_metal_from_regolith_carbothermic_v0
    quantity: 73
- cmd: sim.run-recipe
  args:
    recipe: recipe_granite_surface_plate_large_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_copper_clad_laminate_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_dried_material_v0
    quantity: 148
- cmd: sim.run-recipe
  args:
    recipe: recipe_silica_purified_v0
    quantity: 179
- cmd: sim.run-recipe
  args:
    recipe: recipe_grease_bearing_high_temp_v0
    quantity: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_wire_and_connectors_v0
    quantity: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_coating_material_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_fiber_material_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_housing_steel_v0
    quantity: 11
- cmd: sim.run-recipe
  args:
    recipe: recipe_nickel_chromium_alloy_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_stainless_steel_ingot_v0
    quantity: 35
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_powder_mixture_v0
    quantity: 421
- cmd: sim.run-recipe
  args:
    recipe: recipe_feeder_trough_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_barium_oxide_v0
    quantity: 40000
- cmd: sim.run-recipe
  args:
    recipe: recipe_oxygen_gas_v0
    quantity: 185
- cmd: sim.run-recipe
  args:
    recipe: recipe_iron_pig_or_ingot_v0
    quantity: 23948
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_v0
    quantity: 2442
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_steel_high_carbon_v0
    quantity: 63
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrical_steel_sheet_v0
    quantity: 131
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicon_powder_v0
    quantity: 30
- cmd: sim.run-recipe
  args:
    recipe: recipe_bare_pcb_import_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_element_resistive_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_stainless_steel_sheet_v1
    quantity: 35
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_powder_v0
    quantity: 380
- cmd: sim.run-recipe
  args:
    recipe: recipe_crucible_refractory_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_wire_v0
    quantity: 151
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_heavy_v0
    quantity: 21
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_dioxide_gas_v0
    quantity: 61
- cmd: sim.run-recipe
  args:
    recipe: recipe_casting_furnace_shell_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_dies_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_shell_refractory_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_gas_blower_basic_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_grinding_spindle_assembly_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_element_set_high_temp_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_high_temp_power_supply_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lubrication_pack_basic_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_base_large_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_medium_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_magnetic_separator_drum_body_v0
    quantity: 19
- cmd: sim.run-recipe
  args:
    recipe: recipe_molding_press_v1
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_molten_material_or_preform_v0
    quantity: 700
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_bearing_set_small_v0
    quantity: 14
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_mill_shell_generic_v0
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_part_support_frame_welded_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_frame_medium_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_raw_metal_block_v0
    quantity: 255
- cmd: sim.run-recipe
  args:
    recipe: recipe_reactor_vessel_mre_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_separator_frame_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_silver_ingot_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_welded_assemblies_v0
    quantity: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_welded_fabrications_v0
    quantity: 87
- cmd: sim.run-recipe
  args:
    recipe: recipe_wire_crimping_tools_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_gearbox_housing_cast_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_billet_or_slab_v0
    quantity: 1417
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_ingot_v0
    quantity: 20834
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_small_v0
    quantity: 26
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_tubing_stock_v1
    quantity: 700
- cmd: sim.run-recipe
  args:
    recipe: recipe_anchor_installation_kit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_precision_tooling_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_shear_blade_or_saw_band_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_precursor_v0
    quantity: 39
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_monoxide_v0
    quantity: 289
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_column_cast_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_base_metal_parts_v1
    quantity: 170
- cmd: sim.run-recipe
  args:
    recipe: recipe_heliostat_actuator_unit_v0
    quantity: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_wire_feed_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silver_contact_material_v1
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_headstock_blank_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_raw_v0
    quantity: 670
- cmd: sim.run-recipe
  args:
    recipe: recipe_array_mount_structure_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_ball_steel_v0
    quantity: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_sheet_or_plate_v0
    quantity: 106
- cmd: sim.run-recipe
  args:
    recipe: recipe_sheet_metal_or_structural_steel_v0
    quantity: 22
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_or_sheet_v0
    quantity: 11658
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_plate_raw_v0
    quantity: 1173
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_1mm_v0
    quantity: 578
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_22ga_v0
    quantity: 99
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_sheet_3mm_v1
    quantity: 235
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_stock_bar_or_billet_v0
    quantity: 1601
- cmd: sim.run-recipe
  args:
    recipe: recipe_alignment_tools_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_enclosure_small_additive_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hand_tools_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_conditioning_module_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_curing_agent_v0
    quantity: 9
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_polymer_v0
    quantity: 34
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_vessel_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulated_part_or_wire_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_spring_compression_small_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_headstock_simple_v5
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_gear_set_medium_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_frame_welded_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_frame_steel_v0
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_test_bench_frame_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_rod_steel_v0
    quantity: 105
- cmd: sim.run-recipe
  args:
    recipe: recipe_chamber_shell_sealed_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_excavator_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_fixturing_workbench_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hot_wire_cutter_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_frame_small_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_screen_deck_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_screening_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_tank_shell_steel_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_coordinate_measuring_machine_v1
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_cut_parts_v0
    quantity: 281
- cmd: sim.run-recipe
  args:
    recipe: recipe_formed_metal_part_v0
    quantity: 108
- cmd: sim.run-recipe
  args:
    recipe: recipe_heliostat_frame_v0_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_piping_components_v0
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_output_terminals_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_sand_casting_flask_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_frame_heavy_v0
    quantity: 14
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_strip_thin_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_frame_large_v0
    quantity: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_part_surface_treated_v0
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_rock_crusher_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_cage_stamped_v0
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_washer_flat_medium_steel_v0
    quantity: 38
- cmd: sim.run-recipe
  args:
    recipe: recipe_cyclone_separator_body_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrolysis_cell_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_anvil_or_die_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bolt_hex_medium_steel_v0
    quantity: 2736
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_shaft_steel_v0
    quantity: 13
- cmd: sim.run-recipe
  args:
    recipe: recipe_saw_or_cutting_tool_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_bar_stock_v0
    quantity: 854
- cmd: sim.run-recipe
  args:
    recipe: recipe_oscilloscope_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_supply_benchtop_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_coil_insulation_material_v0
    quantity: 19
- cmd: sim.run-recipe
  args:
    recipe: recipe_silicone_rubber_v0
    quantity: 15
- cmd: sim.run-recipe
  args:
    recipe: recipe_hand_tools_electrical_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_tension_gauge_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_refractory_installation_tools_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_quench_tank_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_coolant_pump_system_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_part_raw_v0
    quantity: 513
- cmd: sim.run-recipe
  args:
    recipe: recipe_rough_part_v0
    quantity: 591
- cmd: sim.run-recipe
  args:
    recipe: recipe_tool_station_frame_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_forged_steel_parts_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_seal_set_high_temp_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_washer_lock_medium_steel_v0
    quantity: 26
- cmd: sim.run-recipe
  args:
    recipe: recipe_heliostat_array_system_v0_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_tension_control_system_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_transformer_power_medium_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_tube_bender_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_circuit_breaker_thermal_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_wire_drawing_die_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_cutting_tools_general_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_rings_machined_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_filler_wire_basic_v0
    quantity: 14
- cmd: sim.run-recipe
  args:
    recipe: recipe_inspection_tools_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_nut_hex_medium_steel_v0
    quantity: 79
- cmd: sim.run-recipe
  args:
    recipe: recipe_piping_and_fittings_set_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_brake_die_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_pressing_mold_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_shaft_set_medium_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_structural_steel_frame_v0
    quantity: 7
- cmd: sim.run-recipe
  args:
    recipe: recipe_winding_drums_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_electric_motor_small_v0
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_hammer_drive_motor_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_coil_wound_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_electric_small_v0
    quantity: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_soldering_station_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_spindle_drive_motor_small_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_vibrator_motor_small_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_seals_set_v0
    quantity: 24
- cmd: sim.run-recipe
  args:
    recipe: recipe_seal_rubber_bearing_v0
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_coolant_reservoir_v0
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_crucible_graphite_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_drawing_die_set_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_large_v1
    quantity: 9
- cmd: sim.run-recipe
  args:
    recipe: recipe_generic_chemical_reactor_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_assembly_tools_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_measurement_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_tools_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_finished_part_v0
    quantity: 500
- cmd: sim.run-recipe
  args:
    recipe: recipe_table_top_t_slot_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembly_tools_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lab_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_rings_hardened_v1
    quantity: 11
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_fiber_drawing_tower_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixer_drum_small_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_molding_press_frame_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_tracking_mount_structure_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_work_rest_adjustable_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_fastener_kit_medium_assembly_v0
    quantity: 38
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_leak_test_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bending_machine_v0_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_mixing_tank_medium_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_vacuum_pump_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_cylinder_medium_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembled_equipment_v0
    quantity: 7
- cmd: sim.run-recipe
  args:
    recipe: recipe_hot_press_frame_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_press_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_metal_shear_or_saw_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_sintering_furnace_shell_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_surface_grinder_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_drill_press_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_rings_ground_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_mixer_or_blender_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_assembly_station_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_balancing_machine_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_bath_tank_set_v1
    quantity: 3
- cmd: sim.run-recipe
  args:
    recipe: recipe_coil_winding_machine_v1
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_drive_motor_medium_v1
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_drying_oven_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_filtration_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_gas_handling_system_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_gearbox_reducer_medium_v0
    quantity: 5
- cmd: sim.run-recipe
  args:
    recipe: recipe_induction_forge_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_high_temperature_power_supply_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_powder_mixer_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_power_distribution_bus_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_screening_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_solar_array_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_solar_tracking_optional_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_spinning_machine_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_vibrating_screen_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_vibratory_feeder_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_molding_press_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_pellet_press_v1
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_pelletizer_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_conditioning_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_separation_table_assembly_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_test_bench_electrical_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_power_supply_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_vapor_capture_system_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_basic_fabrication_station_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_rolling_mill_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_basic_fabrication_station_v1
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_spindle_assembly_precision_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_bearing_set_sealed_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_bath_station_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_chemical_separation_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_surface_treatment_station_base_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_dust_collection_system_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_epoxy_processing_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_ball_mill_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_milling_machine_general_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_resource_3d_printer_cartesian_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_magnetic_separator_drum_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_gravity_separator_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_welding_power_supply_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_welding_tig_unit_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_spindle_and_bearings_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lifting_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_engine_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_chlorine_gas_v0
    quantity: 1316
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydrogen_gas_v1
    quantity: 88
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydrochloric_acid_v1
    quantity: 1440
- cmd: sim.run-recipe
  args:
    recipe: recipe_alumina_powder_v0
    quantity: 144
- cmd: sim.run-recipe
  args:
    recipe: recipe_sodium_hydroxide_v0
    quantity: 87
- cmd: sim.run-recipe
  args:
    recipe: recipe_methanol_liquid_v0
    quantity: 397
- cmd: sim.run-recipe
  args:
    recipe: recipe_ethanol_or_isopropanol_feedstock_v0
    quantity: 145
- cmd: sim.run-recipe
  args:
    recipe: recipe_ethanol_or_isopropanol_v0
    quantity: 145
- cmd: sim.run-recipe
  args:
    recipe: recipe_binder_simple_v0
    quantity: 95
- cmd: sim.run-recipe
  args:
    recipe: recipe_cmc_solution_v0
    quantity: 83
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_binder_v0
    quantity: 132
- cmd: sim.run-recipe
  args:
    recipe: recipe_binder_material_v0
    quantity: 119
- cmd: sim.run-recipe
  args:
    recipe: recipe_refractory_brick_set_v0
    quantity: 9
- cmd: sim.run-recipe
  args:
    recipe: recipe_blast_furnace_or_smelter_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_pack_high_temp_v0
    quantity: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_casting_furnace_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_permanent_mold_steel_set_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_casting_mold_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_chemical_reactor_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_milling_machine_cnc_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_basic_v0
    quantity: 13
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_controlled_atmosphere_chamber_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_methane_gas_v1
    quantity: 8
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_anode_material_v0
    quantity: 38
- cmd: sim.run-recipe
  args:
    recipe: recipe_carbon_anode_v1
    quantity: 28
- cmd: sim.run-recipe
  args:
    recipe: recipe_cryolite_flux_v0
    quantity: 6
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_alloy_ingot_v0
    quantity: 49
- cmd: sim.run-recipe
  args:
    recipe: recipe_cooling_fan_assembly_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_motor_electric_medium_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_drilling_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_electrodes_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_forging_press_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_basic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_high_temp_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_glass_furnace_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_casting_machine_base_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_grinder_cylindrical_v0_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_hand_tools_mechanical_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_ceramic_fiber_slurry_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_ceramic_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_insulation_thermal_blanket_v0
    quantity: 9
- cmd: sim.run-recipe
  args:
    recipe: recipe_furnace_shell_insulated_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_refractory_lining_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_heat_treatment_furnace_v0_target_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_furnace_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_heating_plate_induction_heater_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_cutting_fluid_v0
    quantity: 85
- cmd: sim.run-recipe
  args:
    recipe: recipe_aluminum_tube_stock_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_fittings_and_valves_v0
    quantity: 4
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_control_valve_set_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_hydraulic_system_medium_v0
    quantity: 2
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_hot_press_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_kiln_ceramic_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_mre_reactor_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_prepared_mold_v0
    quantity: 69
- cmd: sim.run-recipe
  args:
    recipe: recipe_cast_metal_parts_v0
    quantity: 679
- cmd: sim.run-recipe
  args:
    recipe: recipe_pcb_drilling_station_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_pcb_fab_equipment_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_plastic_extruder_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_plate_rolling_mill_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_power_hammer_or_press_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_coating_compound_v0
    quantity: 50
- cmd: sim.run-recipe
  args:
    recipe: recipe_machined_steel_part_precision_v0
    quantity: 500
- cmd: sim.run-recipe
  args:
    recipe: recipe_lathe_bed_and_headstock_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_precision_lathe_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_precision_levels_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_press_brake_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_press_ram_set_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_pyrolysis_chamber_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_refractory_castable_v0
    quantity: 100
- cmd: sim.run-recipe
  args:
    recipe: recipe_thermal_insulation_high_temp_v0
    quantity: 13
- cmd: sim.run-recipe
  args:
    recipe: recipe_reduction_furnace_shell_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_reduction_furnace_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_sintering_furnace_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_stamping_press_basic_import_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_steel_forming_press_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_storage_enclosure_v0
    quantity: 1
- cmd: sim.run-recipe
  args:
    recipe: recipe_machine_welding_consumables_v0
    quantity: 1
- cmd: sim.status
  args: {}
```
