---
group_id: ream250_kb_merge_0039_structural_frame_support_member
candidate_rows:
  - source_row_number: 295
    item: "92"
    path: research/ream250_bom/ream250_bom_row_0295_92.md
    conversion_section_present: true
  - source_row_number: 359
    item: "915"
    path: research/ream250_bom/ream250_bom_row_0359_915.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0295_92.md
    - research/ream250_bom/ream250_bom_row_0359_915.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0295_92.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0359_915.md#kb-conversion
  notes: "Read both candidate rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. The CAD-derived dimensions and preview evidence were enough to distinguish a long 60 x 60 aluminum modular slotted strut from an 80 x 80 x 5 mild-steel square hollow structural section."
rough_match_basis:
  functional_purpose_key: structural_frame_support_member
  mass_window_kg:
    - 8.276
    - 9.13
merge_decision:
  decision: split
  rationale: "The rows share a broad frame-support role and a similar per-unit mass, but they should not converge to one closure item. Row 295 is a 2120 mm Bosch Rexroth-style 60 x 60 aluminum modular slotted strut with slot-interface guardrails. Row 359 is an 810 mm EN 10219-style 80 x 80 x 5 mild-steel welded square hollow section, BOM quantity 4, with structural tube guardrails. The material family, profile interface, cross-section, quantity context, and profile-stock route differ enough that a single closure item would hide real downstream choices."
  proposed_closure_items:
    - item_id: ream250_aluminum_structural_profile_60x60_v0
      member_rows:
        - 295
      functional_purpose: "modular machine-frame structural support member"
      material: aluminum_strut_profile_alloy_family
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 8.276
          - 8.276
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 8.276
          - 8.276
        profile_size_mm: "60 x 60"
        cut_length_variants_mm:
          - 2120
        scale_class: medium
      geometry_form: long_square_modular_slotted_profile_60x60_cut_to_length
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_steel_square_hollow_structural_profile_80x80_v0
      member_rows:
        - 359
      functional_purpose: "machine-frame structural support member"
      material: mild_steel_structural
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 9.13
          - 9.13
        bom_quantity_range:
          - 4
          - 4
        row_total_mass_range_kg:
          - 36.51
          - 36.51
        profile_size_mm: "80 x 80 x 5"
        cut_length_variants_mm:
          - 810
        scale_class: medium
      geometry_form: square_hollow_structural_profile_cut_to_length
      process_family: structural_profile_stock_fabrication_cutting
material_review:
  can_unify: false
  rationale: "Row 295 resolves to an aluminum strut-profile alloy family used in a commercial modular framing system. Row 359 resolves to mild or non-alloy structural steel hollow-section stock. Both are structural metals, but substituting one material family for the other would affect stiffness, joining and fastening assumptions, corrosion and coating choices, profile forming route, and interface compatibility."
process_review:
  can_unify: false
  rationale: "Both rows use the same high-level structural_profile_stock_fabrication_cutting bucket, but the specific closure handles differ. Row 295 is aluminum profile extrusion, optional anodized surface treatment, cut-to-length, deburring, and inspection. Row 359 is cold-formed welded steel hollow-section stock, cut-to-length, deburring, cleaning, and inspection. Keeping them split preserves the aluminum extrusion versus steel hollow-section production choice for staging."
geometry_review:
  can_unify: false
  rationale: "Row 295 is a 2120 mm long 60 x 60 modular slotted square profile whose slot geometry is part of its fastening interface. Row 359 is an 810 mm long 80 x 80 x 5 square hollow tube/profile with four units in the BOM. The length difference alone could be a variant, but the slotted modular profile and welded hollow tube cross-section are not the same closure geometry."
precision_review:
  blocks_merge: true
  rationale: "Precision does not block each row from becoming a reusable profile-stock item, but it blocks merging the two rows into one item. Row 295 carries modular slot-interface geometry, straightness, end-cut squareness, and alignment guardrails. Row 359 carries length tolerance, cut squareness, straightness, and alignment guardrails for hollow structural section fit-up. The modular slot-interface requirement is unique to the aluminum strut item."
assumptions:
  - "Row 295 should likely align with the earlier staged 60 x 60 aluminum structural profile closure item family, with 2120 mm retained as a cut-length variant rather than a unique item."
  - "Row 359 should remain a separate mild-steel square hollow structural profile closure item, with BOM quantity 4 and row total mass preserved for downstream BOM mapping."
  - "The current KB equivalence rule allows broad functional reuse, but material and interface compatibility are closure-relevant for these two rows."
unresolved:
  - "Final staging should search the KB again for an existing generic aluminum structural profile or steel square hollow structural profile before promoting either proposed item ID."
  - "Row 295 still lacks exact Rexroth material number, surface treatment, slot tolerance, and any end-machining details."
  - "Row 359 still lacks exact EN 10219 steel grade, coating, supplier route, cut-off method, and whether downstream assembly uses welding or mechanical fastening."
---

# Merge Review

The rough match is valid for discovery, but the candidate rows should split into two closure items: one aluminum modular slotted profile cut-length family and one mild-steel square hollow structural profile cut-length family.
