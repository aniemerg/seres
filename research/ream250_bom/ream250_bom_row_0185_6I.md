---
row_identity:
  item: "6I"
  cad_file: "6I_clamping_plate_front"
  source_row_number: 185
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Front clamping plate in reAM250 BOM group 6; it is a thin custom plate that likely clamps or retains adjacent front-side powder handling or carriage hardware while providing clearance through the large central rounded slot."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6I_clamping_plate_front.step; research/ream250_bom/ream250_bom_row_0185_6I__views_2x2.png"
    cited_fact_or_basis: "BOM row 185 and manifest row 185 identify item 6I as 6I_clamping_plate_front, quantity 1, with matched part STEP gold_export/parts/6I_clamping_plate_front.step. FreeCAD measured one solid with bounding box 80.00 x 42.00 x 4.00 mm. The rendered contact sheet shows a thin rectangular plate with a large rounded rectangular/obround center opening, small mounting holes near the ends/corners, and relieved triangular lightening or clearance features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD row name's 'clamping_plate_front' is interpreted as the functional role of this row, paired with adjacent row 186's back clamping plate."
  uncertainty_notes:
    - "The row-level CAD does not include the mating rear clamping plate, fasteners, seals, chute, or carriage context, so the exact clamped component is inferred from row name, adjacent BOM context, and plate geometry."
mass:
  value_kg: 0.0258
  basis: "Per unit for one physical clamping plate; BOM quantity is 1, so row total is also about 0.0258 kg. FreeCAD volume is 9571.780 mm^3 = 9.571780e-6 m^3. Assembly STEP material metadata reports Aluminum 6061 with density 2700 kg/m^3, matching the local aluminum density constant in kb/materials/properties.yaml. Computed mass is 9.571780e-6 m^3 x 2700 kg/m^3 = 0.02584 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6I_clamping_plate_front.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 9571.780 mm^3, area 6266.405 mm^2, and bounding box 80.00 x 42.00 x 4.00 mm. Local assembly material extraction matched 6I_clamping_plate_front to material Aluminum 6061 with density 2700 kg/m^3. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the complete per-unit physical clamping plate for this BOM row."
    - "The reAM250 STEP material density is interpreted as kg/m^3, consistent with the material extractor note and the local density table."
  uncertainty_notes:
    - "CAD volume may omit tiny edge breaks, countersinks, threaded details, or finish thickness, but those effects are negligible for a roughly 26 g aluminum plate."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6I_clamping_plate_front reports material Aluminum 6061 and density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata identifies the alloy family/grade but does not state temper, surface treatment, or whether any inserts or pads are installed separately from this plate row."
how_to_make:
  summary: "Make as a small CNC-machined or profile-cut 6061 aluminum clamping plate"
  manufacturing_steps:
    - "Start from 6061 aluminum sheet or plate stock slightly thicker/larger than the 80 x 42 x 4 mm finished envelope."
    - "Waterjet, laser, router, or CNC mill the outer profile, large central rounded slot, and visible clearance/lightening cutouts."
    - "Drill and countersink or spotface the small mounting holes as required by the assembly drawing."
    - "Deburr all edges, optionally anodize or conversion-coat, clean, and inspect thickness, slot position, and hole locations before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6I_clamping_plate_front.step; research/ream250_bom/ream250_bom_row_0185_6I__views_2x2.png; web search queries"
    cited_fact_or_basis: "CAD evidence shows a one-piece 80.00 x 42.00 x 4.00 mm Aluminum 6061 plate with a large rounded slot and small mounting holes. targeted_web_search: queries tried '\"6I_clamping_plate_front\"', '\"reAM250\" \"clamping_plate_front\"', and '\"reAM250\" \"6I\" \"clamping plate\"'; results found mirrored reAM250 BOM listings but no row-specific vendor drawing, drawing note, or manufacturing process for 6I_clamping_plate_front."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible CAD geometry is a single custom flat aluminum plate rather than a casting, printed part, or external catalog clamp"
    - "Low-volume KB planning favors cutting/machining from plate stock because the part is thin, flat, and contains 2D profile features plus drilled holes."
  uncertainty_notes:
    - "Exact tolerances, fastener hole callouts, surface finish, edge break, and surface-treatment requirements are not present in the row-level evidence."
kb_implications:
  - "item_granularity: simple_part - Model 6I as one custom thin Aluminum 6061 clamping plate; keep mating fasteners, seals, bearings, and front/back assembly context as separate BOM rows or later reusable hardware items."
---
