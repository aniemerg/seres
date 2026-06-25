---
row_identity:
  item: "88"
  cad_file: "88_pressure_gauge"
  source_row_number: 284
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PT_T11_138_310"
function:
  summary: "Vacuum pressure gauge for measuring total pressure in the reAM250 vacuum system; the row-matched product is a Pfeiffer/Busch TTR 101 Pirani/capacitive gauge with DN 16 ISO-KF interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/PT_T11_138_310; research/ream250_bom/ream250_bom_row_0284_88__views_2x2.png"
    cited_fact_or_basis: "BOM row 284 and the manifest identify item 88 as 88_pressure_gauge, quantity 1, product PT T11 138 310, manufacturer Pfeiffer Vacuum. The BOM URL redirects to the official Busch Group shop route for order number PT T11 138 310, titled TTR 101, Pirani/capacitive gauge, DN 16 ISO-KF. The refreshed CAD contact sheet shows a compact gauge-like vendor component body. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/PT_T11_138_310 redirects to https://www.shop.buschgroup.com/global/en/products/PT_T11_138_310/; the alternate route is official because the page carries Busch Group and Pfeiffer Vacuum branding and preserves order number PT T11 138 310."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM filename pressure_gauge is interpreted as the local machine role, while the official product route resolves the specific vacuum gauge type."
  uncertainty_notes: []
mass:
  value_kg: 0.12
  basis: "Per-unit mass for BOM quantity 1 is 0.12 kg, from the Pfeiffer TTR 101 PT T11 138 310 datasheet weight of 120 g. FreeCAD measured the supplied STEP as 1 solid, volume 146082.473 mm^3, surface area 15884.110 mm^2, and bounding box 66.00 x 86.40 x 70.84 mm; the rendered triage preview reports a visible compact body about 66.0 x 60.0 x 44.8 mm. The vendor mass is used because the CAD appears to be simplified geometry for a multi-material instrument."
  source:
    url_or_path: "https://cdn.abicart.com/shop/ws28/75628/art17/204883117-7379af-PTT11138310.en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/88_pressure_gauge.step"
    cited_fact_or_basis: "The Pfeiffer TTR 101 PT T11 138 310 datasheet lists weight 120 g. FreeCAD measured the row STEP as 1 solid with volume 146082.473 mm^3. bom_url_route_check: the BOM-provided URL redirected to the official Busch Group product page and confirmed product/order identity, but the parsed shop page did not expose the weight field; the row-matched Pfeiffer datasheet was used for the mass value."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The datasheet weight applies to one physical gauge represented by the BOM row."
    - "The CAD solid is used for geometry corroboration only, not density-based mass calculation."
  uncertainty_notes:
    - "The STEP material extractor returned only Generic with density 1000.0, so CAD volume is not a resolved material-density mass basis."
material:
  primary_material: "multi-material vacuum gauge assembly; resolved interface materials include stainless steel flange, metal seal, glass feedthrough, and tungsten filament"
  source:
    url_or_path: "https://cdn.abicart.com/shop/ws28/75628/art17/204883117-7379af-PTT11138310.en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer TTR 101 PT T11 138 310 datasheet lists flange material stainless steel, seal metal, feedthrough glass, and filament tungsten. Local assembly STEP material extraction for 88_pressure_gauge reports only Generic with density 1000.0. bom_url_route_check: the BOM-provided URL redirected to the official Busch Group product page and confirmed product/order identity, but the parsed shop page exposed only summary product information; the row-matched Pfeiffer datasheet was used for detailed material facts."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The item is treated as a multi-material purchased instrument because only selected internal and vacuum-interface materials are specified, not the full electronics and housing material stack."
  uncertainty_notes:
    - "Outer housing, PCB, connector, and sensor-package materials are not fully specified by the available row-matched evidence."
how_to_make:
  summary: "Treat as a purchased/calibrated vacuum gauge module. A plausible production route is precision fabrication of the DN 16 ISO-KF stainless vacuum interface, integration of Pirani and capacitive sensing elements, electronic assembly, sealing, cleaning, leak testing, and calibration."
  manufacturing_steps:
    - "Fabricate or procure the stainless DN 16 ISO-KF vacuum flange and metal-sealed gauge body interface."
    - "Install the glass feedthrough, tungsten Pirani element, capacitive sensing element, and vacuum-compatible internal structure."
    - "Assemble signal-conditioning electronics and the FCC 68/RJ45 8-pin connector interface."
    - "Seal, clean, and leak-test the gauge head for vacuum service."
    - "Calibrate the instrument across its pressure range before machine installation."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PT_T11_138_310; https://cdn.abicart.com/shop/ws28/75628/art17/204883117-7379af-PTT11138310.en.pdf; research/ream250_bom/ream250_bom_row_0284_88__views_2x2.png"
    cited_fact_or_basis: "The official BOM URL route identifies PT T11 138 310 as a TTR 101 Pirani/capacitive gauge with DN 16 ISO-KF interface, metal sealing, bakeout rating, and FCC 68/RJ45 connector. The Pfeiffer datasheet adds measuring method, stainless flange, metal seal, glass feedthrough, tungsten filament, max power, and measuring range. targeted_web_search: searched 'PT T11 138 310 Pfeiffer Vacuum pressure gauge material weight', 'PT_T11_138_310 Pfeiffer Vacuum TTR 101 datasheet', and 'TTR 101 PT T11 138 310 datasheet manufacturing'; found row-matched product/catalog data but no vendor factory process route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because this is a calibrated sensor/electronics module, later KB modeling should initially use procurement/import rather than local fabrication of subcomponents."
    - "The manufacturing steps are a functional decomposition inferred from the product type and specified materials, not a Pfeiffer factory traveler."
  uncertainty_notes:
    - "No row-matched source was found that describes the actual factory assembly or calibration workflow."
kb_implications:
  - "item_granularity: complex_module - calibrated commercial vacuum gauge with sensing elements and electronics; model as a complex module unless a future detailed sensor sub-BOM is intentionally added.; defer internal decomposition until a focused sub-BOM and manufacturing workflow are modeled."
---

Research result for reAM250 BOM row 284.
