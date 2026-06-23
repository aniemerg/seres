---
row_identity:
  item: "17A1"
  cad_file: "17A1_strut_profile_20X20_492"
  source_row_number: 220
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Cut-to-length 20 x 20 mm Bosch Rexroth aluminum strut profile used as a light modular framing member or rail in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A1_strut_profile_20X20_492.step; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 220 identifies item 17A1 as Bosch Rexroth AG 'strut profile'; the row STEP measures one 492.5 x 20.0 x 20.0 mm solid with a four-slot profile visible in the rendered right view; Bosch Rexroth describes its aluminum profile system as modular structural framing for building machine frames, workstations, guards, and similar structures. official_alternate_route_check: the BOM link is an official Bosch Rexroth store route for Strebenprofil; the cited Bosch Rexroth aluminum-profile page is the same manufacturer's official product-family route and matches the row's strut-profile family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single STEP solid represents one physical 17A1 profile, and the BOM quantity of 2 means two identical cut pieces."
  uncertainty_notes:
    - "The row does not state the exact mating frame location, so the function is assigned at profile-family level rather than to a specific bracket span."
mass:
  value_kg: 0.22
  basis: "Per unit: FreeCAD volume 81567.384 mm^3 = 0.000081567384 m^3; assembly STEP material metadata gives Aluminum 6061 with density 2700 kg/m^3; 0.000081567384 * 2700 = 0.220 kg. BOM quantity is 2, so the row total is about 0.440 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A1_strut_profile_20X20_492.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 81567.384146 mm^3, area 89481.710282 mm^2, and bounding box 492.5 x 20.0 x 20.0 mm; local assembly STEP material extraction matched product 17A1_strut_profile_20X20_492 to Aluminum 6061 with density 2700.0; the local material properties table lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume is treated as the physical aluminum volume for one cut profile."
    - "The aluminum density in the local material metadata is appropriate for mass estimation at BOM granularity."
  uncertainty_notes:
    - "Public catalog mass for related Bosch Rexroth 20x20 slot-6 profiles is commonly about 0.4 kg/m, which would give about 0.197 kg for 492.5 mm; the CAD-derived value is retained because it is row-specific but should be considered a close engineering-scale estimate."
material:
  primary_material: "Anodized aluminum strut-profile alloy; local CAD package tags the row as Aluminum 6061, while Bosch Rexroth technical data for its strut profiles identifies EN AW aluminum-magnesium-silicon profile alloys."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://docs.rs-online.com/ea04/A700000007302204.pdf; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "Local assembly STEP material extraction reports Aluminum 6061 for 17A1_strut_profile_20X20_492; the Bosch Rexroth 20x20 strut profile sheet lists material as anodized aluminum; Bosch Rexroth technical data describes Rexroth strut-profile material as EN AW aluminum-magnesium-silicon profile alloy. bom_url_route_check: the BOM-provided Bosch Rexroth store link identifies the official strut-profile family but did not expose the row's exact material grade in the accessible page text, so Bosch-authored catalog sheets hosted on distributor/catalog domains were used for material details."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "For KB planning, the important material family is aluminum extrusion stock with anodized surface; differences among common 6xxx profile alloys are not material to this row's coarse mass and manufacturing route."
  uncertainty_notes:
    - "The exact procurement grade is not fully locked because the local CAD tag says Aluminum 6061 while Bosch Rexroth catalog data for strut profiles points to EN AW 6060/6063-family material."
how_to_make:
  summary: "Procure as a Bosch Rexroth 20x20 slot-6 aluminum strut profile cut to about 492.5 mm, or locally reproduce by extruding a matching 20 mm T-slot aluminum profile, anodizing it, cutting to length, and deburring the ends."
  manufacturing_steps:
    - "Start from 6xxx-series aluminum billet or purchased Rexroth-compatible 20x20 profile stock."
    - "Extrude the 20 x 20 mm four-slot cross section through a profile die if making locally."
    - "Age/temper and anodize the profile to match the corrosion-resistant structural profile family."
    - "Cut one piece to about 492.5 mm and deburr or lightly finish the cut ends."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A1_strut_profile_20X20_492.step; https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.boschrexroth.com/en/us/company/press/bosch-rexroth-expands-its-wide-range-of-aluminum-profiles-to-include-an-inch-10-and-15-series-5312.html"
    cited_fact_or_basis: "The row STEP shows a constant 20 x 20 mm slotted profile 492.5 mm long; the Bosch Rexroth 20x20 sheet lists selectable/cut lengths from 50 to 3000 mm and anodized aluminum material; Bosch Rexroth describes its aluminum profile products as aluminum extrusion. targeted_web_search: searched 'Bosch Rexroth strut profile extruded anodized aluminum manufacturing' and 'Bosch Rexroth aluminum structural framing strut profiles anodized aluminum extrusion'; results supported aluminum extrusion/product-family identity but did not provide a row-specific manufacturing process sheet for this exact cut piece."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route follows standard practice for T-slot aluminum framing profiles because the cited sources identify the product as an aluminum extrusion but do not document the full factory process for this row."
  uncertainty_notes:
    - "End machining details such as tapped holes or special Quick & Easy finishes are not evident in the rendered preview or row text, so this route assumes a plain cut profile."
kb_implications:
  - "item_granularity: raw_material_or_stock - model as reusable Bosch/Rexroth-compatible 20x20 aluminum strut profile stock with length captured in BOM or recipe notes, not as a unique reAM250-only assembly."
---

