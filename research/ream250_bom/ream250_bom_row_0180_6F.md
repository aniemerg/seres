---
row_identity:
  item: "6F"
  cad_file: "6F_powder_container_extension_back"
  source_row_number: 180
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One of four small back-side extension plates for the reAM250 recoater powder-container assembly, likely extending or closing the rear powder-container edge near the adjacent front extension, powder chute, and seal rows."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6F_powder_container_extension_back.step; research/ream250_bom/ream250_bom_row_0180_6F__views_2x2.png"
    cited_fact_or_basis: "BOM row 180 lists item 6F, quantity 4, CAD file 6F_powder_container_extension_back. Manifest row 180 maps it to a matched existing part STEP. Neighboring BOM rows name powder-container plates, a front extension, a powder chute, top seal, and bottom brush seal. FreeCAD measured one solid with bounding box 37.75 x 118.50 x 3.00 mm, and the rendered preview shows a thin asymmetric plate or folded extension piece."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and neighboring powder-container rows are interpreted as the local assembly context for this extension plate."
    - "Each of the four row instances is treated as the same physical part."
  uncertainty_notes:
    - "The BOM and STEP do not expose mating constraints, so the exact rear-edge interface and whether the part primarily acts as a spacer, wall extension, or retaining lip remain inferred."
mass:
  value_kg: 0.0287
  basis: "Per-unit estimate for one physical 6F extension. FreeCAD volume is 10632.268 mm^3 = 1.0632268e-5 m^3. Assembly STEP material metadata gives Aluminum 6061 density 2700 kg/m^3, so computed mass is 1.0632268e-5 m^3 * 2700 kg/m^3 = 0.02871 kg per unit. BOM quantity is 4, so the row total is about 0.115 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6F_powder_container_extension_back.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 10632.268 mm^3, area 8069.065 mm^2, and bounding box 37.75 x 118.50 x 3.00 mm. Local assembly STEP material extraction matched product 6F_powder_container_extension_back to material Aluminum 6061 with density 2700.0. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished volume of one extension plate."
    - "The assembly STEP density value is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes any separate fasteners, seals, adhesive, or neighboring powder-container pieces that are separate BOM rows."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 6F_powder_container_extension_back to material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local metadata gives the alloy family/grade but not temper, surface treatment, or finish."
how_to_make:
  summary: "Make as a custom Aluminum 6061 powder-container extension plate: cut or mill the thin profile from 3 mm aluminum stock, machine the asymmetric edges and relief geometry, deburr, clean, and inspect fit against the powder-container back assembly."
  manufacturing_steps:
    - "Start from Aluminum 6061 sheet or plate stock near the 3.00 mm finished thickness."
    - "CNC profile-cut or mill the asymmetric outline and any edge reliefs shown by the STEP geometry."
    - "Machine shallow face/rib geometry if the STEP features are not achievable by simple cutting alone."
    - "Deburr and clean all powder-contact or assembly-contact edges."
    - "Inspect thickness, outline, and fit against the rear powder-container extension location."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6F_powder_container_extension_back.step; research/ream250_bom/ream250_bom_row_0180_6F__views_2x2.png"
    cited_fact_or_basis: "The STEP geometry is one thin Aluminum 6061 solid with a 37.75 x 118.50 x 3.00 mm envelope; the rendered contact sheet shows an asymmetric flat/faceted extension plate without purchased-module features. targeted_web_search: tried '\"6F_powder_container_extension_back\"', '\"reAM250\" \"powder_container_extension_back\"', and '\"6F\" \"powder container extension back\" \"Aluminum 6061\"'; results only duplicated BOM row identity or generic Aluminum 6061 pages, with no row-specific fabrication drawing or manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "CNC cutting/milling from 3 mm Aluminum 6061 stock is the most plausible Manufacturing route for the observed one-piece thin plate geometry."
    - "Powder-container service requires clean, deburred edges to reduce powder hangups and contamination."
  uncertainty_notes:
    - "No row-specific drawing was found, so bend radii, flatness, tolerances, fastener interfaces, and surface-finish requirements remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable custom Aluminum 6061 thin plate/extension piece for the powder-container assembly, not as a purchased module."
---

Research result for the leased reAM250 BOM row only.
