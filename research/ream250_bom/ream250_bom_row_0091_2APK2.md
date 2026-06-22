---
row_identity:
  item: "2APK2"
  cad_file: "2APK2_front_back"
  source_row_number: 91
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Pair of thin front/back plates in the 2APK0 heating-plate-cover group, likely closing or retaining the front and rear sides around the build-platform/heating-plate and inner-seal-guide area."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK2_front_back.step; research/ream250_bom/ream250_bom_row_0091_2APK2__views_2x2.png"
    cited_fact_or_basis: "BOM row 91 lists item 2APK2, quantity 2, CAD file 2APK2_front_back. Manifest row 91 maps it to one matched_existing part STEP. The full assembly names the adjacent parent product 2APK0_heating_plate_cover, with sibling rows 2APK1_bottom and 2APK3_left_right. FreeCAD measured one solid with bounding box 6.00 x 46.00 x 68.00 mm, and the rendered contact sheet shows a thin rectangular front/back cover plate with folded or beveled side edges and small tab-like features along one edge."
    evidence_basis: "bom_provided"
  assumptions:
    - "The suffix front_back means the same physical plate is used at both the front and rear of the heating-plate-cover group."
    - "The closure/retainer role is inferred from the row name, neighboring 2APK cover rows, and plate-like CAD geometry."
  uncertainty_notes:
    - "The CAD/BOM evidence does not expose mating constraints or fastener details, so the exact interface to the bottom, left/right plates, build platform, and seal guide remains unresolved."
mass:
  value_kg: 0.145
  basis: "Per-unit planning estimate for one 2APK2 plate; BOM quantity is 2, so row total is about 0.290 kg. FreeCAD volume is 18504.534 mm^3, equal to 1.8504534e-5 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.14526 kg, rounded to 0.145 kg. If the same CAD volume were aluminum at 2700 kg/m^3, one plate would be about 0.0500 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK2_front_back.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 18504.534 mm^3, area 8045.908 mm^2, and bounding box 6.00 x 46.00 x 68.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried '\"2APK2_front_back\"', '\"2APK2\" \"reAM250\"', '\"2APK2\" \"front_back\" CAD', and '\"2APK0_heating_plate_cover\"'; results found duplicate reAM250 BOM text but no row-specific catalog mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The supplied STEP solid volume is treated as the finished physical volume for one front/back plate."
    - "A steel-like density is used as a conservative single-value planning estimate for this small structural cover/retainer plate because no row-specific material is provided."
  uncertainty_notes:
    - "Actual mass could be closer to 0.0500 kg per plate if this piece is aluminum rather than steel; no catalog weight, drawing, or non-placeholder STEP material metadata resolves the material-dependent range."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0091_2APK2__views_2x2.png"
    cited_fact_or_basis: "BOM row 91 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2APK2_front_back returned material 'Generic' with density 1000.0, which is placeholder metadata. CAD preview shows a rigid thin plate in the heating-plate-cover group. targeted_web_search: tried '\"2APK2_front_back\"', '\"2APK2\" \"reAM250\"', '\"2APK2\" \"front_back\" CAD', and '\"2APK0_heating_plate_cover\"'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The rigid plate geometry and build-platform/heating-plate-cover context indicate a metal plate rather than a polymer seal, felt element, sensor, or consumable."
  uncertainty_notes:
    - "Material family is broad only; downstream KB modeling should not choose a specific alloy or grade without a drawing, designer note, or better assembly metadata."
how_to_make:
  summary: "Fabricate as a small custom front/back cover plate from sheet or plate stock, then cut or machine the profile, edge reliefs, and tab features before deburring and fitting it into the 2APK heating-plate-cover group."
  manufacturing_steps:
    - "Cut a metal blank near the 6 x 46 x 68 mm finished envelope from sheet or flat plate stock."
    - "Machine, laser-cut, waterjet, or form the outside profile and the visible edge reliefs or folded/beveled side features."
    - "Form or machine the small tab-like features along the upper edge if they are functional locating or attachment features."
    - "Deburr edges, clean the part, and inspect fit against the paired front/back location and sibling 2APK bottom and left/right plates."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK2_front_back.step; research/ream250_bom/ream250_bom_row_0091_2APK2__views_2x2.png"
    cited_fact_or_basis: "CAD preview shows a one-piece thin plate with a 6.00 x 46.00 x 68.00 mm bounding box, beveled or folded side edges, and small tab-like features; FreeCAD reports one solid. targeted_web_search: tried '\"2APK2_front_back\" manufacturing', '\"2APK2\" \"reAM250\"', '\"2APK2\" \"front_back\" CAD', and '\"2APK0_heating_plate_cover\"'; no row-specific manufacturing drawing, vendor route, or material specification was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet/plate cutting plus light forming or machining is the most plausible route for a small one-piece custom plate with the observed geometry."
    - "Local self-manufacturing would need surrounding assembly constraints or drawings to set edge-feature tolerances and any surface-finish requirements."
  uncertainty_notes:
    - "The CAD preview is sufficient for manufacturing-route triage but not for bend radius, tolerance, surface finish, or whether the apparent tabs are functional features or export geometry artifacts."
kb_implications:
  - "item_granularity: simple_part - Model later as one reusable custom metal front/back cover plate used twice in the heating-plate-cover area, not as a purchased module."
---

Research result for the leased reAM250 BOM row only.
