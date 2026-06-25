---
row_identity:
  item: "6C2"
  cad_file: "6C2_blade_mount_part_1"
  source_row_number: 172
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long stainless blade-mount rail for the reAM250 recoater/scraper blade assembly, providing a rigid clamping or locating body along the blade span."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C2_blade_mount_part_1.step; research/ream250_bom/ream250_bom_row_0172_6C2__views_2x2.png"
    cited_fact_or_basis: "BOM row 172 names item 6C2 as 6C2_blade_mount_part_1 with quantity 1. Neighboring BOM rows 171-174 are 6C1_blade, 6C3_blade_mount_part_2, and 6C5_blade_extension. The manifest maps row 172 to one matched_existing part STEP. FreeCAD measured one solid with bbox about 265.00 x 42.00 x 14.00 mm, and the rendered preview shows a long narrow rail/channel with repeated holes and stepped/grooved features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and adjacent 6C blade rows identify this part as one side of the blade mounting hardware rather than the blade edge itself."
  uncertainty_notes:
    - "The exact clamp interface and fastener pattern are inferred from CAD geometry because the BOM row does not include an assembly note or drawing callout."
mass:
  value_kg: 0.922
  basis: "FreeCAD volume 115233.832 mm^3 = 0.000115234 m^3. Assembly STEP material metadata for this product reports Stainless Steel with density 8000 kg/m^3, giving 0.9219 kg, rounded to 0.922 kg per unit. BOM quantity is 1, so row total is also about 0.922 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C2_blade_mount_part_1.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 115233.832 mm^3 for the row STEP. Local assembly STEP material extraction for 6C2_blade_mount_part_1 returned material Stainless Steel and density 8000.0, consistent with the local stainless_steel density table value."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported single-solid CAD volume is treated as the physical per-unit volume for this BOM row."
  uncertainty_notes:
    - "Mass does not include any separate screws or mating blade parts; those are represented by other BOM rows if present."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6C2_blade_mount_part_1 returned material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata gives a material family but not a stainless alloy grade or heat treatment."
how_to_make:
  summary: "Fabricate as a machined stainless blade-mount rail; start from stainless bar or plate stock, mill the long profile and grooves, drill or countersink the repeated mounting holes, deburr, passivate, and inspect straightness and blade-contact surfaces"
  manufacturing_steps:
    - "Cut stainless bar or plate stock slightly oversize to the roughly 265 mm rail length."
    - "Mill the outer profile, stepped channel, and blade locating or clamping faces."
    - "Drill and countersink or counterbore the repeated mounting holes shown in the CAD preview."
    - "Deburr sharp edges, passivate or clean the stainless surface, and inspect straightness plus hole spacing before assembly with the blade and mating mount part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C2_blade_mount_part_1.step; research/ream250_bom/ream250_bom_row_0172_6C2__iso.png; research/ream250_bom/ream250_bom_row_0172_6C2__top.png"
    cited_fact_or_basis: "CAD and rendered views show a one-piece stainless rail/channel with long milled surfaces and repeated holes. targeted_web_search: queries tried: 'reAM250 6C2 blade mount part 1 stainless steel recoater blade mount', 'reAM250 recoater scraper blade mount stainless steel 6C2', and 'Renishaw AM250 recoater blade mount stainless steel scraper blade'; result: found general AM recoater blade context but no row-specific vendor drawing or manufacturing specification for 6C2."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining from stainless bar or plate is the most direct route for this low-volume, one-piece grooved rail geometry."
    - "The hole features visible in the CAD preview are functional mounting holes that require positional inspection."
  uncertainty_notes:
    - "The CAD and metadata do not state tolerances, surface finish, passivation requirement, or whether the original part was machined from bar stock, plate, or another near-net blank."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable machined stainless rail or bracket component for the recoater blade mount rather than as a purchased module or multi-part assembly."
---
