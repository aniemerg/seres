# EBF3 Existing Item Replacement Register

Date: 2026-07-23

Purpose: record only EBF3 leaf items that are actively replaced by existing KB
items because the existing item is accurate enough for the EBF3 function at the
current BOM resolution. This register is not a place for imperfect substitutions:
if the candidate is too coarse, it belongs in the not-enough-accuracy section and
the EBF3 leaf remains active in the BOM.

## Summary

- Candidate replacements reviewed: 76.
- Active approved replacements: 31.
- Found candidate but not enough accuracy: 33.
- Wrong functional object, reverted: 12.
- Active replacements preserve the original EBF3 nominal mass in the BOM where
  the replacement item is a bulk/general item.

## Decision Categories

- `approved_reuse`: existing KB item performs the EBF3 function at current BOM
  resolution; replacement is active in the BOM.
- `not_enough_accuracy`: a candidate exists, but it is too coarse for the EBF3
  role; original EBF3 leaf remains active.
- `wrong_functional_object`: candidate is not the right kind of object for the
  EBF3 role; original EBF3 leaf remains active.

## Active Approved Replacements

| Original EBF3 leaf | Replacement item | Parent BOM | Qty | EBF3 function | Decision | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| `ebf3_drive_roll_cover_fastener_tab_set` | `fastener_kit_medium` | `bom_ebf3_drive_roll_cover` | 0.12 kg | cover retention hardware | `approved_reuse` | Approved: this is a standard fastening role with no unique EBF geometry retained at this level. |
| `ebf3_realtime_processor_enclosure` | `enclosure_electrical_medium` | `bom_ebf3_realtime_control_processor` | 0.25 kg | realtime processor housing | `approved_reuse` | Approved: this is a non-vacuum control/electrical housing role; cutouts and mounting are normal enclosure details. |
| `ebf3_safety_logic_enclosure` | `enclosure_electrical_medium` | `bom_ebf3_safety_blocking_logic` | 0.25 kg | safety logic housing | `approved_reuse` | Approved: this is a non-vacuum control/electrical housing role; cutouts and mounting are normal enclosure details. |
| `ebf3_spool_brake_adjuster_lock_nut` | `fastener_kit_medium` | `bom_ebf3_spool_brake_adjuster` | 0.03 kg | adjuster lock nut | `approved_reuse` | Approved: this is a standard fastening role with no unique EBF geometry retained at this level. |
| `ebf3_aux_dc_distribution_terminal_set` | `terminal_block_set` | `bom_ebf3_auxiliary_low_voltage_dc_supply.yaml` | 0.7 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_axis_home_sensor_lead_set` | `electrical_wire_and_connectors` | `bom_ebf3_axis_home_sensors.yaml` | 0.08 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_axis_motor_lead_set` | `electrical_wire_and_connectors` | `bom_ebf3_axis_motors.yaml` | 0.8 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_axis_limit_switch_lead_set` | `electrical_wire_and_connectors` | `bom_ebf3_axis_travel_limit_switches.yaml` | 0.05 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_cabin_sacrificial_liner_panel_set` | `panel_or_door_assembly` | `bom_ebf3_cabin_sacrificial_liner.yaml` | 10 kg | protective panel/liner | `approved_reuse` | Approved: this is a passive protective panel/liner role; the generic panel assembly is sufficient at current BOM resolution. |
| `ebf3_heater_supply_output_terminal_set` | `terminal_block_set` | `bom_ebf3_cathode_heater_supply.yaml` | 0.5 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_controls_cabinet_cable_duct_set` | `assembled_cable_harness` | `bom_ebf3_controls_cabinet.yaml` | 0.7 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_controls_cabinet_panel_terminal_set` | `terminal_block_set` | `bom_ebf3_controls_cabinet.yaml` | 1 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_controls_cabinet_door_and_latch` | `panel_or_door_assembly` | `bom_ebf3_controls_cabinet.yaml` | 0.69 kg | cabinet/panel hardware | `approved_reuse` | Approved: this is a cabinet or low-voltage panel role; the generic panel assembly is sufficient at current BOM resolution. |
| `ebf3_emi_filter_terminal_set` | `terminal_block_set` | `bom_ebf3_emi_filter.yaml` | 0.2 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_lv_distribution_terminal_block_set` | `terminal_block_set` | `bom_ebf3_low_voltage_distribution_panel.yaml` | 0.9 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_lv_distribution_panel_plate` | `panel_or_door_assembly` | `bom_ebf3_low_voltage_distribution_panel.yaml` | 0.8 kg | cabinet/panel hardware | `approved_reuse` | Approved: this is a cabinet or low-voltage panel role; the generic panel assembly is sufficient at current BOM resolution. |
| `ebf3_disconnect_switch_housing` | `enclosure_electrical_medium` | `bom_ebf3_main_disconnect_switch.yaml` | 0.6 kg | electrical housing | `approved_reuse` | Approved: this is a non-vacuum control/electrical housing role; cutouts and mounting are normal enclosure details. |
| `ebf3_disconnect_switch_terminal_set` | `terminal_block_set` | `bom_ebf3_main_disconnect_switch.yaml` | 0.3 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_motion_drive_terminal_block_set` | `terminal_block_set` | `bom_ebf3_motion_control_drive_module.yaml` | 0.4 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_multi_channel_output_terminal_set` | `terminal_block_set` | `bom_ebf3_multi_channel_driver_module.yaml` | 0.8 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_power_input_cable_conductor_set` | `assembled_cable_harness` | `bom_ebf3_power_input_cable_gland.yaml` | 0.7 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_power_input_cable_insulation_set` | `assembled_cable_harness` | `bom_ebf3_power_input_cable_gland.yaml` | 0.5 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_rotary_encoder_signal_lead` | `electrical_wire_and_connectors` | `bom_ebf3_rotary_encoder.yaml` | 0.1 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_safety_logic_terminal_block_set` | `terminal_block_set` | `bom_ebf3_safety_blocking_logic.yaml` | 0.25 kg | terminal/power distribution interface | `approved_reuse` | Approved: this is a cabinet/control terminal-distribution function; normal current, voltage, and wire-gauge selection belongs inside the terminal-block item. |
| `ebf3_spatter_shield_panel_set` | `panel_or_door_assembly` | `bom_ebf3_spatter_shielding.yaml` | 1.1 kg | protective panel/liner | `approved_reuse` | Approved: this is a passive protective panel/liner role; the generic panel assembly is sufficient at current BOM resolution. |
| `ebf3_spool_brake_adjuster_screw` | `fastener_kit_medium` | `bom_ebf3_spool_brake_adjuster.yaml` | 0.1 kg | standard fastener function | `approved_reuse` | Approved: this is a standard fastening role with no unique EBF geometry retained at this level. |
| `ebf3_substrate_clamp_screw_set` | `fastener_kit_medium` | `bom_ebf3_substrate_clamp.yaml` | 0.25 kg | standard fastener function | `approved_reuse` | Approved: this is a standard fastening role with no unique EBF geometry retained at this level. |
| `ebf3_visible_camera_signal_cable` | `assembled_cable_harness` | `bom_ebf3_visible_camera.yaml` | 0.15 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_wire_feed_drive_roll_set_screw_or_key` | `fastener_kit_medium` | `bom_ebf3_wire_feed_drive_roll.yaml` | 0.03 kg | standard fastener function | `approved_reuse` | Approved: this is a standard fastening role with no unique EBF geometry retained at this level. |
| `ebf3_wire_feed_encoder_signal_lead` | `electrical_wire_and_connectors` | `bom_ebf3_wire_feed_encoder_sensor.yaml` | 0.08 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |
| `ebf3_wire_feed_motor_lead_set` | `electrical_wire_and_connectors` | `bom_ebf3_wire_feed_gearmotor.yaml` | 0.15 kg | equipment wiring/cable run | `approved_reuse` | Approved: this is ordinary non-HV equipment wiring; gauge, insulation, shielding, and connector selection are normal parameters of the wiring item. |

