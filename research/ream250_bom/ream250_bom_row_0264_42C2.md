---
row_identity:
  item: "42C2"
  cad_file: "42C2_valve_part_2"
  source_row_number: 264
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "Manual ISO-KF DN40 disc valve in the reAM250 powder/vacuum handling hardware, used to manually open, restrict, or close a DN40 flow path such as a powder bottle, overflow, or AM-machine filling nozzle."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C2_valve_part_2.step; research/ream250_bom/ream250_bom_row_0264_42C2__views_2x2.png; https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; https://www.amproved.com/downloads/files/amproved_dn40_scheibenventil.pdf"
    cited_fact_or_basis: "BOM row 264 states item 42C2, quantity 1, manufacturer AMPROVED, CAD file 42C2_valve_part_2, and description/product text '_aisi_316l-1_4404_-_epdm: part 2 valve sv04_din_cc_dn40_-'. The manifest maps the row to gold_export/parts/42C2_valve_part_2.step as a matched vendor_component. The AMPROVED product page identifies the row-matched product as ISO-KF DN 40 - Scheibenventil, describes it as a manual disc valve for controlling fluid flows in pipelines, and says it is ideal for closing powder bottles, overflows, and filling nozzles in AM machines. The AMPROVED drawing shows the levered DN40 valve geometry, and the rendered CAD preview shows the same lever, circular valve body, and DN/KF-style port geometry. official_alternate_route_check: original BOM URL https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html resolved via AMPROVED search/canonical product route to https://www.amproved.com/iso-kf-dn-40-scheibenventil.html and its AMPROVED-hosted drawing PDF; manufacturer, product name, DN40 valve description, and geometry match the leased row."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents the complete manual DN40 valve shown in the CAD/export rather than only a subcomponent named 'part 2', because the BOM row quantity, manufacturer/product URL, and CAD preview all point to the levered valve assembly."
  uncertainty_notes:
    - "The exact reAM250 mating port or powder bottle interface is not identified by this row alone."
mass:
  value_kg: 0.35
  basis: "FreeCAD volume 45009.926 mm^3 equals 0.000045010 m^3 for the exported row geometry. If treated entirely as stainless steel 1.4404/316L using the local stainless_steel_304 density 8030 kg/m^3, the mass would be 0.361 kg. Because the BOM also names EPDM and the valve is a multi-part assembly with seals and possible small non-solid/export simplifications, the selected per-unit planning estimate is rounded to 0.35 kg for quantity 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C2_valve_part_2.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 45009.926 mm^3, area 13325.750 mm^2, and bounding box 29.58 x 130.70 x 141.00 mm. BOM row 264 names material/component wording AISI 316L / 1.4404 - EPDM. The local density table lists stainless_steel_304 / stainless_steel_1_4301 at 8030 kg/m^3 and representative nitrile rubber at 1100 kg/m^3; it does not list a specific EPDM density. The AMPROVED product route identifies the same DN40 valve but does not state mass. official_alternate_route_check: original BOM URL is an AMPROVED product route for the same DN40 disc valve and the canonical AMPROVED product page/drawing match the row, but they do not provide a weight. targeted_web_search: searched \"AMPROVED ISO-KF DN 40 Scheibenventil weight\", \"AMPROVED DN40 Scheibenventil mass\", \"ISO-KF DN40 disc valve 316L EPDM weight\", and the row product URL/drawing; found a row-matched AMPROVED product page and drawing but no catalog mass or split material volume."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume is used as the per-unit physical-volume proxy for the complete row item."
    - "Most of the exported volume is treated as 316L/1.4404 stainless steel, with EPDM seal volume small enough that rounding to 0.35 kg is more useful than a false high-precision multi-material split."
  uncertainty_notes:
    - "Mass is limited by lack of a catalog weight and lack of split CAD volumes for stainless parts versus EPDM seals; if the STEP export omits cavities, fasteners, or seal compression detail, the true purchased valve mass may differ."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel valve hardware with EPDM sealing material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html"
    cited_fact_or_basis: "BOM row 264 description/product text includes '_aisi_316l-1_4404_-_epdm'. The manifest maps the same row to CAD file 42C2_valve_part_2 and manufacturer AMPROVED. The assembly STEP material extractor matched 42C2_valve_part_2 but returned material Generic and density 1000.0, which is placeholder metadata under the task criteria and is not used as material evidence. The AMPROVED product route confirms the same ISO-KF DN40 disc valve identity. official_alternate_route_check: original BOM URL is AMPROVED-hosted and the canonical AMPROVED product/drawing route matches the same manufacturer, product family, and DN40 valve geometry."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM material wording identifies the primary metal grade and seal family, but not the detailed breakdown of body, disc, shaft, handle, spring/fastener, and seal subcomponents."
how_to_make:
  summary: "Treat as a purchased AMPROVED ISO-KF DN40 manual disc valve module for current KB planning; local manufacture would require a stainless DN40 valve body/disc/shaft/lever assembly plus EPDM seals, but that sub-BOM is not resolved by this row."
  manufacturing_steps:
    - "Procure or specify one AMPROVED ISO-KF DN40 Scheibenventil matching the BOM URL and material wording AISI 316L / 1.4404 with EPDM sealing."
    - "On receipt, verify the DN40 ISO-KF interface, lever action, and three detent positions against the AMPROVED product description and drawing."
    - "Clean for powder/vacuum service and install with compatible DN40 centering/sealing and clamp hardware as required by the neighboring reAM250 assembly."
    - "For a future local-manufacturing model, decompose into stainless machined/turned valve body, disc, shaft, lever/knob, fasteners or detent hardware, and molded/cut EPDM seals before assigning fabrication recipes."
  source:
    url_or_path: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; https://www.amproved.com/downloads/files/amproved_dn40_scheibenventil.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C2_valve_part_2.step; research/ream250_bom/ream250_bom_row_0264_42C2__views_2x2.png"
    cited_fact_or_basis: "AMPROVED lists the row-matched ISO-KF DN40 disc valve as a purchasable product and states the delivery scope is an ISO-KF DN40 disc valve with 3 detent positions. The drawing and rendered CAD preview show a levered DN40 valve assembly rather than a simple one-piece part. official_alternate_route_check: original BOM URL is AMPROVED-hosted; the canonical AMPROVED product page and AMPROVED drawing PDF match the same DN40 Scheibenventil row identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "Current KB planning should model the row as a vendor functional valve module until a sub-BOM and local valve manufacturing workflow are available."
  uncertainty_notes:
    - "The AMPROVED page supports procurement and gross installation route, but not a detailed local manufacturing process, tolerances, seal profile, detent mechanism design, or internal valve subcomponent quantities."
kb_implications:
  - "item_granularity: purchased_module - row 42C2 is a vendor DN40 manual valve assembly with stainless and EPDM materials; model as a purchased functional module unless later work decomposes the valve body, seal, lever, shaft, and detent subassembly."
---

Research result for reAM250 BOM row 264.
