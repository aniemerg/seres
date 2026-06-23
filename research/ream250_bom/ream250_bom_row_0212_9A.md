---
row_identity:
  item: "9A"
  cad_file: "9A_top_square_profile"
  source_row_number: 212
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Top structural hollow profile, about 900 mm long with an 80 x 180 mm outside envelope, used as an upper frame or support member in the reAM250 structure; BOM quantity is 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9A_top_square_profile.step; research/ream250_bom/ream250_bom_row_0212_9A__views_2x2.png"
    cited_fact_or_basis: "BOM row 212 lists item 9A, quantity 1, CAD file 9A_top_square_profile. Manifest row 212 maps the same item to a matched existing part STEP. FreeCAD measured one solid with volume 2,250,000.000 mm^3, surface area 889,548.668 mm^2, and bounding box 900.00 x 80.00 x 180.00 mm. The rendered contact sheet shows a long straight rectangular hollow profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The isolated row STEP represents one physical profile member."
    - "The word 'top' in the CAD filename and neighboring profile/frame rows indicate an upper-frame structural role."
  uncertainty_notes:
    - "The row evidence does not identify the exact installed interface, fastening method, or whether hidden downstream drilling/welding features are applied."
mass:
  value_kg: 17.66
  basis: "Per-unit estimate for BOM quantity 1. FreeCAD measured CAD volume 2,250,000.000 mm^3 = 0.002250000 m^3. The 900 x 80 x 180 mm bounding box and volume imply an average cross-section area of 2500 mm^2, matching a 180 x 80 x 5 mm rectangular hollow section by area: 180*80 - 170*70 = 2500 mm^2. Using the local steel density 7850 kg/m^3 gives 0.002250000 m^3 * 7850 kg/m^3 = 17.6625 kg, rounded to 17.66 kg per unit."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9A_top_square_profile.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 2,250,000.000 mm^3, surface area 889,548.668 mm^2, and bounding box 900.00 x 80.00 x 180.00 mm. Local assembly STEP material extraction for 9A_top_square_profile returned only placeholder material 'Generic' with density 1000.0. kb/materials/properties.yaml lists steel density 7850 kg/m^3. targeted_web_search: searched '9A_top_square_profile reAM250 material', 'reAM250 9A_top_square_profile', 'reAM250 top square profile material', and '80x180x900 rectangular hollow section steel mass kg per metre'; results found the public reAM250 project/BOM context and generic rectangular hollow-section references, but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a steel 180 x 80 x 5 mm rectangular hollow structural profile because the CAD volume exactly matches that wall-section area and nearby reAM250 BOM rows use steel hollow-section profile naming."
    - "The local steel density entry is used as the calculation constant for the planning estimate."
  uncertainty_notes:
    - "If this top profile was actually aluminum or another alloy, the mass would differ substantially; the same CAD volume at 2700 kg/m^3 would be about 6.08 kg per unit."
    - "The CAD-derived mass assumes the STEP volume captures the true hollow-profile wall geometry, including any simplifications of corner radii and end condition."
material:
  primary_material: "structural steel rectangular hollow profile/tube"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9A_top_square_profile.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 212 names 9A_top_square_profile but gives no material, manufacturer, product ID, or link. FreeCAD measured a 900.00 x 80.00 x 180.00 mm hollow-profile shape. Assembly STEP material extraction returned only placeholder 'Generic' material and density 1000.0. Nearby BOM rows include steel square hollow section rows using DIN EN 10219-2 naming. targeted_web_search: searched '9A_top_square_profile reAM250 material', 'reAM250 9A_top_square_profile', 'reAM250 top square profile material', and 'DIN EN 10219 rectangular hollow section steel'; results found the public reAM250 project/BOM context and generic structural hollow-section steel references, but no row-specific drawing, alloy, or grade."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Material is kept at broad structural-steel-family precision because the row lacks a specific material grade and the STEP metadata is placeholder."
    - "The hollow structural profile geometry and surrounding steel-profile BOM context are stronger evidence than an aluminum T-slot or solid machined-block interpretation."
  uncertainty_notes:
    - "No row-specific grade such as S235, S275, S355, stainless, or aluminum alloy is provided."
    - "The exact coating, finish, and corrosion-protection state are unknown."
how_to_make:
  summary: "Procure as 180 x 80 x 5 mm structural steel rectangular hollow section stock and cut to the 900 mm CAD length; full local manufacture would use steel tube forming and seam welding followed by sizing, cut-off, deburring, and inspection."
  manufacturing_steps:
    - "Source structural steel rectangular hollow section stock close to the CAD-implied 180 x 80 x 5 mm profile."
    - "Cut one member to the 900 mm CAD length."
    - "Deburr and clean the cut ends, preserving the profile envelope for fit-up."
    - "Inspect length, squareness, straightness, and wall/profile condition before fastening or welding into the upper frame."
    - "If making the stock locally, form steel strip into a rectangular hollow profile, weld the seam, size and straighten the section, then cut to length."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9A_top_square_profile.step; research/ream250_bom/ream250_bom_row_0212_9A__views_2x2.png; web targeted search"
    cited_fact_or_basis: "The row STEP and preview show a constant-section 900.00 x 80.00 x 180.00 mm hollow profile. targeted_web_search: searched '9A_top_square_profile reAM250 material', 'reAM250 top square profile material', and '180x80x5 rectangular hollow section steel'; results supported the common structural hollow-section stock route but did not provide a row-specific manufacturing drawing or supplier process for this exact reAM250 part."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, the normal route is procurement of stock hollow section and saw/abrasive cut-to-length rather than machining from solid."
    - "No special machined holes, slots, pockets, or welded attachments are visible in the rendered contact sheet."
  uncertainty_notes:
    - "The row does not specify whether the production part is painted, plated, welded into a larger frame, or modified after cutting."
kb_implications:
  - "item_granularity: raw_material_or_stock - Model later as cut structural hollow steel profile stock, approximately 180 x 80 x 5 x 900 mm, with length/profile variants handled as stock cuts rather than unique purchased modules."
---

Research result for the leased reAM250 BOM row only.
