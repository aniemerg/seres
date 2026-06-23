---
row_identity:
  item: "3O3"
  cad_file: "3O3_end_piece_320SWN063"
  source_row_number: 129
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "One stainless end fitting/flange of the Pfeiffer 320SFK063-130 DN 63 ISO-K spring bellows; it provides the rigid ISO-K connection and weld/attachment end for the flexible bellows assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O3_end_piece_320SWN063.step; research/ream250_bom/ream250_bom_row_0129_3O3__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html"
    cited_fact_or_basis: "BOM row 129 names item 3O3 as '320SFK063: end piece' by Pfeiffer Vacuum. The CAD preview shows a short annular flanged ring/end fitting. The official shop page identifies 320SFK063-130 as a DN 63 ISO-K spring bellows with flange connection length 30 mm. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the alternate vacuum-shop.com page is branded 'Pfeiffer Vacuum Online Shop', lists Pfeiffer Vacuum contact/copyright information, and matches product ID 320SFK063-130."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row's 'end piece' is interpreted as one rigid end fitting of the complete 320SFK063-130 spring bellows rather than the complete bellows assembly."
  uncertainty_notes:
    - "The CAD export is a vendor component subdivision; it does not show the final weld joint to the bellows."
mass:
  value_kg: 0.412
  basis: "FreeCAD measured one solid with volume 51352.068 mm^3. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 51352.068e-9 m^3 * 8030 kg/m^3 = 0.412 kg per end piece. BOM quantity is 1, so the row total is also about 0.412 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O3_end_piece_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 51352.06790278328 mm^3, area 26491.578678240712 mm^2, and bounding box 35.28805 x 105.13275441440022 x 105.13275441440022 mm. The official shop page states spring-bellows material as stainless steel with flange 304 and bellows 316L; kb/materials/properties.yaml gives stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the alternate vacuum-shop.com page is branded 'Pfeiffer Vacuum Online Shop', lists Pfeiffer Vacuum contact/copyright information, and matches product ID 320SFK063-130."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid is treated as one physical end piece with no missing internal regions significant to mass."
    - "Because this row is the end piece/flange rather than the bellows, the flange material 304 is used for density."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic density 1000.0, so material identity comes from the row-matched supplier product-family page, not embedded CAD material metadata."
material:
  primary_material: "stainless steel 304 / EN 1.4301 for the end-piece flange fitting"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "The official shop page for ISO-K Spring Bellows lists material as stainless steel, with flange 304 and bellows 316L for DN 63 to DN 100 and DN 320; BOM row 129 identifies this row as the 320SFK063 end piece. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the alternate vacuum-shop.com page is branded 'Pfeiffer Vacuum Online Shop', lists Pfeiffer Vacuum contact/copyright information, and matches product ID 320SFK063-130."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 'end piece' corresponds to the flange/end fitting portion of the spring bellows material statement."
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material was available; if Pfeiffer uses a different weld stub alloy for this exact end piece, the supplier family page does not expose that distinction."
how_to_make:
  summary: "Procure as part of Pfeiffer 320SFK063-130, or locally manufacture as a turned stainless 304 ISO-K end fitting and weld/braze it into the spring-bellows assembly."
  manufacturing_steps:
    - "Start from stainless 304 round bar, tube, or forged ring stock sized for a DN 63 ISO-K flange/end fitting."
    - "Turn the annular profile, bore, sealing shoulder, and outer flange features on a lathe; finish critical sealing and weld-prep surfaces."
    - "Deburr, clean for vacuum service, and inspect dimensions and surface condition."
    - "Join to the 316L bellows tube/end by controlled TIG/orbital welding or the vendor-equivalent joining process, followed by leak testing of the completed spring bellows."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O3_end_piece_320SWN063.step; research/ream250_bom/ream250_bom_row_0129_3O3__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html"
    cited_fact_or_basis: "CAD shows an axisymmetric annular end piece with flange-like shoulders; the official shop page identifies the parent item as a stainless DN 63 ISO-K spring bellows with 304 flange and 316L bellows. targeted_web_search: searched 'Pfeiffer Vacuum 320SFK063 320SWN063 end piece material DN63', '320SWN063-0250 Pfeiffer datasheet DN 63 ISO-K stainless steel flange 1.4301', and '320SFK063-130 Pfeiffer Vacuum flexible pipe ISO-K DN63 material'; results resolved product family, dimensions, and materials but did not provide a row-specific manufacturing process for the end piece."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The annular CAD geometry is suitable for conventional turning/machining rather than casting."
    - "Joining and leak testing are inferred from vacuum bellows construction practice and the supplier pressure-range claims for the finished spring bellows."
  uncertainty_notes:
    - "The exact vendor fabrication sequence, heat treatment, cleaning specification, and acceptance test details are not provided by the BOM or supplier page."
kb_implications:
  - "item_granularity: simple_part - Model this as a reusable stainless ISO-K DN63 end fitting/flange component of a purchased or assembled spring-bellows module, not as raw stock or the complete bellows assembly."
---
