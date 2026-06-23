---
row_identity:
  item: "17AJ"
  cad_file: "17AJ_sheet_front"
  source_row_number: 238
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin front sheet or cover strip for the 17A hood/frame area."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AJ_sheet_front.step; research/ream250_bom/ream250_bom_row_0238_17AJ__views_2x2.png"
    cited_fact_or_basis: "BOM row 238 lists item 17AJ, quantity 1, CAD file 17AJ_sheet_front. FreeCAD measured one solid with bounding box 2.00 x 32.00 x 634.40 mm. The rendered contact sheet shows a plain long thin rectangular sheet/strip."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name suffix sheet_front and the long thin rectangular CAD geometry indicate a front cover or sheet member rather than a mechanism or purchased module."
  uncertainty_notes: []
mass:
  value_kg: 0.319
  basis: "FreeCAD volume 40601.600 mm^3 converted to 4.06016e-5 m^3; multiplied by generic steel density 7850 kg/m^3 as a conservative metal-sheet scenario. If aluminum were used instead, the same CAD volume would be about 0.110 kg using 2700 kg/m^3."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AJ_sheet_front.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 40601.600 mm^3 and bounding box 2.00 x 32.00 x 634.40 mm. The local density table lists steel at 7850 kg/m^3 and aluminum at 2700 kg/m^3. targeted_web_search: searched \"17AJ_sheet_front material\", \"17AJ sheet_front reAM250 material\", \"reAM250 17AJ sheet_front\", and \"17AJ_sheet_front\"; found duplicate BOM text and no row-specific vendor/material/mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a metal sheet/strip because of the sheet_front name, thin rectangular CAD form, and frame-cover context."
    - "Generic steel density is used for the reported value as a conservative mass estimate for a thin machine cover strip."
  uncertainty_notes:
    - "The CAD volume is measured, but the material is not; aluminum or another sheet material would change mass by roughly a factor of three."
material:
  primary_material: "unknown metal/alloy sheet material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AJ_sheet_front.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 238 identifies the row as 17AJ_sheet_front. FreeCAD measured a 2.00 mm thick rectangular sheet-like solid. Assembly STEP material extraction for 17AJ_sheet_front returned only placeholder material Generic with density 1000.0, which the task workflow treats as unresolved material evidence. targeted_web_search: searched \"17AJ_sheet_front material\", \"17AJ sheet_front reAM250 material\", \"reAM250 17AJ sheet_front\", and \"17AJ_sheet_front\"; found duplicate BOM text and no row-specific vendor/material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A front sheet in this mechanical frame context is most plausibly a metal sheet or strip; no specific alloy or grade is claimed."
  uncertainty_notes:
    - "No BOM field, STEP metadata, vendor link, or targeted search result states the actual material family or alloy."
how_to_make:
  summary: "Cut a 2 mm sheet-metal strip to the CAD outline, then deburr and finish as needed for the hood/front cover assembly."
  manufacturing_steps:
    - "Select flat metal sheet stock matching the required final material and 2.00 mm thickness."
    - "Cut the rectangular blank to approximately 32.00 x 634.40 mm by shear, saw, waterjet, or laser cutting."
    - "Deburr long edges and check flatness and final dimensions."
    - "Apply any required surface finish or protective coating before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AJ_sheet_front.step; research/ream250_bom/ream250_bom_row_0238_17AJ__views_2x2.png"
    cited_fact_or_basis: "CAD geometry is one simple solid with bounding box 2.00 x 32.00 x 634.40 mm. The contact sheet shows a plain long thin rectangular sheet with no visible holes, slots, bends, flanges, or attached subparts. targeted_web_search: searched \"17AJ_sheet_front material\", \"17AJ sheet_front reAM250 material\", \"reAM250 17AJ sheet_front\", and \"17AJ_sheet_front\"; found duplicate BOM text and no row-specific vendor/manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because no holes, bends, or complex features are visible, a simple sheet-cutting route is sufficient for KB-level modeling."
    - "Final edge finish and coating requirements are not specified by the row and would be chosen from the surrounding assembly requirements."
  uncertainty_notes:
    - "If hidden mounting features or a specific coating are required outside this per-part STEP, the manufacturing route may need extra drilling, forming, or finishing steps."
kb_implications:
  - "item_granularity: simple_part - one plain sheet/strip part, likely modeled as a cut sheet-metal component rather than a purchased module or assembly."
---
