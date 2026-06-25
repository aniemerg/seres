---
row_identity:
  item: "3N2"
  cad_file: "3N2_end_piece_320SWN063"
  source_row_number: 126
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "ISO-K DN 63 stainless end piece/flange for a Pfeiffer flexible vacuum hose or spring-bellows run; it provides the rigid circular connection face at the hose end for sealing and clamping into the vacuum line."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0126_3N2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row 126 identifies item 3N2 as quantity 2, cad file 3N2_end_piece_320SWN063, description '320SFK063: end piece', manufacturer Pfeiffer Vacuum. CAD preview shows a stepped annular end fitting with a through bore. The BOM-provided Pfeiffer product route identifies 320SFK063-130 as DN 63 ISO-K spring bellows with flange connection length 30 mm. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum shop URL; vacuum-shop.com is a Pfeiffer Vacuum online shop page for the same 320SFK063-130 order number and product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is one end fitting from the associated flexible hose/bellows assembly rather than the complete 320SFK063-130 product."
  uncertainty_notes:
    - "The CAD export is a single vendor-component solid for the end piece, so it resolves shape/function better than internal manufacturing detail."
mass:
  value_kg: 0.412
  basis: "Per-unit estimate from FreeCAD STEP volume 51352.068 mm^3 = 5.1352068e-5 m^3 multiplied by local stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml, giving 0.4124 kg. BOM quantity is 2, so row total is about 0.825 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3N2_end_piece_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073103/iso-k-corrugated-hose-flexible.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 51352.06790278328 mm^3 and bounding box about 35.29 x 105.13 x 105.13 mm. Pfeiffer's corrugated-hose family page for 320SWN063 lists flange material as stainless steel 1.4301/304 and bellows as 316L; the local density table gives stainless_steel_304 as 8030 kg/m^3. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum shop URL for the linked 320SFK063-130 family; the opened Pfeiffer Vacuum online shop route also exposes the closely named 320SWN063 DN 63 ISO-K flexible hose family that matches the CAD filename."
    evidence_basis: "bom_provided"
  assumptions:
    - "The end piece volume is treated as stainless steel 304/1.4301 because the CAD preview is the rigid flange/end fitting, not the bellows wall."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only Generic with density 1000 kg/m^3, so material identity comes from the BOM-linked Pfeiffer product family rather than row-specific STEP metadata."
material:
  primary_material: "stainless steel 1.4301/304 for the rigid flange/end piece"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073103/iso-k-corrugated-hose-flexible.html; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Pfeiffer's DN 63 ISO-K corrugated-hose family lists flange material as stainless steel 1.4301/304 and bellows as 316L; the BOM-linked 320SFK063-130 spring-bellows page lists material as stainless steel with flange 304 and bellows 316L. Local STEP material extraction for 3N2 found only Generic, so it does not resolve material. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum shop URL for 320SFK063-130; vacuum-shop.com is a Pfeiffer Vacuum online shop route with matching order/product-family facts."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row is named end piece and the CAD preview is the rigid end fitting, the flange material applies more directly than the bellows material."
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material was present; if the CAD end piece includes any hidden weld collar or insert, the simple material assignment may miss a minor second alloy."
how_to_make:
  summary: "A machined stainless ISO-K end fitting joined to the corrugated hose or bellows assembly and leak-tested"
  manufacturing_steps:
    - "Local fabrication route: cut stainless 304/1.4301 round stock or tubing blank, turn the stepped ISO-K flange/end geometry, bore the central opening, deburr and clean for vacuum service."
    - "Join to the stainless bellows or corrugated hose body by vacuum-compatible welding, then helium leak-test and inspect sealing faces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0126_3N2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row marks this as a Pfeiffer Vacuum vendor component linked to 320SFK063-130. The Pfeiffer route provides a purchasable DN 63 ISO-K stainless bellows/flexible connector with 3D STEP download; CAD preview of the row shows a turned annular end fitting. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum shop URL; vacuum-shop.com is a Pfeiffer Vacuum online shop route for the same order number and product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The Manufacturing route is secondary"
  uncertainty_notes:
    - "The source package does not state the exact factory process sequence for this individual end piece."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless ISO-K DN 63 hose/bellows end fitting or flange-end simple part; keep the complete flexible hose/bellows as a separate purchased module if modeled later."
---
