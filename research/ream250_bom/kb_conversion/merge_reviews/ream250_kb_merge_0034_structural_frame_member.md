---
group_id: ream250_kb_merge_0034_structural_frame_member
candidate_rows:
  - source_row_number: 288
    item: "91C"
    path: research/ream250_bom/ream250_bom_row_0288_91C.md
    conversion_section_present: true
  - source_row_number: 33
    item: "2AA"
    path: research/ream250_bom/ream250_bom_row_0033_2AA.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0288_91C.md
    - research/ream250_bom/ream250_bom_row_0033_2AA.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0288_91C.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0033_2AA.md#kb-conversion
  notes: "Read both candidate rows' original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. The row evidence separates a 200 mm mild-steel DIN 59370 equal L-angle profile cut length from a custom wedge-like Z-axis machined support plate with unresolved structural metal material."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 0.746
    - 1.13
merge_decision:
  decision: split
  rationale: "The rough structural-frame key and 2x mass window are useful for discovery, but the two rows do not converge to one closure item. Row 288 is standard mild-steel 50 x 50 x 5 mm equal angle stock cut to 200 mm, with quantity three and a structural_profile_stock_fabrication_cutting closure path. Row 33 is a monolithic handed Z-axis support plate or web with a 135 x 218.6 x 23 mm envelope, mounting-hole row, unresolved metal alloy, and a general_subtractive_machining closure path. Merging them would hide stock-form, material, geometry, process, and alignment guardrails that matter for Phase 3 staging."
  proposed_closure_items:
    - item_id: ream250_mild_steel_equal_l_angle_profile_50x50x5_v0
      member_rows:
        - 288
      functional_purpose: "provide a small structural bracket spacer stiffener or mounting member from cut angle stock"
      material: mild_steel
      scale_or_capacity:
        per_unit_mass_kg: 0.746
        bom_quantity: 3
        row_total_mass_kg: 2.24
        profile_size_mm: "50 x 50 x 5 equal L-angle"
        cut_length_mm: 200
        scale_class: small
      geometry_form: 50x50x5mm_equal_l_angle_profile_200mm_cut_length
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_z_axis_handed_machined_support_plate_v0
      member_rows:
        - 33
      functional_purpose: "brace and locate Z-axis guide bearing or side-plate hardware as a handed structural support"
      material: metal_alloy_unresolved
      scale_or_capacity:
        per_unit_mass_kg_aluminum_scenario: 1.13
        per_unit_mass_kg_steel_scenario: 3.28
        bom_quantity: 1
        row_total_mass_kg_aluminum_scenario: 1.13
        envelope_mm: "135 x 218.6 x 23"
        scale_class: medium
      geometry_form: wedge_like_machined_support_plate_with_mounting_hole_row
      process_family: general_subtractive_machining
material_review:
  can_unify: false
  rationale: "Row 288 has direct mild-steel evidence from STEP material extraction and a steel-profile standard context. Row 33 has placeholder STEP material metadata and only an engineering hypothesis that it is a structural metal component, with aluminum and steel both plausible mass scenarios. Even if row 33 later resolves to steel, it would still be a machined plate/web rather than a standard mild-steel angle-stock cut length."
process_review:
  can_unify: false
  rationale: "Row 288 uses structural profile stock fabrication and cutting: form or source equal steel angle, cut to length, deburr, and inspect. Row 33 uses custom subtractive fabrication from plate or billet: rough cutting, CNC milling of faces and wedge/web geometry, drilling or reaming the mounting-hole row, deburring, cleaning, and dimensional inspection. These are different closure handles rather than variants of one shared process family."
geometry_review:
  can_unify: false
  rationale: "Row 288 is a constant-section 50 x 50 x 5 mm L-angle profile segment with a 200 mm cut length. Row 33 is a one-off wedge-like support plate/web with a 135 x 218.6 x 23 mm envelope and a row of through holes on a narrow mounting face. Cut length and squareness variants for angle stock cannot cover the custom handed support-plate geometry."
precision_review:
  blocks_merge: true
  rationale: "Precision guardrails differ enough to block a single closure item. The angle profile needs cross-section, cut length, cut-end finish, and squareness control. The Z-axis support plate needs mounting-face flatness, hole-position accuracy, possible reamed/counterbored or threaded hole details, and Z-axis alignment guardrails. Those interface requirements should remain visible for staging."
assumptions:
  - "Row 288 is one of three identical 200 mm mild-steel angle-profile segments; quantity and row total mass should be preserved in downstream BOM mappings rather than creating separate item IDs per instance."
  - "Row 33 should later be compared with the right-hand support plate row and related Z-axis support plates before Phase 3 promotes a final closure item."
  - "Existing KB recipes for small steel frames or basic supports may provide process context, but no obvious existing KB item from the narrow search cleanly replaces either row-specific closure item at merge-review time."
  - "The proposed item IDs are Phase 2 staging suggestions only; final reuse, new item creation, import/local manufacture, and item naming decisions belong to Phase 3."
unresolved:
  - "Row 288 still lacks exact steel grade, profile tolerance class, surface finish, coating, load case, and installation location."
  - "Row 33 still lacks alloy family, grade, temper, surface treatment, threaded-hole or counterbore details, datum scheme, and exact Z-axis interface tolerances."
  - "Phase 3 should search existing KB items and staged outputs for reusable structural angle stock and generic machined support plates before promoting either proposed closure item."
  - "Final local manufacture versus import decisions are deferred for both proposed closure items."
---

# Merge Review

Split the group. Row 288 should remain a small mild-steel equal L-angle cut-stock closure item, while row 33 should remain a custom handed Z-axis machined support-plate closure item. Their rough functional key overlaps, but material certainty, stock form, process route, geometry, and precision guardrails do not.
