---
group_id: ream250_kb_merge_0016_joint_clamping
candidate_rows:
  - source_row_number: 285
    item: "89"
    path: research/ream250_bom/ream250_bom_row_0285_89.md
    conversion_section_present: true
  - source_row_number: 251
    item: "35"
    path: research/ream250_bom/ream250_bom_row_0251_35.md
    conversion_section_present: true
  - source_row_number: 258
    item: "41C"
    path: research/ream250_bom/ream250_bom_row_0258_41C.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0285_89.md
    - research/ream250_bom/ream250_bom_row_0251_35.md
    - research/ream250_bom/ream250_bom_row_0258_41C.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0285_89.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0251_35.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0258_41C.md#kb-conversion
  notes: "Read each candidate row's frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence in the row research was used to compare split or hinged annular ISO-KF clamp geometry, tightening hardware, and standard flange-fit guardrails."
rough_match_basis:
  functional_purpose_key: joint_clamping
  mass_window_kg:
    - 0.163
    - 0.265
merge_decision:
  decision: merge
  rationale: "All three rows are Pfeiffer-style stainless 304/1.4301 ISO-KF clamping rings for elastomer-sealed vacuum flange joints. They differ by nominal DN size, per-unit mass, BOM quantity, and small geometry details, but the function, material family, process abstraction, hardware form, and precision risks are close enough for one reusable staged closure item with DN variants preserved as guardrails."
  proposed_closure_items:
    - item_id: ream250_iso_kf_stainless_clamping_ring_v0
      member_rows:
        - 285
        - 251
        - 258
      functional_purpose: "clamp an elastomer-sealed ISO-KF flange joint in gas or vacuum plumbing"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.163
          - 0.265
        bom_quantity_range:
          - 1
          - 4
        row_total_mass_range_kg:
          - 0.163
          - 0.74
        nominal_interfaces:
          - DN_10_16_ISO_KF
          - DN_32_40_ISO_KF
          - DN_50_ISO_KF
        scale_class: small
      geometry_form: split_or_hinged_annular_iso_kf_clamp_ring_with_wingnut_tightening_hardware
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: true
  rationale: "Every row resolves to stainless steel 304 / EN 1.4301 from row-matched Pfeiffer product or datasheet evidence. Placeholder Generic material metadata in local STEP files was explicitly rejected in the research, so there is no material blocker to a shared stainless clamp-ring closure item."
process_review:
  can_unify: true
  rationale: "Rows 285 and 258 select plumbing_connector_fabrication_testing directly, while row 251 selects a metal additive route with finish machining. The underlying operations are compatible for staging: stainless clamp body fabrication, drilling/thread interfaces, deburring or passivation, assembly of hinge/screw/wingnut hardware, dimensional inspection, and acceptance in a leak-tested elastomer-sealed joint."
geometry_review:
  can_unify: true
  rationale: "All three rows are split or hinged annular ISO-KF clamp rings with tightening hardware. DN 10-16, DN 32-40, and DN 50 size differences affect interface guardrails and per-row BOM mapping, but they are standard size variants of the same closure abstraction rather than distinct machine-specific geometry families."
precision_review:
  blocks_merge: false
  rationale: "Flange fit, tightening torque, hinge or screw alignment, contact finish, cleanliness, and sealing performance must remain guardrails. None of the row evidence shows a unique precision requirement that forces separate closure items before Phase 3 staging."
assumptions:
  - "The staged closure item may represent size variants of ISO-KF clamp rings, with Phase 3 preserving each row's nominal DN interface, BOM quantity, and mass."
  - "Wingnut, screw, and hinge details can stay inside the clamp hardware item for this merge pass rather than becoming separate closure items."
  - "Existing broad fittings or fastener kit items are too generic to preserve ISO-KF clamp function and seal-loading guardrails, so the proposed item ID is a staging suggestion rather than immediate KB creation."
  - "Final import/local manufacture remains deferred; merge review only determines that these rows can share one staged closure abstraction."
unresolved:
  - "Exact factory production route, hinge pin and screw materials, passivation method, contact-surface requirements, ISO-KF tolerance class, and helium leak-rate acceptance remain unresolved."
  - "Phase 3 should search existing KB items again before promotion and decide whether this becomes a new local-manufacture candidate, a standard hardware import, or a mapping to an existing vacuum fittings abstraction."
  - "Per-row nominal interface mapping must preserve DN 10-16 for row 285, DN 50 for row 251, and DN 32-40 for row 258."
---

# Merge Review

Rows 285, 251, and 258 merge into one staged ISO-KF stainless clamping-ring abstraction. Preserve each row's DN size, quantity, mass, tightening hardware, and seal-loading guardrails for Phase 3 rather than creating row-specific clamp items.
