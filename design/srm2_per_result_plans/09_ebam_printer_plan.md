# 09 EBAM Printer - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/09_ebam_printer_detailed_research_report.md`

## Scope in report
- Electron-beam additive manufacturing (wire-feed) machine option.

## Current KB mapping
- Existing close matches:
  - `ebm_machine_lunar_v0`
  - `ebf3_wire_feed_machine_v0`
  - `wire_arc_additive_machine` (WAAM, non-electron-beam)
  - vacuum and HV support chain exists in multiple machine/part entries

## Decision
- `reuse + targeted process addition` first.
- Use `ebf3_wire_feed_machine_v0` as the wire-feed EBAM anchor.

## Proposed KB deltas
- Add process: `electron_beam_additive_manufacturing_v0`
- Add output material: `ebam_deposited_metal_blank_v0`
- Keep existing machine entries and avoid duplicate machine proliferation for now.

## Machine requirements for new/updated process
- `ebf3_wire_feed_machine_v0`
- supporting vacuum and power-conditioning systems as process requirements if needed

## Key risks / open issues
- Potential overlap/confusion between EBM and EBAM naming in current KB.
- Need to resolve whether this chain is import-first versus local-build-first for early generations.
