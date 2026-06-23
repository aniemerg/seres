---
row_identity:
  item: "87"
  cad_file: "87_reduction_T_pipe_ISO_KF_DN40_DN16"
  source_row_number: 283
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120RTR040_016"
function:
  summary: "ISO-KF stainless reducing tee that connects a DN 40 ISO-KF vacuum line to a reduced DN 16 ISO-KF branch while preserving clamp-and-center-ring vacuum interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/87_reduction_T_pipe_ISO_KF_DN40_DN16.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/120RTR040_016"
    cited_fact_or_basis: "BOM row 283 lists item 87, quantity 1, product 120RTR040-016, Pfeiffer Vacuum link URL. The row STEP renders as a tee-shaped tube with KF lips and a smaller side branch. The Pfeiffer BOM URL identifies 120RTR040-016 as a Reduzier-T-Stueck / reducing tee with connection flange DN 40 ISO-KF to DN 16 ISO-KF."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP contact sheet is used only for row-specific shape/function triage, not exact dimensional measurement."
  uncertainty_notes: []
mass:
  value_kg: 0.32
  basis: "Per-unit estimate for one physical reducing tee. FreeCAD measured one solid with volume 39807.357 mm^3, area 38266.303 mm^2, and bounding box about 130.00 x 59.53 x 59.53 mm. Using local density constant for stainless_steel_304 from kb/materials/properties.yaml, 8030 kg/m^3, gives 39807.357 mm^3 * 1e-9 m^3/mm^3 * 8030 kg/m^3 = 0.31965 kg, rounded to 0.32 kg. BOM quantity is 1, so row total is about 0.32 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/87_reduction_T_pipe_ISO_KF_DN40_DN16.step; kb/materials/properties.yaml; https://www.pfeiffer-vacuum.com/global/de/shop/products/120RTR040_016"
    cited_fact_or_basis: "FreeCAD measured the supplied row STEP as a single solid with volume 39807.357 mm^3. The Pfeiffer BOM URL states material in contact with media as stainless steel 1.4301 (AISI 304). kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied single-solid STEP volume is treated as the physical metal volume for one tee."
    - "Stainless steel 304 / EN 1.4301 local density is a suitable calculation constant for this fitting."
  uncertainty_notes:
    - "If the vendor STEP omits small internal chamfers or flange details, actual mass may differ modestly from the CAD-derived estimate."
material:
  primary_material: "stainless steel 1.4301 (AISI 304)"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120RTR040_016; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer BOM URL for 120RTR040-016 states materials in contact with media as stainless steel 1.4301 (AISI 304). Local assembly STEP material extraction for this CAD object returned only Generic at density 1000.0, which is placeholder metadata and was not used to resolve material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source resolves the wetted fitting material; it does not separately specify any surface finish or passivation."
how_to_make:
  summary: "Best modeled as a procured ISO-KF reducer tee; plausible local manufacture would form or machine stainless 304 tube/flange features, join the reduced DN16 branch to the DN40 run, finish sealing faces, and inspect for vacuum leakage."
  manufacturing_steps:
    - "Procurement route: buy Pfeiffer Vacuum 120RTR040-016 or an equivalent DN 40 ISO-KF to DN 16 ISO-KF stainless 304 reducing tee."
    - "Local route: cut stainless 304 tube blanks for the DN40 run and DN16 branch."
    - "Form or machine ISO-KF lip/flange sealing interfaces to the row dimensions."
    - "Weld or braze the reduced branch into the main tube, then clean, passivate if required, and leak-test the fitting."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120RTR040_016; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/87_reduction_T_pipe_ISO_KF_DN40_DN16.step"
    cited_fact_or_basis: "The Pfeiffer BOM URL identifies a commercially supplied stainless 1.4301/304 reducing tee with DN 40 ISO-KF to DN 16 ISO-KF interfaces. The supplied STEP/contact sheet shows a tee-shaped metal tube with KF flange lips; the detailed local fabrication sequence is inferred from that geometry."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route is inferred from standard stainless vacuum fitting geometry rather than a Pfeiffer process disclosure."
  uncertainty_notes:
    - "targeted_web_search: searched `Pfeiffer 120RTR040-016 manufacturing process stainless reducing tee`, `120RTR040-016 datasheet material dimensions`, and `ISO-KF stainless reducing tee fabrication`; row-matched results resolved procurement, dimensions, and material but did not provide a manufacturer process route."
kb_implications:
  - "item_granularity: simple_part - Treat as reusable standard ISO-KF stainless vacuum plumbing hardware rather than a reAM250-specific assembly or calibrated module."
---
