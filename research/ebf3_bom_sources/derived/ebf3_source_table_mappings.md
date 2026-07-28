# EBF3 Source-Table Mappings

Authority note: this is a consolidated first-pass scaffold mapping from
user-derived subsystem tables. It preserves candidate item IDs and high-level
modeling intent, but it is not a decomposition planning file and cannot by
itself justify child BOM creation, material selection, recipe closure, or local
manufacturability.

Use the corresponding `organized/*_level_2_audit.md` file when a mapping row
needs source-table correction, boundary rationale, or readiness interpretation.
Masses are first-pass allocations constrained to the current subsystem masses.
Leaf items intentionally have no local recipes unless a separate material/process
readiness review says otherwise.

## Controls

Aligned after `research/ebf3_bom_sources/organized/controls_level_2_audit.md`.

| Source row | Item ID | Modeling decision |
| --- | --- | --- |
| CTL-1 | `ebf3_control_computer` | Industrial PC/control computer for operator commands, subsystem coordination, and fabrication process management. |
| CTL-2 | `ebf3_realtime_control_processor` | Deterministic controller/FPGA/DSP/MCU hardware for high-voltage, motion, wire-feed, and interlock timing. |
| CTL-3 | `ebf3_control_software` | Control software stored on controller media; command sequencing, interlocks, data logging, and process control logic. |
| CTL-4 | `ebf3_can_bus_interface` | CAN-bus communication interface between control computer and HV, magnetic, modulator, alarm, and subsystem controllers. |
| CTL-5 | `ebf3_analog_input_adc_module` | Analog input and ADC module for voltage, current, temperature, and feedback measurement. |
| CTL-6 | `ebf3_sensor_interface_module` | Sensor interface electronics for thermocouples, pressure sensors, beam diagnostics, and isolated signal conditioning. |
| CTL-7 | `ebf3_data_logger_timebase` | Data logger and timebase module for process history and later analysis. |
| CTL-8 | `ebf3_visible_camera` | Visible camera assembly for monitoring deposition and chamber process state. |
| CTL-9 | `ebf3_thermal_imaging_monitoring_system` | Thermal imaging monitoring system for melt-pool temperature or thermal-field monitoring. |
| CTL-10 | `ebf3_motion_control_drive_module` | Motion drive/control module for commanded positioning subsystem motion. |
| CTL-11 | `ebf3_wire_feed_control_module` | Wire-feed control electronics for feed motor command and feedback. |
| CTL-12 | `ebf3_safety_blocking_logic` | Safety logic, alarm, and blocking/interlock module. |
| CTL-13 | `ebf3_controls_cabinet` | Controls cabinet assembly for control computer, I/O, communication hardware, safety logic, terminal blocks, and cabinet hardware. |

Deferred candidates kept out of the source-table Level-2 presentation:

- `ebf3_process_monitor_lighting`
- `ebf3_control_cabinet_harness`

## Power Supplies

Aligned after `research/ebf3_bom_sources/organized/power_supplies_level_2_audit.md`.

| Source row | Item ID | Modeling decision |
| --- | --- | --- |
| PS-1 | `ebf3_power_input_cable_gland` | AC input connector, cable gland, strain relief, and cabinet entry hardware. |
| PS-2 | `ebf3_main_disconnect_switch` | Main disconnect switch for isolation and service safety. |
| PS-3 | `ebf3_emi_filter` | EMI filter for reducing high-frequency conducted noise. |
| PS-4 | `ebf3_input_rectifier` | Input rectifier converting AC input to DC bus voltage. |
| PS-5 | `ebf3_dc_link_capacitor_bank` | DC-link capacitor bank for bus energy storage and smoothing. |
| PS-6 | `ebf3_ripple_damping_inductor` | Ripple damping/filter inductor in the rectified DC input stage. |
| PS-7 | `ebf3_full_bridge_inverter` | Full-bridge inverter power stage for high-frequency transformer drive. |
| PS-8 | `ebf3_inverter_matching_network` | Impedance matching network for inverter/HV transformer drive. |
| PS-9 | `ebf3_primary_isolation_transformer` | Primary-side isolation transformer in the HV source drive chain. |
| PS-10 | `ebf3_control_electrode_bias_supply` | Bias supply for electron-gun control electrode. |
| PS-11 | `ebf3_cathode_heater_supply` | Stabilized cathode heater power supply. |
| PS-12 | `ebf3_auxiliary_low_voltage_dc_supply` | Auxiliary low-voltage DC supply for sensors, interfaces, motors, valves, drivers, feeder electronics, and positioning electronics. |
| PS-13 | `ebf3_low_voltage_distribution_panel` | Low-voltage distribution panel for protected branches. |
| PS-14 | `ebf3_multi_channel_driver_module` | Multi-channel driver module for magnetic, deflection, feeder, and positioning loads. |
| PS-15 | `ebf3_power_electronics_thermal_management` | Thermal management hardware for power electronics. |

