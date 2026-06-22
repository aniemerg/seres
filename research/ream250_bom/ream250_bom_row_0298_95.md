---
row_identity:
  item: "95"
  cad_file: "95_profile_60x60_740"
  source_row_number: 298
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 60 x 60 mm aluminum strut profile, cut to 740 mm length, used as a modular machine-frame structural rail or support member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/95_profile_60x60_740.step; research/ream250_bom/ream250_bom_row_0298_95__views_2x2.png"
    cited_fact_or_basis: "BOM row 298 states item 95, quantity 2, CAD file 95_profile_60x60_740, description strut profile, and manufacturer Bosch Rexroth AG. The manifest maps row 298 to gold_export/parts/95_profile_60x60_740.step as a matched_existing vendor_component. FreeCAD measured one solid with bounding box 740.00 x 60.00 x 60.00 mm. The rendered contact sheet shows a long slotted square profile with a 60 x 60 mm end section."
    evidence_basis: "bom_provided"
  assumptions:
    - "The strut profile is interpreted as part of the modular structural frame because Bosch Rexroth strut profiles are frame members and the CAD is a long 60 x 60 mm rail."
  uncertainty_notes:
    - "The exact mating connectors and load path in the parent assembly are not identified by this row alone."
mass:
  value_kg: 2.889
  basis: "Per-unit mass for one 740 mm profile. FreeCAD volume 1069860.759 mm^3 equals 0.001069861 m^3; using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 2.889 kg. BOM quantity is 2, so the row total is about 5.78 kg. This agrees with the catalog-style check of 3.9 kg/m for a 60 x 60 profile over 0.740 m, which gives 2.886 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/95_profile_60x60_740.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1069860.759 mm^3, area 670057.019 mm^2, and bounding box 740.00 x 60.00 x 60.00 mm. The local assembly STEP material extractor matched 95_profile_60x60_740 with material Aluminum and density 2700.0. The local density table lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one supplied profile."
    - "The local STEP material density is treated as kg/m^3-like, consistent with the extraction script note and the local aluminum density table."
  uncertainty_notes:
    - "Mass excludes separate connector hardware or end caps; this row represents the profile itself."
material:
  primary_material: "aluminum"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched 95_profile_60x60_740 and returned material Aluminum with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 740 mm CAD length is a cut length of the Bosch Rexroth 60 x 60 strut-profile family rather than a separate material variant."
  uncertainty_notes:
    - "The specific aluminum alloy grade and surface finish are not stated in the BOM or local STEP metadata; a row-matched Bosch Rexroth 60 x 60 profile listing describes anodized aluminum, but the local row evidence only resolves aluminum."
how_to_make:
  summary: "Procure Bosch Rexroth-compatible 60 x 60 anodized aluminum strut profile stock and cut to 740 mm length; local reproduction would require aluminum extrusion of the profile cross-section followed by sawing, deburring, and anodizing."
  manufacturing_steps:
    - "Preferred route: buy Bosch Rexroth 60 x 60 strut profile or compatible profile stock from the modular framing system."
    - "Cut the profile to 740 mm length for this row, preserving square ends and the slot geometry."
    - "Deburr cut edges and clean the profile before assembly."
    - "For local manufacturing, extrude aluminum through a die matching the 60 x 60 slotted cross-section, stretch/straighten as required, age or heat treat if the alloy requires it, cut to length, and anodize or otherwise finish the surface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/95_profile_60x60_740.step; research/ream250_bom/ream250_bom_row_0298_95__views_2x2.png; https://esd.equipment/en/bosch-rexroth-3842990350.html"
    cited_fact_or_basis: "BOM row 298 names Bosch Rexroth AG and strut profile. CAD and preview show a 740.00 x 60.00 x 60.00 mm slotted profile. The row-matched Bosch Rexroth 60 x 60 profile listing describes a variable-length cut-to-order anodized aluminum strut profile with 4 open slots and length range 50-6070 mm. bom_url_route_check: the BOM-provided Bosch Rexroth category route was checked first but did not resolve a specific 60 x 60 technical line in accessible text, so the independent row-matched listing was used for the cut-to-length procurement detail. targeted_web_search: searched \"Bosch Rexroth strut profile 60x60 aluminum profile 60x60\", \"95_profile_60x60_740 Bosch Rexroth\", and the BOM-provided Bosch Rexroth strut-profile URL; found row-family procurement and product-family facts, but no exact row-specific manufacturing process sheet for the 740 mm profile."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cut-to-length procurement is the normal route because the BOM row is a vendor_component from Bosch Rexroth AG."
    - "Extrusion plus cut/deburr/anodize is the plausible local manufacturing route inferred from the constant slotted aluminum profile geometry and common production of aluminum structural framing."
  uncertainty_notes:
    - "The cited sources do not state the extrusion die, alloy temper, heat treatment, or surface-finish process parameters for this exact row; those would be separate manufacturing-detail research."
kb_implications:
  - "item_granularity: purchased_module - model as a reusable Bosch Rexroth 60 x 60 aluminum strut-profile stock/cut-length family rather than creating a unique item for every nearby length."
---

Research result for reAM250 BOM row 298.
