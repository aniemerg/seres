---
row_identity:
  item: "42C3"
  cad_file: "42C3_valve_part_3"
  source_row_number: 265
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "AMPROVED ISO-KF DN40 manual disc valve component or subassembly for shutting and manually controlling powder/fluid flow at a DN40 KF port in the reAM250 machine."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C3_valve_part_3.step; research/ream250_bom/ream250_bom_row_0265_42C3__views_2x2.png; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html"
    cited_fact_or_basis: "BOM row 265 states item 42C3, quantity 1, CAD file 42C3_valve_part_3, manufacturer AMPROVED, and links to the AMPROVED ISO-KF DN40 Scheibenventil. The manifest maps the row to gold_export/parts/42C3_valve_part_3.step as a matched vendor_component. FreeCAD measured one solid with bounding box 72.00 x 97.00 x 97.00 mm. The rendered contact sheet shows KF-style side flanges, a central bore, and a larger round valve body/disc feature. The AMPROVED canonical page describes an ISO-KF DN40 disc valve for manually controlling fluid streams in piping and closing powder bottles, overflows, and filling ports in AM machines, supplied with 3 detent positions. official_alternate_route_check: the original BOM URL https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html resolves to the same first-party AMPROVED product at https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; manufacturer, DN40 disc-valve name, and product family match the BOM row."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because this row is one exported vendor_component from a multi-part valve CAD set, it is treated as the row's valve component/subassembly rather than reinterpreted as a different AMPROVED product."
  uncertainty_notes:
    - "The row-level CAD and BOM identify the DN40 valve component role, but not which internal valve member, housing half, or seal subcomponent the vendor CAD part number 3 corresponds to."
mass:
  value_kg: 1.22
  basis: "FreeCAD volume 153137.310 mm^3 equals 0.000153137 m^3. Using the local stainless_steel density 8000 kg/m^3 gives 1.225 kg, rounded to 1.22 kg per physical item. BOM quantity is 1, so row total is also about 1.22 kg. If the whole volume were modeled as AISI 316L at 7900 kg/m^3 from the vendor-material reference, the estimate would be about 1.21 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C3_valve_part_3.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 153137.310 mm^3, area 44760.364 mm^2, and bounding box 72.00 x 97.00 x 97.00 mm. BOM row 265 describes the row material text as _aisi_316l-1_4404_-_epdm: part 3. The local density table lists stainless_steel density 8000 kg/m^3. The AMPROVED product page identifies the row-matched item as an ISO-KF DN40 disc valve. targeted_web_search: searched \"AMPROVED ISO-KF DN 40 Scheibenventil AISI 316L EPDM weight\", \"AMPROVED SV04 DIN CC DN40 mass\", and \"ISO-KF DN40 Scheibenventil 316L EPDM weight\"; found the row-matched AMPROVED product page and general valve/316L references, but no row-specific mass or material-fraction table."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the per-unit physical-volume proxy for this exported vendor component."
    - "The stainless body dominates mass; EPDM seal volume is assumed small enough that the all-stainless calculation is a planning-level estimate rather than a precise weighed mass."
  uncertainty_notes:
    - "The CAD export is a single solid and the STEP assembly metadata returns only Generic material with density 1000.0, so it does not provide a split between stainless and EPDM material regions."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel with EPDM sealing material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.amproved.com/iso-kf-dn-40-scheibenventil.html"
    cited_fact_or_basis: "BOM row 265 material/product text states _aisi_316l-1_4404_-_epdm: part 3. The assembly STEP material extractor matched 42C3_valve_part_3 but returned material Generic and density 1000.0, which is placeholder metadata under the task rules. The AMPROVED canonical product route confirms the linked row is the ISO-KF DN40 disc valve. official_alternate_route_check: the original BOM URL resolves to the first-party AMPROVED canonical product page on the same domain, matching manufacturer AMPROVED and the ISO-KF DN40 Scheibenventil product family."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM-side material wording gives the family/grade set but does not assign exact material regions to the visible CAD subfeatures."
how_to_make:
  summary: "Best current route is procurement as the AMPROVED ISO-KF DN40 disc valve or matched spare valve component; a later local route would machine/passivate the 316L stainless valve body features and assemble the EPDM sealing element and detent/actuation hardware."
  manufacturing_steps:
    - "Procure the AMPROVED ISO-KF DN40 Scheibenventil or row-matched spare component through the BOM-provided product route."
    - "For a local manufacturing study, machine the stainless valve body/disc geometry from 316L/1.4404 stainless stock, including KF flange faces, central bore, and fastener or detent features visible in CAD."
    - "Passivate and clean stainless wetted or powder-contact surfaces for vacuum/powder-service compatibility."
    - "Mold, cut, or procure the EPDM seal element and assemble it to the stainless valve body with the manual detent/actuation components from the sibling valve rows."
    - "Inspect KF interface dimensions, valve motion, three-position detent behavior, and leak or powder-sealing performance."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/42C3_valve_part_3.step; research/ream250_bom/ream250_bom_row_0265_42C3__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "The AMPROVED product page provides the procurement route for the ISO-KF DN40 disc valve and states it is supplied as a disc valve with 3 detent positions for manual control/closure in AM-machine powder/fluid paths. CAD preview shows machined valve-body/flange geometry. BOM row 265 states AISI 316L/1.4404 and EPDM material wording. targeted_web_search: searched \"AMPROVED ISO-KF DN 40 Scheibenventil drawing material\", \"AMPROVED DN40 Scheibenventil manufacturing\", and \"SV04 DIN CC DN40 316L EPDM\"; found the first-party product page and image-only 2D drawing route, but no source that states detailed manufacturing operations."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed machining, passivation, EPDM forming, and assembly steps are inferred from the CAD geometry, material wording, and normal construction of a stainless/EPDM manual valve, not stated by the vendor page."
    - "The three sibling valve CAD rows should be considered together before any later KB itemization decides whether to keep this as a vendor module or split a local sub-BOM."
  uncertainty_notes:
    - "No row-specific vendor drawing with tolerances, seal cross-section, internal mechanism details, or weighed mass was available from the searchable product route."
kb_implications:
  - "item_granularity: complex_module - model the AMPROVED ISO-KF DN40 disc valve rows as a functional valve module first, with later consolidation of sibling valve parts before attempting a detailed stainless-body, EPDM-seal, and actuator sub-BOM.; defer internal decomposition until a focused sub-BOM and manufacturing workflow are modeled."
---

Research result for reAM250 BOM row 265.
