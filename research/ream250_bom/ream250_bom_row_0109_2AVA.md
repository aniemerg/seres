---
row_identity:
  item: 2AVA
  cad_file: "2AVA_DIN 912 - M4x0,7x20x18,25"
  source_row_number: 109
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Socket-head cylinder cap screw used as M4 threaded fastening hardware in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVA_DIN 912 - M4x0,7x20x18,25.step; research/ream250_bom/ream250_bom_row_0109_2AVA__views_2x2.png"
    cited_fact_or_basis: "BOM row 109 identifies item 2AVA, quantity 20, CAD file '2AVA_DIN 912 - M4x0,7x20x18,25', description 'cylinder head cap screw'. The rendered CAD preview shows an externally threaded screw with cylindrical socket head and internal hex drive."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.00302
  basis: "Per screw. FreeCAD measured volume 384.920 mm^3 for one solid; assembly STEP material metadata gives Steel, Mild density 7850 kg/m^3. Calculation: 384.920e-9 m^3 * 7850 kg/m^3 = 0.0030216 kg per screw. BOM quantity is 20, so row total is about 0.0604 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVA_DIN 912 - M4x0,7x20x18,25.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measurement: 1 solid, volume 384.920331 mm^3, area 430.857616 mm^2, bounding box 24.00 x 7.58 x 7.58 mm. Local assembly STEP material extractor matched product name to material 'Steel, Mild' with density 7850 kg/m^3; kb/materials/properties.yaml lists generic steel density 7850 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - "The CAD solid represents one physical screw for the BOM row."
    - "The STEP density is interpreted as kg/m^3, consistent with the extractor note and local steel density table."
  uncertainty_notes:
    - "Thread and socket geometry are taken from the exported CAD; any supplier-specific head tolerances or minor chamfer differences would only slightly change this mass."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product '2AVA_DIN 912 - M4x0,7x20x18,25' returned material 'Steel, Mild' and density 7850 kg/m^3."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - "No coating, property class, or heat-treatment grade is specified by the BOM-side evidence."
how_to_make:
  summary: "Treat as standard M4 DIN 912 socket-head cap screw hardware.7 thread and 20 mm nominal length, or model later as a generic steel socket-head screw if local fastener production is expanded"
  manufacturing_steps:
    - "Verify thread, head diameter, socket drive, length, and quantity before installation."
    - "For later local manufacturing detail, split into steel wire/rod preparation, head forming, socket forming, thread rolling or cutting, finishing, and inspection."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0109_2AVA__views_2x2.png"
    cited_fact_or_basis: "BOM and manifest identify a cylinder head cap screw with CAD filename parameters DIN 912, M4x0.7, and 20 mm length; the rendered preview confirms socket-head screw geometry."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - "The BOM-side evidence does not specify a supplier part number, strength class, coating, or acceptance standard beyond the DIN 912-style designation in the CAD filename."
kb_implications:
  - "item_granularity: simple_part - Standard M4 socket-head cap screw hardware should map to a reusable fastener item rather than a reAM250-specific purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0109_2AVA.md
source_research_sha256: "8d4d4e614332c17e23b3a2c5cb7025c763275d91edbd340a64f99836147815a5"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the fastening function, CAD-derived per-unit and row-total mass, mild steel material metadata, standard fastener route, KB implications, and preview showing an M4 socket-head cap screw."
decomposition:
  decision: simple_part
  rationale: "The row is standard steel threaded hardware with no internal closure dependencies beyond fastener manufacture."
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
    - process_id: fastener_kit_small_fabrication_v0
      fit: partial
      reason: "Aggregates small fastener fabrication and kitting, matching this M4 row at closure level."
    - process_id: fastener_kit_medium_production_v0
      fit: poor_fit
      reason: "Documents integrated fastener production but targets larger mixed kits instead of M4 hardware."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Can cover fallback small-batch machined screw features if heading and thread rolling are not separately represented."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers thread, length, socket, head, and material checks."
  abstraction_decision: keep_original_family
  rationale: "The source evidence identifies standard socket-head screw hardware. The canonical fastener bucket is the correct closure handle before fastener merge review."
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
    mass_kg: 0.00302
    bom_quantity: 20
    row_total_mass_kg: 0.0604
    scale_class: small
  geometry_form: din_912_m4_socket_head_cap_screw
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
  post_merge_decision_notes: "Final import/local decision is deferred until merge review decides whether individual M4 sizing matters beyond small fastener kit modeling."
kb_staging:
  proposed_item_id: null
  notes: "Wait for fastener merge review; quantity 20 and 0.0604 kg row total should be preserved in staging."
assumptions:
  - "Mild steel STEP metadata is accepted for row-level classification."
  - "The DIN 912 M4 designation is standard enough to merge with other small threaded fastener rows under guardrails."
unresolved:
  - "Installed joint duty, property class, coating, exact grade, supplier tolerance, and final kit-level abstraction are not specified."
```
