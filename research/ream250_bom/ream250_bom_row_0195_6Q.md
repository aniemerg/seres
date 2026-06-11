---
function:
  summary: "Small stainless-steel belt pulley or pulley mount component for the reAM250 belt path; the source name identifies a belt pulley without teeth, and the matched CAD file is a compact single solid."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv:195 and design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv:195"
    cited_fact_or_basis: "BOM row 195 lists item 6Q, quantity 9, as '6Q_mount_belt_pulley_without_teeth'; manifest row 195 maps it to a matched part STEP export with one instance found."
    confidence: medium
mass:
  value_kg: 0.014259
  basis: "Per unit mass from CAD volume and STEP material density: FreeCAD reports volume 1782.4339059137299 mm^3 for one solid. The assembly STEP material extractor reports Stainless Steel with density 8000.0 kg/m^3-like units, giving 0.014259 kg per part. BOM quantity 9 implies about 0.128335 kg total for the row."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Q_mount_belt_pulley_without_teeth.step"
    cited_fact_or_basis: "FreeCAD Part.Shape read of the STEP file: 1 solid, volume 1782.4339059137299 mm^3, area 1184.884312061741 mm^2, bounding box 13.684210526315127 x 20.0 x 30.800000000000228 mm."
    confidence: high
material:
  primary_material: "Stainless Steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "extract_step_materials.py for product '6Q_mount_belt_pulley_without_teeth' found material 'Stainless Steel' and density 8000.0."
    confidence: high
how_to_make:
  summary: "Make as a small stainless machined pulley or pulley-mount part: cut a blank, turn or mill the belt-contact geometry from the CAD model, finish any bore or mounting features, then deburr and inspect."
  manufacturing_steps:
    - "Cut stainless stock or near-net blank sized for the 13.7 x 20.0 x 30.8 mm CAD envelope."
    - "Turn or mill the circular belt-contact/pulley surfaces and any central mounting geometry from the STEP model."
    - "Drill, ream, or finish attachment features shown in the CAD model."
    - "Deburr, clean, and inspect dimensions and surface finish before installation in the belt path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6Q_mount_belt_pulley_without_teeth.step"
    cited_fact_or_basis: "Manufacturing route inferred from the matched single-solid stainless CAD geometry and compact pulley-like part name; no vendor process sheet or third-party part link is present in the BOM row."
    confidence: medium
assumptions:
  - "CAD units are interpreted as millimeters, consistent with the small 13.7 x 20.0 x 30.8 bounding box."
  - "The mass value is per physical part, not the row total; multiply by BOM quantity 9 for row mass."
  - "Because no manufacturer or third-party link is present, the manufacturing route is a practical process inference from CAD geometry and material metadata."
uncertainty_notes:
  - "The BOM row has no manufacturer, product ID, material family hint, or third-party URL."
  - "The part name says belt pulley without teeth, but the STEP file was not semantically annotated beyond the product name and geometry."
  - "No local or vendor evidence identifies a specific stainless grade, heat treatment, bearing interface, or surface finish requirement."
kb_implications:
  - "Model as a small discrete stainless pulley or pulley-mount part for belt guidance, with per-unit mass about 0.0143 kg."
  - "Do not create a specific stainless alloy grade from this row alone; use generic stainless steel unless later evidence identifies a grade."
  - "For a simplified KB BOM, this may fold into a belt pulley or motion-axis hardware group if fine pulley variants are below the needed modeling resolution."
---

# reAM250 BOM Row 195 - Item 6Q

The current row evidence supports a concise component entry: quantity 9 of a small stainless belt pulley or pulley-mount part. CAD geometry is available and matched, and the full assembly STEP provides explicit Stainless Steel material metadata, so the mass estimate is stronger than rows with only generic material tags.
