---
row_identity:
  item: "3S2"
  cad_file: "3S2_mount"
  source_row_number: 146
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small mounting bracket for the 3S gas outlet/flange area, likely used as a local support, spacer, or attachment point for the neighboring 3S outlet components."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S2_mount.step; research/ream250_bom/ream250_bom_row_0146_3S2__views_2x2.png"
    cited_fact_or_basis: "BOM row 146 lists item 3S2, quantity 2, CAD file 3S2_mount. The manifest maps row 146 to one matched_existing part STEP. FreeCAD measured one solid with a 20.00 x 30.00 x 15.00 mm bounding box, and the rendered preview shows a compact L/bracket-like mount with a circular through feature. Nearby BOM rows include 3S1_flange and 3S31-3S35 gas outlet pipe parts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'mount' and proximity to 3S flange/gas outlet rows identify the part as support or attachment hardware rather than a flow-path duct."
  uncertainty_notes:
    - "The exact mating part and fastener role are not specified by the BOM row, so the support/attachment function is inferred from row context and CAD geometry."
mass:
  value_kg: 0.0105
  basis: "FreeCAD volume 1332.948 mm^3 = 1.332948e-6 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.01046 kg per mount, rounded to 0.0105 kg. BOM quantity is 2, so the row total would be about 0.021 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S2_mount.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 1332.948 mm^3, area 1621.266 mm^2, and bounding box 20.00 x 30.00 x 15.00 mm. The local density table lists steel at 7850 kg/m^3 and aluminum at 2700 kg/m^3. targeted_web_search: searched \"3S2_mount reAM250\", \"3S2 reAM250 mount\", \"reAM250 3S2\", and \"3S2_mount\"; found duplicate BOM text but no row-specific material or catalog mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume is treated as the physical material volume for one mount."
    - "Generic steel density is used as a conservative metal-bracket estimate because no source resolves the alloy."
  uncertainty_notes:
    - "Material is not directly specified; if this mount is aluminum, the same CAD volume would be about 0.0036 kg using the local aluminum density."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 146 identifies the part only as 3S2_mount and provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S2_mount returned only placeholder material 'Generic' with density 1000.0. targeted_web_search: searched \"3S2_mount reAM250\", \"3S2 reAM250 mount material\", \"reAM250 3S2 mount material\", and \"3S2_mount\"; found duplicate BOM text but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is modeled as metal hardware because the CAD shows a rigid compact mounting bracket in a gas/vacuum outlet area."
  uncertainty_notes:
    - "No evidence resolves the exact material family or grade; downstream KB modeling should keep this broad unless a drawing or assembly material note identifies the alloy."
how_to_make:
  summary: "Make as a simple machined or bent metal mounting bracket: cut a small metal blank, form or machine the L-like profile, drill or machine the circular mounting feature, deburr, clean, and inspect fit against the mating outlet hardware."
  manufacturing_steps:
    - "Cut a small metal blank from sheet, plate, or bar stock to cover the roughly 20 x 30 x 15 mm envelope."
    - "Bend/form the right-angle bracket shape or machine the profile from a small block, depending on tolerance and stock choice."
    - "Drill, bore, or mill the circular through feature visible in the CAD preview."
    - "Deburr, clean, and inspect the mounting faces and hole location before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S2_mount.step; research/ream250_bom/ream250_bom_row_0146_3S2__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 20.00 x 30.00 x 15.00 mm bounding box. The rendered preview shows a compact bracket-like geometry with two perpendicular legs and a circular through feature. targeted_web_search: searched \"3S2_mount reAM250 manufacturing\", \"3S2 reAM250 mount drawing\", \"reAM250 3S2 mount\", and \"3S2_mount\" found duplicate BOM text but no row-specific fabrication drawing or manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the simple bracket geometry and likely low-volume machine-specific hardware role."
    - "Either bent sheet/plate or simple machining is plausible; final choice depends on material and tolerance callouts not present in the row evidence."
  uncertainty_notes:
    - "The CAD and BOM do not state tolerances, material, surface finish, or whether the original part was bent from sheet or machined from solid stock."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable small metal mounting bracket/spacer for the 3S outlet area, not as a purchased module or multi-part assembly."
---

Research result for reAM250 BOM row 146.
