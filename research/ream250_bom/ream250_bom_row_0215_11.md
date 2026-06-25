---
row_identity:
  item: "11"
  cad_file: "11_rack_chamber"
  source_row_number: 215
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Large stainless rack/frame for the reAM250 chamber subsystem; the open rectangular structure provides the chamber support envelope and mounting frame for neighboring chamber plates, seals, doors, and chamber-side hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/11_rack_chamber.step; research/ream250_bom/ream250_bom_row_0215_11__views_2x2.png"
    cited_fact_or_basis: "BOM row 215 identifies item 11, quantity 1, CAD file 11_rack_chamber. Manifest row 215 maps the same row to gold_export/parts/11_rack_chamber.step as a matched part. FreeCAD measured one solid with a 900.00 x 580.00 x 460.00 mm bounding box, and the rendered contact sheet shows an open rectangular rack/frame."
    evidence_basis: "bom_provided"
  assumptions:
    - "The name rack_chamber and neighboring chamber BOM rows are interpreted as a chamber support-frame role rather than a sealed pressure vessel wall."
  uncertainty_notes:
    - "The CAD and BOM do not expose mating constraints, so exact attachment points and carried loads are not resolved."
mass:
  value_kg: 85.68
  basis: "Per unit. BOM quantity is 1, so row total is also about 85.68 kg. FreeCAD volume 10709384.798 mm^3 = 0.010709384798 m^3; assembly STEP material metadata reports Stainless Steel density 8000 kg/m^3; computed mass = 0.010709384798 m^3 * 8000 kg/m^3 = 85.675 kg, rounded to 85.68 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/11_rack_chamber.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 10709384.798 mm^3, area 1419183.077 mm^2, and bounding box 900.00 x 580.00 x 460.00 mm. The local assembly STEP material extractor matched 11_rack_chamber to material Stainless Steel with density 8000.0. The local density table lists stainless_steel density_kg_per_m3: 8000."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical rack/frame volume."
    - "The assembly STEP stainless steel density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass is CAD-derived and excludes any separate chamber plates, seals, doors, fasteners, or mounted hardware represented by other BOM rows."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 11_rack_chamber to material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a stainless steel family but not a specific alloy grade, heat treatment, or surface finish."
how_to_make:
  summary: "Make as a custom stainless structural chamber rack: cut stainless tube/profile or formed frame members to length, fixture the rectangular frame, weld or otherwise join the corners and cross members, machine or finish mounting faces as needed, clean/passivate, and inspect the large frame envelope."
  manufacturing_steps:
    - "Cut stainless steel structural profiles, tube sections, or formed members to the lengths needed for the 900 x 580 x 460 mm rack envelope."
    - "Fixture the rectangular frame so corners, cross members, and mounting faces stay square during joining."
    - "Weld, braze, or mechanically join the frame members; for a local self-manufacturing route, welded stainless fabrication is the primary planning assumption."
    - "Machine, drill, tap, or face any mounting interfaces required by adjacent chamber plates, seals, door hardware, and chamber subsystem components."
    - "Deburr, clean, and passivate or otherwise finish stainless surfaces, then inspect overall envelope, squareness, and mounting alignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/11_rack_chamber.step; research/ream250_bom/ream250_bom_row_0215_11__views_2x2.png"
    cited_fact_or_basis: "The STEP/contact sheet shows one large open rectangular stainless rack/frame with a 900.00 x 580.00 x 460.00 mm envelope and frame-like members. targeted_web_search: searched \"11_rack_chamber reAM250\", \"reAM250 rack chamber\", and \"11_rack_chamber stainless steel\" results found duplicate reAM250 BOM text and project-level reAM250 pages, but no row-specific fabrication drawing, tolerance callout, or vendor manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the large open stainless frame geometry and chamber-support role, not from a row-specific process sheet."
    - "Welded or joined stainless structural-profile fabrication is used as the KB planning route because the item is much larger than a simple machined solid block and has frame-like geometry."
  uncertainty_notes:
    - "Exact profile cross sections, weld details, machining callouts, leak/vacuum cleanliness requirements, and inspection tolerances are not specified by the BOM row or STEP metadata."
kb_implications:
  - "item_granularity: simple_part - Model as one custom stainless structural chamber rack/frame made from stainless profile or tube stock with cut/fixture/join/finish operations; do not split into a sub-BOM until chamber-frame fabrication becomes a detailed modeling target."
---

Research result for reAM250 BOM row 215.
