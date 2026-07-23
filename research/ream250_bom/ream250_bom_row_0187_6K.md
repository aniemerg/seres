---
row_identity:
  item: "6K"
  cad_file: "6K_fixed_bearing_mount"
  source_row_number: 187
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small fixed bearing mount for the reAM250 axis/subassembly around BOM group 6; it provides the local bearing pocket/support that acts as the fixed-side bearing support paired with the adjacent floating bearing mount."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6K_fixed_bearing_mount.step; research/ream250_bom/ream250_bom_row_0187_6K__views_2x2.png"
    cited_fact_or_basis: "BOM row 187 and manifest row 187 identify item 6K as 6K_fixed_bearing_mount, quantity 1, with matched part STEP gold_export/parts/6K_fixed_bearing_mount.step. FreeCAD measured one solid with bounding box 52.00 x 24.00 x 8.00 mm. The rendered contact sheet shows a compact rectangular mount/plate with a large circular bearing feature and relieved/chamfered ends."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD row name's 'fixed bearing mount' is interpreted in the conventional mechanical sense: this mount supports the bearing location that defines the fixed axial reference, paired near row 188's floating bearing mount."
  uncertainty_notes:
    - "The row-level CAD does not include the mating bearing, shaft, fasteners, or surrounding axis hardware, so the exact load path and retention details are inferred from the row name and adjacent BOM context."
mass:
  value_kg: 0.0194
  basis: "Per unit for one physical mount; BOM quantity is 1, so row total is also about 0.0194 kg. FreeCAD volume is 7183.457 mm^3 = 7.183457e-6 m^3. Assembly STEP material metadata reports Aluminum 6061 with density 2700 kg/m^3, matching the local aluminum density constant in kb/materials/properties.yaml. Computed mass is 7.183457e-6 m^3 x 2700 kg/m^3 = 0.01940 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6K_fixed_bearing_mount.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 7183.457 mm^3, area 3791.252 mm^2, and bounding box 52.00 x 24.00 x 8.00 mm. Local assembly material extraction matched 6K_fixed_bearing_mount to material Aluminum 6061, Welded with density 2700 kg/m^3. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the complete per-unit physical mount for this BOM row."
    - "The reAM250 STEP material density is interpreted as kg/m^3, consistent with the material extractor note and the local density table."
  uncertainty_notes:
    - "CAD volume may omit very small edge breaks, threaded details, or finish thickness, but those effects are negligible at this tens-of-grams scale."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6K_fixed_bearing_mount reports material 'Aluminum 6061, Welded' and density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata identifies the alloy family/grade but does not state temper, surface treatment, or whether the 'Welded' material label reflects stock/process history rather than a weld in this small part."
how_to_make:
  summary: "Make as a small CNC-machined 6061 aluminum bearing-mount plate/block"
  manufacturing_steps:
    - "Start from 6061 aluminum plate or bar stock slightly larger than the 52 x 24 x 8 mm finished envelope."
    - "CNC mill the outside profile, relieved/chamfered end features, and flat bearing-mount surfaces."
    - "Drill and circular-interpolate or bore the large bearing pocket/through-hole, then add any smaller mounting holes or fastener features required by the assembly drawing."
    - "Deburr, optionally anodize or conversion-coat, clean, and inspect bore position/diameter and fixed-side bearing reference surfaces before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6K_fixed_bearing_mount.step; research/ream250_bom/ream250_bom_row_0187_6K__views_2x2.png; https://mccormickind.com/aluminum-brake-shaft-bearing-blocks/"
    cited_fact_or_basis: "CAD evidence shows a one-piece 52.00 x 24.00 x 8.00 mm Aluminum 6061 mount with a large circular bearing feature and chamfered/relieved geometry. McCormick Industries describes comparable aluminum brake shaft bearing blocks as machined from 6061-T6 aluminum billet with precision-drilled mounting holes and a central bearing bore. targeted_web_search: query tried 'fixed bearing mount aluminum 6061 machined block bearing support'; results found general 6061 bearing-block machining examples but no row-specific vendor drawing or manufacturing process for 6K_fixed_bearing_mount."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible CAD geometry is a single aluminum machined part rather than a casting or multi-part external bearing block"
    - "Low-volume KB planning favors CNC machining from stock over casting because the part is small, flat, and has a precision bearing feature."
  uncertainty_notes:
    - "Exact tolerances, bearing fit class, surface finish, hole callouts, and heat-treatment/temper requirements are not present in the row-level evidence."
