---
group_id: ream250_kb_merge_0021_mounting_interface
candidate_rows:
  - source_row_number: 370
    item: "1764"
    path: research/ream250_bom/ream250_bom_row_0370_1764.md
    conversion_section_present: true
  - source_row_number: 309
    item: "179"
    path: research/ream250_bom/ream250_bom_row_0309_179.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0370_1764.md
    - research/ream250_bom/ream250_bom_row_0309_179.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0370_1764.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0309_179.md#kb-conversion
  notes: "Read both rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected the referenced CAD preview PNGs: row 370 is a long narrow 8 x 60 x 285 mm plate with internal cutout/rib features, while row 309 is a 140 x 140 x 25 mm annular scanner flange with central aperture and repeated mounting features."
rough_match_basis:
  functional_purpose_key: mounting_interface
  mass_window_kg:
    - 0.363
    - 0.487
merge_decision:
  decision: split
  rationale: "The broad mounting_interface key and similar aluminum-scenario masses are not enough to make one closure item. Row 370 is a camera-area mounting or spacing plate made through sheet/plate profile cutting with possible precision cleanup. Row 309 is a scanner alignment adapter flange made through general subtractive machining, with annular geometry, central aperture, hole pattern, concentricity, possible sealing surface, and optical-alignment guardrails. Those functions, process buckets, and geometry forms should remain separate at KB staging."
  proposed_closure_items:
    - item_id: ream250_camera_mounting_plate_v0
      member_rows:
        - 370
      functional_purpose: "mounting and spacing interface for camera support hardware"
      material: unknown_structural_metal_alloy
      scale_or_capacity:
        per_unit_mass_kg: 0.363
        bom_quantity: 1
        row_total_mass_kg: 0.363
        envelope_mm: "8 x 60 x 285"
        scale_class: medium
      geometry_form: long_narrow_plate_with_internal_cutouts
      process_family: sheet_plate_cutting_drilling
    - item_id: ream250_scanner_adapter_flange_v0
      member_rows:
        - 309
      functional_purpose: "scanner mounting and alignment interface"
      material: unknown_structural_metal_alloy
      scale_or_capacity:
        per_unit_mass_kg: 0.487
        bom_quantity: 1
        row_total_mass_kg: 0.487
        envelope_mm: "140 x 140 x 25"
        scale_class: small
      geometry_form: annular_scanner_flange_with_central_aperture_and_holes
      process_family: general_subtractive_machining
material_review:
  can_unify: true
  rationale: "Both rows remain broad unknown structural metal/alloy with aluminum, steel, or stainless scenarios unresolved. Material alone would not block a merge, but it also does not create positive evidence for one shared item because the stock forms and interface duties differ."
process_review:
  can_unify: false
  rationale: "Row 370 selected sheet_plate_cutting_drilling with cutting, deburring, surface finishing, dimensional inspection, and possible precision machining. Row 309 selected general_subtractive_machining with cutting, drilling, precision machining, cleaning, and inspection for a machined scanner flange. The flange's thickness, annular profile, central aperture, and repeated alignment/mounting features require a different primary closure handle than the long shallow plate."
geometry_review:
  can_unify: false
  rationale: "The row 370 preview shows a long narrow plate or spacer with internal cutout features. The row 309 preview shows a thick circular/annular scanner flange with a central aperture and repeated hole features around the annulus. These are not length or handedness variants of one part family; they are distinct geometry classes."
precision_review:
  blocks_merge: true
  rationale: "Row 370 carries flatness, interface alignment, and cutout-profile guardrails for a camera-area mounting plate. Row 309 adds hole pattern, concentricity, optical alignment, and possible sealing-surface guardrails for a scanner interface. The scanner flange precision stack is more specific and should not be merged into a generic plate interface."
assumptions:
  - "The aluminum-scenario masses from row research are kept for comparison, while final material remains unresolved for both rows."
  - "Existing KB items such as instrument_mounts_basic, precision_mounts_and_fixtures, fixture_mounting_plate_set, modular_machine_interface_v0, and mounting_bracket_steel were considered but are bulk, kit, steel, too massive, or too generic to replace these one-piece reAM250 geometry-specific staged closure items without losing guardrails."
  - "The row 370 part may later merge with other camera-support plates if additional candidates share long shallow plate geometry and alignment requirements."
  - "The row 309 part may later merge with other annular scanner or optical-interface flanges if those candidates share aperture, hole-pattern, concentricity, and interface requirements."
unresolved:
  - "Exact material, alloy grade, coating, thread details, flatness, surface finish, and inspection tolerances remain unknown for both rows."
  - "Row 370 mating faces and whether it directly carries camera hardware or acts as an intermediate spacer remain unresolved."
  - "Row 309 scanner interface standard, bolt specification, sealing role, cleanliness requirement, and optical alignment tolerance remain unresolved."
  - "A later KB staging pass should re-check for newly added generic metal mounting-plate or optical scanner-flange items before promoting the staged item IDs."
---

# Merge Review

The candidate pool should split into two staged closure items. The rough key correctly found two mounting-interface parts in a close mass band, but the CAD evidence and conversion sections separate them into a camera-area plate and a scanner adapter flange with different process and precision guardrails.
