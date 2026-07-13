---
group_id: ream250_kb_merge_0026_plumbing_connection
candidate_rows:
  - source_row_number: 121
    item: "3J"
    path: research/ream250_bom/ream250_bom_row_0121_3J.md
    conversion_section_present: true
  - source_row_number: 118
    item: "3G"
    path: research/ream250_bom/ream250_bom_row_0118_3G.md
    conversion_section_present: true
  - source_row_number: 112
    item: "3A"
    path: research/ream250_bom/ream250_bom_row_0112_3A.md
    conversion_section_present: true
  - source_row_number: 138
    item: "3Q1"
    path: research/ream250_bom/ream250_bom_row_0138_3Q1.md
    conversion_section_present: true
  - source_row_number: 255
    item: "39"
    path: research/ream250_bom/ream250_bom_row_0255_39.md
    conversion_section_present: true
  - source_row_number: 139
    item: "3Q2"
    path: research/ream250_bom/ream250_bom_row_0139_3Q2.md
    conversion_section_present: true
  - source_row_number: 123
    item: "3L"
    path: research/ream250_bom/ream250_bom_row_0123_3L.md
    conversion_section_present: true
  - source_row_number: 339
    item: "426"
    path: research/ream250_bom/ream250_bom_row_0339_426.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0121_3J.md
    - research/ream250_bom/ream250_bom_row_0118_3G.md
    - research/ream250_bom/ream250_bom_row_0112_3A.md
    - research/ream250_bom/ream250_bom_row_0138_3Q1.md
    - research/ream250_bom/ream250_bom_row_0255_39.md
    - research/ream250_bom/ream250_bom_row_0139_3Q2.md
    - research/ream250_bom/ream250_bom_row_0123_3L.md
    - research/ream250_bom/ream250_bom_row_0339_426.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0121_3J.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0118_3G.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0112_3A.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0138_3Q1.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0255_39.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0139_3Q2.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0123_3L.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0339_426.md#kb-conversion
  notes: "Read every candidate row's frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview and geometry evidence in the row research were used where available; rows with unavailable previews were compared using STEP dimensions, product identity, and conversion guardrails."
rough_match_basis:
  functional_purpose_key: plumbing_connection
  mass_window_kg:
    - 0.914
    - 1.74
merge_decision:
  decision: partial_merge
  rationale: "The rough pool correctly groups stainless ISO-K vacuum plumbing connectors in the same mass range, and all rows share the plumbing_connector_fabrication_testing process family. A single all-rows closure item would hide rigid versus flexible behavior, straight versus elbow geometry, DN63 versus DN100 interface tooling, and length or motion guardrails. Rows 121 and 255 should merge as DN63 straight full-nipple variants, and rows 118 and 123 should merge as DN63 flexible bellows or corrugated hose variants. Rows 138, 112, 139, and 339 stay separate staged items because their nominal diameter and geometry form are closure-relevant."
  proposed_closure_items:
    - item_id: ream250_dn63_iso_k_straight_full_nipple_v0
      member_rows:
        - 121
        - 255
      functional_purpose: "rigid straight flanged connection section between DN63 ISO-K vacuum plumbing components"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg_range:
          - 0.914
          - 1.62
        bom_quantity_range:
          - 1
          - 2
        row_total_mass_range_kg:
          - 1.62
          - 1.828
        nominal_interface: DN63_ISO-K
        length_guardrail_mm:
          - 88
          - 214
        scale_class: medium
      geometry_form: straight_hollow_cylindrical_tube_with_iso_k_flanged_ends
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn100_iso_k_straight_full_nipple_v0
      member_rows:
        - 138
      functional_purpose: "rigid straight flanged connection section between DN100 ISO-K vacuum plumbing components"
      material: stainless_steel_1_4301_304
      scale_or_capacity:
        per_unit_mass_kg: 1.55
        bom_quantity: 1
        row_total_mass_kg: 1.55
        nominal_interface: DN100_ISO-K
        length_mm: 108
        scale_class: medium
      geometry_form: straight_hollow_cylindrical_tube_with_iso_k_flanged_ends
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn63_iso_k_90_degree_elbow_v0
      member_rows:
        - 112
      functional_purpose: "turn a DN63 ISO-K vacuum plumbing line through a right angle"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.999
        bom_quantity: 15
        row_total_mass_kg: 14.98
        nominal_interface: DN63_ISO-K
        angle_deg: 90
        scale_class: medium
      geometry_form: ninety_degree_flanged_pipe_elbow
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn100_iso_k_90_degree_elbow_v0
      member_rows:
        - 139
      functional_purpose: "turn a DN100 ISO-K vacuum plumbing line through a right angle"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 1.67
        bom_quantity: 1
        row_total_mass_kg: 1.67
        nominal_interface: DN100_ISO-K
        angle_deg: 90
        scale_class: medium
      geometry_form: ninety_degree_flanged_pipe_elbow
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn63_iso_k_flexible_bellows_connector_v0
      member_rows:
        - 118
        - 123
      functional_purpose: "compliant flexible DN63 ISO-K vacuum plumbing connection that tolerates routing offset, vibration, and limited motion"
      material: stainless_steel_304_flanges_with_316l_bellows
      scale_or_capacity:
        per_unit_mass_kg_range:
          - 0.929
          - 1.697
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 0.929
          - 1.697
        nominal_interface: DN63_ISO-K
        length_guardrail_mm:
          - 130
          - 750
        axial_stroke_mm: "+/-16 for row 118; row 123 unresolved"
        scale_class: medium
      geometry_form: corrugated_flexible_bellows_or_hose_with_iso_k_flanged_ends
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn100_iso_k_flexible_bellows_connector_v0
      member_rows:
        - 339
      functional_purpose: "compliant flexible DN100 ISO-K vacuum and powder path connection between rigid machine components"
      material: stainless_steel_304_flanges_with_316l_bellows
      scale_or_capacity:
        per_unit_mass_kg: 1.74
        bom_quantity: 1
        row_total_mass_kg: 1.74
        nominal_interface: DN100_ISO-K
        length_mm: 250
        scale_class: medium
      geometry_form: corrugated_flexible_bellows_hose_with_iso_k_flanged_ends
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: true
  rationale: "All rows are stainless vacuum plumbing hardware at the closure-family level. Rigid nipples and elbows normalize to 304 or 1.4301/304, while flexible rows use 304/1.4301 flanges with 316L bellows. This supports one stainless plumbing fabrication material family for process review, while the exact grade split remains a staging guardrail for flexible bellows connectors."
