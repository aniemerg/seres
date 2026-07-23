---
row_identity:
  item: "2AP6"
  cad_file: "2AP6_outer_seal"
  source_row_number: 75
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Outer seal for the reAM250 2AP build/lifting-platform stack, most likely a perimeter gasket that closes or isolates the outer edge of the platform/seal interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/reports/missing_or_suspicious_items.md; research/ream250_bom/ream250_bom_row_0075_2AP6_sibling_inner_seal_context__views_2x2.png"
    cited_fact_or_basis: "BOM row 75 states item 2AP6, quantity 1, CAD file 2AP6_outer_seal, manufacturer/distributor field Mercateo. The manifest and missing/suspicious report state that no 2AP6_outer_seal CAD product or exported file was found and that 2AP6_inner_seal exists separately. Nearby BOM rows include a heating plate, lifting platform, pressing plate, felt seal, build platform, and inner seal guide. The separately mapped 2AP6_inner_seal preview shows a thin 250 x 250 x 5 mm square frame seal shape used only as contextual evidence for the seal family."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The name outer_seal is interpreted relative to the separately listed inner_seal as the outer perimeter member of a two-seal interface around the build/lifting platform."
    - "The part is treated as a sealing consumable rather than a structural frame because the BOM name is seal and the sibling seal is a thin frame."
  uncertainty_notes:
    - "targeted_web_search: searched \"2AP6_outer_seal\", \"2AP6 outer seal Mercateo\", \"2AP6_inner_seal\", and \"2AP6 inner seal\"; results were duplicate reAM250 BOM text or unrelated seal products, with no row-specific vendor page, drawing, or function note."
    - "The row-specific CAD is missing, so the exact interface, cross-section, compression direction, and sealing medium are unresolved."
mass:
  value_kg: 0.12
  basis: "No row-specific outer-seal CAD volume is available. A size-class estimate uses the separately mapped 2AP6_inner_seal as a sibling proxy: FreeCAD measured volume 112482.832 mm^3, bounding box 250.00 x 250.00 x 5.00 mm. Using the local NBR representative density of 1100 kg/m^3 gives 0.1237 kg, rounded to 0.12 kg per unit. BOM quantity is 1, so the row total is also about 0.12 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP6_inner_seal.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "The manifest says 2AP6_outer_seal is missing_in_cad and that 2AP6_inner_seal is mapped separately. FreeCAD measured the sibling inner seal as 1 solid, volume 112482.832 mm^3, area 53975.965 mm^2, and bounding box 250.00 x 250.00 x 5.00 mm. The local density table lists representative nitrile rubber / NBR density as 1100 kg/m^3. targeted_web_search: searched \"2AP6_outer_seal weight\", \"2AP6 outer seal Mercateo weight\", \"2AP6_outer_seal material\", and \"2AP6 inner seal weight\"; found no row-specific catalog mass or drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The outer seal is assumed to be in the same size class as the separately mapped inner seal because both share item code 2AP6 and are adjacent BOM rows in the same platform seal stack."
    - "NBR density is used as a representative elastomer density for planning because the exact elastomer is unresolved."
  uncertainty_notes:
    - "The 0.12 kg value is a proxy estimate, not a measured outer-seal mass; actual mass could differ if the outer seal has a larger frame, different cross-section, foam/felt construction, or metal carrier."
material:
  primary_material: "unknown elastomer seal material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP6_inner_seal.step; research/ream250_bom/ream250_bom_row_0075_2AP6_sibling_inner_seal_context__views_2x2.png"
    cited_fact_or_basis: "BOM row 75 names the row 2AP6_outer_seal but provides no material grade. Assembly STEP material extraction found no product match for 2AP6_outer_seal. The separately mapped 2AP6_inner_seal extraction returned Generic with density 1000.0, which is placeholder metadata under the task rules. The sibling preview shows a thin square frame seal. targeted_web_search: searched \"2AP6_outer_seal material\", \"2AP6 outer seal Mercateo material\", \"2AP6_inner_seal material\", and \"reAM250 2AP6 seal material\"; found duplicate BOM text and unrelated seal pages, not a row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A broad elastomer seal material family is inferred from the BOM name outer_seal and the thin frame geometry of the sibling inner seal."
  uncertainty_notes:
    - "The specific compound is unresolved; NBR, FKM, silicone, EPDM, felt, or another compliant gasket material may be required depending on temperature, powder exposure, vacuum/leak requirements, and compression set limits."
how_to_make:
  summary: "Prepare as a replacement gasket/seal if the original Mercateo route can be recovered; otherwise fabricate locally as a custom cut elastomer frame from sheet stock after the mating groove and compression requirements are measured"
  manufacturing_steps:
    - "Recover or measure the outer-seal groove/profile from the 2AP platform assembly because the row-specific CAD export is missing."
    - "Select an elastomer sheet or gasket material compatible with the platform temperature, powder exposure, and required compression set."
    - "Waterjet cut, knife cut, die cut, or CNC knife plot the outer perimeter and inner opening from sheet stock; use molding or vulcanized tooling only if the seal has a non-rectangular cross-section or embedded carrier."
    - "Inspect thickness, perimeter dimensions, corner radii, and joint continuity; clean for the machine environment before installation."
    - "Install with controlled compression against the mating plate or guide and replace if permanent set, tearing, or leakage appears."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0075_2AP6_sibling_inner_seal_context__views_2x2.png"
    cited_fact_or_basis: "BOM row 75 identifies a Mercateo-sourced outer seal with quantity 1, but no product ID or link URL. The manifest records missing_in_cad for the outer seal. Sibling inner-seal visual context shows a flat square frame seal form. targeted_web_search: searched \"2AP6_outer_seal Mercateo\", \"2AP6 outer seal replacement\", \"2AP6_outer_seal drawing\", and \"2AP6 seal reAM250\" no row-specific manufacturing drawing, catalog page, material callout, or process route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Flat-sheet gasket cutting is assumed as the simplest plausible Manufacturing route for a thin frame seal when no molded cross-section is evidenced."
  uncertainty_notes:
    - "If the original outer seal is molded, reinforced, adhesive-backed, or made from felt rather than elastomer sheet, The manufacturing route and mass estimate would need revision."
kb_implications:
  - "item_granularity: simple_part - model as a replaceable perimeter seal/gasket for the 2AP platform stack, with exact material and dimensions deferred until the missing CAD, drawing, or supplier product ID is recovered."
---

Research result for reAM250 BOM row 75.