Deferred/derived functional candidates kept out of the source-table Level-2
presentation:

- `ebf3_damping_resistor`
- `ebf3_snubber_network`
- `ebf3_accelerating_voltage_dc_supply`
- `ebf3_lens_corrector_current_supplies`
- `ebf3_power_supply_control_board`
- `ebf3_power_supply_cabinet_bus_cooling`

## High Voltage Tank

Mapped after `research/ebf3_bom_sources/organized/high_voltage_tank_level_2_audit.md`.

| Source ID | KB item ID | Modeling decision |
| --- | --- | --- |
| HV-1 | `ebf3_hv_tank_enclosure` | Oil-filled high-voltage tank enclosure for transformer, rectifier, filter, and interfaces. |
| HV-2 | `ebf3_hv_transformer_insulating_fluid` | Silicone/silicon oil or transformer insulating fluid for dielectric isolation and heat transfer. |
| HV-3/4/5 sectioned architecture | `ebf3_hv_section_module_set` | Concise section-module-set representation for source-backed winding/rectifier/filter section architecture. |
| HV-3 functional constituent | `ebf3_sectioned_hv_step_up_transformer` | Step-up transformer/winding function inside the section-module set. |
| HV-4 functional constituent | `ebf3_hv_rectifier_stack_tank_side` | Rectifier function inside the section-module set. |
| HV-5 functional constituent | `ebf3_hv_output_filter_capacitor` | Output filter capacitor function inside the section-module set. |
| HV-6 | `ebf3_internal_hv_leads_terminals` | Oil-side internal high-voltage conductors, straps, studs, and rounded terminals. |
| HV-7 | `ebf3_transformer_insulation_spacers` | Transformer/rectifier/capacitor support spacers and insulation distance maintainers. |
| HV-8 | `ebf3_tank_side_hv_output_bushing` | Tank-side high-voltage output bushing/feedthrough/socket assembly. |
| HV-9 | `ebf3_hv_cable_to_gun` | High-voltage cable carrying accelerating voltage from tank to fixed electron beam gun. |
| HV-10 | `ebf3_hv_discharge_bleeder_resistor_chain` | High-voltage discharge/bleeder resistor chain candidate. |
| HV-11 | `ebf3_hv_output_voltage_divider_sensing` | High-voltage output voltage divider or scaled voltage sensing candidate. |
| HV-12 | `ebf3_hv_output_return_current_monitor` | HV output or return current monitor candidate. |
| HV-13 split | `ebf3_hv_tank_fill_drain_ports` | Oil fill, drain, sampling, and service ports for HV tank. |
| HV-13 split | `ebf3_hv_tank_pressure_relief` | Pressure relief or venting hardware for oil-filled tank safety. |
| HV-13 split | `ebf3_hv_tank_oil_level_indicator` | Oil level indicator or sight interface for tank maintenance. |
| HV-14 | `ebf3_hv_tank_temperature_sensor` | Oil or HV transformer temperature sensing hardware for protection and control. |
| HV-15 partial | `ebf3_hv_tank_grounding_terminal` | Grounding terminal and bonding interface for HV tank enclosure; shielding/interlock details remain unresolved. |

