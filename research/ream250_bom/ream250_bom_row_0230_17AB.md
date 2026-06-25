---
row_identity:
  item: "17AB"
  cad_file: "17AB_strut_profile_20X20_473"
  source_row_number: 230
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 20 x 20 mm aluminum strut profile used as a light structural frame rail or support member; BOM quantity is 6."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AB_strut_profile_20X20_473.step; https://docs.rs-online.com/ea04/A700000007302204.pdf"
    cited_fact_or_basis: "The BOM row names item 17AB as a Bosch Rexroth AG strut profile. FreeCAD measured a 472.50 x 20.00 x 20.00 mm single solid, and the rendered preview shows a long square slotted extrusion. The Bosch Rexroth strut profile 20x20 datasheet describes 6 mm slot profiles for light structures such as supports and lab fixtures. bom_url_route_check: the BOM-provided Bosch Rexroth store URL was checked as a strut-profile product-family route but did not expose a row-specific 20x20 cut-length technical table in the accessible page; the RS-hosted Bosch Rexroth PDF was used for the 20x20 function/spec facts."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The row does not provide a Bosch article number for the exact cut piece; identity is locked to the BOM description, manufacturer, CAD envelope, and 20x20 profile family."
mass:
  value_kg: 0.189
  basis: "Per unit mass is calculated from the Bosch Rexroth 20x20 profile mass of 0.4 kg/m and the CAD length of 472.50 mm: 0.4 kg/m * 0.4725 m = 0.189 kg per cut profile. BOM quantity is 6, so row total is about 1.13 kg. CAD solid volume is 78255.003 mm^3; using local aluminum density 2700 kg/m^3 would give about 0.211 kg, close enough to support the catalog mass-per-meter estimate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AB_strut_profile_20X20_473.step; kb/materials/properties.yaml; https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 78255.003 mm^3, area 85861.387 mm^2, and bounding box 472.50 x 20.00 x 20.00 mm. The Bosch Rexroth 20x20 datasheet lists mass 0.4 for the profile; the Bosch Rexroth distributor page states weight per metre is 0.4 kg for 20 x 20 mm Bosch Rexroth aluminum strut profile. The local material table lists aluminum density 2700 kg/m^3. bom_url_route_check: the BOM-provided Bosch Rexroth store URL was checked as a strut-profile product-family route but did not expose a row-specific 20x20 cut-length mass table in the accessible page; the RS-hosted Bosch Rexroth PDF and Bosch Rexroth distributor page were used for the mass-per-meter fact."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD length of 472.50 mm is the physical cut length represented by one BOM row item."
    - "The catalog 0.4 kg/m value applies to the same Bosch Rexroth 20x20, slot-6 aluminum strut profile family."
  uncertainty_notes:
    - "The CAD material extractor returned only Generic with density 1000, so material metadata from the assembly STEP was ignored for mass."
    - "The PDF's mass unit label is terse; the distributor page clarifies the same Bosch Rexroth 20x20 profile weight as per metre."
material:
  primary_material: "anodized aluminum Bosch Rexroth 20x20 strut profile"
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/"
    cited_fact_or_basis: "The Bosch Rexroth 20x20 datasheet lists material as anodized aluminum for the strut profile family, and the Bosch Rexroth distributor page identifies the 20 x 20 mm profile as aluminum with anodized finish. bom_url_route_check: the BOM-provided Bosch Rexroth store URL was checked as a strut-profile product-family route but did not expose row-specific material details in the accessible page; the RS-hosted Bosch Rexroth PDF and Bosch Rexroth distributor page were used for material."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "No exact alloy grade was resolved for the BOM row. A separate Bosch Rexroth aluminum framing technical-data PDF identifies Rexroth strut-profile material families such as EN AW-6060 / AW-6063-T66, but this row result keeps the material at the sourced anodized-aluminum family level."
how_to_make:
  summary: "Model as a cut-to-length external aluminum T-slot/strut extrusion: extrude the aluminum profile, anodize, saw cut to the 472.5 mm CAD length, deburr, and inspect length and slot geometry"
  manufacturing_steps:
    - "Extrude aluminum alloy through a 20 x 20 mm slot-6 strut-profile die."
    - "Straighten and age or temper the extrusion according to the profile supplier's standard process."
    - "Anodize the profile to the natural aluminum finish stated for the product family."
    - "Saw cut the standard-length profile to about 472.5 mm, then deburr the cut ends."
    - "Inspect length, cross-section, slot opening, and straightness before frame assembly."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0230_17AB__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AB_strut_profile_20X20_473.step; https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/"
    cited_fact_or_basis: "The CAD preview shows a long slotted 20x20 profile, and FreeCAD measured a 472.50 mm long part. Bosch Rexroth documentation identifies the item family as a 20x20 strut profile with 6 mm groove and anodized aluminum material. The distributor page says the Bosch Rexroth 20x20 aluminum profile can be cut to required size. bom_url_route_check: the BOM-provided Bosch Rexroth store URL was checked as a strut-profile product-family route but did not expose row-specific manufacturing details in the accessible page; the Bosch Rexroth PDF and distributor page were used for product identity and cut-to-size evidence."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route infers standard aluminum extrusion and saw-cut finishing from the sourced strut-profile geometry and material."
    - "No precision machining beyond cutting/deburring is needed for this plain cut-length profile unless later assembly requires tapped or drilled ends."
  uncertainty_notes:
    - "The cited sources resolve product family, material, and cut-to-size availability but do not state the actual Bosch production route for this specific cut piece."
    - "Targeted_web_search: searched \"Bosch Rexroth strut profile 20x20 0.4 kg/m material\", \"site:boschrexroth.com strut profile 20x20 aluminum anodized mass kg/m\", and \"17AB_strut_profile_20X20_473 Bosch Rexroth\" found row-family product specifications and cut-to-size evidence, but no row-specific manufacturing process sheet for 17AB."
kb_implications:
  - "item_granularity: simple_part - reusable cut length of standard 20x20 anodized aluminum strut/profile stock; later KB modeling should prefer one generic profile-stock item with length handled in BOM notes or quantity rather than a unique item for every cut length."
---

# reAM250 BOM Row 230 - 17AB

Research result for the leased reAM250 BOM row.
