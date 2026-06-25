---
row_identity:
  item: "3J"
  cad_file: "3J_pipe_ISO_K_DN63_320RZS063"
  source_row_number: 121
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight ISO-K DN 63 full nipple / vacuum pipe spool connecting two ISO-K flanged vacuum components in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3J_pipe_ISO_K_DN63_320RZS063.step; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 121 identifies Pfeiffer Vacuum product 320RZS063; CAD preview shows a straight hollow tube with ISO-K flanges at both ends; official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 corresponds to Pfeiffer Vacuum product 320RZS063, while the accessible Pfeiffer Vacuum online shop page on vacuum-shop.com lists 320RZS063 as a 'Full nipple' with connection flange DN 63 ISO-K, matching the BOM product ID and CAD geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one straight full nipple; BOM quantity 2 means two identical pieces."
  uncertainty_notes: []
mass:
  value_kg: 0.914
  basis: "FreeCAD measured one CAD solid volume as 113870.559 mm^3. Using local stainless_steel_1_4301 density 8030 kg/m^3 gives 113870.559e-9 m^3 * 8030 kg/m^3 = 0.914 kg per full nipple. BOM quantity is 2, so the row total is about 1.83 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3J_pipe_ISO_K_DN63_320RZS063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 113870.559 mm^3, area 60263.770 mm^2, and bounding box 88.00 x 105.13 x 105.13 mm. The local density table gives stainless_steel_1_4301 as 8030 kg/m^3. official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 maps to the accessible Pfeiffer Vacuum online shop page on vacuum-shop.com for the same product ID 320RZS063, which states stainless steel 1.4301/AISI 304 and length 88 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the per-unit metal volume for the physical row item."
  uncertainty_notes:
    - "CAD volume may omit very small chamfers, weld-prep details, or surface finish effects, so the estimate is best used as an approximate per-unit planning mass."
material:
  primary_material: "stainless steel 1.4301 / AISI 304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The official Pfeiffer Vacuum online shop page for 320RZS063 names the product 'Full nipple, stainless steel 1.4301/304' and lists media-contact material as stainless steel 1.4301 (AISI 304). official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 identifies the same Pfeiffer product ID; the accessible vacuum-shop.com page is a Pfeiffer Vacuum Components & Solutions shop page and matches product ID 320RZS063."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Assembly STEP material metadata for this CAD object is only 'Generic' at density 1000, so the usable material evidence comes from the row-matched Pfeiffer product route rather than embedded CAD material metadata."
how_to_make:
  summary: "Prepare as a standard Pfeiffer 320RZS063 ISO-K DN 63 full nipple, or manufacture locally as a stainless 304/1.4301 vacuum tube with two ISO-K flange ends, weld/braze or form the tube-flange geometry, then finish and leak-test for high-vacuum service"
  manufacturing_steps:
    - "Cut stainless 304/1.4301 tube stock to the 88 mm overall length envelope for DN 63 ISO-K geometry."
    - "Form or machine the ISO-K flange lips/end features and join them to the tube if made from separate flange rings."
    - "Deburr and clean the internal bore and sealing faces for vacuum compatibility."
    - "Leak-test and inspect the finished spool against ISO-K DN 63 interface dimensions."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3J_pipe_ISO_K_DN63_320RZS063.step; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "Pfeiffer identifies the row product as a stainless 1.4301/304 full nipple with DN 63 ISO-K connection and 88 mm length; CAD preview shows a straight hollow cylindrical spool with flanged ends. targeted_web_search: searched 'Pfeiffer 320RZS063 manufacturing full nipple stainless steel 1.4301' and '320RZS063 datasheet manufacturing' and found row-matched product/datasheet facts but no row-specific manufacturing process description."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common vacuum hardware fabrication practice inferred from the product geometry and material, not a Pfeiffer-published process sheet."
  uncertainty_notes:
    - "Exact factory process details such as deep drawing versus machined flange rings plus welded tube are not resolved."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless ISO-K DN 63 straight full nipple / pipe spool rather than a reAM250-specific assembly."
---