The previous inferred HV tank mounting-frame row was removed from the active
mapping because no source row or external source confirms it as a separate
modeled assembly.

## Fixed Electron Beam Gun

User-derived table: `research/ebf3_bom_sources/organized/V2_fixed_electron_beam_gun_item_table.pdf`.

| Source ID | KB item ID | Modeling decision |
| --- | --- | --- |
| FG-1 | `ebf3_gun_cathode` | Discrete refractory-metal cathode; material variant still pending. |
| FG-2 | `ebf3_gun_anode` | Discrete refractory-metal precision electrode. |
| FG-3 | `ebf3_gun_control_electrode` | Discrete refractory-metal control electrode. |
| FG-4 | `ebf3_gun_control_electrode_insulator` | Discrete ceramic insulator. |
| FG-5 | `ebf3_gun_screen_electrode` | Discrete refractory-metal screen/boundary electrode. |
| FG-6 | `ebf3_gun_dynamic_magnetic_lens` | Composite electromagnetic lens assembly. |
| FG-7 | `ebf3_gun_main_magnetic_lens` | Composite electromagnetic lens assembly. |
| FG-8 | `ebf3_gun_two_axis_deflection_coils` | Composite X/Y deflection coil assembly. |
| FG-9 | `ebf3_gun_beam_boundary_pickup` | Composite beam protection/diagnostic pickup. |
| FG-10 | `ebf3_gun_secondary_electron_pickup` | Composite secondary-electron monitoring pickup. |
| FG-11 | `ebf3_gun_trajectory_corrector` | Composite magnetic corrector assembly. |
| FG-12 | `ebf3_gun_hv_input` | Composite high-voltage feedthrough/input assembly. |
| FG-13 | `ebf3_gun_hv_insulator` | Discrete ceramic high-voltage insulator. |
| FG-14 | `ebf3_gun_cathode_heater_leads` | Composite heater lead assembly. |
| FG-15 | `ebf3_gun_cathode_cartridge` | Composite replaceable cathode holder/cartridge. |
| FG-16 | `ebf3_gun_cathode_radiation_shield` | Discrete refractory-metal shield set; inferred component. |
| FG-17 | `ebf3_gun_column` | Composite/mechanical structural column. |
| FG-18 | `ebf3_gun_side_oil_tank` | Composite gun-side oil tank assembly. |
| FG-19 | `ebf3_gun_signal_wiring` | Composite signal wiring/harness assembly. |

FG leaf items are intentionally left without local recipes for now: closure
would be premature and would hide unresolved material, precision, vacuum,
high-voltage, and high-temperature manufacturing questions.

## Manufacture Cabin

Mapped from `V1_manufacture cabin item table`.

| Source ID | Item ID | Modeling decision |
| --- | --- | --- |
| MC-1 | `ebf3_cabin_frame` | Structural skeleton of the sealed manufacturing chamber. |
| MC-2 | `ebf3_cabin_wall_panels` | Vacuum boundary wall panels and stiffened chamber shell surfaces. |
| MC-3 | `ebf3_cabin_access_door` | Service access door assembly with latch, hinge, and vacuum seal interface. |
| MC-4 | `ebf3_cabin_viewport` | Viewport or optical window for process observation. |
| MC-5 | `ebf3_cabin_gun_mounting_port` | Top/side chamber port and flange interface for fixed electron beam gun insertion. |
| MC-6 | `ebf3_cabin_wire_feeder_mounting_port` | Chamber-side wire-feeder mounting port or passive datum. |
| MC-7 | `ebf3_cabin_sacrificial_liner` | Replaceable liner or shield protecting cabin walls from condensate, spatter, and deposition debris. |
| MC-8 | `ebf3_cabin_positioning_mount_interface` | Chamber floor/access interface for the four-axis positioning subsystem. |
| MC-9 | `ebf3_cabin_lighting_mount_and_port` | Cabin-side passive lighting mount, optical access, or chamber penetration. |

