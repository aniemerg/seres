---
row_identity:
  item: "83"
  cad_file: "83_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 279
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "ISO-KF DN 32-40 clamping ring used to fasten an elastomer-sealed small-flange vacuum joint; the row quantity is 12 clamps."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; research/ream250_bom/ream250_bom_row_0279_83__views_2x2.png"
    cited_fact_or_basis: "BOM row 279 identifies item 83 as Pfeiffer Vacuum 120BSR040. The official shop route identifies 120BSR040 as a clamping ring for elastomer seals with connection flange DN 32-DN 40 ISO-KF and 2 Nm wingnut torque. The local contact sheet shows clamp/screw geometry. official_alternate_route_check: the BOM URL on pfeiffer-vacuum.com redirects or canonically corresponds to the official Pfeiffer/Busch shop route; vacuum-shop.com identifies Pfeiffer Vacuum Components & Solutions and the same product ID 120BSR040."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local per-row STEP export shows only a small subbody-like clamp feature, so the function is taken from the row-matched vendor product identity rather than the small local preview alone."
mass:
  value_kg: 0.247
  basis: "Per unit: vendor STEP volume 30759.372 mm^3 = 3.0759372e-5 m^3 multiplied by local stainless_steel_304 density 8030 kg/m^3 gives 0.246998 kg, rounded to 0.247 kg. BOM quantity is 12, so the row total is about 2.96 kg."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; /tmp/120BSR040.stp; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/83_clamping_ring_ISO_KF_DN40_120BSR040.step"
    cited_fact_or_basis: "The official shop page provides a 3D STEP download for row-matched product 120BSR040 and states stainless steel 1.4301/304. FreeCAD measured the downloaded product STEP as 8 solids, volume 30759.371872947188 mm^3, bounding box 99.60382945588033 x 87.67677092980742 x 17.169032225746005 mm. The local density table gives stainless_steel_304 density 8030 kg/m^3. The local row STEP measured 1014.1884788467468 mm^3 with a 6.20 x 45.00 x 15.30 mm bounding box, which appears incomplete for the full clamp. official_alternate_route_check: the BOM URL on pfeiffer-vacuum.com is the row link for 120BSR040; vacuum-shop.com is an official Pfeiffer Vacuum Components & Solutions shop route for the same product ID and provides the product STEP used for full-geometry mass."
    evidence_basis: "bom_provided"
  assumptions:
    - "The vendor STEP represents the full purchased 120BSR040 clamping ring, while the smaller local row STEP is treated as incomplete for mass."
    - "The stainless 304 density constant from kb/materials/properties.yaml is suitable for the vendor-stated stainless steel 1.4301/304."
  uncertainty_notes:
    - "The vendor page did not provide a catalog weight; mass is calculated from CAD volume and material density, so any hidden non-stainless hardware or STEP simplification would shift the estimate."
material:
  primary_material: "stainless steel 1.4301/304 clamping ring hardware"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official product route states material Stainless steel 1.4301/304 for 120BSR040. The local assembly material extractor found only Generic material with density 1000.0 for this CAD product, so that metadata is not used as the material source. official_alternate_route_check: the BOM URL identifies the same Pfeiffer product 120BSR040; the alternate official shop page is row-matched by product ID and official Pfeiffer Vacuum Components & Solutions shop identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source names the product material but does not separately describe the screw, hinge, or wingnut submaterials; all are modeled under the stainless 1.4301/304 hardware family unless later split data is found."
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 120BSR040, a standard ISO-KF DN 32-40 stainless clamping ring for elastomer-sealed vacuum joints."
  manufacturing_steps:
    - "Purchase or stock the row-matched Pfeiffer Vacuum 120BSR040 clamping ring."
    - "Install by placing it around the ISO-KF DN 32-40 elastomer-sealed flange joint and tightening the wingnut to the vendor-stated 2 Nm torque."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 279 specifies Pfeiffer Vacuum 120BSR040. The official shop route states it is suitable for elastomer seals, DN 32-DN 40 ISO-KF, and uses 2 Nm torque on the wingnut. official_alternate_route_check: vacuum-shop.com is an official Pfeiffer Vacuum Components & Solutions route for the same 120BSR040 product linked by the BOM-provided Pfeiffer URL."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "This is a procurement and installation route, not a locally sourced fabrication plan; detailed local manufacture of the clamp parts would need separate process modeling."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable standard ISO-KF DN 32-40 stainless clamping-ring hardware item rather than a calibrated purchased module; keep quantity separate in BOMs."
---

