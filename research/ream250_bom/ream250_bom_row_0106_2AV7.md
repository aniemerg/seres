---
row_identity:
  item: "2AV7"
  cad_file: "2AV7_DIN 912 - M4x0,7x25x23,25"
  source_row_number: 106
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 M4 x 0.7 x 25 cylinder-head/socket-head cap screw used as standard fastening hardware in the reAM250 assembly; BOM quantity is 8."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV7_DIN 912 - M4x0,7x25x23,25.step; research/ream250_bom/ream250_bom_row_0106_2AV7__views_2x2.png"
    cited_fact_or_basis: "BOM row 106 lists item 2AV7, quantity 8, CAD file '2AV7_DIN 912 - M4x0,7x25x23,25', and description 'cylinder head cap screw'. The manifest maps the row to the matched part STEP. FreeCAD measured one solid with a 29.00 x 7.58 x 7.58 mm bounding box, and the rendered preview shows a socket-head screw form with cylindrical head, shank, threaded end, and internal hex socket."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 912 designation is interpreted as the standard socket-head cap screw form represented by the row's CAD and description."
  uncertainty_notes:
    - "The row does not expose the mating parts or exact fastening location, so the function is limited to standard removable mechanical fastening hardware."
mass:
  value_kg: 0.00351
  basis: "Per unit. BOM quantity is 8, so the row total is about 0.0281 kg. FreeCAD measured CAD volume 447.752 mm^3 = 0.000000447752 m^3. Assembly STEP metadata reports Steel, Mild with density 7850 kg/m^3; computed mass = 0.000000447752 m^3 * 7850 kg/m^3 = 0.003515 kg per screw, rounded to 0.00351 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV7_DIN 912 - M4x0,7x25x23,25.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 447.752 mm^3, area 493.689 mm^2, and bounding box 29.00 x 7.58 x 7.58 mm. The local assembly STEP material extractor matched product '2AV7_DIN 912 - M4x0,7x25x23,25' to material Steel, Mild with density 7850.0. The local density table lists steel density_kg_per_m3: 7850."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume for one screw."
    - "The assembly STEP density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "The CAD-derived mass may differ from catalog screw weight if thread roots, socket recess, chamfers, or end details are simplified, but the estimate is adequate for BOM-level mass accounting."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product '2AV7_DIN 912 - M4x0,7x25x23,25' to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a steel family but not a property class, coating, strength grade, or heat treatment."
how_to_make:
  summary: "Prepare as a standard DIN 912 M4 x 0.7 x 25 mild-steel socket-head cap screw; for assembly, specify the standard designation, draw from locally manufactured standard hardware stock, inspect the thread/head fit, and install as one of the eight row fasteners"
  manufacturing_steps:
    - "Specify DIN 912 M4 x 0.7 x 25 cylinder-head/socket-head cap screw, compatible with the row CAD envelope and mild-steel material metadata."
    - "Machine-specific custom part"
    - "Before assembly, verify thread size, screw length, head/socket form, and any needed coating or strength requirements against the mating assembly."
    - "Install as standard reusable fastening hardware in the relevant reAM250 subassembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV7_DIN 912 - M4x0,7x25x23,25.step; research/ream250_bom/ream250_bom_row_0106_2AV7__views_2x2.png"
    cited_fact_or_basis: "The BOM row names a DIN 912 M4 x 0.7 x 25 cylinder head cap screw, and the CAD preview/STEP geometry show the corresponding socket-head screw shape with a 29.00 mm overall CAD envelope along the screw axis. The route is a procurement/standard-hardware-stock route, not a claimed screw factory manufacturing process."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "If local screw manufacture is later modeled, the production process would need separate evidence for heading, socket forming, thread rolling, heat treatment, and coating; those operations are not specified by this row."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard M4 DIN 912 steel screw hardware, preferably consolidated with other DIN 912 M4 socket-head screws rather than as a reAM250-specific custom item."
---

Research result for reAM250 BOM row 106.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0106_2AV7.md
source_research_sha256: "e082b255dd9f9ce6885e40626866a4d353d225302492964aa27689842334a8f8"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the DIN 912 screw function, BOM quantity, CAD-derived mild-steel mass, material metadata, standard-hardware route, KB implication, and CAD preview showing a socket-head cap screw."
decomposition:
  decision: simple_part
  rationale: "The row is a single standard screw; subpart decomposition would not improve closure analysis."
  proposed_subparts: []
process_abstraction:
  original_process_family: standard_steel_socket_head_screw
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - stock_preparation
    - forming
    - thread_forming
    - precision_machining
    - heat_treatment
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_small_fabrication_v0
      fit: partial
      reason: "Anchors small fastener production, though this row needs DIN 912 socket-head geometry and M4 thread details."
    - process_id: machining_process_turning_v0
      fit: supporting
      reason: "Relevant to screw shank and head finishing if not fully cold-headed."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers socket recess and local head features at coarse closure level."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, thread, head, and socket fit inspection."
  abstraction_decision: substitute_process_family
  rationale: "The row evidence uses a standard-stock procurement route; for lunar closure the appropriate abstraction is local fastener forming and thread production."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: removable mechanical fastening with a socket-head cap screw
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.00351
    bom_quantity: 8
    row_total_mass_kg: 0.0281
    scale_class: tiny
  geometry_form: m4_socket_head_cap_screw_twenty_five_mm_length
merge_pool:
  eligible: true
  functional_purpose_key: mechanical_fastening
  precision_guardrails:
    - thread_size
    - screw_length
    - head_socket_form
    - strength_grade
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Strength grade, coating, heat treatment, and socket-forming requirements are not resolved from the row."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review consolidates standard screws across nearby sizes and materials."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely merge with other small steel socket-head cap screws within size guardrails."
assumptions:
  - "The mild-steel STEP material metadata is adequate for row-level closure planning."
  - "DIN 912 standard geometry should be generalized rather than staged as a reAM250-specific item."
unresolved:
  - "Property class, coating, heat treatment, exact screw standard tolerance, and mating assembly location remain unresolved."
```
