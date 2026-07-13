---
row_identity:
  item: "3Q2"
  cad_file: "3Q2_angle_pipe_ISO_K_DN100_320RRB100-90"
  source_row_number: 139
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90"
function:
  summary: "DN 100 ISO-K 90 degree vacuum elbow/angle pipe used to turn a large vacuum line while preserving a flanged ISO-K connection at both ends."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q2_angle_pipe_ISO_K_DN100_320RRB100-90.step; research/ream250_bom/ream250_bom_row_0139_3Q2__views_2x2.png"
    cited_fact_or_basis: "BOM row 139 identifies item 3Q2 as Pfeiffer Vacuum product 320RRB100-90. The BOM-provided Pfeiffer page titles it as a 90 degree pipe elbow, stainless 1.4301/304, DN 100 ISO-K. FreeCAD measured one solid, and the contact sheet shows a curved elbow with circular ISO-style end flanges."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical elbow for this BOM row."
  uncertainty_notes: []
mass:
  value_kg: 1.67
  basis: "Per-unit planning estimate for BOM quantity 1. FreeCAD volume is 207940.963 mm^3, equal to 2.07940963e-4 m^3. Using the local stainless_steel_304 density constant of 8030 kg/m^3 gives 1.6698 kg, rounded to 1.67 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q2_angle_pipe_ISO_K_DN100_320RRB100-90.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 207940.963 mm^3 and bounding box 179.51 x 179.51 x 143.02 mm. The BOM-provided Pfeiffer page identifies product 320RRB100-90 as stainless 1.4301/304. kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is used as the physical metal volume for one elbow."
    - "Stainless 1.4301/304 is mapped to the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "If the STEP volume omits small weld beads, flange details, or internal seam geometry, the actual catalog weight may differ modestly from this CAD-derived estimate."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided Pfeiffer page for article number 320RRB100-90 states the DN 100 ISO-K 90 degree elbow is Edelstahl 1.4301/304. Local assembly STEP extraction for this product returned only material 'Generic' with density 1000.0, so the vendor/BOM route supplies the material value."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Locally fabricate as a cleaned stainless 304 ISO-K 90 degree vacuum elbow with two ISO-K flange ends"
  manufacturing_steps:
    - "Cut or form a stainless 304 90 degree elbow body sized for DN 100 vacuum service."
    - "Machine or form the ISO-K flange features at both ends, matching the DN 100 interface."
    - "Weld or otherwise join the elbow body and flange ends, then finish and clean internal surfaces for vacuum compatibility."
    - "Inspect flange geometry, leak-tightness, and cleanliness before installation in the vacuum line."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB100_90; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q2_angle_pipe_ISO_K_DN100_320RRB100-90.step; research/ream250_bom/ream250_bom_row_0139_3Q2__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Pfeiffer page identifies the row as a stainless 1.4301/304 DN 100 ISO-K 90 degree elbow, and the CAD preview shows a flanged curved pipe fitting. targeted_web_search: tried 'Pfeiffer 320RRB100-90 weight dimensions 90 angle pipe DN 100 ISO-K', '320RRB100-90 Pfeiffer Vacuum mass weight', and '\"320RRB100-90\" \"kg\"'; results confirmed product identity/material/dimensions but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local fabrication route is inferred from the observed vacuum elbow geometry and stainless ISO-K component type, not from a Pfeiffer manufacturing disclosure."
  uncertainty_notes:
    - "Detailed fabrication choices such as mandrel bending versus segmented welding, flange-forming method, weld procedure, and acceptance leak rate remain unspecified by the BOM evidence."
kb_implications:
  - "item_granularity: simple_part - Treat as a standard stainless vacuum pipe fitting/elbow for KB planning, reusable across ISO-K DN 100 vacuum plumbing rather than as a calibrated vendor module."
---

Result generated for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0139_3Q2.md
source_research_sha256: "46c48d78a0ade30c249ff6462a8f0185efeacb014fa60550aeff224147691477"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read DN100 vacuum elbow function, CAD-volume stainless mass basis, Pfeiffer stainless 304 evidence, local fabrication route, KB implication, and preview of the flanged curved pipe fitting."
decomposition:
  decision: simple_part
  rationale: "The row is one vacuum pipe fitting with two flange interfaces and no hidden module structure; clamps and seals are separate hardware rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_vacuum_elbow_forming_welding_machining_testing
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - joining
    - precision_machining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: tube_stock_forming_v0
      fit: partial
      reason: "Covers forming metal tubing stock; DN100 elbow geometry needs connector-specific flange work and leak checks."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Relevant for leak-tight stainless joining between elbow body and flange ends."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers flange face and interface feature finishing after forming and joining."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Covers pressure/vacuum leak checks for the completed pipe fitting."
    - process_id: vacuum_testing_v0
      fit: supporting
      reason: "Relevant if acceptance depends on vacuum-level hold and outgassing checks."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks of flange interfaces and elbow geometry."
  abstraction_decision: keep_original_family
  rationale: "The source and fallback route already describe a stainless vacuum plumbing elbow; the canonical closure handle should preserve forming, flange finishing, cleaning, and leak testing."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: flanged elbow redirecting a vacuum plumbing line
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 1.67
    bom_quantity: 1
    row_total_mass_kg: 1.67
    scale_class: medium
  geometry_form: dn100_iso_k_ninety_degree_flanged_pipe_elbow
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - flange_standard_compatibility
    - sealing_surface_finish
    - weld_leak_tightness
    - vacuum_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "DN100 ISO-K flange compatibility and leak-tight stainless joining may require specialized fixtures and inspection."
    - "Cleanliness and vacuum acceptance criteria are not quantified by the row evidence."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review with other stainless vacuum plumbing fittings."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review across vacuum plumbing elbows and adapters before assigning a closure item ID."
assumptions:
  - "Use stainless 304/1.4301 as resolved material from Pfeiffer evidence."
  - "Treat clamps, seals, and fasteners as separate rows."
  - "Use the CAD-derived 1.67 kg mass as the planning estimate for one elbow."
unresolved:
  - "Exact weld procedure and acceptance leak rate."
  - "Surface finish and cleanliness standard for the vacuum line."
  - "Whether lunarized staging can merge DN100 elbows with other flanged plumbing fittings at the closure-item level."
```
