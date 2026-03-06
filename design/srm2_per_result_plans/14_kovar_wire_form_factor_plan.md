# 14 Kovar Wire Form Factor - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/14_kovar_wire_form_factor_detailed_research_report.md`

## Scope in report
- Convert `kovar_alloy_fe_ni_co_v0` bulk stock into wire form for feedthroughs/leads/seal-compatible interconnects.

## Current KB mapping
- Existing:
  - `kovar_alloy_fe_ni_co_v0`
  - generic wire drawing processes: `wire_drawing_process_v0`, `metal_wire_drawing_process_v0`
  - die tooling chain references in drawing recipes
- No dedicated Kovar wire material ID.

## Decision
- `new variant material` + recipe using existing wire-drawing process chain.

## Proposed KB deltas
- Add material: `kovar_wire_v0`
- Add recipe: `recipe_kovar_wire_v0`
- Add process variant only if needed:
  - `kovar_wire_drawing_v0` (otherwise reuse `wire_drawing_process_v0`)
- Optional insulation companion entries from report 12 can attach here.

## Machine requirements for new process
- Reuse existing:
  - wire drawing bench/machine entries already used by wire recipes
  - anneal furnace / controlled-atmosphere capability if modeled explicitly

## Key risks / open issues
- Need clear distinction between composition-grade Kovar alloy and form-factor wire stock.
- If feedthrough reliability modeling is later added, may need temper/anneal variants.
