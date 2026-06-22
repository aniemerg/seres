---
row_identity:
  item: "3S43"
  cad_file: "3S43_part_3"
  source_row_number: 154
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One thin formed piece of the reAM250 gas outlet, apparently acting as a deflector or wall segment in the outlet flow path rather than as a purchased valve or sensor."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S43_part_3.step; research/ream250_bom/ream250_bom_row_0154_3S43__views_2x2.png"
    cited_fact_or_basis: "BOM row 154 names item 3S43 as 'gas outlet: part 3' with quantity 1. FreeCAD measured one solid and the rendered contact sheet shows a thin bent/faceted panel about 35.00 x 50.00 x 90.71 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical item for this BOM row."
  uncertainty_notes:
    - "The BOM names the parent function as gas outlet but does not identify the exact internal face, duct side, or assembly interface this panel occupies."
mass:
  value_kg: 0.039
  basis: "Per-unit planning estimate for quantity 1. FreeCAD volume is 5023.879 mm^3, equal to 5.023879e-6 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.0394 kg; if the same CAD volume were aluminum at 2700 kg/m^3, it would be about 0.0136 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S43_part_3.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 5023.879 mm^3 and bounding box 35.00 x 50.00 x 90.71 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried 'reAM250 3S43 gas outlet part 3 material', '\"3S43\" \"gas outlet\" \"reAM250\"', '\"gas outlet: part 3\" \"3S43\"', and '\"reAM250\" \"gas outlet\"'; results duplicated the BOM identity or gave general reAM250/gas-flow context, with no row-specific mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-like density is used as the conservative single-value planning estimate because the gas-outlet panel is a thin machine duct/deflector part and no row-specific material is provided."
  uncertainty_notes:
    - "Actual mass could be closer to 0.014 kg if this part is aluminum rather than steel; no catalog weight or material-specific STEP metadata resolves that range."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 154 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 3S43_part_3 returned material 'Generic' with density 1000.0, which is placeholder metadata. targeted_web_search: tried 'reAM250 3S43 gas outlet part 3 material', '\"3S43\" \"gas outlet\" \"reAM250\"', '\"gas outlet: part 3\" \"3S43\"', and '\"reAM250\" \"gas outlet\"'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The thin rigid CAD geometry and gas-outlet service indicate a metal sheet or plate part rather than a polymer seal, filter, or consumable."
  uncertainty_notes:
    - "Material family is broad only; downstream KB modeling should not select a specific grade without checking the full gas-outlet assembly design intent."
how_to_make:
  summary: "Fabricate as a small formed sheet/plate gas-outlet panel, or procure as part of the reAM250 gas-outlet fabrication package."
  manufacturing_steps:
    - "Cut a thin metal blank to the CAD profile from sheet or plate stock."
    - "Form the bends/faceted faces shown in the STEP geometry."
    - "Deburr edges and verify fit against the neighboring gas-outlet pieces."
    - "Apply any required surface finish or cleaning compatible with the build-chamber gas path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S43_part_3.step; research/ream250_bom/ream250_bom_row_0154_3S43__views_2x2.png"
    cited_fact_or_basis: "CAD preview shows a thin bent/faceted panel without visible purchased-module features; FreeCAD reports one solid with small sheet-like volume. targeted_web_search: tried 'reAM250 3S43 gas outlet part 3 material', '\"3S43\" \"gas outlet\" \"reAM250\"', '\"gas outlet: part 3\" \"3S43\"', and '\"reAM250\" \"gas outlet\"'; no source stated the manufacturing route for this row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet cutting and forming are the most plausible local route for a thin one-piece gas-outlet panel with the observed folded geometry."
  uncertainty_notes:
    - "The CAD preview is sufficient for route triage but not for bend radius, thickness, tolerance, or surface-finish requirements."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable one-piece formed metal gas-outlet panel/deflector rather than as a purchased module."
---

Result generated for the leased reAM250 BOM row only.
