---
row_identity:
  item: "9B"
  cad_file: "9B_profile_60x60_960"
  source_row_number: 213
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 60 x 60 mm aluminum strut profile cut to 960 mm, used as a modular machine-frame member in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.boschrexroth.com/de/at/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "The BOM row and manifest identify item 9B as quantity 1, cad_file 9B_profile_60x60_960, description strut profile, manufacturer Bosch Rexroth AG. The Bosch Rexroth aluminum-profile page says system profiles are used to realize machine frames, ergonomic workplaces, shelves, or protective fences, and highlights standardized components, connection technology, and high-force-absorbing profiles."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename suffix 60x60_960 is interpreted as a 60 mm square profile cut to a 960 mm length, consistent with the CAD bounding box."
  uncertainty_notes: []
mass:
  value_kg: 3.747
  basis: "FreeCAD measured CAD volume 1387927.471 mm^3 for one 960 mm profile. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 3.7474 kg per strut. As a cross-check, the Bosch Rexroth catalog lists the 60x60 strut profile mass as 3.9 kg/m, giving 3.744 kg for 0.960 m."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9B_profile_60x60_960.step; kb/materials/properties.yaml; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec2_Profiles.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1387927.471 mm^3, area 868403.520 mm^2, and bounding box 960.00 x 60.00 x 60.00 mm. The local material density table lists aluminum density 2700 kg/m^3. The Bosch Rexroth Aluminum Framing 8.0 catalog table lists 60x60 profile area 14.4 cm2 and mass 3.9 kg/m. bom_url_route_check: the BOM-provided Bosch Rexroth store URL was checked first; it identifies the strut-profile product family but did not expose row-specific 60x60 mass in the accessible page, so the Bosch Rexroth catalog PDF mirror was used for catalog mass cross-check."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is treated as the physical metal volume for one cut profile."
    - "The local aluminum density is used as the calculation constant for the aluminum extrusion."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic/Generisch at density 1000.0, so the mass relies on CAD volume plus catalog aluminum-profile identity rather than local STEP material metadata."
material:
  primary_material: "anodized aluminum strut-profile alloy family; Rexroth technical data lists EN AW AlMgSi / EN AW-6060 with AW-6063-T66 designation for strut profiles"
  source:
    url_or_path: "https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf; https://www.boschrexroth.com/de/at/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "Bosch Rexroth technical data for strut profiles lists EN AW-AlMgSi, EN AW-6060, and AW-6063-T66 designations, and an anodizing layer/process entry. The Bosch Rexroth aluminum-profile page identifies the product family as aluminum profiles. official_alternate_route_check: the original BOM URL is the Bosch Rexroth store strut-profile family route; the alternate Bosch Rexroth product-family page and Bosch Rexroth catalog technical-data page match the same manufacturer and strut-profile product family, while the catalog mirror preserves Bosch Rexroth document title and content for the material-grade details."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's Bosch Rexroth strut profile follows the Rexroth strut-profile material family stated in the technical-data catalog."
  uncertainty_notes:
    - "The leased row does not include a Bosch material number, so the exact machining option or finish variant is not locked beyond the 60x60 aluminum strut-profile family."
how_to_make:
  summary: "Manufacture as a standard aluminum T-slot/strut extrusion: cast; for near-term KB modeling, treat it as reusable aluminum structural-profile stock cut to length"
  manufacturing_steps:
    - "Prepare aluminum alloy billet compatible with EN AW-6060/AW-6063-series profile extrusion."
    - "Hot-extrude through a 60x60 strut-profile die to form the slotted hollow cross-section visible in the CAD preview."
    - "Quench, stretch/straighten, and age to the required temper for structural profile service."
    - "Anodize the profile surface, then saw cut to the 960 mm BOM length and deburr the ends."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0213_9B__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9B_profile_60x60_960.step; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "The rendered contact sheet shows a long constant-section slotted structural profile. FreeCAD measured a 960.00 x 60.00 x 60.00 mm bounding box. Bosch Rexroth technical data identifies the material family and anodizing information for strut profiles. targeted_web_search: searched \"Bosch Rexroth strut profile 60x60 aluminum material mass kg/m\", \"site:boschrexroth.com strut profile 60x60 960 aluminum Bosch Rexroth\", and \"Bosch Rexroth Strebenprofil 60x60 material gewicht kg/m\" found row-family catalog material and mass data but no source stating the actual factory process for this specific cut row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A constant 60x60 slotted aluminum profile is produced by extrusion rather than subtractive machining from solid stock."
    - "Cut-to-length and deburring are sufficient post-processing for the BOM row unless later assembly evidence requires drilled or tapped end features."
  uncertainty_notes:
    - "The cited Bosch evidence resolves the profile family, material, and anodizing context, but not the complete vendor production routing for this exact 960 mm cut part."
kb_implications:
  - "item_granularity: simple_part - model as an aluminum structural profile cut to length, preferably reusing a generic 60x60 aluminum extrusion/strut profile item rather than creating a machine-specific frame member."
---

# reAM250 BOM Row 213 - 9B

Research result for the leased reAM250 BOM row.
