---
row_identity:
  item: "3I"
  cad_file: "3I_pipe_ISO_K_DN63_320RZS063-176"
  source_row_number: 120
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight DN 63 ISO-K vacuum full nipple/spool that provides a rigid 176 mm stainless pipe section between ISO-K vacuum flanges in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3I_pipe_ISO_K_DN63_320RZS063-176.step; https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 120 identifies item 3I, quantity 7, product 320RZS063, manufacturer Pfeiffer Vacuum, and CAD file 3I_pipe_ISO_K_DN63_320RZS063-176. The row STEP/contact sheet shows one straight flanged tube with a 176 mm x about 95 mm x 95 mm bounding box. The official Pfeiffer shop page for 320RZS063-176 identifies the item as a full nipple with DN 63 ISO-K connection flange and length 176 mm. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the row-specific official shop page is on vacuum-shop.com, carries Pfeiffer Vacuum copyright/contact details, and matches the row product family plus CAD-specific 320RZS063-176/176 mm identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD suffix -176 selects the 176 mm variant of the BOM product family 320RZS063."
  uncertainty_notes: []
mass:
  value_kg: 1.401
  basis: "FreeCAD measured CAD solid volume 174498.270 mm^3, rounded to 174498.270 mm^3. Using stainless steel 304 / 1.4301 density 8030 kg/m^3 from kb/materials/properties.yaml gives 174498.270e-9 m^3 * 8030 kg/m^3 = 1.401 kg per nipple. BOM quantity is 7, so the row total is about 9.81 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3I_pipe_ISO_K_DN63_320RZS063-176.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD read one solid from the row STEP and measured volume 174498.27033717747 mm^3 with bounding box 176.0 mm x 105.13275441440022 mm x 105.13275441440022 mm. The official Pfeiffer shop page identifies materials in contact with media as stainless steel 1.4301 (AISI 304). kb/materials/properties.yaml gives stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the vacuum-shop.com page is an official Pfeiffer Vacuum shop route and matches product 320RZS063-176, DN 63 ISO-K, and length 176 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents one physical row item and includes the flanged tube geometry needed for mass estimation."
  uncertainty_notes:
    - "Mass is CAD-derived rather than a catalog shipping or net-weight value; small deviations are possible if the supplied STEP omits manufacturing details or final surface finish."
material:
  primary_material: "Stainless steel 1.4301 / AISI 304 for media-contacting full nipple body."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official Pfeiffer shop page for 320RZS063-176 states materials in contact with media are stainless steel 1.4301 (AISI 304). Local assembly STEP material extraction for 3I_pipe_ISO_K_DN63_320RZS063-176 returned only Generic with density 1000.0, which is a placeholder and was not used to resolve material. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the alternate vacuum-shop.com route is an official Pfeiffer Vacuum shop page and row-matches product 320RZS063-176."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source specifies media-contacting material; it does not separately state whether any non-wetted surface treatment or marking material exists."
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 320RZS063-176 full nipple, then clean, inspect, and install with compatible DN 63 ISO-K seals and clamps."
  manufacturing_steps:
    - "Order or inventory the row-matched Pfeiffer Vacuum 320RZS063-176 full nipple."
    - "Verify DN 63 ISO-K interfaces, 176 mm length, cleanliness, and absence of flange or tube damage before installation."
    - "Install between matching ISO-K flanges using the separate centering ring/seal and clamp hardware required by the adjacent assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 120 provides the manufacturer and product route. The official Pfeiffer shop page lists 320RZS063-176 as a purchasable full nipple with DN 63 ISO-K connection flange, delivery-time/shop information, and downloadable data sheet/CAD. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the vacuum-shop.com page is an official Pfeiffer Vacuum shop page matching the row-specific 320RZS063-176 variant."
    evidence_basis: "bom_provided"
  assumptions:
    - "For this BOM research row, procurement is the appropriate route because the row is a named Pfeiffer Vacuum catalog component."
  uncertainty_notes: []
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable standard DN 63 ISO-K stainless vacuum nipple/spool, not a machine-specific custom assembly or calibrated module."
---
