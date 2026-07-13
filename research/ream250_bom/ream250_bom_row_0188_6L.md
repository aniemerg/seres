---
row_identity:
  item: "6L"
  cad_file: "6L_floating_bearing_mount"
  source_row_number: 188
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small floating bearing mount for the reAM250 axis/subassembly around BOM group 6; it provides a local bearing pocket/support feature while allowing the opposite side of the bearing arrangement to act as the non-fixed support."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6L_floating_bearing_mount.step; research/ream250_bom/ream250_bom_row_0188_6L__views_2x2.png"
    cited_fact_or_basis: "BOM row 188 and manifest row 188 identify item 6L as 6L_floating_bearing_mount, quantity 1, with matched part STEP gold_export/parts/6L_floating_bearing_mount.step. FreeCAD measured one solid with bounding box 52.00 x 24.00 x 8.00 mm. The rendered contact sheet shows a compact rectangular mount/plate with a large circular through feature or pocket and relieved/chamfered ends."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD row name's 'floating bearing mount' is interpreted in the conventional mechanical sense: this mount supports a bearing location that does not define the fully fixed axial reference, paired near row 187's fixed bearing mount."
  uncertainty_notes:
    - "The row-level CAD does not include the mating bearing, shaft, fasteners, or surrounding axis hardware, so the exact load direction and float mechanism are inferred from the row name and adjacent BOM context."
mass:
  value_kg: 0.0192
  basis: "Per unit for one physical mount; BOM quantity is 1, so row total is also about 0.0192 kg. FreeCAD volume is 7126.908 mm^3 = 7.126908e-6 m^3. Assembly STEP material metadata reports Aluminum 6061 with density 2700 kg/m^3, matching the local aluminum density constant in kb/materials/properties.yaml. Computed mass is 7.126908e-6 m^3 x 2700 kg/m^3 = 0.01924 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6L_floating_bearing_mount.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 7126.908 mm^3, area 3797.535 mm^2, and bounding box 52.00 x 24.00 x 8.00 mm. Local assembly material extraction matched 6L_floating_bearing_mount to material Aluminum 6061 with density 2700 kg/m^3. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3."
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
    cited_fact_or_basis: "Local STEP material extraction for product 6L_floating_bearing_mount reports material Aluminum 6061 and density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata identifies the alloy family/grade but does not state temper, surface treatment, or whether any local insert or bushing is installed separately from this mount row."
how_to_make:
  summary: "Make as a small CNC-machined 6061 aluminum bearing-mount plate/block"
  manufacturing_steps:
    - "Start from 6061 aluminum plate or bar stock slightly larger than the 52 x 24 x 8 mm finished envelope."
    - "CNC mill the outside profile, relieved/chamfered end features, and flat bearing-mount surfaces."
    - "Drill and circular-interpolate or bore the large bearing pocket/through-hole, then add any smaller mounting holes or fastener features required by the assembly drawing."
    - "Deburr, optionally anodize or conversion-coat, clean, and inspect bore position/diameter and flatness before installing with the mating bearing hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6L_floating_bearing_mount.step; research/ream250_bom/ream250_bom_row_0188_6L__views_2x2.png; https://www.coxmanufacturing.com/aluminum-6061"
    cited_fact_or_basis: "CAD evidence shows a one-piece 52.00 x 24.00 x 8.00 mm Aluminum 6061 mount with a large circular bearing feature and chamfered/relieved geometry. Cox Manufacturing describes Aluminum 6061 as commonly machined by CNC milling/turning/Swiss machining and notes good corrosion resistance, clean surface finish, welding/forming suitability, and anodizing suitability. targeted_web_search: query tried 'floating bearing mount aluminum 6061 machined plate bearing mount manufacturing'; results found general 6061 machining and bearing-housing examples but no row-specific vendor drawing or manufacturing process for 6L_floating_bearing_mount."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible CAD geometry is a single aluminum machined part rather than a casting or multi-part external bearing block"
    - "Low-volume KB planning favors CNC machining from stock over casting because the part is small, flat, and has a precision bearing feature."
  uncertainty_notes:
    - "Exact tolerances, bearing fit class, surface finish, hole callouts, and heat-treatment/temper requirements are not present in the row-level evidence."
kb_implications:
  - "item_granularity: simple_part - Model 6L as a reusable small machined Aluminum 6061 bearing-mount part; keep bearing, shaft, and fasteners as separate BOM rows or later generic hardware items."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0188_6L.md
source_research_sha256: "8fdafc7acb0b4aa350d3280b22325de92b3b9748cabb08807b49b84dc95a7efc"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the floating-bearing support function, CAD-derived mass, Aluminum 6061 evidence, CNC-machining route, and bearing-pocket geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one small machined aluminum mount body; bearing, shaft, fasteners, and neighboring fixed mount are separate BOM rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machined_aluminum_bearing_mount
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - drilling
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers stock-to-machined metal part conversion, but the bearing feature needs tighter bore and position control."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for bearing bore diameter, position, flatness, and mating-surface control."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers smaller mounting holes when recipe bindings expose them."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks before later staging decides whether stronger metrology is needed."
  abstraction_decision: keep_original_family
  rationale: "The original route is CNC machining from aluminum stock, and the functional bearing pocket makes subtractive machining the clearest closure handle."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: floating bearing support mount for shaft axis hardware
  material: aluminum_alloy_6061
  scale_or_capacity:
    mass_kg: 0.0192
    bom_quantity: 1
    row_total_mass_kg: 0.0192
    scale_class: small
  geometry_form: compact_rectangular_bearing_mount_with_precision_circular_bore
merge_pool:
  eligible: true
  functional_purpose_key: bearing_mount
  precision_guardrails:
    - bore_diameter
    - bore_position
    - bearing_fit
    - flatness
    - alignment_accuracy
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Bearing fit tolerance and alignment may require precision machining plus inspection."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; compare with fixed bearing mount and other small aluminum bearing supports."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before deciding whether this can share a generic small aluminum bearing mount closure item."
assumptions:
  - "The circular feature is a bearing pocket through feature that controls shaft support alignment."
  - "No separate bushing, insert, nor seal is part of this row."
  - "Optional anodizing is treated as finishing and not as identity-defining in this pass."
unresolved:
  - "Exact bearing fit class, bore diameter tolerance, flatness, and fastener hole callouts are not available."
  - "The relation to the adjacent fixed bearing mount should be checked during merge review."
```
