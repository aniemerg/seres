---
row_identity:
  item: "17A3"
  cad_file: "17A3_strut_profile_20X20_135"
  source_row_number: 222
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short Bosch Rexroth 20 x 20 mm slotted aluminum strut profile used as a modular frame member or spacer in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A3_strut_profile_20X20_135.step; research/ream250_bom/ream250_bom_row_0222_17A3__views_2x2.png"
    cited_fact_or_basis: "BOM row 222 names item 17A3 as a Bosch Rexroth AG 'strut profile' with quantity 1. The manifest maps the row to 17A3_strut_profile_20X20_135.step. FreeCAD measured one solid with a 120.00 x 20.00 x 20.00 mm bounding box, and the rendered contact sheet shows a square slotted extrusion profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file is the physical item represented by this BOM row."
  uncertainty_notes:
    - "The CAD filename ends in 135 while FreeCAD reports a 120.00 mm bounding length; the function as a short 20 x 20 strut profile is unaffected."
mass:
  value_kg: 0.0537
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 19874.286 mm^3, or 1.9874286e-5 m^3. Using the row-specific STEP material density of 2700 kg/m^3 gives 0.0537 kg. As a sanity check, Bosch Rexroth 20 x 20 profile catalog mass values around 0.4-0.5 kg/m imply about 0.048-0.060 kg for a 120 mm segment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A3_strut_profile_20X20_135.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 19874.286 mm^3 and bounding box 120.00 x 20.00 x 20.00 mm. Local assembly STEP material extraction for product 17A3_strut_profile_20X20_135 returned Aluminum 6061 with density 2700.0. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The measured STEP volume excludes no hidden inserts or fasteners; the BOM row is treated as one cut extrusion segment."
  uncertainty_notes:
    - "If the intended physical length is 135 mm from the CAD filename rather than the 120 mm solid bounding box, mass would scale upward by roughly 12.5 percent for the same cross-section."
material:
  primary_material: "Aluminum 6061, anodized aluminum profile family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
    cited_fact_or_basis: "Assembly STEP material extraction for 17A3_strut_profile_20X20_135 returned Aluminum 6061 and density 2700.0. BOM row 222 identifies the item as a Bosch Rexroth AG strut profile and gives the Bosch Rexroth strut-profile shop route."
    evidence_basis: "bom_provided"
  assumptions:
    - "The Bosch Rexroth strut profile is treated as an anodized aluminum extrusion; the local STEP grade is used as the specific material grade for this row."
  uncertainty_notes:
    - "The public BOM URL is a product-family route rather than a row-specific part-number page, so surface finish and exact Rexroth alloy designation should be rechecked before precision manufacturing."
how_to_make:
  summary: "Procure as a Bosch Rexroth cut-to-length 20 x 20 aluminum strut profile, or locally reproduce by extruding the 20 x 20 slotted aluminum profile, cutting to length, deburring, and anodizing or otherwise finishing the segment."
  manufacturing_steps:
    - "Extrude Aluminum 6061 or a compatible structural aluminum alloy through a die matching the 20 x 20 mm slotted profile."
    - "Cut the extrusion to the row length represented by the STEP geometry."
    - "Deburr the cut ends and verify slot geometry for connectors or brackets."
    - "Anodize or apply an equivalent protective finish if matching the Bosch Rexroth profile family."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A3_strut_profile_20X20_135.step; research/ream250_bom/ream250_bom_row_0222_17A3__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
    cited_fact_or_basis: "BOM row evidence identifies a Bosch Rexroth strut profile, and CAD preview shows a constant 20 x 20 mm slotted extrusion. targeted_web_search: tried 'Bosch Rexroth strut profile 20x20 material aluminum mass kg m' and 'site:boschrexroth.com strut profile 20x20 Bosch Rexroth material'; results matched the Bosch Rexroth strut-profile product family and catalog/distributor pages for 20 x 20 aluminum profiles, but did not state a row-specific manufacturing process for this cut segment."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Aluminum extrusion plus cut-to-length finishing is the plausible local manufacturing route for a constant-section slotted structural profile."
  uncertainty_notes:
    - "The CAD and product-family evidence do not specify extrusion temper, anodizing thickness, cut tolerance, or end-machining details for this row."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut aluminum T-slot/strut extrusion segment, parameterized by profile size and length rather than as a purchased module."
---

Result generated for the leased reAM250 BOM row only.
