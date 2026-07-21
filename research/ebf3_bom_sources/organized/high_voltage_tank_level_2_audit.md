# High Voltage Tank Level-2 Audit

Status: scaffold audit, source-tag cleanup, and first mechanical/interface
child splits completed for current high-voltage tank items.

Purpose:

- Check whether the current `ebf3_high_voltage_tank` children match the
  available high-voltage tank sources before deeper decomposition.
- Identify source-tag or ownership issues that should be fixed before creating
  child BOMs.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/high_voltage_tank/high_voltage_tank_sources.md`
- `research/ebf3_bom_sources/sources/level_2_parts/hv_tank_interface/hv_tank_interface_sources.md`

Related review:

- `research/ebf3_bom_sources/organized/hv_tank_interface_review.md`

## Source Authority Assessment

1. `RAW-BINP-60KV-15KW-HV-TANK` supports the core HV source architecture:
   sectioned transformer, rectifier, output filter capacitors, oil-filled tank,
   silicone oil, transformer temperature/current protection, and HV cable.
2. `LOCAL-EBF3-HV-TANK-TABLE` is user-derived and candidate-only. It is useful
   for proposed interface, service, and protection items, but source row IDs must
   be checked before using them in KB notes.
3. External cable/feedthrough/bushing/transformer-service sources support
   generic component classes but do not make items local-ready.

## Current Scaffold Check

| KB item | Current source tag in note | Audit status | Rationale |
| --- | --- | --- | --- |
| `ebf3_hv_tank_enclosure` | HV-1 | keep | Matches oil-filled tank enclosure concept. |
| `ebf3_hv_transformer_insulating_fluid` | HV-2 | keep | Matches silicon/silicone oil row. |
| `ebf3_hv_section_module_set` | HV-3/HV-4/HV-5 architecture | added | Concise section-module-set model adopted to represent source-backed winding/rectifier/filter section architecture. |
| `ebf3_sectioned_hv_step_up_transformer` | HV-3 functional constituent | keep under section-module set | Represents transformer/winding function inside the section-module set. |
| `ebf3_hv_rectifier_stack_tank_side` | HV-4 functional constituent | keep under section-module set | Represents rectifier function inside the section-module set. |
| `ebf3_hv_output_filter_capacitor` | HV-5 functional constituent | keep under section-module set | Represents output filter capacitance inside the section-module set. |
| `ebf3_internal_hv_leads_terminals` | HV-6 | keep | Matches internal oil-side leads/terminals row. |
| `ebf3_transformer_insulation_spacers` | HV-7 | keep | Matches transformer insulation/spacer row. |
| `ebf3_tank_side_hv_output_bushing` | HV-8 | keep | Matches tank-side HV bushing/feedthrough/socket row. |
| `ebf3_hv_cable_to_gun` | HV-9 | keep | Matches HV cable to fixed electron beam gun row. |
| `ebf3_hv_discharge_bleeder_resistor_chain` | HV-10 | added | Added scaffold item for visible HV-10 discharge/bleeder resistor chain row. |
| `ebf3_hv_output_voltage_divider_sensing` | HV-11 | added | Added scaffold item for visible HV-11 voltage divider/output voltage sensing row. |
| `ebf3_hv_output_return_current_monitor` | HV-12 | added | Added scaffold item for visible HV-12 output/return current monitor row. |
| `ebf3_hv_tank_fill_drain_ports` | HV-13 split | corrected | Visible table row HV-10 is discharge/bleeder resistor chain; fill/drain/service hardware appears under HV-13. |
| `ebf3_hv_tank_grounding_terminal` | HV-15 partial | corrected | Visible table row HV-11 is voltage divider/output voltage sensing; tank grounding/shielding/service interlock appears under HV-15. |
| `ebf3_hv_tank_temperature_sensor` | HV-14 | corrected | Visible table row HV-12 is output/return current monitor; temperature sensing appears under HV-14. |
| `ebf3_hv_tank_pressure_relief` | HV-13 | partial split | Pressure relief appears within HV-13 oil service/level/pressure-relief hardware, but current KB split separates pressure relief from fill/drain/level. |
| `ebf3_hv_tank_oil_level_indicator` | HV-13 split | corrected | Visible table row HV-14 is temperature sensing; oil level indicator appears within HV-13. |
| HV tank mounting frame | derived candidate | deferred / not in KB | Visible table row HV-15 is tank grounding/shielding/service interlock. No source row or external source currently confirms a separate HV tank mounting-frame assembly for this model. |

## Missing Or Misrepresented Candidate Rows

The current KB scaffold does not separately represent these visible
`LOCAL-EBF3-HV-TANK-TABLE` rows:

| Source row | Candidate | Current representation | Audit decision |
| --- | --- | --- | --- |
| HV-10 | HV discharge / bleeder resistor chain | `ebf3_hv_discharge_bleeder_resistor_chain` | Added as unresolved scaffold item; no child BOM or recipe. |
| HV-11 | HV voltage divider / output voltage sensing hardware | `ebf3_hv_output_voltage_divider_sensing` | Added as unresolved scaffold item; controls boundary remains. |
| HV-12 | HV output or return current monitor | `ebf3_hv_output_return_current_monitor` | Added as unresolved scaffold item; electrical return boundary remains. |
| HV-13 | Oil service, level, pressure-relief hardware | Split into fill/drain, pressure relief, oil level indicator | Split is plausible but source tags in notes need cleanup. |
| HV-14 | Oil and HV transformer temperature sensing hardware | `ebf3_hv_tank_temperature_sensor` | Existing item should be retagged to HV-14. |
| HV-15 | Tank grounding, shielding, and service interlock hardware | `ebf3_hv_tank_grounding_terminal` partially | Existing item should be retagged to HV-15; shielding/interlock not fully represented. |

## Current KB Action

- Added child BOMs for clear tank mechanical/service/interface assemblies:
  enclosure, internal HV leads and terminals, transformer insulation spacers,
  tank-side HV output bushing, fill/drain ports, grounding terminal, pressure
  relief, and oil-level indicator.
- Source-tag cleanup has added the missing HV-10/HV-11/HV-12 scaffold items and
  corrected notes for existing HV-13/HV-14/HV-15-derived items.
- Use `hv_tank_interface_review.md` for HV tank/gun interface ownership.
- Keep resistor chains, voltage-divider sensing, current monitor, temperature
  sensing, shielding, service interlock, and transformer/rectifier internals
  unresolved until their electrical topology is selected.

## Applied Child Splits

| HV tank parent | Child BOM | Current split |
| --- | --- | --- |
| `ebf3_hv_tank_enclosure` | `bom_ebf3_hv_tank_enclosure` | shell, lid, lid seal |
| `ebf3_internal_hv_leads_terminals` | `bom_ebf3_internal_hv_leads_terminals` | HV lead conductors, rounded terminals, local standoffs |
| `ebf3_transformer_insulation_spacers` | `bom_ebf3_transformer_insulation_spacers` | insulation barriers and spacer posts |
| `ebf3_tank_side_hv_output_bushing` | `bom_ebf3_tank_side_hv_output_bushing` | conductor, insulator body, mounting flange, cable socket interface, and local field-grading shield marker |
| `ebf3_hv_tank_fill_drain_ports` | `bom_ebf3_hv_tank_fill_drain_ports` | fill port, drain valve, service plugs |
| `ebf3_hv_tank_grounding_terminal` | `bom_ebf3_hv_tank_grounding_terminal` | tank ground lug and bonding anchor |
| `ebf3_hv_tank_pressure_relief` | `bom_ebf3_hv_tank_pressure_relief` | relief valve body and seal |
| `ebf3_hv_tank_oil_level_indicator` | `bom_ebf3_hv_tank_oil_level_indicator` | sight window, indicator body, indicator seal |

## Batch Child Split Review

| Parent scope | Current status | Rationale |
| --- | --- | --- |
| Tank enclosure | adopt / detail deferred | Oil-filled tank evidence supports a physical enclosure. Shell, lid, and lid seal are retained as package children; internal supports, wall thickness, welding, oil compatibility, and test procedure remain unresolved. |
| Internal HV leads and terminals | adopt / detail deferred | BINP supports oil-side HV source internals; rounded terminals and support standoffs preserve HV-clearance/corona concerns without selecting geometry. |
| Transformer insulation spacers | adopt / detail deferred | BINP supports sectioned transformer architecture and insulation spacing. Barrier and spacer-post children are retained, but dielectric material and field-stress design remain unresolved. |
| Tank-side HV output bushing | adopt / detail deferred | Bushing/feedthrough sources support conductor, insulation, mounted barrier, and field-grading concerns. The child BOM now includes a field-grading marker, while exact cable socket/termination geometry and field-control shape remain unresolved. |
| Fill/drain, pressure relief, oil-level indicator | adopt / detail deferred | Transformer service sources support fluid level, temperature, and pressure/service hardware classes. Exact valve, gauge, seal, and service procedure remain unresolved. |
| Grounding terminal | adopt / split-boundary guarded | Tank protective bonding is real and distinct from beam-current return or HV return. Full return topology and service interlock remain outside this child BOM. |
| Resistor, voltage-divider, current-monitor, temperature-sensor packages | adopt package split / electrical detail deferred | These are real HV sensing/protection functions from the table and comparable sources. Component values, isolation, controls acquisition, and return-leg placement remain unresolved. |
| Transformer insulating fluid | keep leaf | Fluid is a material/consumable item, not an assembly to split at this stage. |

## Next Work

1. HV electrical-interface review for HV-10/HV-11/HV-12, controls, power
   supplies, current return, and interlocks is recorded in
   `research/ebf3_bom_sources/organized/hv_electrical_interface_review.md`.
2. HV oil-service/protection review for HV-13/HV-14/HV-15 is recorded in
   `research/ebf3_bom_sources/organized/hv_tank_service_protection_review.md`.
3. HV tank core review for HV-3/HV-4/HV-5/HV-6/HV-7 is recorded in
   `research/ebf3_bom_sources/organized/hv_tank_core_decomposition_plan.md`;
   it adopts the concise `ebf3_hv_section_module_set` model.
4. HV tank interface hardware review for HV-8/HV-9 is recorded in
   `research/ebf3_bom_sources/organized/hv_tank_interface_hardware_plan.md`.
5. Keep HV tank mounting frame deferred unless a source row, installation layout,
   or external source confirms it as a separate modeled assembly.
