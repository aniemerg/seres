---
row_identity:
  item: "86"
  cad_file: "86_T_pipe_ISO_KF_DN40"
  source_row_number: 282
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040"
function:
  summary: "DN 40 ISO-KF stainless tee fitting for branching or joining three vacuum lines in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040; https://www.shop.buschgroup.com/global/en/products/170RTS040/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/86_T_pipe_ISO_KF_DN40.step; research/ream250_bom/ream250_bom_row_0282_86__views_2x2.png"
    cited_fact_or_basis: "BOM row 282 identifies item 86 as 86_T_pipe_ISO_KF_DN40, quantity 1, product 170RTS040, manufacturer Pfeiffer Vacuum. The BOM-provided Pfeiffer URL redirects to the official Busch/Pfeiffer shop page, which identifies order number 170RTS040 as a Tee, stainless steel 316L/1.4404, DN 40 ISO-KF under vacuum chambers and components / piping components / tees. FreeCAD measured one CAD solid with bounding box about 130.00 x 94.77 x 59.53 mm; the contact sheet shows a three-port tee with ISO-KF flange lips. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040 redirects to https://www.shop.buschgroup.com/global/en/products/170RTS040/, an official Busch Group/Pfeiffer shop route that preserves order number 170RTS040 and the same DN 40 ISO-KF tee identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.513
  basis: "Use 0.513 kg per tee for KB planning. BOM quantity is 1, so the row total is also about 0.513 kg. FreeCAD volume is about 64,114.012 mm3 = 0.000064114 m3; multiplying by the local stainless_steel density constant 8000 kg/m3 gives about 0.5129 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/86_T_pipe_ISO_KF_DN40.step; kb/materials/properties.yaml; https://www.shop.buschgroup.com/global/en/products/170RTS040/"
    cited_fact_or_basis: "FreeCAD measured one solid, volume about 64,114.012 mm3, area about 49,670.033 mm2, and bounding box about 130.00 x 94.77 x 59.53 mm. The official Busch/Pfeiffer product page identifies the part as stainless steel 316L/1.4404. kb/materials/properties.yaml lists stainless_steel density as 8000 kg/m3. official_alternate_route_check: the BOM-provided Pfeiffer URL redirects to the official Busch/Pfeiffer shop page for the same order number 170RTS040; that route resolved the material used with the CAD volume."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the physical metal volume of one tee closely enough for a per-unit planning mass."
    - "The local generic stainless_steel density constant is used for 316L/1.4404 because the local table has no separate 316L entry."
  uncertainty_notes:
    - "Small deviations are possible from CAD tessellation/export simplification and from using a generic stainless density rather than a 316L-specific density."
material:
  primary_material: "Stainless steel 316L / EN 1.4404."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040; https://www.shop.buschgroup.com/global/en/products/170RTS040/; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "The BOM row gives product 170RTS040 and manufacturer Pfeiffer Vacuum. The BOM-provided Pfeiffer URL redirects to the official Busch/Pfeiffer shop page, whose product title identifies order number 170RTS040 as a Tee, stainless steel 316L/1.4404, DN 40 ISO-KF. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040 redirects to https://www.shop.buschgroup.com/global/en/products/170RTS040/, an official route matching the same order number and tee product."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Near-term route is to procure Pfeiffer/Busch order number 170RTS040 as a finished DN 40 ISO-KF stainless tee and install it into the vacuum plumbing with compatible ISO-KF seals and clamps."
  manufacturing_steps:
    - "Procure the catalog 170RTS040 DN 40 ISO-KF tee from the Pfeiffer/Busch product route."
    - "Inspect the three KF flange faces and sealing lips, clean for vacuum service, and install with the required centering rings, seals, and clamps."
    - "Leak-check the assembled branch connection as part of the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.shop.buschgroup.com/global/en/products/170RTS040/; research/ream250_bom/ream250_bom_row_0282_86__views_2x2.png"
    cited_fact_or_basis: "BOM row 282 identifies product 170RTS040 from Pfeiffer Vacuum. The official Busch/Pfeiffer product page identifies the same order number as a DN 40 ISO-KF stainless tee. The CAD contact sheet shows a finished three-flange tee fitting rather than raw stock or a calibrated subsystem. official_alternate_route_check: the BOM-provided Pfeiffer URL redirects to the official Busch/Pfeiffer shop page for the same order number, so the procurement route is row-matched."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row is intended to represent the finished catalog tee, not the clamps or seals needed to install it."
  uncertainty_notes:
    - "A future local fabrication recipe would still need weld/braze method, flange forming, internal finish, cleaning, and leak-test requirements; those are not specified by the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable finished ISO-KF stainless tee fitting; keep clamps, centering rings, and seals as separate hardware or consumable rows rather than folding them into this tee."
---
