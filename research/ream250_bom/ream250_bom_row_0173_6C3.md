---
row_identity:
  item: "6C3"
  cad_file: "6C3_blade_mount_part_2"
  source_row_number: 173
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin stainless blade-mount strip for the reAM250 recoater/scraper blade assembly, likely serving as a narrow clamp, spacer, or backing strip along the blade span."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C3_blade_mount_part_2.step; research/ream250_bom/ream250_bom_row_0173_6C3__views_2x2.png"
    cited_fact_or_basis: "BOM row 173 names item 6C3 as 6C3_blade_mount_part_2 with quantity 1. Neighboring BOM rows include 6C2_blade_mount_part_1 and 6C5_blade_extension. The manifest maps row 173 to one matched_existing part STEP. FreeCAD measured one solid with bbox about 265.00 x 3.50 x 20.00 mm, and the rendered preview shows a long, very thin profiled strip with angled end features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and adjacent 6C blade rows identify this part as blade mounting hardware rather than the recoater blade edge itself."
    - "The narrow strip geometry makes a clamp, spacer, or backing-strip role more plausible than a load-bearing rail."
  uncertainty_notes:
    - "The exact interface face and whether this part clamps, spaces, or backs the blade is inferred from row naming and CAD shape because no assembly drawing or callout is present in the BOM row."
mass:
  value_kg: 0.133
  basis: "FreeCAD volume 16669.771 mm^3 = 0.000016670 m^3. Assembly STEP material metadata for this product reports Stainless Steel with density 8000 kg/m^3, giving 0.13336 kg, rounded to 0.133 kg per unit. BOM quantity is 1, so row total is also about 0.133 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C3_blade_mount_part_2.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 16669.771 mm^3 for the row STEP. Local assembly STEP material extraction for 6C3_blade_mount_part_2 returned material Stainless Steel and density 8000.0, matching the local stainless_steel density table value."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported single-solid CAD volume is treated as the physical per-unit volume for this BOM row."
  uncertainty_notes:
    - "Mass does not include screws, the blade, or the larger mating mount rail; those are separate BOM rows if present."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6C3_blade_mount_part_2 returned material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata gives a material family but not a stainless alloy grade, hardness, or surface treatment."
how_to_make:
  summary: "Fabricate as a simple machined or profile-cut stainless strip; start from thin stainless strip or plate stock, cut the long profile and angled end geometry, deburr, clean or passivate, and inspect length, flatness, and edge condition before assembly with the blade mount"
  manufacturing_steps:
    - "Cut stainless strip or thin plate stock slightly oversize to the roughly 265 mm length."
    - "Profile-cut or mill the long narrow outline and angled end features shown in the CAD preview."
    - "Deburr and break sharp edges while preserving the blade-contact or spacer faces."
    - "Clean or passivate the stainless surface and inspect length, thickness, straightness, and flatness before installing with the mating blade mount hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C3_blade_mount_part_2.step; research/ream250_bom/ream250_bom_row_0173_6C3__views_2x2.png; web_search"
    cited_fact_or_basis: "CAD and rendered views show a one-piece stainless strip about 265 mm long, 20 mm tall, and 3.5 mm thick with profiled ends. targeted_web_search: queries tried: 'reAM250 6C3 blade mount part 2 stainless steel recoater blade mount', 'Renishaw AM250 recoater blade mount stainless steel scraper blade', and 'reAM250 recoater blade mount part 2'; result: found general recoater-blade context for metal AM systems but no row-specific vendor drawing or manufacturing specification for 6C3."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For a low-volume one-piece stainless strip, cutting or light machining from strip or plate stock is the simplest plausible manufacturing route."
    - "The profiled ends are functional clearance or alignment features that should be preserved during finishing."
  uncertainty_notes:
    - "The CAD and metadata do not state tolerances, surface finish, passivation requirement, or whether the original part was laser-cut, waterjet-cut, milled, or stamped."
kb_implications:
  - "item_granularity: simple_part - Model as one simple stainless blade-mount strip or spacer in the recoater blade mount family, not as a purchased module or multi-part assembly."
---
