---
row_identity:
  item: "99"
  cad_file: "99_bottom_square_profile"
  source_row_number: 302
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Bottom structural hollow profile, about 900 mm long with a 100 x 80 mm outside envelope, used as a frame/base member in the reAM250 structure; BOM quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/99_bottom_square_profile.step; research/ream250_bom/ream250_bom_row_0302_99__views_2x2.png"
    cited_fact_or_basis: "BOM row 302 lists item 99, quantity 2, CAD file 99_bottom_square_profile. Manifest row 302 maps the same item to the matched part STEP. FreeCAD measured one solid with volume 1529999.999999999 mm^3, area 599948.6677646162 mm^2, and bounding box 900.00 x 100.00 x 80.00 mm. The rendered contact sheet shows a straight hollow rectangular/square tube-like profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The isolated row STEP represents one physical profile member, not the total row quantity."
    - "The word 'bottom' in the CAD filename and nearby frame/profile BOM rows indicate a base or lower-frame structural role."
  uncertainty_notes:
    - "The row evidence does not identify the exact installed location, connection method, or whether end holes/notches are added elsewhere."
mass:
  value_kg: 12.01
  basis: "Per-unit estimate for one physical profile. FreeCAD measured CAD volume 1,530,000.000 mm^3 = 0.001530000 m^3. The 900 x 100 x 80 mm bounding box and volume imply an average cross-section area of 1700 mm^2, matching a 100 x 80 x 5 mm rectangular hollow section by area: 100*80 - 90*70 = 1700 mm^2. Using the local steel density 7850 kg/m^3 gives 0.001530000 m^3 * 7850 kg/m^3 = 12.0105 kg, rounded to 12.01 kg per unit. BOM quantity is 2, so the row total is about 24.02 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/99_bottom_square_profile.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1529999.999999999 mm^3, area 599948.6677646162 mm^2, and bounding box 900.00 x 100.00 x 80.00 mm. Local assembly STEP material extraction for 99_bottom_square_profile returned only placeholder material 'Generic' with density 1000.0. kb/materials/properties.yaml lists steel density 7850 kg/m^3. targeted_web_search: searched '99_bottom_square_profile reAM250 material', 'bottom_square_profile reAM250', '100x80x5 rectangular hollow section steel kg per metre', and 'EN 10219 rectangular hollow section 100x80x5 steel mass kg/m'; results found the public BOM row and generic rectangular hollow-section steel references, but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a steel 100 x 80 x 5 mm hollow structural profile because the CAD volume exactly matches that wall-section area and nearby BOM rows use steel DIN EN 10219 hollow profiles."
    - "The local steel density entry is used as the calculation constant for the planning estimate."
  uncertainty_notes:
    - "If this bottom profile was actually aluminum or another alloy, the mass would differ substantially; for example the same CAD volume at 2700 kg/m^3 would be about 4.13 kg per unit."
    - "The CAD-derived mass assumes the STEP includes the true hollow profile wall, corner radii, and length."
material:
  primary_material: "structural steel rectangular hollow profile/tube"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/99_bottom_square_profile.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 302 names 99_bottom_square_profile but gives no material, manufacturer, product ID, or link. FreeCAD measured a 900.00 x 100.00 x 80.00 mm hollow-profile shape. Assembly STEP material extraction returned only placeholder 'Generic' material and density 1000.0. Nearby BOM rows include steel square hollow section rows using DIN EN 10219-2 naming. targeted_web_search: searched '99_bottom_square_profile reAM250 material', 'bottom_square_profile reAM250', '100x80x5 rectangular hollow section steel kg per metre', and 'DIN EN 10219 rectangular hollow section non-alloy fine grain steels'; results found the public BOM row and generic structural hollow-section steel references, but no row-specific drawing, alloy, or grade."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Material is kept at broad structural-steel-family precision because the row lacks a specific material grade and the STEP metadata is placeholder."
    - "The geometry and surrounding BOM context are stronger evidence for a hollow structural steel profile than for a Bosch-style aluminum T-slot profile."
  uncertainty_notes:
    - "No row-specific grade such as S235, S275, S355, stainless, or aluminum alloy is provided."
    - "The exact surface finish or coating is unknown."
how_to_make:
  summary: "Procure as 100 x 80 x 5 mm structural steel hollow profile/tube stock and cut to the 900 mm CAD length; full local manufacture would use steel tube forming and seam welding followed by cut-off and deburring."
  manufacturing_steps:
    - "Source structural steel rectangular hollow section stock close to the CAD-implied 100 x 80 x 5 mm profile."
    - "Cut one member to the 900 mm CAD length."
    - "Deburr and clean the cut ends, preserving the profile envelope for fit-up."
    - "Inspect length, squareness, straightness, and wall/profile condition before fastening or welding into the lower frame."
    - "If making the stock locally, form steel strip into a rectangular hollow profile, weld the seam, size/straighten the section, then cut to length."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/99_bottom_square_profile.step; research/ream250_bom/ream250_bom_row_0302_99__views_2x2.png; web targeted search"
    cited_fact_or_basis: "The row STEP and preview show a constant-section 900.00 x 100.00 x 80.00 mm hollow profile. targeted_web_search: searched '99_bottom_square_profile reAM250 material', '100x80x5 rectangular hollow section steel kg per metre', and 'EN 10219 rectangular hollow section 100x80x5 steel mass kg/m'; results supported the common structural hollow-section stock route but did not provide a row-specific manufacturing drawing or supplier process for this exact reAM250 part."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, the normal route is procurement of stock hollow section and saw/abrasive cut-to-length rather than bespoke machining from solid."
    - "No special machined features are visible in the rendered contact sheet."
  uncertainty_notes:
    - "The row does not specify whether the production part is painted, plated, welded into a larger frame, or modified after cutting."
kb_implications:
  - "item_granularity: raw_material_or_stock - Model later as cut structural hollow steel profile stock, approximately 100 x 80 x 5 x 900 mm, with BOM quantity/length variants handled as profile-stock cuts rather than unique purchased modules."
---

Research result for the leased reAM250 BOM row only.
