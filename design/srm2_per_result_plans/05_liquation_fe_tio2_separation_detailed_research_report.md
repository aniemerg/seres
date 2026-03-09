# Liquation Fe/TiO2 Separation Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/05_liquation_fe_tio2_separation.md`
Purpose: map the report's post-reduction Fe/TiO2 split route into concrete KB process and recipe entries.

## 1) Source extraction summary
Report 05 defines a post-reduction separation route:
- thermal conditioning ("liquation"-style coarsening)
- deagglomeration/liberation
- primary magnetic split and secondary cleanup
- outputs:
  - Fe-rich product
  - TiO2-rich product
  - residual tailings/fines

The report's recommended first-generation route is solid-state conditioning + separation, not full smelting.

## 2) Existing KB mapping
Existing compatible process/material chain:
- process candidates:
  - `iron_reduction_from_ilmenite_v0`
  - `vacuum_pyrolysis_ilmenite_v0`
- existing output materials:
  - `iron_metal_pure`
  - `titanium_oxide`
  - `tailings`
- existing machines:
  - `furnace_high_temp`
  - `magnetic_separator_drum_v0`
  - `centrifugal_separator_v0`
  - `gravity_separator`

Gap:
- no explicit liquation/separation process ID
- no explicit reduced mixed feed material for post-reduction conditioning workflows
- no liquation-specific recipe variants feeding `iron_metal_pure` and `titanium_oxide`

## 3) Recommended KB structure for result 05
### Material layer
- `reduced_ilmenite_residue_v0` (new intermediate feed)

### Process layer
- `liquation_fe_tio2_separation_v0`

### Recipe layer
- `recipe_reduced_ilmenite_residue_v0`
- `recipe_iron_metal_from_liquation_v0`
- `recipe_titanium_oxide_liquation_v0`

## 4) Intermediate policy justification
`reduced_ilmenite_residue_v0` should be explicit because:
- report 05 centers on separation after reduction, on a mixed-phase residue
- this intermediate is likely reusable for alternate Fe/Ti processing chains
- explicit representation improves future process branching and simulator transparency

## 5) Process design intent
`liquation_fe_tio2_separation_v0` should:
- consume `reduced_ilmenite_residue_v0`
- output mass-balanced:
  - `iron_metal_pure`
  - `titanium_oxide`
  - `tailings`
- require separation-capable machine chain:
  - `furnace_high_temp`
  - `magnetic_separator_drum_v0`
  - `centrifugal_separator_v0`
  - `gravity_separator`
  - `labor_bot_general_v0`

## 6) Conservative-mode compliance notes
- reused existing Fe/TiO2 product IDs rather than adding purity variants now
- introduced one high-value intermediate where downstream reuse is likely
- avoided machine proliferation by using existing furnaces/separators

## 7) Validation checklist
- `python -m src.cli validate --id process:liquation_fe_tio2_separation_v0`
- `python -m src.cli validate --id item:reduced_ilmenite_residue_v0`
- `python -m src.cli validate --id item:iron_metal_pure`
- `python -m src.cli validate --id item:titanium_oxide`
- full index after updates.
