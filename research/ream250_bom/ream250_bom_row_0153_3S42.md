---
row_identity:
  item: "3S42"
  cad_file: "3S42_part_2"
  source_row_number: 153
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom gas outlet segment, likely one bent wall or duct panel in the multi-part reAM250 gas outlet assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S42_part_2.step; research/ream250_bom/ream250_bom_row_0153_3S42__views_2x2.png"
    cited_fact_or_basis: "BOM row 153 identifies item 3S42, quantity 1, CAD file 3S42_part_2, description 'gas outlet: part 2'. FreeCAD measured one solid with bounding box 43.00 x 50.00 x 90.71 mm; the rendered preview shows a thin bent plate-like segment."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted within neighboring BOM rows 3S41 through 3S48, which are sequential 'gas outlet' parts, so this part is one segment of that outlet rather than a standalone purchased fitting."
  uncertainty_notes:
    - "The BOM does not state the exact gas-flow interface or mating parts for this segment."
mass:
  value_kg: 0.041
  basis: "CAD volume 5182.937 mm^3 converted to 5.182937e-6 m^3, multiplied by an assumed dense sheet-metal/stainless-steel density of 8000 kg/m^3 from kb/materials/properties.yaml; rounded to 0.041 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S42_part_2.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 5182.937 mm^3. The local density table lists stainless_steel at 8000 kg/m^3."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume."
    - "A stainless-steel-like density is used as a conservative vacuum/gas-handling sheet-metal scenario because the row has no resolved material."
  uncertainty_notes:
    - "targeted_web_search: searched \"3S42_part_2 gas outlet reAM250 material\", \"3S42 gas outlet reAM250\", and \"reAM250 gas outlet material\"; found duplicate BOM text but no row-specific vendor, drawing, or material source."
    - "If this custom outlet segment is aluminum rather than stainless steel, the same CAD volume would imply roughly 0.014 kg instead of 0.041 kg."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0153_3S42__views_2x2.png"
    cited_fact_or_basis: "BOM row 153 names a custom gas outlet part but provides no material family or grade. The assembly STEP material extractor matched 3S42_part_2 only to placeholder material 'Generic' with density 1000.0. The rendered CAD preview shows a thin bent plate-like form."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A gas outlet segment in this machine is modeled as sheet metal because the visible CAD geometry is thin, folded, and duct-like."
  uncertainty_notes:
    - "targeted_web_search: searched \"3S42_part_2 gas outlet reAM250 material\", \"3S42 gas outlet reAM250\", and \"reAM250 gas outlet material\"; found only duplicate BOM listings and no row-specific material source."
    - "The broad metal/alloy family is supported by function and CAD shape, but no evidence resolves aluminum versus stainless steel or another alloy."
how_to_make:
  summary: "Cut a thin metal sheet blank, bend it along the modeled fold lines, deburr edges, and join or fasten it with adjacent gas-outlet segments during outlet assembly."
  manufacturing_steps:
    - "Cut the flat blank from thin metal sheet using laser, waterjet, or CNC shear/profile cutting."
    - "Bend the blank to the CAD angles on a press brake or equivalent sheet-forming setup."
    - "Deburr and clean the edges for gas-path assembly."
    - "Join to neighboring gas outlet parts by welding, brazing, adhesive/sealant, or mechanical fastening according to the final outlet design."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S42_part_2.step; research/ream250_bom/ream250_bom_row_0153_3S42__views_2x2.png"
    cited_fact_or_basis: "FreeCAD measured a one-solid part with bounding box 43.00 x 50.00 x 90.71 mm; the rendered preview shows a thin folded plate-like geometry without visible machined bosses, shafts, or standard fitting features."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible thin folded geometry is treated as sheet-metal work rather than casting or billet machining."
    - "Final sealing/joining details are deferred to the surrounding gas outlet assembly because this row represents only part 2."
  uncertainty_notes:
    - "Targeted_web_search: searched \"3S42_part_2 gas outlet reAM250 material\", \"3S42 gas outlet reAM250\", and \"reAM250 gas outlet material\" found no row-specific manufacturing drawing or process note."
    - "The CAD preview does not show the complete gas outlet assembly, so the final joining method remains unresolved."
kb_implications:
  - "item_granularity: simple_part - Custom thin folded gas-outlet segment best modeled as one fabricated sheet-metal part, with assembly-level joining handled by the larger gas outlet."
---

Research result for reAM250 BOM row 153.
