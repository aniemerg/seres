---
row_identity:
  item: "3C"
  cad_file: "3C_reduction_T_pipe_ISO_K_DN63_KF_DN40_320RTR063-040"
  source_row_number: 114
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040"
function:
  summary: "Reducer tee vacuum piping component that connects a DN 63 ISO-K port to a reduced DN 40 ISO-KF branch/connection in the reAM250 vacuum plumbing."
  source:
    url_or_path: "https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf"
    cited_fact_or_basis: "Row-matched Pfeiffer datasheet names order number 320RTR063-040 as a reducer tee, DN 63 ISO-K/40 KF, and lists the connection flange as DN 63 ISO-K / DN 40 ISO-KF. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access; the alternate datasheet is a Pfeiffer product datasheet for the same manufacturer, order number, and DN 63 ISO-K/40 KF product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM product ID 320RTR063-040 and manufacturer Pfeiffer Vacuum identify the same reducer tee described in the datasheet."
  uncertainty_notes:
    - "The local CAD preview shows the reduced flange/tube geometry but not the full 176 mm datasheet envelope, so CAD shape evidence is treated as supportive rather than complete for function."
mass:
  value_kg: 0.1164
  basis: "Per-unit estimate from FreeCAD STEP volume 14496.435 mm^3 multiplied by local stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml, giving 0.1164 kg each. BOM quantity is 2, so the row total is about 0.2328 kg if this CAD volume represents one complete row item."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3C_reduction_T_pipe_ISO_K_DN63_KF_DN40_320RTR063-040.step; kb/materials/properties.yaml; https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 14496.434917 mm^3, area 13675.173988 mm^2, and bounding box 59.53 x 47.92 x 59.53 mm; local density table lists stainless_steel_304 at 8030 kg/m^3; row-matched Pfeiffer datasheet states stainless steel 304/1.4301. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access; the alternate datasheet is a Pfeiffer product datasheet for the same manufacturer, order number, and DN 63 ISO-K/40 KF product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single CAD solid volume is used as the per-unit physical volume represented by this row's STEP file."
    - "The part is modeled as fully stainless steel 304/1.4301 for mass calculation."
  uncertainty_notes:
    - "Mass may be low for the complete commercial reducer tee because the datasheet dimensions include A 176 mm, B 75 mm, C 70 mm, and D 40.5 mm, while the local STEP bounding box is only about 59.53 x 47.92 x 59.53 mm."
material:
  primary_material: "stainless steel 304 / EN 1.4301"
  source:
    url_or_path: "https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf"
    cited_fact_or_basis: "Row-matched Pfeiffer datasheet states reducer tee, stainless steel 304/1.4301, DN 63 ISO-K/40 KF, and lists materials in contact with media as stainless steel 1.4301 (AISI 304). official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access; the alternate datasheet is a Pfeiffer product datasheet for the same manufacturer, order number, and DN 63 ISO-K/40 KF product identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Assembly STEP material extraction returned only Generic with density 1000.0, so local STEP metadata does not independently confirm the grade."
how_to_make:
  summary: "Welded and machined stainless vacuum tubing/flange fabrication followed by leak testing and surface finishing"
  manufacturing_steps:
    - "Cut or form 304/1.4301 stainless tube sections and flange blanks for the DN 63 ISO-K and DN 40 ISO-KF interfaces."
    - "Machine flange lips, sealing faces, bores, and weld-prep edges to ISO-K/ISO-KF geometry."
    - "Weld the reduced tee body from the inside where accessible, finish external welds where geometry prevents internal-only welding, then clean/passivate."
    - "Helium leak-test and inspect sealing surfaces before installation."
  source:
    url_or_path: "https://vacuum-shop.com/2076398/downloads/datasheets/Datasheet_320RTR063-040_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3C_reduction_T_pipe_ISO_K_DN63_KF_DN40_320RTR063-040.step"
    cited_fact_or_basis: "Datasheet supports procurement identity, stainless material, ISO-K/ISO-KF interfaces, pressure range, and temperature range; CAD preview shows a flanged reducer/tube form. targeted_web_search: exact queries \"320RTR063-040 weight\", \"320RTR063-040 kg\", and \"Reducer tee 320RTR063-040 weight\" found row-matched datasheet/catalog pages but no directly stated manufacturing process or mass. bom_url_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTR063_040 returned HTTP 403 to local curl/browser access."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common stainless high-vacuum fitting practice inferred from geometry and material; the cited datasheet does not state the fabrication process."
  uncertainty_notes:
    - "Detailed weld sequence, wall thickness, and acceptance criteria should be sourced from a fabrication drawing or supplier manufacturing specification before modeling a production recipe."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable stainless vacuum piping fitting/reducer tee rather than a reAM250-specific assembly; model vendor procurement first and refine local stainless vacuum-fitting fabrication later."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0114_3C.md
