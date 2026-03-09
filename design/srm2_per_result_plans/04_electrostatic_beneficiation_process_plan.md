# 04 Electrostatic Beneficiation Process - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/04_electrostatic_beneficiation_process_detailed_research_report.md`

## Scope in report
- Process chain for dry regolith conditioning, tribocharging, E-field split, and product routing.

## Current KB mapping
- Existing beneficiation processes:
  - `beneficiate_regolith_magnetic_v0`
  - `ilmenite_extraction_from_regolith_v0`
  - `mineral_processing_basic_v0`
- Existing material endpoints:
  - `anorthite_ore`, `pyroxene_concentrate`, `ilmenite_concentrate`, `tailings`, `non_magnetic_tailings`
- No explicit electrostatic beneficiation process currently found.

## Decision
- `new` process with recipe variants against existing material IDs.
- Reuse existing output materials where functionally equivalent.
- Add explicit middlings stream because report emphasizes recycle/reclean loops.

## Proposed KB deltas
- Add process: `electrostatic_beneficiation_regolith_v0`
- Add recipe variants that target existing material IDs:
  - `recipe_ilmenite_concentrate_electrostatic_v0`
  - `recipe_pyroxene_concentrate_electrostatic_v0`
  - `recipe_tailings_electrostatic_v0`
  - `recipe_anorthite_ore_electrostatic_v0`
- Add intermediate:
  - `electrostatic_middlings_v0`
  - `recipe_electrostatic_middlings_v0`

## Machine requirements for new process
- `electrostatic_separator_v0` (from report 03 plan)
- Existing support chain:
  - feed preparation equipment (crusher/screen)
  - optional `magnetic_separator_drum_v0` for pre-clean stage
  - `vibratory_feeder_v0` for metered feed to separator

## Key risks / open issues
- Keep mass balance and coproduct outputs explicit to satisfy ADR-018 validation behavior.
- Avoid creating too many new mineral IDs when existing concentrate/tailings IDs can carry the stream.
