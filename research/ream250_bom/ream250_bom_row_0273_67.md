---
row_identity:
  item: "67"
  cad_file: "67_plate_back"
  source_row_number: 273
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom back plate in the reAM250 recoater/conveyor-side row-8 subsystem, likely serving as a rear structural/end support plate for adjacent shafts, belt, bearing, or guide hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/67_plate_back.step; research/ream250_bom/ream250_bom_row_0273_67__views_2x2.png"
    cited_fact_or_basis: "BOM row 273 lists item 67, quantity 1, CAD file 67_plate_back. Manifest row 273 maps it to a matched part STEP. FreeCAD measured one solid with a 136.00 x 178.50 x 10.00 mm bounding box, and the rendered preview shows a thin irregular plate with pockets, reliefs, and mounting-like holes. Neighboring BOM rows include 66_plate_front, 68_convex_crowned_shaft, 69_deflection_shaft, conveyor belt, gliding surface, blades, and other recoater/conveyor-related parts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'plate_back' and neighboring BOM context are interpreted as a rear support/end plate role rather than a cover-only panel."
  uncertainty_notes:
    - "The BOM and STEP export do not include mating constraints or a drawing, so the exact shaft, belt, guide, or fastener interfaces remain uncertain."
mass:
  value_kg: 0.349
  basis: "Per unit. BOM quantity is 1, so row total is also about 0.349 kg. FreeCAD volume 129348.217 mm^3 = 0.000129348217 m^3; assembly STEP metadata reports Aluminum 6061 density 2700 kg/m^3; computed mass = 0.000129348217 m^3 * 2700 kg/m^3 = 0.349240 kg, rounded to 0.349 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/67_plate_back.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 129348.217 mm^3, area 40055.246 mm^2, and bounding box 136.00 x 178.50 x 10.00 mm. The local assembly STEP material extractor matched 67_plate_back to material Aluminum 6061 with density 2700.0. The local density table lists aluminum density_kg_per_m3: 2700."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical part volume for one plate."
    - "The assembly STEP Aluminum 6061 density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes any fasteners, bearings, shafts, inserts, coatings, or belt hardware that are represented as separate BOM rows."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 67_plate_back to material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata identifies the alloy but does not specify temper, surface finish, coating, or heat-treatment condition."
how_to_make:
  summary: "Make as a custom machined Aluminum 6061 plate: cut plate stock near the 136 x 178.5 x 10 mm envelope, CNC mill the irregular outline, pockets, holes, and relief features, deburr, clean, and inspect interfaces."
  manufacturing_steps:
    - "Start from Aluminum 6061 plate stock at least 10 mm thick, with allowance around the 136.00 x 178.50 mm profile."
    - "Saw, waterjet, or rough mill the blank to the near-net rectangular or irregular outline."
    - "CNC mill the outside profile, pockets, reliefs, slots, and mounting holes visible in the CAD."
    - "Deburr edges and holes; clean chips and surface contamination."
    - "Inspect thickness, hole locations, pocket depths, and critical mating faces against the STEP model or a downstream assembly drawing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/67_plate_back.step; research/ream250_bom/ream250_bom_row_0273_67__views_2x2.png; web search"
    cited_fact_or_basis: "The STEP geometry is a single Aluminum 6061 solid with a 136.00 x 178.50 x 10.00 mm envelope, and the preview shows a thin non-axisymmetric plate with irregular perimeter, pockets, reliefs, and mounting-like holes. targeted_web_search: searched \"67_plate_back reAM250\", \"reAM250 67_plate_back\", and \"Renishaw AM250 plate back aluminum\"; results found duplicate/mirrored reAM250 BOM listings and unrelated AM250/back-plate references, but no row-specific fabrication drawing, tolerance callout, or vendor manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The flat plate geometry and Aluminum 6061 material make subtractive machining from plate stock the most plausible local route."
    - "Waterjet or saw roughing is optional; final interface geometry is assumed to need milling because the CAD includes pockets and localized features."
  uncertainty_notes:
    - "No row-specific drawing was found, so exact tolerances, datums, surface finish, and whether anodizing or another post-machining finish is required remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as one custom Aluminum 6061 machined plate, not a purchased module; reuse with the matching front/back plate family only if later KB work finds equivalent geometry within the 5x approximation rule."
---

Research result for reAM250 BOM row 273.
