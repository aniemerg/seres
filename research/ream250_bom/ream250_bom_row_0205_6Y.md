---
row_identity:
  item: "6Y"
  cad_file: "6Y_spacer_11_mm"
  source_row_number: 205
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small rectangular 11 mm spacer block in the recoater/motor-mount area, used to stand off or align a connected bracket, rail, or motor-mount feature with three through-fastener positions."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Y_spacer_11_mm.step; research/ream250_bom/ream250_bom_row_0205_6Y__views_2x2.png"
    cited_fact_or_basis: "BOM row 205 lists item 6Y, quantity 1, CAD file 6Y_spacer_11_mm. The manifest maps row 205 to gold_export/parts/6Y_spacer_11_mm.step as a matched_existing part. FreeCAD measured one solid with bounding box about 44.00 x 23.00 x 11.00 mm, and the contact-sheet preview shows a rectangular block with three through holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD filename's 11 mm value is interpreted as the spacer thickness, matching the measured 11.00 mm bounding-box dimension."
    - "The neighboring BOM rows 6S through 6X are treated as the local motor-mount and linear-guide connection context for this spacer."
  uncertainty_notes:
    - "The isolated part geometry does not show the mating assembly, so the exact installed interface and load path remain inferred from row context and visible hole pattern."
mass:
  value_kg: 0.0812
  basis: "FreeCAD volume 10347.976 mm^3 = 1.0347976e-5 m^3. Using a steel-family density constant of 7850 kg/m^3 gives about 0.0812 kg per spacer. BOM quantity is 1, so the row total is also about 0.0812 kg. If the part is aluminum instead, the same CAD volume would be about 0.0279 kg using 2700 kg/m^3."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Y_spacer_11_mm.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 10347.976 mm^3, area 3925.649 mm^2, and bounding box about 44.00 x 23.00 x 11.00 mm. Local assembly STEP material extraction for product 6Y_spacer_11_mm returned only material Generic with density 1000.0, which is placeholder metadata. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3 and aluminum density as 2700 kg/m^3. targeted_web_search: searched \"6Y_spacer_11_mm\", \"reAM250 6Y_spacer_11_mm\", \"reAM250 recoater spacer 11 mm material\", and \"6Y spacer_11_mm material\"; found duplicate BOM listings and no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported STEP solid is treated as the complete per-unit geometry for one BOM row 6Y part."
    - "A steel-family density is used as the planning value because the part is a small structural spacer in a motor-mount/linear-guide group and nearby researched row 6S2 is steel; this is not row-specific material evidence."
  uncertainty_notes:
    - "Material is unresolved for this row; the steel-density mass may be about 3x higher than an aluminum version of the same geometry."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 205 provides no manufacturer, product ID, or material note. Local assembly STEP material extraction for product 6Y_spacer_11_mm reports only Generic with density 1000.0, which is placeholder metadata under the task acceptance criteria. targeted_web_search: searched \"6Y_spacer_11_mm material\", \"reAM250 6Y spacer material\", \"reAM250 recoater spacer 11 mm\", and \"6Y_spacer_11_mm drawing\"; found duplicate BOM text and no row-specific drawing, alloy, or vendor page."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The spacer is modeled as a metallic structural part because the CAD shows a compact fastened block and the neighboring BOM group contains motor-mount and linear-guide connection parts."
  uncertainty_notes:
    - "The exact alloy, coating, and heat treatment are not resolved; downstream KB modeling should avoid encoding a specific grade from this row alone."
how_to_make:
  summary: "Make as a simple spacer by machining or cutting a small metal block to the 44 x 23 x 11 mm envelope, drilling the three through holes, deburring, and checking thickness and hole spacing."
  manufacturing_steps:
    - "Start from rectangular metal bar or plate stock slightly larger than 44 x 23 x 11 mm."
    - "Saw, mill, or waterjet the blank to the rectangular outer profile and finish the 11 mm spacer thickness if needed."
    - "Drill the three through holes visible in the CAD preview, then deburr both faces and hole edges."
    - "Inspect overall length, width, thickness, and hole positions against the STEP geometry before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Y_spacer_11_mm.step; research/ream250_bom/ream250_bom_row_0205_6Y__views_2x2.png; web targeted search"
    cited_fact_or_basis: "The STEP is one solid with a 44.00 x 23.00 x 11.00 mm bounding box; the contact-sheet preview shows a small rectangular block with three through holes. targeted_web_search: searched \"6Y_spacer_11_mm manufacturing\", \"reAM250 6Y_spacer_11_mm drawing\", and \"reAM250 spacer 11 mm CAD\"; found duplicate BOM listings and no row-specific manufacturing drawing or process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A cut, drilled, and deburred stock route is selected because the geometry is a simple prismatic spacer with visible through holes and no apparent bends, threads, electronics, or multi-part features."
    - "No special surface treatment is included because none is specified in BOM-side evidence."
  uncertainty_notes:
    - "The CAD preview does not provide tolerances, required flatness, coating, or installed fastener sizes, so the route is suitable for coarse KB planning rather than final fabrication instructions."
kb_implications:
  - "item_granularity: simple_part - model as one reusable simple metal spacer block with drilled holes, not as a purchased module or assembly."
---

Research result for reAM250 BOM row 205.
