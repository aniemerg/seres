---
row_identity:
  item: "17AE"
  cad_file: "17AE_strut_profile_20X20_604"
  source_row_number: 233
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Structural 20 x 20 mm slotted strut profile used as a light frame/support member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AE_strut_profile_20X20_604.step; https://docs.rs-online.com/ea04/A700000007302204.pdf"
    cited_fact_or_basis: "BOM and manifest identify row 233 as Bosch Rexroth AG item 17AE, description 'strut profile', CAD file 17AE_strut_profile_20X20_604; FreeCAD measured one solid with 604.0 x 20.0 x 20.0 mm bounding box; Bosch Rexroth product data describes 20x20 strut profiles with 6 mm slot for light structures such as supports and lab fixtures. bom_url_route_check: BOM URL is the Bosch Rexroth strut-profile store category; row-specific catalog facts were resolved from a Bosch Rexroth PDF hosted by RS because the BOM category route did not expose the row's 20x20 technical table in the local scrape."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD filename suffix 604 and the measured bounding box indicate this BOM row is the 604 mm cut length of the Bosch Rexroth 20x20 strut profile family."
  uncertainty_notes:
    - "The row does not give a Bosch ordering number, so exact end machining options are inferred only from the CAD filename and geometry."
mass:
  value_kg: 0.2416
  basis: "Per-unit mass from Bosch Rexroth 20x20 profile catalog mass 0.4 kg/m multiplied by CAD-measured length 0.604 m = 0.2416 kg. BOM quantity is 2, so row total is about 0.483 kg. CAD volume was 100033.909 mm^3, which is consistent with an approximately 1.66 cm^2 extrusion cross-section."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AE_strut_profile_20X20_604.step"
    cited_fact_or_basis: "Bosch Rexroth 20x20 strut profile technical data lists mass m = 0.4 kg/m; FreeCAD measured the row-specific STEP length as 604.0 mm and volume as 100033.909 mm^3. bom_url_route_check: BOM URL is the Bosch Rexroth strut-profile store category; mass per meter was resolved from the Bosch Rexroth PDF because the BOM category page did not expose the row-specific technical mass in the local scrape."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The catalog mass per meter applies to the same standard 20x20 profile cross-section represented by this CAD file."
  uncertainty_notes:
    - "Any drilled, tapped, or cut-end finishing mass difference is expected to be small relative to this coarse BOM estimate but is not separately modeled."
material:
  primary_material: "anodized aluminum Bosch Rexroth strut profile; Rexroth profile alloy family EN AW-6060 / AW-6063-T66"
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "Bosch Rexroth 20x20 strut profile product data lists material as anodized aluminum; Bosch Rexroth aluminum framing technical data identifies Rexroth strut profiles as EN AW-Al MgSi with material designation EN AW-6060 and AW-6063-T66. bom_url_route_check: BOM URL is the Bosch Rexroth strut-profile store category; material details were resolved from Bosch Rexroth PDF data because the BOM category route did not expose the row-specific technical material in the local scrape."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The general Rexroth strut-profile alloy data applies to this Bosch Rexroth 20x20 profile row."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic with density 1000.0, so local STEP metadata does not independently resolve material."
how_to_make:
  summary: "Prepare as a Bosch Rexroth 20x20 anodized aluminum strut profile cut to 604 mm; extrude the slotted aluminum profile, anodize it, and saw/cut to length with any end finishing required by the frame design"
  manufacturing_steps:
    - "Produce"
    - "Extrude the 20 x 20 mm slot-6 strut profile cross-section."
    - "Anodize the profile surface."
    - "Cut one profile to 604 mm length and deburr or finish ends as needed."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; research/ream250_bom/ream250_bom_row_0233_17AE__views_2x2.png"
    cited_fact_or_basis: "Bosch Rexroth product data identifies this family as 20x20 anodized aluminum strut profiles and lists configurable lengths/orders; rendered CAD preview shows a long constant-section slotted profile. targeted_web_search: tried 'Bosch Rexroth strut profile 20x20 material aluminum 20x20' and 'site:boschrexroth.com strut profile 20x20 Bosch Rexroth material aluminum 20x20'; results found Bosch/Rexroth product data but no row-specific manufacturing process statement beyond profile/material/finish facts."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Extrusion plus anodizing is the plausible manufacturing route for a constant-section anodized aluminum strut profile."
  uncertainty_notes: []
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length structural aluminum extrusion profile rather than a machine-specific purchased module."
---

