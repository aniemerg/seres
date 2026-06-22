---
row_identity:
  item: "3P7"
  cad_file: "3P7_reduction_ISO_K_DN63_KF_DN40"
  source_row_number: 137
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK063_040_63"
function:
  summary: "Pfeiffer Vacuum 320RRK063-040-63 conical reducing adapter that transitions one vacuum line interface from DN 63 ISO-K to DN 40 ISO-KF."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://vacuum-shop.com/shop/en_US/category/2072968/iso-k-kf-conical-adapter.html"
    cited_fact_or_basis: "BOM row 137 and the manifest identify item 3P7 as quantity 1 of 3P7_reduction_ISO_K_DN63_KF_DN40, product 320RRK063-040-63, manufacturer Pfeiffer Vacuum. The Pfeiffer Vacuum Online Shop category lists 320RRK063-040-63 under ISO-K/KF conical adapters with connection flange DN 63 ISO-K / DN 40 ISO-KF. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK063_040_63 resolves to a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, matches manufacturer, product ID, and the same DN 63 ISO-K / DN 40 ISO-KF interface."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.499
  basis: "Per-unit estimate for BOM quantity 1. FreeCAD measured volume 62170.859 mm^3, equal to 6.2170859e-5 m^3. Using the local stainless_steel_304 density constant of 8030 kg/m^3 gives 0.499232 kg, rounded to 0.499 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P7_reduction_ISO_K_DN63_KF_DN40.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2072968/iso-k-kf-conical-adapter.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 62170.859 mm^3, area 33261.079 mm^2, and bounding box 63.00 x 105.13 x 105.13 mm. The Pfeiffer Vacuum Online Shop row for 320RRK063-040-63 identifies the stainless version as stainless steel 1.4301/304. kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK063_040_63 resolves to a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, matches the same product ID and interface, and supplies the stainless material family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP solid is treated as the physical solid volume of one adapter."
    - "The local stainless_steel_304 density is used as the calculation constant for stainless steel 1.4301/304."
  uncertainty_notes:
    - "No catalog weight was found in the row evidence, so the estimate depends on the CAD solid representing the delivered adapter without omitted small geometry or simplification."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072968/iso-k-kf-conical-adapter.html"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop category groups order number 320RRK063-040-63 under the stainless steel 1.4301/304 ISO-K/KF conical adapter table for DN 63 ISO-K / DN 40 ISO-KF. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRK063_040_63 resolves to a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches the row manufacturer, product ID, and connection flange."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local assembly STEP material extractor returned only placeholder Generic material at density 1000.0, so the material value is taken from the row-matched Pfeiffer product route rather than STEP metadata."
how_to_make:
  summary: "Model as a stainless vacuum flange reducer: procure as standard Pfeiffer ISO-K/KF hardware, or locally fabricate by forming/machining a conical stainless adapter body with ISO-K and KF flange features, then clean and inspect for vacuum service."
  manufacturing_steps:
    - "Start from stainless steel 1.4301/304 tube, forged blank, or machined billet sized for the DN 63 ISO-K outer flange and DN 40 ISO-KF end."
    - "Turn or form the conical reducer body and machine the sealing and clamp-interface flange faces."
    - "Deburr and polish sealing-adjacent surfaces, then clean/passivate for vacuum-compatible stainless hardware."
    - "Inspect flange dimensions, sealing faces, concentricity, and leak-tightness before installation."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0137_3P7__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P7_reduction_ISO_K_DN63_KF_DN40.step; https://vacuum-shop.com/shop/en_US/category/2072968/iso-k-kf-conical-adapter.html"
    cited_fact_or_basis: "The rendered CAD contact sheet shows a one-piece conical reducer with two circular vacuum-flange ends. FreeCAD measured one solid with bounding box 63.00 x 105.13 x 105.13 mm. The Pfeiffer Vacuum Online Shop page identifies the row-matched product as a stainless ISO-K/KF conical adapter. targeted_web_search: tried 'Pfeiffer Vacuum 320RRK063-040-63 reduction ISO-K DN 63 KF DN 40 material weight' and reviewed the row-matched Pfeiffer product route; found material and interface facts, but no row-specific manufacturing process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route is inferred from the stainless material, vacuum-flange function, and one-piece conical CAD geometry."
    - "Vacuum service requires clean, burr-free, leak-tight sealing and clamp-interface surfaces."
  uncertainty_notes:
    - "The row evidence does not state Pfeiffer's actual production route, surface finish, or leak-test specification."
kb_implications:
  - "item_granularity: simple_part - standard one-piece stainless ISO-K/KF conical adapter; later KB modeling should map it to reusable vacuum flange adapter hardware rather than a reAM250-specific module."
---

Research result for the leased reAM250 BOM row.
