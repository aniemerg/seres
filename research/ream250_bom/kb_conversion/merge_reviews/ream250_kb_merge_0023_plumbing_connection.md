---
group_id: ream250_kb_merge_0023_plumbing_connection
candidate_rows:
  - source_row_number: 315
    item: "195"
    path: research/ream250_bom/ream250_bom_row_0315_195.md
    conversion_section_present: true
  - source_row_number: 319
    item: "272"
    path: research/ream250_bom/ream250_bom_row_0319_272.md
    conversion_section_present: true
  - source_row_number: 114
    item: "3C"
    path: research/ream250_bom/ream250_bom_row_0114_3C.md
    conversion_section_present: true
  - source_row_number: 207
    item: "8B"
    path: research/ream250_bom/ream250_bom_row_0207_8B.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0315_195.md
    - research/ream250_bom/ream250_bom_row_0319_272.md
    - research/ream250_bom/ream250_bom_row_0114_3C.md
    - research/ream250_bom/ream250_bom_row_0207_8B.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0315_195.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0319_272.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0114_3C.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0207_8B.md#kb-conversion
  notes: "Read every candidate row's frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence in the row research was used to compare the shallow DN40 blind flange disk, slender fluid feedthrough, DN63 ISO-K to DN40 ISO-KF reducer tee, and DN40 ISO-KF right-angle elbow."
rough_match_basis:
  functional_purpose_key: plumbing_connection
  mass_window_kg:
    - 0.0744
    - 0.141
merge_decision:
  decision: split
  rationale: "The rough pool correctly groups small vacuum plumbing hardware that shares fabrication, cleaning, and leak-test concerns, but the rows are not interchangeable closure items. The group spans a blind termination cap, a through-boundary fluid feedthrough, a reducer tee between two flange standards, and a right-angle elbow. Those geometries, nominal interfaces, and service guardrails change BOM mapping and staging enough that a single closure item would hide real design constraints."
  proposed_closure_items:
    - item_id: ream250_dn40_iso_kf_blind_flange_v0
      member_rows:
        - 315
      functional_purpose: "close an unused DN40 ISO-KF vacuum port while preserving a clamped seal interface"
      material: corrosion_resistant_metal_variant_unresolved
      scale_or_capacity:
        per_unit_mass_kg: 0.0744
        bom_quantity: 2
        row_total_mass_kg: 0.149
        nominal_interface: DN40_ISO-KF
        scale_class: small
      geometry_form: shallow_round_iso_kf_dn40_blind_flange_disk
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_small_fluid_feedthrough_v0
      member_rows:
        - 319
      functional_purpose: "pass a service fluid line through a chamber boundary with a sealed interface"
      material: stainless_steel_assumed
      scale_or_capacity:
        per_unit_mass_kg: 0.093
        bom_quantity: 1
        row_total_mass_kg: 0.093
        approximate_envelope_mm: "32.47 x 32.47 x 176"
        scale_class: small
      geometry_form: slender_tube_feedthrough_with_end_fittings_and_central_collar
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn63_iso_k_to_dn40_iso_kf_reducer_tee_v0
      member_rows:
        - 114
      functional_purpose: "connect a DN63 ISO-K vacuum line to a reduced DN40 ISO-KF branch"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.1164
        bom_quantity: 2
        row_total_mass_kg: 0.2328
        nominal_interfaces:
          - DN63_ISO-K
          - DN40_ISO-KF
        scale_class: small
      geometry_form: reduced_iso_k_to_iso_kf_flanged_tube_fitting
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn40_iso_kf_90_degree_elbow_v0
      member_rows:
        - 207
      functional_purpose: "turn a DN40 ISO-KF vacuum line through a right angle while preserving clamp-flange interfaces"
      material: aluminum_6082
      scale_or_capacity:
        per_unit_mass_kg: 0.141
        bom_quantity: 5
        row_total_mass_kg: 0.707
        nominal_interface: DN40_ISO-KF
        scale_class: small
      geometry_form: ninety_degree_elbow_with_integral_dn40_iso_kf_flanges
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: false
  rationale: "The rows do not share one material identity: row 315 is unresolved among stainless and aluminum Wissel blind-flange variants, row 319 assumes stainless feedthrough construction, row 114 has stainless steel 304 evidence, and row 207 has aluminum EN AW-6082 evidence. These materials can share high-level plumbing fabrication review, but staging should preserve row-specific alloy and uncertainty."
process_review:
  can_unify: true
  rationale: "All four conversions select plumbing_connector_fabrication_testing as the primary closure bucket, with supporting machining, cleaning, inspection, and leak or pressure testing. The shared process family is useful for closure planning, but it does not imply one reusable item because the blind cap, feedthrough, reducer tee, and elbow require different fabrication details and interfaces."
geometry_review:
  can_unify: false
  rationale: "The geometry forms are different functional classes: a shallow blind disk, a slender through-boundary tube feedthrough, a reduced tee with two flange standards, and a right-angle elbow. These are not length, material, or minor-size variants of one part."
precision_review:
  blocks_merge: true
  rationale: "Leak tightness, sealing-face finish, clamp-interface geometry, fluid feedthrough pressure rating, tube bore, branch alignment, reducer interface standards, and elbow passage continuity block a single closure item. These guardrails should remain attached to separate staged items unless a later stage deliberately chooses a broad vacuum fittings kit abstraction."
assumptions:
  - "Existing KB abstractions such as piping_and_fittings_set, pipe_and_fittings_set, piping_and_valves_set, fittings_and_valves, hose_fittings, coolant_piping, metal_fittings_raw, and electrical_feedthrough_vacuum were considered as conservative reuse context; they are too broad or differently scoped to preserve these row-specific ISO-K/KF interfaces, feedthrough role, quantities, materials, and leak-test guardrails."
  - "The prior plumbing merge reviews in this directory are relevant precedent: they split non-duplicate vacuum connector geometries and merged only true duplicate or near-duplicate fitting rows."
  - "Proposed item IDs are staging suggestions only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
  - "Vacuum service is preserved as sealing, cleanliness, pressure, and leak-test guardrails rather than as a functional-purpose key axis."
unresolved:
  - "Exact ISO-K/KF flange tolerances, sealing-face roughness, passivation and cleanliness requirements, weld procedures, and leak-rate thresholds remain unresolved for local manufacturing models."
  - "Row 315's exact Wissel article suffix and material grade remain unresolved."
  - "Row 319's fluid type, tube bore, fitting standard, seal material, pressure rating, and leak-rate target remain unresolved."
  - "Row 114 has a CAD-to-datasheet size mismatch; exact wall thickness, reducer tee geometry, and weld acceptance criteria remain unresolved."
  - "Row 207's commercial manufacturing route, surface treatment, cleaning specification, and leak-rate criterion remain unresolved."
  - "Later KB staging should decide whether any proposed item should reuse a broad piping/fittings kit while preserving source quantities, nominal interfaces, material, and precision guardrails."
  - "Final local manufacture versus import decisions are deferred for all proposed closure items."
---

# Merge Review

Split all four rows into separate staged plumbing connector items. They share a plumbing connector fabrication and leak-test process family, but the blind flange, fluid feedthrough, reducer tee, and 90-degree elbow are different closure items with distinct interfaces and precision guardrails.
