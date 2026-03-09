# 12 Electrical Insulation Form Factors - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/12_electrical_insulation_form_factors_detailed_research_report.md`

## Scope in report
- Form-factor level insulation entries:
  - flexible glass fiber cloth
  - rigid porcelain stand-off style
  - fused glass enamel insulation coating

## Current KB mapping
- Existing insulation-adjacent entries:
  - `ceramic_insulators`
  - `insulator_drilled`, `center_insulator_ceramic`
  - `coating_insulation_v0` process
- No explicit IDs for glass-cloth and enamel-glass form factors as report describes.

## Decision
- `variant/new` for form factors, with strong reuse of existing ceramic and coating process chains.

## Proposed KB deltas
- Add material/part IDs:
  - `glass_fiber_cloth_insulation_v0`
  - `porcelain_insulator_v0`
  - `enamel_glass_insulation_v0`
- Add process/recipe entries:
  - `porcelain_insulator_fabrication_v0`
  - `enamel_glass_insulation_coating_v0`
  - recipe files for each new target item
- Update existing machine BOMs where these appear as better-fit insulators.

## Machine requirements for new process
- Existing likely reusable machines:
  - `kiln_ceramic_v0` / high-temp furnace chain
  - `coating_station` for enamel coating route

## Key risks / open issues
- Keep insulation entries physical and form-factor specific; avoid abstract duplicate materials.
- Vacuum/outgassing constraints should be captured in notes and substitution policy.
