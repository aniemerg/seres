# High Voltage Tank Unresolved Items

Status: tracker for unresolved HV tank decomposition and interface decisions.

Purpose:

- Keep unresolved HV tank candidates visible without blocking progress.
- Avoid reintroducing source-tag mismatches or duplicate gun/HV tank boundary
  items.

Source plans:

- `research/ebf3_bom_sources/organized/hv_tank_interface_review.md`
- `research/ebf3_bom_sources/organized/high_voltage_tank_level_2_audit.md`
- `research/ebf3_bom_sources/organized/hv_electrical_interface_review.md`
- `research/ebf3_bom_sources/organized/hv_grounding_return_review.md`
- `research/ebf3_bom_sources/organized/hv_tank_service_protection_review.md`
- `research/ebf3_bom_sources/organized/hv_tank_core_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/hv_tank_interface_hardware_plan.md`

## Register

| ID | Candidate | Status | Applies to | Blocker / reason not modeled now | Next unblock condition | Source plan |
| --- | --- | --- | --- | --- | --- | --- |
| HV-D-001 | Separate gun-side oil volume | defer | FG-18 / HV tank | Main tank oil is represented by HV-2; separate gun oil package not confirmed. | Source separate gun-side oil volume. | HV tank interface |
| HV-D-002 | Repeated individual HV section modules | defer | `ebf3_hv_section_module_set` | Concise section-module-set model adopted; repeated section count is intentionally hidden until topology is selected. | Source/select EBF3 section count and topology. | HV tank core |
| HV-D-003 | Transformer winding pack | defer | HV-3 / section module set | Winding exists inside section source, but geometry/count unresolved. | Source winding design. | HV tank core |
| HV-D-004 | Half-bridge rectifier per section | defer | HV-4 / section module set | Section-module-set model adopted, but detailed per-section rectifier split remains unresolved. | Source rectifier section design and ratings. | HV tank core |
| HV-D-005 | Output filter capacitors per section | defer | HV-5 / section module set | Section-module-set model adopted, but detailed per-section capacitor split remains unresolved. | Source capacitor section design and ratings. | HV tank core |
| HV-D-006 | Additional final output capacitor | defer | HV-5 | Comparable 30 kW source mentions additional capacitor; EBF3 topology unknown. | Source selected HV tank topology. | HV tank core |
| HV-D-007 | Diode/equalizing resistor/capacitor dielectric children | defer | HV-4/HV-5 | Component-level split needs ratings and architecture. | Electrical design/material readiness review. | HV tank core |
| HV-D-008 | Detailed oil-side leads/rounded terminals | defer | HV-6 | Current leaf is sufficient until layout is sourced. | Source oil-side layout. | HV tank core |
| HV-D-009 | Detailed spacer/barrier shapes | defer | HV-7 | Spacer function supported, geometry/material not sourced. | Source transformer insulation design. | HV tank core |
| HV-D-010 | Fill/drain valve children | defer | HV-13 | Service hardware real, but valve/thread/seal details unknown. | Oil-service material/process review. | HV service/protection |
| HV-D-011 | Pressure relief valve child | defer | HV-13 | Function real, rating/type unknown. | Source tank pressure-relief specification. | HV service/protection |
| HV-D-012 | Oil level gauge child | defer | HV-13 | Gauge class real, type unknown. | Source tank level indicator design. | HV service/protection |
| HV-D-013 | Temperature sensor RTD/thermistor child | defer | HV-14 | Primary sensor exists, type/feedthrough unresolved. | Source sensor construction. | HV service/protection |
| HV-D-014 | Enclosure shielding/bonding hardware | defer | HV-15 | Overlaps grounding terminal/enclosure. | Source shielding/bonding layout. | HV service/protection |
| HV-D-015 | Physical service interlock switch | defer / split_boundary | HV-15 / controls | Interlock concept real, physical switch location unknown. | Source switch location or cabinet layout. | HV service/protection |
| HV-D-016 | Manual discharge point | defer | HV-15 / HV-10 | May duplicate bleeder/discharge chain. | Source service procedure. | HV service/protection |
| HV-D-017 | Bushing conductor/insulation children | defer | HV-8 | Bushing function real, geometry unknown. | Source selected bushing/feedthrough design. | HV interface hardware |
| HV-D-018 | Field grading/corona shield | defer | HV-8 / FG-12 / FG-13 | Tank-side versus gun-side assignment unknown. | Source interface geometry. | HV interface hardware |
| HV-D-019 | Cable conductor/dielectric/shield/jacket children | defer | HV-9 | Cable material classes known, selected cable unknown. | Source cable specification. | HV interface hardware |
| HV-D-020 | Tank-side and gun-side cable terminations | defer / split_boundary | HV-8 / HV-9 / FG-12 | Connector/socket geometry unknown. | Source termination design. | HV interface hardware |
| HV-D-021 | HV output voltage divider internals | defer | HV-11 | Divider function kept as leaf; ratios/ratings unknown. | Electrical design review. | HV electrical interface |
| HV-D-022 | HV current monitor sensor type | defer | HV-12 | Shunt/CT/Hall/return-leg placement remains unresolved after boundary review. | Source or select current-monitor topology and ratings. | HV electrical interface; HV grounding return |
| HV-D-023 | Global grounding/current-return architecture | split_boundary / defer | HV tank / power supplies / gun / positioning / controls | Boundary model is documented, but physical return topology is not source-fixed. | Source/select external return conductor, cabinet return bus, and platform connection topology. | HV grounding return |

## Next Work

1. Use `hv_grounding_return_review` before changing current-monitor,
   beam-return, power-supply return, or controls acquisition items.
2. Defer material/process readiness for valves, gauges, bushings, cable, spacers,
   transformer windings, rectifier stacks, and capacitor internals.
