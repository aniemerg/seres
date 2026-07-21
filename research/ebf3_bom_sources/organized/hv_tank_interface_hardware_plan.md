# HV Tank Interface Hardware Plan

Status: combined Level-2 interface-hardware planning with tank-side bushing,
main HV cable, and gun-side HV-input package splits completed.

Purpose:

- Review HV-8 tank-side bushing and HV-9 HV cable together with the already
  reviewed FG-12 gun-side HV input.
- Decide whether enough source support exists to split bushing/cable
  terminations now.

Parent/current items:

- `ebf3_tank_side_hv_output_bushing` (HV-8)
- `ebf3_hv_cable_to_gun` (HV-9)
- `ebf3_gun_hv_input` (FG-12, cross-reference only)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_tank_interface/hv_tank_interface_sources.md`

## Source Evidence And Use

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "voltage cable"
- "oil-filled tank"

Use:

- Supports the existence of a main HV cable and oil-filled tank interface.
- Does not expose bushing/socket/termination geometry.

### RAW-EBF-US-PATENT

Evidence:

- "high Voltage power cable"
- "electron beam gun"
- "high Voltage power supply"

Use:

- Supports the tank-to-gun cable boundary.
- Does not split tank-side versus gun-side terminations.

### WEB-HIVOLT-XRAY-EBEAM-CABLE

Evidence:

- "E Beam cables"
- "EPR or Silicone dielectric"
- "semiconductive layers"
- "braided shield"

Use:

- Supports HV cable as a composite assembly.
- Does not justify child BOM before cable type and connector geometry are known.

### WEB-CERAMTEC-FEEDTHROUGH-PDF

Evidence:

- "High Voltage to 100 KV"
- "hermetic seal"
- "electrical isolation"

Use:

- Supports bushing/feedthrough function for HV-8/FG-12.
- Does not assign ceramic body to HV-8 versus FG-12/FG-13.

### WEB-GE-VERNOVA-OIL-AIR-BUSHING

Evidence:

- "oil impregnated paper insulation"
- "upper part in open air"
- "lower part immersed in the transformer oil"

Use:

- Supports oil-to-external bushing concepts and field-grading concerns.
- Does not directly map to a compact EBF3 tank-to-gun cable connector.

## Decision Matrix

| Candidate/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Tank-side bushing body/feedthrough | parent assembly | HV-8 | `ebf3_tank_side_hv_output_bushing` | Function supported, with child package markers for the minimum tank-side interface structure. |
| Bushing conductor | adopted / detail deferred | HV-8 | `ebf3_tank_side_bushing_central_conductor` | Feedthrough/bushing sources require a conductor path across an insulated tank boundary. Material, diameter, and termination remain unresolved. |
| Bushing insulation body | adopted / detail deferred | HV-8 | `ebf3_tank_side_bushing_insulator_body` | Feedthrough/bushing sources support an insulating barrier. Ceramic/OIP choice, creepage, and field-stress design remain unresolved. |
| Bushing mounting flange/housing | adopted / detail deferred | HV-8 | `ebf3_tank_side_bushing_mounting_flange` | A tank-wall bushing needs a mechanical mounting/sealing interface. Exact flange, gasket, and fastener geometry remain unresolved. |
| Tank-side cable socket/interface | adopted / detail deferred | HV-8 / HV-9 | `ebf3_tank_side_bushing_cable_socket_interface` | Needed to keep the tank-side cable interface visible without placing it in the main cable body. Connector family and stress-control transition remain unresolved. |
| Field grading/corona shield | modeled / detail deferred | HV-8 / FG-12 / FG-13 | `ebf3_tank_side_bushing_field_grading_shield`; gun-side marker under FG-13 | Real HV concern. Current BOM uses interface-local markers on the tank-side bushing and gun-side HV insulator; final geometry and potential connection remain unresolved. |
| Cable body | parent assembly | HV-9 | `ebf3_hv_cable_to_gun` | Cable is main inter-subsystem transmission item owned by the HV tank. |
| Cable conductor/dielectric/shield/jacket children | adopted / detail deferred | HV-9 | `ebf3_hv_cable_central_conductor`, `ebf3_hv_cable_dielectric_insulation`, `ebf3_hv_cable_semiconductive_stress_control_layer`, `ebf3_hv_cable_braided_shield`, `ebf3_hv_cable_outer_jacket` | Hivolt supports e-beam/x-ray HV cable construction classes. Material ratings, dimensions, and termination treatments remain deferred. |
| Tank-side cable termination | modeled / detail deferred | HV-8 / HV-9 | `ebf3_tank_side_bushing_cable_socket_interface` | The tank-side receiving interface is represented under HV-8; exact connector/socket geometry remains unresolved. |
| Gun-side cable termination | modeled / detail deferred | HV-9 / FG-12 | `ebf3_gun_hv_input_receiving_terminal` | The gun-side receiving interface is represented under FG-12; exact connector/socket geometry remains unresolved. |

## KB Action

- Create `bom_ebf3_hv_cable_to_gun` for cable layers only.
- Create `bom_ebf3_tank_side_hv_output_bushing` for the minimum tank-side
  package split: conductor, insulator body, mounting flange, and cable socket
  interface.
- Keep tank-side and gun-side cable terminations out of the cable BOM. The
  gun-side receiving terminal is under FG-12; tank-side connector/socket remains
  represented only as an unresolved socket/interface marker under HV-8.
- Keep final field-grading/corona-shield geometry and potential connections
  deferred.

## Manufacturing Readiness

No interface hardware item is local-ready. Cable rating, connector geometry,
creepage, oil compatibility, insulation system, shielding/grounding, field
grading, and HV test procedure need a later supplier/design review.
