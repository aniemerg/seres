---
row_identity:
  item: "2AS"
  cad_file: "2AS_end_switch_sensor_bottom"
  source_row_number: 95
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin bottom end-switch sensor target or mounting flag associated with the reAM250 bottom inductive end-switch sensor group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step"
    cited_fact_or_basis: "BOM row 95 identifies item 2AS as quantity 1, cad_file 2AS_end_switch_sensor_bottom. Neighboring BOM rows identify 2AQ as inductive_sensor_mount, 2AT3 as a Balluff inductive sensor bottom, and 2AU3 as a Balluff inductive sensor top. FreeCAD measured the row STEP as one solid with a 50.00 x 65.00 x 2.00 mm bounding box, and the rendered contact sheet shows a thin L-shaped plate/flag with a visible round hole. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found duplicate reAM250 BOM listings and generic end-switch pages, but no row-specific vendor/function source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row name and adjacency to the Balluff bottom inductive sensor row are interpreted as a bottom end-switch target or sensor-side flag rather than the purchased sensor itself."
    - "The round feature visible in the preview is interpreted as a mounting or clearance hole for fastening or aligning the flag/plate in the local end-switch assembly."
  uncertainty_notes:
    - "The BOM and CAD do not explicitly state whether this part is the sensed target, a protective flag, or a small sensor-side mounting plate; all interpretations imply the same simple thin-plate KB granularity."
mass:
  value_kg: 0.029
  basis: "FreeCAD measured 3729.515 mm^3 volume, 4235.763 mm^2 area, and a 50.00 x 65.00 x 2.00 mm bounding box. Using the local steel density table value of 7850 kg/m^3 gives 0.0293 kg, rounded to 0.029 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, 3729.515 mm^3 volume, 4235.763 mm^2 area, and a 50.00 x 65.00 x 2.00 mm bounding box. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid is treated as the physical material volume of the part."
    - "Generic steel density is used because the part appears to serve an inductive end-switch target/flag role and the local material metadata does not resolve a grade."
  uncertainty_notes:
    - "If the plate is aluminum rather than steel, the same CAD volume would imply about 0.010 kg; the material uncertainty is therefore the main mass uncertainty."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step"
    cited_fact_or_basis: "BOM row 95 names the part 2AS_end_switch_sensor_bottom. Neighboring BOM rows place it with Balluff inductive sensors and M12x1 sensor nuts. The row STEP measures as a 2.00 mm thick plate-like solid. Assembly STEP material extraction returned only material 'Allgemein' with density 1000.0, which is a placeholder and not resolved material evidence. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found no row-specific vendor, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal sheet family is selected because an inductive end-switch target/flag should be a reliable metal target and the geometry is a thin plate with a fastening or clearance feature."
    - "The result keeps the material at family level because neither BOM fields, STEP metadata, nor targeted web searches identify a specific alloy or grade."
  uncertainty_notes:
    - "The specific alloy, magnetic response, surface finish, and whether the actual material is carbon steel, stainless steel, or aluminum are unresolved."
how_to_make:
  summary: "Make as a simple thin sheet-metal flag or bracket: cut the 2 mm plate profile, drill or cut the visible hole/clearance feature, deburr, and finish as needed for the end-switch assembly."
  manufacturing_steps:
    - "Cut the L-shaped 2 mm sheet profile from ferrous sheet stock by laser, waterjet, CNC router/mill, or manual sheet cutting."
    - "Drill, punch, or cut the visible round mounting or clearance hole from the CAD-defined position."
    - "Deburr edges and holes, then apply corrosion protection or passivation if the selected steel grade requires it."
    - "Install and align the plate/flag in the bottom end-switch sensor assembly with the adjacent inductive sensor hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step; research/ream250_bom/ream250_bom_row_0095_2AS__views_2x2.png"
    cited_fact_or_basis: "The row STEP measures one 50.00 x 65.00 x 2.00 mm solid, and the rendered contact sheet shows a thin plate-like L-shaped part with a visible round hole. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\" found no row-specific manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The dominant manufacturing route is inferred from the thin constant-thickness plate geometry and visible plate feature."
    - "Hole size, exact contour, and any edge chamfers should be taken from CAD during downstream fabrication planning, not from the preview image."
  uncertainty_notes:
    - "The CAD preview is visual triage only; it does not establish tolerances, finish requirements, or whether small chamfers or bends are functionally required."