source_research_sha256: "2cd32464df048e3ffa8a3b35ab97b65d718e588b6cdbb93e1720accac7bd1f19"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the DN63 ISO-K to DN40 ISO-KF reducer tee function, 0.1164 kg per-unit CAD-derived mass with BOM quantity 2 and 0.2328 kg row total, stainless 304 material evidence, welded/machined vacuum fitting route, KB implication, and CAD preview showing reduced flanged tube geometry."
decomposition:
  decision: simple_part
  rationale: "The row is one stainless vacuum plumbing fitting with no internal mechanisms; closure can model it as a reusable flanged connector/fitting with leak-test requirements."
  proposed_subparts: []
process_abstraction:
  original_process_family: welded_machined_stainless_vacuum_fitting
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - joining
    - surface_finishing
    - cleaning
    - leak_testing
    - pressure_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: tube_bending_and_cutting_v0
      fit: partial
      reason: "Covers tube stock preparation and cutting, though reducer tee geometry needs flange and tee fabrication."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to flange lips, sealing faces, bores, and weld-prep features."
    - process_id: welding_and_fabrication_v0
      fit: partial
      reason: "Covers welded stainless fitting fabrication, but not high-vacuum acceptance criteria by itself."
    - process_id: surface_treatment_basic_v0
      fit: supporting
      reason: "Covers cleaning, passivation, and surface preparation after welding."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Directly relevant to vacuum fitting acceptance after fabrication."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and visual checks of flanges and sealing faces."
  abstraction_decision: keep_original_family
  rationale: "The source evidence is already a stainless vacuum fitting; the selected bucket keeps the fitting role, machining, welding, cleaning, and leak testing visible without making a row-specific machine."
  process_guardrails:
    tolerance: review
    surface_finish: sealing_face_review
    sealing_quality: high
    alignment_accuracy: moderate
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "reduced flanged plumbing connection for vacuum pipework"
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.1164
    bom_quantity: 2
    row_total_mass_kg: 0.2328
    scale_class: small
  geometry_form: reduced_iso_k_to_iso_kf_flanged_tube_fitting
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - dn63_iso_k_interface
    - dn40_iso_kf_interface
    - sealing_face_finish
    - leak_tightness
    - cad_datasheet_size_mismatch
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "High-vacuum leak tightness, sealing-face finish, wall thickness, and weld acceptance criteria are not specified."
    - "CAD bounding box appears smaller than the datasheet envelope, creating uncertainty in mass and exact geometry."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other stainless vacuum plumbing fittings and flange reducers."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic stainless vacuum plumbing connector/reducer family."
assumptions:
  - "BOM quantity is 2, mass is 0.1164 kg per unit, and row total mass is 0.2328 kg using the CAD-derived estimate."
  - "Stainless steel 304/1.4301 is accepted from the row-matched datasheet."
  - "Leak testing is treated as mandatory process support for any local fabrication path."
unresolved:
  - "Exact geometry mismatch between CAD preview and datasheet, wall thickness, weld sequence, leak-test standard, and sealing-face finish remain unresolved."
  - "Whether this row should merge by DN interface family, flange family, mass range, and fitting geometry is deferred."
```
