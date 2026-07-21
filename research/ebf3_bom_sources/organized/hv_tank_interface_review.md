# HV Tank Interface Review

Status: boundary review completed for the current fixed-gun and high-voltage
tank scaffold.

Current interface entry point:
`research/ebf3_bom_sources/organized/ebf3_interface_architecture.md`.

Purpose:

- Define the interface between `ebf3_high_voltage_tank` and
  `ebf3_fixed_electron_beam_gun` before decomposing HV tank internals.
- Prevent duplicate modeling of cable terminations, ceramic feedthroughs,
  silicone oil, bushings, gun-side oil volumes, and grounding paths.

Parent/interface items:

- `ebf3_hv_tank_enclosure`
- `ebf3_hv_transformer_insulating_fluid`
- `ebf3_internal_hv_leads_terminals`
- `ebf3_tank_side_hv_output_bushing`
- `ebf3_hv_cable_to_gun`
- `ebf3_gun_hv_input` (FG-12)
- `ebf3_gun_hv_insulator` (FG-13)
- `ebf3_gun_side_oil_tank` (FG-18)
- `ebf3_hv_tank_grounding_terminal`

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_tank_interface/hv_tank_interface_sources.md`

Related planning files:

- `research/ebf3_bom_sources/organized/hv_gun_side_insulation_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/fixed_electron_beam_gun_unresolved_items.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-BINP-60KV-15KW-HV-TANK` is the strongest source for the main high-voltage
   tank: sectioned transformer, rectifier, output filter capacitors, oil-filled
   tank, silicone oil, transformer temperature/current protection, and HV cable.
2. `RAW-BINP-60KEV-30KW` supports a comparable combined gun/source context and
   lists gun-side oil tank, high-voltage insulator, and high-voltage input in
   the electron-optical legend.
3. `RAW-EBF-US-PATENT` supports that EBF3 connects the electron beam gun to a
   high-voltage power supply by a high-voltage power cable.
4. Hivolt, CeramTec, and GE Vernova sources support cable, feedthrough, bushing,
   and field-grading concepts generically. They do not assign these details to
   the EBF3 tank or gun by themselves.
5. Maddox supports transformer service/monitoring functions generically. It is
   used only for later HV tank service hardware review, not for gun-side HV
   ownership.
6. User-derived HV and FG tables introduce candidate components but cannot by
   themselves justify child BOM creation.

## Source Evidence And Use

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "Sectioned high-voltage transformer"
- "winding, half-bridge rectifier and output filter capacitors"
- "oil-filled tank"
- "diameter 600mm, high 800mm"
- "The silicon oil [1] is used"
- "voltage cable"
- "temperature of transformer and input current"

Use:

- Supports assigning the main oil-filled enclosure, main insulating fluid,
  transformer, rectifier, filter capacitors, internal oil-side HV conductors,
  transformer protection sensing, and main HV cable to the high-voltage tank
  subsystem.
- Does not justify a second silicone-oil item under the gun-side oil tank unless
  separate gun-side oil volume evidence appears.

### RAW-BINP-60KEV-30KW

Evidence:

- "1-oil tank"
- "2-high voltage insulator"
- "14-high voltage input"
- "The silicon oil [2] is used"
- "Cathode heater with stabilized current"

Use:

- Supports keeping FG-12/FG-13/FG-18 visible on the fixed-gun side.
- Does not prove that FG-18 is a separate physical oil tank rather than the oil
  volume around a comparable HV transformer/gun package.

### RAW-EBF-US-PATENT

Evidence:

- "high Voltage power cable"
- "electron beam gun"
- "high Voltage power supply"

Use:

- Supports `ebf3_hv_cable_to_gun` as the main inter-subsystem transmission item.
- Does not define tank-side versus gun-side termination geometry.

### WEB-HIVOLT-XRAY-EBEAM-CABLE

Evidence:

- "E Beam cables"
- "EPR or Silicone dielectric"
- "semiconductive layers"
- "braided shield"
- "complete cable assemblies"

Use:

- Supports treating the HV cable as a composite cable assembly rather than a
  single conductor.
- Does not justify splitting terminations before tank/gun connector geometry is
  sourced.

### WEB-CERAMTEC-FEEDTHROUGH-PDF

Evidence:

- "transfer of electrical power"
- "hermetic seal"
- "electrical isolation"
- "High Voltage to 100 KV"

Use:

- Supports feedthrough/bushing concepts for tank-side and gun-side HV interfaces.
- Does not decide whether ceramic insulation belongs to FG-12, FG-13, or HV-8.

### WEB-CERAMTEC-CERAMASEAL-FEEDTHROUGHS

Evidence:

- "High-voltage feedthroughs"
- "20 to 100 kV"
- "alumina ceramics"

Use:

- Supports high-voltage ceramic feedthrough material/function class.
- Material support does not create child geometry.

### WEB-GE-VERNOVA-OIL-AIR-BUSHING

Evidence:

- "radial and longitudinal electrical gradient"
- "between the conductor and the fixing flange"
- "grounded"
- "impregnated with oil"

Use:

- Supports field grading and oil-to-external bushing concerns on the tank side.
- Does not map directly to the EBF3 gun-side HV input.

### WEB-MADDOX-TRANSFORMER-GAUGES

Evidence:

- "liquid level gauge"
- "fluid level inside your transformer"
- "temperature gauge"
- "pressure vacuum gauge"

Use:

- Supports later review of tank service and monitoring hardware.
- Not used to create fixed-gun interface children.

## Boundary Decision Matrix

| Interface/function | Decision | Owning item/subsystem | Rationale |
| --- | --- | --- | --- |
| Main oil-filled HV generation tank | Keep in HV tank | `ebf3_hv_tank_enclosure` | BINP HV source directly supports oil-filled transformer tank. |
| Main insulating fluid / silicone oil | Keep in HV tank | `ebf3_hv_transformer_insulating_fluid` | BINP HV source directly states silicon oil for the main oil-filled transformer tank. Do not duplicate under FG-18. |
| Gun-side oil volume/package | Boundary marker only | `ebf3_gun_side_oil_tank` | BINP gun legend names an oil tank, but ownership and separation from main tank remain unclear. |
| Internal oil-side HV leads/terminals | Keep in HV tank | `ebf3_internal_hv_leads_terminals` | These connect tank internals: transformer, rectifier, filter, bushing. |
| Tank-side HV bushing/feedthrough/socket | Keep in HV tank | `ebf3_tank_side_hv_output_bushing` | Tank wall/oil-side to cable interface belongs to the tank package. |
| Main HV cable body | Keep in HV tank | `ebf3_hv_cable_to_gun` | Boundary policy assigns main inter-subsystem transmission cable to the source package. |
| Tank-side cable termination | Defer under HV tank interface | `ebf3_tank_side_hv_output_bushing` / `ebf3_hv_cable_to_gun` | Real feature, but geometry not sourced enough to split. |
| Gun-side cable termination / receiving terminal | Defer under gun input | `ebf3_gun_hv_input` | Gun owns receiving/input hardware, but conductor/flange/ceramic split is not sourced. |
| Gun HV ceramic feedthrough body | Split-boundary / defer | `ebf3_gun_hv_input` / `ebf3_gun_hv_insulator` | Do not duplicate FG-13 inside FG-12 until source clarifies standalone insulator versus feedthrough body. |
| Gun high-voltage structural insulator | Keep as unresolved fixed-gun item | `ebf3_gun_hv_insulator` | BINP gun legend names high-voltage insulator separately. |
| Field grading / corona shield | Defer | HV-8 / FG-12 / FG-13 | Real HV design function, but needs geometry to assign tank-side versus gun-side. |
| HV tank grounding terminal | Keep in HV tank | `ebf3_hv_tank_grounding_terminal` | Tank enclosure grounding belongs to HV tank; beam/current return paths need separate review. |
| Beam/current return path | Split-boundary / defer | HV tank / power supplies / gun / positioning | Do not hide return path inside tank grounding or gun column. |

## KB Note Updates

- Tighten HV-8, HV-9, FG-12, FG-13, FG-18, HV-2, HV-6, and tank-grounding notes
  to point to this review and preserve the tank/gun split.
- FG-12 now has a minimal gun-side input child BOM in
  `research/ebf3_bom_sources/organized/hv_gun_side_insulation_decomposition_plan.md`.
  This does not change HV tank ownership of the main cable or tank-side bushing.
- Do not create child BOMs or recipes for HV-8/HV-9 in this pass.
- Do not rename IDs in this pass.

## Resolved / Still Unresolved Rows

Updates for
`research/ebf3_bom_sources/organized/fixed_electron_beam_gun_unresolved_items.md`:

- FG-D-052 is now `modeled / detail deferred`: central conductor is modeled
  under FG-12, while material, clearance, and joint details remain unresolved.
- FG-D-053 remains `split_boundary / defer`: FG-12 versus FG-13 ceramic
  ownership still unresolved.
- FG-D-054 is now `modeled / detail deferred`: local FG-12 flange/housing is
  modeled, while chamber/gun-column flange overlap remains unresolved.
- FG-D-055 is now split: main HV cable stays in HV tank; gun-side receiving
  terminal is modeled under FG-12; tank-side termination remains deferred.
- FG-D-056 remains `defer`: field grading/corona shield needs geometry.
- FG-D-057 remains `defer`: standalone HV insulator geometry unresolved.
- FG-D-058 remains `defer`: metallized ends/collars remain generic practice.
- FG-D-059 remains `defer`: FG-18 still cannot be decomposed as a separate oil
  volume.
- FG-D-060 remains `defer`: no separate gun-side oil shell/lid evidence.
- FG-D-061 remains `split_boundary / defer`: main silicone oil belongs to HV
  tank; add gun oil only if separate volume is confirmed.
- FG-D-062 remains `defer`: oil-compatible seals/supports need package source.
- FG-D-063 remains `split_boundary / defer`: grounding/return interface needs a
  separate electrical interface review.

## Next Action

The Level-2 scaffold audit and source-tag cleanup are recorded in
`research/ebf3_bom_sources/organized/high_voltage_tank_level_2_audit.md`.
Before decomposing HV protection/control hardware, run an electrical-interface
review for HV-10/HV-11/HV-12, controls, power supplies, current return, and
interlocks.
