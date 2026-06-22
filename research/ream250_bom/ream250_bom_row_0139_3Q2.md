---
row_identity:
  item: "3Q2"
  cad_file: "3Q2_angle_pipe_ISO_K_DN100_320RRB100-90"
  source_row_number: 139
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90"
function:
  summary: "DN 100 ISO-K 90 degree vacuum elbow/angle pipe used to turn a large vacuum line while preserving a flanged ISO-K connection at both ends."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q2_angle_pipe_ISO_K_DN100_320RRB100-90.step; research/ream250_bom/ream250_bom_row_0139_3Q2__views_2x2.png"
    cited_fact_or_basis: "BOM row 139 identifies item 3Q2 as Pfeiffer Vacuum product 320RRB100-90. The BOM-provided Pfeiffer page titles it as a 90 degree pipe elbow, stainless 1.4301/304, DN 100 ISO-K. FreeCAD measured one solid, and the contact sheet shows a curved elbow with circular ISO-style end flanges."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical elbow for this BOM row."
  uncertainty_notes: []
mass:
  value_kg: 1.67
  basis: "Per-unit planning estimate for BOM quantity 1. FreeCAD volume is 207940.963 mm^3, equal to 2.07940963e-4 m^3. Using the local stainless_steel_304 density constant of 8030 kg/m^3 gives 1.6698 kg, rounded to 1.67 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q2_angle_pipe_ISO_K_DN100_320RRB100-90.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 207940.963 mm^3 and bounding box 179.51 x 179.51 x 143.02 mm. The BOM-provided Pfeiffer page identifies product 320RRB100-90 as stainless 1.4301/304. kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is used as the physical metal volume for one elbow."
    - "Stainless 1.4301/304 is mapped to the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "If the STEP volume omits small weld beads, flange details, or internal seam geometry, the actual catalog weight may differ modestly from this CAD-derived estimate."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided Pfeiffer page for article number 320RRB100-90 states the DN 100 ISO-K 90 degree elbow is Edelstahl 1.4301/304. Local assembly STEP extraction for this product returned only material 'Generic' with density 1000.0, so the vendor/BOM route supplies the material value."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 320RRB100-90, or locally fabricate as a cleaned stainless 304 ISO-K 90 degree vacuum elbow with two ISO-K flange ends."
  manufacturing_steps:
    - "Cut or form a stainless 304 90 degree elbow body sized for DN 100 vacuum service."
    - "Machine or form the ISO-K flange features at both ends, matching the DN 100 interface."
    - "Weld or otherwise join the elbow body and flange ends, then finish and clean internal surfaces for vacuum compatibility."
    - "Inspect flange geometry, leak-tightness, and cleanliness before installation in the vacuum line."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q2_angle_pipe_ISO_K_DN100_320RRB100-90.step; research/ream250_bom/ream250_bom_row_0139_3Q2__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Pfeiffer page identifies the row as a stainless 1.4301/304 DN 100 ISO-K 90 degree elbow, and the CAD preview shows a flanged curved pipe fitting. targeted_web_search: tried 'Pfeiffer 320RRB100-90 weight dimensions 90 angle pipe DN 100 ISO-K', '320RRB100-90 Pfeiffer Vacuum mass weight', and '\"320RRB100-90\" \"kg\"'; results confirmed product identity/material/dimensions but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local fabrication route is inferred from the observed vacuum elbow geometry and stainless ISO-K component type, not from a Pfeiffer manufacturing disclosure."
  uncertainty_notes:
    - "Detailed fabrication choices such as mandrel bending versus segmented welding, flange-forming method, weld procedure, and acceptance leak rate remain unspecified by the BOM evidence."
kb_implications:
  - "item_granularity: simple_part - Treat as a standard stainless vacuum pipe fitting/elbow for KB planning, reusable across ISO-K DN 100 vacuum plumbing rather than as a calibrated vendor module."
---

Result generated for the leased reAM250 BOM row only.
