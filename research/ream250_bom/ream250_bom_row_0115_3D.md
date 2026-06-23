---
row_identity:
  item: "3D"
  cad_file: "3D_ISO_KF_DN40_hose_connection_110ASC040-12"
  source_row_number: 115
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/110ASC040_12"
function:
  summary: "DN 40 ISO-KF hose connector fitting that provides a vacuum-compatible transition from an ISO-KF flange face to a barbed hose connection in the gas circulation plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3D_ISO_KF_DN40_hose_connection_110ASC040-12.step; research/ream250_bom/ream250_bom_row_0115_3D__views_2x2.png"
    cited_fact_or_basis: "BOM row 115 identifies item 3D as 110ASC040-12 from Pfeiffer Vacuum and describes it as a 3D_ISO_KF_DN40_hose_connection. The CAD preview shows a round KF flange disk with a central through bore and ribbed hose-barb stem."
    evidence_basis: "bom_provided"
  assumptions:
    - "The adjacent BOM context with DN40 reducer and DN40 seal/filter means this connector belongs to the DN40 vacuum/gas line rather than a general structural mount."
  uncertainty_notes: []
mass:
  value_kg: 0.0302
  basis: "Per-unit mass for quantity 1. FreeCAD measured one solid with volume 11178.519 mm^3, equal to 1.1178519e-5 m^3. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 0.03018 kg, rounded to 0.0302 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3D_ISO_KF_DN40_hose_connection_110ASC040-12.step; https://www.idealvac.com/files/manuals/Pfeiffer_Vacuum_Technology_Chambers_and_Components.pdf; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured volume 11178.519 mm^3 and bounding box about 40.00 x 59.53 x 59.53 mm. The Pfeiffer catalog row for 110ASC040-12 lists the item under Aluminum EN AW-6082/3.2315. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. bom_url_route_check: the BOM-provided Pfeiffer URL was checked first but returned only an anti-bot wrapper in local curl; the Ideal Vacuum route exposed a Pfeiffer catalog PDF with an exact 110ASC040-12 row."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "CAD volume represents the solid aluminum connector body and does not include packaging or separately installed clamp/seal parts."
  uncertainty_notes:
    - "The full assembly STEP material extractor returned only Generic with density 1000.0 for this row, so material was resolved from the exact catalog row instead of local STEP metadata."
material:
  primary_material: "Aluminum EN AW-6082/3.2315"
  source:
    url_or_path: "https://www.idealvac.com/files/manuals/Pfeiffer_Vacuum_Technology_Chambers_and_Components.pdf"
    cited_fact_or_basis: "The Pfeiffer catalog ISO-KF hose connection table lists order number 110ASC040-12 for DN 40 KF under Aluminum EN AW-6082/3.2315, with A 40 mm, B 12 mm, and C 7 mm. bom_url_route_check: the original BOM Pfeiffer shop route was checked first but did not expose parseable product facts through local curl; the exact product was then resolved through a Pfeiffer catalog PDF linked from the Ideal Vacuum product page."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "A distributor page contains generic stainless-steel wording for LF fittings, but the exact Pfeiffer catalog row places 110ASC040-12 in the aluminum section; the exact row was preferred."
how_to_make:
  summary: "Procure as Pfeiffer Vacuum 110ASC040-12 DN 40 ISO-KF hose connector; a local substitute would be machined as a one-piece aluminum KF flange and hose-barb fitting."
  manufacturing_steps:
    - "Procurement route: order the finished Pfeiffer 110ASC040-12 hose connector and install it with the matching DN40 ISO-KF seal/filter and clamp hardware."
    - "Local fabrication route if needed: machine or turn EN AW-6082 aluminum bar/forging into the KF flange face, central bore, shoulder, and hose-barb ribs, then deburr and clean for vacuum service."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.idealvac.com/files/manuals/Pfeiffer_Vacuum_Technology_Chambers_and_Components.pdf; research/ream250_bom/ream250_bom_row_0115_3D__views_2x2.png"
    cited_fact_or_basis: "BOM row 115 specifies Pfeiffer Vacuum 110ASC040-12. The Pfeiffer catalog identifies 110ASC040-12 as a DN 40 KF hose connection in Aluminum EN AW-6082/3.2315. The rendered CAD preview shows a one-piece flange plus hose-barb geometry. bom_url_route_check: the BOM Pfeiffer shop URL was checked first but did not expose parseable product details locally; the linked Pfeiffer catalog route resolved the exact order number."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD shape is a single machined connector body, so machining from aluminum stock is the plausible local manufacturing route."
  uncertainty_notes:
    - "No row-specific process drawing or tolerance callout was found; vacuum sealing dimensions should be checked against ISO 2861/Pfeiffer drawings before local manufacture."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable DN40 ISO-KF aluminum hose-connector fitting rather than a multi-component assembly; clamp and seal/filter remain separate BOM rows."
---
