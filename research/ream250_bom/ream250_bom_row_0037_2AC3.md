---
row_identity:
  item: 2AC3
  cad_file: 2AC3_part_3
  source_row_number: 37
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Bottom-axis supported bearing block for the reAM250 lower axis bearing assembly; it supports a 16 mm shaft/ballscrew end radially while matching the axis height of the paired HIWIN SFA/GFD support hardware.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0037_2AC3__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "BOM row 37 names item 2AC3/2AC3_part_3 as 'axis bearing bottom'. The manifest maps it to bottom-axis-bearing assembly context 2AC0_bottom_axis_bearing_SLA10. The rendered context shows a pillow-block-like bearing support with a central bearing bore and mounting ears. HIWIN identifies SLA10 as a supported bearing, shaft nominal diameter 16 mm, with dimensions L 86 mm, B 24 mm, H 58 mm and bearing type 6200.2RS; those dimensions match the FreeCAD context bbox 86.00 x 24.00 x 58.00 mm."
    evidence_basis: independent_vendor_spec
  assumptions:
    - The row label 2AC3_part_3 imports with zero solids, so the matching SLA10 assembly context is treated as the row-level geometry/function proxy.
  uncertainty_notes:
    - The exact 2AC3 subpart cannot be isolated from the supplied CAD; function could represent one instance/subcomponent within the bottom-axis bearing assembly rather than a separately modeled commercial unit.
mass:
  value_kg: 0.53
  basis: "FreeCAD measured the available SLA10 assembly context volume as 67013.783 mm3. Treating that whole context as a steel-family metal volume gives 67013.783 mm3 x 1e-9 m3/mm3 x 7850 kg/m3 = 0.526 kg, rounded to 0.53 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step; kb/materials/properties.yaml; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "FreeCAD measured 6 solids, volume 67013.783 mm3, area 20516.186 mm2, bbox 86.00 x 24.00 x 58.00 mm for the assembly context. The local density table gives generic steel density as 7850 kg/m3. HIWIN SLA10 dimensions match the CAD context, but no row-level catalog mass was found. targeted_web_search: tried 'SLA10 bottom axis bearing material SLA10 bearing housing', 'HIWIN SLA supported bearing material SLA10 housing steel', and 'HIWIN SLA10 mass weight'; results identified function/dimensions but did not provide a row-specific mass."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The available assembly context volume is used as the row-level volume because the manifest says the specific 2AC3 label imported with zero solids.
    - A steel-family effective density is used as a conservative first estimate for the metal bearing support unit.
  uncertainty_notes:
    - If the isolated 2AC3 part is only one housing half, spacer, or other subcomponent of the SLA10 context, the row mass may be materially lower than 0.53 kg.
    - If the housing is aluminum, zinc alloy, cast iron, or a mixed metal/rubber bearing assembly, the all-steel-density estimate could be off by more than a factor of two.
material:
  primary_material: unknown metal/alloy bearing support unit with rolling bearing and seal elements
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "Local STEP material extraction for 2AC3_part_3 returned only Generic with density 1000.0, which is placeholder metadata. HIWIN identifies the matching SLA10 as a supported bearing using bearing type 6200.2RS, but the checked product page did not state housing or bearing material. targeted_web_search: tried 'HIWIN SLA supported bearing material SLA10 housing steel', 'HIWIN SFA SLA bearing units material housing', and 'HIWIN ballscrew supports SLA10 material datasheet'; no row-matched material grade/specification was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The functional item is modeled broadly as a metal/alloy bearing support rather than assigning an unsupported steel, cast iron, or aluminum grade.
  uncertainty_notes:
    - Material grade is unresolved at the level needed for manufacturing; later KB work should split housing, bearing, circlip, and seal materials if a catalog drawing or teardown source is found.
