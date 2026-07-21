# Beam Diagnostics Decomposition Plan

Status: Level-3 planning file with minimal pickup/signal split completed.

Parent items:

- `ebf3_gun_beam_boundary_pickup` (FG-9)
- `ebf3_gun_secondary_electron_pickup` (FG-10)
- `ebf3_gun_signal_wiring` (FG-19)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/beam_diagnostics/beam_diagnostics_sources.md`

Target KB BOMs:

- `bom_ebf3_gun_beam_boundary_pickup`
- `bom_ebf3_gun_secondary_electron_pickup`
- `bom_ebf3_gun_signal_wiring`

This pass creates minimal gun-side diagnostic children: collector/isolation for
FG-9/FG-10, local diagnostic signal leads, a gun-diagnostic feedthrough
insert/interface marker, and a local shield-termination interface marker for
FG-19. Chamber passive ports, DAQ, controls processing, final pinout, and bias
supplies remain deferred across subsystem boundaries.

Workflow and decision-status definitions:

- `research/ebf3_bom_sources/README.md`
- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`

## Source Authority Assessment

1. `RAW-BINP-60KEV-30KW` supports FG-9 and FG-10 existence in a comparable
   electron-optical system and supports monitored beam/cathode currents, but it
   does not expose pickup geometry or wiring.
2. Kimball, OSTI, and JACOW sources support Faraday-cup style collector,
   shielding, suppression, insulation, vacuum feedthrough, and external
   measurement functions. They are not EBF3 beam-boundary pickup drawings.
3. J-STAGE and Research India Publications sources support secondary-current
   pickup concepts in electron-beam welding, including a ring collector and
   biased collector path. They do not define EBF3 fixed-gun hardware.
4. Signal-feedthrough sources support the need for vacuum-compatible signal
   passage, shielding, and feedthrough selection, but chamber ports and central
   DAQ remain subsystem-boundary items.
5. `LOCAL-EBF3-FG-TABLE` is user-derived and candidate-only.

## Source Evidence And Use

### RAW-BINP-60KEV-30KW

Evidence:

- "12-pick-up of beam boundary"
- "13-pick-up of secondary electrons"
- "registering reflected from the work piece electrons"
- "beam current, cathode heat current"

Use:

- Supports keeping FG-9 and FG-10 as fixed-gun diagnostic assemblies.
- Supports FG-19 as local gun-side signal wiring for monitored gun signals.
- Does not define collector shape, insulator geometry, feedthrough construction,
  or external electronics.

### LOCAL-EBF3-FG-TABLE

Evidence:

- User-derived FG-9 candidates include collector electrode, insulating mount,
  shielded signal lead, and feedthrough/interface.
- User-derived FG-10 candidates include collector plate or ring, optional bias
  electrode, insulator, shielded signal lead, and feedthrough.
- User-derived FG-19 candidates include sensor pickup, shielded wires, ceramic
  feedthrough, connector, and grounding/shield termination.

Use:

- Introduces candidate Level-3 children only. It cannot justify `adopt` by
  itself.

### WEB-KIMBALL-FARADAY-CUPS

Evidence:

- "mounted in the vacuum system"
- "vacuum flange feedthrough"
- "hollow stainless steel cylinder"
- "outer, grounded cylinder"
- "electrical connection"

Use:

- Supports collector, shield, electrical connection, and vacuum feedthrough as
  real diagnostic-pickup functions.
- Does not prove that the EBF3 beam-boundary pickup is a full Faraday cup or
  that the secondary-electron pickup uses this geometry.

### WEB-OSTI-FARADAY-CUP-DESIGN

Evidence:

- "stop and measure the beam charge"
- "graphite and Copper pieces"
- "Electrical isolation"
- "ceramic break"
- "graphite cone, copper (OFHC) and Steel"

Use:

- Supports beam-intercepting collector materials and insulation as real design
  concerns for a beam-boundary pickup.
- This is an accelerator Faraday cup design, so it should not be adopted as
  EBF3 geometry.

### WEB-JACOW-BIW2010-FARADAY-CUP

Evidence:

- "OFHC copper was chosen"
- "suppressing electrode made of stainless steel"
- "ring shape instead of a grid"

Use:

- Supports OFHC copper collector, stainless suppressor/ring, and secondary
  electron suppression as real charged-particle diagnostic options.
- The source is for low-energy antiproton/ion measurements, so it is material
  and function support only.

### WEB-JSTAGE-EBW-SECONDARY-CURRENT

Evidence:

- "secondary current signal collected in plasma"
- "ring electrode collector"
- "positive potential of 50 volts"
- "data acquisition system"

Use:

- Supports a ring-electrode collector and bias path as plausible
  secondary-electron/current pickup features in electron-beam welding.
- DAQ and computer processing belong to controls, not the fixed electron beam
  gun.

### WEB-RIPUBLICATION-SECONDARY-CURRENT

Evidence:

- "detection of secondary current"
- "electron collector was installed"
- "positive potential of 48V"
- "online monitoring"

Use:

- Supports secondary-current monitoring as a real EBW diagnostic function.
- Reinforces that the signal interpretation/control path should remain outside
  the gun hardware BOM.

### WEB-DESIGN-REALIZED-SIGNAL-FEEDTHROUGHS

Evidence:

- "Beam diagnostics systems"
- "Multi-Pin & Signal Vacuum Feedthroughs"
- "low-noise RF transmission"

Use:

- Supports vacuum signal feedthrough as a real interface class.
- Does not define whether the insert belongs under FG-19, the cabin
  feedthroughs, or a shared controls harness.

### WEB-ALLECTRA-COAXIAL-FEEDTHROUGHS

Evidence:

