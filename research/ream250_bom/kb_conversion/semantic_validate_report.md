# reAM250 BOM-to-KB Row Conversion Semantic Validate

## Summary

- Conversion files: 262
- Hard errors: 0
- Warning rows: 8
- Warning count: 8

## Queue Status

- `done`: 663
- `pending`: 139

## Row Conversion Queue Status

- `done`: 262
- `pending`: 139

## Primary Process Buckets

- `sheet_plate_cutting_drilling`: 55
- `plumbing_connector_fabrication_testing`: 46
- `general_subtractive_machining`: 44
- `precision_component_import_decompose_later`: 41
- `structural_profile_stock_fabrication_cutting`: 31
- `fastener_forming_thread_rolling`: 21
- `polymer_elastomer_forming_dispensing`: 16
- `general_metal_additive_with_finish_machining`: 7
- `manual_assembly_with_general_tools`: 1

## Functional Purpose Keys

- `structural_frame_member`: 28
- `plumbing_connection`: 27
- `enclosure_barrier`: 10
- `linear_guidance`: 9
- `interface_clamping`: 9
- `joint_clamping`: 8
- `threaded_fastening`: 7
- `joint_sealing`: 5
- `structural_support`: 5
- `bearing_support`: 5
- `mechanical_fastening`: 5
- `powder_containment`: 5
- `environment_barrier`: 4
- `structural_frame_support_member`: 4
- `interface_sealing`: 3
- `rolling_element`: 3
- `flow_control`: 3
- `sealing_element`: 3
- `mounting_support`: 3
- `gas_flow_routing`: 3
- `spacing_alignment`: 2
- `structural_spacing`: 2
- `rolling_contact`: 2
- `mechanical_retention`: 2
- `motor_mounting`: 2
- `particulate_separator`: 2
- `gas_flow_path`: 2
- `gas_flow_guidance`: 2
- `motion_transmission`: 2
- `manual_flow_control`: 2
- `mounting_interface`: 2
- `optical_interface_mount`: 1
- `manual_handle`: 1
- `optical_access`: 1
- `adapter_support_frame`: 1
- `optical_mounting_adapter`: 1
- `optical_port_mounting_retention`: 1
- `mechanical_clamping`: 1
- `hinge_hardware`: 1
- `articulated_joint`: 1
- `rotary_support`: 1
- `bearing_retention`: 1
- `rotary_bearing`: 1
- `bearing_rolling_element`: 1
- `axis_bearing_positioning`: 1
- `linear_position_feedback`: 1
- `linear_actuation`: 1
- `right_angle_speed_reduction_torque_transmission`: 1
- `motion_actuation`: 1
- `structural_guidance_shell`: 1
- `mounting_spacing`: 1
- `heat_distribution`: 1
- `fastening_hardware`: 1
- `platform_support`: 1
- `spring_reaction_support`: 1
- `preload_support`: 1
- `mechanical_support`: 1
- `temperature_measurement`: 1
- `mechanical_spacing`: 1
- `heater_area_cover_closure`: 1
- `cover_retention`: 1
- `subassembly_retention`: 1
- `sensor_triggering`: 1
- `end_switch_sensor_flag`: 1
- `fastening`: 1
- `threaded_fastening_hardware`: 1
- `flexible_plumbing_connector`: 1
- `particle_filtration`: 1
- `gas_flow_path_segment`: 1
- `gas_flow_rectification`: 1
- `oxygen_concentration_measurement`: 1
- `sliding_contact_guidance`: 1
- `wear_resistant_contact_member`: 1
- `bonded_component_retention`: 1
- `powder_spreading`: 1
- `blade_clamping`: 1
- `bearing_mount`: 1
- `rotary_power_transmission`: 1
- `rotary_motion_transmission`: 1
- `rotary_actuation`: 1
- `power_transmission`: 1
- `upper_frame_support`: 1
- `perimeter_panel_barrier`: 1
- `gas_sensing`: 1
- `leakage_prevention`: 1
- `synchronous_motion_transmission`: 1
- `laser_beam_steering`: 1
- `axial_retention`: 1
- `shaft_retention`: 1
- `rotating_contact_support`: 1
- `laser_source`: 1
- `gas_pumping`: 1
- `flow_control_valve`: 1
- `pressure_sensing`: 1
- `structural_spacer`: 1
- `modular_machine_frame_member`: 1
- `machine_interface`: 1
- `pressure_relief`: 1
- `joint_centering`: 1
- `electrical_signal_transfer`: 1
- `heat_exchange`: 1
- `structural_housing`: 1
- `timing_belt_power_transmission`: 1
- `interface_support`: 1
- `powder_guidance_chute`: 1
- `plumbing_connection_reducer`: 1
- `threaded_fastener`: 1
- `threaded_clamping_fastener`: 1
- `identification_labeling`: 1
- `elastomer_sealing`: 1
- `thermal_imaging_module`: 1
- `camera_mounting`: 1
- `mechanical_stop`: 1
- `structural_connection`: 1
- `compression_sealing`: 1
- `optical_window`: 1
- `mounting_base`: 1
- `rotary_shaft_sealing`: 1
- `rotary_torque_feedthrough`: 1
- `machine_support`: 1
- `rolling_bearing`: 1
- `torque_transmission_shaft`: 1

