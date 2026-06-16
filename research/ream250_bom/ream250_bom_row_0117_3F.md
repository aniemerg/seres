---
row_identity:
  item: "3F"
  cad_file: "3F_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 117
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "ISO-KF DN 32-40 stainless clamping ring used to fasten an elastomer-sealed vacuum flange joint."
  source:
    url_or_path: "https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "The BOM-provided Pfeiffer URL redirects to the official Busch Group page for order number 120BSR040. The page identifies the product as a clamping ring for elastomer seal, stainless steel 304/1.4301, DN 32-40 ISO-KF, and states that it is suitable for use with elastomer seals."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.093
  basis: "FreeCAD measured the row STEP volume as 11613.114 mm^3. Converting to 0.000011613114 m^3 and applying the local standard density-table value of 8030 kg/m^3 for stainless steel 304/1.4301 gives 0.09325 kg, rounded to 0.093 kg per clamping ring."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3F_clamping_ring_ISO_KF_DN40_120BSR040.step; kb/materials/properties.yaml; https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "The local STEP measured as one solid with volume 11613.114 mm^3, surface area 7339.078 mm^2, and a 90.35 x 36.90 x 16.00 mm bounding box. The BOM-provided product page states stainless steel 304/1.4301. The local density table lists stainless steel 304 / EN 1.4301 density as 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is used as the physical volume of the stainless clamping ring."
  uncertainty_notes:
    - "Mass is computed from CAD solid volume and density rather than from a vendor-listed item weight."
material:
  primary_material: "stainless steel 304/1.4301"
  source:
    url_or_path: "https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "The BOM-provided Pfeiffer URL redirects to the official Busch Group page whose product title names stainless steel 304/1.4301 and whose page lists order number 120BSR040."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Fabricate as a small stainless ISO-KF clamp ring with an arcuate clamp profile, closure ears, and local fastener or hinge features, then deburr and passivate for vacuum service."
  manufacturing_steps:
    - "Cut or stamp stainless steel 304/1.4301 blank features for the curved clamp body, end ears, hinge or latch details, and fastener holes."
    - "Form the arcuate ISO-KF clamp profile to the DN 32-40 envelope."
    - "Machine, coin, or finish the clamp-profile ribs and local bearing/contact features visible in the STEP preview."
    - "Deburr contact edges, clean, and passivate the stainless steel part before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3F_clamping_ring_ISO_KF_DN40_120BSR040.step; research/ream250_bom/ream250_bom_row_0117_3F__views_2x2.png; https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "BOM-provided product data gives the part family, DN 32-40 ISO-KF interface, and stainless steel 304/1.4301 material. Local CAD geometry and preview show a compact open semi-circular clamp ring with closure ears, holes, ribbed clamp-profile faces, and end features."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from stainless clamp geometry and common fabrication methods for small vacuum fastening hardware."
  uncertainty_notes:
    - "The vendor page does not state the commercial manufacturing process; the actual supplier route may use proprietary stamping, forming, machining, welded subcomponents, or a combination of those steps."
kb_implications:
  - "item_granularity: simple_part - one reusable stainless vacuum clamp part; treat product ID 120BSR040 as procurement traceability, and reuse a generic ISO-KF stainless clamping ring where exact DN 32-40 sizing is not structurally important."
---

Research result for reAM250 BOM row 117, item 3F.