Deferred source-related candidates:

- `ebf3_cabin_build_substrate_support`
- `ebf3_cabin_feedthroughs_and_wiring_ports`

See `research/ebf3_bom_sources/organized/manufacture_cabin_level_2_audit.md`
for the source-table correction and boundary rationale.

## Wire Feeder

Mapped from the wire feeder source table.

| Source ID | Item ID | Modeling decision |
| --- | --- | --- |
| WF-1 | `ebf3_wire_spool` | Wire spool holding feedstock wire before feeding. |
| WF-2 | `ebf3_spool_hub` | Hub supporting spool bore and rotation. |
| WF-3 | `ebf3_spool_support_shaft` | Support shaft for spool hub rotation. |
| WF-4 | `ebf3_spool_retaining_ring` | Retaining ring preventing spool/hub axial displacement. |
| WF-5 | `ebf3_spool_brake_washer` | Brake washer adding friction to prevent spool overrun. |
| WF-6 | `ebf3_spool_brake_adjuster` | Spool tension nut or adjustment hardware for spool brake force. |
| WF-7 | `ebf3_wire_feed_gearmotor` | Wire feed drive gearmotor assembly. |
| WF-8 | `ebf3_wire_feed_motor_clamp_insulator` | Insulating clamp component for motor/electrical isolation. |
| WF-9 | `ebf3_wire_feed_motor_mount_clamp` | Clamp or bracket holding feed motor in position. |
| WF-10 | `ebf3_drive_roll_carrier` | Carrier holding each drive roll in position. |
| WF-11 | `ebf3_drive_roll_carrier_spacer` | Spacer maintaining drive-roll carrier alignment. |
| WF-12 | `ebf3_wire_feed_drive_roll` | Drive roll converting motor torque into feed force. |
| WF-13 | `ebf3_wire_feed_pressure_arm` | Pressure-arm assembly applying force between wire and drive rolls. |
| WF-14 | `ebf3_pressure_adjustment_knob` | Knob or adjuster setting drive-roll pressure. |
| WF-15 | `ebf3_pressure_spring` | Spring providing drive-roll pressure force. |
| WF-16 | `ebf3_wire_inlet_guide` | Inlet guide positioning wire into the drive-roll area. |
| WF-17 | `ebf3_intermediate_wire_guide` | Intermediate guide between wire-feed regions. |
| WF-18 | `ebf3_wire_outlet_guide_tube` | Outlet wire guide toward the liner or downstream guide. |
| WF-19 | `ebf3_anti_wear_guide` | Anti-wear guide insert near the drive rolls. |
| WF-20 | `ebf3_feed_liner` | Replaceable downstream feed liner or guide tube. |
| WF-21 | `ebf3_ebf_wire_guide_tip` | Final EBF wire guide tip near the melt pool. |
| WF-22 | `ebf3_gun_feeder_adapter` | Adapter between feeder output and gun-side/downstream guide interface. |
| WF-23 | `ebf3_wire_feed_encoder_sensor` | Digital tachometer, encoder, or feed-rate sensor. |
| WF-24 | `ebf3_wire_feeder_base` | Structural base plate for the feeder. |
| WF-25 | `ebf3_wire_feeder_base_stiffener` | Base stiffener plate or rib. |
| WF-26 | `ebf3_drive_roll_cover` | Cover for drive-roll area. |
| WF-27 | `ebf3_wire_feeder_mount_to_gun_bracket` | Bracket mounting feeder to fixed electron beam gun. |

Deferred source-related candidates:

- `ebf3_wire_feed_pressure_roll`
- `ebf3_wire_feed_roll_bearing_set`
- `ebf3_wire_feed_drive_gear_set`
- `ebf3_wire_feed_idler_arm`
- `ebf3_wire_feed_spring_tensioner`
- `ebf3_wire_straightener_guides`
- `ebf3_wire_feed_nozzle`
- `ebf3_wire_feeder_body`
- `ebf3_wire_feeder_cover`
- `ebf3_wire_feeder_vacuum_motor_wiring`
- `ebf3_wire_feeder_feedthrough_connector`
- `ebf3_wire_feeder_fasteners_small`