process_review:
  can_unify: true
  rationale: "Every row conversion selected plumbing_connector_fabrication_testing with supporting cutting, forming, joining, precision machining, cleaning, leak testing, and dimensional inspection. The shared process family is valid for closure planning, but it should not collapse rigid nipples, elbows, and flexible bellows into one item because geometry and interface guardrails remain distinct."
geometry_review:
  can_unify: false
  rationale: "The pool contains three geometry classes: straight full nipples, 90-degree elbows, and flexible corrugated bellows or hose connectors. Rows 121 and 255 share a DN63 straight-nipple geometry with length variation, and rows 118 and 123 share a DN63 flexible-bellows connector geometry with length and stroke variation. DN100 straight, DN63 elbow, DN100 elbow, and DN100 flexible hose should remain separate staged items."
precision_review:
  blocks_merge: true
  rationale: "Precision guardrails block a single all-rows merge. ISO-K nominal diameter, flange sealing face finish, flange coaxiality, elbow bend geometry, hose length, bellows flexibility, axial stroke, cleanliness, and leak-tightness must stay attached to the staged item and BOM mapping. These guardrails do not block the narrower DN63 straight-nipple merge or the DN63 flexible-connector merge."
assumptions:
  - "Existing KB items such as piping_and_fittings_set, pipe_and_fittings_set, piping_components, metal_fittings_raw, hose_fittings, hydraulic_hose_assembly, gas_loop_piping_set, and plumbing_system_assembly were considered as conservative reuse context; they are too broad or differently scoped to preserve ISO-K nominal interfaces, length, bellows compliance, quantities, and high-vacuum leak guardrails for these reAM250 rows."
  - "Rows 121 and 255 are treated as DN63 ISO-K full-nipple variants despite the catalog-versus-CAD length mismatch noted for row 255; length remains a staging guardrail."
  - "Rows 118 and 123 are treated as DN63 flexible stainless bellows/hose variants because both use ISO-K DN63 flanges, stainless 304/316L construction, flexible corrugated geometry, and leak-test requirements."
  - "DN63 and DN100 variants are not merged across nominal diameter in this review because later KB staging needs explicit interface tooling, fit, and BOM mapping."
  - "Proposed item IDs are staging suggestions only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Exact ISO-K flange tolerances, sealing-face roughness, passivation and cleanliness requirements, weld procedures, and helium leak-rate thresholds remain unresolved."
  - "Row 255's catalog length and CAD length differ; staging should preserve the CAD-derived 214 mm length unless layout review resolves the mismatch."
  - "Flexible connector rows still need bellows wall thickness, convolution geometry, forming method, weld qualification, cleaning process, and leak-test acceptance limits."
  - "Later KB staging should decide whether any proposed item should reuse a broad existing piping or fittings set while preserving row-specific quantity, nominal interface, material, mass, length, flexibility, and precision guardrails."
  - "Final local manufacture versus import decisions are deferred for all proposed closure items."
---

# Merge Review

Partial merge. Merge rows 121 and 255 as DN63 ISO-K straight full-nipple variants, and rows 118 and 123 as DN63 ISO-K flexible bellows connector variants. Keep rows 138, 112, 139, and 339 as separate staged connector items because nominal diameter, rigid/flexible behavior, elbow geometry, length, and leak-tightness guardrails are closure-relevant.
