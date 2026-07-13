---
row_identity:
  item: "2AG"
  cad_file: "2AG_cover_plate"
  source_row_number: 58
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Protective or closure cover plate for the reAM250 z-axis inside assembly, located with the K+C glass-scale slide/track and adjacent connection mount hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0058_2AG__views_2x2.png"
    cited_fact_or_basis: "BOM row 58 names item 2AG as 2AG_cover_plate. The assembly STEP places 2AG_cover_plate inside product definition 2A0_z_axis_inside next to 2AE_glass_scale_slide, 2AF0_glass_scale_K+C_S5_500, 2AF1_track, and 2AH_connection_mount. The CAD preview shows a shallow cover-like plate with perimeter flanges/ribs and small mounting holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD name cover_plate is interpreted literally as a local cover rather than as a load-bearing structural frame member."
  uncertainty_notes:
    - "The exact protected component and installed orientation are inferred from nearby z-axis assembly entries rather than a drawing note."
mass:
  value_kg: 1.51
  basis: "Per-unit estimate for quantity 1. FreeCAD measured one solid with volume 558200.927 mm^3, area 92959.659 mm^2, and bounding box 210.00 x 200.00 x 15.00 mm. Mass uses the local aluminum density constant 2700 kg/m^3 from kb/materials/properties.yaml: 558200.927 mm^3 = 0.000558200927 m^3, so mass is about 1.507 kg, rounded to 1.51 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AG_cover_plate.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid, volume 558200.927 mm^3, bounding box 210.00 x 200.00 x 15.00 mm. Local STEP material extraction from 00_assembly.step returned only Generic material and density 1000.0, which does not resolve material. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. targeted_web_search: searched \"2AG_cover_plate\", \"2AG cover plate reAM250\", \"reAM250 2AG\", and \"2AG cover plate additive manufacturing machine\"; results exposed the public BOM row context but no row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The single STEP solid is treated as the physical volume of one BOM-row item."
    - "Aluminum is used as the planning-density assumption because the part is a broad machined cover in an axis/measuring-scale area where low mass is plausible."
  uncertainty_notes:
    - "Material is not sourced; if the same CAD volume were steel, mass would be about 4.38 kg instead of 1.51 kg."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AG_cover_plate.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 58 gives no material family or grade. The part STEP names the product 2AG_cover_plate and the preview shows a thin machined plate-like solid. Local assembly STEP material extraction returned only Generic material and density 1000.0, which is placeholder metadata. targeted_web_search: searched \"2AG_cover_plate material\", \"2AG cover plate reAM250 material\", \"reAM250 2AG cover plate\", and \"2AG_cover_plate weight\"; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal alloy is assumed because the CAD is a rigid, ribbed, drilled machine cover plate inside a motion-axis assembly."
  uncertainty_notes:
    - "No source resolves whether the alloy is aluminum, steel, stainless steel, or another metal."
how_to_make:
  summary: "Machine or fabricate as a custom cover plate from metal plate stock, then drill/countersink mounting holes, deburr edges, and finish as needed for the z-axis assembly."
  manufacturing_steps:
    - "Cut rectangular metal stock slightly larger than the 210 x 200 mm envelope."
    - "CNC mill the shallow ribs, recessed fields, perimeter edges, and local reliefs visible in the CAD."
    - "Drill the small mounting holes shown in the top view; add countersinks or spotfaces only if required by the mating fasteners."
    - "Deburr, clean, and apply corrosion-control finish compatible with the selected alloy."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0058_2AG__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AG_cover_plate.step"
    cited_fact_or_basis: "The CAD preview and STEP geometry show a shallow 210 x 200 x 15 mm cover-like solid with machined-looking ribs/flanges and multiple mounting holes. targeted_web_search: searched \"2AG_cover_plate manufacturing\", \"2AG cover plate reAM250 drawing\", and \"reAM250 2AG cover plate material\" no row-specific manufacturing note or drawing was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "CNC machining from plate stock is selected as the plausible route for a low-quantity custom machine cover with reliefs and holes."
  uncertainty_notes:
    - "The source CAD does not state tolerances, surface finish, heat treatment, or final coating requirements."
kb_implications:
  - "item_granularity: simple_part - Model 2AG as one custom machined cover plate for the z-axis/glass-scale area, not as a purchased module or multi-part assembly."
---

# reAM250 BOM Row 58 - 2AG

Result for the leased reAM250 BOM research row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0058_2AG.md
source_research_sha256: "da49c09a980288d36afd82ebe2d59931a5d797ea0c78e3c080bea0b879ef71e0"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed function, mass basis, BOM quantity, material uncertainty, manufacturing route, KB implications, and CAD preview evidence before conversion."
decomposition:
  decision: simple_part
  rationale: "The row describes one rigid cover plate with machined reliefs and mounting holes, not a vendor module and not a multi-part assembly."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machining_from_plate_stock
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers the primary plate-stock cutting route for a cover plate."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers shallow ribs, reliefs, and other local machined features after the plate blank is cut."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if the cover establishes alignment and clearance near the z-axis glass scale, though no tight tolerance is sourced."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers the visible mounting-hole operation after plate machining."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers deburring and edge cleanup expected for a machined plate installed in a motion-axis assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and visual checks before assembly around the z-axis/glass-scale hardware."
  abstraction_decision: add_post_processing
  rationale: "The row is a plate-like cover, so the closure handle should be sheet/plate cutting and drilling. CNC machining remains a supporting post-process for shallow ribs, reliefs, hole features, clearance, finishing, and inspection."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: protective closure cover for z-axis and glass-scale area
  material: unknown_metal_alloy
  scale_or_capacity:
    mass_kg: 1.51
    bom_quantity: 1
    row_total_mass_kg: 1.51
    scale_class: small
  geometry_form: shallow_machined_cover_plate_with_mounting_holes
merge_pool:
  eligible: true
  functional_purpose_key: enclosure_barrier
  precision_guardrails:
    - hole_pattern_alignment
    - clearance_to_motion_axis_components
    - material_substitution_review
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material family is unresolved; aluminum planning mass may be wrong if the original part is steel, stainless, another metal family."
    - "Potential alignment and clearance requirements near the z-axis glass-scale area need review before merging with generic covers."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review; likely local if a generic metal cover plate can satisfy mounting and clearance guardrails."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review against other cover plates, enclosure barriers, and small mounting plates before assigning a closure item ID."
assumptions:
  - "Treat the BOM quantity as 1 and row total mass as 1.51 kg."
  - "Treat the item as a rigid metal cover; aluminum is only a mass-planning assumption, not sourced material identity."
  - "No sourced evidence requires treating the part as a sealed vacuum barrier, precision metrology component, unique module."
unresolved:
  - "Actual alloy and finish are not sourced."
  - "Exact mating interfaces, flatness requirements, and hole tolerances are not sourced."
```
