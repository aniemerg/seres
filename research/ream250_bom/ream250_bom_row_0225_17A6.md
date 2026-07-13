---
row_identity:
  item: 17A6
  cad_file: 17A6_strut_profile_20X20_D108
  source_row_number: 225
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
  link_url: https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE
function:
  summary: >
    Short Bosch Rexroth 20x20 aluminum strut profile used as a light structural
    member in the reAM250 frame or support structure, with T-slot-like grooves
    for modular fastening.
  source:
    url_or_path: >
      design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv;
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A6_strut_profile_20X20_D108.step;
      research/ream250_bom/ream250_bom_row_0225_17A6__views_2x2.png
    cited_fact_or_basis: >
      BOM row 225 identifies item 17A6 as "strut profile" from Bosch Rexroth
      AG. FreeCAD measured a 131.0 mm x 20.0 mm x 20.0 mm single solid, and
      the rendered contact sheet shows a slotted rectangular extrusion profile.
    evidence_basis: bom_provided
  assumptions:
    - The row represents one cut profile segment because quantity is 1 and the CAD export contains one solid.
  uncertainty_notes:
    - The exact installed load path is not identified by the row alone, so the function is limited to structural frame/support use.
mass:
  value_kg: 0.0604
  basis: >
    Per unit. FreeCAD volume is 22355.677 mm3, equal to 0.000022355677 m3.
    Multiplying by the row-specific STEP density of 2700 kg/m3 gives
    0.06036 kg for the single 131 mm cut length. Quantity is 1, so row total is
    also about 0.0604 kg.
  source:
    url_or_path: >
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A6_strut_profile_20X20_D108.step;
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step;
      kb/materials/properties.yaml
    cited_fact_or_basis: >
      FreeCAD measured 1 solid, volume 22355.677 mm3, surface area
      23559.111 mm2, and bounding box 131.0 mm x 20.0 mm x 20.0 mm. The local
      assembly STEP material extractor returned material "Aluminum 6061" with
      density 2700.0 for product 17A6_strut_profile_20X20_D108. The local
      density table lists aluminum density as 2700 kg/m3.
    evidence_basis: bom_provided
  assumptions:
    - The STEP solid volume is treated as the physical aluminum volume of one row item.
    - The local aluminum density constant is appropriate for the STEP material label Aluminum 6061.
  uncertainty_notes:
    - CAD export tolerances and small modeled details may shift the mass slightly, but the estimate is within the needed BOM planning scale.
material:
  primary_material: Aluminum 6061
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: >
      The local assembly STEP material extractor matched product
      17A6_strut_profile_20X20_D108 and returned material "Aluminum 6061" with
      density 2700.0.
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - Surface treatment is not explicit in the local material metadata; Bosch strut profiles are commonly anodized, but this row-specific result keeps the sourced material to Aluminum 6061.
how_to_make:
  summary: >
    Model as cut-to-length aluminum extrusion stock: extrude a 20x20 slotted
    6061 aluminum profile, cut to the CAD length, deburr, and optionally anodize
    Or otherwise finish before assembly.
  manufacturing_steps:
    - Extrude Aluminum 6061 through a die matching the 20x20 slotted profile.
    - Cut the extrusion to the CAD-measured 131 mm length.
    - Deburr cut ends and inspect slot geometry and overall length.
    - Apply anodizing or comparable corrosion-resistant finish if required by the local assembly environment.
  source:
    url_or_path: >
      Design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A6_strut_profile_20X20_D108.step;
      Https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE
    cited_fact_or_basis: >
      The BOM URL route and row identify a Bosch Rexroth strut profile, while
      The CAD geometry shows a constant 20x20 slotted cross-section. targeted_web_search:
      Queries tried "Bosch Rexroth strut profile 20x20 manufacturing extrusion
      Anodized" and "Bosch Rexroth 20x20 strut profile aluminum catalog" results
      Supported aluminum profile stock but did not provide a row-specific factory
      Process for this cut length.
    evidence_basis: engineering_hypothesis
  assumptions:
    - A constant-section aluminum strut profile is best represented as extruded stock cut to length.
    - Use a generic aluminum extrusion and finishing workflow rather than a machine-specific custom machining route.
  uncertainty_notes:
    - The exact Bosch production process and finish for this row are not specified in the BOM or local STEP metadata.
kb_implications:
  - "item_granularity: simple_part - Treat as reusable aluminum profile stock or cut-to-length extrusion rather than a unique machine-specific part."
---

Research result for reAM250 BOM row 225.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0225_17A6.md
source_research_sha256: "ec5222030add38a71a19f85a64cf57f49f3705a986c34bce328c3b51a0638d69"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed function, per-unit mass, Aluminum 6061 material evidence, extrusion/cut-to-length route, and CAD preview evidence for the 20x20 slotted profile."
decomposition:
  decision: simple_part
  rationale: "The row is one short constant-section aluminum strut profile segment, not a vendor module nor an assembly with hidden internal closure dependencies."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - cutting
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Represents aluminum extrusion from ingot to profile stock, but its current item bindings are heat-sink-specific rather than generic strut profile stock."
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Covers saw and abrasive cutting of metal stock to the required short length."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant if the final closure item preserves anodized plus comparable corrosion-resistant aluminum surface treatment."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers visual and dimensional checks for length, straightness, and slot geometry before frame assembly."
  abstraction_decision: keep_original_family
  rationale: "The source route is already a structural aluminum extrusion workflow; the closure abstraction keeps the same family while avoiding a row-specific Bosch profile item until merge review."
  process_guardrails:
    tolerance: low
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: light structural member for modular fastening in the frame support structure
  material: aluminum_alloy_6061
  scale_or_capacity:
    mass_kg: 0.0604
    bom_quantity: 1
    row_total_mass_kg: 0.0604
    scale_class: small
  geometry_form: cut_20x20_slotted_t_slot_extrusion_profile
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - slot_geometry
    - cut_length
    - straightness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Requires an extrusion die plus equivalent reusable profile-forming capability for the 20x20 slotted section."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review; likely mergeable with other small aluminum frame/profile members if slot geometry is closure-equivalent."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning a closure item ID; likely candidate family is small aluminum structural profile stock cut to length."
assumptions:
  - "Aluminum 6061 from STEP metadata is adequate for closure material classification as aluminum alloy."
  - "The slotted modular interface matters for assembly compatibility, but exact Bosch profile geometry can be reviewed against other profile rows during merge."
  - "Optional anodizing is treated as supporting surface finishing rather than part identity unless later evidence shows the finish is function-critical."
unresolved:
  - "Exact installed load path and whether the T-slot geometry is required at full commercial precision are not known from this row alone."
```
