---
row_identity:
  item: "8B"
  cad_file: "8B_angle_pipe_ISO_KF_DN40"
  source_row_number: 207
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90"
function:
  summary: "DN 40 ISO-KF 90-degree vacuum elbow used to turn a KF vacuum line through a right angle while preserving the clamp-flange interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0207_8B__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "BOM row 207 identifies item 8B, quantity 5, product 110RRB040-90 by Pfeiffer Vacuum; CAD preview shows a right-angle elbow with two KF-style flanged ends; vendor page names it 'Elbow fitting, 90°' with connection flange DN 40 ISO-KF. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90; alternate route https://vacuum-shop.com is the Pfeiffer Vacuum Components & Solutions GmbH online shop, carries the same order number 110RRB040-90/global number 2000050096, and matches the same DN 40 ISO-KF 90-degree elbow row."
    evidence_basis: "bom_provided"
  assumptions:
    - "The per-row CAD part represents one physical elbow; the BOM quantity of 5 means five identical elbows are used."
  uncertainty_notes: []
mass:
  value_kg: 0.141
  basis: "Per-unit mass estimate from FreeCAD volume 52,397.365 mm^3 = 0.000052397365 m^3 multiplied by local aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.141 kg per elbow. BOM quantity is 5, so the row total is about 0.707 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8B_angle_pipe_ISO_KF_DN40.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 52,397.364951 mm^3 and bounding box about 94.77 x 94.77 x 59.53 mm; vendor page gives material Aluminum 3.2315/EN AW-6082; local material table gives aluminum density 2700 kg/m^3. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90; alternate route https://vacuum-shop.com is an official Pfeiffer Vacuum online shop page and matches order number 110RRB040-90 for the same DN 40 ISO-KF elbow."
    evidence_basis: "bom_provided"
  assumptions:
    - "CAD solid volume is used as the physical aluminum volume for one elbow."
    - "The local generic aluminum density is close enough for EN AW-6082 at this planning precision."
  uncertainty_notes:
    - "STEP assembly metadata for this row reports only Generic material at density 1000.0, so material identity comes from the row-matched vendor route rather than embedded STEP material metadata."
material:
  primary_material: "Aluminum 3.2315 / EN AW-6082"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "Vendor page for order number 110RRB040-90 states material and media-contact material as Aluminum 3.2315/EN AW-6082. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90; alternate route https://vacuum-shop.com is operated as Pfeiffer Vacuum Components & Solutions GmbH online shop and matches the same product ID, global number, and DN 40 ISO-KF 90-degree elbow."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 110RRB040-90, a standard DN 40 ISO-KF aluminum 90-degree elbow; later local modeling can treat it as a formed or machined aluminum vacuum fitting if procurement is replaced."
  manufacturing_steps:
    - "Buy or stock the row-matched Pfeiffer 110RRB040-90 elbow fitting."
    - "Inspect DN 40 ISO-KF flange faces and sealing surfaces before assembly into the vacuum line."
    - "Install with compatible ISO-KF centering rings and clamps supplied elsewhere in the BOM."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "BOM row gives manufacturer Pfeiffer Vacuum and product ID 110RRB040-90; vendor page lists the same order number as an orderable DN 40 ISO-KF 90-degree aluminum elbow fitting. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90; alternate route https://vacuum-shop.com is a Pfeiffer Vacuum online shop page with matching product identity and ordering data."
    evidence_basis: "bom_provided"
  assumptions:
    - "The current KB route should prefer procurement/standard-part reuse over modeling this row as a bespoke machine-specific fabrication."
  uncertainty_notes:
    - "Detailed local fabrication operations are not sourced here; this result only establishes a procurement route and part identity."
kb_implications:
  - "item_granularity: simple_part - Model as reusable DN 40 ISO-KF aluminum 90-degree vacuum elbow hardware rather than a calibrated purchased module."
---

Research result for reAM250 BOM row 207.
