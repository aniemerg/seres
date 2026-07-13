---
group_id: ream250_kb_merge_0028_powder_containment
candidate_rows:
  - source_row_number: 177
    item: "6E2"
    path: research/ream250_bom/ream250_bom_row_0177_6E2.md
    conversion_section_present: true
  - source_row_number: 336
    item: "423"
    path: research/ream250_bom/ream250_bom_row_0336_423.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0177_6E2.md
    - research/ream250_bom/ream250_bom_row_0336_423.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0177_6E2.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0336_423.md#kb-conversion
  notes: "Read both rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected both referenced CAD preview PNGs: row 177 is a 32.91 x 118.50 x 268.00 mm stainless bent or angled right-side recoater plate, while row 336 is an 80.00 x 268.00 x 4.00 mm flat tapered powder-chute front/back panel with shallow edge features."
rough_match_basis:
  functional_purpose_key: powder_containment
  mass_window_kg:
    - 0.272
    - 0.38
merge_decision:
  decision: split
  rationale: "The two rows share the powder_containment screening key, similar length, small mass, and sheet_plate_cutting_drilling process bucket, but they should not converge to one closure item. Row 177 is a recoater right-side plate in a four-plate recoater set, with a tall bent side-wall geometry and fit-to-recoater guardrails. Row 336 is a powder-chute front/back wall or liner panel, with a flat tapered 4 mm panel geometry and chute-fit plus edge-lip guardrails. A single closure item would hide different installed interfaces and geometry even though later staging can reuse the same stock, cutting, forming, finishing, and inspection process anchors."
  proposed_closure_items:
    - item_id: ream250_recoater_side_powder_containment_plate_v0
      member_rows:
        - 177
      functional_purpose: "side containment and structural boundary plate for recoater powder-handling hardware"
      material: stainless_steel
      scale_or_capacity:
        per_unit_mass_kg: 0.272
        bom_quantity: 1
        row_total_mass_kg: 0.272
        envelope_mm: "32.91 x 118.50 x 268.00"
        scale_class: small
      geometry_form: tall_bent_or_angled_recoater_side_plate
      process_family: sheet_plate_cutting_drilling
    - item_id: ream250_powder_chute_wall_panel_v0
      member_rows:
        - 336
      functional_purpose: "powder chute wall or liner panel guiding powder flow"
      material: unknown_powder_compatible_metal_sheet
      scale_or_capacity:
        per_unit_mass_kg: 0.38
        bom_quantity: 1
        row_total_mass_kg: 0.38
        envelope_mm: "80.00 x 268.00 x 4.00"
        scale_class: small
      geometry_form: flat_tapered_powder_chute_panel_with_shallow_edge_features
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: true
  rationale: "Material does not block shared staging assumptions. Row 177 has sourced stainless steel family metadata, while row 336 has unresolved metal sheet material and a steel-density planning mass. Both can be treated as powder-compatible metal sheet or thin plate for process closure, with stainless grade, wear behavior, and surface finish preserved as row-specific guardrails. Existing KB entries such as metal_sheet, metal_sheet_or_plate, formed_sheet_metal_parts, discharge_chute_steel, and powder_recoater_module_v0 are raw stock, broad intermediates, a generic chute, or larger modules; none directly replaces both proposed row-specific closure items without losing reAM250 powder-contact interface details."
process_review:
  can_unify: true
  rationale: "Both conversions select sheet_plate_cutting_drilling and cite the same local process anchors: sheet_metal_cutting_v0, sheet_metal_bending_and_forming_v0 or metal_forming_basic_v0, finishing_deburring_v0, machining_basic_v0 for local features, and inspection_basic_v0. The common closure chain is stock preparation, profile cutting, forming or local edge machining where needed, deburring, surface finishing, and dimensional inspection. This process commonality supports a shared manufacturing strategy but is not enough to merge the installed parts."
geometry_review:
  can_unify: false
  rationale: "The CAD previews separate the parts. Row 177 is a tall narrow bent or angled side plate with visible folded side-wall form and a 32.91 x 118.50 x 268.00 mm envelope. Row 336 is a long flat tapered 4 mm chute wall panel, 80.00 x 268.00 x 4.00 mm, with shallow edge or lip features. These are not simple handedness, thickness, or length variants of one closure item; they represent different powder-contact panel geometries in different parent subassemblies."
precision_review:
  blocks_merge: true
  rationale: "The precision risks differ by interface. Row 177 carries fit_to_recoater_plate_set, powder_contact_surface_finish, bend_angle_accuracy, and stainless_grade_review guardrails. Row 336 carries powder_contact_surface_finish, edge_lip_geometry, chute_fit, and material_wear_behavior guardrails. Powder-contact finish overlaps, but recoater plate alignment and bend angle control are distinct from powder-chute wall fit and edge-lip geometry, so precision and interface guardrails block a single merged closure item."
assumptions:
  - "The shared 268 mm dimension and powder_containment key reflect rough screening, not proof of common installed function."
  - "Both rows remain local sheet or thin-plate fabrication candidates for Phase 3 unless later evidence shows certified material, coating, or finish requirements that force import."
  - "The proposed item IDs are staging names for review and should be rechecked against any future adjacent recoater-plate or powder-chute merge groups before promotion."
  - "Existing KB sheet, formed-sheet, generic chute, and powder-recoater module items were considered but are either too generic, raw-stock-like, or assembly-level for direct reuse at this merge-review stage."
unresolved:
  - "Row 177 exact stainless grade, surface finish, bend method, and recoater mating tolerances remain unsourced."
  - "Row 336 actual alloy, wear behavior, surface finish, attachment method, and parent chute interface remain unsourced."
  - "Phase 3 should preserve row-specific envelope, subassembly placement, material confidence, and powder-contact guardrails in proposed BOM mappings."
---

# Merge Review

Split the candidate set into two staged closure items. The shared powder-containment function and fabrication route are useful for process planning, but the CAD evidence and interface guardrails separate a recoater side plate from a powder-chute wall panel.
