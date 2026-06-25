---
row_identity:
  item: "3R2"
  cad_file: "3R2_seal_ISO_K_DN63_311ZRA063"
  source_row_number: 144
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063"
function:
  summary: "DN 63 ISO-K vacuum centering ring and seal assembly; it centers the flange interface and provides the NBR elastomer sealing element."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html; research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png"
    cited_fact_or_basis: "The BOM row identifies item 3R2 as Pfeiffer Vacuum product 311ZRA063. The row-matched product page identifies 311ZRA063 as a centering ring with outer ring for connection flange DN 63 ISO-K. The CAD contact sheet shows a thin annular ring form. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.013
  basis: "FreeCAD measured one solid with volume 5586.124 mm^3, surface area 6239.540 mm^2, and bounding box 85.99 x 86.00 x 8.00 mm. The rendered preview reported an about 79.3 x 79.3 x 8.0 mm mesh bounding box for visual triage only. Estimated mass uses the CAD volume as a combined material-volume proxy and a coarse 75% aluminum / 25% NBR volume split. Local density constants from kb/materials/properties.yaml are aluminum 2700 kg/m^3 and NBR 1100 kg/m^3, giving effective density about 2300 kg/m^3 and mass about 0.01285 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R2_seal_ISO_K_DN63_311ZRA063.step; kb/materials/properties.yaml; https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html"
    cited_fact_or_basis: "FreeCAD measured 5586.124 mm^3 for the row STEP. The row-matched product page and datasheet state aluminum for media-contact material and NBR for the O-ring. The local density table lists aluminum at 2700 kg/m^3 and NBR at 1100 kg/m^3. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The single-solid STEP volume is used as a combined volume proxy for the aluminum ring and NBR O-ring because the CAD does not expose separate material volumes."
    - "A 75% aluminum / 25% NBR volume split is used as a coarse estimate."
  uncertainty_notes:
    - "targeted_web_search: searched \"311ZRA063 Pfeiffer Vacuum material seal ISO-K DN63\", \"311ZRA063 Pfeiffer Vacuum seal ISO-K DN63 NBR aluminum\", and \"311ZRA063 mass weight\"; found row-matched material and dimensional facts but no catalog mass or material-volume split."
    - "The aluminum-to-NBR volume fraction is not measured separately, so the mass should be treated as an order-of-magnitude estimate."
material:
  primary_material: "aluminum ring with NBR O-ring"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html"
    cited_fact_or_basis: "The row-matched product page and datasheet for 311ZRA063 state aluminum outer ring, materials in contact with media aluminum, and O-ring material NBR. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Manufacture as a small vacuum flange seal consumable: form the aluminum centering/outer ring, mold or procure the NBR O-ring, clean and deburr the ring, install the O-ring, and inspect fit and sealing surfaces."
  manufacturing_steps:
    - "Machine, stamp, or otherwise form the aluminum centering/outer ring profile to DN 63 ISO-K geometry."
    - "Mold, cut, or procure the NBR O-ring to the matching seal cross-section."
    - "Deburr and clean the aluminum ring so flange-contact and seal-contact surfaces are smooth."
    - "Install the NBR O-ring onto the aluminum ring and inspect fit, concentricity, and visible seal damage."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html; research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png"
    cited_fact_or_basis: "The row-matched product page identifies an aluminum outer-ring centering ring with NBR O-ring for DN 63 ISO-K. The CAD contact sheet shows a thin annular ring/seal geometry. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the stated aluminum plus NBR construction and the visible thin annular profile, not from a vendor process specification."
  uncertainty_notes:
    - "targeted_web_search: searched \"311ZRA063 Pfeiffer Vacuum material seal ISO-K DN63\", \"311ZRA063 Pfeiffer Vacuum seal ISO-K DN63 NBR aluminum\", and \"311ZRA063 manufacturing process centering ring\"; found product material and dimensional facts but no vendor manufacturing process description."
kb_implications:
  - "item_granularity: simple_part - replaceable ISO-K vacuum centering ring/seal assembly; later KB modeling can keep it as a purchased replaceable or applied part unless vacuum-seal fabrication becomes in scope."
---
