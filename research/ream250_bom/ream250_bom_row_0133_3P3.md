---
row_identity:
  item: "3P3"
  cad_file: "3P3_valve_ISO_K_DN63_310VEP063-01"
  source_row_number: 133
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02"
function:
  summary: "Pfeiffer Vacuum EVB 063 PA electro-pneumatic bellows-sealed normally closed angle isolation valve for a DN 63 ISO-K vacuum connection, with pilot valve and position indicator."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 133 identifies item 3P3 as Pfeiffer Vacuum product 310VEP063. The official Pfeiffer shop route names 310VEP063-02 as EVB 063 PA angle valve, lists DN 63 ISO-K connection flange, electro-pneumatic actuator, normally closed operation, bellows sealing, visual position indicator, pilot valve, and type Angle valve. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions:
    - "In the reAM250 vacuum plumbing, this valve is treated as an isolation/control valve for opening or closing a DN 63 ISO-K vacuum path."
  uncertainty_notes:
    - "The BOM row does not state the exact connected chamber, pump branch, or pneumatic control circuit location for item 3P3."
mass:
  value_kg: 3.9
  basis: "Per-unit catalog weight for quantity 1. BOM quantity is 1, so the row total is also 3.9 kg. The local per-row STEP measured only 257.185 mm^3 with an 5.80 x 8.50 x 8.50 mm bounding box, which is far smaller than the catalog dimensions A 232 mm, B 108 mm, C 191 mm, D 88 mm; the catalog weight is therefore used instead of CAD-derived volume mass."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P3_valve_ISO_K_DN63_310VEP063-01.step"
    cited_fact_or_basis: "The official Pfeiffer shop route lists Weight 3.9 kg for 310VEP063-02 and dimensions A 232, B 108, C 191, D 88 mm. FreeCAD measured the supplied row STEP as one solid, volume 257.185 mm^3, area 298.272 mm^2, and bounding box 5.80 x 8.50 x 8.50 mm. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row product ID 310VEP063 is interpreted as the shop product 310VEP063-02 shown by the BOM-provided URL route."
  uncertainty_notes:
    - "The local CAD file appears to be a small proxy or incomplete exported subshape rather than the full valve body, so it is not suitable for a volume-derived mass estimate."
material:
  primary_material: "aluminum housing; FKM seal; stainless steel bellows/feedthrough; electro-pneumatic actuator, pilot valve, and microswitch position indicator components"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official Pfeiffer shop route lists Seal: FKM, Feedthrough: Bellows and Stainless steel, Housing: Aluminum, and Position indicator: Microswitch included. Local assembly STEP material extraction for product 3P3_valve_ISO_K_DN63_310VEP063-01 returned only Generic with density 1000.0, which is placeholder metadata. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source resolves component material families but not aluminum alloy, stainless grade, actuator internal materials, or microswitch construction."
how_to_make:
  summary: "Procure as the Pfeiffer 310VEP063-02 electro-pneumatic angle valve module; a local manufacturing route would require a machined aluminum valve body, stainless bellows/feedthrough assembly, FKM sealing elements, pneumatic actuator/pilot hardware, position-indicator microswitch integration, and vacuum leak/performance testing."
  manufacturing_steps:
    - "For near-term KB modeling, purchase or import the row as a calibrated vendor valve module matching Pfeiffer 310VEP063-02."
    - "If modeled for local production later, machine the DN 63 ISO-K aluminum angle-valve body and sealing interfaces."
    - "Fabricate or procure the stainless bellows/feedthrough and install the FKM sealing elements."
    - "Assemble the electro-pneumatic actuator, pilot valve, and microswitch position indicator."
    - "Clean, leak-test, cycle-test, and verify vacuum tightness, pressure range, 24 V DC controls, and open/close timing."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; research/ream250_bom/ream250_bom_row_0133_3P3__views_2x2.png"
    cited_fact_or_basis: "The official Pfeiffer shop route identifies the purchased valve module and lists DN 63 ISO-K flange, electro-pneumatic actuator, pilot valve, position indicator, aluminum housing, FKM seal, stainless steel bellows/feedthrough, tightness 1e-10 Pa m3/s, service life 3,000,000 cycles, and closing/opening time 300 ms/300 ms. The CAD contact sheet shows only a small cylindrical/faceted proxy rather than the full valve. targeted_web_search: searched 'Pfeiffer Vacuum 310VEP063 3/2 way valve ISO-K DN63', '310VEP063-02 EVB 063 PA datasheet', and 'Pfeiffer 310VEP063 material weight'; found row-matched product and datasheet facts but no row-specific manufacturing-process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed local manufacturing steps are inferred from the sourced module function, component materials, and standard vacuum-valve construction; the source supports procurement and component facts, not the factory process."
    - "Vacuum service requires precision sealing surfaces, clean assembly, and leak testing even if not all inspection details are specified in the BOM."
  uncertainty_notes:
    - "The vendor evidence resolves procurement identity and performance requirements, but not internal actuator sub-BOM, bellows forming method, seal geometry, or factory acceptance-test procedure."
kb_implications:
  - "item_granularity: purchased_module - Treat as a vendor electro-pneumatic vacuum valve subsystem for now; later KB work can split it only if valve body, bellows, actuator, seals, controls, and calibration/leak-test workflows are modeled."
---

Result generated for the leased reAM250 BOM row only.
