---
row_identity:
  item: "2AL211"
  cad_file: "2AL211_motor"
  source_row_number: 64
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.br-automation.com/en/products/80mpf5500d114-01/"
function:
  summary: "B&R 80MPF5.500D114-01 2-phase hybrid stepper motor module with 60 mm flange, incremental encoder, and holding brake, used as an actuated motion source in the reAM250."
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step; research/ream250_bom/ream250_bom_row_0064_2AL211__views_2x2.png"
    cited_fact_or_basis: "BOM row 64 identifies item 2AL211 as quantity 1, CAD file 2AL211_motor, manufacturer B&R, and link URL for 80MPF5.500D114-01. The B&R page identifies 80MPF5.500D114-01 as a stepper motor with 60 mm flange, length 184.4 mm, incremental encoder and brake; it also lists 3.5 Nm holding torque, 2.5 Nm stall torque, and 24 VDC brake data. FreeCAD measured one solid with bounding box 204.40 x 60.00 x 78.20 mm, and the preview shows a long rectangular motor body with square flange and shaft."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied CAD, manifest row, and B&R URL describe the same physical motor despite the BOM text containing extra 'elastomer jaw coupling GN 2240-' wording."
  uncertainty_notes:
    - "The CSV description appears to include conflicting trailing coupling text, but the manufacturer, product URL, CAD filename, CAD geometry, and B&R product page all match the stepper motor identity."
mass:
  value_kg: 1.8
  basis: "Per-unit mass for quantity 1. The B&R mechanical properties table gives weight as 1,800 g, so the BOM row total is also 1.8 kg. FreeCAD measured CAD volume 556244.165 mm^3; using the vendor weight implies an effective packaged motor density of about 3236 kg/m^3, plausible for a motor assembly with metal, copper, magnet, air gaps, encoder, and brake."
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step"
    cited_fact_or_basis: "The B&R page lists mechanical weight as 1,800 g and length 184.4 mm. FreeCAD measured one solid with volume 556244.165 mm^3 and bounding box 204.40 x 60.00 x 78.20 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The vendor listed weight is used as the mass of one complete motor module represented by the row."
  uncertainty_notes:
    - "The CAD length is slightly longer than the B&R listed motor length, likely because the per-row CAD includes shaft/flange detail; the vendor weight remains the best mass basis for the complete row item."
material:
  primary_material: "multi-material electromechanical motor module: unknown metal housing/frame and shaft, magnetic steel laminations/rotor, permanent magnet material, copper windings/coils, brake and encoder components"
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step"
    cited_fact_or_basis: "The B&R page identifies the row product as a 2-phase hybrid stepper motor with incremental encoder and brake, but does not state material grades. Assembly STEP material extraction for product 2AL211_motor returned only material 'Generic' with density 1000.0, which is placeholder metadata. FreeCAD and the preview show a motor-like module but no material split. targeted_web_search: tried 'B&R 80MPF5.500D114-01 material housing copper winding magnet', '80MPF5.500D114-01 datasheet material housing', and '2-phase hybrid stepper motor construction materials copper windings permanent magnet'; results found row-matched motor specifications and general hybrid-stepper construction references, but no row-specific B&R material or grade list."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The broad material set follows from the B&R row identity as a hybrid stepper motor with brake and encoder, combined with standard motor construction requirements."
  uncertainty_notes:
    - "No row-specific source resolves housing alloy, shaft alloy, magnet grade, winding mass, brake friction material, or encoder/electronics material splits, so downstream KB modeling should treat this as a purchased electromechanical module until a teardown or manufacturer material declaration is available."
