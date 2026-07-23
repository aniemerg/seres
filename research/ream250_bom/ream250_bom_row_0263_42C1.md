---
row_identity:
  item: "42C1"
  cad_file: "42C1_valve_part_1"
  source_row_number: 263
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "Subpart of the AMproved ISO-KF DN40 manual disc valve used to close or control flow at powder-bottle, overflow, fill-port, or pipe interfaces in the reAM250 gas/powder handling system."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0263_42C1__views_2x2.png"
    cited_fact_or_basis: "AMproved identifies the product as an ISO-KF DN40 disc valve for manual fluid-flow control in pipes and for closing powder bottles, overflows, and filling ports in AM machines; BOM row 263 identifies this row as part 1 of valve sv04_din_cc_dn40; CAD preview shows a compact cylindrical ring-like valve subpart with side features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD-split row represents one physical subpart of the complete valve, not the entire valve assembly."
  uncertainty_notes:
    - "The row does not name the exact internal role of part 1 within the valve, so the function is assigned at valve-subpart granularity rather than as a named body, gland, or retainer."
mass:
  value_kg: 0.173
  basis: "Per-unit mass for one 42C1_valve_part_1 item. FreeCAD measured 1 solid, volume 21574.099 mm^3, surface area 8200.189 mm^2, and bounding box about 38.00 x 45.50 x 38.00 mm. Using local stainless_steel density 8000 kg/m^3 from kb/materials/properties.yaml gives 21574.099 mm^3 * 1e-9 m^3/mm^3 * 8000 kg/m^3 = 0.1726 kg, rounded to 0.173 kg. BOM quantity is 1, so the row total is also about 0.173 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C1_valve_part_1.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured the row-specific STEP volume and bounding box; kb/materials/properties.yaml lists stainless_steel density as 8000 kg/m^3. The BOM row material text names AISI 316L / 1.4404 and EPDM."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the solid material volume for one item."
    - "The visible part 1 geometry is treated as the stainless metal subpart of the valve, so the stainless-steel density constant is the relevant mass conversion."
  uncertainty_notes:
    - "The full assembly material extractor returned only Generic with density 1000.0 for this product, so it did not independently confirm material assignment."
    - "If this split CAD part includes non-steel EPDM volume, the all-stainless calculation will overstate mass; if the CAD omits small hardware, it will understate the complete valve-subpart mass."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel with EPDM sealing material in the valve family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv"
    cited_fact_or_basis: "BOM row 263 description/product field states '_aisi_316l-1_4404_-_epdm: part 1 valve sv04_din_cc_dn40_-'; the manifest maps the row to 42C1_valve_part_1.step as a matched_existing vendor_component."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM material wording applies to the valve part represented by the row, with stainless steel as the structural material and EPDM as the associated sealing elastomer."
  uncertainty_notes:
    - "The row does not split the stainless and EPDM material fractions across valve parts 1, 2, and 3."
how_to_make:
  summary: "Manufacturing route would machine the stainless valve body/ring features from 316L/1.4404 stock, finish sealing and clamp interfaces, and assemble with the EPDM sealing element and the other valve parts"
  manufacturing_steps:
    - "For local manufacture, start from 316L/1.4404 stainless bar or near-net stock sized for the about 38 x 45.5 x 38 mm envelope."
    - "Turn and mill the cylindrical bore, outer surfaces, side lugs, and engagement features indicated by the CAD preview."
    - "Deburr, passivate or clean for vacuum/powder service, and verify ISO-KF DN40 fit and sealing surfaces."
    - "Install or pair with the EPDM sealing element and the remaining valve parts during final valve assembly."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C1_valve_part_1.step; research/ream250_bom/ream250_bom_row_0263_42C1__views_2x2.png"
    cited_fact_or_basis: "AMproved supplies the row-matched ISO-KF DN40 disc valve as a purchasable product; CAD geometry and preview show a small cylindrical machined-looking valve subpart. targeted_web_search: tried 'SV04_DIN_CC_DN40 AISI 316L EPDM', 'valve sv04_din_cc_dn40', and 'SV04 DIN DN40 EPDM 316L'; results did not provide a row-specific manufacturing process for this AMproved split CAD part."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining from stainless stock is a plausible Manufacturing route for the visible geometry because no source provided the actual supplier manufacturing route for the split subpart."
  uncertainty_notes:
    - "The exact production process, tolerance stack, and sealing-surface finish requirements are not specified by the BOM or vendor page."
kb_implications:
  - "item_granularity: complex_module - Model the complete ISO-KF DN40 manual disc valve as a functional functional complex module for this pass; this row is one CAD-split valve subpart and should not become a separate reusable KB item unless the valve is later decomposed into a sub-BOM."
---
