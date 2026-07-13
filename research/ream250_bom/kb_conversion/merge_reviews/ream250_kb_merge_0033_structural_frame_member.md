---
group_id: ream250_kb_merge_0033_structural_frame_member
candidate_rows:
  - source_row_number: 233
    item: "17AE"
    path: research/ream250_bom/ream250_bom_row_0233_17AE.md
    conversion_section_present: true
  - source_row_number: 272
    item: "66"
    path: research/ream250_bom/ream250_bom_row_0272_66.md
    conversion_section_present: true
  - source_row_number: 371
    item: "1765"
    path: research/ream250_bom/ream250_bom_row_0371_1765.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0233_17AE.md
    - research/ream250_bom/ream250_bom_row_0272_66.md
    - research/ream250_bom/ream250_bom_row_0371_1765.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0233_17AE.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0272_66.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0371_1765.md#kb-conversion
  notes: "Read each candidate row's original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. Also inspected the referenced CAD preview PNGs: row 233 is a 604 mm long 20x20 slotted aluminum profile, row 371 is a 150 mm long 40x40 T-slot aluminum profile, and row 272 is a thin irregular machined Aluminum 6061 support plate with pockets, cutouts, and mounting/interface features."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 0.2416
    - 0.4477
merge_decision:
  decision: partial_merge
  rationale: "The rough pool correctly finds small aluminum structural members, but it combines two different closure families. Rows 233 and 371 are commercial-style modular slotted extrusion cut lengths with the same structural profile stock fabrication route, anodized aluminum material family, and length/slot/squareness guardrails, so they can share one generic cut slotted aluminum structural profile abstraction. Row 272 is a custom machined front support plate for recoater or conveyor hardware; its plate geometry, pockets, holes, bearing or shaft alignment risks, and subtractive machining process should remain a separate closure item."
  proposed_closure_items:
    - item_id: ream250_cut_slotted_aluminum_structural_profile_v0
      member_rows:
        - 233
        - 371
      functional_purpose: "provide modular aluminum structural frame members and attachment spacers"
      material: anodized_aluminum_alloy_6060_6063_family
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.2416
          - 0.4477
        bom_quantity_range:
          - 2
          - 2
        row_total_mass_range_kg:
          - 0.4832
          - 0.895
        profile_sizes_mm:
          - 20x20
          - 40x40
        cut_lengths_mm:
          - 604
          - 150
        scale_class: small
      geometry_form: cut_slotted_t_slot_aluminum_profile_segment
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_recoater_machined_aluminum_support_plate_v0
      member_rows:
        - 272
      functional_purpose: "support recoater or conveyor-side shafts, belt, guide, or bearing hardware as a front structural end plate"
      material: aluminum_6061
      scale_or_capacity:
        per_unit_mass_kg: 0.327
        bom_quantity: 3
        row_total_mass_kg: 0.982
        envelope_mm: "136 x 178.5 x 10"
        scale_class: small
      geometry_form: thin_irregular_machined_plate_with_pockets_cutouts_and_mounting_features
      process_family: general_subtractive_machining
material_review:
  can_unify: false
  rationale: "Rows 233 and 371 can unify as anodized aluminum structural profile alloy family items, with exact Bosch/Rexroth article and temper unresolved. Row 272 is Aluminum 6061 plate stock and lacks coating evidence. Aluminum as a broad class is shared, but the profile alloy/finish family and 6061 machined plate identity should remain separate for closure and BOM mapping."
process_review:
  can_unify: false
  rationale: "Rows 233 and 371 both use structural_profile_stock_fabrication_cutting with extrusion, anodizing or surface finishing, cut-to-length, deburring, and inspection. Row 272 uses general_subtractive_machining from plate stock with cutting, drilling, pocket machining, cleaning, and dimensional inspection. Those process routes are related aluminum fabrication work but not one closure process family for a single reusable item."
geometry_review:
  can_unify: false
  rationale: "Rows 233 and 371 are constant-section slotted extrusion segments whose differences are profile size and length variants. Row 272 is a flat irregular custom support plate with local pockets, holes, cutouts, and likely shaft/bearing or belt-guide interfaces. That geometry is not an extrusion cut-length variant."
precision_review:
  blocks_merge: true
  rationale: "Length, straightness, slot compatibility, and end squareness are manageable guardrails for the two extrusion rows. Row 272 adds hole-position accuracy, pocket depth, and shaft or bearing interface alignment concerns that would be hidden by a single structural-frame-member item, so precision and interface guardrails block a full-group merge."
assumptions:
  - "The project reuse rule supports merging 20x20 and 40x40 slotted aluminum profile segments as one staged profile family while preserving per-row profile size, cut length, mass, quantity, and slot-compatibility guardrails."
  - "Rows 233 and 371 should preserve their source quantities of two segments each; row 272 should preserve three identical plate instances as BOM quantity rather than separate item definitions."
  - "Existing broad KB notions for frames, aluminum stock, or structural members may be relevant in Phase 3, but this merge review does not write KB YAML and does not make the final reuse/import/local-manufacture decision."
  - "The proposed item IDs are staging suggestions only."
unresolved:
  - "Exact Bosch Rexroth article numbers, alloy tempers, anodizing specifications, slot standards, and end machining for rows 233 and 371 remain unresolved."
  - "For row 272, exact temper, coating, datums, critical holes, shaft or bearing interfaces, pocket tolerances, and surface finish remain unresolved."
  - "Phase 3 should search existing KB items for generic structural profiles, frame members, aluminum extrusion stock, and machined support plates before promoting either proposed item."
  - "Final local manufacture versus import decisions are deferred for both proposed closure items."
---

# Merge Review

Partially merge the group. Rows 233 and 371 become one staged cut slotted aluminum structural profile abstraction, with profile size and length retained in BOM mappings. Row 272 remains a separate staged machined Aluminum 6061 support plate because its custom plate geometry and interface precision guardrails do not fit the extrusion profile item.
