---
row_identity:
  item: "6J"
  cad_file: "6J_clamping_plate_back"
  source_row_number: 186
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Back clamping plate for the reAM250 6J row: a thin rectangular plate with a large central rounded slot/opening and small corner holes, likely spreading clamping load and providing a rear bearing/clamp face for an adjacent mechanism."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6J_clamping_plate_back.step; research/ream250_bom/ream250_bom_row_0186_6J__views_2x2.png"
    cited_fact_or_basis: "BOM row 186 names item 6J as 6J_clamping_plate_back with quantity 1. Manifest row 186 maps it to a matched part STEP. FreeCAD/rendered preview shows one thin plate, bbox about 80.00 x 42.00 x 4.00 mm, with a central rounded opening and small corner holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'clamping_plate_back' describes the intended role, while the CAD opening and mounting holes indicate a plate used as a clamp/backing element rather than a sealed cover."
  uncertainty_notes:
    - "No adjacent assembly context or drawing callouts were present in the BOM row, so the exact mating component and load path remain uncertain."
mass:
  value_kg: 0.0258
  basis: "Per unit. Quantity in BOM row is 1, so row total is also about 0.0258 kg. FreeCAD measured volume 9571.780 mm^3 = 9.571780e-6 m^3; assembly STEP metadata reports Aluminum 6061 density 2700 kg/m^3; computed mass = 9.571780e-6 m^3 * 2700 kg/m^3 = 0.025844 kg, rounded to 0.0258 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6J_clamping_plate_back.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 9571.780 mm^3 and bbox about 80.00 x 42.00 x 4.00 mm. Local assembly STEP material extraction for product 6J_clamping_plate_back returned material Aluminum 6061 and density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical part volume."
    - "The assembly STEP material density is interpreted as kg/m^3-like density, consistent with the extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes any coating, screws, inserts, or separate hardware not represented in this row's part STEP."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6J_clamping_plate_back returned material 'Aluminum 6061' with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM CSV itself does not state a material; the material comes from local assembly STEP metadata."
how_to_make:
  summary: "Machine or waterjet/laser-cut the profile from thin Aluminum 6061 plate stock, then finish the central rounded slot, perimeter, and small mounting holes by CNC milling/drilling and deburr the edges."
  manufacturing_steps:
    - "Start from approximately 4 mm Aluminum 6061 plate or flat stock."
    - "Cut the rectangular outline and rough central rounded opening by CNC milling, waterjet, or laser routing suitable for aluminum plate."
    - "Finish-machine the slot, small holes, and critical clamp surfaces to the required fit."
    - "Deburr and clean; add surface treatment only if later assembly requirements call for it."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6J_clamping_plate_back.step; https://www.chalcoaluminum.com/knowledge/6061-aluminum-tooling-plate-block-2504-lx/"
    cited_fact_or_basis: "CAD evidence: one thin Aluminum 6061 plate with through features and bbox about 80.00 x 42.00 x 4.00 mm. targeted_web_search: query 'Aluminum 6061 plate CNC machining clamping plate manufacturing' found general supplier/manufacturing references for 6061 aluminum plate/block used in CNC machining, fixtures, equipment platforms, and custom mechanical components, but no row-specific reAM250 manufacturing drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the part is a small flat aluminum plate with cutouts and holes, subtractive manufacture from plate stock is the simplest plausible route."
    - "No evidence was found for casting, additive manufacturing, or a purchased catalog part for this row."
  uncertainty_notes:
    - "The exact tolerances, surface finish, and edge break requirements are not available from the BOM or STEP export."
kb_implications:
  - "item_granularity: simple_part - Model as one machined Aluminum 6061 clamping/backing plate rather than a purchased module or multi-part assembly."
---
