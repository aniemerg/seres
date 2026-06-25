---
row_identity:
  item: "96"
  cad_file: "96_profile_60x60_300"
  source_row_number: 299
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 60 x 60 mm slotted aluminum strut profile used as a short structural framing member in the reAM250 machine frame or support structure; the BOM row quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/96_profile_60x60_300.step; research/ream250_bom/ream250_bom_row_0299_96__views_2x2.png; https://www.boschrexroth.com/de/de/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "BOM row 299 identifies item 96, quantity 2, description 'strut profile', manufacturer Bosch Rexroth AG, and CAD file 96_profile_60x60_300. The manifest maps the row to the same per-part STEP file with matched_existing vendor_component status. The rendered CAD contact sheet shows a square slotted extrusion profile; FreeCAD measured one solid with a 240.00 x 60.00 x 60.00 mm bounding box. Bosch Rexroth's official aluminum profile system page describes system profiles for machine frames, workstations, shelves, safety fences, and other structures. official_alternate_route_check: the original BOM URL is a Bosch Rexroth Store strut-profile category URL; the used Bosch Rexroth aluminum-profile-kit page is an official Bosch Rexroth product-family route on boschrexroth.com and matches the row manufacturer and strut-profile product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents one physical strut-profile piece for this BOM row."
    - "The profile is treated as a structural frame/support member because the BOM row gives the generic strut-profile description rather than a more specific guard, cover, or tooling role."
  uncertainty_notes:
    - "The exact installed location in the reAM250 assembly is not stated in the row context."
    - "The CAD file name ends in 300, but the measured STEP bounding-box length is 240.00 mm; downstream use should preserve that length mismatch."
mass:
  value_kg: 0.937
  basis: "Per-unit mass estimate for one physical profile piece. FreeCAD measured CAD volume 346981.868 mm^3, equal to 0.000346981868 m^3. Assembly STEP material extraction for this product returned Aluminum with density 2700 kg/m^3, so 0.000346981868 m^3 * 2700 kg/m^3 = 0.93685 kg, rounded to 0.937 kg per unit. BOM quantity is 2, so the row total is about 1.87 kg. If the nominal file-name length of 300 mm were used with the same cross-section instead of the CAD-measured 240 mm length, the per-unit mass would scale to about 1.17 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/96_profile_60x60_300.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 346981.868 mm^3, area 219269.517 mm^2, and bounding box 240.00 x 60.00 x 60.00 mm. Local assembly STEP material extraction for product 96_profile_60x60_300 returned material Aluminum and density 2700.0. kb/materials/properties.yaml also lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the complete solid volume of one profile piece, including slots and internal voids."
    - "The extracted aluminum density is used as the calculation constant for the whole profile."
  uncertainty_notes:
    - "The mass is based on the CAD-measured 240 mm length, not the 300 mm length implied by the CAD file name."
    - "No separate catalog weight for this exact cut length was found in the row evidence; the CAD-volume calculation should be preferred for this row unless the length mismatch is later resolved."
material:
  primary_material: "aluminum strut-profile extrusion"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.boschrexroth.com/de/de/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 96_profile_60x60_300 returned material Aluminum with density 2700.0. Bosch Rexroth's official aluminum-profile system page identifies the relevant product family as aluminum profiles. official_alternate_route_check: the original BOM URL is a Bosch Rexroth Store strut-profile category URL; the used boschrexroth.com aluminum-profile-kit page is an official Bosch Rexroth product-family route and matches the row manufacturer and strut-profile family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP material metadata applies to the single per-row profile body."
  uncertainty_notes:
    - "The row evidence resolves aluminum as the material family but does not prove a specific alloy temper or anodized finish for this cut piece."
how_to_make:
  summary: "Prepare as a Bosch Rexroth modular aluminum strut-profile cut piece; extrude a 60 x 60 mm slotted aluminum profile, apply any required surface finish, cut to the row length, deburr, and inspect slot geometry and end squareness"
  manufacturing_steps:
    - "Produce"
    - "Cut the extrusion stock to the required row length, noting that the supplied CAD measures 240 mm while the file name implies 300 mm."
    - "Deburr the cut ends and slots."
    - "Apply or preserve the required surface finish, such as anodizing if specified by the selected Rexroth profile variant."
    - "Inspect overall length, 60 x 60 mm cross-section, slot geometry, and end squareness before frame assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/96_profile_60x60_300.step; research/ream250_bom/ream250_bom_row_0299_96__views_2x2.png; https://www.boschrexroth.com/de/de/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "The CAD preview shows a constant-section slotted extrusion profile; FreeCAD measured a 60 x 60 mm cross-section and 240 mm bounding-box length. Bosch Rexroth identifies this product family as aluminum profiles for modular structures. targeted_web_search: tried 'Bosch Rexroth Strebenprofil 60x60 material aluminum weight kg m', 'Bosch Rexroth strut profile 60x60 aluminum profile', and 'site:boschrexroth.com Strebenprofil 60x60 Bosch Rexroth aluminum strut profile'; results resolved the official aluminum-profile product family and similar product specs, but no row-specific Bosch page stated the manufacturing process for this exact cut piece."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Extrusion, finishing, cut-to-length, deburring, and inspection are the plausible Manufacturing route for a constant-section aluminum strut profile."
  uncertainty_notes:
    - "The evidence does not state Bosch Rexroth's actual production process, exact alloy temper, finish, tolerances, or whether the row's installed part has post-cut machining."
    - "The length mismatch between file name and measured CAD geometry remains unresolved."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable cut length of generic 60 x 60 aluminum extrusion/strut profile rather than as a reAM250-specific purchased module."
---

Research result for the leased reAM250 BOM row.
