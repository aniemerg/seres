---
row_identity:
  item: "2A8"
  cad_file: "2A8_left_distance_piece"
  source_row_number: 31
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom left-side distance piece or spacer block for the reAM250 2A axis/structural subassembly; CAD shows a long rectangular machined spacer with lightening pockets/webs and small mounting holes, likely setting separation and alignment between neighboring plates, supports, rails, or bearing structures."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A8_left_distance_piece.step; research/ream250_bom/ream250_bom_row_0031_2A8__views_2x2.png"
    cited_fact_or_basis: "BOM row 31 states item 2A8, quantity 1, CAD file 2A8_left_distance_piece. The manifest maps the row to gold_export/parts/2A8_left_distance_piece.step as a matched part export. FreeCAD measured one solid with bounding box 40.00 x 140.00 x 30.00 mm. The rendered contact sheet shows a long block-like distance piece with recessed/lightened faces and small holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name left_distance_piece and neighboring BOM rows for left/right plates, right distance piece, support plates, guide rails, and axis-bearing components are interpreted as a 2A-axis spacer/alignment context."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the row as a distance piece but does not identify the exact mating faces, preload role, tolerance class, or whether it primarily spaces fixed frame plates or moving-axis parts."
mass:
  value_kg: 0.36
  basis: "FreeCAD volume 133243.550 mm^3 equals 0.000133244 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.360 kg per unit. Quantity is 1, so row total is also about 0.360 kg. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 1.046 kg; stainless steel at 8000 kg/m^3 would be about 1.066 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A8_left_distance_piece.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 133243.550 mm^3, area 27014.428 mm^2, and bounding box 40.00 x 140.00 x 30.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"2A8_left_distance_piece\", \"reAM250 left_distance_piece\", and \"reAM250 2A8 distance\"; found duplicate BOM listings but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured part."
    - "Aluminum is used as the nominal scenario because the part is a small custom machined spacer in a precision motion/plate stack and no heat, wear, vacuum sealing, or high-strength steel requirement is stated."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.36 kg as an aluminum-scenario estimate, with steel or stainless construction near 1.05-1.07 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A8_left_distance_piece.step; research/ream250_bom/ream250_bom_row_0031_2A8__views_2x2.png"
    cited_fact_or_basis: "BOM row 31 has blank manufacturer, product, link, material-family, and grade fields. The assembly STEP material extractor matched 2A8_left_distance_piece but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a rigid spacer/block with machined pockets and holes. targeted_web_search: searched \"2A8_left_distance_piece\", \"reAM250 left_distance_piece\", and \"reAM250 2A8 distance\"; found duplicate BOM listings but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the spacer role, 30 mm thickness, pocketed solid geometry, and neighboring linear-guide/axis-support BOM context."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for a custom machined spacer, while steel or stainless steel remain possible if stiffness, wear resistance, or vacuum/thermal requirements dominate."
how_to_make:
  summary: "Fabricate as a custom machined distance piece from structural metal stock, most likely by CNC milling a rectangular bar or plate blank to the CAD outline, pockets, holes, and mating faces."
  manufacturing_steps:
    - "Select structural metal bar or plate stock in the resolved alloy, nominally at least 40 x 140 x 30 mm before finish machining."
    - "Saw or rough-cut the blank to length with machining allowance."
    - "CNC mill the outside faces to final 40.00 x 140.00 x 30.00 mm envelope and machine recessed pockets/lightening geometry visible in the CAD."
    - "Drill, counterbore, countersink, or tap the small mounting holes required by the mating left/right plate or support interfaces."
    - "Finish-machine datum faces for parallelism and spacing accuracy, then deburr, clean, and inspect critical dimensions and hole locations."
    - "Apply anodizing, passivation, blackening, or other surface treatment only if later drawing evidence identifies a required finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A8_left_distance_piece.step; research/ream250_bom/ream250_bom_row_0031_2A8__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 40.00 x 140.00 x 30.00 mm solid with a rectangular distance-piece form, recessed/lightened faces, and small holes. targeted_web_search: searched \"2A8_left_distance_piece\", \"reAM250 left_distance_piece\", and \"reAM250 2A8 distance\" no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part because the BOM row has no manufacturer, product ID, or link URL and the CAD name is assembly-specific"
    - "Subtractive machining from bar or plate stock is assumed from the block/spacer geometry, pockets, and expected need for accurate spacing/alignment faces."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, heat treatment, coating, or whether the pockets are for lightening, clearance, stiffness tuning, or access."
kb_implications:
  - "item_granularity: simple_part - custom structural distance spacer likely modeled as one machined metal part, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 31.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0031_2A8.md
source_research_sha256: "a5068bcadd1dd6e213ac89826d5fc8b231c7fd951f154f8c9c7811623af38ecc"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the row function, mass basis, unresolved structural metal evidence, machining route, KB implications, and CAD preview showing a pocketed rectangular distance piece with small mounting holes."
decomposition:
  decision: simple_part
  rationale: "The row is one custom distance piece with no separable internal parts; pockets and holes are geometric features of a single machined body."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_milled_bar_plate_stock
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - drilling
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers milling a structural metal blank into the spacer body, but datum-face accuracy and pocket geometry may need tighter controls."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for parallel faces, spacing accuracy, hole position, and alignment interfaces."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers the small mounting holes visible in the CAD preview."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers verification of envelope dimensions, datum faces, hole pattern, and spacing accuracy."
  abstraction_decision: keep_original_family
  rationale: "The original route is a subtractive machining route from structural metal stock. The pocketed block geometry and datum-face role make general subtractive machining a better primary bucket than simple sheet and plate cutting."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "spacing and alignment between machine axis support interfaces"
  material: unknown_structural_metal_alloy
  scale_or_capacity:
    mass_kg: 0.36
    bom_quantity: 1
    row_total_mass_kg: 0.36
    scale_class: small
  geometry_form: pocketed_rectangular_distance_piece_with_mounting_holes
merge_pool:
  eligible: true
  functional_purpose_key: spacing_alignment
  precision_guardrails:
    - parallelism
    - hole_position
    - datum_face_accuracy
    - flatness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material is unresolved; aluminum, steel, and stainless choices change mass and upstream closure."
    - "Unknown parallelism, datum-face, and hole-position tolerances could require precision machining."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares spacer and distance-piece rows with similar function and scale."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; candidate for a generic machined spacing-alignment block if material and precision assumptions converge."
assumptions:
  - "The aluminum-scenario mass from the row research is retained while material identity remains unresolved."
  - "Lightening pockets are treated as closure-insignificant geometry unless later evidence shows a stiffness, clearance, vibration, and access requirement."
unresolved:
  - "Exact alloy, coating, mating faces, preload role, tolerance class, surface finish, and pocket purpose are not specified by the row evidence."
```
