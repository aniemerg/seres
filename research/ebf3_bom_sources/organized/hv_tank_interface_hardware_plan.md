# HV Tank Interface Hardware Plan

Status: combined Level-2 interface-hardware planning completed.

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
| Tank-side bushing body/feedthrough | keep leaf | HV-8 | `ebf3_tank_side_hv_output_bushing` | Function supported, geometry unresolved. |
| Bushing conductor | defer | HV-8 | None | Generic feedthrough/bushing feature; no EBF3 geometry. |
| Bushing ceramic/OIP insulation | defer | HV-8 | None | Source supports insulation class, not specific part split. |
| Field grading/corona shield | defer | HV-8 / FG-12 / FG-13 | None | Real concern, but tank-side/gun-side ownership unknown. |
| Cable body | keep leaf | HV-9 | `ebf3_hv_cable_to_gun` | Cable is main inter-subsystem transmission item. |
| Cable conductor/dielectric/shield/jacket children | defer | HV-9 | None | Hivolt supports classes, but cable selection and dimensions are unknown. |
| Tank-side cable termination | defer | HV-8 / HV-9 | None | Needs connector/socket geometry. |
| Gun-side cable termination | split_boundary / defer | HV-9 / FG-12 | `ebf3_gun_hv_input` remains receiving assembly | Gun owns receiving input; termination split needs source geometry. |

## KB Action

- Do not create child BOMs for HV-8 or HV-9 in this pass.
- Keep HV-8 and HV-9 as unresolved interface leaves.
- Update notes to point to this plan and make termination/field-grading defers
  explicit.

## Manufacturing Readiness

No interface hardware item is local-ready. Cable rating, connector geometry,
creepage, oil compatibility, insulation system, shielding/grounding, field
grading, and HV test procedure need a later supplier/design review.
