---
group_id: ream250_kb_merge_0014_joint_clamping
candidate_rows:
  - source_row_number: 143
    item: "3R1"
    path: research/ream250_bom/ream250_bom_row_0143_3R1.md
    conversion_section_present: true
  - source_row_number: 328
    item: "323"
    path: research/ream250_bom/ream250_bom_row_0328_323.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0143_3R1.md
    - research/ream250_bom/ream250_bom_row_0328_323.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0143_3R1.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0328_323.md#kb-conversion
  notes: "Read both candidate row frontmatter blocks, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Geometry evidence cited in the row research was used to compare the compact stepped claw clamp form, central M8 interface, bearing faces, and DN 63-DN 100 ISO-K/base-plate guardrails."
rough_match_basis:
  functional_purpose_key: joint_clamping
  mass_window_kg:
    - 0.0323
    - 0.0323
merge_decision:
  decision: merge
  rationale: "Rows 143 and 328 resolve to the same Pfeiffer Vacuum 350BPD100 zinc-plated steel ISO-K base-plate claw clamp. They share the same vendor product identity, material, CAD volume, per-unit mass, bounding box, DN 63-DN 100 ISO-K interface, and compact stepped claw geometry. The only closure-relevant difference is BOM quantity and row total mass, so one staged closure item should cover both appearances."
  proposed_closure_items:
    - item_id: ream250_iso_k_base_plate_claw_clamp_v0
      member_rows:
        - 143
        - 328
      functional_purpose: "clamp an ISO-K flange to a grooved base plate in a vacuum flange joint"
      material: zinc_plated_steel
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.0323
          - 0.0323
        bom_quantity_range:
          - 4
          - 8
        row_total_mass_range_kg:
          - 0.129
          - 0.259
        nominal_interfaces:
          - DN_63_to_DN_100_ISO_K
          - M8_base_plate_clamp_interface
        scale_class: small
      geometry_form: compact_stepped_iso_k_claw_clamp_block_with_central_m8_interface
      process_family: fastener_forming_thread_rolling
material_review:
  can_unify: true
  rationale: "Both rows cite row-matched Pfeiffer Vacuum product evidence identifying 350BPD100 as zinc-plated steel. Both mass estimates use the same STEP volume with generic steel density and explicitly treat the zinc coating as negligible for mass but relevant for surface protection."
process_review:
  can_unify: true
  rationale: "The row conversions choose neighboring abstractions: row 143 emphasizes machining a small steel clamp blank, while row 328 emphasizes standard fastener/clamping hardware with forming, machining, drilling, threading, coating, and inspection. Those operations are compatible for one staged closure item; Phase 3 can choose the final local path or import boundary while preserving machining, M8 interface, coating, and fit inspection guardrails."
geometry_review:
  can_unify: true
  rationale: "The CAD and research evidence give the same one-piece compact claw clamp geometry with a 24.00 x 18.60 x 15.00 mm bounding box, stepped clamp shoulders, central M8 interface, and bearing or seating faces for the ISO-K/base-plate joint. Row file naming differs by local BOM item code, not by geometry family."
precision_review:
  blocks_merge: false
  rationale: "Clamp shoulder geometry, seating face finish, M8 interface fit, burr control, coating, and DN 63-DN 100 ISO-K/base-plate fit remain staging guardrails. No evidence shows row-specific tolerances, material, or geometry that would force separate closure items."
assumptions:
  - "Rows 143 and 328 represent the same purchased Pfeiffer 350BPD100 part used in different locations of the reAM250 BOM."
  - "Phase 3 should preserve the different BOM quantities and row total masses in row mappings rather than making separate closure items."
  - "The M8 interface is treated as an integrated feature of the clamp item for this merge pass."
  - "Final import/local manufacture remains deferred; this review only decides that the two rows can share one staged closure abstraction."
unresolved:
  - "Exact steel grade, zinc plating specification, factory production process, thread or clearance-hole detail, and clamp tolerance stack are not resolved by row evidence."
  - "Phase 3 should search existing KB items again before promotion and decide whether this maps to an existing fastener or vacuum hardware item, a new local-manufacture candidate, or a standard hardware import."
  - "If later evidence proves the central M8 feature is clearance-only rather than threaded, update the staging guardrails without splitting these two rows."
---

# Merge Review

Rows 143 and 328 merge into one staged zinc-plated steel ISO-K base-plate claw clamp abstraction. Preserve each row's BOM quantity, row total mass, M8 interface guardrail, DN 63-DN 100 ISO-K fit, and coating requirements for Phase 3.
