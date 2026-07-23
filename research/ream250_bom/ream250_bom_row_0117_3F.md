---
row_identity:
  item: "3F"
  cad_file: "3F_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 117
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "Clamping ring that secures a DN 32-40 ISO-KF vacuum flange joint using an elastomer seal; the reAM250 BOM uses quantity 3 of this row item."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; research/ream250_bom/ream250_bom_row_0117_3F__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Pfeiffer URL redirects to the official Busch Group shop page for order number 120BSR040, whose title identifies a clamping ring for elastomer seal, DN 32-40 ISO-KF, and whose product information says it is suitable for elastomer seals. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirected to https://www.shop.buschgroup.com/global/en/products/120BSR040/; the alternate route is an official Busch/Pfeiffer shop page and matches order number 120BSR040. The CAD preview shows a curved clamp form with tightening/lug features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row identity, manufacturer, product ID, and CAD filename lock this result to Pfeiffer/Busch order number 120BSR040."
  uncertainty_notes: []
mass:
  value_kg: 0.0933
  basis: "FreeCAD measured one solid with volume 11613.114 mm^3, surface area 7339.078 mm^2, and bounding box about 90.35 x 36.90 x 16.00 mm. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.093253 kg per clamping ring. BOM quantity is 3, so the row total is about 0.280 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3F_clamping_ring_ISO_KF_DN40_120BSR040.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured the row-specific STEP volume as 11613.114 mm^3. The BOM-provided Pfeiffer URL redirects to the official Busch Group page matching order number 120BSR040 and identifying the material as stainless steel 304/1.4301. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirected to https://www.shop.buschgroup.com/global/en/products/120BSR040/; the alternate route is an official Busch/Pfeiffer shop page and matches order number 120BSR040. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the material-volume proxy for one physical clamping ring."
    - "The 304/1.4301 product material is represented by the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "Mass excludes any packaging and any vendor-supplied loose accessories not represented in the single CAD solid."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
    cited_fact_or_basis: "The BOM-provided Pfeiffer URL redirects to the official Busch Group page matching order number 120BSR040; the product title states stainless steel 304/1.4301. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirected to https://www.shop.buschgroup.com/global/en/products/120BSR040/; the alternate route is an official Busch/Pfeiffer shop page and matches order number 120BSR040."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Locally fabricate as a stainless clamping ring if the KB later models vacuum fitting manufacture"
  manufacturing_steps:
    - "Start from stainless steel 304/1.4301 strip, sheet, or near-net blank sized for a DN 32-40 ISO-KF clamp."
    - "Form or machine the curved clamp profile and lug geometry visible in the row CAD preview."
    - "Drill or machine the fastening features, fit the screw or wingnut hardware, and deburr the clamp edges."
    - "Clean or passivate for vacuum-service compatibility, then inspect fit against DN 32-40 ISO-KF flanges with an elastomer seal."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0117_3F__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
    cited_fact_or_basis: "The CAD preview shows a curved clamp body with side lug/tightening features. The BOM-provided product route identifies the row item as a stainless steel 304/1.4301 DN 32-40 ISO-KF clamping ring for elastomer seals. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 redirected to https://www.shop.buschgroup.com/global/en/products/120BSR040/; the alternate route is an official Busch/Pfeiffer shop page and matches order number 120BSR040. targeted_web_search: searched \"120BSR040 clamping ring stainless steel 304 1.4301 manufacturing drawing\", \"Pfeiffer 120BSR040 clamping ring DN 40 material weight\", and \"ISO-KF DN40 clamping ring stainless steel manufacturing\" found product/spec pages and generic ISO-KF clamp information but no row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local fabrication route is inferred from the row CAD geometry, stainless material, and common small metal clamp fabrication practice."
  uncertainty_notes:
    - "The exact vendor production method, fastener subparts, surface finish, and inspection tolerances are not specified by the row evidence."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard ISO-KF vacuum clamp hardware rather than a machine-specific custom assembly; use a separate subpart model only if later KB work expands vacuum fitting manufacture."
---
## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0117_3F.md
source_research_sha256: "c1a89764908565c3742d2510d36515188fc1780b78707e14b1fb693c45430df5"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed DN32-40 ISO-KF clamp function, CAD-derived mass with quantity 3, official 304/1.4301 material evidence, inferred forming/machining route, and preview showing curved clamp and tightening features."
decomposition:
  decision: simple_part
  rationale: "The row is reusable standard clamp hardware; screw/wingnut details can stay within the clamp item unless a later fitting-manufacture pass decomposes it."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_iso_kf_clamp_forming_and_fit_inspection
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - forming
    - precision_machining
    - drilling
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Captures reusable line-connection hardware but lacks ISO-KF clamp geometry detail."
    - process_id: sheet_metal_forming_v0
      fit: partial
      reason: "Covers curved clamp body forming from stainless stock."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers lug and fastening-feature finishing."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers tightening fastener holes if needed after forming."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers fit checks against DN32-40 ISO-KF flanges and elastomer seal stack."
  abstraction_decision: keep_original_family
  rationale: "The source row is already standard stainless plumbing connector hardware, fitting the plumbing connector fabrication/testing bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: clamp an elastomer-sealed flange joint closed
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.0933
    bom_quantity: 3
    row_total_mass_kg: 0.280
    scale_class: small
  geometry_form: iso_kf_dn32_40_clamping_ring_with_tightening_lugs
merge_pool:
  eligible: true
  functional_purpose_key: joint_clamping
  precision_guardrails:
    - flange_size_range
    - clamp_fit
    - tightening_feature_geometry
    - sealing_stack_compatibility
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Standard clamp geometry and stainless finish must match the flange/seal stack."
    - "Small purchased clamps may remain import kit candidates until fitting hardware volume justifies local production."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups ISO-KF clamp hardware and checks local connector-fabrication capability."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as generic ISO-KF stainless clamp hardware."
assumptions:
  - "Official 304/1.4301 material evidence is normalized to stainless steel 304."
  - "The CAD solid represents one clamp item and row quantity 3 represents identical instances."
unresolved:
  - "Exact fastener subparts, surface finish, vendor production method, and tolerances are not specified."
```
