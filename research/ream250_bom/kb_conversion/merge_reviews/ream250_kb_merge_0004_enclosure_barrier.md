---
group_id: ream250_kb_merge_0004_enclosure_barrier
candidate_rows:
  - source_row_number: 58
    item: "2AG"
    path: research/ream250_bom/ream250_bom_row_0058_2AG.md
    conversion_section_present: true
  - source_row_number: 344
    item: "522"
    path: research/ream250_bom/ream250_bom_row_0344_522.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0058_2AG.md
    - research/ream250_bom/ream250_bom_row_0344_522.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0058_2AG.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0344_522.md#kb-conversion
  notes: "Read both rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected both referenced CAD preview PNGs: row 58 is a 210 x 200 x 15 mm ribbed z-axis cover plate with small mounting holes, while row 344 is a 170 x 393 x 10 mm flat front scanner cover panel with edge lips and laser-safety material uncertainty."
rough_match_basis:
  functional_purpose_key: enclosure_barrier
  mass_window_kg:
    - 1.51
    - 1.8
merge_decision:
  decision: split
  rationale: "The rows share the broad enclosure_barrier screening key, similar aluminum-scenario mass, and sheet_plate_cutting_drilling process bucket, but they should not converge to one closure item. Row 58 protects a z-axis and glass-scale area with local mounting-hole, rib, clearance, and alignment guardrails. Row 344 is the front member of the scanner laser-safety cover set, where opaque barrier material and laser-safety rating dominate the risk. A single closure item would hide different installed functions and qualification constraints."
  proposed_closure_items:
    - item_id: ream250_z_axis_glass_scale_cover_plate_v0
      member_rows:
        - 58
      functional_purpose: "protective closure cover for z-axis and glass-scale area"
      material: unknown_metal_alloy
      scale_or_capacity:
        per_unit_mass_kg: 1.51
        bom_quantity: 1
        row_total_mass_kg: 1.51
        envelope_mm: "210 x 200 x 15"
        scale_class: small
      geometry_form: shallow_ribbed_machined_cover_plate_with_mounting_holes
      process_family: sheet_plate_cutting_drilling
    - item_id: ream250_scanner_front_laser_barrier_panel_v0
      member_rows:
        - 344
      functional_purpose: "opaque front barrier panel for scanner enclosure"
      material: unknown_opaque_laser_safety_barrier_material
      scale_or_capacity:
        per_unit_mass_kg: 1.8
        bom_quantity: 1
        row_total_mass_kg: 1.8
        envelope_mm: "170 x 393 x 10"
        scale_class: small
      geometry_form: flat_rectangular_cover_panel_with_edge_lip_features
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: false
  rationale: "Row 58 is modeled as an unknown metal alloy cover based on rigid ribbed plate geometry inside a motion-axis assembly. Row 344 deliberately keeps material broader as an unknown opaque laser-safety barrier material because the source identifies a laser safety cover but does not resolve whether the physical barrier is ordinary metal, coated material, specialty polymer, composite, or another certified opaque stock. Existing KB items such as protective_cover_set, transparent_panel_set, panel_or_door_assembly, enclosure_small, chamber_shell_sealed, and metal_sheet_or_plate were considered but are sets, transparent panels, assemblies, cabinets, sealed shells, or raw stock rather than direct reusable closure items for both rows."
process_review:
  can_unify: true
  rationale: "The manufacturing strategy can use the same high-level process family. Both row conversions select sheet_plate_cutting_drilling with stock preparation, cutting, local machining, deburring, finishing, and dimensional inspection. The row 58 chain emphasizes drilling and local precision machining for ribs, reliefs, and z-axis clearance. The row 344 chain adds coating or finish plus later laser-safety suitability checks. Shared process anchors support common manufacturing planning but do not justify one closure item."
geometry_review:
  can_unify: false
  rationale: "The CAD previews show different finished forms. Row 58 is nearly square, shallow, and visibly ribbed with several small mounting holes and local machined reliefs in a 210 x 200 x 15 mm envelope. Row 344 is a longer rectangular scanner-cover panel, 170 x 393 x 10 mm, with edge lips and no visible comparable hole pattern in the preview. These are not simple handedness, length, or thickness variants of one panel family because their interface features and installed roles differ."
precision_review:
  blocks_merge: true
  rationale: "Row 58 carries hole_pattern_alignment, clearance_to_motion_axis_components, alignment review near the glass-scale area, and material-substitution guardrails. Row 344 carries enclosure_fit, laser_safety_rating, edge_lip_geometry, and opaque material qualification guardrails. Laser-safety qualification is a distinct failure mode from motion-axis cover clearance and mounting alignment, so precision and qualification requirements block a single merged closure item."
assumptions:
  - "BOM quantity is 1 for both rows, so row total mass equals each per-unit planning mass."
  - "The aluminum-scenario masses are retained only for rough scale comparison; neither row has sourced final material."
  - "Both rows remain local sheet or plate fabrication candidates for Phase 3 unless later material, coating, certification, or tolerance evidence forces import."
  - "The proposed item IDs are staging names for review; Phase 3 should re-check adjacent scanner-cover and z-axis cover candidates before promotion."
  - "Existing KB cover, panel, enclosure, chamber-shell, and raw plate items are not close enough to replace both proposed staged items without losing row-specific guardrails."
unresolved:
  - "Row 58 actual alloy, finish, hole tolerances, flatness, and clearance requirements near the z-axis glass scale remain unsourced."
  - "Row 344 actual material family, optical density, laser wavelength rating, finish, attachment details, and certification basis remain unsourced."
  - "Phase 3 should preserve the row-specific envelope, parent assembly, material uncertainty, geometry, and precision guardrails in proposed BOM mappings."
---

# Merge Review

Split the candidate set into two staged closure items. The shared enclosure-barrier key and plate-fabrication route are useful for discovery, but the evidence separates a z-axis/glass-scale cover plate from a scanner laser-safety front barrier panel.
