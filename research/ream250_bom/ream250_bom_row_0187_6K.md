---
row_identity:
  item: "6K"
  cad_file: "6K_fixed_bearing_mount"
  source_row_number: 187
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small fixed bearing mount for the reAM250 axis/subassembly around BOM group 6; it provides the local bearing pocket/support that acts as the fixed-side bearing support paired with the adjacent floating bearing mount."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6K_fixed_bearing_mount.step; research/ream250_bom/ream250_bom_row_0187_6K__views_2x2.png"
    cited_fact_or_basis: "BOM row 187 and manifest row 187 identify item 6K as 6K_fixed_bearing_mount, quantity 1, with matched part STEP gold_export/parts/6K_fixed_bearing_mount.step. FreeCAD measured one solid with bounding box 52.00 x 24.00 x 8.00 mm. The rendered contact sheet shows a compact rectangular mount/plate with a large circular bearing feature and relieved/chamfered ends."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD row name's 'fixed bearing mount' is interpreted in the conventional mechanical sense: this mount supports the bearing location that defines the fixed axial reference, paired near row 188's floating bearing mount."
  uncertainty_notes:
    - "The row-level CAD does not include the mating bearing, shaft, fasteners, or surrounding axis hardware, so the exact load path and retention details are inferred from the row name and adjacent BOM context."
mass:
  value_kg: 0.0194
  basis: "Per unit for one physical mount; BOM quantity is 1, so row total is also about 0.0194 kg. FreeCAD volume is 7183.457 mm^3 = 7.183457e-6 m^3. Assembly STEP material metadata reports Aluminum 6061 with density 2700 kg/m^3, matching the local aluminum density constant in kb/materials/properties.yaml. Computed mass is 7.183457e-6 m^3 x 2700 kg/m^3 = 0.01940 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6K_fixed_bearing_mount.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 7183.457 mm^3, area 3791.252 mm^2, and bounding box 52.00 x 24.00 x 8.00 mm. Local assembly material extraction matched 6K_fixed_bearing_mount to material Aluminum 6061, Welded with density 2700 kg/m^3. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the complete per-unit physical mount for this BOM row."
    - "The reAM250 STEP material density is interpreted as kg/m^3, consistent with the material extractor note and the local density table."
  uncertainty_notes:
    - "CAD volume may omit very small edge breaks, threaded details, or finish thickness, but those effects are negligible at this tens-of-grams scale."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6K_fixed_bearing_mount reports material 'Aluminum 6061, Welded' and density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata identifies the alloy family/grade but does not state temper, surface treatment, or whether the 'Welded' material label reflects stock/process history rather than a weld in this small part."
how_to_make:
  summary: "Make as a small CNC-machined 6061 aluminum bearing-mount plate/block"
  manufacturing_steps:
    - "Start from 6061 aluminum plate or bar stock slightly larger than the 52 x 24 x 8 mm finished envelope."
    - "CNC mill the outside profile, relieved/chamfered end features, and flat bearing-mount surfaces."
    - "Drill and circular-interpolate or bore the large bearing pocket/through-hole, then add any smaller mounting holes or fastener features required by the assembly drawing."
    - "Deburr, optionally anodize or conversion-coat, clean, and inspect bore position/diameter and fixed-side bearing reference surfaces before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6K_fixed_bearing_mount.step; research/ream250_bom/ream250_bom_row_0187_6K__views_2x2.png; https://mccormickind.com/aluminum-brake-shaft-bearing-blocks/"
    cited_fact_or_basis: "CAD evidence shows a one-piece 52.00 x 24.00 x 8.00 mm Aluminum 6061 mount with a large circular bearing feature and chamfered/relieved geometry. McCormick Industries describes comparable aluminum brake shaft bearing blocks as machined from 6061-T6 aluminum billet with precision-drilled mounting holes and a central bearing bore. targeted_web_search: query tried 'fixed bearing mount aluminum 6061 machined block bearing support'; results found general 6061 bearing-block machining examples but no row-specific vendor drawing or manufacturing process for 6K_fixed_bearing_mount."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible CAD geometry is a single aluminum machined part rather than a casting or multi-part external bearing block"
    - "Low-volume KB planning favors CNC machining from stock over casting because the part is small, flat, and has a precision bearing feature."
  uncertainty_notes:
    - "Exact tolerances, bearing fit class, surface finish, hole callouts, and heat-treatment/temper requirements are not present in the row-level evidence."
kb_implications:
  - "item_granularity: simple_part - Model 6K as a reusable small machined Aluminum 6061 fixed bearing-mount part; keep bearing, shaft, and fasteners as separate BOM rows or later generic hardware items."
---
