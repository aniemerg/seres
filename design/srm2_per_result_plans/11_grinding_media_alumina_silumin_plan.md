# 11 Grinding Media (Alumina/Silumin) - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/11_grinding_media_alumina_silumin_detailed_research_report.md`

## Scope in report
- Alternative grinding media to reduce contamination or tune wear/performance.

## Current KB mapping
- Existing:
  - `grinding_media_steel` + `grinding_media_fabrication_v0`
  - `alumina_ceramic_v0`
  - `silumin_alloy`
- No dedicated alumina or silumin grinding media IDs.

## Decision
- `new variants` justified for contamination-sensitive chains.

## Proposed KB deltas
- Add materials:
  - `grinding_media_alumina_v0`
  - `grinding_media_silumin_v0`
- Add process/recipe variants:
  - `grinding_media_alumina_fabrication_v0`
  - `recipe_grinding_media_alumina_v0`
  - `recipe_grinding_media_silumin_v0`
- Update milling recipes where selective media choice is useful.

## Machine requirements for new process
- `sintering_furnace_v0` or equivalent for alumina route
- casting/forming + heat treatment chain for silumin route (existing foundry stack)

## Key risks / open issues
- Ensure additions are represented as media variants, not separate mill machines.
- Validate where substitution materially changes outputs vs just contamination assumptions.
