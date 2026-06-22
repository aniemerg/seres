---
row_identity:
  item: "6C1"
  cad_file: "6C1_blade"
  source_row_number: 171
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Steel blade element in the reAM250 recoater scraper-blade subassembly, providing the long straight working edge that helps scrape or level powder across the recoater path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/60_recoater.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C1_blade.step; research/ream250_bom/ream250_bom_row_0171_6C1__views_2x2.png"
    cited_fact_or_basis: "BOM row 171 lists item 6C1, quantity 1, CAD file 6C1_blade. Manifest row 171 maps it to a matched existing part STEP. The 60_recoater STEP assembly contains 6C1_blade under 6C0_scraper_blade, and the rendered preview shows a single long narrow blade-like solid with a 265.00 x 6.00 x 20.00 mm envelope."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-level part is interpreted in its local 60_recoater and 6C0_scraper_blade assembly context."
    - "The long straight narrow geometry is treated as the working blade member, while mounts and extensions are separate adjacent BOM rows."
  uncertainty_notes:
    - "The CAD and assembly labels do not expose contact preload, exact powder-bed clearance, or whether this blade is one of multiple scraper edges used in the recoater."
mass:
  value_kg: 0.202
  basis: "Per-unit mass for the single physical blade in BOM row 171. FreeCAD measured volume 25731.939 mm^3 = 2.5731939e-5 m^3. Assembly STEP material metadata reports Steel density 7850 kg/m^3; computed mass is 2.5731939e-5 m^3 * 7850 kg/m^3 = 0.201996 kg, rounded to 0.202 kg. BOM quantity is 1, so the row total is also about 0.202 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C1_blade.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 25731.939 mm^3, area 12944.851 mm^2, and bounding box 265.00 x 6.00 x 20.00 mm. The local assembly STEP material extractor matched product 6C1_blade to material Steel with density 7850.0. kb/materials/properties.yaml lists steel density_kg_per_m3: 7850."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished volume of one blade."
    - "The assembly STEP density value is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes mounting parts 6C2, 6C3, blade extensions 6C5, and any wear strip or fasteners represented by neighboring BOM rows."
material:
  primary_material: "Steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 6C1_blade to material Steel with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata resolves the material family but not a specific steel grade, hardness, surface treatment, or wear coating."
how_to_make:
  summary: "Make as a custom steel scraper/recoater blade: cut a steel blank to the long narrow profile, machine or grind the working edge and any shallow profile changes, deburr, clean, and inspect straightness and edge condition before assembly into the scraper-blade mount."
  manufacturing_steps:
    - "Start from steel flat bar or plate stock sized above the 265.00 x 20.00 x 6.00 mm finished envelope."
    - "Saw, waterjet, laser cut, or mill the long blade blank to the CAD outline."
    - "Machine or grind the working edge and shallow lengthwise profile visible in the CAD preview."
    - "Deburr and clean all edges to avoid powder contamination or scratches."
    - "Inspect length, straightness, thickness, edge condition, and fit against the 6C2 and 6C3 blade mount parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6C1_blade.step; research/ream250_bom/ream250_bom_row_0171_6C1__views_2x2.png"
    cited_fact_or_basis: "The STEP geometry is one steel solid with a 265.00 x 6.00 x 20.00 mm envelope, and the rendered preview shows a long narrow blade/strip without purchased-module features. targeted_web_search: tried '\"6C1_blade\" reAM250 material', '\"6C1_blade\" \"scraper_blade\"', '\"6C0_scraper_blade\" reAM250', and 'RenAM 250 recoater blade scraper blade metal additive manufacturing powder bed recoater function'; results found duplicate reAM250 BOM listings and general recoater-blade context, but no row-specific fabrication drawing or manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cutting and edge machining/grinding from steel stock is the most plausible local route for the observed one-piece blade geometry."
    - "Powder-bed recoater service requires a clean, straight, burr-free working edge."
  uncertainty_notes:
    - "No row-specific drawing was found, so exact edge angle, flatness, hardness, coating, and surface-finish requirements remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model later as one custom steel recoater/scraper blade with stock-cutting, edge finishing, cleaning, and inspection, separate from its blade mounts and extensions."
---

Research result for the leased reAM250 BOM row only.
