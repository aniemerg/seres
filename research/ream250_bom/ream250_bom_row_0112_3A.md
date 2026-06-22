---
row_identity:
  item: 3A
  cad_file: 3A_angle_pipe_ISO_K_DN63_320RRB063-90
  source_row_number: 112
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
  link_url: https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90
function:
  summary: Standard DN 63 ISO-K 90-degree radius elbow used to turn a vacuum line while preserving the ISO-K flange interface.
  source:
    url_or_path: https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90
    cited_fact_or_basis: "BOM row 112 lists item 3A, quantity 15, Pfeiffer Vacuum product 320RRB063-90; the BOM URL redirects to the official Busch/Pfeiffer shop page titled 90-degree elbow, radius, stainless steel 304/1.4301, DN 63 ISO-K, order number 320RRB063-90. CAD preview shows a flanged 90-degree pipe elbow. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com; redirected official shop URL is https://www.shop.buschgroup.com/global/en/products/320RRB063_90/ with Pfeiffer branding and the same order number."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.999
  basis: "Per-unit estimate from FreeCAD material volume 124399.904 mm^3 = 0.000124399904 m^3 multiplied by local stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml. BOM quantity is 15, giving an approximate row total of 14.98 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3A_angle_pipe_ISO_K_DN63_320RRB063-90.step; kb/materials/properties.yaml; https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 124399.904 mm^3, area 81713.913 mm^2, and bounding box about 140.57 x 140.57 x 105.13 mm. Official redirected Pfeiffer/Busch product route identifies material as stainless steel 304/1.4301 for order number 320RRB063-90. Local density table gives stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com; redirected official shop URL is https://www.shop.buschgroup.com/global/en/products/320RRB063_90/ with Pfeiffer branding and the same order number."
    evidence_basis: bom_provided
  assumptions:
    - The STEP solid volume represents the material volume for one elbow, not only an envelope volume.
  uncertainty_notes:
    - CAD tessellation/render metadata reported a slightly smaller preview bounding box than the direct FreeCAD shape read; mass uses the direct FreeCAD volume.
material:
  primary_material: stainless steel 304 / EN 1.4301
  source:
    url_or_path: https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90
    cited_fact_or_basis: "The official redirected Pfeiffer/Busch shop page for order number 320RRB063-90 titles the product as a DN 63 ISO-K 90-degree elbow in stainless steel 304/1.4301. The local assembly STEP material extractor returned only placeholder material Generic at density 1000.0, so it was not used to resolve material. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com; redirected official shop URL is https://www.shop.buschgroup.com/global/en/products/320RRB063_90/ with Pfeiffer branding and the same order number."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: Treat as a purchased standard Pfeiffer Vacuum ISO-K elbow; later local modeling can represent it as a stainless vacuum piping component if procurement is replaced.
  manufacturing_steps:
    - Procure Pfeiffer Vacuum order number 320RRB063-90 or a fully equivalent DN 63 ISO-K stainless 304/1.4301 90-degree radius elbow.
    - Install between compatible DN 63 ISO-K vacuum flanges with the appropriate centering ring, seal, and clamps from adjacent BOM rows or system hardware.
  source:
    url_or_path: https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90
    cited_fact_or_basis: "BOM row 112 provides the Pfeiffer Vacuum product identity and URL; the official redirected shop route identifies order number 320RRB063-90 as a standard DN 63 ISO-K 90-degree elbow in stainless steel 304/1.4301. official_alternate_route_check: original BOM URL is pfeiffer-vacuum.com; redirected official shop URL is https://www.shop.buschgroup.com/global/en/products/320RRB063_90/ with Pfeiffer branding and the same order number."
    evidence_basis: bom_provided
  assumptions:
    - Procurement is the intended near-term route for this vendor component row.
  uncertainty_notes:
    - No sub-process route for forming, welding, passivation, leak testing, or flange finishing is modeled here.
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard vacuum piping hardware, not as raw pipe stock or a calibrated purchased module; variants can be keyed by ISO-K nominal diameter, elbow angle, radius, and stainless grade."
---
