---
row_identity:
  item: "2AR"
  cad_file: "2AR_end_switch_sensor_top"
  source_row_number: 94
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin top end-switch sensor target or mounting flag associated with the reAM250 top inductive end-switch sensor group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step"
    cited_fact_or_basis: "BOM row 94 identifies item 2AR as quantity 1, cad_file 2AR_end_switch_sensor_top. Neighboring BOM rows identify 2AQ as inductive_sensor_mount, 2AT3 as inductive sensor bottom, and 2AU3 as inductive sensor top. FreeCAD measured the row STEP as one solid with a 40.00 x 60.00 x 2.00 mm bounding box, and the rendered contact sheet shows a thin L-shaped plate/flag with two round holes. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found duplicate reAM250 BOM listings and generic end-switch material pages, but no row-specific vendor/function source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row name and adjacency to the Balluff top inductive sensor row are interpreted as a top end-switch target or sensor-side flag rather than the purchased sensor itself."
    - "The two holes visible in the preview are interpreted as mounting holes for fastening the flag/plate into the local end-switch assembly."
  uncertainty_notes:
    - "The BOM and CAD do not explicitly state whether this part is the sensed target, a protective flag, or a small sensor-side mounting plate; all interpretations imply the same simple thin-plate KB granularity."
mass:
  value_kg: 0.028
  basis: "FreeCAD measured 3529.515 mm^3 volume, 3975.763 mm^2 area, and a 40.00 x 60.00 x 2.00 mm bounding box. Using the local steel density table value of 7850 kg/m^3 gives 0.0277 kg, rounded to 0.028 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, 3529.515 mm^3 volume, 3975.763 mm^2 area, and a 40.00 x 60.00 x 2.00 mm bounding box. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid is treated as the physical material volume of the part."
    - "Generic steel density is used because the part appears to serve an inductive end-switch target/flag role and the local material metadata does not resolve a grade."
  uncertainty_notes:
    - "If the plate is aluminum rather than steel, the same CAD volume would imply about 0.0095 kg; the material uncertainty is therefore the main mass uncertainty."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step"
    cited_fact_or_basis: "BOM row 94 names the part 2AR_end_switch_sensor_top. Neighboring BOM rows place it with Balluff inductive sensors and M12x1 sensor nuts. The row STEP measures as a 2.00 mm thick plate-like solid. Assembly STEP material extraction returned only material 'Allgemein' with density 1000.0, which is a placeholder and not resolved material evidence. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found no row-specific vendor, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal sheet family is selected because an inductive end-switch target/flag should be a reliable metal target and the geometry is a thin plate with fastening holes."
    - "The result keeps the material at family level because neither BOM fields, STEP metadata, nor targeted web searches identify a specific alloy or grade."
  uncertainty_notes:
    - "The specific alloy, magnetic response, surface finish, and whether the actual material is carbon steel, stainless steel, or aluminum are unresolved."
how_to_make:
  summary: "Make as a simple thin sheet-metal flag or bracket: cut the 2 mm plate profile, drill or cut the two mounting holes, deburr, and finish as needed for the end-switch assembly."
  manufacturing_steps:
    - "Cut the L-shaped 2 mm sheet profile from ferrous sheet stock by laser, waterjet, CNC router/mill, or manual sheet cutting."
    - "Drill, punch, or cut the two mounting holes visible in the CAD preview."
    - "Deburr edges and holes, then apply corrosion protection or passivation if the selected steel grade requires it."
    - "Install and align the plate/flag in the top end-switch sensor assembly with the adjacent inductive sensor hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step; research/ream250_bom/ream250_bom_row_0094_2AR__views_2x2.png"
    cited_fact_or_basis: "The row STEP measures one 40.00 x 60.00 x 2.00 mm solid, and the rendered contact sheet shows a thin plate-like L-shaped part with two round holes. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\" found no row-specific manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The dominant manufacturing route is inferred from the thin constant-thickness plate geometry and visible mounting holes."
    - "Hole sizes and any bend/edge chamfers should be taken from CAD during downstream fabrication planning, not from the preview image."
  uncertainty_notes:
    - "The CAD preview is visual triage only; it does not establish tolerances, finish requirements, or whether bends/chamfers are functionally required."
kb_implications:
  - "item_granularity: simple_part - thin plate/flag with one dominant sheet-cutting or machining route; no sub-BOM is implied by the row evidence."
---

CAD preview: `research/ream250_bom/ream250_bom_row_0094_2AR__views_2x2.png`

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0094_2AR.md
source_research_sha256: "d8004d5ee2832d43017fa58fae12beaffb5a8774adce347d013d3cd988d58af4"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the end-switch flag function, CAD-volume mass estimate, uncertain metal-sheet material evidence, sheet cutting route, KB implication, and CAD preview showing a thin L-shaped plate with two holes."
decomposition:
  decision: simple_part
  rationale: "The row is a single thin plate/flag associated with sensor triggering and has no subassembly dependencies."
  proposed_subparts: []
process_abstraction:
  original_process_family: thin_sheet_metal_cutting_drilling
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: direct
      reason: "Matches cutting a small constant-thickness sheet profile."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers the two mounting holes visible in the CAD preview."
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Alternative coarse cutting anchor for a small metal plate."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers hole spacing, outline, and fit checks before sensor alignment."
  abstraction_decision: keep_original_family
  rationale: "The inferred manufacturing route is already simple sheet cutting and drilling, matching the canonical sheet and plate bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: end-switch trigger flag and local sensor mounting feature
  material: unknown_metal_sheet
  scale_or_capacity:
    mass_kg: 0.028
    bom_quantity: 1
    row_total_mass_kg: 0.028
    scale_class: tiny
  geometry_form: small_l_shaped_two_mm_sheet_plate_with_two_mounting_holes
merge_pool:
  eligible: true
  functional_purpose_key: sensor_triggering
  precision_guardrails:
    - hole_pattern
    - target_position
    - inductive_detectability
    - plate_thickness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material family is unresolved; inductive sensor target behavior may require ferrous steel rather than aluminum."
    - "Alignment to the sensor group may impose tighter positional tolerance than the CAD preview indicates."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares other small sensor flags and brackets."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; may merge with other small sheet-metal sensor flags if material and alignment guardrails match."
assumptions:
  - "Generic steel density was used for mass planning because the exact material is unresolved and inductive target service likely needs metal."
  - "The top label is positional context and should not force a unique closure item."
unresolved:
  - "Exact alloy, magnetic response, coating, hole dimensions, bend/chamfer details, and end-switch assembly alignment tolerance remain unresolved."
```
