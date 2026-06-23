---
row_identity:
  item: "3C"
  cad_file: "3C_reduction_T_pipe_ISO_K_DN63_KF_DN40_320RTR063-040"
  source_row_number: 114
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040"
function:
  summary: "Reducer tee vacuum piping component that connects a DN 63 ISO-K port to a reduced DN 40 ISO-KF branch/connection in the reAM250 vacuum plumbing."
  source:
    url_or_path: "https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf"
    cited_fact_or_basis: "Row-matched Pfeiffer datasheet names order number 320RTR063-040 as a reducer tee, DN 63 ISO-K/40 KF, and lists the connection flange as DN 63 ISO-K / DN 40 ISO-KF. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access; the alternate datasheet is a Pfeiffer product datasheet for the same manufacturer, order number, and DN 63 ISO-K/40 KF product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM product ID 320RTR063-040 and manufacturer Pfeiffer Vacuum identify the same reducer tee described in the datasheet."
  uncertainty_notes:
    - "The local CAD preview shows the reduced flange/tube geometry but not the full 176 mm datasheet envelope, so CAD shape evidence is treated as supportive rather than complete for function."
mass:
  value_kg: 0.1164
  basis: "Per-unit estimate from FreeCAD STEP volume 14496.435 mm^3 multiplied by local stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml, giving 0.1164 kg each. BOM quantity is 2, so the row total is about 0.2328 kg if this CAD volume represents one complete row item."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3C_reduction_T_pipe_ISO_K_DN63_KF_DN40_320RTR063-040.step; kb/materials/properties.yaml; https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 14496.434917 mm^3, area 13675.173988 mm^2, and bounding box 59.53 x 47.92 x 59.53 mm; local density table lists stainless_steel_304 at 8030 kg/m^3; row-matched Pfeiffer datasheet states stainless steel 304/1.4301. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access; the alternate datasheet is a Pfeiffer product datasheet for the same manufacturer, order number, and DN 63 ISO-K/40 KF product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single CAD solid volume is used as the per-unit physical volume represented by this row's STEP file."
    - "The part is modeled as fully stainless steel 304/1.4301 for mass calculation."
  uncertainty_notes:
    - "Mass may be low for the complete commercial reducer tee because the datasheet dimensions include A 176 mm, B 75 mm, C 70 mm, and D 40.5 mm, while the local STEP bounding box is only about 59.53 x 47.92 x 59.53 mm."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf"
    cited_fact_or_basis: "Row-matched Pfeiffer datasheet states reducer tee, stainless steel 304/1.4301, DN 63 ISO-K/40 KF, and lists materials in contact with media as stainless steel 1.4301 (AISI 304). official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access; the alternate datasheet is a Pfeiffer product datasheet for the same manufacturer, order number, and DN 63 ISO-K/40 KF product identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Assembly STEP material extraction returned only Generic with density 1000.0, so local STEP metadata does not independently confirm the grade."
how_to_make:
  summary: "Procure as Pfeiffer 320RTR063-040 for the current BOM; a plausible local route is welded and machined stainless vacuum tubing/flange fabrication followed by leak testing and surface finishing."
  manufacturing_steps:
    - "Cut or form 304/1.4301 stainless tube sections and flange blanks for the DN 63 ISO-K and DN 40 ISO-KF interfaces."
    - "Machine flange lips, sealing faces, bores, and weld-prep edges to ISO-K/ISO-KF geometry."
    - "Weld the reduced tee body from the inside where accessible, finish external welds where geometry prevents internal-only welding, then clean/passivate."
    - "Helium leak-test and inspect sealing surfaces before installation."
  source:
    url_or_path: "https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3C_reduction_T_pipe_ISO_K_DN63_KF_DN40_320RTR063-040.step"
    cited_fact_or_basis: "Datasheet supports procurement identity, stainless material, ISO-K/ISO-KF interfaces, pressure range, and temperature range; CAD preview shows a flanged reducer/tube form. targeted_web_search: exact queries \"320RTR063-040 weight\", \"320RTR063-040 kg\", and \"Reducer tee 320RTR063-040 weight\" found row-matched datasheet/catalog pages but no directly stated manufacturing process or mass. bom_url_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route follows common stainless high-vacuum fitting practice inferred from geometry and material; the cited datasheet does not state the fabrication process."
  uncertainty_notes:
    - "Detailed weld sequence, wall thickness, and acceptance criteria should be sourced from a fabrication drawing or supplier manufacturing specification before modeling a production recipe."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable stainless vacuum piping fitting/reducer tee rather than a reAM250-specific assembly; model vendor procurement first and refine local stainless vacuum-fitting fabrication later."
---
