---
row_identity:
  item: 2APG
  cad_file: 2APG_pressing_plate
  source_row_number: 86
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Thin square pressing plate in the reAM250 z-axis/build-platform subassembly, likely used to clamp or preload the nearby felt seal/build-platform stack while providing four corner fastener locations.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APG_pressing_plate.step; research/ream250_bom/ream250_bom_row_0086_2APG__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
    cited_fact_or_basis: "BOM row 86 names the item 2APG_pressing_plate; the manifest maps it to one matched part STEP. FreeCAD measured one solid with bounding box 225.00 x 225.00 x 3.80 mm, and the rendered preview shows a thin square plate with four corner holes and stiffened/relieved geometry. Neighboring BOM rows include shim disks, a felt seal, build platform, and inner seal guide."
    evidence_basis: bom_provided
  assumptions:
    - The filename "pressing_plate" is interpreted as a clamp/preload role because the CAD has corner holes and sits next to seal and build-platform rows.
  uncertainty_notes:
    - The exact mating faces and load path are not specified by the BOM row, so the function should be treated as subassembly-context inference rather than a sourced design description.
mass:
  value_kg: 1.45
  basis: "CAD volume 185298.002 mm^3 = 0.000185298 m^3. Using generic steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 1.454 kg, rounded to 1.45 kg. If aluminum were used, the same volume would be about 0.50 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APG_pressing_plate.step; kb/materials/properties.yaml
    cited_fact_or_basis: "FreeCAD measured volume 185298.00184445217 mm^3 for the row-specific STEP. Local density table lists generic steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried \"2APG_pressing_plate\", \"2APG pressing plate reAM250\", \"2APG 2APG_pressing_plate\", and \"reAM250 pressing plate\"; results repeated the public BOM/CAD identity but did not provide row-specific mass or material."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Generic steel is used as the planning density because a thin pressing/clamping plate in this machine area is more likely a metal structural part than a polymer part, and the local STEP material is only Generic.
  uncertainty_notes:
    - Material is unresolved beyond a broad metal/alloy family, so mass could plausibly range from about 0.50 kg for aluminum to about 1.48 kg for stainless steel at the measured CAD volume.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
    cited_fact_or_basis: "Assembly STEP material extraction for product 2APG_pressing_plate returned material Generic with density 1000.0, which is a placeholder and not a real material resolution. BOM row 86 and the manifest provide no manufacturer, product ID, or material hint. targeted_web_search: tried \"2APG_pressing_plate\", \"2APG pressing plate reAM250\", \"2APG 2APG_pressing_plate\", and \"reAM250 pressing plate\"; no row-specific material source was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The part is treated as a broad metal/alloy because the CAD is a thin perforated pressing plate in a mechanical build-platform/seal stack.
  uncertainty_notes:
    - No source distinguishes steel, stainless steel, or aluminum for this row; downstream KB modeling should avoid assigning a specific grade until a drawing, material list, or fabrication note is found.
how_to_make:
  summary: Make as a custom flat metal plate from sheet or thin plate stock, with profile cutting, corner-hole drilling, light machining or forming of the relieved/stiffened geometry, deburring, and inspection; procurement would be as a custom-fabricated machine plate rather than a catalog module.
  manufacturing_steps:
    - Cut a 225 mm square blank from sheet or thin plate stock.
    - Cut or machine the relieved/stiffened central geometry and outer profile features visible in CAD.
    - Drill or machine the four corner mounting holes.
    - Deburr, flatten if needed, and inspect hole positions and overall thickness.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APG_pressing_plate.step; research/ream250_bom/ream250_bom_row_0086_2APG__views_2x2.png
    cited_fact_or_basis: "CAD/preview show a single thin 225.00 x 225.00 x 3.80 mm plate with corner holes and cut/machined geometry. targeted_web_search: tried \"2APG_pressing_plate\", \"2APG pressing plate reAM250\", \"2APG 2APG_pressing_plate\", and \"reAM250 pressing plate\"; no vendor route or fabrication note was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Sheet/plate cutting plus drilling/machining is selected as the simplest plausible route for the observed single-plate geometry.
  uncertainty_notes:
    - The CAD does not reveal tolerances, flatness requirement, surface finish, or whether the raised/relieved features are machined, formed, or simplified from a source model.
kb_implications:
  - "item_granularity: simple_part - Model as one custom metal plate with a later material-grade decision; it does not need a sub-BOM unless future evidence shows inserts or bonded features."
---
