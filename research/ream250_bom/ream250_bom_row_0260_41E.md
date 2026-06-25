---
row_identity:
  item: "41E"
  cad_file: "41E_cover_drivetrain"
  source_row_number: 260
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Protective cover for the drivetrain belt/pulley area, enclosing or shielding the small timing-belt drive components around BOM rows 41A-41D."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41E_cover_drivetrain.step; research/ream250_bom/ream250_bom_row_0260_41E__views_2x2.png"
    cited_fact_or_basis: "BOM row 260 names item 41E as 41E_cover_drivetrain, adjacent to timing belt and pulley rows 41A-41D; FreeCAD reads one solid, and the rendered preview shows an open rectangular cover with folded side walls."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row position next to the belt and pulley BOM entries identifies the drivetrain being covered."
  uncertainty_notes:
    - "CAD preview shows the cover shape but not installed clearance or attachment interfaces."
mass:
  value_kg: 0.15
  basis: "Per unit for quantity 1. FreeCAD measured CAD volume 55450.388 mm^3 and bounding box 154.49 x 66.82 x 49.79 mm. Using the local aluminum density constant of 2700 kg/m^3 gives 0.1497 kg; if steel were used instead, the same CAD volume would be about 0.435 kg, so material uncertainty dominates."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41E_cover_drivetrain.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured volume 55450.388 mm^3 for one solid. Local material properties list aluminum density 2700 kg/m^3 and steel density 7850 kg/m^3. targeted_web_search: queries tried: \"41E_cover_drivetrain\", \"reAM250 cover drivetrain material\", \"41E cover drivetrain reAM250\", and \"41E_cover_drivetrain 41E\"; results repeated BOM row text or project pages and did not provide row-specific material or weight."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid represents the physical cover volume without major missing hardware."
    - "Aluminum sheet is used as the mass basis because the visible geometry is a small non-load-bearing protective cover where low mass and easy forming are plausible."
  uncertainty_notes:
    - "Assembly STEP metadata reports only Generic material with density 1000.0, which is a placeholder and was not used."
    - "If modeled as steel sheet, use approximately 0.44 kg instead of 0.15 kg."
material:
  primary_material: "unknown sheet metal/alloy cover material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 260 provides no manufacturer, product ID, or material. Assembly STEP material extraction for 41E_cover_drivetrain returns material Generic with density 1000.0. targeted_web_search: queries tried: \"41E_cover_drivetrain\", \"reAM250 cover drivetrain material\", \"41E cover drivetrain reAM250\", and \"41E_cover_drivetrain 41E\"; no row-specific usable material source found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is a folded or formed sheet-metal guard rather than a plastic printed cover, based on its thin-wall CAD form and use near a mechanical belt drive."
  uncertainty_notes:
    - "No source supports a specific alloy or grade; do not model this as confirmed aluminum or confirmed steel without later drawing/material evidence."
how_to_make:
  summary: "Fabricate as a small sheet-metal drivetrain guard: cut a flat blank, bend the side flanges and return lips, deburr, and finish or coat as needed before mounting."
  manufacturing_steps:
    - "Laser-cut, waterjet-cut, or CNC punch a sheet blank to the cover outline."
    - "Press-brake bend the long side walls, end returns, and small lips visible in the CAD preview."
    - "Deburr edges and add holes or slots if required by the assembly drawing."
    - "Apply finish appropriate to the selected sheet material, such as anodizing for aluminum or passivation/paint for steel."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41E_cover_drivetrain.step; research/ream250_bom/ream250_bom_row_0260_41E__views_2x2.png"
    cited_fact_or_basis: "CAD preview shows a thin open cover with straight folded walls and lips, not a complex machined block. targeted_web_search: queries tried: \"41E_cover_drivetrain\", \"reAM250 cover drivetrain material\", \"41E cover drivetrain reAM250\", and \"41E_cover_drivetrain 41E\" no row-specific manufacturing drawing or vendor route found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is intended for conventional sheet-metal fabrication because its geometry is dominated by flat faces and bends."
  uncertainty_notes:
    - "STEP geometry alone does not show bend radii requirements, fastener details, surface finish, or exact stock thickness."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable small sheet-metal protective cover/guard, not a purchased module or drivetrain assembly."
---
