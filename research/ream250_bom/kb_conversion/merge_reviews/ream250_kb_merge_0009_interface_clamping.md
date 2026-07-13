---
group_id: ream250_kb_merge_0009_interface_clamping
candidate_rows:
  - source_row_number: 313
    item: "193"
    path: research/ream250_bom/ream250_bom_row_0313_193.md
    conversion_section_present: true
  - source_row_number: 323
    item: "276"
    path: research/ream250_bom/ream250_bom_row_0323_276.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0313_193.md
    - research/ream250_bom/ream250_bom_row_0323_276.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0313_193.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0323_276.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD preview evidence in the row research was used to compare the compact ISO-KF Pratze/claw clamp body, single through-hole geometry, and body-only versus complete-hardware boundary."
rough_match_basis:
  functional_purpose_key: interface_clamping
  mass_window_kg:
    - 0.0056
    - 0.00562
merge_decision:
  decision: merge
  rationale: "Rows 313 and 323 are the same Wissel ISO-KF Pratze/claw clamp family with identical measured CAD volume, nearly identical body mass, aluminum clamp-body evidence, M6 through-hole geometry, and the same unresolved stainless screw/washer boundary. DN16 versus DN40 filename context and different BOM quantities are standard interface variants and do not require separate closure items at merge review."
  proposed_closure_items:
    - item_id: ream250_iso_kf_aluminum_pratze_clamp_body_v0
      member_rows:
        - 313
        - 323
      functional_purpose: "clamp an ISO-KF flange or fitting against a baseplate or mating support"
      material: aluminum_alloy_with_optional_stainless_m6_hardware
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.0056
          - 0.00562
        bom_quantity_range:
          - 8
          - 16
        row_total_mass_range_kg:
          - 0.045
          - 0.0896
        nominal_interfaces:
          - DN16_ISO_KF
          - DN40_ISO_KF
          - DN10_DN50_vendor_family
        scale_class: tiny
      geometry_form: compact_l_shaped_iso_kf_pratze_claw_clamp_body_with_m6_through_hole
      process_family: general_subtractive_machining
material_review:
  can_unify: true
  rationale: "Both rows resolve to an aluminum cast clamp body from the Wissel ISO-KF Pratze product family and reject local Generic STEP material metadata as placeholder. Both also note possible stainless M6 screw and washer hardware if the complete vendor set is modeled, so material can unify as an aluminum body with optional separate stainless hardware guardrails."
process_review:
  can_unify: true
  rationale: "Row 313 selects general_subtractive_machining and row 323 selects metal additive with finish machining as a lunarized substitute for casting. The underlying closure operations are compatible: fabricate a small aluminum clamp body, drill or finish the M6 through hole, machine contact faces if needed, deburr, inspect, and optionally assemble with reusable stainless M6 screw and washer items. For this merged staged item, general_subtractive_machining is the simpler shared process family, while additive manufacture can remain an alternate Phase 3 note if local stock or tooling assumptions change."
geometry_review:
  can_unify: true
  rationale: "The two CAD rows have the same measured volume and bounding box and both describe a compact L-shaped or claw-like Pratze body with one through hole. DN16 and DN40 row names are interface-use variants within the same DN10-DN50 vendor family rather than distinct closure geometry families; Phase 3 should preserve nominal interface and quantity in BOM mappings."
precision_review:
  blocks_merge: false
  rationale: "Clamp contact geometry, hole diameter and position, flange-standard fit, clamping force, and seal load path remain guardrails. Neither row identifies a unique tolerance, surface finish, or sealing precision requirement that blocks one shared staged clamp-body abstraction."
assumptions:
  - "The proposed closure item represents the CAD-modeled aluminum clamp body, not necessarily the complete delivered Pratze set."
  - "M6 screw and washer hardware can map to reusable fastener items if Phase 3 models the complete clamp assembly."
  - "Existing broad fastener, fitting, hose-fitting, and vacuum-seal KB items are too generic to preserve the ISO-KF Pratze hold-down function and body/hardware boundary, so the item_id is a staging suggestion rather than immediate KB creation."
  - "Final import/local manufacture remains deferred to Phase 3."
unresolved:
  - "Exact Wissel article/SKU, stainless-versus-aluminum body variant, and delivered set contents are not fully locked."
  - "Required clamp contact tolerance, surface finish, clamping-force specification, and vacuum flange seal-load acceptance remain unresolved."
  - "Phase 3 should decide whether to stage this as body-only, complete clamp body plus M6 screw and washer set, or reuse an existing KB abstraction with row-specific guardrails."
  - "Per-row BOM mapping must preserve row 313 as quantity 16 with DN40 filename context and row 323 as quantity 8 with DN16 filename context."
---

# Merge Review

Rows 313 and 323 merge into one staged ISO-KF aluminum Pratze clamp-body abstraction. Preserve DN context, BOM quantity, body-only mass basis, and the optional stainless M6 screw/washer boundary for Phase 3.