how_to_make:
  summary: "Fabricate the support housing, Manufacture a 6200.2RS bearing, add the circlip/seals, and assemble/inspect the bearing block"
  manufacturing_steps:
    - For local manufacture, machine or cast the bearing housing to the 86 mm x 24 mm x 58 mm envelope with mounting features and a bearing seat.
    - Install a 6200.2RS bearing and circlip, then check bore alignment, shaft fit, and radial support function in the bottom-axis assembly.
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0037_2AC3__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "The vendor page identifies a ready-made SLA10 supported bearing with dimensions and 6200.2RS bearing type. The preview shows a compact bearing block with central bore and mounting ears. The detailed machining/casting and assembly route is inferred from geometry and standard bearing-block construction rather than stated by a source. targeted_web_search: tried 'HIWIN SLA10 manufacturing housing material', 'HIWIN SLA10 datasheet material', and 'SLA10 bearing block material'; results did not provide a row-specific manufacturing process."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The inferred Manufacturing route assumes conventional bearing-block construction: machined/cast housing plus installed rolling bearing and retainer hardware.
  uncertainty_notes:
    - Without a manufacturer drawing or teardown, local manufacturing details such as heat treatment, fits/tolerances, housing alloy, seal material, and bearing preload are not resolved.
kb_implications:
  - "item_granularity: complex_module - Model this row as a functional SLA10-class supported bearing block for this pass; split into housing, 6200.2RS bearing, circlip/seal, and assembly operations only when a sub-BOM or material drawing is available."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0037_2AC3.md
source_research_sha256: "a92c58e398e627566614631f98e66a31ef0b2d16df86fa2f81f605d04d0a2d43"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the bottom-axis supported-bearing-block function, 0.53 kg context-derived mass estimate, unresolved metal bearing-support material evidence, inferred housing plus bearing assembly route, KB implication, and CAD preview showing a pillow-block-like supported bearing unit."
decomposition:
  decision: complex_module
  rationale: "The row-level geometry is a supported bearing block containing at least a housing, rolling bearing, retainer hardware, seals, fits, and alignment requirements; these are closure-relevant if local manufacture is pursued."
  proposed_subparts:
    - bearing_block_housing
    - rolling_bearing_6200_2rs
    - retainer_clip
    - seal_elements
    - mounting_fasteners_context
process_abstraction:
  original_process_family: vendor_supported_bearing_block_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - precision_machining
    - heat_treatment
    - grinding_lapping
    - assembly
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: bearing_set_heavy_production_v0
      fit: partial
      reason: "Anchors rolling bearing manufacture, but does not cover the specific 6200.2RS bearing and housing integration."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to bearing seat, mounting faces, and shaft alignment in the housing."
    - process_id: heat_treatment_hardening_v0
      fit: supporting
      reason: "Relevant to bearing races and rolling elements if local bearing manufacture is attempted."
    - process_id: precision_grinding_basic_v0
      fit: supporting
      reason: "Relevant to bearing race and seat surface finish requirements."
    - process_id: seal_installation_v0
      fit: supporting
      reason: "Relevant to 2RS sealing elements and protected bearing assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Basic QA anchor; later staging needs bore alignment, shaft fit, and runout checks."
  abstraction_decision: needs_human
  rationale: "The row should not be represented as only a machined block because the supported bearing assembly depends on precision rolling elements, seals, and alignment. Decompose before any local manufacturing recipe."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: review
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: "supported bearing block for radial support of a machine axis shaft"
  material: unresolved_metal_bearing_support_with_bearing_and_seals
  scale_or_capacity:
    mass_kg: 0.53
    bom_quantity: 1
    row_total_mass_kg: 0.53
    scale_class: small
  geometry_form: compact_pillow_block_bearing_support_with_mounting_ears
merge_pool:
  eligible: false
  functional_purpose_key: bearing_support
  precision_guardrails:
    - bearing_type_6200_2rs
    - shaft_bore_alignment
    - bearing_seat_tolerance
    - seal_materials
    - context_geometry_proxy
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Specific isolated row geometry is unavailable because the named part imported with zero solids and context geometry was used."
    - "Rolling bearing manufacture, housing fit, seals, and alignment inspection create a high closure burden."
  post_merge_decision_notes: "Final import/local decision is deferred until supported bearing blocks are reviewed together and decomposed into housing, bearing, seal, and retainer items if needed."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple closure item ID at row conversion; merge/decomposition review should decide the SLA10-class bearing support abstraction."
assumptions:
  - "BOM quantity is 1 and row total mass is treated as 0.53 kg from the assembly-context estimate."
  - "The available SLA10 context is used because the specific 2AC3 label imported with zero solids."
  - "The item is treated as a functional supported bearing block rather than only the housing."
unresolved:
  - "Exact isolated geometry, housing material, bearing material, seal material, fits, preload, and inspection sequence remain unresolved."
  - "Whether this row should be an imported bearing-block module, a decomposed local assembly, and a merge candidate with other supported bearings is deferred."
```
