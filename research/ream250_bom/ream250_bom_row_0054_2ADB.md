---
row_identity:
  item: 2ADB
  cad_file: 2ADB_part_B
  source_row_number: 54
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Small upper axis-bearing ring or locator in the reAM250 Z-axis/bearing stack; the CAD shows an annular stepped ring with side reliefs/notches, consistent with locating, retaining, or spacing a bearing-related axis component.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADB_part_B.step; research/ream250_bom/ream250_bom_row_0054_2ADB__views_2x2.png
    cited_fact_or_basis: "BOM row 54 identifies item 2ADB, quantity 1, CAD file 2ADB_part_B, description 'axis bearing top'. FreeCAD measured one solid with bounding box about 24.04 x 6.27 x 24.04 mm, and the rendered preview shows a stepped annular part with relief/notch features."
    evidence_basis: bom_provided
  assumptions:
    - The row is one of several adjacent upper axis-bearing parts, so this component is interpreted as one member of the top bearing support/retention stack rather than as a complete bearing assembly.
  uncertainty_notes:
    - The BOM phrase does not specify whether this exact ring is a cap, spacer, preload feature, retainer, or labyrinth-like cover within the bearing stack.
mass:
  value_kg: 0.006
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 760.144 mm^3, equal to 7.60144e-7 m^3. Using a generic steel density of 7850 kg/m^3 from kb/materials/properties.yaml gives 0.00597 kg, rounded to 0.006 kg; row total is the same because quantity is 1."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADB_part_B.step; kb/materials/properties.yaml
    cited_fact_or_basis: "CAD volume measured as 760.144 mm^3 for one solid; local density table lists generic steel density as 7850 kg/m^3. targeted_web_search: queries tried: \"2ADB\" \"axis bearing top\", \"2ADB_part_B\", \"reAM250\" \"axis bearing top\", and \"axis bearing top\" \"reAM250\"; results found BOM mirrors but no row-specific material or catalog mass."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Steel density is used as a planning proxy because bearing support hardware commonly needs stiffness and wear resistance, while the local STEP material metadata was only Generic with density 1000 kg/m^3.
  uncertainty_notes:
    - If the actual part is aluminum, mass would be about 0.0021 kg; if stainless steel, about 0.0061 kg. No source resolved the actual material grade or catalog mass.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "BOM row gives no manufacturer, link, or material. Assembly STEP material extraction for product 2ADB_part_B returned only Generic with density 1000.0, which is placeholder metadata. targeted_web_search: queries tried: \"2ADB\" \"axis bearing top\", \"2ADB_part_B\", \"reAM250\" \"axis bearing top\", and \"axis bearing top\" \"reAM250\"; results found BOM mirrors only, not material data."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Treat as a machined metal part for later modeling because the CAD is a compact bearing-stack ring and nearby axis hardware includes shafts, rails, and bearing-related components.
  uncertainty_notes:
    - The evidence does not distinguish steel, stainless steel, aluminum, or another alloy; downstream KB modeling should keep material broad unless later CAD/source data identifies a grade.
how_to_make:
  summary: Plausible route is to machine the ring from metal bar, tube, or plate stock, creating the inner bore, stepped faces, outside profile, and radial relief/notch features, then deburr and inspect fit in the axis-bearing stack.
  manufacturing_steps:
    - Cut metal stock blank slightly oversize.
    - Turn or mill the annular bore, outer diameter, and stepped shoulder features.
    - Mill or slot the visible side relief/notch features.
    - Deburr, clean, and inspect critical diameters and thickness.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADB_part_B.step; research/ream250_bom/ream250_bom_row_0054_2ADB__views_2x2.png
    cited_fact_or_basis: "CAD geometry is a small annular stepped solid with relief/notch features and about 24 mm outside span by 6.27 mm thickness. targeted_web_search: queries tried: \"2ADB\" \"axis bearing top\", \"2ADB_part_B\", \"reAM250\" \"axis bearing top\", and \"axis bearing top\" \"reAM250\"; results did not provide a row-specific manufacturing route."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Low-volume local production favors conventional CNC turning/milling or mill-turn machining over casting or additive manufacture for this small bearing-stack part.
  uncertainty_notes:
    - Exact tolerance, heat treatment, and surface finish are unknown; bearing-contact or preload surfaces may need tighter finishing than the CAD-only route can prove.
kb_implications:
  - "item_granularity: simple_part - Model as a reusable small machined bearing-retainer/spacer-style metal part, not as a purchased bearing module or full top-axis bearing assembly."
---
