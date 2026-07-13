---
row_identity:
  item: "41C"
  cad_file: "41C_clamping_ring_ISO_KF_DN40_120BSR040"
  source_row_number: 258
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040"
function:
  summary: "DN 32-40 ISO-KF stainless clamping ring used to tighten and secure an elastomer-sealed KF vacuum flange joint in the powder inlet area; BOM quantity is 2."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr040/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 258 identifies Pfeiffer Vacuum order number 120BSR040. The associated product page and datasheet identify 120BSR040 as a clamping ring for elastomer seals, DN 32-40 ISO-KF, suitable for elastomer seals. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 was blocked to direct curl, but the associated vacuum-shop product route and linked Pfeiffer datasheet match manufacturer Pfeiffer Vacuum, order number 120BSR040, product family, material, and DN 32-40 ISO-KF row identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is locked to BOM item 41C and product 120BSR040, not to the adjacent toothed-belt-pulley row mentioned in the raw row text."
  uncertainty_notes: []
mass:
  value_kg: 0.265
  basis: "FreeCAD measured one solid with volume 32971.270 mm^3, surface area 17328.748 mm^2, and bounding box about 101.47 x 16.00 x 72.81 mm. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.264759 kg per clamping ring. BOM quantity is 2, so row total is about 0.530 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41C_clamping_ring_ISO_KF_DN40_120BSR040.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/2075879/downloads/datasheets/Datasheet_120BSR040_en.pdf"
    cited_fact_or_basis: "FreeCAD measured CAD volume 32971.270 mm^3 for the row-specific STEP. The datasheet for 120BSR040 states material stainless steel 1.4301/304, and kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 was blocked to direct curl; the associated vacuum-shop datasheet route matches order number 120BSR040 and Pfeiffer Vacuum product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the material volume proxy for one complete clamp."
    - "The 304/1.4301 material stated by the BOM-provided product route is represented by the local stainless_steel_304 density."
  uncertainty_notes:
    - "No published catalog weight was found in the accessible product page or datasheet, so the mass is CAD-volume-derived rather than a vendor-weighed value."
    - "The assembly STEP material extractor returned only Generic with density 1000.0, which is treated as placeholder metadata and not used for mass."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://www.vacuum-shop.com/2075879/downloads/datasheets/Datasheet_120BSR040_en.pdf"
    cited_fact_or_basis: "The 120BSR040 datasheet states material stainless steel 1.4301/304 for the clamping ring. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR040 was blocked to direct curl; the associated vacuum-shop datasheet route matches order number 120BSR040, Pfeiffer Vacuum identity, DN 32-40 ISO-KF connection, and product description."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local assembly STEP material metadata was only Generic/1000.0 and therefore did not independently resolve material."
how_to_make:
  summary: "Treat as external Pfeiffer ISO-KF vacuum hardware for KB modeling. fabricate stainless 304 clamp halves/ring geometry, add hinge and wingnut tightening features, deburr/passivate, and inspect DN 32-40 ISO-KF fit"
  manufacturing_steps:
    - "For local fabrication, cut or stamp stainless 304/1.4301 strip or near-net blanks for the curved clamp band geometry."
    - "Form the clamp band into the KF profile and create hinge, lug, and tightening-feature geometry visible in the CAD preview."
    - "Machine or drill attachment features, fit screw/wingnut hardware, deburr and passivate or clean for vacuum service."
    - "Verify fit and tightening torque against DN 32-40 ISO-KF elastomer-seal flange hardware."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0258_41C__views_2x2.png; https://www.vacuum-shop.com/2075879/downloads/datasheets/Datasheet_120BSR040_en.pdf"
    cited_fact_or_basis: "The CAD preview shows a curved clamp with hinge/lug/tightening features; the datasheet identifies 120BSR040 as a stainless 304/1.4301 clamping ring for elastomer seal, DN 32-40 ISO-KF, with 2 N m wingnut torque. targeted_web_search: searched \"120BSR040 weight mass\", \"120BSR040 clamping ring stainless steel 304 1.4301 manufacturing drawing\", and \"Pfeiffer 120BSR040 DN 40 clamping ring material\" found product/spec and datasheet evidence but no row-specific manufacturing process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed local fabrication operations are inferred from clamp geometry and common stainless vacuum-clamp production practice because the cited sources identify the product but do not specify manufacturing process."
    - "External-module handling is preferred because this is standard commercial vacuum fastening hardware"
  uncertainty_notes:
    - "Exact production process, fastener subpart material, surface finish, and inspection plan are not specified by the row evidence."
