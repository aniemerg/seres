---
group_id: ream250_kb_merge_0017_joint_sealing
candidate_rows:
  - source_row_number: 330
    item: "332"
    path: research/ream250_bom/ream250_bom_row_0330_332.md
    conversion_section_present: true
  - source_row_number: 144
    item: "3R2"
    path: research/ream250_bom/ream250_bom_row_0144_3R2.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0330_332.md
    - research/ream250_bom/ream250_bom_row_0144_3R2.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0330_332.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0144_3R2.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD preview evidence was checked for both rows; both previews show the same thin annular DN63 ISO-K centering-ring seal geometry with about 79.3 x 79.3 x 8.0 mm visual bounding box."
rough_match_basis:
  functional_purpose_key: joint_sealing
  mass_window_kg:
    - 0.0123
    - 0.013
merge_decision:
  decision: merge
  rationale: "Rows 330 and 144 should converge to one closure item. Both rows cite the same Pfeiffer product/order number 311ZRA063, same DN63 ISO-K centering and sealing function, same aluminum ring with NBR O-ring material stack, same STEP-derived volume, matching CAD geometry, and nearly identical per-unit mass estimates. The row-conversion difference between simple_part and decompose_into_parts is a staging granularity issue for mixed aluminum/elastomer closure, not a blocker to merging these duplicate BOM references."
  proposed_closure_items:
    - item_id: ream250_dn63_iso_k_centering_ring_seal_v0
      member_rows:
        - 330
        - 144
      functional_purpose: "center and seal a DN63 ISO-K flanged gas-line joint with an annular locating ring and elastomer sealing element"
      material: aluminum_outer_ring_with_nbr_o_ring
      scale_or_capacity:
        per_unit_mass_kg_range:
          - 0.0123
          - 0.013
        bom_quantities_by_row:
          "330": 44
          "144": 1
        row_total_mass_kg_by_row:
          "330": 0.541
          "144": 0.013
        nominal_interface: DN63_ISO-K
        visual_bounding_box_mm: "79.3 x 79.3 x 8.0"
        catalog_dimensions_mm:
          A: 70
          B: 68
          C: 3.9
          D: 8
          E: 5.33
        scale_class: small
      geometry_form: thin_annular_centering_ring_with_integrated_elastomer_o_ring
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: true
  rationale: "Both rows have row-matched evidence for aluminum media-contact/outer-ring material and an NBR O-ring on Pfeiffer 311ZRA063. The aluminum alloy grade and aluminum-to-NBR volume split remain unresolved, but those unknowns are shared by both rows and can be carried on one staged item."
process_review:
  can_unify: true
  rationale: "Both conversions select plumbing_connector_fabrication_testing as the primary closure bucket. The shared process chain is aluminum ring forming or machining, deburring, cleaning, O-ring installation, dimensional inspection, and leak-test context. Existing anchors such as machining_basic_v0, elastomer_molding_basic_v0, seal_installation_v0, leak_testing_v0, cleaning_basic_v0, and inspection_basic_v0 remain supporting candidates for Phase 3."
geometry_review:
  can_unify: true
  rationale: "The rows are not merely similar; they reference the same STEP-derived geometry and the CAD previews are visually identical. Both are thin annular DN63 ISO-K centering-ring seals with the same about 8 mm thickness and matching ring profile."
precision_review:
  blocks_merge: false
  rationale: "Both rows carry the same precision needs: DN63 ISO-K flange fit, concentricity, O-ring seating, sealing-surface finish, cleanliness, compression geometry, and leak-tightness after installation. These guardrails are important for staging, but they do not distinguish the two rows."
assumptions:
  - "Rows 330 and 144 are duplicate BOM references to the same catalog part, not two different seal designs."
  - "The row 330 quantity of 44 and row 144 quantity of 1 should remain separate BOM mapping quantities even though the closure item is shared."
  - "Existing KB items such as seal_o_ring_rubber and vacuum_seal_assembly are relevant conservative reuse checks for Phase 3, but neither alone captures the DN63 ISO-K aluminum centering ring plus NBR O-ring interface without preserving additional guardrails."
  - "Proposed item ID is a staging suggestion only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Phase 3 should decide whether to stage this as one assembled centering-ring seal item with subpart assumptions, decompose it into aluminum centering ring plus NBR O-ring mappings, and how to preserve the row-specific BOM quantities."
  - "Exact aluminum alloy, NBR compound details beyond the material family, aluminum-to-NBR mass split, seal compression specification, and leak-rate acceptance remain unresolved."
  - "Phase 3 should decide whether a close existing KB abstraction can be reused while retaining DN63 ISO-K nominal interface, mixed-material construction, and vacuum/flange sealing guardrails."
---

# Merge Review

Merge rows 330 and 144 into one DN63 ISO-K centering-ring seal closure item. They are the same Pfeiffer 311ZRA063 aluminum/NBR annular seal, with quantity differences preserved for later BOM mapping.
