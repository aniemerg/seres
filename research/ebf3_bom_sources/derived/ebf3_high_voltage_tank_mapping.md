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
| HV-3 | `ebf3_sectioned_hv_step_up_transformer` | Sectioned high-voltage step-up transformer assembly in the oil-filled tank. |
| HV-4 | `ebf3_hv_rectifier_stack_tank_side` | High-voltage rectifier stack inside the tank. |
| HV-5 | `ebf3_hv_output_filter_capacitor` | High-voltage output filter capacitor assembly for ripple reduction. |
| HV-6 | `ebf3_internal_hv_leads_terminals` | Oil-side internal high-voltage conductors, straps, studs, and rounded terminals. |
| HV-7 | `ebf3_transformer_insulation_spacers` | Transformer/rectifier/capacitor support spacers and insulation distance maintainers. |
| HV-8 | `ebf3_tank_side_hv_output_bushing` | Tank-side high-voltage output bushing/feedthrough/socket assembly. |
| HV-9 | `ebf3_hv_cable_to_gun` | High-voltage cable carrying accelerating voltage from tank to fixed electron beam gun. |
| HV-10 | `ebf3_hv_tank_fill_drain_ports` | Oil fill, drain, and service ports for HV tank. |
| HV-11 | `ebf3_hv_tank_grounding_terminal` | Grounding terminal and bonding interface for HV tank enclosure. |
| HV-12 | `ebf3_hv_tank_temperature_sensor` | Oil or tank temperature sensing element for protection and control. |
| HV-13 | `ebf3_hv_tank_pressure_relief` | Pressure relief or venting hardware for oil-filled tank safety. |
| HV-14 | `ebf3_hv_tank_oil_level_indicator` | Oil level indicator or sight interface for tank maintenance. |
| HV-15 | `ebf3_hv_tank_mounting_frame` | Mounting frame or bracket set for HV tank installation. |

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.
