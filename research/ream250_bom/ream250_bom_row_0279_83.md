---
row_identity:
  item: "83"
  cad_file: "83_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 279
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "ISO-KF DN 32-DN 40 clamping ring used to mechanically close matching small-flange vacuum hardware around an elastomer seal; the reAM250 BOM row uses quantity 12 of this standard clamp."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0279_83__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 279 identifies item 83 as quantity 12 of Pfeiffer Vacuum product 120BSR040 with CAD file 83_clamping_ring_ISO_KF_DN40_120BSR040. The manifest maps the row to a matched vendor-component STEP file. The row contact sheet shows a narrow clamp screw/handle or hinge-side subfeature. The BOM-provided Pfeiffer URL redirects to the official Busch Group shop page for order number 120BSR040, titled as a stainless steel 304/1.4301 DN 32-DN 40 ISO-KF clamping ring for elastomer seals. The official Pfeiffer vacuum-shop page for the same order number states it is suitable for elastomer seals. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirects to https://www.shop.buschgroup.com/global/en/products/120BSR040/ with Busch Group and Pfeiffer branding; the vacuum-shop alternate lists Pfeiffer Vacuum Components & Solutions GmbH contact information and matches order number 120BSR040."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is locked to BOM item 83 and product 120BSR040; neighboring BOM rows that reference the same commercial clamp are not separate product identities."
  uncertainty_notes:
    - "The local per-row STEP preview is an incomplete subfeature, so function is resolved from the row-matched product identity and official product route rather than from the local geometry alone."
mass:
  value_kg: 0.247
  basis: "Per-unit estimate for one physical clamping ring. The local row STEP measured one solid, volume 1014.188 mm^3, surface area 855.769 mm^2, and bounding box about 6.20 x 45.00 x 15.30 mm, which is too small for the full DN 32-DN 40 clamp. The BOM-route official 120BSR040 STEP download measured 8 solids, volume 30759.372 mm^3, surface area 20265.342 mm^2, and bounding box about 99.60 x 87.68 x 17.17 mm, consistent with the vendor dimensions A 90 mm, B 68 mm, C 17 mm. Converting 30759.372 mm^3 to 3.0759372e-5 m^3 and multiplying by the local stainless_steel_304 density 8030 kg/m^3 gives 0.246998 kg, rounded to 0.247 kg per clamp. BOM quantity is 12, so row total is about 2.96 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/83_clamping_ring_ISO_KF_DN40_120BSR040.step; https://www.vacuum-shop.com/2075879/downloads/step/120BSR040.stp; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured the local row STEP as volume 1014.188 mm^3 and bounding box 6.20 x 45.00 x 15.30 mm. FreeCAD measured the official row-matched 120BSR040 STEP as 8 solids, volume 30759.372 mm^3, surface area 20265.342 mm^2, and bounding box 99.60 x 87.68 x 17.17 mm. The official product page identifies material as stainless steel 1.4301/304 and lists dimensions A 90 mm, B 68 mm, C 17 mm. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 is a Pfeiffer product route; vacuum-shop.com is an official Pfeiffer Vacuum Components & Solutions route for the same order number and provides the product STEP used for full-geometry mass."
    evidence_basis: "bom_provided"
  assumptions:
    - "The official 120BSR040 STEP solid volume is used as the material-volume proxy for one complete clamping ring because the local row STEP is a partial exported subfeature."
    - "The local stainless_steel_304 density constant is appropriate for vendor-stated stainless steel 1.4301/304."
  uncertainty_notes:
    - "The mass is CAD-volume-derived rather than a published catalog weight."
    - "If the official STEP omits small hardware details or represents simplified solids, the calculated mass will shift accordingly."
material:
  primary_material: "stainless steel 1.4301/304 clamping ring hardware"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided Pfeiffer URL redirects to the official Busch Group product page titled as stainless steel 304/1.4301 for order number 120BSR040. The official Pfeiffer vacuum-shop page for the same order number lists Material Stainless steel 1.4301/304. The local assembly STEP material extractor returned material Generic with density 1000.0 for this product, so that placeholder metadata is not used as material evidence. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirects to the official Busch/Pfeiffer shop route; the vacuum-shop alternate lists Pfeiffer Vacuum Components & Solutions GmbH and matches product ID 120BSR040."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source names the product material but does not separately describe hinge, screw, or wingnut submaterials; this row-level result keeps them within the stainless 1.4301/304 hardware family unless later split data is found."
how_to_make:
  summary: "Use Pfeiffer Vacuum 120BSR040 or a compatible DN 32-DN 40 ISO-KF stainless clamping ring; for local closure, model it as a simple stainless clamp made by forming or machining the clamp body, adding hinge and wingnut-side tightening hardware, cleaning/passivating, and verifying ISO-KF fit and 2 Nm wingnut tightening."
  manufacturing_steps:
    - "Local fabrication route: start from stainless steel 304/1.4301 strip, sheet, or near-net blanks sized for the DN 32-DN 40 ISO-KF clamp geometry."
    - "Form, stamp, or machine the curved clamp body and lug/hinge/tightening features indicated by the product CAD and local row preview."
    - "Add hinge and screw or wingnut tightening hardware, then deburr, clean, and passivate stainless surfaces for vacuum-service use."
    - "Inspect flange fit, clamp closure, surface condition, and tightening behavior against the vendor-stated 2 Nm wingnut torque."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0279_83__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The official product route identifies 120BSR040 as a purchasable DN 32-DN 40 ISO-KF stainless clamping ring for elastomer seals and states 2 Nm torque on the wingnut. The CAD preview shows a clamp screw/handle or hinge-side feature, while the official STEP gives the complete clamp geometry. targeted_web_search: searched \"120BSR040 clamping ring stainless steel 304 1.4301 manufacturing drawing\", \"Pfeiffer 120BSR040 DN40 clamping ring material weight\", and \"ISO-KF DN40 clamping ring stainless steel manufacturing\" results found official product/spec/CAD evidence and generic ISO-KF clamp information but no row-specific manufacturing process sheet. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirects to the official Busch/Pfeiffer route for order number 120BSR040; vacuum-shop.com is an official Pfeiffer Vacuum Components & Solutions route matching the same row identity."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The detailed inferred from clamp geometry, stainless material, and ordinary small stainless clamp production practice because the official product evidence supports product identity and installation facts, not the factory process."
  uncertainty_notes:
    - "Exact vendor production tooling, hinge pin construction, thread specification, surface finish, and inspection tolerances are not resolved in this row-level pass."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard ISO-KF stainless vacuum fastening hardware; keep DN size, stainless grade, hinge/wingnut tightening, cleaning, and torque requirements as parameters or notes rather than decomposing it into a complex module."
---
