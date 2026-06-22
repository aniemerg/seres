---
row_identity:
  item: "89"
  cad_file: "89_clamping_ring_ISO_KF_DN16"
  source_row_number: 285
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR016"
function:
  summary: "DN 10-16 ISO-KF stainless clamping ring for fastening an elastomer-sealed small-flange vacuum joint; BOM quantity is 1."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv"
    cited_fact_or_basis: "BOM row 285 and the manifest identify item 89 as Pfeiffer Vacuum 120BSR016, CAD file 89_clamping_ring_ISO_KF_DN16, one matched_existing vendor_component. The official Pfeiffer shop route identifies 120BSR016 as a clamping ring for elastomer seals with connection flange DN 10-16 ISO-KF and torque 2 Nm on the wingnut. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR016; alternate URL https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details, and matches row product ID 120BSR016."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is locked to Pfeiffer 120BSR016, not to adjacent ISO-KF clamp variants."
  uncertainty_notes: []
mass:
  value_kg: 0.163
  basis: "The official product page links a vendor 3D STEP for 120BSR016. FreeCAD measured that full-scale vendor STEP as 8 solids with volume 20303.170 mm^3 and bounding box about 71.60 x 73.22 x 17.17 mm. Using the local stainless_steel_304 density 8030 kg/m^3 gives 0.163033 kg per clamping ring. BOM quantity is 1, so the row total is also about 0.163 kg."
  source:
    url_or_path: "https://www.vacuum-shop.com/2074846/downloads/step/120BSR016.stp; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; kb/materials/properties.yaml"
    cited_fact_or_basis: "Vendor STEP from the official Pfeiffer shop route measured 20303.170 mm^3, 15020.628 mm^2 surface area, and 71.60 x 73.22 x 17.17 mm bounding box in FreeCAD. The same product route states material stainless steel 1.4301/304. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR016; alternate URL https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html is the Pfeiffer Vacuum Online Shop page for product 120BSR016 and links the measured STEP file."
    evidence_basis: "bom_provided"
  assumptions:
    - "The vendor STEP solid volume represents the complete physical clamp item, including clamp body and tightening hardware, for one purchased unit."
    - "The stainless steel 1.4301/304 product material is represented by the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "The local row STEP is a simplified or normalized 10.00 x 1.00 x 10.00 mm ring with volume 52.011 mm^3, so it was used only for shape confirmation; the mass estimate uses the full-scale vendor STEP linked from the row-matched product route."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The row-matched Pfeiffer shop page for order number 120BSR016 states the material as stainless steel 1.4301/304. Local assembly STEP material extraction returned only Generic with density 1000.0, which is placeholder metadata and is not used as material evidence. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR016; alternate URL https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html is branded Pfeiffer Vacuum Online Shop and matches the same product ID."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Treat as standard purchased ISO-KF vacuum clamp hardware for current KB modeling. A plausible local route would form or machine the stainless clamp body geometry, add the wingnut/bolt tightening hardware, deburr/passivate, and inspect fit on DN 10-16 ISO-KF flanges."
  manufacturing_steps:
    - "Procure or cut stainless 304/1.4301 blanks for the clamp body and tightening hardware."
    - "Form, stamp, or machine the curved clamp-body profile and hinge/lug features visible in the vendor/local CAD previews."
    - "Machine, drill, and thread the bolt or wingnut interface, then assemble the clamp body with the tightening hardware."
    - "Deburr, clean or passivate for vacuum service, and verify DN 10-16 ISO-KF fit and wingnut torque behavior."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0285_89__views_2x2.png; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr016/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The rendered local CAD preview shows a thin annular clamp-like ring; the official product route identifies the item as a stainless 304/1.4301 DN 10-16 ISO-KF clamping ring for elastomer seals with a wingnut torque specification. targeted_web_search: searched '120BSR016 weight mass Pfeiffer clamping ring', '120BSR016 manufacturing clamping ring stainless steel 304 ISO-KF', and 'ISO-KF clamping ring manufacturing stainless steel wingnut'; results found row-matched product/spec pages and generic ISO-KF clamp references but no row-specific supplier manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The production route is inferred from standard stainless clamp geometry and common small vacuum-hardware fabrication practice because the supplier does not state its manufacturing process."
    - "Purchased standard hardware is the preferred current model unless later KB work needs to decompose reusable ISO-KF clamp manufacture."
  uncertainty_notes:
    - "Exact factory process, fastener subpart details, surface finish, and inspection tolerances are not specified by row evidence."
kb_implications:
  - "item_granularity: simple_part - standard ISO-KF stainless vacuum clamp hardware; later KB work should map it to a reusable standard clamp/fastener item rather than a machine-specific module."
---
