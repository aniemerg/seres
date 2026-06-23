---
row_identity:
  item: "17A5"
  cad_file: "17A5_strut_profile_20X20_484"
  source_row_number: 224
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 20 x 20 mm modular aluminum strut profile, cut to about 484 mm length, used as a light structural rail/member in the reAM250 frame or support structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A5_strut_profile_20X20_484.step; research/ream250_bom/ream250_bom_row_0224_17A5__views_2x2.png"
    cited_fact_or_basis: "BOM row 224 names item 17A5 as quantity 1, cad_file 17A5_strut_profile_20X20_484, description strut profile, manufacturer Bosch Rexroth AG. Manifest row 224 maps the same item to the matched part STEP. FreeCAD measured one solid with bounding box 483.70 x 20.00 x 20.00 mm, and the preview shows a long slotted square extrusion."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row item is interpreted as a cut length of the Bosch Rexroth 20x20, slot-6 strut-profile family rather than a separate custom-machined bar."
  uncertainty_notes:
    - "The row does not identify the exact Bosch article number or end machining option, so the function is kept at the strut-profile family level."
mass:
  value_kg: 0.1935
  basis: "Bosch Rexroth/authorized distributor data gives the 20 x 20 mm strut profile mass as 0.4 kg per meter. The row CAD length is 483.70 mm, so 0.48370 m * 0.4 kg/m = 0.19348 kg per unit, rounded to 0.1935 kg. BOM quantity is 1, so row total is also about 0.1935 kg. CAD-volume cross-check: FreeCAD volume 80109.936 mm^3 equals 0.000080109936 m^3; using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives about 0.2163 kg, within about 12% of the catalog linear-mass estimate."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A5_strut_profile_20X20_484.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "The Bosch Rexroth strut profile 20x20 data sheet lists material anodized aluminum, groove 6, mass m 0.4 kg, and ordering length range 50-3000 mm for the 20x20 profile family. The authorized-distributor page for Bosch Rexroth 3842992888 states weight per metre 0.4 kg, material aluminum with anodized finish, 20 x 20 mm size, and 6 mm slot. FreeCAD measured one solid, volume 80109.936 mm^3, area 87888.768 mm^2, and bounding box 483.70 x 20.00 x 20.00 mm. The local density table lists aluminum density 2700 kg/m^3. bom_url_route_check: the BOM-provided Bosch Rexroth store category URL was checked; its rendered store page did not expose row-specific mass/material data in a directly parseable route, so Bosch Rexroth data-sheet and distributor routes matching the same 20x20 strut-profile family were used."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The catalog mass value is treated as kg/m for cut-length profiles, consistent with the distributor specification and the length-scaled nature of the CAD model."
    - "The CAD length 483.70 mm is used as the physical cut length for the BOM row."
  uncertainty_notes:
    - "The CAD-volume aluminum-density cross-check is slightly heavier than the catalog linear-mass estimate, likely due to CAD simplification, profile variant differences, or rounding; catalog linear mass is preferred for the final value."
material:
  primary_material: "anodized aluminum strut-profile extrusion"
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Bosch Rexroth strut profile 20x20 data sheet lists the profile material as anodized aluminum. The authorized-distributor page for Bosch Rexroth 3842992888 states material aluminum with anodized finish. The assembly STEP material extractor matched 17A5_strut_profile_20X20_484 but returned only Generic material and density 1000.0, which is placeholder metadata and does not resolve material. bom_url_route_check: the BOM-provided Bosch Rexroth store category URL was checked but did not expose parseable row-specific material data, so Bosch Rexroth data-sheet and distributor routes matching the same 20x20 strut-profile family were used."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's 20x20 slotted CAD geometry and Bosch Rexroth manufacturer field map to the standard anodized aluminum Bosch Rexroth 20x20 strut-profile family."
  uncertainty_notes:
    - "Exact aluminum alloy temper is not stated in the available row-matched sources; downstream modeling should use aluminum/anodized aluminum rather than a specific alloy grade."
how_to_make:
  summary: "Procure as Bosch Rexroth 20x20 modular aluminum profile cut to length; a plausible local manufacturing route is aluminum-alloy extrusion through a 20x20 slot-6 die, stretch/straighten, anodize, saw-cut to 483.7 mm, deburr, and optionally drill/tap any end features if the assembly requires them."
  manufacturing_steps:
    - "Procure/catalog route: order Bosch Rexroth 20x20, slot-6 anodized aluminum strut profile and cut it to the row length."
    - "Local route: extrude aluminum alloy through a die that forms the 20 x 20 mm slotted profile cross-section."
    - "Straighten, age or stress-relieve as appropriate for the alloy, and anodize the extrusion for the standard surface finish."
    - "Saw-cut the extrusion to about 483.7 mm, deburr cut edges, and add any required standard end finishing such as drilling or tapping."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0224_17A5__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A5_strut_profile_20X20_484.step; https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/"
    cited_fact_or_basis: "CAD preview/STEP show a long 483.70 x 20.00 x 20.00 mm slotted extrusion. Bosch Rexroth data lists standard and customized profile finishes for the 20x20 profile family and ordering lengths in the 50-3000 mm range. The distributor page states the profile can be cut to required size and that cuts remove about 3 mm of available length. The detailed extrusion, anodizing, and finishing sequence is inferred from the standard aluminum-profile geometry and material, not directly specified as the supplier's production route. targeted_web_search: searched 'Bosch Rexroth strut profile 20x20 material mass kg m', 'Bosch Rexroth 3842992888 weight per metre anodized aluminum', and 'Bosch Rexroth 20x20 strut profile manufacturing extrusion anodized'; results resolved material, linear mass, cut-to-length procurement, and profile finishes but no row-specific factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB modeling, procurement or generic aluminum-extrusion manufacturing is more appropriate than treating this as a bespoke machined part."
    - "Any end machining is optional because the row CAD name does not encode M6, D8, or other finish variants."
  uncertainty_notes:
    - "The exact article number and end-finish option are unresolved; if later rows or drawings show tapped/drilled ends, model that as a finishing operation on the same base profile rather than a new material."
kb_implications:
  - "item_granularity: simple_part - model as a reusable cut-to-length aluminum strut profile, with profile length/end-finish captured in BOM notes rather than creating a unique item for every similar extrusion length."
---

# reAM250 BOM Row 224 - 17A5

Research result for the leased reAM250 BOM row.
