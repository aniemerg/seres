---
row_identity:
  item: "17A8"
  cad_file: "17A8_strut_profile_20X20_D70"
  source_row_number: 227
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short Bosch Rexroth 20 x 20 mm strut/profile extrusion segment used as a light structural spacer, rail, bracket member, or frame element in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A8_strut_profile_20X20_D70.step; research/ream250_bom/ream250_bom_row_0227_17A8__views_2x2.png"
    cited_fact_or_basis: "BOM row 227 names item 17A8 as 'strut profile' from Bosch Rexroth AG; the STEP geometry is one solid with 70.40 x 20.00 x 20.00 mm bounding box; the rendered preview shows a short slotted extrusion profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "In this BOM context, the short strut profile functions as a structural mounting/profile element rather than as raw stock inventory."
  uncertainty_notes:
    - "The row has no parent assembly note, so exact mating components and load path are inferred from the BOM name and local CAD shape."
mass:
  value_kg: 0.0315
  basis: "Per-unit mass for quantity 1. FreeCAD measured volume is 11659.581 mm^3, equal to 1.1659581e-5 m^3. Assembly STEP material metadata gives Aluminum 6061 with density 2700 kg/m^3, so mass = 1.1659581e-5 m^3 * 2700 kg/m^3 = 0.03148 kg. As a sanity check, an independent Bosch Rexroth 20x20 profile listing gives 0.4 kg/m; at the CAD length of 70.4 mm this would be about 0.0282 kg, close enough for profile/cut/model variation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A8_strut_profile_20X20_D70.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measurement: 1 solid, volume 11659.581408903745 mm^3, area 13074.777683936163 mm^2, bounding box 70.4 x 20.0 x 20.0 mm. Local STEP material extractor matched product 17A8_strut_profile_20X20_D70 to material Aluminum 6061 and density 2700.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "STEP density is treated as kg/m^3, consistent with the extractor note for this reAM250 export."
    - "Anodized surface mass is negligible relative to the aluminum extrusion mass at this scale."
  uncertainty_notes:
    - "Mass depends on the exported CAD solid being the actual row cut length, not a library nominal profile segment."
material:
  primary_material: "Aluminum 6061 profile; anodized aluminum finish indicated by same-family Bosch Rexroth 20x20 strut profile listing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://esd.equipment/de/bosch-rexroth-3842992888.html"
    cited_fact_or_basis: "Local assembly STEP material extraction gives row-specific material 'Aluminum 6061' with density 2700.0. Independent product listing for Bosch Rexroth 3842992888 describes a 20x20 strut profile as anodized aluminum."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The independent 20x20 Bosch Rexroth strut profile listing is used only to qualify the finish as anodized; the base alloy comes from local row-specific STEP metadata."
  uncertainty_notes:
    - "bom_url_route_check: The BOM-provided Bosch Rexroth store URL returned a Salesforce Commerce Cloud file-not-found page and did not expose row-specific material or finish data; the independent ESD listing was used as a same-manufacturer, same-profile-family cross-check for anodized aluminum finish."
how_to_make:
  summary: "Extrude Bosch/Rexroth-compatible 20 x 20 mm aluminum T-slot/strut profile, anodize if required, saw cut to about 70.4 mm, deburr, and install with compatible connectors or fasteners"
  manufacturing_steps:
    - "Extrude 6061 or compatible aluminum alloy through a 20 x 20 mm slotted profile die."
    - "Anodize or otherwise finish the profile for corrosion and wear resistance."
    - "Cut stock to the CAD row length of about 70.4 mm, accounting for saw kerf and tolerance."
    - "Deburr cut edges and use the four open slots for attachment to mating brackets, connectors, or fasteners."
  source:
    url_or_path: "https://esd.equipment/de/bosch-rexroth-3842992888.html; research/ream250_bom/ream250_bom_row_0227_17A8__views_2x2.png"
    cited_fact_or_basis: "Independent listing describes Bosch Rexroth 20x20 strut profile as anodized aluminum, 4 open 6 mm slots, variable cut length 50-3000 mm, profile area 1.6 cm^2, mass 0.4 kg/m. CAD preview shows a cut short slotted extrusion."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Follow ordinary aluminum extrusion plus cut/deburr steps for the Rexroth-style cut-to-length profile"
  uncertainty_notes:
    - "Bom_url_route_check: The original BOM Link URL was checked directly and returned a file-not-found page, so it did not resolve manufacturing or cut-length details; the independent same-manufacturer product listing was used for route details."
kb_implications:
  - "item_granularity: simple_part - Model as a cut length of reusable aluminum T-slot/strut profile stock rather than a bespoke machined part; BOM/recipe can carry the 70.4 mm cut length."
---
