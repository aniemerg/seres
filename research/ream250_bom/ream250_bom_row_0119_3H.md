---
row_identity:
  item: "3H"
  cad_file: "3H_pipe_ISO_K_DN63"
  source_row_number: 119
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight DN 63 ISO-K full nipple / short flanged vacuum pipe used as a rigid connection section between ISO-K vacuum components."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3H_pipe_ISO_K_DN63.step; research/ream250_bom/ream250_bom_row_0119_3H__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "BOM row 119 identifies item 3H as Pfeiffer Vacuum product 320RZS063, named 3H_pipe_ISO_K_DN63; the manifest maps the row to the matching STEP file. FreeCAD measured one solid with a 70.00 x 105.13 x 105.13 mm bounding box, and the rendered preview shows a straight cylindrical tube with ISO-style flange lips at both ends. The Pfeiffer Vacuum Online Shop category identifies product 320RZS063 as an ISO-K Full Nipple with DN 63 ISO-K connection, A=88 mm and B=70 mm. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route for 320RZS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product number 320RZS063, Global-No. 2000042732, and the DN 63 ISO-K full-nipple family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row CAD name 'pipe' and the vendor family term 'full nipple' are treated as the same straight flanged ISO-K vacuum pipe component."
  uncertainty_notes:
    - "The direct Pfeiffer URL was not parseable as a detailed product page in the local browser, so the official Pfeiffer Vacuum Online Shop alternate route is used for the row-matched catalog facts."
mass:
  value_kg: 0.814
  basis: "Per-unit mass for one physical full nipple. FreeCAD measured CAD volume 101,403.415 mm^3, equal to 1.01403415e-4 m^3; using local stainless_steel_304 density 8030 kg/m^3 gives 0.81427 kg, rounded to 0.814 kg. BOM quantity is 1, so the row total is also about 0.814 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3H_pipe_ISO_K_DN63.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 101,403.415 mm^3 for 3H_pipe_ISO_K_DN63.step; the row-matched Pfeiffer Vacuum Online Shop entry identifies 320RZS063 under Stainless steel 1.4301/304; kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route for 320RZS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product number 320RZS063 and Global-No. 2000042732."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume of one row item."
    - "Pfeiffer's 1.4301/304 material designation maps to the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "If the STEP export omits small weld radii, internal features, or vendor manufacturing details, the actual catalog mass may differ from the CAD-density estimate."
material:
  primary_material: "Stainless steel 1.4301 / AISI 304."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched Pfeiffer Vacuum Online Shop ISO-K Full Nipple entry places product 320RZS063 under Stainless steel 1.4301/304. Local assembly STEP material extraction for 3H_pipe_ISO_K_DN63 returned only Generic material with density 1000.0, which does not resolve material. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route for 320RZS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product number 320RZS063 and the same DN 63 ISO-K full-nipple row."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local STEP package lacks a real material assignment for this part; the material value depends on the row-matched official shop/catalog route."
how_to_make:
  summary: "Manufacturing route would form or machine stainless 304 tube/flange geometry, clean/passivate it, and leak-test it for vacuum service"
  manufacturing_steps:
    - "Inspect the DN 63 ISO-K interfaces, 70 mm tube/body span, sealing lips, bore clearance, cleanliness, and surface condition before installation."
    - "For local manufacture, start from stainless 304 tube/flange stock, machine or form the two ISO-K flange profiles, join as needed by welding or one-piece machining, passivate/clean the part, and helium leak-test the finished vacuum component."
    - "Install between compatible ISO-K components using the appropriate centering ring/seal and clamp hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0119_3H__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "BOM row 119 gives Pfeiffer Vacuum product 320RZS063; the CAD preview shows a one-piece straight flanged pipe, and the Pfeiffer Vacuum Online Shop identifies the row-matched DN 63 ISO-K stainless full-nipple product family and dimensions. The machining/forming/welding route is inferred from the CAD geometry and stainless vacuum fitting construction."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing steps are plausible operations for a stainless ISO-K full nipple but are not directly specified by the cited product page."
  uncertainty_notes:
    - "Targeted_web_search: searched '320RZS063 Pfeiffer Vacuum DN 63 pipe material weight', 'Pfeiffer 320RZS063 ISO-K DN 63 pipe stainless 1.4301', and '320RZS063 Pfeiffer Vacuum full nipple'; results resolved row-matched product identity, material, and dimensions but did not provide a row-specific manufacturing process or catalog weight."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable standard stainless DN63 ISO-K straight pipe/full nipple rather than a reAM250-specific custom part or calibrated module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0119_3H.md
source_research_sha256: "4536b865c67370015c9dd88134aae12d2d9181c88a69da606c68f6245e2bf26b"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the row-matched Pfeiffer product evidence, DN 63 ISO-K function, stainless 304 material evidence, CAD volume mass estimate, straight flanged tube geometry, and local manufacturing assumptions."
decomposition:
  decision: simple_part
  rationale: "The row is one reusable straight flanged pipe/full-nipple component. It should stay separate from clamps, centering rings, seals, and adjacent plumbing assemblies rather than decomposing into hidden vendor details."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_iso_k_plumbing_connector_fabrication_and_leak_test
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - joining
    - surface_finishing
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers fitting and connecting tubes plus leak checks at system level; it is broader than a single DN 63 full-nipple fabrication step."
    - process_id: tube_bending_and_cutting_v0
      fit: partial
      reason: "Covers metal tube stock cutting and setup, but this row is straight and mainly needs ISO-K flange profiling."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Relevant for machining the flange lips, bore clearance, and mating faces from stainless stock."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Relevant for post-machining cleanliness before this connector enters controlled gas-handling service."
    - process_id: leak_testing_v0
      fit: direct
      reason: "Directly covers leak-tight verification for sealed joints and components using pressure/vacuum methods."
  abstraction_decision: keep_original_family
  rationale: "The source route already describes stainless tube/flange fabrication followed by cleaning/passivation and leak testing, which maps directly to the plumbing connector fabrication/testing closure bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: critical
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: rigid straight flanged connection section between ISO-K components
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.814
    bom_quantity: 1
    row_total_mass_kg: 0.814
    scale_class: small
  geometry_form: straight_cylindrical_tube_with_iso_k_flange_lips
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - iso_k_interface_dimensions
    - sealing_surface_finish
    - leak_tightness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
    - general_subtractive_machining
  import_risk_factors:
    - "ISO-K sealing surfaces require controlled dimensions, surface condition, cleanliness, and leak-test acceptance."
    - "Commercial standardization may matter for interchangeability with clamps, centering rings, and adjacent DN 63 components."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until ISO-K connector rows are merge-reviewed and sealing/interface requirements are staged."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other DN 63 ISO-K straight, elbow, clamp, seal, and adapter rows before assigning a closure item ID."
assumptions:
  - "Quantity 1 and row total mass 0.814 kg use the stainless 304 CAD-volume estimate from the original research."
  - "The vendor material 1.4301/304 is normalized to stainless_steel_304 for later KB staging."
  - "Leak testing and cleanliness are process guardrails, while clamps and centering seals remain separate closure items."
unresolved:
  - "Actual catalog mass was not found; the conversion relies on CAD volume times stainless 304 density."
  - "Detailed ISO-K tolerances, surface roughness, and helium leak-rate acceptance are not specified in the row evidence."
  - "Merge review should decide whether DN 63 straight full nipples of nearby lengths can share one closure item."
```
