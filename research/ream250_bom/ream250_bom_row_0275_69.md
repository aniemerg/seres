---
row_identity:
  item: "69"
  cad_file: "69_deflection_shaft"
  source_row_number: 275
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long stainless deflection shaft in the reAM250 recoater-side assembly area, likely serving as a belt/roller guide or deflection member for the adjacent recoater/conveyor mechanism."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/69_deflection_shaft.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/60_recoater.step; research/ream250_bom/ream250_bom_row_0275_69__views_2x2.png"
    cited_fact_or_basis: "BOM row 275 lists item 69, quantity 1, CAD file 69_deflection_shaft. Manifest row 275 maps it to a matched part STEP. FreeCAD measured one solid with a 292.00 x 26.00 x 26.00 mm bounding box, and the rendered preview shows a long round shaft with smaller end journals. The 60_recoater STEP assembly contains product 69_deflection_shaft near adjacent rows for retaining rings, plates, convex crowned shaft, and conveyor-belt-related parts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'deflection_shaft' and long round shaft geometry are interpreted as a shaft/roller-like guide or deflection member rather than a stationary flat support."
    - "The neighboring recoater/conveyor rows are used only to infer local assembly context, not to assign a precise bearing layout."
  uncertainty_notes:
    - "The BOM row and STEP export do not expose mating constraints or a drawing, so the exact load path and whether the shaft rotates freely or acts as a fixed guide remain uncertain."
mass:
  value_kg: 1.162
  basis: "Per unit. BOM quantity is 1, so row total is also about 1.162 kg. FreeCAD volume 145255.715 mm^3 = 0.000145255715 m^3; assembly STEP metadata reports Stainless Steel density 8000 kg/m^3; computed mass = 0.000145255715 m^3 * 8000 kg/m^3 = 1.1620457 kg, rounded to 1.162 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/69_deflection_shaft.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 145255.715 mm^3, area 23762.019 mm^2, and bounding box 292.00 x 26.00 x 26.00 mm. The local assembly STEP material extractor matched 69_deflection_shaft to material Stainless Steel with density 8000.0. The local density table lists stainless_steel density_kg_per_m3: 8000."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical part volume."
    - "The assembly STEP stainless steel density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes any bearings, retaining rings, coatings, or fasteners that are separate BOM rows."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 69_deflection_shaft to material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a stainless steel family but not a specific alloy grade or heat treatment."
how_to_make:
  summary: "Make as a custom stainless turned shaft: cut stainless round bar to length, turn the main diameter and smaller end journals on a lathe, add any CAD-defined shoulders/grooves, deburr, clean, and inspect straightness and journal diameters."
  manufacturing_steps:
    - "Start from stainless steel round bar stock slightly larger than the 26 mm maximum shaft diameter."
    - "Saw or part the blank to slightly over the 292 mm finished length."
    - "CNC-turn or manual-lathe-turn the long shaft body, smaller end journals, shoulders, and any retaining-ring or bearing-seat features visible in the CAD."
    - "Deburr the ends and transitions; polish bearing/contact surfaces if the shaft runs against belt, roller, or bearing elements."
    - "Clean and inspect overall length, straightness, runout, and journal diameters against the CAD or downstream assembly fit."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/69_deflection_shaft.step; research/ream250_bom/ream250_bom_row_0275_69__views_2x2.png"
    cited_fact_or_basis: "The STEP geometry is a single stainless solid with a 292.00 x 26.00 x 26.00 mm envelope, and the preview shows an axisymmetric long shaft with smaller end journals. targeted_web_search: searched \"69_deflection_shaft reAM250\", \"deflection shaft recoater stainless steel\", and \"convex crowned shaft deflection shaft recoater\"; results found duplicate reAM250 BOM text and general shaft-deflection references, but no row-specific fabrication drawing, tolerance callout, or vendor manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The axisymmetric shaft geometry is best represented as a turned round-bar part rather than a casting, additive part, or purchased catalog module."
    - "Bearing/contact cleanup and inspection steps are included because the local assembly includes nearby retaining rings and shaft-like recoater/conveyor components."
  uncertainty_notes:
    - "No row-specific drawing was found, so exact tolerances, surface finish, heat treatment, and whether the shaft requires hardening remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as one custom stainless turned shaft with round-bar stock input and lathe-turning/deburring/inspection route."
---

Research result for reAM250 BOM row 275.
