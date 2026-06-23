---
row_identity:
  item: "17A7"
  cad_file: "17A7_strut_profile_20X20_D50"
  source_row_number: 226
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short 20 x 20 mm Bosch Rexroth strut-profile segment used as a structural or spacer/connector member in the reAM250 frame or subassembly; the four open slots accept matching profile fasteners and brackets."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A7_strut_profile_20X20_D50.step; research/ream250_bom/ream250_bom_row_0226_17A7__views_2x2.png"
    cited_fact_or_basis: "BOM row 226 identifies item 17A7 as quantity 1, description 'strut profile', manufacturer Bosch Rexroth AG. FreeCAD measured one solid with 50.00 x 20.00 x 20.00 mm bounding box, and the rendered preview shows a four-slot extrusion cross-section."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD export represents the one physical profile segment in the BOM row."
  uncertainty_notes:
    - "The BOM and CAD do not state the exact mounting location, so the function is resolved at profile-member granularity rather than a specific frame joint."
mass:
  value_kg: 0.0224
  basis: "Per-unit mass for quantity 1. FreeCAD volume 8280.953 mm^3 = 8.280953e-6 m^3; assembly STEP material metadata reports density 2700 kg/m^3 for Aluminum 6061; 8.280953e-6 m^3 * 2700 kg/m^3 = 0.02236 kg. Optional row total is the same because quantity is 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A7_strut_profile_20X20_D50.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 8280.953 mm^3, area 9382.047 mm^2, and 50.00 x 20.00 x 20.00 mm bounding box. Local STEP material extraction for product 17A7_strut_profile_20X20_D50 returned material Aluminum 6061 and density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is treated as the as-installed material volume for one BOM-row item."
    - "The STEP density is treated as kg/m^3-like metadata, consistent with the extraction script note for the reAM250 export."
  uncertainty_notes:
    - "Small CAD export simplifications or end-cut details could shift the mass slightly, but the estimate is within the precision needed for BOM planning."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 17A7_strut_profile_20X20_D50 returned material 'Aluminum 6061' with density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local metadata resolves the alloy family for this CAD row, but it does not separately specify surface treatment such as anodizing."
how_to_make:
  summary: "Procure a Bosch Rexroth-compatible 20 x 20 mm aluminum strut profile segment, preferably cut to the 50 mm row length, then install it with the matching slot fasteners or brackets in the reAM250 assembly."
  manufacturing_steps:
    - "Order or cut a Bosch Rexroth 20 x 20 mm strut profile to 50 mm length."
    - "Deburr cut ends if cut from longer stock."
    - "Assemble through the four profile slots using compatible Bosch Rexroth profile connectors, sliding blocks, or brackets required by the surrounding assembly."
  source:
    url_or_path: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A7_strut_profile_20X20_D50.step"
    cited_fact_or_basis: "The BOM-provided Bosch Rexroth store route is for 'Strebenprofil' strut profiles, BOM row 226 names Bosch Rexroth AG and 'strut profile', and CAD fixes the row length and cross-section at 50.00 x 20.00 x 20.00 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB planning, procurement or cut-to-length stock preparation is the relevant route for this vendor extrusion row."
  uncertainty_notes:
    - "The exact connector set used with this short segment is outside this row and should be resolved from adjacent BOM rows or the parent assembly."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable 20 x 20 aluminum profile cut-length variant or parameterized stock segment, not as a machine-specific purchased module."
---
