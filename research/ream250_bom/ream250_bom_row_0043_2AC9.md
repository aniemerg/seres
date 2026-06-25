---
row_identity:
  item: "2AC9"
  cad_file: "2AC9_part_9"
  source_row_number: 43
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One lower-axis bearing support block or bracket for the reAM250 axis bearing bottom group, with a central bearing/shaft bore and side mounting features."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC9_part_9.step; research/ream250_bom/ream250_bom_row_0043_2AC9__views_2x2.png"
    cited_fact_or_basis: "BOM row 43 identifies item 2AC9, quantity 1, CAD file 2AC9_part_9, description 'axis bearing bottom'. The manifest maps the row to gold_export/parts/2AC9_part_9.step with matched_existing part status. FreeCAD measured one solid with bounding box 86.00 x 24.00 x 58.00 mm, and the contact sheet shows a blocky bracket with a large central circular bore plus smaller side mounting holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the physical lower bearing support part for this row."
  uncertainty_notes:
    - "The BOM names the bottom-axis bearing group but does not identify the exact mating shaft, bearing insert, or fastener interfaces used with this support block."
mass:
  value_kg: 0.49
  basis: "Per-unit planning estimate for quantity 1. FreeCAD volume is 62373.201 mm^3, equal to 6.2373201e-5 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.4896 kg, rounded to 0.49 kg. If the same CAD volume were aluminum at 2700 kg/m^3, mass would be about 0.168 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC9_part_9.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 62373.201 mm^3, area 15145.115 mm^2, and bounding box 86.00 x 24.00 x 58.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried '\"2AC9\" \"axis bearing bottom\"', '\"reAM250\" \"axis bearing bottom\"', and '\"2AC9_part_9\"'; results duplicated the BOM row identity but did not provide row-specific material, mass, drawing, or catalog data."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-like density is used as the conservative single-value planning estimate because the part is a bearing support block with load-bearing geometry and no row-specific material."
    - "The CAD solid volume is treated as the physical solid volume of one item."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so the estimate depends on the steel-density assumption; an aluminum part would be much lighter."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0043_2AC9__views_2x2.png"
    cited_fact_or_basis: "BOM row 43 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2AC9_part_9 returned material 'Generic' with density 1000.0, which is placeholder metadata. The contact sheet shows a rigid machined support-block form. targeted_web_search: tried '\"2AC9\" \"axis bearing bottom\"', '\"reAM250\" \"axis bearing bottom\"', and '\"2AC9_part_9\"'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The load-bearing bracket/block geometry and axis-bearing context indicate a metal part rather than a polymer, seal, or consumable."
  uncertainty_notes:
    - "The evidence supports only a broad metal/alloy family; downstream KB modeling should not assign a specific grade without a drawing, material callout, or related assembly note."
how_to_make:
  summary: "Fabricate as a one-piece machined bearing support bracket from metal billet or plate stock"
  manufacturing_steps:
    - "Cut a metal billet or thick plate blank large enough for the 86 x 24 x 58 mm envelope."
    - "CNC mill the external block, feet, and angled relief faces."
    - "Drill, bore, or ream the central bearing/shaft opening and the smaller side mounting holes."
    - "Deburr and inspect hole location, bore diameter, flatness, and mounting-face alignment."
    - "Apply any required corrosion protection or cleaning compatible with the axis bearing assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC9_part_9.step; research/ream250_bom/ream250_bom_row_0043_2AC9__views_2x2.png"
    cited_fact_or_basis: "The CAD preview shows a one-piece block/bracket with a central bore, mounting ears/feet, smaller side holes, and machined-looking planar faces; FreeCAD measured one solid. targeted_web_search: tried '\"2AC9\" \"axis bearing bottom\"', '\"reAM250\" \"axis bearing bottom\"', and '\"2AC9_part_9\"'; no source stated a row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining from metal stock is the most plausible low-volume route for the observed one-piece bearing support geometry."
  uncertainty_notes:
    - "The CAD preview is sufficient for route triage but not for tolerance, fit, material grade, heat treatment, or surface-finish requirements."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable custom machined metal bearing support/bracket, likely shared conceptually with adjacent 2AC bottom-axis-bearing rows, rather than as a purchased module or raw stock."
---

Research result for the leased reAM250 BOM row only.
