---
row_identity:
  item: "84"
  cad_file: "84_valve"
  source_row_number: 280
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PF_A58_204"
function:
  summary: "Pfeiffer Vacuum PF A58 204 is an AVC 040 PA DN 40 ISO-KF electropneumatic high-vacuum angle valve with position indicator and pilot valve; in the reAM250 vacuum train it acts as an isolation/shutoff valve for a DN 40 KF line."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/84_valve.step; https://www.dreebit-service.eu/en/product/detail/avc-040-pa%2C-angle-valve%2C-electropneumatic%2C-with-pi%2C-with-pv%2C-pv-24-v-dc.html"
    cited_fact_or_basis: "BOM row 280 gives item 84, quantity 2, product PF A58 204, manufacturer Pfeiffer Vacuum. DREEBIT row-matched service page names PF A58 204 as 'AVC 040 PA, angle valve, electropneumatic, with PI, with PV, PV 24 V DC' and category Angle Valve. CAD preview shows a right-angle valve body with two KF-style flanged ports and an actuator/indicator body. bom_url_route_check: the BOM Pfeiffer shop route for PF_A58_204 was checked but returned HTTP 403, so the row-matched DREEBIT service page was used to resolve the product function."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Isolation/shutoff duty is inferred from the product category and its placement among adjacent vacuum pump/filter/KF fitting rows in the BOM."
  uncertainty_notes:
    - "The BOM-provided Pfeiffer shop URL returned HTTP 403 from this environment; the row match was preserved through the original URL, BOM product ID, DREEBIT product page, and CAD geometry."
mass:
  value_kg: 1.21
  basis: "Per-unit catalog mass for AVC 040 PA / PF A58 204. BOM quantity is 2, so row total planning mass is about 2.42 kg. Local CAD volume is 528917.741 mm^3 with bounding box about 99.50 x 69.00 x 201.53 mm; using catalog mass implies an effective whole-assembly density near 2288 kg/m^3, plausible for a mixed aluminum valve with steel bellows, elastomer seals, and actuator hardware."
  source:
    url_or_path: "https://www.dianchuvacuum.com/data/upload/image/20240626/1719391402200601.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/84_valve.step"
    cited_fact_or_basis: "Row-matched AVC 040 PA / PF A58 204 catalog PDF search result states weight 1.21 kg. FreeCAD measured one solid, volume 528917.741 mm^3, area 53846.811 mm^2, and bounding box 99.50 x 69.00 x 201.53 mm for 84_valve.step. bom_url_route_check: the BOM Pfeiffer shop route for PF_A58_204 was checked but returned HTTP 403, so the row-matched PDF source was used for mass."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The CAD export is visually and dimensionally consistent with the valve but has only generic STEP material metadata, so the catalog weight is preferred over density-from-volume mass."
material:
  primary_material: "Aluminum housing with stainless steel bellows/feedthrough, FKM sealing elements, and electropneumatic pilot/position-indicator hardware."
  source:
    url_or_path: "https://www.dianchuvacuum.com/data/upload/image/20240626/1719391402200601.pdf; queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py output for 84_valve"
    cited_fact_or_basis: "Row-matched AVC 040 PA / PF A58 204 catalog PDF search result states FKM, aluminum housing, and stainless-steel bellows. Local assembly STEP material extraction for 84_valve returned only Generic with density 1000.0, which is a placeholder and not treated as material evidence. bom_url_route_check: original Pfeiffer shop route for PF_A58_204 was checked first but returned HTTP 403."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Pilot valve, microswitch/position indicator, springs, and fasteners are grouped as actuator hardware because the catalog snippets identify the main housing/seal/bellows materials but not every small subcomponent."
  uncertainty_notes:
    - "Exact aluminum alloy and stainless grade are not resolved from the available row-matched evidence."
how_to_make:
  summary: "Manufacturing route would machine or cast the aluminum angle-valve body, machine KF interfaces and valve seat, Fabricate the stainless bellows/feedthrough, fit FKM seals, assemble the pneumatic actuator, pilot valve, and position indicator, then leak-test and cycle-test the complete valve"
  manufacturing_steps:
    - "For local manufacture, produce the aluminum valve body with right-angle flow path, DN 40 ISO-KF flange geometry, and valve-seat features."
    - "Install stainless bellows/feedthrough, valve plate or poppet, FKM seals, pneumatic actuator, pilot valve, and electrical position-indicator components."
    - "Perform vacuum leak testing, pressure/function checks, and cycle testing before installation."
  source:
    url_or_path: "https://www.dreebit-service.eu/en/product/detail/avc-040-pa%2C-angle-valve%2C-electropneumatic%2C-with-pi%2C-with-pv%2C-pv-24-v-dc.html; research/ream250_bom/ream250_bom_row_0280_84__views_2x2.png"
    cited_fact_or_basis: "DREEBIT identifies the row product as a Pfeiffer Vacuum AVC 040 PA electropneumatic angle valve with PI/PV, and the rendered CAD contact sheet shows an angle-valve body with KF flanges and actuator/indicator package. The detailed fabrication sequence is inferred from this valve architecture and material set."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Use conventional precision machining/casting, elastomer sealing, locally made or separately fabricated bellows, and vacuum component leak-testing practices"
  uncertainty_notes:
    - "Targeted_web_search: queries tried included 'PF A58 204 Pfeiffer Vacuum valve', 'AVC 040 PA 1.21 kg Aluminum FKM', and 'AVC 040 PA Bellows stainless steel 1.21 kg'; results resolved product identity/material/mass but did not provide a manufacturer-stated production process for this valve."
