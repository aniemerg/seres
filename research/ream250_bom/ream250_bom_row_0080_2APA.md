---
row_identity:
  item: "2APA"
  cad_file: "2APA_spring_block_right"
  source_row_number: 80
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Right-side spring block for the reAM250 build-platform/heating-plate area; model as a long narrow mechanical support or preload block paired with the front, back, and left spring blocks."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APA_spring_block_right.step; research/ream250_bom/ream250_bom_row_0080_2APA__views_2x2.png"
    cited_fact_or_basis: "BOM row 80 lists item 2APA, quantity 1, CAD file '2APA_spring_block_right'. Nearby BOM rows 79, 81, and 82 list matching front, back, and left spring blocks. The manifest maps row 80 to one matched_existing part STEP. FreeCAD measured one solid with a bounding box about 251.00 x 22.00 x 15.00 mm; the rendered preview shows a long narrow block with small end features and a tapered or relieved face."
    evidence_basis: "bom_provided"
  assumptions:
    - "The four named spring blocks form a set around the adjacent spring plate, assembly plate, heating plate, and build-platform rows."
    - "The visible long block geometry is interpreted as a mechanical support or preload/contact block rather than an electronic, sensor, or purchased module."
  uncertainty_notes:
    - "The CAD and BOM naming identify the part role only broadly; they do not show the exact mating spring interface, preload force, or contact faces."
mass:
  value_kg: 0.40
  basis: "FreeCAD measured volume 50480.728 mm^3, which is 5.048073e-5 m^3. Using generic steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 0.396 kg per unit, rounded to 0.40 kg. Quantity is 1, so the row total is also about 0.40 kg. If later material evidence shows aluminum instead, the same CAD volume would be about 0.136 kg using 2700 kg/m^3."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APA_spring_block_right.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 50480.728 mm^3 volume, 19464.674 mm^2 area, and about 251.00 x 22.00 x 15.00 mm bounding box. The local density table lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. Assembly STEP material extraction for product 2APA_spring_block_right returned only placeholder material Generic with density 1000.0. targeted_web_search: searched '2APA_spring_block_right material', '2APA spring_block_right reAM250', 'reAM250 spring_block_right', and 'spring block reAM250 material'; found public reAM250 project/BOM context and unrelated pages, but no row-specific material, vendor, or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported single-solid STEP volume is used as the physical per-unit volume for this custom block."
    - "A steel-like density is used as the conservative default for a narrow machined block in a heated, mechanically loaded build-platform region."
  uncertainty_notes:
    - "Mass is material-sensitive; if the block is aluminum rather than steel, the per-unit mass would be roughly one third of the stated value."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0080_2APA__views_2x2.png"
    cited_fact_or_basis: "BOM row 80 names the part '2APA_spring_block_right' but provides no manufacturer, product ID, material family, grade, or link URL. Assembly STEP material extraction for product 2APA_spring_block_right returned only placeholder material Generic with density 1000.0. The preview shows a long block-like solid compatible with a machined metal component. targeted_web_search: searched '2APA_spring_block_right material', '2APA spring_block_right reAM250', 'reAM250 spring_block_right', and 'spring block reAM250 material'; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal or alloy is inferred from the block geometry, spring-block naming, and location among build-platform/heating-plate mechanical rows."
  uncertainty_notes:
    - "No BOM field, STEP material metadata, vendor page, or row-specific web result identified the actual grade or whether the block is steel, stainless steel, or aluminum."
how_to_make:
  summary: "Machine the spring block from rectangular metal bar or plate stock, creating the long block profile, end reliefs/radii, and tapered or relieved face, then deburr and inspect fit against the spring-block assembly."
  manufacturing_steps:
    - "Select rectangular steel, stainless steel, or aluminum stock sized slightly above the 251 x 22 x 15 mm bounding envelope."
    - "Saw or mill the blank to length and square the reference faces."
    - "Mill the long tapered or relieved face and any shallow side/end details visible in the STEP geometry."
    - "Deburr edges and inspect length, width, thickness, flatness, and fit with the adjacent spring block or spring plate interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APA_spring_block_right.step; research/ream250_bom/ream250_bom_row_0080_2APA__views_2x2.png"
    cited_fact_or_basis: "The STEP file contains one solid with a long 251.00 x 22.00 x 15.00 mm bounding box; the rendered preview shows a simple elongated block with planar faces, small end features, and a tapered or relieved face. targeted_web_search: searched '2APA_spring_block_right material', '2APA spring_block_right reAM250', 'reAM250 spring_block_right', and '2APA_spring_block_right manufacturing'; found no row-specific vendor or manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Subtractive machining from bar or plate stock is the representative low-volume route for this simple custom block."
    - "No casting, additive manufacturing, heat treatment, or calibrated purchased-module workflow is required unless later drawings specify a special material or spring property."
  uncertainty_notes:
    - "The exact tolerances, surface finish, and mating features are not specified by the BOM row or local STEP export."
kb_implications:
  - "item_granularity: simple_part - Treat as a custom machined metal block; consolidate with the other spring-block rows if later KB modeling can represent orientation variants with one reusable spring_block part."
---
