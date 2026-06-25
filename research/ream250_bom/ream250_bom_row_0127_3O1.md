---
row_identity:
  item: "3O1"
  cad_file: "3O1_curvature_320SWN063"
  source_row_number: 127
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "Curved/bent bellows or corrugated-hose segment for a Pfeiffer Vacuum DN 63 ISO-K flexible vacuum connector, used to provide a compliant vacuum line offset or bend between ISO-K flange interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0250; https://vacuum-shop.com/shop/en_US/category/2073103/iso-k-corrugated-hose-flexible.html"
    cited_fact_or_basis: "BOM row 127 identifies item 3O1 as quantity 1, CAD file 3O1_curvature_320SWN063, description 320SFK063: curvature, manufacturer Pfeiffer Vacuum, and a Pfeiffer product URL. The manifest maps the same row to a matched vendor-component STEP. The official Pfeiffer/Busch product page identifies 320SWN063-0250 as a corrugated hose, flexible, stainless steel, DN 63 ISO-K. The Pfeiffer-branded shop category lists ISO-K corrugated hose flexible parts with DN 63 ISO-K entries and bending-radius data. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the used Pfeiffer/Busch 320SWN063 page and vacuum-shop.com Pfeiffer Vacuum Online Shop pages are official or branded Pfeiffer routes, match the row's Pfeiffer manufacturer and 320SWN/320SFK DN 63 ISO-K hose/bellows family, and resolve the same flexible vacuum connector context."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's 'curvature' CAD export is interpreted as one bent section of the vendor flexible connector/hose geometry, not a separate catalog product."
  uncertainty_notes:
    - "The contact-sheet renderer hung during Matplotlib image generation, so visible-shape triage is unavailable; function confidence comes from BOM/manifest identity, CAD envelope, and row-matched Pfeiffer product-family evidence."
mass:
  value_kg: 0.24
  basis: "FreeCAD measured one solid with volume 29828.919 mm^3 = 2.9828919e-5 m^3. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.2395 kg per 3O1 curvature item, rounded to 0.24 kg. BOM quantity is 1, so row total is also about 0.24 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O1_curvature_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073103/iso-k-corrugated-hose-flexible.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 29828.919 mm^3, area 303921.028 mm^2, and bounding box 181.43 x 122.34 x 102.95 mm. The Pfeiffer-branded ISO-K corrugated hose page states the family uses stainless steel 1.4301/304 flanges and stainless steel 316L bellows. The local density table lists stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the vacuum-shop.com page is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches the row's 320SWN/320SFK DN 63 ISO-K flexible connector family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical metal volume for one 3O1 curvature item."
    - "Stainless_steel_304 density is used as a close calculation constant for the mixed 304/316L stainless family; the density difference is negligible at this estimate precision."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only placeholder Generic material at density 1000.0, and no catalog weight for this CAD subpiece was found, so mass is CAD-volume-derived rather than vendor-weighed."
material:
  primary_material: "stainless steel vacuum bellows/hose family: 1.4301/304 flange material and 316L bellows material for DN 63 ISO-K flexible connector hardware"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073103/iso-k-corrugated-hose-flexible.html; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "The Pfeiffer-branded ISO-K corrugated hose page states 'Flange: stainless steel 1.4301/304; bellows: stainless steel 316L' for the 320SWN DN 63 ISO-K flexible hose family. The row's BOM-provided 320SFK063-130 route also resolves to a Pfeiffer-branded spring-bellows page that states stainless steel material with 304 flanges and DN 63 to DN 100 bellows as 316L. official_alternate_route_check: original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the used vacuum-shop.com pages are branded Pfeiffer Vacuum Online Shop, list Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and match the row's manufacturer, product-family naming, and DN 63 ISO-K flexible/bellows context."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row is named curvature_320SWN063, the curved section is assigned to the stainless bellows/hose portion of the connector rather than to a separate nonmetal insert."
  uncertainty_notes:
    - "The row-specific STEP material metadata is placeholder only, and the CAD subpiece does not separately label flange versus bellows regions; material should be kept as stainless bellows/hose family unless later subpart metadata identifies a narrower grade."
how_to_make:
  summary: "Procure as part of a Pfeiffer DN 63 ISO-K flexible corrugated hose or spring-bellows connector for current KB modeling; a plausible local route would form thin-wall stainless bellows/corrugated tubing, weld or join it to stainless ISO-K end hardware, bend/fixture the connector to the required curvature, clean/passivate, and helium leak-test for vacuum service."
  manufacturing_steps:
    - "Procure route: buy the row-matched Pfeiffer DN 63 ISO-K flexible hose/spring-bellows connector and model this curvature as part of that vendor connector."
    - "Local route: form or hydroform thin-wall stainless 316L bellows/corrugated tube stock to the required DN 63 profile."
    - "Join stainless 304/1.4301 ISO-K end hardware to the bellows or hose section using vacuum-compatible welding or equivalent joining."
    - "Fixture the assembly to the required bend/curvature, then clean, passivate as needed, and helium leak-test for vacuum tightness."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O1_curvature_320SWN063.step; https://vacuum-shop.com/shop/en_US/category/2073103/iso-k-corrugated-hose-flexible.html; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "FreeCAD measured a 181.43 x 122.34 x 102.95 mm curved-part envelope for the row STEP. Pfeiffer-branded product pages identify DN 63 ISO-K flexible hose/spring-bellows hardware, stainless 304 flange material, 316L bellows material, pressure/tightness service data, and bending-radius or axial-stroke service context. The detailed local fabrication sequence is inferred from the bellows/hose geometry and stainless vacuum-service requirements rather than directly stated by a manufacturing process sheet. targeted_web_search: searched 'Pfeiffer Vacuum 320SFK063 130 flexible pipe DN 63 material weight', '320SFK063 Pfeiffer Vacuum curvature 320SWN063 material', 'site:pfeiffer-vacuum.com 320SFK063 320SWN063', '320SWN063-0250 weight kg Pfeiffer', and '320SFK063-130 weight kg Pfeiffer spring bellows'; results resolved product family, dimensions, and material, but no row-specific manufacturing process or catalog weight."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Local production would need vacuum-grade thin-wall stainless forming and joining capability; the BOM row itself is better modeled as a purchased connector component until that process chain is intentionally expanded."
  uncertainty_notes:
    - "The vendor/CAD evidence does not state the actual Pfeiffer factory process, weld details, corrugation process, bend fixture method, surface finish, or inspection protocol."
kb_implications:
  - "item_granularity: simple_part - Treat 3O1 as the curved bellows/corrugated-hose segment of a DN63 ISO-K flexible connector; model local closure with bellows forming, end joining, cleaning, and leak testing instead of a deferred complex module."
---

Research result for reAM250 BOM row 127.
