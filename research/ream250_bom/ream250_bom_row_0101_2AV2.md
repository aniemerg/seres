---
row_identity:
  item: "2AV2"
  cad_file: "2AV2_DIN 912 - M8x1,25x35x31,875"
  source_row_number: 101
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "M8 DIN 912 cylinder/socket head cap screw used as one of ten machine fasteners in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV2_DIN 912 - M8x1,25x35x31,875.step; research/ream250_bom/ream250_bom_row_0101_2AV2__views_2x2.png"
    cited_fact_or_basis: "BOM row 101 identifies item 2AV2, quantity 10, CAD file 2AV2_DIN 912 - M8x1,25x35x31,875, and description 'cylinder head cap screw'. The manifest maps the row to a matched part STEP. FreeCAD measured one solid with bounding box 43.00 x 14.07 x 14.07 mm; the rendered contact sheet shows a cylindrical socket-head screw with an internal hex drive and threaded shaft."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP represents one physical screw for this BOM row."
  uncertainty_notes:
    - "The local row evidence identifies the screw standard/size family but not the exact mating joint or clamped reAM250 subassembly."
mass:
  value_kg: 0.0209
  basis: "Per-unit mass for one screw. FreeCAD volume is 2660.509 mm^3 = 2.660509e-6 m^3. Assembly STEP metadata gives density 7850 kg/m^3 for Steel, Mild, so 2.660509e-6 m^3 * 7850 kg/m^3 = 0.0209 kg per screw. BOM quantity is 10, so the row total is about 0.209 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV2_DIN 912 - M8x1,25x35x31,875.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 2660.509 mm^3, area 1532.851 mm^2, and bounding box 43.00 x 14.07 x 14.07 mm. Assembly STEP material extraction for product 2AV2_DIN 912 - M8x1,25x35x31,875 returned material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is treated as the physical solid volume of one screw, including the modeled socket recess and threads."
  uncertainty_notes:
    - "The estimate depends on the CAD thread/socket representation matching the real screw; catalog mass was not provided in the BOM row."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Assembly STEP material extraction for product 2AV2_DIN 912 - M8x1,25x35x31,875 returned material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "DIN 912 socket head cap screws are commonly sold in several steel grades and finishes, but this row's local STEP metadata resolves only the broad mild-steel material family, not a property class or coating."
how_to_make:
  summary: "Prepare as a standard DIN 912 M8x35 socket head cap screw; a Manufacturing route would form or machine a steel screw blank, create the cylindrical head and hex socket, roll or cut the M8 thread, apply heat treatment/coating if required, and inspect thread/head dimensions"
  manufacturing_steps:
    - "Start from steel wire, rod, or screw blank stock sized for an M8 socket head cap screw."
    - "Cold-head or machine the cylindrical cap head and shank."
    - "Broach or form the internal hex socket in the head."
    - "Roll or cut the M8 x 1.25 thread along the shaft length shown in the CAD."
    - "Apply any required heat treatment, coating, cleaning, and dimensional inspection for the DIN 912 interface."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0101_2AV2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV2_DIN 912 - M8x1,25x35x31,875.step; https://accu-components.com/us/metric-cap-head-screws/386839-SSC-M8-35-12-9-Z; https://www.item24.com/en-de/hexagon-socket-head-cap-screw-din-912-m8x35-bright-zinc-plated-65515"
    cited_fact_or_basis: "The CAD preview shows a socket-head threaded screw geometry. The Accu M8 x 35 mm DIN 912 page identifies this size family as full-thread socket head cap screws and lists M8, 35 mm length, DIN 912 / ISO 4762, steel material, and zinc-plated finish for one common variant. The item24 page lists a DIN 912 M8x35 bright-zinc-plated hexagon socket head cap screw with cylindrical head. targeted_web_search: tried 'DIN 912 M8 x 35 socket head cap screw dimensions material steel' and 'DIN 912 M8 x 35 socket head cap screw bright zinc plated steel M8x35'; found matching standard-part/vendor identity and material examples, but no row-specific reAM250 manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the row's standard screw geometry and common fastener production methods, not from a reAM250 production drawing."
  uncertainty_notes:
    - "The row does not state property class, coating, or actual supplier process; those details matter for strength/corrosion modeling but not for coarse BOM mass closure."
kb_implications:
  - "item_granularity: simple_part - standard M8 DIN 912 socket head cap screw; later KB modeling should reuse a generic steel metric socket-head screw item rather than create a machine-specific part."
---

Research result for reAM250 BOM row 101.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0101_2AV2.md
source_research_sha256: "3e24751043d90894a35208f8eb68fa1272a7edab52a819de47c176bf1c2b5f5d"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the fastener function, CAD/material mass basis, mild steel evidence, standard screw manufacturing route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is a batch of standard DIN 912 M8 socket-head cap screws. It should merge into reusable metric fastener hardware rather than become a machine-specific item."
  proposed_subparts: []
process_abstraction:
  original_process_family: cold_heading_socket_forming_thread_rolling
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - thread_forming
    - heat_treatment
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_medium_production_v0
      fit: direct
      reason: "Covers medium fastener-family operations for M6-M12 hardware, including forging, threading, heat treatment, sorting, and kitting."
    - process_id: fastener_kit_small_fabrication_v0
      fit: partial
      reason: "Covers small fastener fabrication but is less size-aligned than the medium kit anchor."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Relevant to forming the cylindrical socket head from steel stock."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers screw length, head geometry, socket fit, and thread checks."
  abstraction_decision: keep_original_family
  rationale: "The row is a standard formed and threaded fastener, directly matching the fastener forming/thread rolling closure bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: provide threaded mechanical fastening with a socket head
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.0209
    bom_quantity: 10
    row_total_mass_kg: 0.209
    scale_class: tiny
  geometry_form: m8x35_socket_head_cap_screw
merge_pool:
  eligible: true
  functional_purpose_key: mechanical_fastening
  precision_guardrails:
    - thread_size
    - screw_length
    - socket_head_geometry
    - property_class
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Property class, coating, heat treatment, and supplier-specific quality level are unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups standard fasteners and decides fastener kit granularity."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely belongs in a reusable medium steel fastener family rather than a row-specific item."
assumptions:
  - "The CAD and material metadata represent one mild steel screw, with BOM quantity ten."
  - "DIN 912 M8 x 35 identity is sufficient for merge grouping by standard fastener dimensions."
unresolved:
  - "Fastener property class, coating, exact heat treatment, supplier, and clamped joint are not resolved by row evidence."
```
