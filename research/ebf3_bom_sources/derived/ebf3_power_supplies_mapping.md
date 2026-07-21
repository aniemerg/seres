# ebf3_power_supplies Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Power supplies leaf items aligned to the source table after
`research/ebf3_bom_sources/organized/power_supplies_level_2_audit.md`; no leaf
recipes yet to preserve fidelity.

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

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.

Deferred/derived functional candidates kept out of the source-table Level-2
presentation:

- `ebf3_damping_resistor`
- `ebf3_snubber_network`
- `ebf3_accelerating_voltage_dc_supply`
- `ebf3_lens_corrector_current_supplies`
- `ebf3_power_supply_control_board`
- `ebf3_power_supply_cabinet_bus_cooling`