kb_implications:
  - "item_granularity: simple_part - standard commercial ISO-KF vacuum clamping hardware; model as a reusable manufacturable clamp unless later KB work intentionally decomposes KF clamp rings, hinges, and tightening hardware."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0258_41C.md
source_research_sha256: "b526167321420e2632e1b130d6f01bbf12a4e671a3cd9ed1f00803344022bdd5"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the row research, CAD preview, CAD-derived mass basis, stainless 304 material evidence, DN 32-40 ISO-KF clamping function, and inferred local fabrication route before conversion."
decomposition:
  decision: simple_part
  rationale: "Treat as one reusable clamp item for Phase 1 closure. The hinge, screw, and wingnut features are visible and matter to function, but the row evidence frames the commercial part as standard KF clamping hardware rather than a complex module needing internal closure decomposition now."
  proposed_subparts: []
process_abstraction:
  original_process_family: commercial_vacuum_hardware_stainless_forming_machining
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - cutting
    - forming
    - drilling
    - thread_forming
    - deburring
    - surface_finishing
    - assembly
    - dimensional_inspection
    - leak_testing
  candidate_existing_processes:
    - process_id: metal_forming_basic_shop_v0
      fit: partial
      reason: "Covers bending/forming stainless clamp-band geometry from strip and near-net blanks; does not by itself define the KF profile, hinge, and tightening hardware."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Relevant for local drilling, lug cleanup, hinge feature fitting, and profile finishing after forming."
    - process_id: assembly_basic_v0
      fit: supporting
      reason: "Covers fitting hinge and wingnut tightening hardware into the formed clamp body."
    - process_id: surface_treatment_basic_v0
      fit: supporting
      reason: "Represents passivation and cleaning needed for stainless hardware used around sealed powder and gas interfaces."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "The clamp is not leak-tested alone, but final acceptance should verify an elastomer-sealed KF joint assembled with this clamp."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers DN 32-40 fit, hinge movement, tightening feature checks, and dimensional acceptance before merge/staging."
  abstraction_decision: substitute_process_family
  rationale: "The source route treats the row as commercial Pfeiffer vacuum hardware. For closure, generalize it to a reusable plumbing/joint-clamping hardware bucket with stainless forming, light machining, assembly, cleaning, and joint-fit/leak-test guardrails."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: tighten and secure an elastomer-sealed flange joint
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.265
    bom_quantity: 2
    row_total_mass_kg: 0.53
    scale_class: small
  geometry_form: split_curved_clamping_ring_with_hinge_and_wingnut
merge_pool:
  eligible: true
  functional_purpose_key: joint_clamping
  precision_guardrails:
    - flange_fit
    - tightening_torque
    - sealing_quality
    - hinge_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
    - metal_forming_basic_shop_v0
    - machining_basic_v0
  import_risk_factors:
    - "Commercial standard vacuum hardware with unknown detailed production route and fastener subpart material."
    - "Final usefulness depends on KF flange fit, elastomer compression, cleanliness, and leak performance rather than bulk strength alone."
  post_merge_decision_notes: "Defer import/local manufacture decision until merge review groups this with related joint clamps and plumbing connector hardware."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable with other small joint-clamping hardware if function, scale, material, and fit guardrails converge."
assumptions:
  - "BOM quantity is 2 and CAD-derived mass is 0.265 kg per clamp, giving about 0.530 kg row total."
  - "Stainless steel 304/EN 1.4301 remains the closure material because the source datasheet explicitly identifies it."
  - "The clamp can be represented as one closure part for now; hinge and wingnut details are captured as manufacturing and precision guardrails."
unresolved:
  - "Exact production process, fastener material, passivation method, and catalog weight remain unavailable in the accessible source evidence."
  - "Merge review must decide whether DN 32-40 sizing stays separate versus merging into a generic small flange/joint clamp item."
```