kb_implications:
  - "item_granularity: complex_module - Model as one complex electropneumatic DN40 KF vacuum angle-valve module for near-term KB use; split into aluminum body, stainless bellows, FKM seals, pilot valve, position indicator, and actuator hardware only if valve manufacturing becomes an explicit modeling target."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0280_84.md
source_research_sha256: "5e4ff59ba5d11d981fcafe7601af8bb05f8d7f0ea9bc33014be54d8524867bcd"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read product function, quantity, catalog mass basis, mixed-material evidence, inferred manufacturing route, kb implications, and CAD preview showing a DN40 angle valve with actuator package."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a complex electropneumatic valve module with aluminum body, stainless bellows/feedthrough, FKM seals, pilot valve, position indicator, actuator hardware, and test requirements. Those internal closure dependencies matter before merge review."
  proposed_subparts:
    - aluminum_angle_valve_body
    - stainless_bellows_feedthrough
    - fkm_seal_set
    - pneumatic_actuator_hardware
    - pilot_valve_and_position_indicator
process_abstraction:
  original_process_family: precision_valve_body_manufacture_and_electropneumatic_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - precision_machining
    - elastomer_forming
    - assembly
    - leak_testing
    - pressure_testing
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: valve_body_boring_v0
      fit: partial
      reason: "Relevant to machining valve bores and sealing surfaces, but the full DN40 angle valve includes actuator, bellows, seals, and control hardware."
    - process_id: hydraulic_control_valve_set_assembly_v0
      fit: poor_fit
      reason: "Provides a generic valve assembly precedent, but the row is a vacuum electropneumatic angle valve rather than a hydraulic control valve set."
    - process_id: pressure_test_basic_v0
      fit: supporting
      reason: "Covers basic integrity testing; later staging should add vacuum leak and cycle testing."
    - process_id: electrical_testing_and_calibration_v0
      fit: supporting
      reason: "Relevant to validating the position indicator and pilot valve electronics after module assembly."
  abstraction_decision: needs_human
  rationale: "The source item is a mixed-material vacuum valve with precision flow surfaces, elastomer seals, stainless bellows, pneumatic actuation, electrical indication, leak testing, and cycle testing. Row conversion should not collapse it into one simple local process bucket."
  process_guardrails:
    tolerance: review
    surface_finish: sealing_surface_review
    sealing_quality: vacuum_leak_tight_review
    alignment_accuracy: actuator_seat_alignment_review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: remotely actuated shutoff control for a DN40 gas line
  material: mixed_aluminum_stainless_fkm_electromechanical_hardware
  scale_or_capacity:
    mass_kg: 1.21
    bom_quantity: 2
    row_total_mass_kg: 2.42
    scale_class: small
  geometry_form: right_angle_dn40_kf_valve_with_actuator
merge_pool:
  eligible: false
  functional_purpose_key: flow_control_valve
  precision_guardrails:
    - vacuum_leak_tightness
    - valve_seat_surface_finish
    - actuator_cycle_life
    - electrical_position_feedback
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Electropneumatic actuation, position feedback, bellows/feedthrough fabrication, FKM seal performance, and high-vacuum leak acceptance are unresolved."
    - "Catalog mass and mixed-material construction indicate the module may remain imported until valve subparts are explicitly modeled."
  post_merge_decision_notes: "Final import/local decision is deferred until decomposition separates body, seal, bellows, actuator, pilot valve, and indicator dependencies."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a final closure item ID during row conversion; review as a decomposition candidate before merge."
assumptions:
  - "BOM quantity is 2, so row total mass is about 2.42 kg from the 1.21 kg catalog mass."
  - "The CAD preview confirms the product is a complete actuated valve module rather than a bare valve body."
  - "DN40 KF interfaces and shutoff function should be preserved as guardrails during decomposition."
unresolved:
  - "Exact aluminum alloy, stainless grade, FKM compound, and actuator subcomponent materials."
  - "Vacuum leak rate, cycle life, seat geometry, and cleaning specification."
  - "Whether the pilot valve and position indicator are separate imported electronics items in later staging."
```
