---
row_identity:
  item: "3T"
  cad_file: "3T_diffusor"
  source_row_number: 160
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom gas diffuser body in the reAM250 gas outlet/inlet path, spreading flow between a smaller round neck and a larger rectangular duct interface before the adjacent flow rectifier."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3T_diffusor.step; research/ream250_bom/ream250_bom_row_0160_3T__views_2x2.png"
    cited_fact_or_basis: "BOM row 160 states item 3T, quantity 1, CAD file 3T_diffusor. Neighboring BOM rows are gas outlet parts followed by 3U_flow_rectifier and 3V_gas_in_top. The manifest maps the row to gold_export/parts/3T_diffusor.step as one matched part. FreeCAD measured one solid with a 300.00 x 100.00 x 300.00 mm bounding box. The rendered contact sheet shows a tapered diffuser/funnel body with a rectangular upper flange/opening, smaller round lower neck/flange, and internal divider/vanes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD filename diffusor is interpreted as diffuser, and the neighboring gas outlet and flow rectifier rows place this part in the gas-flow path."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the local flow-path role but not the exact gas direction, pressure drop target, or mating seal interfaces."
mass:
  value_kg: 1.38
  basis: "FreeCAD volume 512111.010 mm^3 equals 0.000512111 m^3. Assembly STEP material metadata gives Aluminum 6061 with density 2700 kg/m^3, so one diffuser is about 1.383 kg. BOM quantity is 1, so the row total is also about 1.38 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3T_diffusor.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 512111.010 mm^3, area 287573.011 mm^2, and bounding box 300.00 x 100.00 x 300.00 mm. The local assembly STEP material extractor matched product 3T_diffusor to material Aluminum 6061 and density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume is used as the physical-volume proxy for one manufactured diffuser."
    - "The STEP material density is interpreted in kg/m^3, consistent with the extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass depends on CAD export fidelity; small omitted fasteners, gaskets, coatings, or surface-treatment mass are not represented in the single-part STEP."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 3T_diffusor and returned material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM table itself has blank material fields, so the material assignment relies on row-specific assembly STEP metadata rather than a drawing note or vendor datasheet."
how_to_make:
  summary: "Fabricate as a custom Aluminum 6061 diffuser, likely by CNC machining or welded/formed aluminum fabrication followed by finish machining of the flange and mating features."
  manufacturing_steps:
    - "Start from Aluminum 6061 plate/block stock or preformed/welded aluminum sections sized for the 300 x 100 x 300 mm envelope."
    - "Create the tapered diffuser body, rectangular upper interface, round lower neck, and internal vanes/divider geometry by machining from billet or by joining formed/cut aluminum sections."
    - "Machine the rectangular and round flange faces, openings, mounting features, and any seal-critical mating surfaces to final dimensions."
    - "Deburr internal flow surfaces and inspect flange flatness, duct alignment, and vane geometry."
    - "Clean for the machine gas path and apply anodizing or other surface treatment only if later design evidence requires it."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3T_diffusor.step; research/ream250_bom/ream250_bom_row_0160_3T__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one Aluminum 6061 diffuser-shaped solid with tapered walls, a rectangular upper flange/opening, a smaller round lower neck/flange, internal divider/vanes, and a 300.00 x 100.00 x 300.00 mm bounding box. targeted_web_search: searched \"3T_diffusor reAM250 material manufacturing\", \"3T diffusor reAM250\", and \"3T_diffusor aluminum diffuser CAD\" results found mirrored BOM listings but no row-specific drawing, fabrication note, or vendor manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row is treated as a custom fabricated simple part because the BOM has no manufacturer, product ID, or Link URL, while the manifest classifies the CAD export as a matched part."
    - "Machining and/or welded aluminum fabrication is inferred from the aluminum material, diffuser geometry, flange interfaces, and internal flow features."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify whether the actual part is billet-machined, cast, additively manufactured, formed and welded, or assembled from multiple pieces."
kb_implications:
  - "item_granularity: simple_part - custom Aluminum 6061 gas diffuser should be modeled as one reusable machined/fabricated flow-path part, not as a purchased module unless a later drawing exposes a subassembly."
---

Research result for reAM250 BOM row 160.
