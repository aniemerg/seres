---
row_identity:
  item: "3M"
  cad_file: "3M_pipe_ISO_K_DN63_320RZS063_L_218"
  source_row_number: 124
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight ISO-K DN 63 vacuum pipe spool / full nipple connecting two ISO-K flanged vacuum components in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3M_pipe_ISO_K_DN63_320RZS063_L_218.step; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 124 identifies item 3M as Pfeiffer Vacuum product 320RZS063 with CAD file 3M_pipe_ISO_K_DN63_320RZS063_L_218. The CAD preview shows a straight hollow cylindrical tube with ISO-K style flanged ends and an about 218 mm overall length. official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 corresponds to Pfeiffer Vacuum product 320RZS063; the accessible Pfeiffer Vacuum online shop page on vacuum-shop.com lists 320RZS063 in the ISO-K Full Nipple family with DN 63 ISO-K connection, matching the row product ID and pipe-spool geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one straight DN 63 ISO-K full-nipple pipe spool; the CAD-specific L_218 name and measured 218 mm envelope are used for this row rather than the shorter catalog base length."
  uncertainty_notes:
    - "The BOM product ID is the base 320RZS063 while the row CAD name and geometry indicate a longer 218 mm spool; treat this as the same Pfeiffer ISO-K full-nipple family with row-specific length."
mass:
  value_kg: 1.633
  basis: "FreeCAD measured one CAD solid volume as 203434.224 mm^3. Using local stainless_steel_1_4301 density 8030 kg/m^3 gives 203434.224e-9 m^3 * 8030 kg/m^3 = 1.633 kg per pipe spool. BOM quantity is 1, so the row total is also about 1.633 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3M_pipe_ISO_K_DN63_320RZS063_L_218.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 203434.224 mm^3, area 119972.880 mm^2, and bounding box 218.00 x 105.13 x 105.13 mm. The local density table gives stainless_steel_1_4301 as 8030 kg/m^3. official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 maps to the accessible Pfeiffer Vacuum online shop page on vacuum-shop.com for the same product family, which states stainless steel 1.4301/304."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the per-unit metal volume for the physical row item."
    - "The Pfeiffer 320RZS063 family material applies to this CAD-specific longer spool variant."
  uncertainty_notes:
    - "CAD volume may omit very small weld-prep details, flange-face finish, or manufacturing tolerances, so the estimate is a planning mass rather than a catalog shipping weight."
material:
  primary_material: "stainless steel 1.4301 / AISI 304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official Pfeiffer Vacuum online shop page for 320RZS063 names the product 'Full nipple, stainless steel 1.4301/304' and lists the ISO-K Full Nipple subcategory as stainless steel 1.4301/304. official_alternate_route_check: BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063 identifies the same Pfeiffer product ID; the accessible vacuum-shop.com page is a Pfeiffer Vacuum Components & Solutions shop page and matches product ID 320RZS063."
    evidence_basis: "bom_provided"
  assumptions:
    - "The material stated for the Pfeiffer 320RZS063 DN 63 ISO-K full nipple family is used for this row-specific L_218 spool."
  uncertainty_notes:
    - "Assembly STEP material metadata for this CAD object is only 'Generic' at density 1000, so the usable material evidence comes from the row-matched Pfeiffer product route rather than embedded CAD material metadata."
how_to_make:
  summary: "Procure as a Pfeiffer ISO-K DN 63 stainless full nipple / pipe spool in the 320RZS063 family, or manufacture locally as a stainless 304/1.4301 vacuum tube with ISO-K DN 63 flange ends, then clean and leak-test for high-vacuum service."
  manufacturing_steps:
    - "Cut stainless 304/1.4301 tube stock or tube-plus-flange blanks to the row-specific 218 mm overall length envelope."
    - "Form or machine the ISO-K DN 63 flange lips and sealing-end features; join separate flange rings to the tube if the blank is not one-piece."
    - "Deburr, clean, and finish the bore and sealing faces for vacuum compatibility."
    - "Inspect ISO-K DN 63 interface dimensions and helium leak-test the finished spool."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3M_pipe_ISO_K_DN63_320RZS063_L_218.step; https://vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "Pfeiffer identifies the product family as a stainless 1.4301/304 full nipple with DN 63 ISO-K connection, and the CAD preview shows a straight hollow cylindrical spool with flanged ends and an about 218 mm envelope. targeted_web_search: searched 'Pfeiffer 320RZS063 manufacturing full nipple stainless steel 1.4301', '320RZS063 datasheet manufacturing', and 'ISO-K full nipple stainless steel manufacturing weld tube flange'; found row-matched product and dimension/material facts but no row-specific factory process description."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local route follows common vacuum hardware fabrication practice inferred from the product geometry and material, not a Pfeiffer-published process sheet."
    - "The row-specific length is manufactured as a longer straight spool within the same ISO-K DN 63 interface family."
  uncertainty_notes:
    - "Exact factory process details such as one-piece forming versus machined flange rings welded to tube are not resolved."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless ISO-K DN 63 straight full nipple / pipe spool with a length parameter or variant note, not as a reAM250-specific assembly."
---
