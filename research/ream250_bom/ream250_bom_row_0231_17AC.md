---
row_identity:
  item: "17AC"
  cad_file: "17AC_strut_profile_20X20_296"
  source_row_number: 231
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Cut length of Bosch Rexroth 20 x 20 mm modular aluminum strut profile used as a light structural rail or frame member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AC_strut_profile_20X20_296.step; research/ream250_bom/ream250_bom_row_0231_17AC__views_2x2.png"
    cited_fact_or_basis: "BOM row 231 identifies item 17AC as quantity 1, CAD file 17AC_strut_profile_20X20_296, description strut profile, manufacturer Bosch Rexroth AG. Manifest row 231 maps the same item to the matched STEP part. FreeCAD measured one solid with bounding box 288.00 x 20.00 x 20.00 mm, and the rendered contact sheet shows a long square slotted extrusion."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row item is interpreted as a cut-to-length member of the Bosch Rexroth 20x20 strut-profile family rather than a separate custom machined block."
  uncertainty_notes:
    - "The filename suffix suggests 296 mm while the STEP bounding box measures 288.00 mm; the structural profile function is unaffected, but downstream length modeling should prefer the measured CAD length unless the source BOM length is later clarified."
mass:
  value_kg: 0.1152
  basis: "Per-unit mass for quantity 1. Bosch Rexroth/authorized distributor data gives the 20 x 20 mm strut profile mass as 0.4 kg per meter. The supplied row CAD length is 288.00 mm, so 0.28800 m * 0.4 kg/m = 0.1152 kg per unit. BOM quantity is 1, so row total is also about 0.1152 kg. CAD-volume cross-check: FreeCAD volume 47698.288 mm^3 equals 0.000047698288 m^3; using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives about 0.1288 kg."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AC_strut_profile_20X20_296.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "The Bosch Rexroth strut profile 20x20 data sheet lists mass m as 0.4 kg for the 20x20 profile family and ordering length range 50-3000 mm. The authorized-distributor page for Bosch Rexroth 3842 992 888 states weight per metre 0.4 kg, 20 x 20 mm size, 6 mm slot, and aluminum anodized material. FreeCAD measured one solid, volume 47698.288 mm^3, area 52463.900 mm^2, and bounding box 288.00 x 20.00 x 20.00 mm. The local density table lists aluminum density 2700 kg/m^3. bom_url_route_check: the BOM-provided Bosch Rexroth store category URL was checked; its accessible page state did not expose row-specific mass/material data in a directly parseable route, so Bosch Rexroth data-sheet and authorized-distributor routes matching the same 20x20 strut-profile family were used."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The 0.4 kg/m catalog mass applies to this Bosch Rexroth 20x20 slot-6 profile cut length."
    - "The measured 288.00 mm STEP length is used for per-unit mass instead of the filename suffix."
  uncertainty_notes:
    - "If later evidence confirms the intended cut length is 296 mm, the same 0.4 kg/m catalog value would give about 0.1184 kg instead of 0.1152 kg."
material:
  primary_material: "anodized aluminum strut profile; Bosch Rexroth technical data identifies the 20x20 profile material as anodized aluminum, and broader Rexroth strut-profile technical data maps the family to EN AW aluminum-magnesium-silicon profile alloys."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Bosch Rexroth 20x20 strut profile sheet lists material as anodized aluminum for part family 3842992888. The authorized-distributor page states material aluminum with anodized finish for the 20 x 20 mm Bosch Rexroth profile. Bosch Rexroth technical data for strut profiles lists EN AW-Al MgSi / EN AW-6060 / AW-6063-T66 family material designations. Local assembly STEP material extraction for 17AC_strut_profile_20X20_296 returned only Generic material and density 1000.0, which is placeholder metadata and does not resolve material. bom_url_route_check: the BOM-provided Bosch store route was checked but did not expose parseable row-specific material, so Bosch Rexroth data-sheet and distributor routes matching the same 20x20 strut-profile family were used."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's Bosch Rexroth manufacturer field, 20x20 slotted CAD geometry, and BOM strut-profile description map to the standard anodized aluminum Bosch Rexroth 20x20 strut-profile family."
  uncertainty_notes:
    - "The exact procurement alloy grade for this cut piece is not locked by row-specific STEP metadata; catalog evidence supports the anodized aluminum 6xxx-family profile material."
how_to_make:
  summary: "Procure as Bosch Rexroth 20x20 slot-6 anodized aluminum strut profile cut to the row length; a plausible local route is aluminum-alloy extrusion through a matching 20x20 slotted die, straightening/aging as required, anodizing, saw-cutting to length, and deburring."
  manufacturing_steps:
    - "Procure/catalog route: order Bosch Rexroth 20x20, slot-6 anodized aluminum strut profile and cut to the required machine length."
    - "Local route: extrude compatible 6xxx-series aluminum billet through a 20 x 20 mm slot-6 profile die."
    - "Straighten and finish the extrusion, then anodize or apply an equivalent protective surface finish."
    - "Saw-cut to the row length, deburr the ends, and add any end drilling/tapping only if required by the assembly."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0231_17AC__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AC_strut_profile_20X20_296.step; https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/"
    cited_fact_or_basis: "CAD preview/STEP show a constant-section 288.00 x 20.00 x 20.00 mm slotted extrusion. Bosch Rexroth data lists anodized aluminum 20x20 profiles and standard/customized profile finishes with ordering lengths in the 50-3000 mm range. The authorized-distributor page states the profile can be cut to required size and that cuts remove about 3 mm of available length. The detailed extrusion, anodizing, cutting, and deburring sequence is inferred from the standard aluminum-profile geometry and material, not directly specified as the supplier's row-specific production route. targeted_web_search: searched 'Bosch Rexroth strut profile 20x20 material mass kg m', 'Bosch Rexroth 3842992888 weight per metre anodized aluminum', and 'Bosch Rexroth 20x20 strut profile manufacturing extrusion anodized'; results resolved material, linear mass, profile finish, and cut-to-size procurement but did not provide a row-specific factory manufacturing process for item 17AC."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, procurement as cut profile stock is preferred unless future modeling needs to represent extrusion and anodizing as local processes."
    - "Any row-specific end features are not visible in the current CAD preview and are therefore not included as required operations."
  uncertainty_notes:
    - "The local manufacturing route is plausible for an aluminum T-slot profile but is not sourced as Bosch Rexroth's exact factory process for this row."
kb_implications:
  - "item_granularity: raw_material_or_stock - model as reusable Bosch/Rexroth-compatible 20x20 aluminum strut profile stock with length captured in BOM or recipe notes rather than as a unique reAM250-only assembly."
---