how_to_make:
  summary: "Local production as a future sub-BOM problem covering motor laminations, windings, rotor/magnets, bearings, encoder, brake, housing, shaft, assembly, and electrical test"
  manufacturing_steps:
    - "Verify nameplate/specification match: 5 A parallel wiring, 3.5 Nm holding torque, 2.5 Nm stall torque, ABR 24 VDC encoder, and 24 VDC brake."
    - "Inspect the CAD/interface envelope against the reAM250 mounting location before installation."
    - "If later localized, decompose into a dedicated motor sub-BOM and process chain for laminated stator/rotor stack, copper winding, shaft and bearing assembly, permanent magnet rotor, brake, encoder, housing, calibration, and test."
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step; research/ream250_bom/ream250_bom_row_0064_2AL211__views_2x2.png"
    cited_fact_or_basis: "The B&R page provides the row-matched product identity and specifications: 80MPF5.500D114-01, 2-phase hybrid stepper motor, 60 mm flange, incremental encoder and brake, 5 A parallel wiring, 3.5 Nm holding torque, 2.5 Nm stall torque, and brake electrical data. CAD preview and FreeCAD geometry confirm a complete motor module envelope rather than a simple one-piece bracket or stock material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
kb_implications:
  - "item_granularity: complex_module - model as a complex/calibrated stepper motor complex module for this pass; split into a motor sub-BOM only when local electromechanical manufacturing and calibration details are intentionally added."
---

Result generated for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0064_2AL211.md
source_research_sha256: "a10146664251143f93b5146e887dd17331c6e81d7eb317ed613e7c64d9f1bfee"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the motor function, vendor weight, multi-material module evidence, decomposition-oriented manufacturing notes, KB implications, and CAD preview before conversion."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a complete hybrid stepper motor module with encoder and holding brake. It contains magnetic, copper, bearing, housing, brake, encoder, and calibration dependencies that should be exposed before any local-manufacture decision."
  proposed_subparts:
    - laminated_stator_and_rotor_stack
    - copper_windings
    - permanent_magnet_rotor
    - shaft_and_bearing_set
    - motor_housing_and_flange
    - holding_brake_module
    - incremental_encoder_module
    - wiring_and_connector_set
process_abstraction:
  original_process_family: vendor_electromechanical_stepper_motor_module
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - assembly
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: motor_assembly_standard_fabrication_v0
      fit: partial
      reason: "Relevant to a future simplified motor assembly route, but it does not cover the encoder, brake, magnet, winding, and calibration detail in this row."
    - process_id: motor_final_assembly_v0
      fit: supporting
      reason: "Anchors final motor assembly work if the module is decomposed into local subparts later."
    - process_id: electronic_assembly_v0
      fit: supporting
      reason: "Relevant to encoder and connector electronics, but not the magnetic and mechanical motor body."
    - process_id: calibration_basic_v0
      fit: supporting
      reason: "Covers functional calibration and verification after assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers interface envelope, flange, shaft, and mounting inspection."
  abstraction_decision: needs_human
  rationale: "The row is outside a simple fabrication bucket because it is a calibrated multi-material motor with brake and encoder. Phase 1 should preserve it as a decomposition target and likely import-risk item."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: provide controlled rotary motion actuation with position feedback and holding brake
  material: mixed_electromechanical
  scale_or_capacity:
    mass_kg: 1.8
    bom_quantity: 1
    row_total_mass_kg: 1.8
    scale_class: small
  geometry_form: rectangular_stepper_motor_with_60mm_flange_shaft_encoder_and_brake
merge_pool:
  eligible: true
  functional_purpose_key: motion_actuation
  precision_guardrails:
    - holding_torque
    - stall_torque
    - flange_size
    - shaft_interface
    - encoder_feedback
    - brake_voltage
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Hybrid stepper motor requires laminated magnetic stack, copper windings, magnet materials, bearings, brake, encoder, wiring, calibration, and electrical test."
    - "Vendor specs include torque, encoder, and brake behavior that may be hard to reproduce within the current local closure scope."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups comparable motion actuators and a later decomposition pass defines a motor sub-BOM."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review and decomposition; do not create a row-specific B&R SKU item unless no reusable actuator abstraction fits."
assumptions:
  - "Vendor listed 1.8 kg weight represents the complete motor module."
  - "The trailing coupling text in the BOM description is treated as conflicting metadata; the product URL, CAD file, and geometry support the motor identity."
  - "The encoder and brake are part of the module for closure purposes."
unresolved:
  - "Housing alloy, shaft alloy, magnet grade, winding mass, brake material, encoder construction, connector details, and calibration requirements are not resolved by row evidence."
```