## Candidate Exists But Not Enough Accuracy

These have a recognizable existing KB candidate, but they are not active
replacements. They remain as EBF3-specific leaves because the candidate is too
coarse for the function or would hide performance requirements.

| EBF3 leaf kept active | Candidate item | Parent BOM | EBF3 function | Decision | Reason |
| --- | --- | --- | --- | --- | --- |
| `ebf3_control_software` | `compiled_firmware_binary` | `bom_ebf3_controls` | software/control logic | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: firmware binary is an artifact, while EBF3 control behavior/interlocks remain functional content. |
| `ebf3_emi_filter_enclosure` | `enclosure_electrical_medium` | `bom_ebf3_emi_filter` | EMI filter housing | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: housing role involves EBF3-specific power, thermal, EMI, voltage-clearance, or service geometry. |
| `ebf3_full_bridge_heat_sink` | `heat_sink_base_machined` | `bom_ebf3_full_bridge_inverter` | inverter power-stage heat removal | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: heat removal is performance-defining and needs thermal resistance, mounting, isolation, and cooling path. |
| `ebf3_heater_supply_heat_sink` | `heat_sink_base_machined` | `bom_ebf3_cathode_heater_supply` | cathode-heater supply heat removal | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: heat removal is performance-defining and needs thermal resistance, mounting, isolation, and cooling path. |
| `ebf3_heater_supply_enclosure` | `enclosure_electrical_medium` | `bom_ebf3_cathode_heater_supply` | cathode-heater supply cabinet/housing | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: housing role involves EBF3-specific power, thermal, EMI, voltage-clearance, or service geometry. |
| `ebf3_multi_channel_heat_sink` | `heat_sink_base_machined` | `bom_ebf3_multi_channel_driver_module` | multi-channel driver thermal path | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: heat removal is performance-defining and needs thermal resistance, mounting, isolation, and cooling path. |
| `ebf3_multi_channel_driver_enclosure` | `enclosure_electrical_medium` | `bom_ebf3_multi_channel_driver_module` | multi-channel driver housing | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: housing role involves EBF3-specific power, thermal, EMI, voltage-clearance, or service geometry. |
| `ebf3_power_electronics_heat_sink_set` | `heat_sink_base_machined` | `bom_ebf3_power_electronics_thermal_management` | power-electronics heat-sink mass set | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: heat removal is performance-defining and needs thermal resistance, mounting, isolation, and cooling path. |
| `ebf3_spool_brake_washer` | `fastener_kit_medium` | `bom_ebf3_wire_feeder` | spool brake washer/friction interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: friction/wear/surface behavior is part of the EBF3 function. |
| `ebf3_adc_module_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_analog_input_adc_module.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |
| `ebf3_cabin_access_door_panel` | `panel_or_door_assembly` | `bom_ebf3_cabin_access_door.yaml` | vacuum cabin wall/access boundary | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this is part of a vacuum cabin boundary, so sealing, leak testing, stiffness, and interface geometry matter. |
| `ebf3_cabin_access_door_hinge_set` | `door_hinge_assembly` | `bom_ebf3_cabin_access_door.yaml` | access-door hinge | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: cabin access hinge must satisfy vacuum-door load, seal compression, and lubrication/material constraints. |
| `ebf3_cabin_access_door_latch_set` | `panel_or_door_assembly` | `bom_ebf3_cabin_access_door.yaml` | vacuum cabin wall/access boundary | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this is part of a vacuum cabin boundary, so sealing, leak testing, stiffness, and interface geometry matter. |
| `ebf3_cabin_wall_panel_set` | `panel_or_door_assembly` | `bom_ebf3_cabin_wall_panels.yaml` | vacuum cabin wall/access boundary | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this is part of a vacuum cabin boundary, so sealing, leak testing, stiffness, and interface geometry matter. |
| `ebf3_can_bus_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_can_bus_interface.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |
| `ebf3_control_computer_io_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_control_computer.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |
| `ebf3_bias_supply_terminal_set` | `terminal_block_set` | `bom_ebf3_control_electrode_bias_supply.yaml` | biased/control terminal interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this terminal role is tied to biased/HV-adjacent behavior, so voltage/creepage assumptions need explicit modeling. |
| `ebf3_data_logger_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_data_logger_timebase.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |
| `ebf3_hv_return_current_monitor_signal_lead` | `electrical_wire_and_connectors` | `bom_ebf3_hv_output_return_current_monitor.yaml` | isolated low-energy sensing lead | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_hv_voltage_divider_shielded_lead` | `electrical_wire_and_connectors` | `bom_ebf3_hv_output_voltage_divider_sensing.yaml` | isolated low-energy sensing lead | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_hv_pressure_relief_valve_body` | `pressure_relief_valve` | `bom_ebf3_hv_tank_pressure_relief.yaml` | HV tank pressure relief | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: tank relief function needs set pressure, fluid compatibility, leak tightness, and service topology. |
| `ebf3_hv_tank_temperature_sensor_lead_set` | `electrical_wire_and_connectors` | `bom_ebf3_hv_tank_temperature_sensor.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_realtime_processor_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_realtime_control_processor.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |
| `ebf3_sensor_interface_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_sensor_interface_module.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |
| `ebf3_positioning_motor_power_conductor_set` | `electrical_wire_and_connectors` | `bom_ebf3_vacuum_compatible_motor_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_motor_cable_insulation_set` | `assembled_cable_harness` | `bom_ebf3_vacuum_compatible_motor_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_motor_cable_shield_set` | `assembled_cable_harness` | `bom_ebf3_vacuum_compatible_motor_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_motor_cable_termination_set` | `assembled_cable_harness` | `bom_ebf3_vacuum_compatible_motor_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_signal_conductor_set` | `electrical_wire_and_connectors` | `bom_ebf3_vacuum_compatible_signal_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_signal_cable_insulation_set` | `assembled_cable_harness` | `bom_ebf3_vacuum_compatible_signal_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_signal_cable_shield_set` | `assembled_cable_harness` | `bom_ebf3_vacuum_compatible_signal_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_positioning_signal_cable_termination_set` | `assembled_cable_harness` | `bom_ebf3_vacuum_compatible_signal_cabling.yaml` | in-chamber or tank-adjacent wiring | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: this wiring is vacuum, oil, HV-sensing, or in-chamber adjacent, so insulation, outgassing, shielding, and isolation matter. |
| `ebf3_wire_feed_control_connector_set` | `connector_electrical_multi_pin` | `bom_ebf3_wire_feed_control_module.yaml` | connector/interface | `not_enough_accuracy` | Candidate found, but not enough accuracy yet: connector pin count, rating, shielding, or environment affects the specific EBF3 board/interface function. |

