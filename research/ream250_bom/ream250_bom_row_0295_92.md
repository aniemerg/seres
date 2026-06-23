---
row_identity:
  item: "92"
  cad_file: "92_profile_60x60_2120"
  source_row_number: 295
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Structural aluminum strut profile used as a long 60 x 60 mm frame member in the reAM250 machine structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/92_profile_60x60_2120.step; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 295 names item 92 as 'strut profile' from Bosch Rexroth AG; FreeCAD measured one solid with bounding box 2120.00 x 60.00 x 60.00 mm; CAD preview shows a long straight square profile; Bosch Rexroth describes its aluminum profile system for machine frames, workstations, enclosures, shelves, and safety fences."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single exported STEP body represents one physical profile cut to the row length."
  uncertainty_notes: []
mass:
  value_kg: 8.276
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 3065006.499 mm^3 = 0.003065006499 m^3. Assembly STEP material metadata gives Aluminum with density 2700 kg/m^3, matching kb/materials/properties.yaml aluminum density. Calculation: 0.003065006499 m^3 * 2700 kg/m^3 = 8.2755 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/92_profile_60x60_2120.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured STEP volume 3065006.499 mm^3 and bounding box 2120.00 x 60.00 x 60.00 mm; local STEP material extractor matched product 92_profile_60x60_2120 to material Aluminum with density 2700.0; local material table lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is the net aluminum volume of the profile, including hollow/slot geometry."
  uncertainty_notes:
    - "Mass depends on CAD export fidelity for the internal profile cross-section; if the supplier profile variant differs from the STEP, use the supplier kg/m value instead."
material:
  primary_material: "Aluminum strut-profile alloy family; Rexroth technical data for strut profiles lists EN AW-6060 / AW-6063-T66 family."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "Local STEP material metadata for 92_profile_60x60_2120 states Aluminum and density 2700.0. Bosch Rexroth technical data for strut profiles lists EN AW-AlMgSi, AW-6063-T66, and material designation EN AW-6060 / AW-6063-T66 for Rexroth strut profiles. bom_url_route_check: BOM Link URL is the Bosch Rexroth strut-profile shop route; the accessible Bosch Rexroth framing page confirmed the same product family but did not expose the alloy table, so the Bosch Rexroth technical-data PDF mirrored on Airline Hydraulics was used for the alloy-family table."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's Bosch Rexroth strut profile uses the standard Rexroth strut-profile alloy family rather than a special nonstandard alloy."
  uncertainty_notes:
    - "The BOM row and local STEP metadata do not state the exact Rexroth material number or surface treatment for this cut length."
how_to_make:
  summary: "Procure a Bosch Rexroth aluminum strut profile or locally reproduce it by extruding the matching 60 x 60 mm profile from aluminum alloy, anodizing if required, cutting to 2120 mm, and deburring the cut ends."
  manufacturing_steps:
    - "Source or cast suitable aluminum extrusion billet."
    - "Extrude through a die matching the Bosch Rexroth 60 x 60 mm T-slot/profile cross-section."
    - "Straighten, age/heat treat to the target 6060/6063-T66 family properties, and anodize if the machine requires the commercial finish."
    - "Cut the profile to the CAD/BOM length of 2120 mm and deburr or machine the ends for assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/92_profile_60x60_2120.step; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "BOM/CAD identify a 2120 mm long Bosch Rexroth strut profile; Bosch Rexroth describes the profile system as modular aluminum framing with catalog material numbers and dimensional drawings; Rexroth technical data states the profile alloy family and anodizing process data. targeted_web_search: searched 'Bosch Rexroth strut profile 60x60 material manufacturing extrusion anodized' and 'Bosch Rexroth 60x60 strut profile weight kg/m 8mm slot'; results supported aluminum strut-profile use and material data but did not provide a row-specific manufacturing route for this exact cut length."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Local manufacture would use standard aluminum profile extrusion practice because the part is a constant cross-section profile."
    - "Commercial procurement remains the near-term route unless the KB later models extrusion dies and finishing capacity."
  uncertainty_notes:
    - "The exact Rexroth cross-section variant and any end-machining operations are not specified in the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length aluminum strut profile rather than a machine-specific assembly."
---
