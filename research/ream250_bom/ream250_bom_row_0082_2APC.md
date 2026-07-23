---
row_identity:
  item: "2APC"
  cad_file: "2APC_spring_block_left"
  source_row_number: 82
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Left-side spring block for the reAM250 build-platform/heating-plate area; model as a long narrow mechanical support or preload block paired with the front, right, and back spring blocks."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APC_spring_block_left.step; research/ream250_bom/ream250_bom_row_0082_2APC__views_2x2.png"
    cited_fact_or_basis: "BOM row 82 lists item 2APC, quantity 1, CAD file '2APC_spring_block_left'. Nearby BOM rows 79-81 list matching front, right, and back spring blocks. The manifest maps row 82 to a matched_existing part STEP. FreeCAD measured one solid with a bounding box about 251.00 x 22.00 x 15.00 mm; the rendered preview shows a long narrow block with small end features and a tapered or relieved face."
    evidence_basis: "bom_provided"
  assumptions:
    - "The four named spring blocks form a set around the adjacent spring plate, assembly plate, heating plate, and build platform rows."
    - "The visible long block geometry is interpreted as a mechanical support or preload/contact block rather than an electronic, sensor, or purchased module."
  uncertainty_notes:
    - "The CAD and BOM naming identify the part role only broadly; they do not show the mating spring interface or exact preload function."
mass:
  value_kg: 0.40
  basis: "FreeCAD STEP volume 50480.728 mm^3 converted to 5.048073e-5 m^3 and multiplied by a steel-like density of 7850 kg/m^3 from kb/materials/properties.yaml, giving about 0.396 kg. An aluminum-density scenario would be about 0.136 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APC_spring_block_left.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 50480.728 mm^3 volume, 19464.674 mm^2 area, and about 251.00 x 22.00 x 15.00 mm bounding box. The local density table lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: searched '2APC_spring_block_left material', '2APC spring_block_left reAM250', 'reAM250 spring_block_left', and 'spring block reAM250 material'; found duplicate BOM/platform pages but no row-specific vendor, material, or drawing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-like density is used as the conservative default for a narrow machined block in a heated, mechanically loaded build-platform region."
    - "The exported single-solid STEP volume is used as the physical volume for this row."
  uncertainty_notes:
    - "The material is not resolved beyond a metal/alloy hypothesis, so mass could plausibly be closer to 0.14 kg if the block is aluminum rather than steel or stainless steel."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0082_2APC__views_2x2.png"
    cited_fact_or_basis: "BOM row 82 names the part '2APC_spring_block_left'. The assembly STEP material extractor matched the product only to placeholder material 'Generic' with density 1000.0. The preview shows a long block-like solid. targeted_web_search: searched '2APC_spring_block_left material', '2APC spring_block_left reAM250', 'reAM250 spring_block_left', and 'spring block reAM250 material'; found duplicate BOM/platform pages but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal or alloy is inferred from the block geometry, spring-block naming, and location among build-platform/heating-plate mechanical rows."
  uncertainty_notes:
    - "No BOM field, STEP material metadata, vendor page, or row-specific web result identified the actual grade or whether the block is steel, stainless steel, or aluminum."
how_to_make:
  summary: "Machine the spring block from rectangular metal bar or plate stock, creating the long block profile, end reliefs/radii, and tapered or relieved face, then deburr and inspect fit against the spring-block assembly."
  manufacturing_steps:
    - "Select rectangular steel, stainless steel, or aluminum stock sized slightly above the 251 x 22 x 15 mm bounding envelope."
    - "Saw or mill the blank to length and square the reference faces."
    - "Mill the long tapered or relieved face and any shallow side/end details visible in the STEP geometry."
    - "Deburr edges and inspect length, width, thickness, flatness, and fit with the adjacent spring block or spring plate interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APC_spring_block_left.step; research/ream250_bom/ream250_bom_row_0082_2APC__views_2x2.png"
    cited_fact_or_basis: "The STEP file contains one solid with a long 251.00 x 22.00 x 15.00 mm bounding box; the rendered preview shows a simple elongated block with planar faces, small end features, and a tapered or relieved face. targeted_web_search: searched '2APC_spring_block_left material', '2APC spring_block_left reAM250', 'reAM250 spring_block_left', and 'spring block reAM250 material'; found no row-specific vendor or manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Subtractive machining from bar or plate stock is the representative low-volume route for this simple custom block."
    - "No casting, additive manufacturing, heat treatment, or calibrated external-module workflow is required unless later drawings specify a special material or spring property"
  uncertainty_notes:
    - "The exact tolerances, surface finish, and mating features are not specified by the BOM row or local STEP export."
kb_implications:
  - "item_granularity: simple_part - Treat as a custom machined metal block; consolidate with the other spring-block rows if later KB modeling can represent orientation variants with one reusable spring_block part."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0082_2APC.md
source_research_sha256: "edf05d1d0b99399ef495341d1a13e88105ae2c4d80e9b5d6b985dcf6b10f42da"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the spring-block function, steel-density mass assumption, unknown metal evidence, machined-stock route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is a one-piece elongated support/preload block. Orientation-specific naming should be handled during merge review rather than as a unique closure item."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_rectangular_bar_support_block
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: cutting_basic_v0
      fit: partial
      reason: "Covers cutting rectangular stock to the long block blank."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers milling the tapered face, end details, and reference faces."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if spring preload contact faces require tight flatness and alignment."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers cleanup of the long block edges and end features."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, width, thickness, flatness, and fit checks."
  abstraction_decision: substitute_process_family
  rationale: "The source route is simple machining from bar/plate stock, but the closure handle should be reusable structural/profile stock fabrication and cutting with secondary machining for the tapered detail."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: support and preload a build-platform spring interface
  material: unknown_metal
  scale_or_capacity:
    mass_kg: 0.40
    bom_quantity: 1
    row_total_mass_kg: 0.40
    scale_class: small
  geometry_form: long_narrow_rectangular_block_with_tapered_relief_face
merge_pool:
  eligible: true
  functional_purpose_key: mechanical_support
  precision_guardrails:
    - length
    - contact_face_flatness
    - preload_interface
    - orientation_variant
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Material is unresolved and the steel-density mass is a conservative planning assumption."
    - "Heated build-platform service may impose material, flatness, and thermal expansion requirements not captured by the row."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this row with front, right, and back spring-block rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely a reusable spring support block with orientation noted outside item identity."
assumptions:
  - "The steel-like mass estimate is retained for conservative scale grouping."
  - "The part is one machined metal block, not an assembled module."
  - "Left-side orientation is treated as a merge guardrail rather than a separate functional key."
unresolved:
  - "Exact alloy, preload contact requirements, flatness tolerance, surface finish, and thermal service limits are not resolved by row evidence."
```
