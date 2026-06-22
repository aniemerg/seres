---
row_identity:
  item: "91H"
  cad_file: "91H_mount_bottom"
  source_row_number: 294
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom lower mounting or adapter plate in the reAM250 structural frame group, providing a steel bottom mount interface near the adjacent 80 x 80 steel profiles, M12 plates, and top mount."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91H_mount_bottom.step; research/ream250_bom/ream250_bom_row_0294_91H__views_2x2.png"
    cited_fact_or_basis: "BOM row 294 and manifest row 294 identify item 91H as quantity 1 of 91H_mount_bottom, with matched part STEP gold_export/parts/91H_mount_bottom.step. Neighboring BOM rows 286-293 list 80 x 80 x 5 square hollow sections, 50 x 5 angle profiles, 80 x 80 x 10 M12 plates, and 91G_mount_top. FreeCAD measured one solid with bounding box 120.00 x 80.00 x 10.00 mm, and the rendered contact sheet shows a flat rectangular/wedge-like mount plate with a round mounting or clearance hole."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'mount_bottom' and neighboring top/profile/plate rows are interpreted as a bottom structural mount role rather than as a consumable or calibrated vendor module."
    - "The visible round feature is treated as a mounting, clearance, or alignment hole for mating frame hardware."
  uncertainty_notes:
    - "The row-level CAD does not include mating fasteners, weldments, or assembly constraints, so the exact load path and attachment orientation remain unresolved."
mass:
  value_kg: 0.74
  basis: "Per unit for one physical bottom mount; BOM quantity is 1, so row total is also about 0.740 kg. FreeCAD volume is 94266.888 mm^3 = 9.4266888e-5 m^3. Assembly STEP material metadata reports Steel with density 7850 kg/m^3, matching the local steel density constant in kb/materials/properties.yaml. Computed mass is 9.4266888e-5 m^3 x 7850 kg/m^3 = 0.739995 kg, rounded to 0.740 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91H_mount_bottom.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 94266.888 mm^3, area 23272.911 mm^2, and bounding box 120.00 x 80.00 x 10.00 mm. Local assembly material extraction matched 91H_mount_bottom to material Steel with density 7850 kg/m^3. kb/materials/properties.yaml lists steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the complete per-unit physical mount for this BOM row."
    - "The reAM250 STEP material density is interpreted as kg/m^3, consistent with the material extractor note and the local density table."
  uncertainty_notes:
    - "CAD volume may omit very small edge breaks, surface coating, threads, or finish thickness, but those effects are minor relative to a roughly 0.74 kg steel plate."
material:
  primary_material: "Steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 91H_mount_bottom reports material Steel and density 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata identifies the material family but not the exact steel grade, heat treatment, coating, or surface finish."
how_to_make:
  summary: "Make as a custom steel bottom mount plate from 10 mm steel plate stock, with the profile, inclined/relief faces, and hole machined or cut to the CAD geometry."
  manufacturing_steps:
    - "Start from steel plate stock slightly larger than the 120 x 80 x 10 mm finished envelope."
    - "Saw, waterjet, laser cut, or mill the rectangular outline and any tapered or relieved top geometry visible in the CAD."
    - "Drill, bore, ream, or countersink the round mounting or clearance feature as required by the mating frame hardware."
    - "Deburr edges, clean, apply any required protective finish, and inspect hole position, flatness, thickness, and fit against the adjacent frame/profile hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91H_mount_bottom.step; research/ream250_bom/ream250_bom_row_0294_91H__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "The row STEP and contact sheet show one steel 120.00 x 80.00 x 10.00 mm custom mount with a plate-like envelope and round hole; BOM row 294 names the item 91H_mount_bottom. targeted_web_search: searches tried '91H_mount_bottom reAM250 manufacturing material', '91H_mount_bottom', 'reAM250 91H mount_bottom', and 'steel bottom mount plate CNC machining manufacturing'; results found duplicate reAM250 BOM listings and generic plate/mount machining pages but no row-specific drawing or stated manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Low-volume KB planning favors cutting and machining from steel plate stock because the part is a simple custom steel solid with a plate-like 10 mm thickness and no evidence of casting or a multi-part assembly."
    - "Any threaded, countersunk, or tolerance-critical details are handled as machining/inspection operations after profile cutting."
  uncertainty_notes:
    - "Exact tolerances, hole callouts, surface treatment, and whether the relief geometry is functionally critical are not present in the row-level evidence."
kb_implications:
  - "item_granularity: simple_part - Model 91H as one reusable custom steel bottom mount/adapter plate; keep neighboring profiles, top mount, M12 plates, and fasteners as separate parts or generic hardware."
---
