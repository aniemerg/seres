---
row_identity:
  item: "8B"
  cad_file: "8B_angle_pipe_ISO_KF_DN40"
  source_row_number: 207
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90"
function:
  summary: "DN 40 ISO-KF 90 degree vacuum elbow fitting that turns a vacuum line through a right angle while preserving ISO-KF clamp-flange interfaces at both ends."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8B_angle_pipe_ISO_KF_DN40.step; research/ream250_bom/ream250_bom_row_0207_8B__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "BOM row 207 identifies item 8B, quantity 5, CAD file 8B_angle_pipe_ISO_KF_DN40, product 110RRB040-90, and manufacturer Pfeiffer Vacuum. The manifest maps row 207 to gold_export/parts/8B_angle_pipe_ISO_KF_DN40.step as a matched vendor component. The vendor route identifies order number 110RRB040-90 as an elbow fitting, 90 degrees, with DN 40 ISO-KF connection flange. FreeCAD measured one solid with a 94.77 x 94.77 x 59.53 mm raw bounding box; the rendered contact sheet shows a right-angle tube with KF-style flanged ends. official_alternate_route_check: the BOM URL is on pfeiffer-vacuum.com for product 110RRB040_90; the vacuum-shop.com page is a Pfeiffer Vacuum Components & Solutions shop page for the same order number 110RRB040-90 and global number 2000050096, so it is treated as an official alternate route for the same row."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single exported STEP solid represents one physical elbow fitting in the BOM row."
  uncertainty_notes:
    - "Local evidence identifies the elbow's connection role, but not the exact mating hose, pipe, or chamber ports in the reAM250 assembly."
mass:
  value_kg: 0.141
  basis: "FreeCAD volume 52,397.365 mm^3 equals 0.000052397365 m^3. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 0.000052397365 m^3 * 2700 kg/m^3 = 0.14147 kg per unit, rounded to 0.141 kg. BOM quantity is 5, so the row total is about 0.707 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8B_angle_pipe_ISO_KF_DN40.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 52,397.365 mm^3, area 36,746.774 mm^2, and raw bounding box 94.77 x 94.77 x 59.53 mm. The vendor route identifies the part material as aluminum 3.2315/EN AW-6082. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. official_alternate_route_check: the BOM URL is on pfeiffer-vacuum.com for product 110RRB040_90; the vacuum-shop.com page is a Pfeiffer Vacuum Components & Solutions shop page for the same order number 110RRB040-90 and global number 2000050096, so it is treated as an official alternate route for the same row."
    evidence_basis: "bom_provided"
  assumptions:
    - "The isolated CAD solid volume is used as the complete per-unit volume for one elbow fitting."
    - "The local aluminum density is used as a calculation constant for EN AW-6082 because the local density table has aluminum but not that specific alloy."
  uncertainty_notes:
    - "The estimate depends on CAD volume fidelity; the vendor page does not provide a catalog weight for cross-checking."
material:
  primary_material: "aluminum 3.2315 / EN AW-6082"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/110RRB040_90; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 8B_angle_pipe_ISO_KF_DN40 returned material Generic with density 1000.0, which is placeholder metadata under the task criteria and does not resolve material. The vendor route states material and media-contact material as aluminum 3.2315/EN AW-6082 for order number 110RRB040-90. official_alternate_route_check: the BOM URL is on pfeiffer-vacuum.com for product 110RRB040_90; the vacuum-shop.com page is a Pfeiffer Vacuum Components & Solutions shop page for the same order number 110RRB040-90 and global number 2000050096, so it is treated as an official alternate route for the same row."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Surface treatment, cleaning specification, and exact temper are not stated by the row evidence."
