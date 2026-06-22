---
row_identity:
  item: "6Q"
  cad_file: "6Q_mount_belt_pulley_without_teeth"
  source_row_number: 195
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small mount or axle support for the toothless belt pulley/idler in the reAM250 belt drive area."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0195_6Q__views_2x2.png"
    cited_fact_or_basis: "BOM row 195 names item 6Q as 6Q_mount_belt_pulley_without_teeth with quantity 9; the manifest maps it to gold_export/parts/6Q_mount_belt_pulley_without_teeth.step; the preview shows one small post-and-boss part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD filename's 'mount_belt_pulley_without_teeth' wording is interpreted in the neighboring belt-pulley context of rows 6O, 6P, 6R, and 6S."
  uncertainty_notes:
    - "The row does not identify the mating pulley or fastener interface, so the exact load path and mounting orientation are inferred from local BOM context and shape."
mass:
  value_kg: 0.0143
  basis: "FreeCAD volume 1782.434 mm^3 converted to 1.782434e-6 m^3 and multiplied by the assembly STEP material metadata density of 8000 kg/m^3, yielding about 0.01426 kg per part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Q_mount_belt_pulley_without_teeth.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1782.434 mm^3, area 1184.884 mm^2, and bounding box 13.68 x 20.00 x 30.80 mm; local assembly STEP material extraction matched Stainless Steel with density 8000.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid is treated as the complete per-unit geometry for one BOM row 6Q part."
    - "The STEP material metadata density is used directly as the stainless steel density constant for the CAD volume calculation."
  uncertainty_notes:
    - "The estimate excludes any separate bearing, screw, washer, or pulley hardware that may assemble with this mount elsewhere in the BOM."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6Q_mount_belt_pulley_without_teeth reports material Stainless Steel and density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The extracted material gives a family, not a specific stainless grade."
how_to_make:
  summary: "Machine as a small one-piece stainless steel pulley mount/idler post from bar or rod stock, then deburr and inspect."
  manufacturing_steps:
    - "Cut stainless steel bar or rod stock to a blank slightly larger than the 13.68 x 20.00 x 30.80 mm CAD envelope."
    - "Turn the cylindrical post features and shoulders on a lathe or mill-turn setup."
    - "Mill the transverse boss/flange surfaces and any required flats or relief geometry."
    - "Deburr edges, clean the part, and inspect the post diameter, boss width, and overall height against the STEP geometry."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Q_mount_belt_pulley_without_teeth.step; research/ream250_bom/ream250_bom_row_0195_6Q__views_2x2.png"
    cited_fact_or_basis: "The STEP is a single solid with a 13.68 x 20.00 x 30.80 mm bounding box; the preview shows a cylindrical post integrated with a transverse boss/flange. targeted_web_search: searched \"6Q_mount_belt_pulley_without_teeth material\", \"reAM250 6Q mount_belt_pulley_without_teeth\", and \"mount belt pulley without teeth stainless steel\"; found duplicate BOM listings and generic pulley/idler pages, but no row-specific manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A subtractive route is chosen because the part is small, metallic, axis-featured, and appears to be a one-piece machined bracket/post rather than a sheet-metal or molded component."
    - "No heat treatment or coating is specified because the BOM and STEP metadata only resolve stainless steel family and geometry."
  uncertainty_notes:
    - "The STEP preview does not expose tolerances or surface finish requirements, so lathe/milling operations are a plausible route rather than a process plan."
kb_implications:
  - "item_granularity: simple_part - one small stainless steel pulley mount/idler support that can be modeled as a machined part from stainless stock; associated bearing or pulley hardware should remain separate BOM items."
---

Research result for reAM250 BOM row 195.