## Wrong Functional Object

These candidates were removed because they are not the right functional object
for the EBF3 role, even as a coarse replacement.

| EBF3 leaf kept active | Removed candidate | Parent BOM | Decision | Reason |
| --- | --- | --- | --- | --- |
| `ebf3_hv_cable_central_conductor` | `assembled_cable_harness` | `bom_ebf3_hv_cable_to_gun.yaml` | `wrong_functional_object` | HV cable conductor geometry and material are core to high-voltage performance; a complete harness item is the wrong functional object. |
| `ebf3_hv_cable_dielectric_insulation` | `assembled_cable_harness` | `bom_ebf3_hv_cable_to_gun.yaml` | `wrong_functional_object` | Dielectric layer thickness/material/voltage rating define cable feasibility; a generic harness cannot represent this layer. |
| `ebf3_hv_cable_semiconductive_stress_control_layer` | `assembled_cable_harness` | `bom_ebf3_hv_cable_to_gun.yaml` | `wrong_functional_object` | Stress-control layer is a field-grading feature, not a general cable harness. |
| `ebf3_hv_cable_braided_shield` | `assembled_cable_harness` | `bom_ebf3_hv_cable_to_gun.yaml` | `wrong_functional_object` | Shield geometry/termination affects HV safety and EMI; generic harness is not a sufficient function representative. |
| `ebf3_hv_cable_outer_jacket` | `assembled_cable_harness` | `bom_ebf3_hv_cable_to_gun.yaml` | `wrong_functional_object` | Outer jacket material/environmental rating matters for HV cable; generic harness is too broad. |
| `ebf3_hv_bleeder_chain_terminal_set` | `terminal_block_set` | `bom_ebf3_hv_discharge_bleeder_resistor_chain.yaml` | `wrong_functional_object` | HV bleeder terminals need creepage, field shape, and oil/HV compatibility beyond DIN terminal blocks. |
| `ebf3_hv_lead_conductor_set` | `electrical_wire_and_connectors` | `bom_ebf3_internal_hv_leads_terminals.yaml` | `wrong_functional_object` | Internal HV lead conductor geometry and insulation are part of HV design, not ordinary wire stock. |
| `ebf3_hv_lead_support_standoff_set` | `electrical_wire_and_connectors` | `bom_ebf3_internal_hv_leads_terminals.yaml` | `wrong_functional_object` | Support standoffs are insulating supports, not wire/connectors. |
| `ebf3_hv_rounded_terminal_set` | `terminal_block_set` | `bom_ebf3_internal_hv_leads_terminals.yaml` | `wrong_functional_object` | Rounded terminal shape is part of HV field management; terminal blocks are not functionally equivalent. |
| `ebf3_tank_side_bushing_central_conductor` | `electrical_wire_and_connectors` | `bom_ebf3_tank_side_hv_output_bushing.yaml` | `wrong_functional_object` | Bushing central conductor is a feedthrough conductor with field and sealing constraints, not generic wire stock. |
| `ebf3_tank_side_bushing_cable_socket_interface` | `assembled_cable_harness` | `bom_ebf3_tank_side_hv_output_bushing.yaml` | `wrong_functional_object` | Cable socket/interface geometry is a connector/feedthrough feature, not an assembled harness. |
| `ebf3_cabin_wall_panel_seam_set` | `panel_or_door_assembly` | `bom_ebf3_cabin_wall_panels.yaml` | `wrong_functional_object` | The seam set is the vacuum sealing/joining interface between panels, not a panel/door body. |

## Follow-Up Rules

- Do not put a row in active approved replacements unless the replacement is
  good enough for the EBF3 function at current BOM resolution.
- If the judgment says "too coarse", "proxy only", or "performance-defining",
  the row belongs in `not_enough_accuracy`, not active replacement.
- High-voltage field-shaping, vacuum feedthrough, electron-gun geometry,
  precision motion, vacuum boundary sealing, and thermal-performance-defining
  items require dedicated EBF3 leaves unless the existing KB item exposes the
  needed performance requirements.
