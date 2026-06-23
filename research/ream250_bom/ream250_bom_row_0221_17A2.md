---
row_identity:
  item: "17A2"
  cad_file: "17A2_strut_profile_20X20_629"
  source_row_number: 221
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 20 x 20 mm aluminum strut profile used as a modular machine-frame member, rail, spacer, or support in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A2_strut_profile_20X20_629.step; research/ream250_bom/ream250_bom_row_0221_17A2__views_2x2.png; https://www.boschrexroth.com/de/de/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "BOM row 221 states item 17A2, quantity 3, description strut profile, manufacturer Bosch Rexroth AG, and CAD file 17A2_strut_profile_20X20_629. The manifest maps the row to gold_export/parts/17A2_strut_profile_20X20_629.step as a matched vendor_component export. FreeCAD measured one solid with bounding box 629.40 x 20.00 x 20.00 mm. The rendered contact sheet and end view show a long 20 mm square slotted extrusion profile. Bosch Rexroth describes its aluminum profile system as enabling machine frames, workplaces, shelves, and protective fences."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one cut-to-length 20 x 20 mm profile piece, with BOM quantity 3 meaning three identical or equivalent physical struts."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the generic frame-member role but not the exact mating connectors or the specific frame segment supported by this row."
mass:
  value_kg: 0.281
  basis: "Per physical strut profile. FreeCAD volume 104240.633 mm^3 equals 0.000104241 m^3. Using the row-specific assembly STEP material density 2700 kg/m^3 gives 0.28145 kg, rounded to 0.281 kg per 629.4 mm strut. BOM quantity is 3, so the row total is about 0.844 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A2_strut_profile_20X20_629.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 104240.633 mm^3, area 114262.826 mm^2, and bounding box 629.40 x 20.00 x 20.00 mm. The local assembly STEP material extractor matched 17A2_strut_profile_20X20_629 and returned material Aluminum 6061 with density 2700.0. The local density table lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one cut strut."
    - "The assembly STEP density is treated as kg/m^3-like metadata, consistent with the task extractor note and local aluminum density table."
  uncertainty_notes:
    - "The mass is CAD-volume-derived rather than a catalog-weighed value, so it depends on the STEP profile including the same internal voids and slot geometry as the installed part."
material:
  primary_material: "aluminum alloy extrusion; row STEP metadata says Aluminum 6061, while Bosch Rexroth profile-family data generally uses aluminum profile alloys such as EN AW-6060/AW-6063-T66"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "The local assembly STEP material extractor matched the row CAD product name and returned material Aluminum 6061 with density 2700.0. The BOM-provided Bosch Rexroth route identifies the row as a Rexroth strut profile product family. A Bosch Rexroth technical-data catalog copy states Rexroth strut profiles use EN AW-Al MgSi / EN AW-6060 with AW-6063-T66 mechanical condition. official_alternate_route_check: the original BOM URL is a Bosch Rexroth store strut-profile route; the Bosch Rexroth aluminum-profile page and linked/catalog technical-data route are first-party or Bosch catalog-family evidence for the same Rexroth aluminum profile family, while the local STEP metadata is row-specific."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB planning, the exact alloy should be treated as an aluminum extrusion alloy unless a later drawing resolves whether the installed piece should follow the STEP's Aluminum 6061 tag or the Bosch profile-family EN AW-6060/AW-6063-T66 convention."
  uncertainty_notes:
    - "The row-specific STEP material and Bosch profile-family material convention do not name the same exact alloy grade, so downstream modeling should preserve the material as aluminum extrusion alloy rather than over-constraining the grade."
how_to_make:
  summary: "Best current route is procurement as a Bosch Rexroth 20 x 20 mm strut profile or equivalent aluminum T-slot extrusion, cut to the 629.4 mm CAD length; a local route would extrude the aluminum profile, age/anodize as required, saw to length, deburr, and inspect slot/profile dimensions."
  manufacturing_steps:
    - "Procure Bosch Rexroth 20 x 20 mm strut profile stock or an equivalent 20 mm modular aluminum profile with matching slot geometry."
    - "Cut the profile to the CAD length of 629.4 mm for each of the three row instances."
    - "Deburr cut ends and clean slot edges so standard profile connectors or fasteners can seat correctly."
    - "For local manufacture, produce the cross-section by aluminum extrusion from the resolved profile alloy, apply required aging/anodizing or surface finish, then cut to length."
    - "Inspect overall length, 20 x 20 mm envelope, straightness, slot geometry, and fit with mating Bosch/Rexroth-compatible connectors."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A2_strut_profile_20X20_629.step; research/ream250_bom/ream250_bom_row_0221_17A2__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE; https://www.boschrexroth.com/de/de/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "BOM row 221 gives manufacturer Bosch Rexroth AG and a Bosch Rexroth strut-profile URL. CAD and preview show one long 629.40 x 20.00 x 20.00 mm slotted profile. Bosch Rexroth's aluminum-profile page describes standardized aluminum profile components for machine frames and related structures. targeted_web_search: searched 'Bosch Rexroth strut profile 20x20 material aluminum', 'site:boschrexroth.com strut profile 20x20 Bosch Rexroth material aluminum 6061', and 'Bosch Rexroth Aluminum Framing technical data strut profiles EN AW 6060'; results found profile-family and material technical data but no row-specific manufacturing-process sheet for this cut 629.4 mm part."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cutting/deburring and the local extrusion route are inferred from the CAD length, profile geometry, and common production route for aluminum structural profiles."
    - "Procurement as standard profile stock is acceptable for current modeling because the BOM row names Bosch Rexroth AG and links to the Bosch strut-profile product family."
  uncertainty_notes:
    - "The sources do not specify the actual supplier's production line, saw tolerance, end finishing, surface treatment for this exact cut length, or whether any end tapping or connector preparation is added elsewhere."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut length of standard aluminum T-slot/strut profile, parameterized by 20 x 20 mm section and length rather than as a machine-specific custom assembly."
---

Research result for reAM250 BOM row 221.
