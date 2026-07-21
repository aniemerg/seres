# HV Tank Service And Protection Review

Status: combined Level-2 review completed for HV-13/HV-14/HV-15 service and
protection items.

Purpose:

- Review HV tank oil-service and protection items together rather than one leaf
  at a time.
- Preserve the split between physical tank hardware and controls/interlock
  logic.

Parent/current items:

- `ebf3_hv_tank_fill_drain_ports` (HV-13 split)
- `ebf3_hv_tank_pressure_relief` (HV-13 split)
- `ebf3_hv_tank_oil_level_indicator` (HV-13 split)
- `ebf3_hv_tank_temperature_sensor` (HV-14)
- `ebf3_hv_tank_grounding_terminal` (HV-15 partial)
- `ebf3_safety_blocking_logic` (controls)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_tank_service_protection/hv_tank_service_protection_sources.md`

## Source Evidence And Use

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "temperature of transformer"
- "input current"
- "oil-filled tank"

Use:

- Supports temperature/protection sensing for the oil-filled HV tank.
- Does not expose service port, level gauge, pressure relief, grounding, or
  interlock construction.

### LOCAL-EBF3-HV-TANK-TABLE

Evidence:

- HV-13 includes fill port, drain port, sampling valve, level gauge, pressure
  relief valve, bleed/vent port, and expansion bellows/bladder candidates.
- HV-14 includes RTD/thermistor, oil probe, sealed feedthrough, input-current
  sensor, and signal leads candidates.
- HV-15 includes ground stud, grounding strap, enclosure shield, lid/service
  interlock switch, service panel terminal, and manual discharge point
  candidates.

Use:

- Introduces candidate service/protection children only.
- Does not justify local-ready parts or detailed child BOMs by itself.

### WEB-EATON-PAD-MOUNTED-TRANSFORMER

Evidence:

- "Drain valve with sampler"
- "Automatic pressure relief valve"
- "Liquid level gauge"
- "Stainless steel 1-hole ground pads"

Use:

- Supports the current split into fill/drain, pressure relief, oil level, and
  grounding hardware as real liquid-filled transformer service features.
- Does not make EBF3 geometry, thread size, seal material, or rating known.

### WEB-EATON-PAD-MOUNTED-INSTRUCTIONS

Evidence:

- "liquid level gauge"
- "Pull ring on pressure relief valve"
- "venting transformer to zero pressure"

Use:

- Supports pressure relief and liquid-level service as safety-relevant tank
  hardware.

### WEB-MADDOX-TRANSFORMER-GAUGES

Evidence:

- "liquid level gauge"
- "temperature gauge"
- "pressure vacuum gauge"

Use:

- Supports transformer service/monitoring gauge classes.
- Does not assign final component type or supplier.

### WEB-SPELLMAN-SL2KW-MANUAL

Evidence:

- "must always be grounded"
- "load and power supply is discharged"

Use:

- Supports grounding/discharge safety concerns for HV equipment.
- Does not prove physical HV tank service interlock details.

### WEB-SPELLMAN-EXTERNAL-INTERLOCKS

Evidence:

- "external interlock points"
- "HV ON mode"
- "low impedance connection"

Use:

- Supports interlock loop concepts.
- Decision logic stays in controls; physical switch location remains deferred.

## Decision Matrix

| Candidate/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Fill/drain/sampling service ports | keep leaf | HV-13 | `ebf3_hv_tank_fill_drain_ports` | Eaton and LOCAL table support service ports; detailed valves/seals remain unresolved. |
| Pressure relief / vent hardware | keep leaf | HV-13 | `ebf3_hv_tank_pressure_relief` | Eaton supports pressure relief hardware; exact type/rating remains unresolved. |
| Oil level indicator / gauge | keep leaf | HV-13 | `ebf3_hv_tank_oil_level_indicator` | Eaton/Maddox support liquid level gauges; exact gauge type remains unresolved. |
| Temperature sensor primary element | keep leaf | HV-14 | `ebf3_hv_tank_temperature_sensor` | BINP supports transformer temperature measurement; sensor construction remains unresolved. |
| RTD/thermistor/probe/feedthrough children | defer | HV-14 | None | Need source-specific sensor architecture before child BOM. |
| Grounding terminal / bonding point | keep leaf | HV-15 | `ebf3_hv_tank_grounding_terminal` | Spellman/Eaton support grounding hardware; global return architecture remains separate. |
| Enclosure shielding/bonding hardware | defer | HV-15 | None | Candidate is real but overlaps grounding terminal and enclosure. |
| Physical service interlock switch | defer | HV-15 / controls | None | Interlock concept is real, but switch location and package are not sourced. |
| Interlock decision logic | split_boundary | controls | `ebf3_safety_blocking_logic` | Controls own central interlock decision and blocking logic. |
| Manual discharge point | defer | HV-15 / HV-10 | None | Could overlap bleeder/discharge chain. Needs source or service procedure. |

## KB Action

- Do not create new child BOMs for HV-13/HV-14/HV-15 in this pass.
- Keep the current HV-13 split items as leaf scaffold items.
- Keep HV-15 represented only by `ebf3_hv_tank_grounding_terminal` for now.
- Update notes to point to this review and make deferred service/interlock
  details explicit.

## Manufacturing Readiness

No service/protection item is local-ready. Pressure rating, oil compatibility,
seal material, thread/flange geometry, transformer-oil compatibility, grounding
ampacity, interlock certification, and service procedure all need later
material/process and safety review.
