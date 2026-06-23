---
row_identity:
  item: "8A"
  cad_file: "8A_seal_ISO_KF_DN16"
  source_row_number: 206
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/112ZRG016"
function:
  summary: "Pfeiffer Vacuum 112ZRG016 DN 16 ISO-KF centering ring/seal component that positions and supports the O-ring between ISO-KF vacuum flanges so the clamp can compress the seal."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/112ZRG016; https://vacuum-shop.com/shop/en_US/category/2072872/product/112zrg016/centering-ring-aluminum-en-aw-6061.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8A_seal_ISO_KF_DN16.step; research/ream250_bom/ream250_bom_row_0206_8A__views_2x2.png"
    cited_fact_or_basis: "BOM row 206 identifies item 8A as Pfeiffer Vacuum product 112ZRG016, quantity 1, CAD file 8A_seal_ISO_KF_DN16. The official product route names 112ZRG016 as a centering ring for DN 16 ISO-KF. Pfeiffer vacuum-technology guidance describes ISO-KF connections as using an O-ring positioned and supported by a centering ring while a clamping ring supplies sealing force. The local CAD preview shows a small annular ring/seal form. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/112ZRG016 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 112ZRG016."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.001
  basis: "Per-unit estimate for BOM quantity 1. FreeCAD measured one solid with volume 430.790 mm^3, equal to 4.30790e-7 m^3, and bounding box 21.59 x 21.59 x 8.00 mm. The official product route resolves aluminum EN AW-6061 plus FKM, but the STEP is a single combined solid with no split material volumes. Using a planning effective density of 2400 kg/m^3, between local aluminum density 2700 kg/m^3 and local FKM density 1800 kg/m^3, gives 0.00103 kg, rounded to 0.001 kg. All-aluminum and all-FKM bounds from the same CAD volume are about 0.00116 kg and 0.00078 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8A_seal_ISO_KF_DN16.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2072872/product/112zrg016/centering-ring-aluminum-en-aw-6061.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 430.790 mm^3, area 1075.082 mm^2, and bounding box 21.59 x 21.59 x 8.00 mm. The official product route lists aluminum EN AW-6061 and FKM. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3 and FKM density 1800 kg/m^3. Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/112ZRG016 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 112ZRG016. targeted_web_search: searched '112ZRG016 weight', 'Pfeiffer 112ZRG016 mass', '112ZRG016 centering ring weight', and 'Pfeiffer DN16 ISO-KF centering ring aluminum FKM weight'; found row-matched material and dimension facts but no catalog net weight or split-material volume."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume is treated as the full physical envelope volume of one purchased centering-ring/seal item."
    - "Because CAD does not split aluminum and FKM volumes and no catalog weight was found on the BOM-provided route, an effective density of 2400 kg/m^3 is used as a midrange planning value."
  uncertainty_notes:
    - "The mass is bounded by known material densities but depends on an unsupported aluminum/FKM volume split; a supplier net weight or split-material CAD model would improve it."
material:
  primary_material: "aluminum EN AW-6061 centering ring with FKM O-ring"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072872/product/112zrg016/centering-ring-aluminum-en-aw-6061.html"
    cited_fact_or_basis: "The official product route for 112ZRG016 lists materials in contact with media as Aluminum EN AW-6061 and FKM, and separately lists O-ring material FKM. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/112ZRG016 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 112ZRG016."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The product page resolves material family and grade for the metal ring plus elastomer family, but not the exact FKM compound formulation or hardness."
how_to_make:
  summary: "Best represented as a purchased standard ISO-KF centering ring/seal; a local route would machine or form the small aluminum centering ring, mold or procure the FKM O-ring, assemble the two, clean for vacuum service, and inspect DN16 ISO-KF dimensions."
  manufacturing_steps:
    - "Procure or cut aluminum EN AW-6061 ring stock or a near-net blank for the DN16 ISO-KF centering ring."
    - "Turn or otherwise machine the annular centering-ring profile and sealing support surfaces to the vendor dimensions."
    - "Procure or mold the matching FKM O-ring."
    - "Assemble the O-ring onto the centering ring, clean for vacuum service, and inspect fit, dimensions, and elastomer condition."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072872/product/112zrg016/centering-ring-aluminum-en-aw-6061.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8A_seal_ISO_KF_DN16.step; research/ream250_bom/ream250_bom_row_0206_8A__views_2x2.png"
    cited_fact_or_basis: "The official product route identifies a standard DN 16 ISO-KF centering ring with aluminum EN AW-6061 and FKM materials, and dimensions A 17, B 16, C 3.9, D 8, E 5 mm. The local CAD/contact sheet shows a small annular ring/seal component consistent with a turned or formed ring plus elastomer seal. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/112ZRG016 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 112ZRG016."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The detailed local manufacturing route is inferred from the sourced product identity, material set, simple annular CAD geometry, and standard vacuum-seal practice; the vendor source does not state Pfeiffer's production process."
    - "For KB planning, procurement/import or reuse of a generic DN16 ISO-KF centering-ring/seal component is more appropriate than decomposing elastomer compounding and precision seal manufacture at this stage."
  uncertainty_notes:
    - "No row-specific source states the actual forming, machining, molding, cleaning, or inspection sequence used by the supplier."
    - "targeted_web_search: searched '112ZRG016 manufacturing process', 'Pfeiffer 112ZRG016 centering ring aluminum FKM manufacturing', and 'ISO-KF centering ring FKM O-ring manufacturing'; found row-matched product/material/dimension facts but no supplier manufacturing-process specification."
kb_implications:
  - "item_granularity: purchased_module - Model as a reusable standard DN16 ISO-KF centering-ring/seal component with aluminum ring and FKM O-ring, not as separate ring and O-ring items unless vacuum seal consumables become a high-priority dependency."
---

Research result for the leased reAM250 BOM row only.
