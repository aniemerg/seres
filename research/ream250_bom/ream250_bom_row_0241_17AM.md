---
row_identity:
  item: "17AM"
  cad_file: "17AM_sheet_back"
  source_row_number: 241
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin back sheet or cover panel for the reAM250 17A hood/frame area."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AM_sheet_back.step; research/ream250_bom/ream250_bom_row_0241_17AM__views_2x2.png"
    cited_fact_or_basis: "BOM row 241 lists item 17AM, quantity 1, CAD file 17AM_sheet_back. The manifest maps it to gold_export/parts/17AM_sheet_back.step as a matched_existing part. FreeCAD measured one solid with bounding box 2.00 x 443.00 x 281.00 mm. The rendered contact sheet shows a plain flat rectangular sheet/panel."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name suffix sheet_back and the flat rectangular CAD geometry indicate a rear cover or backing panel rather than a mechanism or purchased module."
  uncertainty_notes: []
mass:
  value_kg: 1.954
  basis: "Per physical item; BOM quantity is 1, so row total is also about 1.954 kg. FreeCAD volume 248966.000 mm^3 converted to 0.000248966 m^3; multiplied by generic steel density 7850 kg/m^3 as a conservative metal-sheet scenario. If aluminum were used instead, the same CAD volume would be about 0.672 kg using 2700 kg/m^3."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AM_sheet_back.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 248966.000 mm^3 and bounding box 2.00 x 443.00 x 281.00 mm. The local density table lists steel at 7850 kg/m^3 and aluminum at 2700 kg/m^3. targeted_web_search: searched \"17AM_sheet_back material\", \"17AM sheet_back reAM250 material\", \"reAM250 17AM sheet_back\", and \"17A0_hood sheet_back material\"; found duplicate BOM text and no row-specific vendor/material/mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a metal sheet/panel because of the sheet_back name, 2 mm sheet geometry, and hood/frame context."
    - "Generic steel density is used for the reported value as a conservative mass estimate for a thin machine cover panel."
  uncertainty_notes:
    - "The CAD volume is measured, but the material is not; aluminum or another sheet material would change mass by roughly a factor of three."
material:
  primary_material: "unknown metal/alloy sheet material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AM_sheet_back.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 241 identifies the row as 17AM_sheet_back. FreeCAD measured a 2.00 mm thick rectangular sheet-like solid. Assembly STEP material extraction for 17AM_sheet_back returned only placeholder material Generic with density 1000.0, which the task workflow treats as unresolved material evidence. targeted_web_search: searched \"17AM_sheet_back material\", \"17AM sheet_back reAM250 material\", \"reAM250 17AM sheet_back\", and \"17A0_hood sheet_back material\"; found duplicate BOM text and no row-specific vendor/material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A back sheet in this mechanical hood/frame context is most plausibly a metal sheet panel; no specific alloy or grade is claimed."
  uncertainty_notes:
    - "No BOM field, STEP metadata, vendor link, or targeted search result states the actual material family or alloy."
how_to_make:
  summary: "Cut a 2 mm sheet-metal panel to the CAD rectangle, then deburr and finish as needed for the hood/back cover assembly."
  manufacturing_steps:
    - "Select flat metal sheet stock matching the required final material and 2.00 mm thickness."
    - "Cut the rectangular blank to approximately 443.00 x 281.00 mm by shear, saw, waterjet, or laser cutting."
    - "Deburr the edges and check flatness and final dimensions."
    - "Apply any required surface finish or protective coating before installation in the hood assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AM_sheet_back.step; research/ream250_bom/ream250_bom_row_0241_17AM__views_2x2.png"
    cited_fact_or_basis: "CAD geometry is one simple solid with bounding box 2.00 x 443.00 x 281.00 mm. The contact sheet shows a plain rectangular sheet with no visible holes, slots, bends, flanges, or attached subparts. targeted_web_search: searched \"17AM_sheet_back material\", \"17AM sheet_back reAM250 material\", \"reAM250 17AM sheet_back\", and \"17A0_hood sheet_back material\"; found duplicate BOM text and no row-specific vendor/manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because no holes, bends, or complex features are visible, a simple sheet-cutting route is sufficient for KB-level modeling."
    - "Final edge finish and coating requirements are not specified by the row and would be chosen from the surrounding hood assembly requirements."
  uncertainty_notes:
    - "If hidden mounting features or a specific coating are required outside this per-part STEP, the manufacturing route may need extra drilling, forming, or finishing steps."
kb_implications:
  - "item_granularity: simple_part - one plain sheet/panel part, likely modeled as a cut sheet-metal component rather than a purchased module or assembly."
---
