---
row_identity:
  item: "41C"
  cad_file: "41C_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 258
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "DN 32-40 ISO-KF stainless clamping ring used to tighten and secure an elastomer-sealed KF vacuum flange joint in the powder inlet area; BOM quantity is 2."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 258 identifies Pfeiffer Vacuum order number 120BSR040. The associated product page and datasheet identify 120BSR040 as a clamping ring for elastomer seals, DN 32-40 ISO-KF, suitable for elastomer seals. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 was blocked to direct curl, but the associated vacuum-shop product route and linked Pfeiffer datasheet match manufacturer Pfeiffer Vacuum, order number 120BSR040, product family, material, and DN 32-40 ISO-KF row identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is locked to BOM item 41C and product 120BSR040, not to the adjacent toothed-belt-pulley row mentioned in the raw row text."
  uncertainty_notes: []
mass:
  value_kg: 0.265
  basis: "FreeCAD measured one solid with volume 32971.270 mm^3, surface area 17328.748 mm^2, and bounding box about 101.47 x 16.00 x 72.81 mm. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.264759 kg per clamping ring. BOM quantity is 2, so row total is about 0.530 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41C_clamping_ring_ISO_KF_DN40_120BSR040.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/2075879/downloads/datasheets/Datasheet_120BSR040_en.pdf"
    cited_fact_or_basis: "FreeCAD measured CAD volume 32971.270 mm^3 for the row-specific STEP. The datasheet for 120BSR040 states material stainless steel 1.4301/304, and kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 was blocked to direct curl; the associated vacuum-shop datasheet route matches order number 120BSR040 and Pfeiffer Vacuum product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the material volume proxy for one complete clamp."
    - "The 304/1.4301 material stated by the BOM-provided product route is represented by the local stainless_steel_304 density."
  uncertainty_notes:
    - "No published catalog weight was found in the accessible product page or datasheet, so the mass is CAD-volume-derived rather than a vendor-weighed value."
    - "The assembly STEP material extractor returned only Generic with density 1000.0, which is treated as placeholder metadata and not used for mass."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://www.vacuum-shop.com/2075879/downloads/datasheets/Datasheet_120BSR040_en.pdf"
    cited_fact_or_basis: "The 120BSR040 datasheet states material stainless steel 1.4301/304 for the clamping ring. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 was blocked to direct curl; the associated vacuum-shop datasheet route matches order number 120BSR040, Pfeiffer Vacuum identity, DN 32-40 ISO-KF connection, and product description."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local assembly STEP material metadata was only Generic/1000.0 and therefore did not independently resolve material."
how_to_make:
  summary: "Treat as purchased Pfeiffer ISO-KF vacuum hardware for current KB modeling. A plausible local route is to fabricate stainless 304 clamp halves/ring geometry, add hinge and wingnut tightening features, deburr/passivate, and inspect DN 32-40 ISO-KF fit."
  manufacturing_steps:
    - "Procure as Pfeiffer Vacuum 120BSR040 or equivalent DN 32-40 ISO-KF stainless clamping ring where commercial vacuum hardware is allowed."
    - "For local fabrication, cut or stamp stainless 304/1.4301 strip or near-net blanks for the curved clamp band geometry."
    - "Form the clamp band into the KF profile and create hinge, lug, and tightening-feature geometry visible in the CAD preview."
    - "Machine or drill attachment features, fit screw/wingnut hardware, deburr and passivate or clean for vacuum service."
    - "Verify fit and tightening torque against DN 32-40 ISO-KF elastomer-seal flange hardware."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0258_41C__views_2x2.png; https://www.vacuum-shop.com/2075879/downloads/datasheets/Datasheet_120BSR040_en.pdf"
    cited_fact_or_basis: "The CAD preview shows a curved clamp with hinge/lug/tightening features; the datasheet identifies 120BSR040 as a stainless 304/1.4301 clamping ring for elastomer seal, DN 32-40 ISO-KF, with 2 N m wingnut torque. targeted_web_search: searched \"120BSR040 weight mass\", \"120BSR040 clamping ring stainless steel 304 1.4301 manufacturing drawing\", and \"Pfeiffer 120BSR040 DN 40 clamping ring material\"; found product/spec and datasheet evidence but no row-specific manufacturing process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed local fabrication operations are inferred from clamp geometry and common stainless vacuum-clamp production practice because the cited sources identify the product but do not specify manufacturing process."
    - "Purchased-module handling is preferred because this is standard commercial vacuum fastening hardware."
  uncertainty_notes:
    - "Exact production process, fastener subpart material, surface finish, and inspection plan are not specified by the row evidence."
kb_implications:
  - "item_granularity: purchased_module - standard commercial ISO-KF vacuum clamping hardware; model as a reusable purchased/imported clamp unless later KB work intentionally decomposes KF clamp rings, hinges, and tightening hardware."
---
