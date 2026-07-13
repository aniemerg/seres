---
row_identity:
  item: "2AV3"
  cad_file: "2AV3_DIN 912 - M8x1,25x40x28"
  source_row_number: 102
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 M8 x 1.25 x 40 cylinder-head/socket-head cap screw used as standard fastening hardware in the reAM250 assembly; BOM quantity is 30."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV3_DIN 912 - M8x1,25x40x28.step; research/ream250_bom/ream250_bom_row_0102_2AV3__views_2x2.png"
    cited_fact_or_basis: "BOM row 102 lists item 2AV3, quantity 30, CAD file '2AV3_DIN 912 - M8x1,25x40x28', and description 'cylinder head cap screw'. The manifest maps the row to the matched part STEP. FreeCAD measured one solid with a 48.00 x 14.07 x 14.07 mm bounding box, and the rendered preview shows a socket-head screw form with a cylindrical shank/threaded end and larger head."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 912 designation is interpreted as the standard socket-head cap screw form represented by the row's CAD and description."
  uncertainty_notes:
    - "The row does not expose the mating part or exact fastening location, so the function is limited to standard mechanical fastening hardware."
mass:
  value_kg: 0.0229
  basis: "Per unit. BOM quantity is 30, so the row total is about 0.687 kg. FreeCAD measured CAD volume 2911.837 mm^3 = 0.000002911837 m^3. Assembly STEP metadata reports Steel, Mild with density 7850 kg/m^3; computed mass = 0.000002911837 m^3 * 7850 kg/m^3 = 0.022858 kg per screw, rounded to 0.0229 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV3_DIN 912 - M8x1,25x40x28.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 2911.837 mm^3, area 1658.514 mm^2, and bounding box 48.00 x 14.07 x 14.07 mm. The local assembly STEP material extractor matched product '2AV3_DIN 912 - M8x1,25x40x28' to material Steel, Mild with density 7850.0. The local density table lists steel density_kg_per_m3: 7850."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume for one screw."
    - "The assembly STEP density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "The CAD-derived mass may differ from catalog screw weight if the thread model, socket recess, or head detail is simplified, but the estimate is adequate for BOM-level mass accounting."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product '2AV3_DIN 912 - M8x1,25x40x28' to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a steel family but not a property class, coating, strength grade, or heat treatment."
how_to_make:
  summary: "Prepare as a standard DIN 912 M8 x 1.25 x 40 mild-steel socket-head cap screw; for assembly, specify the standard designation, draw from locally manufactured standard hardware stock, inspect the thread/head fit, and install as one of the thirty row fasteners"
  manufacturing_steps:
    - "Specify DIN 912 M8 x 1.25 x 40 cylinder-head/socket-head cap screw, compatible with the row CAD envelope and mild-steel material metadata."
    - "Machine-specific custom part"
    - "On receipt or before assembly, verify thread size, screw length, head/socket form, and material/coating requirements against the assembly need."
    - "Install as standard reusable fastening hardware in the relevant reAM250 subassembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV3_DIN 912 - M8x1,25x40x28.step; research/ream250_bom/ream250_bom_row_0102_2AV3__views_2x2.png"
    cited_fact_or_basis: "The BOM row names a DIN 912 M8 x 1.25 x 40 cylinder head cap screw, and the CAD preview/STEP geometry show the corresponding socket-head screw shape with a 48.00 mm overall CAD envelope along the screw axis. The route is a procurement/standard-hardware-stock route, not a claimed screw factory manufacturing process."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "If local screw manufacture is later modeled, the production process would need separate evidence for heading, socket forming, thread rolling, heat treatment, and coating; those operations are not specified by this row."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard M8 DIN 912 steel screw hardware, not as a purchased module or machine-specific custom assembly."
---

Research result for reAM250 BOM row 102.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0102_2AV3.md
source_research_sha256: "0bb324e15ce4b71a702cf5c420ae56ce283c1a82a444178775423a655aa83ef6"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the fastening function, CAD-derived per-unit and row-total mass, mild steel material metadata, standard hardware route, KB implications, and preview showing a DIN 912 M8 socket-head screw."
decomposition:
  decision: simple_part
  rationale: "The row is standard steel threaded hardware; closure can treat it as a simple fastener item without internal subparts."
  proposed_subparts: []
process_abstraction:
  original_process_family: standard_fastener_forming_threading
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - forming
    - thread_forming
    - precision_machining
    - heat_treatment
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_medium_production_v0
      fit: partial
      reason: "Aggregates M6-M12 class fastener production and kitting, matching this M8 row at closure level."
    - process_id: fastener_kit_small_fabrication_v0
      fit: poor_fit
      reason: "Useful as a small-fastener analogy but sized below this M8 screw family."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Can cover fallback small-batch machined screw features if heading and thread rolling are not separately represented."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers thread, length, socket, head, and material checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is standard fastener hardware. The row should enter the fastener forming and thread rolling bucket rather than become a reAM250-specific machined part."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "removable threaded fastening"
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.0229
    bom_quantity: 30
    row_total_mass_kg: 0.687
    scale_class: small
  geometry_form: din_912_m8_socket_head_cap_screw
merge_pool:
  eligible: true
  functional_purpose_key: threaded_fastening
  precision_guardrails:
    - thread_size
    - socket_fit
    - fastener_property_class
    - coating
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Fastener property class, coating, exact steel grade, and heat treatment are unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review decides whether individual M8 sizing matters beyond medium fastener kit modeling."
kb_staging:
  proposed_item_id: null
  notes: "Wait for fastener merge review; quantity 30 and 0.687 kg row total should be preserved in staging inputs."
assumptions:
  - "Mild steel STEP metadata is accepted for row-level classification."
  - "The DIN 912 M8 designation is standard enough to merge with other threaded fastener rows under guardrails."
unresolved:
  - "Installed joint duty, property class, coating, exact grade, and final kit-level abstraction are not specified."
```