## Active Leases

_None._

## Hard Errors

_None._

## Semantic Warnings

- `research/ream250_bom/ream250_bom_row_0090_2APK1.md`
  - functional_purpose_key `heater_area_cover_closure` appears to contain component form detail
- `research/ream250_bom/ream250_bom_row_0091_2APK2.md`
  - functional_purpose_key `cover_retention` appears to contain component form detail
- `research/ream250_bom/ream250_bom_row_0189_6M1.md`
  - local_manufacturing_paths_considered has more than two paths; keep it focused on the selected closure path
- `research/ream250_bom/ream250_bom_row_0216_12.md`
  - functional_purpose_key `perimeter_panel_barrier` appears to contain component form detail
- `research/ream250_bom/ream250_bom_row_0258_41C.md`
  - local_manufacturing_paths_considered has more than two paths; keep it focused on the selected closure path
- `research/ream250_bom/ream250_bom_row_0272_66.md`
  - plate-like cover/panel/guard uses `general_subtractive_machining`; consider `sheet_plate_cutting_drilling` with machining as supporting work
- `research/ream250_bom/ream250_bom_row_0291_91F1.md`
  - local_manufacturing_paths_considered has more than two paths; keep it focused on the selected closure path
- `research/ream250_bom/ream250_bom_row_0344_522.md`
  - material is unresolved and multiple local manufacturing paths are listed; move speculative material-driven alternatives to assumptions/unresolved/import risks

## New Semantic Warnings

_None._

## Random Review Sample

- `research/ream250_bom/ream250_bom_row_0168_6B1.md` - key `sliding_contact_guidance`, bucket `general_subtractive_machining`
- `research/ream250_bom/ream250_bom_row_0181_6G.md` - key `powder_containment`, bucket `sheet_plate_cutting_drilling`
- `research/ream250_bom/ream250_bom_row_0315_195.md` - key `plumbing_connection`, bucket `plumbing_connector_fabrication_testing`
- `research/ream250_bom/ream250_bom_row_0346_524.md` - key `enclosure_barrier`, bucket `sheet_plate_cutting_drilling`
- `research/ream250_bom/ream250_bom_row_0360_916.md` - key `structural_support`, bucket `structural_profile_stock_fabrication_cutting`

## Singleton Functional Keys

- `adapter_support_frame`
- `articulated_joint`
- `axial_retention`
- `axis_bearing_positioning`
- `bearing_mount`
- `bearing_retention`
- `bearing_rolling_element`
- `blade_clamping`
- `bonded_component_retention`
- `camera_mounting`
- `compression_sealing`
- `cover_retention`
- `elastomer_sealing`
- `electrical_signal_transfer`
- `end_switch_sensor_flag`
- `fastening`
- `fastening_hardware`
- `flexible_plumbing_connector`
- `flow_control_valve`
- `gas_flow_path_segment`
- `gas_flow_rectification`
- `gas_pumping`
- `gas_sensing`
- `heat_distribution`
- `heat_exchange`
- `heater_area_cover_closure`
- `hinge_hardware`
- `identification_labeling`
- `interface_support`
- `joint_centering`
- `laser_beam_steering`
- `laser_source`
- `leakage_prevention`
- `linear_actuation`
- `linear_position_feedback`
- `machine_interface`
- `machine_support`
- `manual_handle`
- `mechanical_clamping`
- `mechanical_spacing`
- `mechanical_stop`
- `mechanical_support`
- `modular_machine_frame_member`
- `motion_actuation`
- `mounting_base`
- `mounting_spacing`
- `optical_access`
- `optical_interface_mount`
- `optical_mounting_adapter`
- `optical_port_mounting_retention`
- `optical_window`
- `oxygen_concentration_measurement`
- `particle_filtration`
- `perimeter_panel_barrier`
- `platform_support`
- `plumbing_connection_reducer`
- `powder_guidance_chute`
- `powder_spreading`
- `power_transmission`
- `preload_support`
- `pressure_relief`
- `pressure_sensing`
- `right_angle_speed_reduction_torque_transmission`
- `rolling_bearing`
- `rotary_actuation`
- `rotary_bearing`
- `rotary_motion_transmission`
- `rotary_power_transmission`
- `rotary_shaft_sealing`
- `rotary_support`
- `rotary_torque_feedthrough`
- `rotating_contact_support`
- `sensor_triggering`
- `shaft_retention`
- `sliding_contact_guidance`
- `spring_reaction_support`
- `structural_connection`
- `structural_guidance_shell`
- `structural_housing`
- `structural_spacer`
- ... 11 more

