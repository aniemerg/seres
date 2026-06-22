---
row_identity:
  item: "42B"
  cad_file: "42B_clamp_ISO_K_DN100_320BKL250"
  source_row_number: 262
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250"
function:
  summary: "ISO-K stainless bracket screw / claw clamp used to clamp DN 63 to DN 250 ISO-K vacuum flanges with metal or elastomer seals; in this row it is associated with valve sv04_din_cc_dn40_- mounting hardware."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250; https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42B_clamp_ISO_K_DN100_320BKL250.step; research/ream250_bom/ream250_bom_row_0262_42B__views_2x2.png"
    cited_fact_or_basis: "BOM row 262 names Pfeiffer Vacuum 320BKL250. The official shop route identifies 320BKL250 as a bracket screw for ISO-K / ISO-F fastening elements, suitable for metal and elastomer seals, with DN 63-DN 250 ISO-K connection flange and 12-16 Nm torque. CAD preview shows a threaded cylindrical screw section joined to a stepped claw block. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com/global/de/shop/products/320BKL250; vacuum-shop.com page is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Copyright Pfeiffer Vacuum, and matches row product ID 320BKL250."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM description appends valve sv04_din_cc_dn40_-, so this row is treated as clamp hardware installed near that valve rather than as part of the valve body."
mass:
  value_kg: 0.0676
  basis: "Per-unit estimate from FreeCAD volume 8445.202 mm3 = 8.445202e-6 m3 for the row STEP solid, multiplied by local kb/materials/properties.yaml generic stainless_steel density 8000 kg/m3. Result is 0.06756 kg, rounded to 0.0676 kg per bracket screw. BOM quantity is 8, giving an optional row total of about 0.541 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42B_clamp_ISO_K_DN100_320BKL250.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 8445.201669 mm3 and bounding box about 61.50 x 23.06 x 14.95 mm. The shop page identifies the row product as stainless steel bracket screw 320BKL250. The local density table gives stainless_steel density 8000 kg/m3. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com/global/de/shop/products/320BKL250; vacuum-shop.com is an official Pfeiffer Vacuum online shop/contact route matching product ID 320BKL250."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid represents one complete physical bracket screw/claw clamp and its volume is treated as solid stainless steel for planning mass."
  uncertainty_notes:
    - "Assembly STEP material metadata for this product returned only Generic at density 1000 kg/m3, so it was ignored per the placeholder-material rule."
    - "Thread-root detail and vendor CAD simplification may shift actual purchased mass slightly, but the estimate is within the intended coarse BOM planning precision."
material:
  primary_material: "stainless steel bracket screw/claw clamp; product title specifies stainless steel 1.4401/316, while technical data lists media-contacting material as stainless steel 1.4404 (AISI 316L)"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250; https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row names manufacturer Pfeiffer Vacuum and product ID 320BKL250. The official shop route titles the product bracket screw, stainless steel 1.4401/316, and its technical data says materials in contact with media are stainless steel 1.4404 (AISI 316L). Local assembly material extraction found only Generic and density 1000 kg/m3 for this product, so it did not resolve material. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com/global/de/shop/products/320BKL250; vacuum-shop.com is branded Pfeiffer Vacuum Online Shop and matches product ID 320BKL250."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source exposes two closely related stainless specifications: product category/title 1.4401/316 and media-contacting 1.4404/316L. Later KB modeling should preserve this as stainless 316-family hardware unless a vendor drawing resolves the exact alloy for every feature."
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 320BKL250 bracket screw where possible; a local manufacturing approximation is machined stainless 316-family hardware with an M10 threaded screw section and milled claw block geometry, then passivated/cleaned for vacuum service."
  manufacturing_steps:
    - "Cut stainless 316-family bar or billet stock sized for the screw and claw body."
    - "Turn the cylindrical screw section and cut or roll the M10 thread."
    - "Mill the stepped claw/block faces and flange-contact geometry shown in CAD."
    - "Deburr, passivate or clean for vacuum service, then inspect fit against DN 63-DN 250 ISO-K flange hardware and torque range."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42B_clamp_ISO_K_DN100_320BKL250.step; research/ream250_bom/ream250_bom_row_0262_42B__views_2x2.png"
    cited_fact_or_basis: "Source identifies the purchased product as stainless bracket screw 320BKL250 for ISO-K fastening and gives M10 and 61.5 mm dimension. CAD/preview shows a threaded cylinder and machined-looking claw block. targeted_web_search: queries tried 'Pfeiffer Vacuum 320BKL250 clamp ISO-K DN100 material weight' and 'site:pfeiffer-vacuum.com 320BKL250 Pfeiffer bracket screw stainless steel 1.4401'; these found the official/product route but no row-specific manufacturing-process statement, so the detailed local machining route is inferred."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local route prioritizes a plausible small-batch manufacturing approximation, not the vendor's actual production route."
  uncertainty_notes:
    - "Vendor procurement is the highest-confidence route; manufacturing operations are inferred from geometry and standard stainless threaded clamp hardware practice."
kb_implications:
  - "item_granularity: simple_part - model as reusable stainless ISO-K bracket screw/claw clamp hardware, not as a purchased module; use quantity-specific BOM rows to capture how many clamps are needed around each vacuum flange or valve."
---

