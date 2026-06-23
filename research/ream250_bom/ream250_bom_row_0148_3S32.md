---
row_identity:
  item: "3S32"
  cad_file: "3S32_part_2"
  source_row_number: 148
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin-wall gas outlet pipe segment, part 2 of the 3S31-3S35 gas outlet pipe group; the CAD shows a hollow square duct section with an angled end, used to route gas through the multi-piece outlet path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S32_part_2.step; research/ream250_bom/ream250_bom_row_0148_3S32__views_2x2.png"
    cited_fact_or_basis: "BOM row 148 lists item 3S32, quantity 1, CAD file 3S32_part_2, description 'gas outlet pipe: part 2'. The manifest maps row 148 to one matched_existing part STEP. FreeCAD measured one solid with a 60.00 x 60.00 x 120.00 mm bounding box, and the rendered preview shows a hollow square duct/tube segment with an angled end."
    evidence_basis: "bom_provided"
  assumptions:
    - "The phrase 'gas outlet pipe: part 2' is interpreted as one segment in the adjacent 3S31-3S35 multi-piece gas outlet pipe sequence."
  uncertainty_notes: []
mass:
  value_kg: 0.347
  basis: "FreeCAD volume 44148.294 mm^3 = 4.4148294e-5 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.3466 kg per part, rounded to 0.347 kg. Stainless steel at 8000 kg/m^3 would give about 0.353 kg. BOM quantity is 1, so per-unit mass and row total are the same."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S32_part_2.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 44148.294 mm^3, area 45152.754 mm^2, and bounding box 60.00 x 60.00 x 120.00 mm. The local density table lists steel at 7850 kg/m^3 and stainless_steel at 8000 kg/m^3. targeted_web_search: searched \"3S32_part_2 gas outlet pipe material\", \"3S32 gas outlet pipe reAM250\", \"reAM250 gas outlet pipe material\", and \"3S32_part_2\"; results were duplicate/public BOM listings only and did not provide row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one duct segment."
    - "Generic steel density is used as a conservative metal duct estimate because neither the BOM nor STEP metadata resolves the alloy."
  uncertainty_notes:
    - "Material is not directly specified; if this duct segment is aluminum, the same CAD volume would be about 0.119 kg using the local aluminum density of 2700 kg/m^3."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0148_3S32__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 148 identifies the part as 'gas outlet pipe: part 2' but provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S32_part_2 returned only placeholder material 'Generic' with density 1000.0. The rendered preview shows a rigid thin-wall duct form. targeted_web_search: searched \"3S32_part_2 gas outlet pipe material\", \"3S32 gas outlet pipe reAM250 material\", \"reAM250 gas outlet pipe material\", and \"3S32_part_2\"; results were duplicate/public BOM listings only and did not resolve material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A gas outlet pipe segment in this machine is modeled as sheet metal because the CAD geometry is a rigid hollow square duct and the row sits among other gas/vacuum outlet hardware."
  uncertainty_notes:
    - "No source resolves the exact material family or grade; later KB modeling should keep this as a broad metal/alloy sheet part unless a drawing or assembly material note identifies the alloy."
how_to_make:
  summary: "Make as a custom sheet-metal duct segment: cut sheet blanks for the square duct walls, form or bend the angled/tapered geometry, join the seam and corners, then trim, deburr, clean, and inspect the openings for fit-up in the gas outlet assembly."
  manufacturing_steps:
    - "Cut sheet-metal blank geometry for the duct walls and angled end features."
    - "Bend or form the sheet to the roughly 60 x 60 x 120 mm hollow square duct geometry shown in CAD."
    - "Join seams and corners by welding, brazing, or folded/sealed seams according to gas-tightness requirements."
    - "Trim, deburr, clean, and inspect the square openings and mating edges before assembling with the neighboring gas outlet pipe segments."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S32_part_2.step; research/ream250_bom/ream250_bom_row_0148_3S32__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 60.00 x 60.00 x 120.00 mm bounding box. The preview shows a hollow square duct/tube segment with thin walls and an angled end. targeted_web_search: searched \"3S32_part_2 gas outlet pipe manufacturing\", \"3S32 gas outlet pipe reAM250 drawing\", \"reAM250 gas outlet pipe material\", and \"3S32_part_2\"; results were duplicate/public BOM listings only and did not provide a row-specific fabrication drawing or process note."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD form represents a fabricated duct shell, so sheet cutting/forming plus seam joining is the dominant route."
  uncertainty_notes:
    - "The CAD and BOM do not state wall thickness callouts, tolerances, surface finish, or gas-tightness class; those details determine whether folded seams are sufficient or welded seams are required."
kb_implications:
  - "item_granularity: simple_part - Model as one custom fabricated sheet-metal gas outlet pipe segment, with assembly-level joining handled by the larger 3S outlet group."
---

Research result for reAM250 BOM row 148.
