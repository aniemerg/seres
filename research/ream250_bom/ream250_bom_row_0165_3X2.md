---
row_identity:
  item: "3X2"
  cad_file: "3X2_valve_part_2"
  source_row_number: 165
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "Part 2 of the AMPROVED ISO-KF DN40 manual disc valve used in the reAM250 powder/AM-machine fluid path; the visible CAD geometry is the lever/shaft and disc subassembly that actuates or closes the valve."
  source:
    url_or_path: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0165_3X2__views_2x2.png"
    cited_fact_or_basis: "BOM row 165 identifies item 3X2 as AMPROVED 'part 2 valve sv04_din_cc_dn40_-' with material text '_aisi_316l-1_4404_-_epdm'. The BOM-provided AMPROVED page names the product ISO-KF DN40 Scheibenventil and describes a manual disc valve for controlling fluid flows in pipes and closing powder bottles, overflows, and filling ports in AM machines. The rendered CAD contact sheet shows a lever, shaft, and disc-like valve element."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one modeled subpart of the AMPROVED DN40 valve rather than a separately cataloged replacement SKU."
  uncertainty_notes:
    - "The source page describes the complete DN40 valve; the split between part 1 and part 2 comes from the BOM/CAD package rather than the vendor page."
mass:
  value_kg: 0.361
  basis: "FreeCAD measured CAD volume 45009.926 mm^3, equivalent to 0.000045009926 m^3. Treating the single-solid CAD volume as stainless steel 316L / 1.4404 and using the local stainless_steel density 8000 kg/m^3 gives 0.360079 kg, rounded to 0.361 kg per unit. BOM quantity is 1, so the row total is also about 0.361 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X2_valve_part_2.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 45009.926 mm^3, area 13325.750 mm^2, and bounding box 29.58 x 130.70 x 141.00 mm. BOM row 165 states material text '_aisi_316l-1_4404_-_epdm'. The local material density table lists stainless_steel density 8000 kg/m^3. targeted_web_search: checked the BOM-provided AMPROVED product page and its linked drawing PDF route, plus query terms 'AMPROVED ISO-KF DN 40 Scheibenventil weight', 'SV04 DIN CC DN40 weight', and 'ISO-KF DN40 Scheibenventil AMPROVED mass'; no row-specific catalog mass for part 2 was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP single-solid volume is treated as the physical volume for one row item."
    - "The stainless component dominates the mass; any EPDM seal contribution is included geometrically but not separately density-weighted."
  uncertainty_notes:
    - "Because the CAD is one unsplit solid and the STEP assembly material extractor returns only Generic at density 1000.0 for this part, the estimate cannot separate stainless and EPDM volumes."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel with EPDM sealing material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv"
    cited_fact_or_basis: "BOM row 165 and manifest row 165 preserve the row description '_aisi_316l-1_4404_-_epdm: part 2 valve sv04_din_cc_dn40_-' for AMPROVED item 3X2."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row does not identify which subfeatures are stainless versus EPDM, and the local STEP material metadata is only placeholder Generic, so downstream modeling should preserve the combined material set rather than assign a detailed material split."
how_to_make:
  summary: "Near-term KB modeling should procure this as an AMPROVED DN40 valve subcomponent or as part of the complete ISO-KF DN40 disc valve; a plausible local route is precision stainless machining for the shaft/disc/lever hardware, EPDM seal fabrication or procurement, cleaning/passivation, assembly, and leak/function testing."
  manufacturing_steps:
    - "Procure the complete AMPROVED ISO-KF DN40 disc valve or the matching replacement subcomponent when available."
    - "For local production, machine the stainless shaft, lever hub, handle, and disc-like closure geometry from 316L/1.4404 stock."
    - "Mold, cut, or procure the EPDM sealing element compatible with the DN40 valve geometry."
    - "Deburr, clean, and passivate stainless surfaces for powder/vacuum-adjacent service."
    - "Assemble the lever and closure element with the seal, then verify the three-position manual action and closure/leak performance in the valve body."
  source:
    url_or_path: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html; research/ream250_bom/ream250_bom_row_0165_3X2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X2_valve_part_2.step"
    cited_fact_or_basis: "The AMPROVED product page identifies the complete product as an ISO-KF DN40 manual disc valve with 3 latch positions for controlling flow and closing powder bottles/filling ports. The CAD contact sheet shows the row-specific lever, shaft, handle, and disc-like closure geometry. FreeCAD measured bounding box 29.58 x 130.70 x 141.00 mm. targeted_web_search: checked the BOM-provided AMPROVED route and searched 'AMPROVED ISO-KF DN 40 Scheibenventil manufacturing', 'SV04 DIN CC DN40 valve material EPDM 316L', and 'ISO-KF DN40 disc valve 316L EPDM manufacturing'; results resolved product use and material wording but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining plus seal assembly is inferred from the stainless/EPDM material set and the visible lever/shaft/disc geometry."
    - "Final testing is required because the component controls a powder or fluid-flow closure interface in the machine."
  uncertainty_notes:
    - "The vendor page does not state the actual production process, tolerances, surface finish, or seal installation details for this subpart."
kb_implications:
  - "item_granularity: complex_module - model 3X2 as a valve subassembly or purchased valve subcomponent for now; split into stainless simple parts plus an EPDM seal only if the DN40 valve becomes a detailed local-manufacturing target."
---

# reAM250 BOM Row 165 - 3X2

Research result for the leased reAM250 BOM row.
