---
row_identity:
  item: "3Q3"
  cad_file: "3Q3_seal_ISO_K_DN100_311ZRA100"
  source_row_number: 140
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA100"
function:
  summary: "DN 100 ISO-K centering ring with an outer ring and elastomer O-ring; it centers and seals ISO-K/ISO-F vacuum flange joints in the reAM250 vacuum hardware."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073005/product/311zra100/centering-ring-with-outer-ring-aluminum.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q3_seal_ISO_K_DN100_311ZRA100.step; research/ream250_bom/ream250_bom_row_0140_3Q3__views_2x2.png"
    cited_fact_or_basis: "The BOM row identifies item 3Q3 as Pfeiffer Vacuum product 311ZRA100. The official product route names 311ZRA100 as a centering ring with outer ring, aluminum, for connection flange DN 100 ISO-K and lists dimensions A=102 mm, B=100 mm, C=3.9 mm, D=8 mm, E=5.33 mm. The CAD contact sheet shows a thin annular seal/centering-ring geometry. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer, exact order number 311ZRA100, and Global-No. 2000042347."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one complete centering-ring seal item, while the BOM quantity is 2 units."
  uncertainty_notes:
    - "The CAD preview supports annular shape only; it does not show the exact reAM250 flange joints where the two units are installed."
mass:
  value_kg: 0.0177
  basis: "Per unit estimate: FreeCAD measured one-solid STEP volume 8060.704 mm^3, or 8.061 cm^3. With sourced aluminum outer ring plus NBR O-ring materials but no split-volume data, an effective density of about 2.2 g/cm^3 gives about 17.7 g per centering ring. If the whole CAD volume were aluminum, the upper calculation is about 0.0218 kg using 2700 kg/m^3; if all NBR, the lower calculation is about 0.00887 kg using 1100 kg/m^3. BOM quantity is 2, giving an optional row planning total of about 0.0355 kg at the selected per-unit estimate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q3_seal_ISO_K_DN100_311ZRA100.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073005/product/311zra100/centering-ring-with-outer-ring-aluminum.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 8060.704 mm^3, area 8996.501 mm^2, and bounding box 120.63 x 120.63 x 8.00 mm for the row STEP. The local density table lists aluminum at 2700 kg/m^3 and NBR at 1100 kg/m^3. The official product route identifies aluminum outer ring and NBR O-ring but does not provide catalog mass or material volume fractions. targeted_web_search: queries tried: '311ZRA100 weight', '311ZRA100 Mass', 'Datasheet_311ZRA100_en.pdf Weight', and '311ZRA100 kg'; result: no row-matched catalog mass found, only dimensions/material listings."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The vendor CAD solid volume is a usable volume proxy for one complete item."
    - "A 2.2 g/cm^3 effective density is used because the item is a mixed aluminum/NBR ring and the metal outer ring appears to dominate the visible CAD volume."
  uncertainty_notes:
    - "Mass uncertainty is mainly from the unknown aluminum-to-NBR volume split; the plausible bound from local densities is roughly 0.009 to 0.022 kg per unit."
material:
  primary_material: "Aluminum outer ring with NBR O-ring"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073005/product/311zra100/centering-ring-with-outer-ring-aluminum.html; https://vacuum-shop.com/2073923/downloads/datasheets/Datasheet_311ZRA100_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official product route and datasheet for 311ZRA100 state aluminum outer ring, materials in contact with media aluminum, and O-ring material NBR. Local assembly STEP material extraction for product 3Q3_seal_ISO_K_DN100_311ZRA100 returned only Generic with density 1000.0, which is placeholder metadata and was not used to resolve material. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page and datasheet are official Pfeiffer Vacuum Components & Solutions routes for the same manufacturer and exact order number 311ZRA100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The aluminum alloy grade is not stated on the row-matched product page or datasheet."
how_to_make:
  summary: "Best current route is procurement as Pfeiffer 311ZRA100 or equivalent ISO-K DN100 aluminum/NBR centering ring; local manufacture would combine a machined aluminum centering ring with a standard NBR O-ring and final dimensional/fit inspection."
  manufacturing_steps:
    - "Procure Pfeiffer 311ZRA100 or equivalent ISO-K DN100 centering ring with aluminum outer ring and NBR O-ring."
    - "For local manufacture, machine or form the aluminum centering/outer ring to DN100 ISO-K dimensions and deburr sealing-adjacent features."
    - "Install an NBR O-ring of the matching cross-section and inspect ring dimensions, O-ring seating, and flange fit."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073005/product/311zra100/centering-ring-with-outer-ring-aluminum.html; research/ream250_bom/ream250_bom_row_0140_3Q3__views_2x2.png"
    cited_fact_or_basis: "The official product route identifies the purchased product, DN100 ISO-K dimensions, aluminum outer ring, and NBR O-ring. The CAD preview shows a simple annular ring profile consistent with machining/forming plus O-ring installation. targeted_web_search: queries tried: 'Pfeiffer 311ZRA100 manufacturing process', 'ISO-K centering ring aluminum NBR manufacture', and '311ZRA100 datasheet manufacturing'; result: no row-specific source states the manufacturing process, so local manufacturing steps are inferred from geometry and materials."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Equivalent local production can use conventional aluminum ring machining/forming and separate elastomer O-ring procurement or molding."
  uncertainty_notes:
    - "The exact aluminum alloy, surface finish, and O-ring procurement/molding specification would need a later manufacturing drawing or standard-part specification."
kb_implications:
  - "item_granularity: consumable - Model later as a reusable ISO-K DN100 centering-ring seal consumable family rather than a reAM250-specific custom machine part; the row quantity represents two instances of the same replaceable flange seal."
---
