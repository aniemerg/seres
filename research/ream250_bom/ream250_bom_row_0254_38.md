---
row_identity:
  item: "38"
  cad_file: "38_T_pipe_ISO_K_DN63_320RTS063"
  source_row_number: 254
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTS063"
function:
  summary: "DN 63 ISO-K vacuum tee fitting that branches one ISO-K vacuum line into a perpendicular third DN63 port while preserving clamp/seal interfaces for the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/38_T_pipe_ISO_K_DN63_320RTS063.step; research/ream250_bom/ream250_bom_row_0254_38__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 254 identifies item 38 as Pfeiffer Vacuum product 320RTS063 named 38_T_pipe_ISO_K_DN63_320RTS063; the manifest maps the row to the matching STEP file. The Pfeiffer Vacuum Online Shop product page identifies 320RTS063 as a Tee, stainless steel 1.4301/304, with DN 63 ISO-K connection. FreeCAD measured one solid with bounding box about 176.00 x 140.57 x 105.13 mm, and the rendered contact sheet shows a three-port tee with ISO-style flanged ends. official_alternate_route_check: original BOM URL is the Pfeiffer product route for 320RTS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches order number 320RTS063 plus Global-No. 2000042718."
    evidence_basis: "bom_provided"
  assumptions:
    - "The three visible flanged ports are treated as vacuum plumbing interfaces, not as structural mounts."
  uncertainty_notes: []
mass:
  value_kg: 1.84
  basis: "Per-unit estimate for quantity 1. FreeCAD measured CAD volume 229667.765 mm^3 = 0.000229667765 m^3. Using kb/materials/properties.yaml stainless_steel_304 density 8030 kg/m^3 gives 0.000229667765 * 8030 = 1.844 kg, rounded to 1.84 kg. BOM quantity is 1, so the row total is also about 1.84 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/38_T_pipe_ISO_K_DN63_320RTS063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 229667.765 mm^3. The row-matched Pfeiffer Vacuum Online Shop page identifies product 320RTS063 as stainless steel 1.4301/304. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL is the Pfeiffer product route for 320RTS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches order number 320RTS063 and Global-No. 2000042718."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied single-solid CAD volume is used as the physical tee metal volume for one purchased item."
  uncertainty_notes:
    - "No catalog weight was found on the row-matched product page, so this is a CAD-volume-derived mass rather than a vendor-stated shipping or measured part weight."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html; .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step --product-name 38_T_pipe_ISO_K_DN63_320RTS063"
    cited_fact_or_basis: "The row-matched Pfeiffer Vacuum Online Shop page lists product 320RTS063 under Stainless steel 1.4301/304. Local assembly STEP material extraction for 38_T_pipe_ISO_K_DN63_320RTS063 returned only Generic material with density 1000.0, which is placeholder metadata and was not used to resolve material. official_alternate_route_check: original BOM URL is the Pfeiffer product route for 320RTS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches the same 320RTS063 tee row."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Best current route is procurement as Pfeiffer 320RTS063 or an equivalent DN63 ISO-K stainless tee; local manufacture would form or cut a 304/1.4301 stainless tee body, attach three ISO-K flange ends, finish sealing faces, clean for vacuum service, and leak-test."
  manufacturing_steps:
    - "Procure Pfeiffer 320RTS063 or equivalent DN63 ISO-K stainless tee for near-term modeling."
    - "For local manufacture, prepare 304/1.4301 stainless tube/tee stock and three compatible ISO-K DN63 flange ends."
    - "Join the perpendicular tee branch and flange ends with vacuum-compatible welding or formed pulled-port fabrication, then remove burrs and clean internal surfaces."
    - "Machine or finish seal-adjacent flange lips/faces, passivate or clean as required for vacuum plumbing, and leak-test the completed tee."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html; https://www.n-c.com/vacuum-flanges-fittings/tees/iso-k-iso-f; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/38_T_pipe_ISO_K_DN63_320RTS063.step"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop page identifies the row as a DN63 ISO-K stainless 1.4301/304 tee. Pfeiffer Vacuum+Fab Solutions states ISO-K/ISO-F tee fittings are made from 304 stainless steel pulled port tubing and ISO-K flanges, with full size tees offering three equal-size flanged connections. The CAD preview shows a three-port flanged tee. targeted_web_search: queries tried: '320RTS063 Pfeiffer T-piece DN63 ISO-K stainless steel 1.4301 weight', 'site:vacuum-shop.com 320RTS063 T-piece stainless steel 1.4301 304', and 'Pfeiffer ISO-K tee manufacturing 304 stainless pulled port tubing'; found row-matched product/material/dimension facts and a Pfeiffer family manufacturing description, but no product-specific factory traveler for 320RTS063."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed welding, flange finishing, cleaning, and leak-test steps are inferred as a plausible local manufacturing route for a vacuum-rated stainless tee."
  uncertainty_notes:
    - "The exact Pfeiffer production sequence for order number 320RTS063 is not published in the sources checked."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable standard DN63 ISO-K stainless tee fitting rather than a reAM250-specific custom part or calibrated purchased module."
---
