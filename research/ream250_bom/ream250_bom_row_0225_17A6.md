---
row_identity:
  item: 17A6
  cad_file: 17A6_strut_profile_20X20_D108
  source_row_number: 225
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
  link_url: https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE
function:
  summary: >
    Short Bosch Rexroth 20x20 aluminum strut profile used as a light structural
    member in the reAM250 frame or support structure, with T-slot-like grooves
    for modular fastening.
  source:
    url_or_path: >
      design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv;
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A6_strut_profile_20X20_D108.step;
      research/ream250_bom/ream250_bom_row_0225_17A6__views_2x2.png
    cited_fact_or_basis: >
      BOM row 225 identifies item 17A6 as "strut profile" from Bosch Rexroth
      AG. FreeCAD measured a 131.0 mm x 20.0 mm x 20.0 mm single solid, and
      the rendered contact sheet shows a slotted rectangular extrusion profile.
    evidence_basis: bom_provided
  assumptions:
    - The row represents one cut profile segment because quantity is 1 and the CAD export contains one solid.
  uncertainty_notes:
    - The exact installed load path is not identified by the row alone, so the function is limited to structural frame/support use.
mass:
  value_kg: 0.0604
  basis: >
    Per unit. FreeCAD volume is 22355.677 mm3, equal to 0.000022355677 m3.
    Multiplying by the row-specific STEP density of 2700 kg/m3 gives
    0.06036 kg for the single 131 mm cut length. Quantity is 1, so row total is
    also about 0.0604 kg.
  source:
    url_or_path: >
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A6_strut_profile_20X20_D108.step;
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step;
      kb/materials/properties.yaml
    cited_fact_or_basis: >
      FreeCAD measured 1 solid, volume 22355.677 mm3, surface area
      23559.111 mm2, and bounding box 131.0 mm x 20.0 mm x 20.0 mm. The local
      assembly STEP material extractor returned material "Aluminum 6061" with
      density 2700.0 for product 17A6_strut_profile_20X20_D108. The local
      density table lists aluminum density as 2700 kg/m3.
    evidence_basis: bom_provided
  assumptions:
    - The STEP solid volume is treated as the physical aluminum volume of one row item.
    - The local aluminum density constant is appropriate for the STEP material label Aluminum 6061.
  uncertainty_notes:
    - CAD export tolerances and small modeled details may shift the mass slightly, but the estimate is within the needed BOM planning scale.
material:
  primary_material: Aluminum 6061
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: >
      The local assembly STEP material extractor matched product
      17A6_strut_profile_20X20_D108 and returned material "Aluminum 6061" with
      density 2700.0.
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - Surface treatment is not explicit in the local material metadata; Bosch strut profiles are commonly anodized, but this row-specific result keeps the sourced material to Aluminum 6061.
how_to_make:
  summary: >
    Model as cut-to-length aluminum extrusion stock: extrude a 20x20 slotted
    6061 aluminum profile, cut to the CAD length, deburr, and optionally anodize
    Or otherwise finish before assembly.
  manufacturing_steps:
    - Extrude Aluminum 6061 through a die matching the 20x20 slotted profile.
    - Cut the extrusion to the CAD-measured 131 mm length.
    - Deburr cut ends and inspect slot geometry and overall length.
    - Apply anodizing or comparable corrosion-resistant finish if required by the local assembly environment.
  source:
    url_or_path: >
      Design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A6_strut_profile_20X20_D108.step;
      Https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE
    cited_fact_or_basis: >
      The BOM URL route and row identify a Bosch Rexroth strut profile, while
      The CAD geometry shows a constant 20x20 slotted cross-section. targeted_web_search:
      Queries tried "Bosch Rexroth strut profile 20x20 manufacturing extrusion
      Anodized" and "Bosch Rexroth 20x20 strut profile aluminum catalog" results
      Supported aluminum profile stock but did not provide a row-specific factory
      Process for this cut length.
    evidence_basis: engineering_hypothesis
  assumptions:
    - A constant-section aluminum strut profile is best represented as extruded stock cut to length.
    - Use a generic aluminum extrusion and finishing workflow rather than a machine-specific custom machining route.
  uncertainty_notes:
    - The exact Bosch production process and finish for this row are not specified in the BOM or local STEP metadata.
kb_implications:
  - "item_granularity: simple_part - Treat as reusable aluminum profile stock or cut-to-length extrusion rather than a unique machine-specific part."
---

Research result for reAM250 BOM row 225.
