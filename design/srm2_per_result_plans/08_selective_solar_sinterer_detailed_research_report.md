# Selective Solar Sinterer Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/08_selective_solar_sinterer.md`
Purpose: map selective solar sintering architecture into concrete KB machine/process/recipe entries.

## 1) Source extraction summary
Report 08 recommends first-generation architecture:
- heliostat/solar concentration chain
- rugged XY motion platform
- controlled powder layering/recoating
- closed-loop sensing and dust-protected optical path

## 2) Existing KB mapping
Reusable existing IDs:
- `solar_concentrator_fresnel_v0`
- `motion_gantry_basic`
- `vibratory_feeder_v0`
- `hopper_feed_system`
- `machine_vision_camera_v0`

Gap:
- no selective solar sinterer machine ID
- no selective-solar process ID
- no selective output material distinct from generic sinter block

## 3) Recommended KB updates
- machine: `selective_solar_sinterer_v0`
- BOM: `bom_selective_solar_sinterer_v0`
- recipe: `recipe_selective_solar_sinterer_v0`
- process: `selective_solar_sintering_v0`
- material: `regolith_sinter_featured_part_v0`
- supporting part modules:
  - `solar_sinter_optics_head_v0`
  - `powder_recoater_module_v0`

## 4) Validation checklist
- validate new machine/process/material IDs
- full index after applying 08 changes.

