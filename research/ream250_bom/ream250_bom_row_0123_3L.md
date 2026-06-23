---
row_identity:
  item: "3L"
  cad_file: "3L_flexible_pipe_ISO_K_DN63_320SWN063-0750"
  source_row_number: 123
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "Flexible corrugated ISO-K DN 63 vacuum hose used to connect vacuum components while tolerating routing offset, vibration, or limited motion in the gas circulation plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3L_flexible_pipe_ISO_K_DN63_320SWN063-0750.step; https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0750"
    cited_fact_or_basis: "BOM row 123 identifies item 3L as quantity 1, Pfeiffer Vacuum, product route 320SFK063, with raw row text containing 063-0750. The manifest maps row 123 to 3L_flexible_pipe_ISO_K_DN63_320SWN063-0750.step. FreeCAD measured a 750.00 x 105.13 x 105.13 mm envelope. The official Pfeiffer/Busch exact-product route identifies order number 320SWN063-0750 as a corrugated hose, flexible, stainless steel, DN 63 ISO-K, length 750 mm. official_alternate_route_check: the original BOM URL is a Pfeiffer shop route for 320SFK063_130; the exact official alternate route on the redirected Busch Group shop domain was derived from the row CAD filename/order suffix 320SWN063-0750 and matches the row length and DN 63 ISO-K hose identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The required contact-sheet render was attempted but did not complete before interruption; shape inference therefore uses CAD dimensions, STEP product identity, and official product text rather than inspected rendered views."
mass:
  value_kg: 1.697
  basis: "FreeCAD measured one CAD solid volume as 212158.307 mm^3. Treating the CAD solid as stainless steel volume and using the local generic stainless_steel density 8000 kg/m^3 gives 212158.307e-9 m^3 * 8000 kg/m^3 = 1.697 kg per flexible hose. BOM quantity is 1, so row total is also about 1.697 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3L_flexible_pipe_ISO_K_DN63_320SWN063-0750.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/2075372/downloads/datasheets/Datasheet_320SWN063-0750_en.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 212158.307 mm^3, area 1147172.325 mm^2, and bounding box 750.00 x 105.13 x 105.13 mm. The local density table gives generic stainless_steel as 8000 kg/m^3. The row-matched datasheet identifies the product as stainless steel, DN 63 ISO-K, length 750 mm. bom_url_route_check: the original BOM URL did not resolve the exact 320SWN063-0750 row, so the exact row-matched datasheet was used for material family while CAD supplied the measured volume."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is treated as the per-unit metal volume for the physical flexible hose."
    - "A single generic stainless density is adequate because the sourced flange 304/1.4301 and bellows 316L stainless grades are close enough for BOM-scale mass planning."
  uncertainty_notes:
    - "This is a CAD-derived mass estimate, not a catalog net weight or weighed part mass."
    - "CAD simplification, wall-thickness representation, weld collars, or omitted small features may shift the true part mass."
material:
  primary_material: "stainless steel: flange 1.4301 / AISI 304; bellows 316L"
  source:
    url_or_path: "https://www.vacuum-shop.com/2075372/downloads/datasheets/Datasheet_320SWN063-0750_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched datasheet for 320SWN063-0750 states material as stainless steel, with flange 1.4301/304 and bellows 316L. The assembly STEP material extractor found only placeholder material Generic with density 1000.0 for this product. bom_url_route_check: the original BOM URL did not resolve the exact 320SWN063-0750 material facts, so the exact row-matched datasheet was used."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "Local STEP material metadata is placeholder Generic, so it does not independently confirm the stainless grades."
how_to_make:
  summary: "Procure as Pfeiffer/Busch 320SWN063-0750, or manufacture locally as a stainless corrugated vacuum hose with DN 63 ISO-K 304 flanges joined to a 316L bellows tube, followed by cleaning and leak testing."
  manufacturing_steps:
    - "Form or source a thin-wall 316L stainless corrugated bellows tube to the 750 mm nominal hose length."
    - "Machine or form two stainless 1.4301/304 ISO-K DN 63 flange end pieces."
    - "Weld the flange ends to the bellows tube while preserving vacuum-clean internal surfaces and avoiding bellows heat damage."
    - "Clean and passivate as needed, inspect ISO-K sealing dimensions, then leak-test for high-vacuum service."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3L_flexible_pipe_ISO_K_DN63_320SWN063-0750.step; https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0750; https://www.vacuum-shop.com/2075372/downloads/datasheets/Datasheet_320SWN063-0750_en.pdf"
    cited_fact_or_basis: "The official exact-product route and datasheet identify a DN 63 ISO-K stainless flexible corrugated hose with 750 mm length, and the STEP measurement confirms the 750 mm hose envelope. targeted_web_search: searched 'Pfeiffer 320SWN063-0750 manufacturing corrugated hose stainless bellows', '320SWN063-0750 datasheet material flange bellows', and 'ISO-K DN63 corrugated hose manufacturing stainless bellows welded flange'; found row-matched product and material facts but no Pfeiffer factory operation sheet for this row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route follows common stainless vacuum bellows hose fabrication practice inferred from the product geometry and material, not a Pfeiffer-published process sheet."
    - "The preferred KB route is procurement as a standard vendor vacuum component unless the model later adds bellows forming, precision welding, cleaning, and leak-test capabilities."
  uncertainty_notes:
    - "Exact factory details such as hydroforming versus mechanical convolution forming, weld process, post-weld cleaning, and acceptance leak-rate specification are unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as reusable ISO-K DN 63 stainless corrugated hose hardware with length variants, not as a reAM250-specific assembly."
---
