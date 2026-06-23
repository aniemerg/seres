---
row_identity:
  item: "3S35"
  cad_file: "3S35_part_5"
  source_row_number: 151
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin-wall gas outlet pipe segment, part 5 of the gas outlet pipe group; the CAD shows a tapered hollow square duct section used to route gas flow between neighboring outlet pieces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S35_part_5.step; research/ream250_bom/ream250_bom_row_0151_3S35__views_2x2.png"
    cited_fact_or_basis: "BOM row 151 lists item 3S35, quantity 1, CAD file 3S35_part_5, description 'gas outlet pipe: part 5'. FreeCAD measured one solid with a 60.00 x 60.00 x 80.00 mm bounding box; the rendered preview shows a tapered hollow square duct form."
    evidence_basis: "bom_provided"
  assumptions:
    - "The phrase 'gas outlet pipe: part 5' is interpreted as one segment in a multi-piece gas outlet duct assembly."
  uncertainty_notes: []
mass:
  value_kg: 0.183
  basis: "FreeCAD volume 23200.000 mm^3 = 2.320e-5 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.182 kg; stainless steel at 8000 kg/m^3 would give 0.186 kg. The reported value rounds this steel/stainless sheet-metal scenario to 0.183 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S35_part_5.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured CAD volume 23200.000 mm^3. The local density table lists steel at 7850 kg/m^3 and stainless_steel at 8000 kg/m^3. targeted_web_search: searched \"3S35_part_5 gas outlet pipe material\", \"3S35 gas outlet pipe reAM250 material\", \"reAM250 gas outlet pipe 3S35\", and \"3S35_part_5\"; found duplicate BOM text and no row-specific material or mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume is treated as the material volume for the thin-wall duct segment."
    - "A steel/stainless sheet-metal density is used because the row has no material field and the part is a gas outlet duct segment in equipment where metallic ducting is plausible."
  uncertainty_notes:
    - "Material is not directly specified; if the part is aluminum, the same CAD volume would be about 0.063 kg using the local aluminum density of 2700 kg/m^3."
material:
  primary_material: "metal sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 151 identifies the part as 'gas outlet pipe: part 5' but provides no material or manufacturer. Local assembly STEP material extraction for 3S35_part_5 returned only placeholder material 'Generic' with density 1000.0. targeted_web_search: searched \"3S35_part_5 gas outlet pipe material\", \"3S35 gas outlet pipe reAM250 material\", \"reAM250 gas outlet pipe 3S35\", and \"3S35_part_5\"; found duplicate BOM text and no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A thin-wall gas outlet pipe segment is modeled as sheet metal rather than polymer or ceramic because the CAD shape is a rigid duct and the row appears among vacuum/gas outlet hardware."
  uncertainty_notes:
    - "No source resolves the exact material family or grade; later KB modeling should keep this as a broad metal part unless a drawing or assembly note identifies the alloy."
how_to_make:
  summary: "Make as a simple sheet-metal duct transition: cut sheet blanks, bend or form the tapered walls, join the seam and corners, then trim and finish the square openings for fit-up in the gas outlet assembly."
  manufacturing_steps:
    - "Cut sheet-metal blank geometry for the four tapered duct faces and rim features."
    - "Bend/form the faces to the 60 mm square by 80 mm tall duct geometry shown in CAD."
    - "Join seams by welding, brazing, or folded/sealed seams depending on gas-tightness requirements."
    - "Deburr, clean, and inspect the openings and mating edges before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S35_part_5.step; research/ream250_bom/ream250_bom_row_0151_3S35__views_2x2.png"
    cited_fact_or_basis: "FreeCAD measured one solid with 60.00 x 60.00 x 80.00 mm bounding box; the preview shows a hollow tapered square duct with thin walls and open square end geometry. targeted_web_search: searched \"3S35_part_5 gas outlet pipe material\", \"3S35 gas outlet pipe reAM250 material\", \"reAM250 gas outlet pipe 3S35\", and \"3S35_part_5\"; found duplicate BOM text and no row-specific fabrication drawing or manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD form represents a fabricated duct shell, so sheet cutting/forming plus seam joining is the dominant route."
  uncertainty_notes:
    - "The CAD preview does not show specified seam design, wall thickness callouts, or gas-tightness tolerance; those details would determine whether folded seams are acceptable or welded seams are required."
kb_implications:
  - "item_granularity: simple_part - one fabricated thin-wall duct segment; model as a simple sheet-metal part unless later evidence shows it is part of a purchased outlet module."
---

Research result for reAM250 BOM row 151.
