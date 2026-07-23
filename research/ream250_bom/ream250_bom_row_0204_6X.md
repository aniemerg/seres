---
row_identity:
  item: "6X"
  cad_file: "6X_connection_linear_guide_top"
  source_row_number: 204
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom upper connection bracket for the reAM250 linear-guide assembly; it appears to tie the top of a linear guide or guide-adjacent carriage support into the surrounding frame."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6X_connection_linear_guide_top.step; research/ream250_bom/ream250_bom_row_0204_6X__views_2x2.png"
    cited_fact_or_basis: "BOM row 204 states item 6X, quantity 1, CAD file 6X_connection_linear_guide_top. The manifest maps the row to gold_export/parts/6X_connection_linear_guide_top.step as a matched part export. FreeCAD measured one solid with bounding box 58.00 x 121.50 x 179.00 mm. The rendered contact sheet shows a tall ribbed bracket with a top mounting face/flange and side/back connection geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename connection_linear_guide_top and visible bracket geometry are interpreted as an upper mechanical connector for the neighboring linear-guide subsystem rather than as the guide rail or bearing block itself."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the local bracket role, but not the exact mating face, fastener pattern, or load case in the larger axis assembly."
mass:
  value_kg: 1.4
  basis: "FreeCAD volume 175328.702 mm^3 equals 0.000175329 m^3. The assembly STEP material extractor reports Stainless Steel, Austenitic with density 8000 kg/m^3 for 6X_connection_linear_guide_top, giving 1.4026 kg per unit. BOM quantity is 1, so the row total is also about 1.40 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6X_connection_linear_guide_top.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 175328.702 mm^3, area 69530.569 mm^2, and bounding box 58.00 x 121.50 x 179.00 mm. Local assembly STEP material extraction matched product 6X_connection_linear_guide_top to material Stainless Steel, Austenitic and density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured row item."
    - "The extracted 8000 kg/m^3 density is used directly as the calculation density for the austenitic stainless steel part."
  uncertainty_notes:
    - "The estimate depends on the CAD export volume being a finished solid without suppressed pockets, inserts, or separate fasteners; no separate physical scale measurement was available."
material:
  primary_material: "austenitic stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local STEP material extractor matched product 6X_connection_linear_guide_top and returned material Stainless Steel, Austenitic with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata resolves the material family, but not the exact stainless grade, heat treatment, finish, or passivation state."
how_to_make:
  summary: "Fabricate as a custom stainless-steel linear-guide connector bracket, most plausibly by CNC machining from a stainless block or by welding/cutting stainless plate features followed by finish machining of the mounting faces and holes."
  manufacturing_steps:
    - "Start from austenitic stainless steel stock large enough for the roughly 58 x 121.5 x 179 mm envelope, or from cut stainless plate sections if modeled as a weldment."
    - "Rough-cut the outer profile and ribbed web geometry by CNC milling, waterjet/laser cutting plus welding, or a hybrid route selected from available shop capability."
    - "Finish-machine the top mounting face, side/back connection faces, and any fastener holes or slots required by the mating linear-guide hardware."
    - "Deburr the ribs and edges, clean for machine assembly, and inspect bracket flatness, perpendicularity, hole positions, and linear-guide alignment interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6X_connection_linear_guide_top.step; research/ream250_bom/ream250_bom_row_0204_6X__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one austenitic-stainless solid with a 58.00 x 121.50 x 179.00 mm envelope, a top flange/mounting face, and ribbed bracket/web geometry. targeted_web_search: searched \"6X_connection_linear_guide_top\", \"reAM250 6X linear guide top\", and \"connection linear guide top stainless steel bracket\" results were duplicate reAM250 BOM text or general linear-guide references, with no row-specific drawing, tolerance, or manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part because the BOM row has no manufacturer, product ID, or link URL, and the manifest classifies it as a matched part rather than a vendor component."
    - "The manufacturing route is inferred from stainless material, bracket geometry, and the need for accurate linear-guide mounting interfaces."
  uncertainty_notes:
    - "The source package does not specify whether the design intent is monolithic machining, weldment fabrication, casting, additive manufacture, or a specific surface finish."
kb_implications:
  - "item_granularity: simple_part - model later as one custom stainless linear-guide connector bracket, not as a purchased guide module."
---

Research result for reAM250 BOM row 204.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0204_6X.md
source_research_sha256: "35cd032e1f2d2095659cb72d779a8dd8446ca65d56cc3bce47d408e63fca380b"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the upper linear-guide connection function, CAD-derived stainless mass, material metadata, inferred fabrication route, and ribbed bracket geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one custom stainless connector body; guide rail, bearing block, fasteners, and surrounding frame members are separate BOM rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_bracket_machining_with_weldment_alternative
  primary_process_bucket: general_metal_additive_with_finish_machining
  supporting_processes:
    - additive_build
    - support_removal
    - precision_machining
    - drilling
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: wire_arc_additive_manufacturing_v0
      fit: partial
      reason: "Provides a metal additive anchor for near-net stainless bracket geometry, though smaller features and interfaces need finish machining."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for mounting faces, hole patterns, perpendicularity, and linear-guide alignment interfaces."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers non-critical cleanup and stock-removal operations after near-net fabrication."
    - process_id: welding_structural_v0
      fit: poor_fit
      reason: "A weldment is a plausible source-route alternative, but it adds fixturing and distortion risks for the selected closure path."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers baseline dimensional checks before stronger metrology is selected."
  abstraction_decision: substitute_process_family
  rationale: "The source route is uncertain across monolithic machining and weldment fabrication; a shared metal additive route with finish machining is a better closure abstraction for the ribbed custom stainless geometry."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: upper connector support for linear guide assembly
  material: stainless_steel_austenitic
  scale_or_capacity:
    mass_kg: 1.4
    bom_quantity: 1
    row_total_mass_kg: 1.4
    scale_class: medium
  geometry_form: tall_ribbed_connector_bracket_with_mounting_faces
merge_pool:
  eligible: true
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - mounting_face_flatness
    - perpendicularity
    - hole_position
    - guide_alignment
    - stiffness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_metal_additive_with_finish_machining
  import_risk_factors:
    - "Linear-guide alignment can require precision machining and metrology beyond ordinary bracket fabrication."
    - "Austenitic stainless near-net fabrication may need distortion control and finish machining."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; compare with other linear-guide supports before choosing a shared closure item."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other guide support and carriage connection rows before assigning a closure item ID."
assumptions:
  - "The part is a custom connector body rather than a purchased guide module."
  - "Near-net additive fabrication plus finish machining can represent the lunar closure route for this geometry."
  - "Guide rail and bearing components remain separate closure items."
unresolved:
  - "Exact stainless grade, surface finish, and passivation state are not specified."
  - "The mating fastener pattern, load case, and alignment tolerance need review with adjacent guide hardware."
```
