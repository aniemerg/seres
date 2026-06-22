---
row_identity:
  item: "2A6"
  cad_file: "2A6_left_plate"
  source_row_number: 29
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Left-hand structural plate for the reAM250 Z-axis/linear-motion assembly, providing a triangular side support with stiffening ribs and a bolted mounting edge."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/20_z_axis.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; research/ream250_bom/ream250_bom_row_0029_2A6__views_2x2.png"
    cited_fact_or_basis: "BOM row 29 identifies item 2A6 as quantity 1 of 2A6_left_plate. The manifest maps it to a matched part STEP. The full assembly places 2A6_left_plate in 20_z_axis.step. FreeCAD measured a 240.00 x 400.00 x 23.00 mm envelope, and the rendered preview shows a triangular ribbed plate with a row of mounting holes along one edge."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name left_plate and its location in 20_z_axis.step identify the side and subsystem role."
  uncertainty_notes:
    - "No drawing callouts or assembly mates were available, so the exact connected components are inferred from CAD shape and subsystem placement."
mass:
  value_kg: 3.50
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 1,295,591.522 mm^3, equal to 0.001295592 m^3. Using local aluminum density 2700 kg/m^3 gives 3.498 kg, rounded to 3.50 kg. If the part were generic steel at 7850 kg/m^3, the same CAD volume would imply about 10.17 kg; aluminum is selected as the best estimate for a ribbed structural motion-axis plate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; kb/materials/properties.yaml; web_search"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 1,295,591.522 mm^3 and bounding box 240.00 x 400.00 x 23.00 mm. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3 and steel density as 7850 kg/m^3. targeted_web_search: searched \"2A6_left_plate reAM250 material\", \"2A6 2A6_left_plate\", \"reAM250 left_plate 2A6\", and \"reAM250 2A6_left_plate manufacturing\"; results duplicated BOM row identity but did not provide row-specific mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The plate is treated as aluminum alloy because its large ribbed motion-axis support geometry is consistent with a lightweight machined structural plate."
    - "The CAD STEP volume is treated as the finished solid volume, including pockets, ribs, holes, and edge features."
  uncertainty_notes:
    - "Assembly STEP material extraction for 2A6_left_plate returned only Generic with density 1000.0, which is placeholder metadata under the task acceptance criteria."
    - "If the actual part is steel rather than aluminum, mass would be roughly 10.17 kg instead of 3.50 kg."
material:
  primary_material: "Aluminum alloy structural plate, exact grade unknown"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAM250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; web_search"
    cited_fact_or_basis: "BOM row 29 has blank manufacturer, description/product ID, material family, specific grade, and link URL fields. Local assembly STEP material extraction for product 2A6_left_plate returned material Generic with density 1000.0. The CAD/contact sheet shows a single ribbed structural plate rather than a catalog module. targeted_web_search: searched \"2A6_left_plate reAM250 material\", \"2A6 2A6_left_plate\", \"reAM250 left_plate 2A6\", and \"reAM250 2A6_left_plate manufacturing\"; no row-specific material or grade source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Use aluminum alloy as the planning material family for later KB modeling because the plate is a large custom motion-axis support where low mass is useful."
  uncertainty_notes:
    - "The actual alloy and temper are not resolved; downstream KB work should keep this as an estimated structural aluminum part unless a drawing or CAD material file is found."
how_to_make:
  summary: "Fabricate as a custom CNC-machined aluminum side plate from thick plate stock, with profile cutting, pocket/rib machining, drilled mounting holes, deburring, and optional surface finish."
  manufacturing_steps:
    - "Start from aluminum plate stock thick enough for the 23 mm finished envelope."
    - "CNC mill or waterjet/rough-cut the triangular outside profile."
    - "CNC mill the ribbed pockets and edge/flange features visible in the STEP preview."
    - "Drill and countersink or spotface the mounting-hole row as required by the mating Z-axis hardware."
    - "Deburr, inspect hole locations and flatness, then anodize or otherwise finish if the machine environment requires corrosion/wear protection."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; research/ream250_bom/ream250_bom_row_0029_2A6__views_2x2.png; web_search"
    cited_fact_or_basis: "The row-specific STEP/contact sheet shows one custom plate-like solid with a triangular outline, milled-looking ribs/pockets, edge features, and mounting holes. targeted_web_search: searched \"2A6_left_plate reAM250 material\", \"2A6 2A6_left_plate\", \"reAM250 left_plate 2A6\", and \"reAM250 2A6_left_plate manufacturing\"; no row-specific manufacturing drawing, vendor page, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The ribbed geometry is treated as machined or plate-fabricated geometry, not a cast part, because the CAD shows planar pockets and regular hole features."
  uncertainty_notes:
    - "A production drawing could specify casting, welded fabrication, surface treatment, or tighter tolerances not visible in the STEP preview."
kb_implications:
  - "item_granularity: simple_part - Model 2A6 as one custom machined structural plate, paired conceptually with 2A7_right_plate but not as a purchased module."
---

# reAM250 BOM Row 29 - 2A6

Research result for the leased reAM250 BOM row.
