# 05 Liquation Fe/TiO2 Separation - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/05_liquation_fe_tio2_separation_detailed_research_report.md`

## Scope in report
- Post-ilmenite reduction separation route to split metallic Fe and TiO2-rich phases.

## Current KB mapping
- Existing relevant processes/materials:
  - `iron_reduction_from_ilmenite_v0`
  - `vacuum_pyrolysis_ilmenite_v0`
  - `titanium_oxide`
  - `iron_powder_or_sheet`, `iron_metal_pure` chain entries
- No dedicated liquation/separation process for Fe/TiO2 split.

## Decision
- `new variant process` preferred over creating many intermediates.
- Use current output material IDs unless quality-specific variant is required.
- Add one explicit intermediate feed: `reduced_ilmenite_residue_v0`.

## Proposed KB deltas
- Add material: `reduced_ilmenite_residue_v0`
- Add process: `liquation_fe_tio2_separation_v0`
- Add recipe variant(s):
  - `recipe_reduced_ilmenite_residue_v0`
  - `recipe_titanium_oxide_liquation_v0`
  - `recipe_iron_metal_from_liquation_v0`
- If purity distinction is important:
  - add variant material IDs like `titanium_oxide_metallurgical_grade_v0`

## Machine requirements for new process
- Existing thermal/processing machines likely sufficient:
  - `furnace_high_temp`
  - `magnetic_separator_drum_v0`
  - `centrifugal_separator_v0` or `gravity_separator` for phase split assistance

## Key risks / open issues
- Decide whether this process is truly additive vs overlapping current ilmenite routes.
- Purity-grade variants should only be added if downstream recipes require them.
