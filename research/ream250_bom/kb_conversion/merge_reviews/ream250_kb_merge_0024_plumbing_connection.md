---
group_id: ream250_kb_merge_0024_plumbing_connection
candidate_rows:
  - source_row_number: 164
    item: "3X1"
    path: research/ream250_bom/ream250_bom_row_0164_3X1.md
    conversion_section_present: true
  - source_row_number: 132
    item: "3P2"
    path: research/ream250_bom/ream250_bom_row_0132_3P2.md
    conversion_section_present: true
  - source_row_number: 250
    item: "34"
    path: research/ream250_bom/ream250_bom_row_0250_34.md
    conversion_section_present: true
  - source_row_number: 283
    item: "87"
    path: research/ream250_bom/ream250_bom_row_0283_87.md
    conversion_section_present: true
  - source_row_number: 341
    item: "428"
    path: research/ream250_bom/ream250_bom_row_0341_428.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0164_3X1.md
    - research/ream250_bom/ream250_bom_row_0132_3P2.md
    - research/ream250_bom/ream250_bom_row_0250_34.md
    - research/ream250_bom/ream250_bom_row_0283_87.md
    - research/ream250_bom/ream250_bom_row_0341_428.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0164_3X1.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0132_3P2.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0250_34.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0283_87.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0341_428.md#kb-conversion
  notes: "Read every candidate row's frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence in the row research was used to compare the compact DN40 valve-body component, annular DN63 ISO-K weld ring, short DN50 ISO-KF spring bellows, DN40-to-DN16 ISO-KF reducing tee, and straight DN40 ISO-KF full nipple."
rough_match_basis:
  functional_purpose_key: plumbing_connection
  mass_window_kg:
    - 0.173
    - 0.325
merge_decision:
  decision: split
  rationale: "The rough pool correctly groups small stainless gas/vacuum plumbing hardware, but none of these rows is an interchangeable duplicate. The group spans a moving valve body, a DN63 ISO-K weld-ring flange, a flexible DN50 bellows connector, a DN40-to-DN16 reducing tee, and a straight DN40 full nipple. Nominal interface, geometry, compliance, branch topology, and valve sealing role are closure-relevant guardrails, so forcing one closure item would hide real manufacturing and staging differences."
  proposed_closure_items:
    - item_id: ream250_dn40_manual_disc_valve_body_component_v0
      member_rows:
        - 164
      functional_purpose: "valve body component for manually closing a DN40 machine flow path"
      material: stainless_steel_316l_with_valve_level_epdm_context
      scale_or_capacity:
        per_unit_mass_kg: 0.173
        bom_quantity: 1
        row_total_mass_kg: 0.173
        nominal_interface: DN40_ISO-KF
        scale_class: small
      geometry_form: compact_bored_cylindrical_valve_body_with_external_lugs
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn63_iso_k_weld_ring_flange_v0
      member_rows:
        - 132
      functional_purpose: "weld-ring flange joining a service tube to a DN63 ISO-K plumbing line interface"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.247
        bom_quantity: 2
        row_total_mass_kg: 0.494
        nominal_interface: DN63_ISO-K
        tube_dimension_mm: "76.1 x 3"
        scale_class: small
      geometry_form: annular_weld_ring_flange
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn50_iso_kf_flexible_bellows_connector_v0
      member_rows:
        - 250
      functional_purpose: "flexible short plumbing connector for DN50 gas and vacuum line compliance"
      material: stainless_steel_304_and_316l
      scale_or_capacity:
        per_unit_mass_kg: 0.3
        bom_quantity: 2
        row_total_mass_kg: 0.6
        nominal_interface: DN50_ISO-KF
        length_mm: 60
        axial_stroke_mm: "+/-6.5"
        scale_class: small
      geometry_form: short_corrugated_bellows_with_iso_kf_dn50_flange_ends
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn40_to_dn16_iso_kf_reducing_tee_v0
      member_rows:
        - 283
      functional_purpose: "connect a larger small-flange gas line to a reduced branch line"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.32
        bom_quantity: 1
        row_total_mass_kg: 0.32
        nominal_interfaces:
          - DN40_ISO-KF
          - DN16_ISO-KF
        scale_class: small
      geometry_form: reducing_tee_tube_with_kf_lipped_interfaces
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn40_iso_kf_full_nipple_v0
      member_rows:
        - 341
      functional_purpose: "short flanged pipe section connecting KF-compatible line components while preserving a clean leak-tight gas path"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.325
        bom_quantity: 1
        row_total_mass_kg: 0.325
        nominal_interface: DN40_ISO-KF
        length_mm: 130
        scale_class: small
      geometry_form: straight_flanged_tube_full_nipple
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: false
  rationale: "Rows 132, 283, and 341 normalize to stainless_steel_304. Row 250 is a mixed 304 flange and 316L bellows assembly, and row 164 is a 316L valve body with EPDM retained as valve-level sealing context. Stainless families are close enough for process comparison, but the EPDM valve context and bellows alloy split should not be collapsed into one material identity for staging."
process_review:
  can_unify: true
  rationale: "All five conversions select plumbing_connector_fabrication_testing with supporting machining/forming/joining/cleaning/leak-test work. That shared process family is appropriate for closure planning, but process unification does not make the rows interchangeable because the connector standard, moving valve role, bellows compliance, and tee branch geometry differ."
geometry_review:
  can_unify: false
  rationale: "The geometries are different functional classes: compact bored valve body with lugs, annular weld-ring flange, corrugated flexible bellows, reducing tee with branch, and straight full nipple. These differences change manufacturing steps, BOM mapping, and installation interfaces."
precision_review:
  blocks_merge: true
  rationale: "Sealing surface finish, leak tightness, interface dimensions, branch alignment, axial compliance, valve bore/detent fit, and EPDM allocation block a single closure item. The guardrails can be preserved in singleton staged items and revisited later only if staging chooses a broader ISO vacuum fittings kit abstraction."
assumptions:
  - "Existing KB abstractions such as piping_and_fittings_set, pipe_and_fittings_set, piping_and_valves_set, fittings_and_valves, valve_components_kit, valve_body_machined, and metal_fittings_raw were considered as conservative equivalents; they are useful coarse context but too broad to preserve row-specific ISO-K/KF sizes, valve/bellows behavior, and high-vacuum guardrails for these rows."
  - "The prior merge review ream250_kb_merge_0025_plumbing_connection is relevant precedent: it split non-duplicate vacuum connector geometries and merged only true duplicate bellows end fittings."
  - "Proposed item IDs are staging suggestions only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
  - "Vacuum service is treated as sealing, cleanliness, and leak-test guardrails rather than as a functional-purpose key axis."
unresolved:
  - "Exact ISO-K/KF flange tolerances, sealing-face roughness, passivation/cleanliness requirements, weld procedures, and helium leak-rate thresholds remain unresolved."
  - "Row 164's EPDM allocation across the two-part valve assembly, detent geometry, and leak/closure performance remain unresolved."
  - "Row 250's exact catalog mass, bellows forming method, weld qualification, and leak-test procedure remain unresolved."
  - "Later KB staging should decide whether any of these should reuse a broad existing piping or valve kit while preserving row-specific quantity, nominal interface, material, and precision guardrails."
  - "Final local manufacture versus import decisions are deferred for all proposed closure items."
---

# Merge Review

Split all five rows into separate staged plumbing connector items. They share a broad stainless plumbing fabrication and leak-test process family, but their geometry, nominal interface, valve/bellows behavior, and precision guardrails are not interchangeable.
