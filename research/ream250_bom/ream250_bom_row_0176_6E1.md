---
row_identity:
  item: "6E1"
  cad_file: "6E1_plate_left"
  source_row_number: 176
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin left-side stainless plate for the row-6 powder/conveyor subassembly, likely serving as a side wall, cover, or spacer plate paired with the adjacent right, front, and back plates."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E1_plate_left.step; research/ream250_bom/ream250_bom_row_0176_6E1__views_2x2.png"
    cited_fact_or_basis: "BOM row 176 names item 6E1 as 6E1_plate_left with quantity 1; manifest row 176 maps it to a matched part STEP; neighboring BOM rows 177-179 are 6E2_plate_right, 6E3_plate_front, and 6E4_plate_back; FreeCAD measured one thin solid with a 1.00 x 118.50 x 268.00 mm bounding box; the rendered preview shows a flat rectangular plate."
    evidence_basis: "bom_provided"
  assumptions:
    - "The left/right/front/back naming is treated as subsystem orientation, not as a globally unique machine side."
  uncertainty_notes:
    - "The leased row has no parent assembly name, fastener-hole pattern, or mating interface detail, so the exact load path and whether the plate is a cover, wall, or spacer remain uncertain."
mass:
  value_kg: 0.254064
  basis: "Per-unit mass for quantity 1. CAD volume 31758.000 mm^3 = 3.1758e-5 m^3; assembly STEP material metadata gives Stainless Steel density 8000 kg/m^3, yielding 0.254064 kg for one plate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E1_plate_left.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD shape read measured one solid, volume 31758.000 mm^3, area 64289.000 mm^2, and bounding box 1.00 x 118.50 x 268.00 mm; local assembly STEP material extraction matched product 6E1_plate_left to Stainless Steel with density 8000.0 in the reAM250 export's kg/m^3-like density convention."
    evidence_basis: "bom_provided"
  assumptions:
    - "The matched CAD solid represents one physical item for BOM quantity 1."
    - "The STEP material density is applied uniformly to the measured CAD volume."
  uncertainty_notes:
    - "Mass excludes any separate fasteners, adhesive, coatings, or weld material that may attach the plate in the parent assembly."
material:
  primary_material: "Stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6E1_plate_left returned material Stainless Steel and density 8000.0 in the reAM250 export's kg/m^3-like density convention."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata does not identify a stainless grade such as 304, 316, or 1.4301."
how_to_make:
  summary: "Make from approximately 1 mm stainless sheet by cutting the rectangular profile, deburring, flattening if needed, and cleaning or passivating before assembly; Cut sheet-metal plate is also plausible"
  manufacturing_steps:
    - "Select stainless sheet stock about 1.0 mm thick."
    - "CNC laser cut, shear, or otherwise blank a roughly 118.5 x 268.0 mm rectangular plate from the sheet."
    - "Deburr and lightly break cut edges; keep the plate flat and free of sharp edges for handling and mating surfaces."
    - "Clean and optionally passivate or finish the stainless plate before installing it with the adjacent row-6 plates."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E1_plate_left.step; https://www.pcbway.com/rapid-prototyping/Sheet-metal/Laser-Cutting.html"
    cited_fact_or_basis: "CAD evidence shows a simple 1.00 mm thick stainless rectangular plate; PCBWay describes CNC laser cutting as a sheet-metal process for metal sheets including stainless steel, with laser cutting used to create 2D flats from sheet material and listed allowable sheet thickness from 0.5-10 mm. targeted_web_search: queries tried: 'stainless steel sheet metal plate laser cutting deburring manufacturing process' and 'custom stainless steel sheet metal plate laser cutting CNC machining flat plate manufacturing'; result: found generic sheet-metal cutting routes for stainless sheet, but no row-specific manufacturing drawing or process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the part is a flat 1 mm plate with no visible bends, holes, bosses, or machined pockets in the preview, sheet cutting plus edge finishing is sufficient for the modeled manufacturing route."
    - "The part can be modeled as a custom flat plate rather than a calibrated vendor module."
  uncertainty_notes:
    - "No tolerance, surface finish, edge radius, passivation, or attachment specification was available from the BOM row or local CAD package."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable flat stainless sheet/plate part family for row-6 side/front/back plates rather than as a purchased module or separate assembly."
---