how_to_make:
  summary: "Locally manufacture as a one-piece aluminum ISO-KF 90 degree elbow by forming or machining the elbow body and KF flange lips, then finish-machining and leak-checking the vacuum interfaces."
  manufacturing_steps:
    - "Start from EN AW-6082 or equivalent aluminum billet, tube stock, or near-net elbow blank sized for a DN 40 ISO-KF 90 degree fitting."
    - "Create the right-angle flow passage by CNC machining from a near-net blank, or by bending/forming an aluminum tube followed by joining or integral-forming of the KF flange lips."
    - "CNC turn or mill both ISO-KF flange faces, centering diameters, clamp lips, and sealing faces to the standard DN 40 interface geometry."
    - "Deburr internal edges, clean for vacuum service, and inspect flange dimensions, face finish, and passage continuity."
    - "Helium leak-test or pressure/vacuum test the finished elbow before assembly into the vacuum line."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8B_angle_pipe_ISO_KF_DN40.step; research/ream250_bom/ream250_bom_row_0207_8B__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2072920/product/110rrb04090/elbow-fitting-90-aluminum-3-2315-en-aw-6082.html; web_search"
    cited_fact_or_basis: "The vendor route identifies a DN 40 ISO-KF 90 degree aluminum elbow. The STEP/contact sheet show a single right-angle elbow with integral KF-style flange lips and no separate subassemblies. targeted_web_search: queries tried \"Pfeiffer Vacuum 110RRB040-90 manufacturing\", \"110RRB040-90 drawing material weight\", and \"ISO-KF DN40 aluminum elbow manufacturing\" results resolved product identity, material, and dimensions, but did not provide a row-specific manufacturing process plan."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The route is a plausible local-manufacturing route inferred from the one-piece aluminum vacuum-fitting geometry; the cited vendor page does not specify the production process."
    - "Leak testing and vacuum cleaning are included because the component is a vacuum piping fitting."
  uncertainty_notes:
    - "The actual commercial process may use casting, forging, bent tube plus welded flanges, or another near-net route; the row evidence does not specify which."
kb_implications:
  - "item_granularity: simple_part - model later as reusable DN 40 ISO-KF aluminum 90 degree elbow hardware; represent quantity, alloy, and interface standard in BOM notes or recipe parameters rather than decomposing into subparts."
---

Research result for reAM250 BOM row 207.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0207_8B.md
source_research_sha256: "6fb9bd3542839aa56edde1b74b659bf3ffe5f44ca4fbad17b960a5bd0e446af5"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the DN40 ISO-KF elbow function, CAD-derived per-unit and row-total mass basis, Pfeiffer aluminum EN AW-6082 material evidence, inferred vacuum fitting manufacturing route, and preview showing a right-angle tube with KF-style flanged ends."
decomposition:
  decision: simple_part
  rationale: "The row is one-piece elbow fitting hardware; BOM quantity five represents repeated fittings rather than subparts."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_vacuum_elbow_fabrication
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - forming
    - precision_machining
    - deburring
    - cleaning
    - leak_testing
    - pressure_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers gas/vacuum fitting context and leak checks, but is oriented toward system installation."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for KF flange lips, centering diameters, sealing faces, and clamp interfaces."
    - process_id: tube_bending_process_v0
      fit: supporting
      reason: "Relevant if the elbow body starts from bent tube stock."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Relevant to near-net forming of the elbow body before finish machining."
    - process_id: leak_testing_v0
      fit: direct
      reason: "Matches vacuum leak testing for the finished elbow fitting."
    - process_id: pressure_testing_v0
      fit: supporting
      reason: "Provides an alternate pressure/vacuum integrity check when helium testing is not modeled in detail."
  abstraction_decision: substitute_process_family
  rationale: "The source item is a vendor vacuum elbow; for closure analysis it belongs with reusable plumbing connector fabrication/testing rather than a product-specific route."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: standard
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: right-angle vacuum line connection preserving ISO-KF clamp interfaces
  material: aluminum_6082
  scale_or_capacity:
    mass_kg: 0.141
    bom_quantity: 5
    row_total_mass_kg: 0.707
    scale_class: small
  geometry_form: ninety_degree_elbow_with_integral_dn40_iso_kf_flanges
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - kf_flange_geometry
    - sealing_face_finish
    - leak_tightness
    - internal_passage_continuity
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "ISO-KF interface precision and vacuum cleanliness may require tighter controls than ordinary pipe elbows."
    - "Commercial route could use a near-net blank not represented in current KB processes."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other KF/ISO plumbing connector rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other DN40 and similar vacuum elbow/connector rows; preserve quantity five as BOM usage."
assumptions:
  - "The CAD solid is treated as the complete per-unit elbow at 0.141 kg."
  - "EN AW-6082 aluminum is retained from the Pfeiffer product evidence."
unresolved:
  - "Exact commercial manufacturing route, surface treatment, cleaning specification, and leak-rate criterion are not specified."
  - "Whether lunar staging should distinguish DN40 elbow geometry from other plumbing connector sizes is deferred to merge review."
```
