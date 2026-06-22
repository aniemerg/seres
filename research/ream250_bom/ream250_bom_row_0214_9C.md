---
row_identity:
  item: "9C"
  cad_file: "9C_top_spacer"
  source_row_number: 214
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Square top spacer or standoff plate in the reAM250 top structural/frame group, likely providing a fixed 10 mm separation and central clearance or fastener pass-through between adjacent top profile members."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9C_top_spacer.step; research/ream250_bom/ream250_bom_row_0214_9C__views_2x2.png"
    cited_fact_or_basis: "BOM row 214 lists item 9C, quantity 1, CAD file 9C_top_spacer, in BOM group 10 after 9A_top_square_profile and 9B_profile_60x60_960. The manifest maps row 214 to gold_export/parts/9C_top_spacer.step as a matched_existing part. FreeCAD measured one solid with bounding box about 80.00 x 10.00 x 80.00 mm, and the contact-sheet preview shows a square plate/spacer with X-shaped ribbing and a central circular through-hole."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename top_spacer and neighboring top-profile rows are interpreted as the local structural context."
    - "The 10.00 mm bounding-box dimension is interpreted as the spacer thickness."
  uncertainty_notes:
    - "The row-level BOM and CAD do not identify the exact mating faces or whether the central hole carries a fastener, clearance feature, or alignment feature."
mass:
  value_kg: 0.169
  basis: "FreeCAD volume 62672.677 mm^3 = 6.2672677e-5 m^3. Using a nominal aluminum-family density constant of 2700 kg/m^3 from kb/materials/properties.yaml gives about 0.169 kg per spacer. BOM quantity is 1, so the row total is also about 0.169 kg. If the same CAD volume is steel at 7850 kg/m^3, the mass would be about 0.492 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9C_top_spacer.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 62672.677 mm^3, area 16142.942 mm^2, and bounding box about 80.00 x 10.00 x 80.00 mm. Local assembly STEP material extraction for product 9C_top_spacer returned only material Generic with density 1000.0, which is placeholder metadata. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3 and generic steel density as 7850 kg/m^3. targeted_web_search: searched \"9C_top_spacer\", \"reAM250 9C top spacer\", and \"reAM250 top spacer material\"; found duplicate BOM/project pages but no row-specific mass, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Aluminum-family density is used as the planning value because this is a custom top-frame spacer adjacent to a Bosch Rexroth strut-profile row and no high-wear, hot-zone, or vacuum-sealing duty is stated."
    - "The CAD solid volume is treated as the physical volume of one row item."
  uncertainty_notes:
    - "The material is unresolved; a steel-family part would be roughly 0.492 kg instead of 0.169 kg."
    - "The full assembly STEP contains placeholder Generic material metadata, so CAD material data cannot confirm the density choice."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9C_top_spacer.step; web targeted search"
    cited_fact_or_basis: "BOM row 214 has blank manufacturer, product, link, material-family, and grade fields. Local assembly STEP material extraction for product 9C_top_spacer reports only Generic with density 1000.0, which is placeholder metadata under the task acceptance criteria. The CAD shows a rigid square structural spacer. targeted_web_search: searched \"9C_top_spacer material\", \"reAM250 9C_top_spacer\", \"reAM250 top spacer drawing\", and \"reAM250 top spacer material\"; found duplicate BOM/project pages and no row-specific drawing, alloy, or vendor page."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal/alloy family is inferred from the rigid spacer role, frame-adjacent context, and X-ribbed plate geometry."
    - "Aluminum alloy is plausible for later planning because the neighboring 9B row is a Bosch Rexroth strut-profile item, but this is not row-specific material evidence."
  uncertainty_notes:
    - "The specific alloy or grade is unresolved; aluminum, steel, or stainless steel remain possible until a source drawing, CAD material assignment, or designer note is found."
how_to_make:
  summary: "Make as a simple custom spacer from metal plate or billet: cut the square 80 x 80 x 10 mm blank, machine the central through-hole and ribbed or pocketed relief faces if required, deburr, and inspect thickness and mating faces."
  manufacturing_steps:
    - "Cut or mill stock to the 80 x 80 mm square outer profile and finish to the 10 mm spacer thickness."
    - "Drill, bore, or mill the central circular through-hole to the CAD-specified location."
    - "Machine the X-ribbed or recessed face features if they are functional rather than cosmetic/export artifacts."
    - "Deburr edges and verify flatness, thickness, and hole location before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9C_top_spacer.step; research/ream250_bom/ream250_bom_row_0214_9C__views_2x2.png; web targeted search"
    cited_fact_or_basis: "The STEP is one solid with an 80.00 x 10.00 x 80.00 mm bounding box; the contact-sheet preview shows a square spacer-like plate with a central through-hole and X-shaped ribs or relief features. targeted_web_search: searched \"9C_top_spacer manufacturing\", \"reAM250 9C_top_spacer drawing\", and \"reAM250 top spacer CAD\"; found duplicate BOM/project pages and no row-specific manufacturing drawing or process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A subtractive plate or billet route is selected because the geometry is a compact prismatic spacer with simple external dimensions and one visible circular through-feature."
    - "The X-shaped features are treated as machinable relief, stiffening, or pocket geometry unless a later drawing shows they are cosmetic CAD artifacts."
  uncertainty_notes:
    - "No source states the actual manufacturing process; additive manufacture, casting, or waterjet plus secondary machining remain possible but are not required by the visible geometry."
kb_implications:
  - "item_granularity: simple_part - model as one reusable custom metal spacer/standoff plate with unresolved alloy, not as a purchased module or multi-part assembly."
---
