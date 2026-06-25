---
row_identity:
  item: "6C5"
  cad_file: "6C5_blade_extension"
  source_row_number: 174
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small blade-extension block for the reAM250 recoater/scraper blade assembly, likely extending, spacing, or fastening the blade/mount interface at a local attachment point."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C5_blade_extension.step; research/ream250_bom/ream250_bom_row_0174_6C5__views_2x2.png"
    cited_fact_or_basis: "BOM row 174 names item 6C5 as 6C5_blade_extension with quantity 1. Neighboring BOM rows 171-173 are 6C1_blade, 6C2_blade_mount_part_1, and 6C3_blade_mount_part_2. The manifest maps row 174 to one matched_existing part STEP. FreeCAD measured one solid with bbox about 22.00 x 14.00 x 4.50 mm, and the rendered preview shows a small rectangular block/plate with two through holes and relieved or chamfered faces."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and adjacent 6C blade rows identify this as blade assembly hardware rather than an independent machine module."
    - "The two holes are treated as fastening or locating holes for connection to the blade or blade mount."
  uncertainty_notes:
    - "The exact interface and whether the part primarily extends, spaces, clamps, or locates the blade is inferred from row naming and CAD shape because no assembly drawing callout is present."
mass:
  value_kg: 0.00903
  basis: "FreeCAD volume 1129.281 mm^3 = 0.000001129281 m^3. Using an assumed stainless-steel-like density of 8000 kg/m^3 gives 0.009034 kg, rounded to 0.00903 kg per unit. BOM quantity is 1, so row total is also about 0.00903 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C5_blade_extension.step; kb/materials/properties.yaml; web_search"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 1129.281 mm^3 for the row STEP. Local density table lists stainless_steel density as 8000 kg/m^3. targeted_web_search: queries tried: 'reAM250 6C5 blade extension material', 'Renishaw AM250 recoater blade extension material', 'reAM250 blade extension recoater scraper blade 6C5', and 'Renishaw AM250 recoater blade mount stainless steel'; result: no row-specific catalog mass or material source for 6C5 was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported single-solid CAD volume is treated as the physical per-unit volume for this BOM row."
    - "The part is estimated using stainless-steel-like density because neighboring completed blade-mount rows 6C2 and 6C3 are stainless steel in assembly STEP metadata, and this small attachment block is in the same blade hardware group."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic with density 1000.0 for this product, so the mass depends on an inferred material density; if the part is aluminum, the per-unit mass would be about 0.00305 kg instead."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAM250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web_search"
    cited_fact_or_basis: "BOM row 174 has no material-family or grade field. Local assembly STEP material extraction for product 6C5_blade_extension returned Generic with density 1000.0, which does not resolve material. targeted_web_search: queries tried: 'reAM250 6C5 blade extension material', 'Renishaw AM250 recoater blade extension material', 'reAM250 blade extension recoater scraper blade 6C5', and 'Renishaw AM250 recoater blade mount stainless steel'; result: no row-specific usable material source for 6C5 was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metallic material is more plausible than polymer or ceramic because the CAD shows a thin drilled fastening block in the recoater blade mounting group."
    - "Stainless steel is the leading local modeling hypothesis because adjacent blade-mount rows 6C2 and 6C3 have stainless steel metadata, but this row's own metadata does not confirm that material."
  uncertainty_notes:
    - "No sourced alloy family, grade, hardness, or surface treatment is available for this row; later KB modeling should keep material broad unless better CAD metadata or drawings are found."
how_to_make:
  summary: "Fabricate as a small machined metal blade-extension block; cut a blank from thin metal bar or plate stock, mill the rectangular/chamfered profile and relieved faces, drill the two through holes, deburr, clean or passivate if stainless, and inspect hole spacing plus flatness before assembly."
  manufacturing_steps:
    - "Cut a metal bar or plate blank slightly oversize for the roughly 22 x 14 x 4.5 mm envelope."
    - "Mill the outside profile and relieved or chamfered faces visible in the CAD preview."
    - "Drill or ream the two through holes shown in the top view, controlling spacing for blade-mount alignment."
    - "Deburr all edges and hole exits, clean the part, and passivate if stainless steel is selected."
    - "Inspect thickness, flatness, hole spacing, and fit against the blade and neighboring mount hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C5_blade_extension.step; research/ream250_bom/ream250_bom_row_0174_6C5__views_2x2.png; web_search"
    cited_fact_or_basis: "CAD and rendered views show a one-piece small block/plate with two holes and simple milled-looking relief/chamfer geometry. targeted_web_search: queries tried: 'reAM250 6C5 blade extension material', 'Renishaw AM250 recoater blade extension material', 'reAM250 blade extension recoater scraper blade 6C5', and 'Renishaw AM250 recoater blade mount stainless steel'; result: found general recoater-blade context but no row-specific manufacturing drawing or process specification for 6C5."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For a low-volume one-piece drilled block, machining from bar or plate stock is the most direct plausible manufacturing route."
    - "The holes are functional mounting or locating features and need positional inspection relative to the blade/mount interface."
  uncertainty_notes:
    - "The CAD and BOM do not state tolerances, surface finish, edge-break requirements, or whether the original part was milled, laser-cut then finished, or made by another route."
kb_implications:
  - "item_granularity: simple_part - Model as a small reusable blade-mount extension block or spacer in the recoater blade hardware family, not as a purchased module or assembly."
---
