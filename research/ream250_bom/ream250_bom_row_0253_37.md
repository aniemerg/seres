---
row_identity:
  item: "37"
  cad_file: "37_reduction_ISO_K_DN63_KF_DN50_320RRG063-050-40"
  source_row_number: 253
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRG063_050_40"
function:
  summary: "Straight vacuum adapter/reducer joining a DN 63 ISO-K flange interface to a DN 50 ISO-KF reduced nominal diameter in the reAM250 vacuum plumbing."
  source:
    url_or_path: "https://vacuum-shop.com/2075428/downloads/datasheets/Datasheet_320RRG063-050-40_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/37_reduction_ISO_K_DN63_KF_DN50_320RRG063-050-40.step; research/ream250_bom/ream250_bom_row_0253_37__views_2x2.png"
    cited_fact_or_basis: "BOM row 253 gives product 320RRG063-050-40 from Pfeiffer Vacuum. Pfeiffer datasheet names it a straight adapter, DN 63 ISO-K/50 KF, with reduced nominal diameter DN 50 ISO-KF and connection flange DN 63 ISO-K / DN 50 ISO-KF. FreeCAD measured one solid; the contact sheet shows a short concentric flanged adapter/reduction body. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRG063_050_40; the vacuum-shop.com datasheet/shop route identifies Pfeiffer Vacuum Components & Solutions GmbH, the same order number 320RRG063-050-40, and the same DN 63 ISO-K/50 KF product family."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.605
  basis: "Per-unit estimate from row-specific CAD volume: 75,286.560 mm^3 = 0.00007528656 m^3. Using local kb/materials/properties.yaml density for stainless_steel_304 / EN 1.4301 of 8030 kg/m^3 gives 0.60455 kg per adapter, rounded to 0.605 kg. BOM quantity is 2, so the row total is about 1.21 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/37_reduction_ISO_K_DN63_KF_DN50_320RRG063-050-40.step; kb/materials/properties.yaml; https://vacuum-shop.com/2075428/downloads/datasheets/Datasheet_320RRG063-050-40_en.pdf"
    cited_fact_or_basis: "FreeCAD shape read returned 1 solid, volume 75,286.55972065835 mm^3, area 32,336.56600837374 mm^2, and bounding box 105.13 x 105.13 x 40.00 mm. Pfeiffer datasheet resolves material as stainless steel 304/1.4301. Local material properties table gives stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRG063_050_40; the vacuum-shop.com datasheet/shop route is an official Pfeiffer Vacuum route for the same order number and product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied STEP solid volume is used as the physical metal volume for one adapter."
    - "The adapter body is treated as all stainless steel 304/1.4301 for mass because the vendor material statement names the wetted material and the CAD part is a single metal adapter body."
  uncertainty_notes:
    - "The local assembly STEP material extractor returned only Generic at 1000 kg/m^3, so material identity comes from the Pfeiffer product route rather than embedded CAD metadata."
material:
  primary_material: "Stainless steel 304 / EN 1.4301 adapter body"
  source:
    url_or_path: "https://vacuum-shop.com/2075428/downloads/datasheets/Datasheet_320RRG063-050-40_en.pdf"
    cited_fact_or_basis: "Pfeiffer datasheet for 320RRG063-050-40 states straight adapter, stainless steel 304/1.4301, DN 63 ISO-K/50 KF, and lists materials in contact with media as stainless steel 1.4301 (AISI 304). official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRG063_050_40; the vacuum-shop.com datasheet/shop route is an official Pfeiffer Vacuum route for the same order number and product family."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Vendor evidence resolves the adapter body material; separate clamps or seals needed to install this adapter are separate BOM rows, not part of this row's material value."
