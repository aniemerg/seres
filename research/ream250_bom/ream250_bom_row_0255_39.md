---
row_identity:
  item: "39"
  cad_file: "39_pipe_ISO_K_DN63"
  source_row_number: 255
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight DN 63 ISO-K vacuum piping nipple used to bridge two ISO-K vacuum components while preserving a sealable high-vacuum flow path."
  source:
    url_or_path: "https://www.shop.buschgroup.com/products/320RZS063; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/39_pipe_ISO_K_DN63.step; research/ream250_bom/ream250_bom_row_0255_39__views_2x2.png"
    cited_fact_or_basis: "official_alternate_route_check: the BOM Link URL is the Pfeiffer product path for 320RZS063; direct fetch of that domain was blocked, but the official Busch Group shop route for the same product code resolves to 'Full nipple, stainless steel 304/1.4301, DN 63 ISO-K', category Piping components, connecting flange DN 63 ISO-K, and product-table name ISO-K Full Nipple. The row STEP and preview show a straight cylindrical pipe with ISO-K-style flanges at both ends."
    evidence_basis: "bom_provided"
  assumptions:
    - "Treat the BOM product code and supplied CAD as the same row identity even though the CAD length is longer than the official catalog dimension exposed by the shop route."
  uncertainty_notes:
    - "The official shop route lists length 88 mm, while the row CAD bounding box is about 214 mm long; function as a straight DN 63 ISO-K vacuum connector is still consistent, but exact variant length should be checked before detailed layout reuse."
mass:
  value_kg: 1.62
  basis: "Per unit for quantity 1. FreeCAD measured one solid with volume 202064.851 mm^3. Converted to 0.000202064851 m^3 and multiplied by the local stainless_steel_304 density constant 8030 kg/m^3 from kb/materials/properties.yaml, giving 1.623 kg, rounded to 1.62 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/39_pipe_ISO_K_DN63.step; kb/materials/properties.yaml; https://www.shop.buschgroup.com/products/320RZS063"
    cited_fact_or_basis: "FreeCAD measured the row STEP as 1 solid, volume 202064.851 mm^3, area 118096.093 mm^2, and bounding box about 214.00 x 105.13 x 105.13 mm. official_alternate_route_check: the BOM Link URL points to Pfeiffer product 320RZS063; direct fetch of that domain was blocked, but the official Busch Group shop route for the same product code resolves the row-matched product and identifies stainless steel 304/1.4301. kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume represents one physical BOM-row item."
    - "Use the local stainless_steel_304 density as an adequate density constant for stainless steel 304/1.4301."
  uncertainty_notes:
    - "If the longer CAD geometry is a machine-specific stretched variant of the catalog full nipple, this CAD-derived mass is preferable for the reAM250 row but may not match the catalog part mass."
material:
  primary_material: "stainless steel 304/1.4301"
  source:
    url_or_path: "https://www.shop.buschgroup.com/products/320RZS063; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "official_alternate_route_check: the BOM Link URL points to Pfeiffer 320RZS063, and the official Busch Group shop route for the same product code names the product 'Full nipple, stainless steel 304/1.4301, DN 63 ISO-K' and lists media-contact material as Stainless steel 1.4301 (AISI 304). Local assembly STEP material extraction for 39_pipe_ISO_K_DN63 returned only material 'Generic' with density 1000.0, so it was not used as material evidence."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material was available; material comes from the official product-code route rather than embedded CAD metadata."
how_to_make:
  summary: "Prepare as Pfeiffer/Busch product 320RZS063 or model locally as a stainless 304/1.4301 ISO-K full nipple made from tube and two ISO-K flange ends, followed by vacuum cleaning and leak/fit inspection"
  manufacturing_steps:
    - "Cut stainless 304/1.4301 tube to the required row length and prepare two ISO-K flange ends."
    - "Join the tube/flange geometry by welding or equivalent vacuum-compatible fabrication, then machine or finish the sealing and clamp-interface surfaces."
    - "Clean for vacuum service and verify dimensions, flange fit, and leak-tightness before installation."
  source:
    url_or_path: "https://www.shop.buschgroup.com/products/320RZS063; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/39_pipe_ISO_K_DN63.step"
    cited_fact_or_basis: "The official alternate route for BOM product 320RZS063 identifies a purchasable DN 63 ISO-K stainless full nipple. The supplied CAD shows a straight tube-like body with flanged ends. The local fabrication sequence is inferred from that geometry and material. targeted_web_search: searched 'Pfeiffer 320RZS063 manufacturing welded tube full nipple' and found product/spec pages but no row-specific manufacturing process disclosure."
    evidence_basis: "engineering_hypothesis"
  assumptions: []
  uncertainty_notes:
    - "Exact flange forming, weld prep, surface finish, and leak-test acceptance criteria are not specified by the row evidence."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable ISO-K stainless vacuum pipe/full-nipple part with size and length variants rather than a calibrated purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0255_39.md
source_research_sha256: "346adf39b69ee4ddb75e55da5bf9a0240ea20cfef5a70545e6026f8dedde78ca"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the connector function, CAD-derived mass, stainless 304/1.4301 material evidence, tube/flange fabrication route, KB implications, and CAD preview showing a straight flanged DN63 tube."
decomposition:
  decision: simple_part
  rationale: "The row is a single straight flanged pipe nipple with no moving parts and no internal subassembly beyond tube and flange geometry."
  proposed_subparts: []
process_abstraction:
  original_process_family: vendor_flanged_tube_nipple
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - cutting
    - joining
    - precision_machining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers plumbing installation and fitting work, but does not fully model fabrication of a stainless ISO-K nipple."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Relevant if tube and flange features are welded for leak-tight service."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for flange faces, clamp interfaces, and sealing geometry."
    - process_id: vacuum_testing_v0
      fit: supporting
      reason: "Covers leak testing and cleanliness verification for a sealed plumbing connector."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, flange geometry, bore, and fit checks."
  abstraction_decision: substitute_process_family
  rationale: "The original route is vendor procurement for a standard flanged stainless nipple. For closure analysis, it should be generalized into plumbing connector fabrication and testing with flange, length, and leak guardrails."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "straight sealed gas-flow connection between flanged components"
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 1.62
    bom_quantity: 1
    row_total_mass_kg: 1.62
    scale_class: medium
  geometry_form: straight_dn63_iso_k_flanged_tube_nipple
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - flange_size
    - connector_length
    - sealing_surface
    - leak_rate
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Flange forming, weld quality, surface finish, and leak acceptance criteria are unresolved."
    - "Catalog length and CAD length differ, so staging must preserve row geometry until layout intent is reviewed."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares ISO-K plumbing connector rows by function, size, material, and length guardrails."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely belongs in a reusable stainless plumbing connection family with DN size and length variants."
assumptions:
  - "Stainless 304/1.4301 product evidence applies to the row despite placeholder CAD material metadata."
  - "CAD-derived mass is preferred for row accounting because it matches the supplied geometry length."
unresolved:
  - "Exact catalog-vs-CAD length relationship, flange forming method, weld prep, surface finish, and leak-test acceptance criteria are not specified."
```
