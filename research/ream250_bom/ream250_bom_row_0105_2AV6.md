---
row_identity:
  item: "2AV6"
  cad_file: "2AV6_DIN 912 - M4x0,7x30x20"
  source_row_number: 105
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 M4 socket-head cap screw used as a small steel fastening screw in the reAM250 assembly; BOM quantity is 10."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0105_2AV6__views_2x2.png"
    cited_fact_or_basis: "BOM row 105 identifies item 2AV6 as quantity 10, CAD file 2AV6_DIN 912 - M4x0,7x30x20, description cylinder head cap screw. The manifest maps the same row to a matched_existing part export. The CAD preview shows a socket-head screw with cylindrical head, shaft/thread form, and hex socket."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD part represents one physical screw from the row, and the row quantity represents ten identical screws."
  uncertainty_notes: []
mass:
  value_kg: 0.00401
  basis: "FreeCAD measured CAD volume 510.584 mm^3 for one solid. Assembly STEP metadata gives density 7850 kg/m^3 for Steel, Mild, so 510.584e-9 m^3 * 7850 kg/m^3 = 0.004008 kg per screw, rounded to 0.00401 kg. BOM quantity is 10, giving an approximate row total of 0.0401 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV6_DIN 912 - M4x0,7x30x20.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 510.584 mm^3, area 556.521 mm^2, and bounding box 34.00 x 7.58 x 7.58 mm. The local assembly STEP material extractor matched product 2AV6_DIN 912 - M4x0,7x30x20 to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume is treated as the physical volume of one screw."
    - "The STEP density value is treated as kg/m^3-like, consistent with the extractor note for the reAM250 export."
  uncertainty_notes:
    - "The estimate depends on CAD export fidelity for small threaded and socket details rather than a catalog weight."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 2AV6_DIN 912 - M4x0,7x30x20 to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM and CAD name do not specify property class, coating, or surface finish, so downstream modeling should not infer strength grade or corrosion behavior from this result."
how_to_make:
  summary: "Treat as standard DIN 912 / ISO 4762-style M4x0.7 x 30 socket-head cap screw hardware"
  manufacturing_steps:
    - "Specify a DIN 912 socket-head cap screw with M4x0.7 thread and 30 mm nominal length, matching the row CAD/designation."
    - "Inspect diameter, length, socket head, and thread fit before assembly use."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0105_2AV6__views_2x2.png"
    cited_fact_or_basis: "The row designation includes standard DIN 912 and parameters M4x0.7x30x20; these parameters are complete enough for screw family, nominal metric thread, and length/interface, but incomplete for property class, coating, or exact supplier. The rendered preview confirms the socket-head cap screw shape."
    evidence_basis: "standard_part_convention"
  assumptions: []
  uncertainty_notes:
    - "The standard designation and CAD resolve the hardware family and basic interface, but not the supplier, strength class, coating, or production process."
kb_implications:
  - "item_granularity: simple_part - standard metric socket-head cap screw hardware that should map to a reusable steel fastener item rather than a machine-specific custom part."
---

# reAM250 BOM Row 105 - 2AV6

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0105_2AV6.md
source_research_sha256: "32bd16addbfb72d6948f7a0484718638e80bbb7ce0aa48b947ffbedda28fd45d"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed DIN 912 M4 screw function, CAD-derived per-screw and row mass, mild-steel material metadata, standard screw hardware route, and preview showing socket-head geometry."
decomposition:
  decision: simple_part
  rationale: "The row is a standard one-piece fastener used ten times, not a custom machine-specific part."
  proposed_subparts: []
process_abstraction:
  original_process_family: standard_metric_socket_head_screw_hardware
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - stock_preparation
    - forming
    - thread_forming
    - heat_treatment
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_small_fabrication_v0
      fit: direct
      reason: "Closest existing process anchor for small reusable screw hardware."
    - process_id: fastener_kit_medium_production_v0
      fit: partial
      reason: "Also covers generic fastener production concepts but is larger than this M4 screw."
    - process_id: machining_process_turning_v0
      fit: supporting
      reason: "Relevant for fallback screw-making from bar stock when thread rolling is unavailable."
    - process_id: heat_treatment_basic_v0
      fit: supporting
      reason: "Relevant if strength class is specified later."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers thread, length, socket, and head geometry checks."
  abstraction_decision: keep_original_family
  rationale: "The source row is already standard screw hardware, matching the fastener forming and thread rolling closure bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: threaded fastening for small mechanical joints
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.00401
    bom_quantity: 10
    row_total_mass_kg: 0.0401
    scale_class: tiny
  geometry_form: din_912_m4_socket_head_cap_screw_30_mm_length
merge_pool:
  eligible: true
  functional_purpose_key: fastening
  precision_guardrails:
    - thread_size
    - screw_length
    - head_socket_geometry
    - strength_class_if_specified
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Strength class, coating, and corrosion behavior are unspecified."
    - "Standard fasteners may be imported as kits until local thread-forming capacity is justified by volume."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups standard metric fasteners and evaluates kit-level closure."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as a generic M4 steel socket-head screw within a small fastener kit entry."
assumptions:
  - "The CAD part represents one screw and BOM quantity 10 represents identical instances."
  - "Mild steel material metadata is accepted, while strength class and coating remain guardrails."
unresolved:
  - "Property class, coating, exact supplier, and production route are not specified."
```
