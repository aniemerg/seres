---
row_identity:
  item: "42A"
  cad_file: "42A_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 261
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "DN 32-40 ISO-KF clamping ring used to tighten and secure an elastomer-sealed KF vacuum flange joint; the reAM250 BOM uses quantity 3 of this row item."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; research/ream250_bom/ream250_bom_row_0261_42A__views_2x2.png"
    cited_fact_or_basis: "BOM row 261 identifies item 42A as Pfeiffer Vacuum product 120BSR040. The associated product route identifies 120BSR040 as a clamping ring for elastomer seals, DN 32-40 ISO-KF. The local row CAD preview shows a clamp/handle feature consistent with vacuum flange clamping hardware. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 is a Pfeiffer product route; the vacuum-shop alternate is a Pfeiffer Vacuum Components & Solutions shop page matching order number 120BSR040, manufacturer identity, DN 32-40 ISO-KF connection, and clamping-ring product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is locked to BOM item 42A and product 120BSR040, not to neighboring BOM rows that reference the same standard clamp."
  uncertainty_notes: []
mass:
  value_kg: 0.247
  basis: "The local row STEP measured one solid, volume 1014.188 mm^3, and bounding box about 6.20 x 45.00 x 15.30 mm, which appears to be an incomplete/simplified clamp feature rather than the full product. The BOM-route official 120BSR040 STEP download measured 8 solids, volume 30759.372 mm^3, surface area 20265.342 mm^2, and bounding box about 99.60 x 87.68 x 17.17 mm, consistent with the published 90 x 68 x 17 mm product dimensions. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.2470 kg per clamping ring. BOM quantity is 3, so row total is about 0.741 kg."
  source:
    url_or_path: "https://www.vacuum-shop.com/2075879/downloads/step/120BSR040.stp; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured the BOM-route official 120BSR040 STEP volume as 30759.372 mm^3. The Pfeiffer product page identifies material as stainless steel 1.4301/304 and lists dimensions A 90 mm, B 68 mm, C 17 mm. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 is a Pfeiffer product route; the vacuum-shop alternate and STEP download are Pfeiffer Vacuum Components & Solutions routes matching order number 120BSR040 and product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The official 120BSR040 STEP solid volume is used as the material-volume proxy for one complete clamping ring."
    - "The 304/1.4301 material stated by the BOM-provided product route is represented by the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "The result is CAD-volume-derived rather than a published catalog weight."
    - "The local row STEP appears incomplete for mass estimation, so the official product STEP from the BOM-provided route is used instead."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The Pfeiffer product page for order number 120BSR040 states material stainless steel 1.4301/304. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 is a Pfeiffer product route; the vacuum-shop alternate is a Pfeiffer Vacuum Components & Solutions shop page matching order number 120BSR040, manufacturer identity, DN 32-40 ISO-KF connection, and product description."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local assembly STEP material extractor returned only Generic with density 1000.0, so material is resolved from the BOM-provided product route instead."
how_to_make:
  summary: "Fabricate stainless 304 clamp body features, add hinge/tightening hardware, deburr/passivate or clean, and inspect DN 32-40 ISO-KF fit"
  manufacturing_steps:
    - "For local fabrication, start from stainless steel 304/1.4301 strip, sheet, or near-net blanks sized for the DN 32-40 ISO-KF clamp geometry."
    - "Form, stamp, or machine the curved clamping geometry and lug/handle features indicated by the CAD evidence."
    - "Add hinge and screw or wingnut tightening hardware, then deburr and clean or passivate for vacuum-service use."
    - "Inspect dimensions, flange fit, and tightening behavior against DN 32-40 ISO-KF elastomer-seal flange hardware."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0261_42A__views_2x2.png; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The local CAD preview shows a clamp/handle feature; the official product route identifies 120BSR040 as a stainless 304/1.4301 DN 32-40 ISO-KF clamping ring for elastomer seals with 2 N m wingnut torque. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 is a Pfeiffer product route; the vacuum-shop alternate is a Pfeiffer Vacuum Components & Solutions page matching order number 120BSR040 and row identity. targeted_web_search: searched \"120BSR040 weight kg\", \"120BSR040 clamping ring stainless steel 304 1.4301 manufacturing drawing\", and \"Pfeiffer 120BSR040 DN40 clamping ring material weight\" found product/spec/CAD evidence but no row-specific manufacturing process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The detailed local fabrication route is inferred from clamp geometry, stainless material, and common small stainless clamp production practice because the product sources do not state a manufacturing process."
  uncertainty_notes:
    - "Exact vendor production method, fastener subpart materials, surface finish, and inspection tolerances are not specified by the row evidence."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard ISO-KF vacuum clamp hardware rather than machine-specific custom geometry; decompose hinge/tightening subparts only if later KB work expands vacuum fitting manufacture."
---
