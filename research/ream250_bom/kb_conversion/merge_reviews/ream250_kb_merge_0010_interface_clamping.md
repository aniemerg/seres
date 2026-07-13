---
group_id: ream250_kb_merge_0010_interface_clamping
candidate_rows:
  - source_row_number: 185
    item: "6I"
    path: research/ream250_bom/ream250_bom_row_0185_6I.md
    conversion_section_present: true
  - source_row_number: 142
    item: "3Q5"
    path: research/ream250_bom/ream250_bom_row_0142_3Q5.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0185_6I.md
    - research/ream250_bom/ream250_bom_row_0142_3Q5.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0185_6I.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0142_3Q5.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD preview evidence was reviewed from the row descriptions: row 185 is a thin slotted aluminum clamping plate, while row 142 is a compact stepped threaded ISO-K claw clamp."
rough_match_basis:
  functional_purpose_key: interface_clamping
  mass_window_kg:
    - 0.0258
    - 0.0323
merge_decision:
  decision: split
  rationale: "The rough interface_clamping key and similar per-unit masses are not enough to merge these rows. Row 185 is a custom flat Aluminum 6061 plate that retains adjacent powder-handling or carriage hardware through a slotted plate interface. Row 142 is a vendor-standard zinc-plated steel ISO-K claw clamp with M8 thread and preload duty for a flange and O-ring groove interface. Material, process route, geometry, and precision guardrails point to separate closure items."
  proposed_closure_items:
    - item_id: ream250_front_clamping_plate_v0
      member_rows:
        - 185
      functional_purpose: "front clamping and retaining plate for adjacent powder-handling and carriage hardware"
      material: aluminum_alloy_6061
      scale_or_capacity:
        per_unit_mass_kg: 0.0258
        bom_quantity: 1
        row_total_mass_kg: 0.0258
        envelope_mm: "80 x 42 x 4"
        scale_class: small
      geometry_form: thin_flat_plate_with_rounded_central_slot_and_mounting_holes
      process_family: sheet_plate_cutting_drilling
    - item_id: iso_k_base_plate_claw_clamp_v0
      member_rows:
        - 142
      functional_purpose: "service flange claw clamp for fastening an ISO-K flange to a base plate and sealing-groove interface"
      material: zinc_plated_steel
      scale_or_capacity:
        per_unit_mass_kg: 0.0323
        bom_quantity: 4
        row_total_mass_kg: 0.129
        nominal_thread: M8
        flange_range: DN63_to_DN100_ISO_K
        scale_class: small
      geometry_form: stepped_threaded_claw_clamp_block
      process_family: general_subtractive_machining
material_review:
  can_unify: false
  rationale: "Row 185 is CAD-resolved Aluminum 6061 plate stock at about 26 g per unit. Row 142 is catalog-resolved zinc-plated steel hardware at about 32 g per unit and four units per BOM row. The materials serve different duties and imply different closure inputs and finishes, so material unification would hide important modeling differences."
process_review:
  can_unify: false
  rationale: "Row 185 selects sheet_plate_cutting_drilling with secondary drilling and inspection for a shallow plate. Row 142 selects general_subtractive_machining with threading, bearing-face finishing, plating, and ISO-K clamp inspection. A later staging pass may reuse generic machining and inspection anchors, but the primary closure process families should stay separate."
geometry_review:
  can_unify: false
  rationale: "Row 185 is an 80 x 42 x 4 mm flat plate with a rounded central slot, clearance features, and mounting holes. Row 142 is a 24 x 18.6 x 15 mm stepped claw clamp block with a central M8 threaded feature and flange-gripping faces. These are different interface classes rather than scale variants of one clamping item."
precision_review:
  blocks_merge: true
  rationale: "Row 185 guardrails are hole position, slot position, plate thickness, and mating clearance. Row 142 guardrails are M8 thread fit, clamp bearing-face finish, ISO-K flange geometry, and preload reliability for a seal interface. Merging would collapse distinct precision risks and make later BOM mappings ambiguous."
assumptions:
  - "The broad interface_clamping key correctly found two clamping-related rows, but the key is only a search index and does not override material, process, geometry, and precision evidence."
  - "Row 185 should remain a custom reAM250 plate-like part unless later staging finds a reusable generic aluminum retaining plate abstraction with matching slot and hole guardrails."
  - "Row 142 should be staged as reusable ISO-K service flange clamp hardware, potentially sharing identity with other ISO-K claw clamp rows if those appear in later merge groups."
  - "The proposed item IDs are staging suggestions only; this task does not write KB YAML and final import/local manufacture remains deferred."
unresolved:
  - "Row 185 exact fastener callouts, countersinks, edge breaks, coating, and mating front/back clamping context remain unresolved."
  - "Row 142 actual vendor production route, zinc plating thickness, property grade, thread tolerance, and inspection standard remain unresolved."
  - "Later staging should search existing KB items and imports for generic retaining plates, clamp plates, ISO-K flange clamps, and fastener kits before promoting either proposed item."
---

# Merge Review

Split the `interface_clamping` candidate pool into two staged closure items. The rows are similar in mass and broad function, but they differ in material, geometry, process family, and precision duty.