kb_implications:
  - "item_granularity: simple_part - Model 6K as a reusable small machined Aluminum 6061 fixed bearing-mount part; keep bearing, shaft, and fasteners as separate BOM rows or later generic hardware items."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0187_6K.md
source_research_sha256: 1ddf14df67f23d367e03b58d40df0ab3d99b7ce775090fa460728f71ac9dfd72
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the original function, mass basis, Aluminum 6061 material evidence, inferred CNC machining route, KB implications,
    and CAD preview showing a compact plate/block with a circular bearing feature.
decomposition:
  decision: simple_part
  rationale: The row is a single small aluminum bearing mount body; the bearing, shaft, fasteners, and neighboring floating
    mount remain separate rows and later generic hardware.
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machining_from_aluminum_stock
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
  - stock_preparation
  - cutting
  - precision_machining
  - deburring
  - surface_finishing
  - dimensional_inspection
  - thread_forming
  - grinding_lapping
  - joining
  - coating
  candidate_existing_processes:
  - process_id: machining_basic_v0
    fit: partial
    reason: Covers basic stock removal; row-specific precision features remain guardrails.
  - process_id: machining_precision_v0
    fit: supporting
    reason: Relevant when bore, sliding, concentricity, and finish control matter.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before staging selects the final recipe.
  - process_id: fastener_kit_small_fabrication_v0
    fit: supporting
    reason: Relevant when the row depends on thread geometry.
  - process_id: precision_grinding_basic_v0
    fit: supporting
    reason: Relevant when rolling, sliding, and raceway surfaces need precision finishing.
  - process_id: welding_basic_v0
    fit: supporting
    reason: Relevant when the row needs permanent joining.
  - process_id: surface_treatment_basic_v0
    fit: supporting
    reason: Relevant when the row needs protective surface treatment.
  abstraction_decision: keep_original_family
  rationale: The source route already belongs to the shared subtractive machining bucket. Accurate bearing pocket, reference
    faces, and hole positions are better handled by machining than by additive manufacturing.
  process_guardrails:
    tolerance: review bearing bore diameter, bore position, and mounting-hole locations
    surface_finish: bearing pocket and reference faces need machined finish
    sealing_quality: not_applicable
    alignment_accuracy: important for fixed-side bearing support and pairing with the adjacent floating mount
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: fixed-side support that locates a bearing for an axis and subassembly
  material: aluminum_6061
  scale_or_capacity:
    mass_kg: 0.0194
    bom_quantity: 1
    row_total_mass_kg: 0.0194
    scale_class: small
  geometry_form: compact_bearing_mount_plate_with_bored_pocket
merge_pool:
  eligible: true
  functional_purpose_key: bearing_support
  precision_guardrails:
  - bearing_bore_fit
  - bore_position_accuracy
  - fixed_reference_face_flatness
  - mounting_hole_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_subtractive_machining
  import_risk_factors:
  - bearing fit and alignment tolerances are unresolved
  - Aluminum 6061 temper and surface treatment requirements are not specified
  post_merge_decision_notes: Final import/local manufacture decision is deferred until after merge review compares this with
    other bearing mounts and small aluminum support parts.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review before assigning an item ID; likely candidate for a generic small aluminum bearing support
    if fixed/floating roles and precision guardrails can be represented by notes and recipe variants.
assumptions:
- The STEP-derived mass of 0.0194 kg is accepted as both per-unit and row-total mass because BOM quantity is 1.
- Aluminum 6061 from STEP material metadata is preserved as aluminum_6061 for merge review.
- General machining can provide the required bearing pocket and fixed reference surfaces if tolerances are later specified.
unresolved:
- Exact bearing size, fit class, bore tolerance, and mounting-hole callouts were not present in row evidence.
- Whether fixed and floating bearing mounts should merge into one bearing-support closure item and stay separate is deferred
  to merge review.
```
