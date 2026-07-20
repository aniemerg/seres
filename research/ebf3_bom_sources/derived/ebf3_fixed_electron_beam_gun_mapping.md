# EBF3 Fixed Electron Beam Gun Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

User-derived table: `research/ebf3_bom_sources/organized/V2_fixed_electron_beam_gun_item_table.pdf`

Initial KB mapping:

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

Masses are first-pass allocation values constrained to preserve the existing
`ebf3_fixed_electron_beam_gun` subsystem mass of 13 kg. The FG leaf items are
intentionally left without local recipes for now: closure would be premature and
would hide unresolved material, precision, vacuum, high-voltage, and
high-temperature manufacturing questions. Next refinement should decompose each
assembly or single-material part until the leaf nodes can be connected to
specific, source-supported local manufacturing routes.
