---
row_identity:
  item: 1B3
  cad_file: 1B3_flange_schlieren_imaging
  source_row_number: 11
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Thin rectangular flange or mounting frame for the schlieren imaging door/window stack, providing a bolted interface around the optical aperture.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B3_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0011_1B3__views_2x2.png"
    cited_fact_or_basis: "BOM row 11 identifies item 1B3 as quantity 1 CAD file 1B3_flange_schlieren_imaging. FreeCAD measured one solid with bounding box 80.00 x 10.00 x 160.00 mm; the rendered preview shows a thin rectangular frame/plate with corner holes and diagonal features."
    evidence_basis: bom_provided
  assumptions:
    - "The filename's 'flange_schlieren_imaging' term is interpreted together with the adjacent BOM rows for glass, seal, frame, and SM2A53 optical adapter as part of the schlieren imaging door/window assembly."
  uncertainty_notes:
    - "The exact mating face and optical-side orientation are not labeled in the per-part STEP; function is inferred from row name, neighboring BOM rows, and visible flange geometry."
mass:
  value_kg: 0.331
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 122504.602 mm^3, equal to 0.000122504602 m^3. Using the local aluminum density constant 2700 kg/m^3 gives 0.3308 kg, rounded to 0.331 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B3_flange_schlieren_imaging.step; kb/materials/properties.yaml; web_search"
    cited_fact_or_basis: "FreeCAD measured volume 122504.602 mm^3 for the row-specific STEP. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. targeted_web_search: queries tried: \"1B3_flange_schlieren_imaging\", \"reAM250 1B3 flange schlieren\", \"reAM250 schlieren imaging flange material\", and \"1B3_flange_schlieren_imaging material\"; results found reAM250 BOM mirrors/pages but no row-specific mass or material."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Use aluminum as the planning-density material because this is a custom, thin machined optical mounting flange and the BOM/STEP package provides no real material metadata."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only Generic with density 1000.0, which is placeholder metadata and not a usable material basis."
    - "If the flange is steel instead of aluminum, the same CAD volume at 7850 kg/m^3 would be about 0.962 kg, so the mass could be roughly 3x higher."
material:
  primary_material: unknown structural metal/alloy
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web_search"
    cited_fact_or_basis: "BOM row 11 has blank Material family and Specific material / grade fields. Local STEP material extraction for product 1B3_flange_schlieren_imaging returned material Generic with density 1000.0. targeted_web_search: queries tried: \"1B3_flange_schlieren_imaging material\", \"reAM250 1B3 flange schlieren material\", and \"reAM250 open-source research platform CAD BOM flange_schlieren_imaging\"; results did not provide a row-specific material."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Treat the part as a structural metal flange for later KB planning because the geometry is a 10 mm thick bolted frame/plate rather than an elastomer, glass, or plastic consumable."
  uncertainty_notes:
    - "No sourced alloy family or grade was found; downstream modeling should keep this broad until original CAD material, drawing, or build documentation is available."
how_to_make:
  summary: "Make as a simple machined plate/flange from metal stock"
  manufacturing_steps:
    - "Cut rectangular blank from approximately 10 mm metal plate or bar stock."
    - "Mill the perimeter, aperture/frame reliefs, diagonal rib or groove features, and any counterbored or through-hole details visible in the CAD."
    - "Deburr and inspect flatness, hole positions, and sealing/mating faces before assembly with the glass, seals, and adjacent frame parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B3_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0011_1B3__views_2x2.png; web_search"
    cited_fact_or_basis: "The row-specific STEP and preview show a single thin rectangular flanged part, 80.00 x 10.00 x 160.00 mm, with holes and machined-looking frame features. targeted_web_search: queries tried: \"1B3_flange_schlieren_imaging manufacturing\", \"reAM250 flange_schlieren_imaging drawing\", and \"reAM250 1B3 flange schlieren\" no row-specific manufacturing route or drawing notes were found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Machining from plate is selected as the plausible route because the CAD shape is prismatic and hole/relief features are accessible with common milling and drilling operations."
  uncertainty_notes:
    - "No original drawing tolerances, finish, flatness requirement, or surface treatment were available; optical-window sealing may require tighter local flatness than the CAD preview alone can prove."
kb_implications:
  - "item_granularity: simple_part - Model as one custom machined flange/plate, not as a purchased optical module or multi-part assembly."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0011_1B3.md
source_research_sha256: "b4ffb94e666ec55f2ad2a806d8888c29fa900e1610d0267bfe3dc2206773b177"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the schlieren-window mounting function, CAD-derived planning mass, unresolved metal material evidence, machined plate route, and rectangular aperture-frame geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one metal mounting frame; glass, seals, optical adapter, fasteners, and adjacent door parts are separate BOM rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_metal_optical_mounting_frame
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
      reason: "Covers cutting metal plate stock into frame blanks."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers through-hole and counterbore preparation for the bolted interface."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for flat sealing faces, aperture edges, and optical-side alignment features."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks before stronger optical flatness metrology is selected."
  abstraction_decision: substitute_process_family
  rationale: "Although source fabrication is described as machining, the part is a shallow plate-like frame, so sheet and plate cutting with secondary precision machining is the conservative closure abstraction."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: bolted mounting interface around an optical access aperture
  material: structural_metal_unknown_aluminum_assumed_for_mass
  scale_or_capacity:
    mass_kg: 0.331
    bom_quantity: 1
    row_total_mass_kg: 0.331
    scale_class: small
  geometry_form: thin_rectangular_aperture_frame_with_corner_holes_and_diagonal_features
merge_pool:
  eligible: true
  functional_purpose_key: optical_access
  precision_guardrails:
    - material_family
    - flatness
    - aperture_alignment
    - hole_position
    - sealing_face_quality
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material uncertainty changes mass and may affect sealing-face finishing."
    - "Optical window stack may require tighter flatness and cleanliness than ordinary frame plates."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; compare with other optical aperture frames and environment barrier interfaces."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning a closure item ID for optical access mounting frames."
assumptions:
  - "Aluminum is only a planning-density assumption."
  - "The row is a passive mounting frame, not the glass, seal, adapter, nor complete optical module."
  - "Sealing and optical alignment requirements are possible guardrails rather than confirmed blockers."
unresolved:
  - "Material family and surface treatment remain unresolved."
  - "Required flatness, sealing compression, and optical-side alignment tolerance are not specified."
```
