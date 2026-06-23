---
row_identity:
  item: "66"
  cad_file: "66_plate_front"
  source_row_number: 272
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom front plate in the reAM250 recoater/conveyor-side assembly, likely acting as a light structural end/support plate for adjacent shafts, bearings, belt, or guide hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/66_plate_front.step; research/ream250_bom/ream250_bom_row_0272_66__views_2x2.png"
    cited_fact_or_basis: "BOM row 272 lists item 66, quantity 3, CAD file 66_plate_front. Manifest row 272 maps it to a matched part STEP. FreeCAD measured one solid with a 136.00 x 178.50 x 10.00 mm bounding box, and the rendered preview shows a thin irregular plate with pockets, cutouts, and mounting-like holes/features. Neighboring BOM rows include retaining rings, 67_plate_back, shafts, conveyor belt, gliding surface, blades, and other recoater/conveyor-related parts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'plate_front' and neighboring BOM context are interpreted as a front support/end plate role rather than a cover-only panel."
    - "The three BOM instances are treated as three identical physical plates."
  uncertainty_notes:
    - "The BOM and STEP export do not include mating constraints or a drawing, so the exact attached shaft, belt, or guide interfaces remain uncertain."
mass:
  value_kg: 0.327
  basis: "Per unit. BOM quantity is 3, so the row total is about 0.982 kg. FreeCAD volume 121264.951 mm^3 = 0.000121264951 m^3; assembly STEP metadata reports Aluminum 6061 density 2700 kg/m^3; computed per-unit mass = 0.000121264951 m^3 * 2700 kg/m^3 = 0.327415 kg, rounded to 0.327 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/66_plate_front.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 121264.951 mm^3, area 37852.756 mm^2, and bounding box 136.00 x 178.50 x 10.00 mm. The local assembly STEP material extractor matched 66_plate_front to material Aluminum 6061 with density 2700.0. The local density table lists aluminum density_kg_per_m3: 2700."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical part volume for one plate."
    - "The assembly STEP Aluminum 6061 density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes any fasteners, bearings, shafts, inserts, coatings, or belt hardware that are separate BOM rows."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 66_plate_front to material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata identifies the alloy but does not specify temper, surface finish, or coating."
how_to_make:
  summary: "Make as a custom machined Aluminum 6061 plate: cut plate stock near the 136 x 178.5 x 10 mm envelope, CNC mill the irregular outline, pockets, holes, and cutouts, deburr, clean, and inspect interfaces."
  manufacturing_steps:
    - "Start from Aluminum 6061 plate stock at least 10 mm thick, with allowance around the 136.00 x 178.50 mm profile."
    - "Saw, waterjet, or rough mill the blank to near-net rectangular or irregular outline."
    - "CNC mill the outside profile, pockets, reliefs, slots, and mounting holes visible in the CAD."
    - "Deburr edges and holes; clean chips and surface contamination."
    - "Inspect thickness, hole locations, pocket depths, and critical mating faces against the STEP model or a downstream assembly drawing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/66_plate_front.step; research/ream250_bom/ream250_bom_row_0272_66__views_2x2.png"
    cited_fact_or_basis: "The STEP geometry is a single Aluminum 6061 solid with a 136.00 x 178.50 x 10.00 mm envelope, and the preview shows a thin non-axisymmetric plate with irregular perimeter, pockets, cutouts, and mounting-like holes. targeted_web_search: searched \"66_plate_front reAM250\", \"reAM250 66_plate_front\", and \"Renishaw AM250 front plate aluminum\"; results found duplicate/mirrored reAM250 BOM text and unrelated AM250/front-plate references, but no row-specific fabrication drawing, tolerance callout, or vendor manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The flat plate geometry and Aluminum 6061 material make subtractive machining from plate stock the most plausible local route."
    - "Waterjet or saw roughing is optional; final interface geometry is assumed to need milling because the CAD includes pockets and localized features."
  uncertainty_notes:
    - "No row-specific drawing was found, so exact tolerances, datums, surface finish, and whether any post-machining coating or anodizing is required remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable custom Aluminum 6061 machined plate, with quantity three in this BOM row rather than three distinct item definitions."
---

Research result for reAM250 BOM row 272.
