---
row_identity:
  item: "6X"
  cad_file: "6X_connection_linear_guide_top"
  source_row_number: 204
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom upper connection bracket for the reAM250 linear-guide assembly; it appears to tie the top of a linear guide or guide-adjacent carriage support into the surrounding frame."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6X_connection_linear_guide_top.step; research/ream250_bom/ream250_bom_row_0204_6X__views_2x2.png"
    cited_fact_or_basis: "BOM row 204 states item 6X, quantity 1, CAD file 6X_connection_linear_guide_top. The manifest maps the row to gold_export/parts/6X_connection_linear_guide_top.step as a matched part export. FreeCAD measured one solid with bounding box 58.00 x 121.50 x 179.00 mm. The rendered contact sheet shows a tall ribbed bracket with a top mounting face/flange and side/back connection geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename connection_linear_guide_top and visible bracket geometry are interpreted as an upper mechanical connector for the neighboring linear-guide subsystem rather than as the guide rail or bearing block itself."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the local bracket role, but not the exact mating face, fastener pattern, or load case in the larger axis assembly."
mass:
  value_kg: 1.4
  basis: "FreeCAD volume 175328.702 mm^3 equals 0.000175329 m^3. The assembly STEP material extractor reports Stainless Steel, Austenitic with density 8000 kg/m^3 for 6X_connection_linear_guide_top, giving 1.4026 kg per unit. BOM quantity is 1, so the row total is also about 1.40 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6X_connection_linear_guide_top.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 175328.702 mm^3, area 69530.569 mm^2, and bounding box 58.00 x 121.50 x 179.00 mm. Local assembly STEP material extraction matched product 6X_connection_linear_guide_top to material Stainless Steel, Austenitic and density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured row item."
    - "The extracted 8000 kg/m^3 density is used directly as the calculation density for the austenitic stainless steel part."
  uncertainty_notes:
    - "The estimate depends on the CAD export volume being a finished solid without suppressed pockets, inserts, or separate fasteners; no separate physical scale measurement was available."
material:
  primary_material: "austenitic stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local STEP material extractor matched product 6X_connection_linear_guide_top and returned material Stainless Steel, Austenitic with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata resolves the material family, but not the exact stainless grade, heat treatment, finish, or passivation state."
how_to_make:
  summary: "Fabricate as a custom stainless-steel linear-guide connector bracket, most plausibly by CNC machining from a stainless block or by welding/cutting stainless plate features followed by finish machining of the mounting faces and holes."
  manufacturing_steps:
    - "Start from austenitic stainless steel stock large enough for the roughly 58 x 121.5 x 179 mm envelope, or from cut stainless plate sections if modeled as a weldment."
    - "Rough-cut the outer profile and ribbed web geometry by CNC milling, waterjet/laser cutting plus welding, or a hybrid route selected from available shop capability."
    - "Finish-machine the top mounting face, side/back connection faces, and any fastener holes or slots required by the mating linear-guide hardware."
    - "Deburr the ribs and edges, clean for machine assembly, and inspect bracket flatness, perpendicularity, hole positions, and linear-guide alignment interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6X_connection_linear_guide_top.step; research/ream250_bom/ream250_bom_row_0204_6X__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one austenitic-stainless solid with a 58.00 x 121.50 x 179.00 mm envelope, a top flange/mounting face, and ribbed bracket/web geometry. targeted_web_search: searched \"6X_connection_linear_guide_top\", \"reAM250 6X linear guide top\", and \"connection linear guide top stainless steel bracket\"; results were duplicate reAM250 BOM text or general linear-guide references, with no row-specific drawing, tolerance, or manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part because the BOM row has no manufacturer, product ID, or link URL, and the manifest classifies it as a matched part rather than a vendor component."
    - "The manufacturing route is inferred from stainless material, bracket geometry, and the need for accurate linear-guide mounting interfaces."
  uncertainty_notes:
    - "The source package does not specify whether the design intent is monolithic machining, weldment fabrication, casting, additive manufacture, or a specific surface finish."
kb_implications:
  - "item_granularity: simple_part - model later as one custom stainless linear-guide connector bracket, not as a purchased guide module."
---

Research result for reAM250 BOM row 204.
