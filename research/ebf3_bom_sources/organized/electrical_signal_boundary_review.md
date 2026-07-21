# Electrical Signal Boundary Review

Status: boundary review completed for current EBF3 scaffold.

Current interface entry point:
`research/ebf3_bom_sources/organized/ebf3_interface_architecture.md`.

Purpose:

- Keep fixed-gun hardware, power electronics, controls, and chamber feedthroughs
  from duplicating the same electrical path.
- Define how electrode bias, coil/corrector current, diagnostic pickup signals,
  feedthrough inserts, and external acquisition should be owned before deeper
  controls or power-supply decomposition.

Related reviews:

- `research/ebf3_bom_sources/organized/feedthrough_interface_review.md`
- `research/ebf3_bom_sources/organized/beam_diagnostics_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/electrode_family_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/magnetic_steering_decomposition_plan.md`
- `research/ebf3_bom_sources/organized/hv_grounding_return_review.md`

## Boundary Rule

| Function layer | Owning subsystem |
| --- | --- |
| Electrode body, lens, corrector, deflection coil, or diagnostic pickup inside the gun | Fixed electron beam gun |
| Short local pickup lead or in-gun signal wiring before a feedthrough split | Fixed electron beam gun |
| Bias supply, regulated current source, amplifier, or motor/coil driver power stage | Power supplies |
| Command logic, DAQ, interlock decision, signal interpretation, and operator interface | Controls |
| Passive chamber wall opening, flange, or port | Manufacture cabin |
| Subsystem-specific vacuum feedthrough insert | Owning load/sensor subsystem until a source shows a shared feedthrough plate |
| HV output measurement and main return/current sensing | High-voltage tank, with acquisition owned by controls |

## Decisions

| Interface | Decision | Reason |
| --- | --- | --- |
| Control-electrode bias contact | Keep deferred under electrode/gun wiring boundary. | The electrode is gun hardware, but the bias source and control logic are outside the gun. |
| Screen-electrode electrical connection | Keep deferred under electrode/gun wiring boundary. | Contact geometry is not sourced and should not become a separate child before wiring ownership is fixed. |
| Trajectory-corrector leads | Keep deferred/split boundary. | The corrector load may be in the gun; the regulated current source and command path belong outside the gun. |
| Deflection coil leads and current driver | Keep leads deferred; driver belongs outside gun. | Current driver/amplifier is power-supply hardware, not a child of the deflection coil assembly. |
| Beam-boundary and secondary-pickup signal path | Keep local pickup wiring in FG-19; external DAQ stays controls. | Diagnostic sources describe external measurement electronics, but that does not make them gun hardware. |
| Vacuum signal feedthrough insert | Keep gun-diagnostic insert/interface marker in FG-19; keep cabin passive port and controls acquisition separate. | This makes the gun-side signal boundary visible without selecting coax, multipin, shared-plate geometry, or controls DAQ hardware. |
| Shield/ground termination | Keep gun-side shield-termination interface marker in FG-19; defer final grounding policy. | Signal shield termination, protective ground, HV return, and beam-current return remain separate decisions. |

## Current Action

- Do not create child BOMs for electrode contacts, driver electronics, controls
  DAQ, final connector pinouts, or final shield-grounding policy yet.
- Update affected item notes so reviewers can see this boundary from item pages.
- Use this review before decomposing controls, power supplies, diagnostics, or
  gun signal wiring.
