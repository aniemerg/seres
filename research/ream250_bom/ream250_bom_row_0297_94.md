---
row_identity:
  item: "94"
  cad_file: "94_profile_60x60_350"
  source_row_number: 297
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "A 350 mm cut length of Bosch Rexroth 60 x 60 aluminum T-slot strut profile used as a structural frame member or support rail in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/94_profile_60x60_350.step; research/ream250_bom/ream250_bom_row_0297_94__views_2x2.png; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 297 names item 94 as quantity 1 of '94_profile_60x60_350', description 'strut profile', manufacturer Bosch Rexroth AG. FreeCAD measured one solid with bounding box 350.00 x 60.00 x 60.00 mm, and the contact sheet shows a long slotted extrusion cross-section. Bosch Rexroth describes its aluminum profile system as modular structural framing for frames, enclosures, workstations, safety fences, and similar industrial structures. official_alternate_route_check: the BOM Link URL is the Bosch Rexroth store category for Strebenprofil; the Bosch Rexroth aluminum profile kit page is a first-party Bosch Rexroth alternate route for the same manufacturer and product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical cut profile for this BOM row."
  uncertainty_notes:
    - "The row does not identify the exact frame location or connector interfaces in the larger reAM250 assembly."
mass:
  value_kg: 1.366
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 506015.224 mm^3, equal to 0.000506015224 m^3. Assembly STEP material extraction reports Aluminum with density 2700 kg/m^3 for product 94_profile_60x60_350, giving 0.000506015224 m^3 * 2700 kg/m^3 = 1.366 kg. This corresponds to about 3.90 kg/m for the 350 mm cut length."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/94_profile_60x60_350.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 506015.224 mm^3 and bounding box 350.00 x 60.00 x 60.00 mm. Local assembly STEP material extraction for product 94_profile_60x60_350 returned material Aluminum and density 2700.0. kb/materials/properties.yaml also lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is used as the net volume of one physical profile, including the hollow and slotted cross-section already present in the STEP geometry."
  uncertainty_notes:
    - "Mass accuracy depends on the CAD export preserving the true extrusion cross-section; no separate catalog cut-length mass was found in the BOM row."
material:
  primary_material: "aluminum strut-profile extrusion; Bosch Rexroth technical data for Rexroth strut profiles generally specifies EN AW Al MgSi / EN AW 6060 (AW-6063-T66)"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "Assembly STEP material extraction for product 94_profile_60x60_350 returned material Aluminum. The Bosch Rexroth Aluminum Framing 8.0 technical data PDF states technical data for Rexroth strut profiles with EN AW - Al MgSi material designation and EN AW - 6060 / AW-6063-T66 material number wording. bom_url_route_check: the BOM-provided Bosch Rexroth store category URL identifies the row as a Bosch Rexroth strut-profile family route but did not expose row-specific alloy text in the local browser result, so the Bosch Rexroth technical-data publication was used for the grade-family detail."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's Bosch Rexroth 60 x 60 strut profile follows the general Rexroth strut-profile material data rather than a special nonstandard alloy."
  uncertainty_notes:
    - "The local row metadata resolves aluminum, but the exact Bosch material number for this 350 mm cut length is not present in the BOM row."
how_to_make:
  summary: "Procure as Bosch Rexroth modular aluminum profile cut to 350 mm, or locally manufacture by aluminum extrusion followed by cut-to-length finishing."
  manufacturing_steps:
    - "Extrude aluminum alloy billet through a 60 x 60 T-slot profile die."
    - "Straighten, age/temper, and apply the profile surface finish or anodized finish appropriate for the Rexroth profile family."
    - "Cut the extrusion to a 350 mm length."
    - "Deburr the cut ends and inspect length, squareness, slot geometry, and visible surface condition."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/94_profile_60x60_350.step; research/ream250_bom/ream250_bom_row_0297_94__views_2x2.png; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "CAD and rendered preview show a uniform 350 mm long slotted profile. Bosch Rexroth identifies this product family as modular aluminum profiles with catalog dimensional drawings, and the technical-data PDF gives Rexroth strut-profile material and anodizing/tolerance context. targeted_web_search: tried 'Bosch Rexroth strut profile 60x60 aluminum extrusion manufacturing anodized', 'Bosch Rexroth Strebenprofil 60x60 EN AW 6060', and 'Bosch Rexroth aluminum framing strut profile technical data anodizing'; results supported the profile-family identity and technical data but did not state a row-specific factory manufacturing route for item 94."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A constant cross-section 60 x 60 T-slot member is most plausibly produced by extrusion and then cut to length."
    - "Procurement is the near-term route because this is a standard Bosch Rexroth framing component."
  uncertainty_notes:
    - "The result does not resolve end machining, tapped holes, or special cut-face treatment; the rendered CAD preview shows no obvious extra end features beyond the cut profile."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable aluminum extrusion/profile cut-to-length part, not as a machine-specific purchased module."
---

Result generated for the leased reAM250 BOM row only.