See `research/ebf3_bom_sources/organized/wire_feeder_level_2_audit.md` for the
source-table correction and boundary rationale.

## Four-Axis Positioning System

Mapped from the four-axis positioning source table.

| Source ID | Item ID | Modeling decision |
| --- | --- | --- |
| FS-1 | `ebf3_positioning_base_frame` | Structural frame for positioning system. |
| FS-2 | `ebf3_positioning_axis_base_plate` | Base plate and datum surface for linear axes. |
| FS-3 | `ebf3_linear_guide_rails` | Precision linear guide rail set. |
| FS-4 | `ebf3_linear_guide_carriages` | Linear guide carriage/block assemblies. |
| FS-5 | `ebf3_ball_screw_shafts` | Ball screw shafts for linear motion. |
| FS-6 | `ebf3_ball_nuts` | Ball nut assemblies for screw drive. |
| FS-7 | `ebf3_fixed_side_screw_bearing_blocks` | Fixed-side screw support bearing blocks. |
| FS-8 | `ebf3_floating_side_screw_bearing_blocks` | Floating-side screw support bearing blocks. |
| FS-9 | `ebf3_axis_motors` | Axis motor assemblies for positioning system. |
| FS-10 | `ebf3_motor_couplings` | Motor-to-screw couplings. |
| FS-11 | `ebf3_motor_mount_brackets` | Brackets aligning motors with screw drives. |
| FS-12 | `ebf3_linear_encoder_scales` | Linear encoder scale/readhead assemblies. |
| FS-13 | `ebf3_axis_home_sensors` | Home sensors and targets for axes. |
| FS-14 | `ebf3_axis_travel_limit_switches` | Travel limit switch assemblies. |
| FS-15 | `ebf3_z_axis_brake` | Z-axis brake or holding mechanism. |
| FS-16 | `ebf3_z_axis_counterbalance` | Counterbalance or load-reduction mechanism for vertical axis. |
| FS-17 | `ebf3_rotary_axis_table` | Rotary build table mounted on linear axes. |
| FS-18 | `ebf3_rotary_axis_bearing` | Rotary bearing assembly supporting build table. |
| FS-19 | `ebf3_rotary_worm_wheel` | Worm wheel for the rotary-axis worm-drive pair. |
| FS-20 | `ebf3_rotary_worm_shaft` | Worm shaft for the rotary-axis worm-drive pair. |
| FS-21 | `ebf3_rotary_encoder` | Rotary encoder for angular position feedback. |
| FS-22 | `ebf3_moveable_build_platform` | Moveable platform carrying substrate through motion path. |
| FS-23 | `ebf3_substrate_clamp` | Clamp securing substrate to build platform. |
| FS-24 | `ebf3_beam_current_return_strap` | Grounding/current return strap for platform and beam current. |
| FS-25 | `ebf3_thermal_isolation_standoffs` | Thermal/electrical isolation standoffs for process zone. |
| FS-26 | `ebf3_positioning_bellows_cover` | Bellows/protective cover for axes near process debris. |
| FS-27 | `ebf3_spatter_shielding` | Shielding against metal vapor, spatter, and process-zone debris. |
| FS-28 | `ebf3_vacuum_compatible_motor_cabling` | Vacuum-compatible motor power cabling. |
| FS-29 | `ebf3_vacuum_compatible_signal_cabling` | Vacuum-compatible encoder and sensor signal cabling. |
| FS-30 | `ebf3_positioning_electrical_feedthrough` | Feedthrough passing motor/sensor signals through chamber wall. |

Deferred source-related candidates:

- `ebf3_rotary_drive_worm_gear`
- `ebf3_rotary_axis_motor`

See `research/ebf3_bom_sources/organized/four_axis_positioning_level_2_audit.md`
for the source-table correction and boundary rationale.
