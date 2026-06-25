---
row_identity:
  item: "84"
  cad_file: "84_valve"
  source_row_number: 280
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PF_A58_204"
function:
  summary: "Pfeiffer Vacuum PF A58 204 is an AVC 040 PA DN 40 ISO-KF electropneumatic high-vacuum angle valve with position indicator and pilot valve; in the reAM250 vacuum train it acts as an isolation/shutoff valve for a DN 40 KF line."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/84_valve.step; https://www.dreebit-service.eu/en/product/detail/avc-040-pa%2C-angle-valve%2C-electropneumatic%2C-with-pi%2C-with-pv%2C-pv-24-v-dc.html"
    cited_fact_or_basis: "BOM row 280 gives item 84, quantity 2, product PF A58 204, manufacturer Pfeiffer Vacuum. DREEBIT row-matched service page names PF A58 204 as 'AVC 040 PA, angle valve, electropneumatic, with PI, with PV, PV 24 V DC' and category Angle Valve. CAD preview shows a right-angle valve body with two KF-style flanged ports and an actuator/indicator body. bom_url_route_check: the BOM Pfeiffer shop route for PF_A58_204 was checked but returned HTTP 403, so the row-matched DREEBIT service page was used to resolve the product function."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Isolation/shutoff duty is inferred from the product category and its placement among adjacent vacuum pump/filter/KF fitting rows in the BOM."
  uncertainty_notes:
    - "The BOM-provided Pfeiffer shop URL returned HTTP 403 from this environment; the row match was preserved through the original URL, BOM product ID, DREEBIT product page, and CAD geometry."
mass:
  value_kg: 1.21
  basis: "Per-unit catalog mass for AVC 040 PA / PF A58 204. BOM quantity is 2, so row total planning mass is about 2.42 kg. Local CAD volume is 528917.741 mm^3 with bounding box about 99.50 x 69.00 x 201.53 mm; using catalog mass implies an effective whole-assembly density near 2288 kg/m^3, plausible for a mixed aluminum valve with steel bellows, elastomer seals, and actuator hardware."
  source:
    url_or_path: "https://www.dianchuvacuum.com/data/upload/image/20240626/1719391402200601.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/84_valve.step"
    cited_fact_or_basis: "Row-matched AVC 040 PA / PF A58 204 catalog PDF search result states weight 1.21 kg. FreeCAD measured one solid, volume 528917.741 mm^3, area 53846.811 mm^2, and bounding box 99.50 x 69.00 x 201.53 mm for 84_valve.step. bom_url_route_check: the BOM Pfeiffer shop route for PF_A58_204 was checked but returned HTTP 403, so the row-matched PDF source was used for mass."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The CAD export is visually and dimensionally consistent with the valve but has only generic STEP material metadata, so the catalog weight is preferred over density-from-volume mass."
material:
  primary_material: "Aluminum housing with stainless steel bellows/feedthrough, FKM sealing elements, and electropneumatic pilot/position-indicator hardware."
  source:
    url_or_path: "https://www.dianchuvacuum.com/data/upload/image/20240626/1719391402200601.pdf; queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py output for 84_valve"
    cited_fact_or_basis: "Row-matched AVC 040 PA / PF A58 204 catalog PDF search result states FKM, aluminum housing, and stainless-steel bellows. Local assembly STEP material extraction for 84_valve returned only Generic with density 1000.0, which is a placeholder and not treated as material evidence. bom_url_route_check: original Pfeiffer shop route for PF_A58_204 was checked first but returned HTTP 403."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Pilot valve, microswitch/position indicator, springs, and fasteners are grouped as actuator hardware because the catalog snippets identify the main housing/seal/bellows materials but not every small subcomponent."
  uncertainty_notes:
    - "Exact aluminum alloy and stainless grade are not resolved from the available row-matched evidence."
how_to_make:
  summary: "Manufacturing route would machine or cast the aluminum angle-valve body, machine KF interfaces and valve seat, Fabricate the stainless bellows/feedthrough, fit FKM seals, assemble the pneumatic actuator, pilot valve, and position indicator, then leak-test and cycle-test the complete valve"
  manufacturing_steps:
    - "For local manufacture, produce the aluminum valve body with right-angle flow path, DN 40 ISO-KF flange geometry, and valve-seat features."
    - "Install stainless bellows/feedthrough, valve plate or poppet, FKM seals, pneumatic actuator, pilot valve, and electrical position-indicator components."
    - "Perform vacuum leak testing, pressure/function checks, and cycle testing before installation."
  source:
    url_or_path: "https://www.dreebit-service.eu/en/product/detail/avc-040-pa%2C-angle-valve%2C-electropneumatic%2C-with-pi%2C-with-pv%2C-pv-24-v-dc.html; research/ream250_bom/ream250_bom_row_0280_84__views_2x2.png"
    cited_fact_or_basis: "DREEBIT identifies the row product as a Pfeiffer Vacuum AVC 040 PA electropneumatic angle valve with PI/PV, and the rendered CAD contact sheet shows an angle-valve body with KF flanges and actuator/indicator package. The detailed fabrication sequence is inferred from this valve architecture and material set."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Use conventional precision machining/casting, elastomer sealing, locally made or separately fabricated bellows, and vacuum component leak-testing practices"
  uncertainty_notes:
    - "Targeted_web_search: queries tried included 'PF A58 204 Pfeiffer Vacuum valve', 'AVC 040 PA 1.21 kg Aluminum FKM', and 'AVC 040 PA Bellows stainless steel 1.21 kg'; results resolved product identity/material/mass but did not provide a manufacturer-stated production process for this valve."
kb_implications:
  - "item_granularity: complex_module - Model as one complex electropneumatic DN40 KF vacuum angle-valve module for near-term KB use; split into aluminum body, stainless bellows, FKM seals, pilot valve, position indicator, and actuator hardware only if valve manufacturing becomes an explicit modeling target."
---
