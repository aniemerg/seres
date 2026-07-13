---
group_id: ream250_kb_merge_0032_structural_frame_member
candidate_rows:
  - source_row_number: 231
    item: "17AC"
    path: research/ream250_bom/ream250_bom_row_0231_17AC.md
    conversion_section_present: true
  - source_row_number: 229
    item: "17AA"
    path: research/ream250_bom/ream250_bom_row_0229_17AA.md
    conversion_section_present: true
  - source_row_number: 228
    item: "17A9"
    path: research/ream250_bom/ream250_bom_row_0228_17A9.md
    conversion_section_present: true
  - source_row_number: 230
    item: "17AB"
    path: research/ream250_bom/ream250_bom_row_0230_17AB.md
    conversion_section_present: true
  - source_row_number: 223
    item: "17A4"
    path: research/ream250_bom/ream250_bom_row_0223_17A4.md
    conversion_section_present: true
  - source_row_number: 220
    item: "17A1"
    path: research/ream250_bom/ream250_bom_row_0220_17A1.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0231_17AC.md
    - research/ream250_bom/ream250_bom_row_0229_17AA.md
    - research/ream250_bom/ream250_bom_row_0228_17A9.md
    - research/ream250_bom/ream250_bom_row_0230_17AB.md
    - research/ream250_bom/ream250_bom_row_0223_17A4.md
    - research/ream250_bom/ream250_bom_row_0220_17A1.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0231_17AC.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0229_17AA.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0228_17A9.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0230_17AB.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0223_17A4.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0220_17A1.md#kb-conversion
  notes: "Read every candidate row's original function, mass, material, how_to_make, kb_implications, KB Conversion section, and CAD preview evidence. All six rows are Bosch Rexroth-style 20 x 20 mm slotted aluminum structural profiles used as light machine-frame members, with cut-length variants from about 271 mm to 492.5 mm and BOM quantities from 1 to 6."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 0.1152
    - 0.22
merge_decision:
  decision: merge
  rationale: "The rough structural-frame grouping is supported by the row evidence. All six candidates are simple cut lengths of the same 20 x 20 mm slotted aluminum profile family, with the same structural framing role, same closure process family, and compatible material evidence. Length, quantity, minor mass-estimate basis differences, and possible 6061 versus 6060 or 6063 catalog-alloy differences are ordinary BOM mapping guardrails rather than reasons for separate closure items."
  proposed_closure_items:
    - item_id: ream250_aluminum_structural_profile_20x20_v0
      member_rows:
        - 231
        - 229
        - 228
        - 230
        - 223
        - 220
      functional_purpose: "light modular machine-frame structural support member"
      material: anodized_aluminum_6xxx_profile_family
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.1152
          - 0.22
        bom_quantity_range:
          - 1
          - 6
        row_total_mass_range_kg:
          - 0.1152
          - 1.13
        profile_size_mm: "20 x 20"
        cut_length_variants_mm:
          - 271
          - 288
          - 358
          - 463.7
          - 472.5
          - 492.5
        scale_class: small
      geometry_form: slotted_square_structural_profile_20x20_cut_length_variants
      process_family: structural_profile_stock_fabrication_cutting
material_review:
  can_unify: true
  rationale: "All rows resolve to an aluminum structural extrusion family. Rows 17AC, 17AA, 17A9, 17AB, and 17A1 cite anodized aluminum Bosch Rexroth profile-family evidence, with 17A9 and 17A1 also pointing to 6060 or 6063-family catalog data. Rows 17A4 and 17A1 include local CAD metadata for Aluminum 6061. At closure-analysis resolution, these are compatible 6xxx aluminum profile variants with anodized finish treated as a guardrail."
process_review:
  can_unify: true
  rationale: "Every row uses the same structural_profile_stock_fabrication_cutting closure handle: make or source constant-section 20 x 20 slotted aluminum profile stock, finish or anodize as needed, cut to length, deburr, and inspect cut length, slot geometry, straightness, and end condition. Existing process anchors named in the row conversions differ slightly, but they consistently point to extrusion plus stock cutting and inspection rather than machining unique frame members."
geometry_review:
  can_unify: true
  rationale: "The candidate rows share the same 20 x 20 mm slotted square or T-slot profile geometry. The CAD previews and row conversions differ only in cut length, with one noted 17AC filename-versus-measured-length discrepancy. Cut length is closure-relevant for BOM mapping but not a reason to create six closure items for the same profile stock."
precision_review:
  blocks_merge: false
  rationale: "No candidate carries precision evidence beyond ordinary modular-profile guardrails: profile size, slot interface compatibility, straightness, cut length, end squareness, anodized or protective finish, and frame alignment. Those guardrails are shared across the group and can be preserved in staging mappings without blocking a single profile-family closure item."
assumptions:
  - "A single 20 x 20 aluminum slotted profile closure item can cover all six rows under the project's 5x equivalence and reusable-stock modeling policy."
  - "Row-specific cut lengths, quantities, per-unit masses, and row-total masses should be preserved in Phase 3 proposed_bom_mappings rather than encoded as separate item IDs."
  - "The material should be normalized to anodized aluminum 6xxx profile family for staging, with 6061 versus 6060 or 6063 kept as unresolved procurement detail."
  - "Existing KB structural frame items are broad assemblies or other profile sizes; this merge review proposes a staged reAM250 20 x 20 profile-family item pending the Phase 3 reuse search."
unresolved:
  - "Final staging should search KB items, imports, and previous reAM250 staging outputs again before promoting the proposed item ID."
  - "Exact Bosch Rexroth article numbers, alloy temper, anodizing specification, slot tolerance, connector compatibility, and end machining details remain unresolved."
  - "Row 17AC has a filename suffix suggesting 296 mm while the measured CAD length is 288 mm; Phase 3 should carry this as a row-specific length uncertainty."
  - "The final import/local decision is deferred; local manufacture would require extrusion die capability, profile finishing, cut-to-length work, and inspection."
---

# Merge Review

This candidate set should merge into one 20 x 20 aluminum slotted structural profile closure item. Length and quantity differences are BOM mapping details, not separate KB item identities.
