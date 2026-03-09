# 13 PMT Localization Feasibility - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/13_pmt_localization_feasibility_detailed_research_report.md`

## Scope in report
- Evaluate pathways for PMT representation: import-only, hybrid localization, full local production.

## Current KB mapping
- Existing import:
  - `photomultiplier_tube_v0` in `kb/imports/`
- Existing adjacent chain:
  - vacuum tube fabrication entries
  - getter and vacuum tooling processes

## Decision
- `defer/full-local`, keep `import-first` now.
- Add staged hybrid plan metadata rather than immediate full PMT manufacturing chain.

## Proposed KB deltas
- Keep `photomultiplier_tube_v0` as active import item.
- Optional planning additions:
  - `photomultiplier_tube_hybrid_v1` (future variant stub, not enabled by default)
  - `photocathode_subassembly_imported_v0` (if hybrid path is modeled explicitly)
- Add documentation note in plan/ADR references for deferred maturity gate.

## Machine requirements for eventual hybrid process
- `glassworking_station`
- `vacuum_chamber` / pump chain
- deposition/sealing infrastructure (likely import-first for key steps)

## Key risks / open issues
- PMT full localization likely violates conservative-mode preference in near term.
- High purity/UHV dependencies make premature local recipes misleading.
