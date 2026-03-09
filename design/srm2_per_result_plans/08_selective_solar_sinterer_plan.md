# 08 Selective Solar Sinterer - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/08_selective_solar_sinterer_detailed_research_report.md`

## Scope in report
- Selective solar thermal sintering system for localized consolidation/fabrication.

## Current KB mapping
- Existing solar/sintering assets:
  - `solar_concentrator_fresnel`, `solar_concentrator_fresnel_v0`
  - `microwave_sintering_equipment_v0`
  - `regolith_sinter_block_process_v0`, `microwave_sintering_regolith_v0`
- No explicit selective solar sintering machine/process ID.

## Decision
- `variant/new` machine and process.
- Reuse solar concentrator and tracking subcomponents where possible.

## Proposed KB deltas
- Add machine: `selective_solar_sinterer_v0`
- Add BOM: `bom_selective_solar_sinterer_v0`
- Add recipe: `recipe_selective_solar_sinterer_v0`
- Add process: `selective_solar_sintering_v0`
- Optional output variants:
  - `regolith_sinter_featured_part_v0` (if distinct from generic sinter block)

## Machine requirements for new process
- Primary: `selective_solar_sinterer_v0`
- If modeled compositionally:
  - `solar_concentrator_fresnel_v0`
  - tracking/control components already in KB

## Key risks / open issues
- Distinguish this from existing microwave/furnace sintering by capability notes and process requirements.
- Throughput and geometric fidelity likely uncertain; keep conservative.
