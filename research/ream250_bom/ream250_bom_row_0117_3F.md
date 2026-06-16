---
row_identity:
  item: "3F"
  cad_file: "3F_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 117
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "ISO-KF DN 32-40 clamping ring used to fasten an elastomer-sealed vacuum flange joint."
  source:
    url_or_path: "https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "The BOM-provided product URL redirects to the Busch Group product page for order number 120BSR040. The page title identifies the item as a clamping ring for elastomer seal, stainless steel 304/1.4301, DN 32-40 ISO-KF, and the Product Information section says it is suitable for use with elastomer seals."
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
    - "Mass is computed from CAD solid volume and density, not copied from a vendor-listed item weight."
material:
  primary_material: "stainless steel 304/1.4301"
  source:
    url_or_path: "https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "The BOM-provided product page title names the material as stainless steel 304/1.4301 and lists order number 120BSR040."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Fabricate as a small stainless ISO-KF clamp ring with a formed arcuate clamp profile and closure ears, then deburr and passivate for vacuum service."
  manufacturing_steps:
    - "Cut or stamp stainless steel 304/1.4301 blank features for the curved clamp body, end ears, hinge/latch details, and fastener holes."
    - "Form the arcuate ISO-KF clamp profile to the DN 32-40 envelope."
    - "Machine or coin the clamp-profile ribs and local bearing/contact features visible in the STEP preview."
    - "Deburr contact edges, clean, and passivate the stainless steel part before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3F_clamping_ring_ISO_KF_DN40_120BSR040.step; research/ream250_bom/ream250_bom_row_0117_3F__views_2x2.png; https://www.shop.buschgroup.com/global/en/products/120BSR040/"
    cited_fact_or_basis: "BOM-provided product data gives the part family and material. Local CAD geometry and preview show a compact open semi-circular clamp ring with closure ears, holes, ribbed clamp-profile faces, and hinge/latch or fastener end features."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Manufacturing route is inferred from stainless clamp geometry and common fabrication methods for small vacuum fastening hardware."
  uncertainty_notes:
    - "The vendor page does not state the commercial manufacturing process; the actual supplier route may use proprietary stamping, forming, machining, welded subcomponents, or a combination of those steps."
kb_implications:
  - "Suggested item kind: part."
  - "Suggested material class: stainless_steel."
  - "Suggested mass: 0.093 kg each; row quantity is 3 units, about 0.280 kg total."
  - "Reuse a generic ISO-KF stainless clamping ring part where exact DN 32-40 sizing is not structurally important; keep product ID 120BSR040 in notes for procurement traceability."
  - "This is a purchased/vendor vacuum fitting candidate unless the KB later models local production of stainless vacuum flange hardware."
---

Research result for reAM250 BOM row 117, item 3F.
