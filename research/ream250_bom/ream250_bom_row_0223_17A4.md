---
row_identity:
  item: "17A4"
  cad_file: "17A4_strut_profile_20X20_463"
  source_row_number: 223
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Cut length of Bosch Rexroth 20 mm strut/profile extrusion used as a lightweight structural rail or frame member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A4_strut_profile_20X20_463.step; research/ream250_bom/ream250_bom_row_0223_17A4__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
    cited_fact_or_basis: "BOM row 223 identifies item 17A4 as quantity 2, CAD file 17A4_strut_profile_20X20_463, description 'strut profile', manufacturer Bosch Rexroth AG. FreeCAD measured a 463.7 x 20.0 x 20.0 mm single solid, and the rendered preview shows a long square slotted extrusion profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one cut-to-length strut profile per physical item; the BOM quantity of 2 means two identical profiles."
  uncertainty_notes:
    - "The BOM URL is a product-family route rather than a row-specific configured length page, so exact catalog article number is not locked beyond the CAD length and BOM identity."
mass:
  value_kg: 0.207
  basis: "Per unit: FreeCAD volume 76,797.555 mm^3 = 0.000076797555 m^3; assembly STEP metadata density for this product is 2700 kg/m^3; mass = 0.207353 kg, rounded to 0.207 kg. BOM quantity is 2, so row total is about 0.415 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A4_strut_profile_20X20_463.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD shape read reported 1 solid, volume 76,797.555 mm^3, area 84,268.444 mm^2, and bounding box 463.7 x 20.0 x 20.0 mm. Local assembly STEP material extraction for product 17A4_strut_profile_20X20_463 returned material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported CAD solid volume is treated as the volume of one physical BOM-row profile."
    - "The STEP material density is treated as kg/m^3-like, consistent with the extractor note for the reAM250 export."
  uncertainty_notes:
    - "Small CAD export or tessellation differences could shift the mass slightly, but the result is within the precision needed for BOM planning."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 17A4_strut_profile_20X20_463 returned material Aluminum 6061 and density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row uses the material metadata attached to the full assembly product definition rather than any generic material placeholder in the standalone STEP."
  uncertainty_notes:
    - "The Bosch strut-profile family is commonly sold as anodized aluminum, but the row-specific local metadata does not separately specify anodized surface finish or temper."
how_to_make:
  summary: "Prepare as a Bosch Rexroth modular aluminum strut profile cut to the CAD length, or locally make by extruding a 20 x 20 mm slotted aluminum profile, cutting to about 463.7 mm, deburring, and applying a protective/anodized finish if needed"
  manufacturing_steps:
    - "Extrude Aluminum 6061 billet through a die matching the 20 x 20 mm slotted profile cross-section."
    - "Cut the extrusion to the CAD length of about 463.7 mm."
    - "Deburr cut ends and inspect slot geometry, straightness, and length."
    - "Apply anodized or equivalent corrosion-resistant finish if the installed environment requires the standard Bosch-style finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A4_strut_profile_20X20_463.step; research/ream250_bom/ream250_bom_row_0223_17A4__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
    cited_fact_or_basis: "BOM row identifies a Bosch Rexroth AG strut profile; CAD and preview show a long 20 x 20 mm slotted extrusion. targeted_web_search: tried 'Bosch Rexroth strut profile 20x20 aluminum 6061 profile'; usable results matched the Bosch Rexroth 20x20 anodized aluminum strut-profile product family, but did not state a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A slotted constant-cross-section aluminum profile is best produced as an extrusion and then cut to length."
  uncertainty_notes:
    - "The detailed die design, alloy temper, and finish specification are not provided by the row evidence."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length aluminum structural profile, with length captured in BOM/recipe notes rather than as a calibrated purchased module."
---
