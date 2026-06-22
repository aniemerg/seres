---
row_identity:
  item: 2AH
  cad_file: 2AH_connection_mount
  source_row_number: 59
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Connection mount for the R16-05T3 ballscrew/axis region, modeled as a long structural bracket or carrier block with a central circular bore and relief pockets.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AH_connection_mount.step; research/ream250_bom/ream250_bom_row_0059_2AH__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv
    cited_fact_or_basis: "BOM/manifest row 59 names item 2AH as 2AH_connection_mount with description R16-05T3-DEB-401-490- 0,023+E1_S21-10+E2_S11-. FreeCAD measured one solid with a 228.00 x 52.00 x 25.00 mm bounding box, and the rendered views show a long mount block with a central bore/clearance hole and lightening or machining pockets."
    evidence_basis: bom_provided
  assumptions:
    - The row name connection_mount and neighboring R16-05T3 connection-axis rows indicate this part mounts or locates the ballscrew/axis connection rather than acting as the ballscrew nut itself.
  uncertainty_notes:
    - The CAD package gives geometry but no assembly placement view in this result, so the exact mating interfaces and load direction are inferred from row naming and visible features.
mass:
  value_kg: 0.655
  basis: "Per-unit value for quantity 1. CAD volume is 242496.524 mm^3, equal to 0.000242496524 m^3. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 0.655 kg; if the same volume were generic steel at 7850 kg/m^3, the mass would be about 1.90 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AH_connection_mount.step; kb/materials/properties.yaml
    cited_fact_or_basis: "FreeCAD measured CAD volume 242496.523836041 mm^3. Local material table lists aluminum density 2700 kg/m^3 and generic steel density 7850 kg/m^3. targeted_web_search: searched \"R16-05T3-DEB-401-490\", \"2AH_connection_mount\", and \"R16-05T3 DEB 401 490 connection mount\"; results found duplicate BOM listings and related ballscrew catalog context, but no row-specific mass, material, or drawing for 2AH_connection_mount."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The selected planning mass assumes the custom mount is machined aluminum, a common choice for a long axis mounting bracket with relief pockets.
  uncertainty_notes:
    - Assembly STEP material extraction returned only material Generic with density 1000.0, so it does not resolve material. The real mass could be substantially higher if the part is steel.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AH_connection_mount.step
    cited_fact_or_basis: "Local assembly STEP material extractor matched product 2AH_connection_mount but returned material Generic with density 1000.0. CAD geometry is a structural machined mount form. targeted_web_search: searched \"R16-05T3-DEB-401-490\", \"2AH_connection_mount\", and \"R16-05T3 DEB 401 490 connection mount material\"; no usable row-specific material source was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Treat as a metallic structural bracket for later KB planning; aluminum alloy is plausible but not sourced.
  uncertainty_notes:
    - The exact alloy or grade is unresolved. Do not encode a specific aluminum or steel grade in KB without better source evidence.
how_to_make:
  summary: Plausibly produced as a CNC-machined metal bracket from rectangular bar or plate stock, with pocketing, end features, and the central bore machined in setup-controlled operations.
  manufacturing_steps:
    - Cut rectangular metal stock to rough length.
    - CNC mill the outer profile, long relief pockets, and end geometry.
    - Drill, bore, or interpolate the central circular feature and any mounting holes or slots required by mating parts.
    - Deburr, inspect critical dimensions, and optionally anodize or otherwise finish if aluminum is used.
  source:
    url_or_path: research/ream250_bom/ream250_bom_row_0059_2AH__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AH_connection_mount.step
    cited_fact_or_basis: "Rendered CAD views show a single-piece block-like mount with planar faces, milled pockets, and a central circular bore, all compatible with subtractive machining from bar or plate stock. targeted_web_search: searched \"2AH_connection_mount manufacturing\", \"R16-05T3-DEB-401-490 connection mount\", and \"R16 ballscrew connection mount drawing\"; no row-specific manufacturing route was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD represents a one-piece custom mount, not an off-the-shelf purchased module.
    - CNC machining is preferred over casting or additive manufacturing because the geometry is prismatic with machined pockets and likely interface tolerances.
  uncertainty_notes:
    - Without a drawing, tolerances, surface finish, heat treatment, and final coating remain unknown.
kb_implications:
  - "item_granularity: simple_part - Model as one custom machined connection-mount part; keep material broad until a drawing or source resolves aluminum versus steel."
---
