# ebf3_high_voltage_tank Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

High voltage tank leaf items mapped from V2_high_voltage_tank_item_table; no leaf recipes yet to preserve fidelity.

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
| derived | `ebf3_hv_tank_mounting_frame` | Mounting frame or bracket set inferred for HV tank installation; not a direct visible HV table row. |

Mapping corrected during
`research/ebf3_bom_sources/organized/high_voltage_tank_level_2_audit.md`.
Masses are first-pass allocations constrained to the current subsystem mass.
Leaf items intentionally have no local recipes yet.
