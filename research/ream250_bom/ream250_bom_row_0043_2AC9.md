---
row_identity:
  item: "2AC9"
  cad_file: "2AC9_part_9"
  source_row_number: 43
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One lower-axis bearing support block or bracket for the reAM250 axis bearing bottom group, with a central bearing/shaft bore and side mounting features."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC9_part_9.step; research/ream250_bom/ream250_bom_row_0043_2AC9__views_2x2.png"
    cited_fact_or_basis: "BOM row 43 identifies item 2AC9, quantity 1, CAD file 2AC9_part_9, description 'axis bearing bottom'. The manifest maps the row to gold_export/parts/2AC9_part_9.step with matched_existing part status. FreeCAD measured one solid with bounding box 86.00 x 24.00 x 58.00 mm, and the contact sheet shows a blocky bracket with a large central circular bore plus smaller side mounting holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the physical lower bearing support part for this row."
  uncertainty_notes:
    - "The BOM names the bottom-axis bearing group but does not identify the exact mating shaft, bearing insert, or fastener interfaces used with this support block."
mass:
  value_kg: 0.49
  basis: "Per-unit planning estimate for quantity 1. FreeCAD volume is 62373.201 mm^3, equal to 6.2373201e-5 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.4896 kg, rounded to 0.49 kg. If the same CAD volume were aluminum at 2700 kg/m^3, mass would be about 0.168 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC9_part_9.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 62373.201 mm^3, area 15145.115 mm^2, and bounding box 86.00 x 24.00 x 58.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried '\"2AC9\" \"axis bearing bottom\"', '\"reAM250\" \"axis bearing bottom\"', and '\"2AC9_part_9\"'; results duplicated the BOM row identity but did not provide row-specific material, mass, drawing, or catalog data."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-like density is used as the conservative single-value planning estimate because the part is a bearing support block with load-bearing geometry and no row-specific material."
    - "The CAD solid volume is treated as the physical solid volume of one item."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so the estimate depends on the steel-density assumption; an aluminum part would be much lighter."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0043_2AC9__views_2x2.png"
    cited_fact_or_basis: "BOM row 43 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2AC9_part_9 returned material 'Generic' with density 1000.0, which is placeholder metadata. The contact sheet shows a rigid machined support-block form. targeted_web_search: tried '\"2AC9\" \"axis bearing bottom\"', '\"reAM250\" \"axis bearing bottom\"', and '\"2AC9_part_9\"'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The load-bearing bracket/block geometry and axis-bearing context indicate a metal part rather than a polymer, seal, or consumable."
  uncertainty_notes:
    - "The evidence supports only a broad metal/alloy family; downstream KB modeling should not assign a specific grade without a drawing, material callout, or related assembly note."
how_to_make:
  summary: "Fabricate as a one-piece machined bearing support bracket from metal billet or plate stock"
  manufacturing_steps:
    - "Cut a metal billet or thick plate blank large enough for the 86 x 24 x 58 mm envelope."
    - "CNC mill the external block, feet, and angled relief faces."
    - "Drill, bore, or ream the central bearing/shaft opening and the smaller side mounting holes."
    - "Deburr and inspect hole location, bore diameter, flatness, and mounting-face alignment."
    - "Apply any required corrosion protection or cleaning compatible with the axis bearing assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC9_part_9.step; research/ream250_bom/ream250_bom_row_0043_2AC9__views_2x2.png"
    cited_fact_or_basis: "The CAD preview shows a one-piece block/bracket with a central bore, mounting ears/feet, smaller side holes, and machined-looking planar faces; FreeCAD measured one solid. targeted_web_search: tried '\"2AC9\" \"axis bearing bottom\"', '\"reAM250\" \"axis bearing bottom\"', and '\"2AC9_part_9\"'; no source stated a row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining from metal stock is the most plausible low-volume route for the observed one-piece bearing support geometry."
  uncertainty_notes:
    - "The CAD preview is sufficient for route triage but not for tolerance, fit, material grade, heat treatment, or surface-finish requirements."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable custom machined metal bearing support/bracket, likely shared conceptually with adjacent 2AC bottom-axis-bearing rows, rather than as a purchased module or raw stock."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0043_2AC9.md
source_research_sha256: "d51e81f6e2dc513b17184b2e790ef28d2f9fe87664524cdf54e4dc239ba734a7"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the axis-bearing function, steel-density mass assumption, unknown metal material evidence, machined-block route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is a one-piece bearing support block with a central bore and mounting features. It is not a module and should remain a simple machined part for merge review."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machined_bearing_support_block
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
      reason: "Covers general stock removal for the block, feet, and planar faces."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if the bearing bore, mounting faces, and axis alignment need tighter control."
    - process_id: machining_process_boring_v0
      fit: supporting
      reason: "Anchors the central bearing and shaft bore operation."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers smaller side mounting holes."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers cleanup of machined edges and bore edges."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers bore diameter, hole location, flatness, and mounting-face checks."
  abstraction_decision: keep_original_family
  rationale: "The inferred source route is machining from metal stock, matching the selected general subtractive machining bucket. Precision boring and inspection are retained as support tags."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: support and locate a lower-axis bearing around a shaft bore
  material: unknown_metal
  scale_or_capacity:
    mass_kg: 0.49
    bom_quantity: 1
    row_total_mass_kg: 0.49
    scale_class: small
  geometry_form: compact_machined_bearing_block_with_central_bore_and_mounting_feet
merge_pool:
  eligible: true
  functional_purpose_key: bearing_support
  precision_guardrails:
    - bore_diameter
    - bore_alignment
    - mounting_face_flatness
    - hole_pattern
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material is unresolved and the steel-density mass is a conservative planning assumption."
    - "Bearing bore and shaft alignment may require precision machining beyond a rough block recipe."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this row with adjacent lower-axis bearing support parts."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely a reusable bearing support block family with material-specific variants if evidence diverges."
assumptions:
  - "Steel-like density is retained for conservative scale grouping because the material is unresolved."
  - "The CAD solid is treated as one physical support block."
  - "A generic machined bearing-support closure item may cover this row if bore and mounting interfaces remain guardrails."
unresolved:
  - "Exact alloy, bearing insert relationship, bore tolerance, heat treatment, and surface finish are not available from the row evidence."
```