kb_implications:
  - "item_granularity: simple_part - thin plate/flag with one dominant sheet-cutting or machining route; no sub-BOM is implied by the row evidence."
---

CAD preview: `research/ream250_bom/ream250_bom_row_0095_2AS__views_2x2.png`

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0095_2AS.md
source_research_sha256: f174b5aad7a8be2989d3419aacb88f4bca09e6ade24326e2fcaa06aa3a4fa4e2
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the row function, material uncertainty, CAD-derived mass basis, sheet-cutting manufacturing hypothesis, KB implications,
    and CAD preview showing a thin L-shaped plate with one round hole.
decomposition:
  decision: simple_part
  rationale: The row evidence describes one small constant-thickness metal plate and flag associated with an inductive end-switch
    sensor; no internal components and sub-BOM are implied.
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_metal_cutting_drilling
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
  - stock_preparation
  - cutting
  - drilling
  - deburring
  - dimensional_inspection
  - calibration
  candidate_existing_processes:
  - process_id: sheet_metal_cutting_v0
    fit: direct
    reason: Covers sheet and plate cutting for flat parts.
  - process_id: drilling_basic_v0
    fit: supporting
    reason: Covers hole creation when the row needs bolt, locating, and passage features.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before staging selects the final recipe.
  - process_id: calibration_and_test_basic_v0
    fit: supporting
    reason: Relevant when calibration affects functional acceptance.
  abstraction_decision: keep_original_family
  rationale: 'The source route already belongs to the shared sheet/plate cutting bucket: cut the profile, make the hole, deburr,
    and finish. Metal additive manufacturing adds process burden without closure benefit for this flat plate.'
  process_guardrails:
    tolerance: review
    surface_finish: low_to_moderate
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: end-switch sensor plate and switching flag
  material: unknown_metal_sheet_likely_ferrous
  scale_or_capacity:
    mass_kg: 0.029
    bom_quantity: 1
    row_total_mass_kg: 0.029
    scale_class: small
  geometry_form: thin_l_shaped_plate_with_round_hole
merge_pool:
  eligible: true
  functional_purpose_key: end_switch_sensor_flag
  precision_guardrails:
  - inductive_sensor_detectability
  - hole_position
  - alignment_accuracy
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - sheet_plate_cutting_drilling
  import_risk_factors:
  - Exact alloy and magnetic response are unresolved; an inductive sensor target may require ferrous and sensor-detectable
    metal.
  - Downstream assembly may require hole and edge location accuracy for reliable switch triggering.
  post_merge_decision_notes: Final import/local manufacture and material substitution should be decided after merge review
    compares similar sensor flags and small mounting plates.
kb_staging:
  proposed_item_id: null
  notes: Do not assign a closure item ID during row conversion; likely merge candidate with other small end-switch plates
    and sensor flags.
assumptions:
- The item is treated as a passive sheet-metal flag and target rather than the purchased Balluff sensor.
- The 0.029 kg mass uses the CAD volume with generic steel density; aluminum would be substantially lighter.
- A simple sheet and plate fabrication route can meet the needed geometry if later alignment checks do not reveal tighter
  requirements.
unresolved:
- Specific alloy, magnetic response, and finish are not identified by the BOM, STEP metadata, and targeted search.
- The exact role among sensed target, protective flag, and small mounting plate remains ambiguous, though all imply similar
  KB granularity.
```
