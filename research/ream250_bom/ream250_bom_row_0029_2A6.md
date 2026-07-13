---
row_identity:
  item: "2A6"
  cad_file: "2A6_left_plate"
  source_row_number: 29
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Left-hand structural plate for the reAM250 Z-axis/linear-motion assembly, providing a triangular side support with stiffening ribs and a bolted mounting edge."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/20_z_axis.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; research/ream250_bom/ream250_bom_row_0029_2A6__views_2x2.png"
    cited_fact_or_basis: "BOM row 29 identifies item 2A6 as quantity 1 of 2A6_left_plate. The manifest maps it to a matched part STEP. The full assembly places 2A6_left_plate in 20_z_axis.step. FreeCAD measured a 240.00 x 400.00 x 23.00 mm envelope, and the rendered preview shows a triangular ribbed plate with a row of mounting holes along one edge."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name left_plate and its location in 20_z_axis.step identify the side and subsystem role."
  uncertainty_notes:
    - "No drawing callouts or assembly mates were available, so the exact connected components are inferred from CAD shape and subsystem placement."
mass:
  value_kg: 3.50
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 1,295,591.522 mm^3, equal to 0.001295592 m^3. Using local aluminum density 2700 kg/m^3 gives 3.498 kg, rounded to 3.50 kg. If the part were generic steel at 7850 kg/m^3, the same CAD volume would imply about 10.17 kg; aluminum is selected as the best estimate for a ribbed structural motion-axis plate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; kb/materials/properties.yaml; web_search"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 1,295,591.522 mm^3 and bounding box 240.00 x 400.00 x 23.00 mm. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3 and steel density as 7850 kg/m^3. targeted_web_search: searched \"2A6_left_plate reAM250 material\", \"2A6 2A6_left_plate\", \"reAM250 left_plate 2A6\", and \"reAM250 2A6_left_plate manufacturing\"; results duplicated BOM row identity but did not provide row-specific mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The plate is treated as aluminum alloy because its large ribbed motion-axis support geometry is consistent with a lightweight machined structural plate."
    - "The CAD STEP volume is treated as the finished solid volume, including pockets, ribs, holes, and edge features."
  uncertainty_notes:
    - "Assembly STEP material extraction for 2A6_left_plate returned only Generic with density 1000.0, which is placeholder metadata under the task acceptance criteria."
    - "If the actual part is steel rather than aluminum, mass would be roughly 10.17 kg instead of 3.50 kg."
material:
  primary_material: "Aluminum alloy structural plate, exact grade unknown"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAM250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; web_search"
    cited_fact_or_basis: "BOM row 29 has blank manufacturer, description/product ID, material family, specific grade, and link URL fields. Local assembly STEP material extraction for product 2A6_left_plate returned material Generic with density 1000.0. The CAD/contact sheet shows a single ribbed structural plate rather than a catalog module. targeted_web_search: searched \"2A6_left_plate reAM250 material\", \"2A6 2A6_left_plate\", \"reAM250 left_plate 2A6\", and \"reAM250 2A6_left_plate manufacturing\"; no row-specific material or grade source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Use aluminum alloy as the planning material family for later KB modeling because the plate is a large custom motion-axis support where low mass is useful."
  uncertainty_notes:
    - "The actual alloy and temper are not resolved; downstream KB work should keep this as an estimated structural aluminum part unless a drawing or CAD material file is found."
how_to_make:
  summary: "Fabricate as a custom CNC-machined aluminum side plate from thick plate stock, with profile cutting, pocket/rib machining, drilled mounting holes, deburring, and optional surface finish."
  manufacturing_steps:
    - "Start from aluminum plate stock thick enough for the 23 mm finished envelope."
    - "CNC mill or waterjet/rough-cut the triangular outside profile."
    - "CNC mill the ribbed pockets and edge/flange features visible in the STEP preview."
    - "Drill and countersink or spotface the mounting-hole row as required by the mating Z-axis hardware."
    - "Deburr, inspect hole locations and flatness, then anodize or otherwise finish if the machine environment requires corrosion/wear protection."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A6_left_plate.step; research/ream250_bom/ream250_bom_row_0029_2A6__views_2x2.png; web_search"
    cited_fact_or_basis: "The row-specific STEP/contact sheet shows one custom plate-like solid with a triangular outline, milled-looking ribs/pockets, edge features, and mounting holes. targeted_web_search: searched \"2A6_left_plate reAM250 material\", \"2A6 2A6_left_plate\", \"reAM250 left_plate 2A6\", and \"reAM250 2A6_left_plate manufacturing\" no row-specific manufacturing drawing, vendor page, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The ribbed geometry is treated as machined or plate-fabricated geometry, not a cast part, because the CAD shows planar pockets and regular hole features."
  uncertainty_notes:
    - "A production drawing could specify casting, welded fabrication, surface treatment, or tighter tolerances not visible in the STEP preview."
kb_implications:
  - "item_granularity: simple_part - Model 2A6 as one custom machined structural plate, paired conceptually with 2A7_right_plate but not as a purchased module."
---

# reAM250 BOM Row 29 - 2A6

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0029_2A6.md
source_research_sha256: "12750fd4314f43b8e7e17dcc23ae634a25328a9e5551358bfd8b4dc553ba4523"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the row function, CAD-derived mass basis, inferred aluminum material, CNC plate manufacturing route, KB implications, and preview evidence showing a triangular ribbed support plate with mounting holes."
decomposition:
  decision: simple_part
  rationale: "The evidence describes one monolithic structural side plate for the Z-axis assembly; no internal module decomposition is needed before merge review."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machined_aluminum_plate
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers generic stock removal for a machined metal part, but does not capture the ribbed pocket geometry and motion-axis alignment guardrails."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for flatness, hole location, and mating-edge tolerances in the Z-axis support structure."
    - process_id: sheet_metal_cutting_v0
      fit: supporting
      reason: "Useful for rough blank/profile preparation from plate stock before machining."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Matches the mounting-hole pattern step, with final tolerances deferred to precision machining and inspection."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks of flatness, hole positions, and interface edges before assembly."
  abstraction_decision: keep_original_family
  rationale: "The original inferred route is CNC machining from thick aluminum plate, and the ribbed pockets plus motion-axis mounting function make general subtractive machining the main closure handle."
  process_guardrails:
    tolerance: review
    surface_finish: standard
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: structural side support for Z-axis linear motion assembly
  material: aluminum_alloy
  scale_or_capacity:
    mass_kg: 3.5
    bom_quantity: 1
    row_total_mass_kg: 3.5
    scale_class: medium
  geometry_form: triangular_ribbed_machined_plate_with_mounting_hole_edge
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - flatness
    - hole_position_accuracy
    - linear_axis_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Actual material could be steel, which would change mass and machining requirements."
    - "Motion-axis alignment may require tighter inspection than ordinary structural plates."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this plate with other Z-axis support and frame-member rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with mirrored and similar structural support plates before assigning a final closure item."
assumptions:
  - "Aluminum alloy is retained as the planning material because the row research selected it from geometry and lightweight motion-axis context."
  - "The CAD volume is accepted as finished-part volume including ribs, pockets, holes, and edge features."
unresolved:
  - "Exact alloy, temper, surface treatment, and production drawing tolerances remain unknown."
  - "Whether a later lunar design can simplify ribbed pockets without losing Z-axis stiffness needs merge-stage review."
```
