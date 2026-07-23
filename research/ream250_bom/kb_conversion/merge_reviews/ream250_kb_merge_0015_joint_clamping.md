---
group_id: ream250_kb_merge_0015_joint_clamping
candidate_rows:
  - source_row_number: 329
    item: "331"
    path: research/ream250_bom/ream250_bom_row_0329_331.md
    conversion_section_present: true
  - source_row_number: 117
    item: "3F"
    path: research/ream250_bom/ream250_bom_row_0117_3F.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0329_331.md
    - research/ream250_bom/ream250_bom_row_0117_3F.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0329_331.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0117_3F.md#kb-conversion
  notes: "Read both candidate row frontmatter blocks, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD preview evidence cited by the row research was used to compare the threaded ISO-K bracket screw with shaped claw head against the annular ISO-KF clamping ring with tightening lugs."
rough_match_basis:
  functional_purpose_key: joint_clamping
  mass_window_kg:
    - 0.0676
    - 0.0933
merge_decision:
  decision: split
  rationale: "The rough joint_clamping key and similar per-unit masses are not enough to merge these rows. Row 329 is a stainless 316L bracket screw with an M10 threaded shank and integral claw head for DN63-DN250 ISO-K flange clamping. Row 117 is a stainless 304 DN32-DN40 ISO-KF clamping ring that closes around an elastomer-sealed flange pair. They differ in nominal flange standard, geometry class, production bucket, BOM quantity, row total mass, and precision guardrails, so one closure item would make later BOM mappings ambiguous."
  proposed_closure_items:
    - item_id: ream250_iso_k_stainless_bracket_screw_clamp_v0
      member_rows:
        - 329
      functional_purpose: "provide threaded claw preload for an ISO-K flange joint"
      material: stainless_steel_316l
      scale_or_capacity:
        per_unit_mass_kg: 0.0676
        bom_quantity: 176
        row_total_mass_kg: 11.9
        nominal_thread: M10
        flange_range: DN63_to_DN250_ISO_K
        torque_range_Nm: "12-16"
        scale_class: small
      geometry_form: threaded_screw_shank_with_integral_claw_clamp_head
      process_family: fastener_forming_thread_rolling
    - item_id: ream250_iso_kf_stainless_clamping_ring_v0
      member_rows:
        - 117
      functional_purpose: "clamp an elastomer-sealed ISO-KF flange joint closed"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.0933
        bom_quantity: 3
        row_total_mass_kg: 0.280
        nominal_interface: DN32_to_DN40_ISO_KF
        scale_class: small
      geometry_form: iso_kf_dn32_40_clamping_ring_with_tightening_lugs
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: false
  rationale: "Both candidates are stainless vacuum-clamping hardware, but row 329 cites 1.4404/AISI 316L media-contact stainless while row 117 cites 304/1.4301. The alloy difference is not the only blocker, but preserving the row-specific stainless grade, surface-cleanliness assumptions, and contact duties is useful for staging."
process_review:
  can_unify: false
  rationale: "Row 329 selects fastener_forming_thread_rolling with thread forming, shaped head machining, cleaning, and thread or torque inspection. Row 117 selects plumbing_connector_fabrication_testing with clamp-ring forming, lug feature machining, cleaning, dimensional fit inspection, and seal-stack compatibility. They may share generic machining and inspection anchors, but their primary closure process families should stay separate."
geometry_review:
  can_unify: false
  rationale: "Row 329 is a compact threaded shank with integral claw clamp head and M10 torque duty across DN63-DN250 ISO-K interfaces. Row 117 is an annular ISO-KF DN32-DN40 clamping ring with tightening lugs around an elastomer seal. These are different hardware forms rather than size variants of one part."
precision_review:
  blocks_merge: true
  rationale: "Row 329 guardrails are thread fit, clamp-contact geometry, torque rating, and stainless surface cleanliness. Row 117 guardrails are flange size range, ring clamp fit, tightening feature geometry, and seal-stack compatibility. Merging would collapse different preload paths and flange-interface constraints."
assumptions:
  - "The broad joint_clamping key correctly found two clamp-related rows, but the key is only a candidate-generation index and does not override geometry, process, and interface evidence."
  - "Row 329 should remain a high-quantity ISO-K bracket screw or claw fastener abstraction unless later staging finds a close existing KB fastener item with the same flange-contact and torque guardrails."
  - "Row 117 should remain an ISO-KF clamping-ring abstraction and may need reconciliation with other ISO-KF clamping-ring merge reviews during Phase 3 staging."
  - "The proposed item IDs are staging suggestions only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Row 329 exact factory process, thread tolerance, clamp-head contact specification, passivation method, and exact 316-family alloy variant remain unresolved."
  - "Row 117 exact fastener subparts, surface finish, vendor production method, clamp tolerances, and leak or sealing acceptance criteria remain unresolved."
  - "Later staging should search existing KB items, fastener kits, vacuum fittings, and previous reAM250 ISO-KF clamp abstractions before promotion."
  - "Final local manufacture versus import decisions are deferred for both proposed closure items."
---

# Merge Review

Split the `joint_clamping` candidate pool into two staged closure items. The rows are both small stainless vacuum-clamping hardware, but the bracket screw/claw fastener and ISO-KF clamping ring have different flange standards, geometry, process families, quantities, and precision guardrails.