how_to_make:
  summary: "Local manufacturing fallback would machine a short 304 stainless adapter body with ISO-K and ISO-KF flange features, then clean and leak-test it for vacuum service"
  manufacturing_steps:
    - "Start from 304/1.4301 stainless round billet, tube stock, or near-net forging sized for the flanges."
    - "Turn the concentric bore, end faces, outside diameters, and flange shoulders; finish sealing/contact surfaces suitable for vacuum hardware."
    - "Deburr, clean for vacuum service, and helium leak-test or pressure/leak check before installation with separate seals and clamps."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072966/iso-k-kf-straight-adapter.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/37_reduction_ISO_K_DN63_KF_DN50_320RRG063-050-40.step"
    cited_fact_or_basis: "Pfeiffer shop lists 320RRG063-050-40 as an ISO-K/KF straight adapter, stainless steel 1.4301/304, DN 63 ISO-K / DN 50 ISO-KF, A = 40 mm and B = 50.6 mm. CAD preview shows an axisymmetric short flanged reducer body. targeted_web_search: queries tried included 'Pfeiffer Vacuum 320RRG063-050-40 material reduction ISO-K DN 63 KF DN 50 mass', 'site:pfeiffer-vacuum.com 320RRG063_050_40 320RRG063-050-40', and '\"320RRG063-050-40\"'; results found official/product-route facts for identity and material but no row-specific source stating a manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The fallback Manufacturing route is inferred from the axisymmetric stainless adapter geometry and common vacuum fitting fabrication practice, not from a Pfeiffer manufacturing disclosure."
    - "Vacuum cleaning and leak checking are included because the part is used in vacuum plumbing."
  uncertainty_notes:
    - "Exact surface finish, flange tolerances, and any proprietary production details are not specified by the BOM-side evidence."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless vacuum adapter/reducer part; clamps and seals remain separate consumable/simple hardware rows."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0253_37.md
source_research_sha256: "b921723eb9af7334ac5a8976b97606d62710cd6a14640d4f71ad3c40611f2d39"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read vendor identity, CAD-derived mass, stainless 304 material evidence, fallback manufacturing route, KB implication, and preview of the concentric reducer body."
decomposition:
  decision: simple_part
  rationale: "The row is one stainless adapter body; clamps, seals, and installation hardware are separate rows, so no internal decomposition is needed at row-conversion stage."
  proposed_subparts: []
process_abstraction:
  original_process_family: turned_stainless_vacuum_adapter
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - precision_machining
    - deburring
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers turning and stock removal for the concentric stainless body, but vacuum flange faces need connector-specific checks."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to bore concentricity, flange shoulders, and sealing/contact surface finish."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Covers pressure/vacuum leak checks for sealed plumbing connections after fabrication."
    - process_id: vacuum_testing_v0
      fit: supporting
      reason: "Relevant if staging requires vacuum-level acceptance testing beyond a basic leak check."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional inspection of nominal diameters and flange interfaces."
  abstraction_decision: substitute_process_family
  rationale: "The source fallback is machining, but the closure role is a vacuum plumbing reducer; the primary bucket should preserve sealing, cleanliness, and leak-test requirements that plain machining does not capture."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: vacuum plumbing adapter reducing DN 63 ISO-K interface to DN 50 ISO-KF interface
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.605
    bom_quantity: 2
    row_total_mass_kg: 1.21
    scale_class: small
  geometry_form: short_axisymmetric_flanged_reducer_adapter
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - sealing_surface_finish
    - flange_standard_compatibility
    - bore_concentricity
    - vacuum_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Commercial flange standard fit and sealing surfaces may require tighter machining and inspection than coarse connector fabrication."
    - "Vacuum-compatible cleaning and leak testing are required before local substitution."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review; retain DN interface and stainless 304 evidence as merge guardrails."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other vacuum and gas plumbing adapters before assigning a closure item ID."
assumptions:
  - "Treat vendor stainless 304/1.4301 evidence as authoritative for the adapter body."
  - "Treat seals and clamps as separate hardware rows, consistent with the research implication."
  - "Use local machining as the fallback fabrication route, then apply connector-specific cleaning and leak testing."
unresolved:
  - "Exact flange tolerances and surface finish acceptance values."
  - "Whether later lunarized design can merge ISO-K and ISO-KF adapter variants into a broader connector family without losing sealing fidelity."
```
