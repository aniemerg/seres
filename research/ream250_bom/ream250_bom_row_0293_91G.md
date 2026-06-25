---
row_identity:
  item: "91G"
  cad_file: "91G_mount_top"
  source_row_number: 293
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom upper structural mount or cap block in the reAM250 frame group, likely providing the top mounting interface paired with the adjacent 91H bottom mount and nearby 80 x 80 steel profile hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91G_mount_top.step; research/ream250_bom/ream250_bom_row_0293_91G__views_2x2.png"
    cited_fact_or_basis: "BOM row 293 and manifest row 293 identify item 91G as quantity 1 of 91G_mount_top, with matched part STEP gold_export/parts/91G_mount_top.step. Neighboring BOM rows 286-294 list 80 x 80 x 5 square hollow sections, 50 x 5 angle profiles, 80 x 80 x 10 M12 plates, 91G_mount_top, and 91H_mount_bottom. FreeCAD measured one solid with bounding box 80.00 x 100.00 x 20.00 mm. The rendered contact sheet shows a compact rectangular top mount with a central round through-hole and sloped/pyramidal stiffening or relief faces."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'mount_top' and the adjacent 'mount_bottom' row are interpreted as a paired structural mounting interface rather than a consumable or calibrated vendor module."
    - "The central circular feature is treated as a mounting, clearance, or alignment hole for mating frame hardware."
  uncertainty_notes:
    - "The BOM and CAD package do not state the exact mating component or load path, so the function is inferred from row name, adjacent structural rows, and visible geometry."
mass:
  value_kg: 1.218
  basis: "Per unit for one physical top mount; BOM quantity is 1, so row total is also about 1.218 kg. FreeCAD volume is 155202.086 mm^3 = 1.55202086e-4 m^3. Assembly STEP material metadata reports Steel with density 7850 kg/m^3, matching the local steel density constant in kb/materials/properties.yaml. Computed mass is 1.55202086e-4 m^3 x 7850 kg/m^3 = 1.21834 kg, rounded to 1.218 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91G_mount_top.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 155202.086 mm^3, area 23762.311 mm^2, and bounding box 80.00 x 100.00 x 20.00 mm. Local assembly material extraction matched 91G_mount_top to material Steel with density 7850 kg/m^3. kb/materials/properties.yaml lists steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the complete per-unit physical mount for this BOM row."
    - "The STEP material density is used as the planning density for the whole part."
  uncertainty_notes: []
material:
  primary_material: "steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 91G_mount_top reports material Steel and density 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata gives steel as a material family but does not specify alloy grade, heat treatment, or surface finish."
how_to_make:
  summary: "Make as a custom steel top mount from steel plate or block stock, with the outer envelope, sloped relief/stiffening faces, and central mounting hole machined to the CAD geometry."
  manufacturing_steps:
    - "Cut an oversized steel blank from plate or rectangular bar/block stock suitable for the roughly 80 x 100 x 20 mm envelope."
    - "CNC mill or fixture-machine the rectangular outside profile and sloped top relief faces shown in the CAD preview."
    - "Drill, bore, ream, or countersink the central mounting or clearance hole as required by the mating frame hardware."
    - "Deburr edges, clean, and apply any corrosion-protection finish required by the frame assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91G_mount_top.step; research/ream250_bom/ream250_bom_row_0293_91G__views_2x2.png; https://steelplate.us/what-we-do/drilling-and-milling/"
    cited_fact_or_basis: "The row STEP and contact sheet show one steel 80.00 x 100.00 x 20.00 mm custom mount with sloped relief faces and a central circular feature. Steel Plate describes drilling as producing circular holes in solid materials and face milling as flattening/smoothing workpiece surfaces. targeted_web_search: searches tried '91G_mount_top reAM250', 'reAM250 91G mount_top', and 'custom steel mount plate CNC machining drilled hole'; results found duplicate reAM250 BOM listings and generic steel plate drilling/milling services, but no row-specific drawing or stated manufacturing process for 91G_mount_top."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The custom geometry is best modeled as subtractive machining from steel stock rather than as a external catalog module"
    - "The sloped faces are manufacturable by CNC milling or equivalent fixture machining."
  uncertainty_notes:
    - "The exact production method, tolerances, hole specification, and finish are not stated by the BOM or CAD package."
kb_implications:
  - "item_granularity: simple_part - Model 91G as one reusable custom steel top mount/cap block; keep neighboring profiles, bottom mount, M12 plates, and fasteners as separate parts or generic hardware."
---
