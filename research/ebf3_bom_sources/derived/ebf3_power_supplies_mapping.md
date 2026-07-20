# ebf3_power_supplies Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Power supplies leaf items mapped from V2_power_supplies_item_table; no leaf recipes yet to preserve fidelity.

| Source ID | KB item ID | Modeling decision |
| --- | --- | --- |
| PS-1 | `ebf3_power_input_cable_gland` | Incoming utility/input power cable, gland, and cabinet entry hardware. |
| PS-2 | `ebf3_main_disconnect_switch` | Main disconnect switch for isolation and service safety. |
| PS-3 | `ebf3_emi_filter` | EMI filter for reducing high-frequency conducted noise. |
| PS-4 | `ebf3_input_rectifier` | Input rectifier converting AC input to DC bus voltage. |
| PS-5 | `ebf3_dc_link_capacitor_bank` | DC-link capacitor bank for bus energy storage and smoothing. |
| PS-6 | `ebf3_damping_resistor` | Damping resistor or network for power supply transient control. |
| PS-7 | `ebf3_snubber_network` | Snubber network for switching transient suppression. |
| PS-8 | `ebf3_inverter_matching_network` | Impedance matching network for inverter/HV transformer drive. |
| PS-9 | `ebf3_full_bridge_inverter` | Full-bridge inverter power stage for high-frequency transformer drive. |
| PS-10 | `ebf3_control_electrode_bias_supply` | Bias supply for electron-gun control electrode. |
| PS-11 | `ebf3_cathode_heater_supply` | Stabilized cathode heater power supply. |
| PS-12 | `ebf3_accelerating_voltage_dc_supply` | Accelerating high-voltage DC supply output stage. |
| PS-13 | `ebf3_lens_corrector_current_supplies` | Current-regulated supplies for magnetic lens, deflection, and corrector coils. |
| PS-14 | `ebf3_power_supply_control_board` | Power-supply controller board and isolated analog/digital interfaces. |
| PS-15 | `ebf3_power_supply_cabinet_bus_cooling` | Power supply cabinet hardware, busbars, cooling, mounting, and internal wiring. |

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.