- "shielding sensitive direct current signals"
- "50 Ohm"
- "vacuum side"

Use:

- Supports coaxial feedthroughs as a plausible signal-path class for shielded
  diagnostic pickup signals.
- Does not justify adopting coax as the EBF3 signal-feedthrough topology before
  the pickup signal bandwidth, grounding, and chamber port layout are selected.

### WEB-PFEIFFER-FEEDTHROUGHS-KNOWHOW

Evidence:

- "current capacity and voltage"
- "vacuum-tightness and temperature resistance"
- "ceramic insulation"
- "gas discharges and flashovers"

Use:

- Supports treating the feedthrough as a rated vacuum/electrical interface, not
  just a wire.
- Reinforces that feedthrough insert, shield, insulation, and clearance choices
  need a physical topology and ratings before child BOM creation.

## Candidate Decision Matrix

| Candidate component/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| Beam-boundary collector / intercept surface | adopted / detail deferred | FG-9 | `ebf3_gun_beam_boundary_collector_electrode` | BINP names the pickup, and charged-particle diagnostic sources support collector electrodes. Exact edge/intercept geometry and heat load remain deferred. |
| Beam dump / heat sink body | defer | FG-9 | None | Faraday-cup references support beam stops/dumps in some diagnostics, but adopting one would over-model FG-9 without EBF3-specific heat-load and geometry evidence. |
| Ground shield / guard cylinder | defer | FG-9 | None | Kimball supports a grounded shield in Faraday cups. EBF3 pickup placement and shield form are unknown. |
| Suppression or bias electrode | defer | FG-9/FG-10 | None | JACOW and Kimball support suppression/bias in diagnostic cups; J-STAGE supports a biased collector for secondary current. Bias supply ownership crosses into power supplies/controls. |
| Ceramic or high-resistance insulator | adopted / detail deferred | FG-9/FG-10 | `ebf3_gun_beam_boundary_pickup_insulator`, `ebf3_gun_secondary_pickup_insulator` | OSTI/JACOW support electrical isolation for diagnostic collectors. Feedthrough insert and exact ceramic shape remain deferred. |
| Secondary-electron ring collector | adopted / detail deferred | FG-10 | `ebf3_gun_secondary_electron_ring_collector` | J-STAGE supports a ring electrode collector for EBW secondary-current pickup. Treat as preferred geometry until a better EBF3-specific shape appears. |
| Secondary-electron plate collector | defer | FG-10 | None | User-derived candidate only for this EBF3 model; current web sources found a ring collector, not a plate collector. |
| Local signal lead from pickup to gun-side interface | adopted / detail deferred | FG-9/FG-10/FG-19 | `ebf3_gun_local_diagnostic_signal_lead_set` | Signal leads are required to carry pickup signals toward the gun-side interface. Feedthrough topology, shield grounding, and controls-side acquisition remain deferred. |
| Vacuum signal feedthrough insert | adopted / detail deferred | FG-19 / cabin / controls | `ebf3_gun_diagnostic_signal_feedthrough_insert` | Feedthroughs are real, and current interface architecture assigns the gun-diagnostic insert/interface marker to FG-19 while cabin keeps passive ports and controls keep acquisition. Coax/multipin/power-feedthrough choice is not selected. |
| External ammeter, digitizer, DAQ, or computer processing | split_boundary | Controls | None under gun | Multiple sources describe external measurement electronics. Keep these in controls, not in fixed-gun child BOMs. |
| Grounding/shield termination | adopted / detail deferred | FG-19 / controls | `ebf3_gun_signal_shield_termination_interface` | A shield termination interface is needed to keep signal shielding distinct from protective ground, HV return, beam-current return, and controls DAQ. Exact grounding policy and connector geometry remain unresolved. |

## Current KB Action

- Create minimal child BOMs for FG-9, FG-10, and FG-19.
- Keep FG-9 and FG-10 as fixed-gun diagnostic pickup assemblies with only
  collector and local isolation children.
- Keep FG-19 as gun-side signal wiring and interface hardware only. External
  measurement, acquisition, processing, interlocks, cabinet harnessing, and
  chamber ports remain outside this BOM.
- Do not create bias/suppression, controls DAQ, connector-family, pinout, or
  final shield-grounding child items yet.

## Signal-Path Follow-Up

Target: decide whether FG-19 can be split into local pickup leads, signal
feedthrough insert, shield termination, and controls-side acquisition.

Decision: split local gun-side diagnostic leads, a gun-diagnostic feedthrough
insert/interface marker, and a local shield-termination interface marker.

Reasoning:

- Existing sources support a physical path from collector to feedthrough to
  external measurement, and current interface architecture assigns the
  gun-diagnostic insert/interface marker to FG-19 while keeping cabin passive
  ports and controls acquisition separate.
- The local in-gun lead set and feedthrough/shield interface markers are now
  modeled because they do not decide connector family, pinout, controls-side
  acquisition, or final shield-grounding policy.
- Coaxial feedthroughs are plausible for shielded diagnostic signals, but a
  multipin signal feedthrough or dedicated diagnostic flange is also plausible.
- Creating connector-family, pinout, DAQ, or cabinet-harness children now would
  still risk duplicating cabin passive ports or controls acquisition hardware.

Next unblock condition:

- Select or source the remaining physical signal path: pickup location,
  in-vacuum cable class, coax/multipin/shared-plate topology, shield/ground
  policy, and controls-side acquisition boundary.

## Manufacturing Readiness

No item in this cluster is local-ready. Collector geometry, heat load,
secondary-electron suppression, vacuum-compatible insulation, low-noise signal
feedthroughs, grounding, and controls integration all need separate review before
manufacturing recipes or local closure are added.
