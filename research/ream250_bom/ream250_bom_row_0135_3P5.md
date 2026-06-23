---
row_identity:
  item: "3P5"
  cad_file: "3P5_reduction_ISO_K_DN100_DN63_320RRK100-063-63"
  source_row_number: 135
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK100_063_63"
function:
  summary: "Conical ISO-K vacuum reducer that adapts a DN 100 ISO-K flange connection down to DN 63 ISO-K while preserving a vacuum-compatible flow path."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073087/product/320rrk10006363/reducing-piece-conical-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P5_reduction_ISO_K_DN100_DN63_320RRK100-063-63.step; research/ream250_bom/ream250_bom_row_0135_3P5__views_2x2.png"
    cited_fact_or_basis: "BOM row 135 gives product 320RRK100-063-63 from Pfeiffer Vacuum. The Pfeiffer shop route identifies it as a conical reducing piece with connection flange DN 100 ISO-K / DN 63 ISO-K and nominal diameter reduced DN 63 ISO-K. CAD preview shows a conical reducer body with two circular ISO-K flange ends. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK100_063_63 maps to the same product ID on Pfeiffer's global product route but the page reported product-load failure; the vacuum-shop.com page is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact/copyright, and matches product 320RRK100-063-63."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 1.06
  basis: "Per-unit mass for quantity 1. FreeCAD measured the row STEP as 1 solid with volume 131604.153 mm^3 and bounding box about 63.00 x 143.02 x 143.02 mm. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.000131604153 m^3 * 8030 kg/m^3 = 1.057 kg, rounded to 1.06 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P5_reduction_ISO_K_DN100_DN63_320RRK100-063-63.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073087/product/320rrk10006363/reducing-piece-conical-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured CAD volume 131604.153 mm^3. The Pfeiffer shop route states stainless steel 1.4301 (AISI 304) for media-contact material. Local density table gives stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK100_063_63 maps to the same product ID on Pfeiffer's global product route but the page reported product-load failure; the vacuum-shop.com page is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact/copyright, and matches product 320RRK100-063-63."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the shipped reducer body for one BOM-row unit."
    - "The reducer is treated as effectively all stainless steel 304/1.4301 for mass; no separate seals or clamps are included in this row."
  uncertainty_notes:
    - "CAD export material metadata was only Generic at density 1000 kg/m^3, so material identity comes from the row-matched Pfeiffer shop route rather than STEP metadata."
material:
  primary_material: "stainless steel 1.4301 / AISI 304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073087/product/320rrk10006363/reducing-piece-conical-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The Pfeiffer shop route title names stainless steel 304/1.4301 and the technical data says materials in contact with media are stainless steel 1.4301 (AISI 304). official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK100_063_63 maps to the same product ID on Pfeiffer's global product route but the page reported product-load failure; the vacuum-shop.com page is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact/copyright, and matches product 320RRK100-063-63."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Material is resolved for the reducer body/media-contact component; any separately purchased seals or clamps are outside this BOM row."
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 320RRK100-063-63, or model local production as a stainless 304 vacuum reducer made from ISO-K flange stock and a conical reducer shell with vacuum-clean finishing and leak checking."
  manufacturing_steps:
    - "Prepare stainless 304/1.4301 ISO-K DN100 and DN63 flange ends and conical reducer shell stock."
    - "Form or machine the conical transition and machine flange sealing and clamp-interface features to ISO-K geometry."
    - "Join the reducer shell to the flange ends, preferably with vacuum-compatible internal welds where geometry permits."
    - "Clean, passivate as needed, inspect dimensions and sealing faces, and helium leak test before installation."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073087/product/320rrk10006363/reducing-piece-conical-stainless-steel-1-4301-304.html; https://www.pfeiffervacuum.com/global/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3_2_materials/; research/ream250_bom/ream250_bom_row_0135_3P5__views_2x2.png"
    cited_fact_or_basis: "The row-matched shop page identifies a stainless 304/1.4301 ISO-K conical reducer. Pfeiffer vacuum-technology guidance says stainless steel is preferred for vacuum chambers/components and can be welded vacuum-tight. CAD preview shows a conical reducer with two flange ends. targeted_web_search: queries tried: 'Pfeiffer 320RRK100-063-63 manufacturing welded', 'Pfeiffer ISO-K conical reducer stainless 304 manufacturing', and 'vacuum conical reducer stainless steel welded'; no row-specific source stated the exact factory process, so detailed forming, machining, welding, finishing, and leak-test steps are inferred from the sourced geometry/material and vacuum-component practice."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Local production would be treated as fabrication of a simple vacuum piping component, not as a calibrated purchased subsystem."
    - "ISO-K sealing surfaces and flange interfaces require machining/inspection precise enough for vacuum service."
  uncertainty_notes:
    - "The exact Pfeiffer factory route is not sourced; local manufacturing steps are plausible process planning for KB modeling, not a vendor manufacturing specification."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless ISO-K conical reducer part rather than a machine-specific purchased module; seals and clamps should remain separate BOM rows when present."
---
