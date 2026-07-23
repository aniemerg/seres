---
group_id: ream250_kb_merge_0038_structural_frame_support_member
candidate_rows:
  - source_row_number: 235
    item: "17AG"
    path: research/ream250_bom/ream250_bom_row_0235_17AG.md
    conversion_section_present: true
  - source_row_number: 236
    item: "17AH"
    path: research/ream250_bom/ream250_bom_row_0236_17AH.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0235_17AG.md
    - research/ream250_bom/ream250_bom_row_0236_17AH.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0235_17AG.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0236_17AH.md#kb-conversion
  notes: "Read both candidate rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. The CAD proxy and preview evidence identify both rows as 60 x 60 slotted aluminum structural profile cut lengths, with row 235 carrying a length ambiguity and row 236 resolving to a 350 mm proxy."
rough_match_basis:
  functional_purpose_key: structural_frame_support_member
  mass_window_kg:
    - 0.9369
    - 1.37
merge_decision:
  decision: merge
  rationale: "Both rows represent the same closure item family: a 60 x 60 mm modular slotted aluminum structural profile used as machine-frame support stock. The per-unit masses differ because the rows are different cut lengths and because row 235 uses an ambiguous proxy STEP, but both stay within the same material, geometry, process, and precision guardrail set. Length, BOM quantity, row total mass, and proxy uncertainty should be preserved in downstream BOM mappings instead of splitting the closure item."
  proposed_closure_items:
    - item_id: ream250_aluminum_structural_profile_60x60_v0
      member_rows:
        - 235
        - 236
      functional_purpose: "modular machine-frame structural support member"
      material: anodized_aluminum_strut_stock
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.9369
          - 1.37
        bom_quantity_range:
          - 2
          - 2
        row_total_mass_range_kg:
          - 1.8738
          - 2.74
        profile_size_mm: "60 x 60"
        cut_length_variants_mm:
          - 300
          - 350
        proxy_measured_length_variants_mm:
          - 240
          - 350
        scale_class: small
      geometry_form: slotted_square_structural_profile_60x60_cut_length_variants
      process_family: structural_profile_stock_fabrication_cutting
material_review:
  can_unify: true
  rationale: "Both rows resolve to aluminum or anodized aluminum machine-frame strut stock. Row 235 lacks a direct material match but uses a row-96 proxy in the same 60 x 60 profile family, while row 236 uses standard 60 x 60 anodized aluminum profile evidence. Exact alloy, temper, and anodize details remain staging guardrails, but they do not require separate closure items."
process_review:
  can_unify: true
  rationale: "Both rows use the same process abstraction: metal profile extrusion through a slotted 60 x 60 die, optional straightening or aging, surface finishing, cut-to-length work, deburring, optional end drilling or tapping, and dimensional inspection. The shared structural_profile_stock_fabrication_cutting bucket captures the relevant lunarized closure handle."
geometry_review:
  can_unify: true
  rationale: "Both rows are slotted square 60 x 60 structural profile lengths. The 300 mm versus 350 mm nominal lengths are ordinary cut-length variants, and row 235's 240 mm proxy measurement is an evidence uncertainty to preserve in BOM notes rather than a distinct closure geometry."
precision_review:
  blocks_merge: false
  rationale: "The precision guardrails are the same for both rows: length accuracy, slot geometry, end squareness, straightness, and frame alignment. No row has evidence of unique high-precision interfaces, sealing, or special machining that would block use of one reusable profile-stock closure item."
assumptions:
  - "Rows 235 and 236 should align with the broader staged 60 x 60 aluminum slotted profile closure item family used by other reAM250 frame-profile rows."
  - "Cut length and BOM quantity should be handled in downstream proposed_bom_mappings rather than by creating one item per profile length."
  - "Optional end drilling or tapping remains a secondary operation only if later drawings show row-specific end features."
unresolved:
  - "Final staging should search KB items and imports for an existing generic 60 x 60 aluminum structural profile before promoting the proposed item ID."
  - "Row 235 still has a canonical CAD gap: the filename implies 300 mm while the proxy STEP measures 240 mm."
  - "Exact profile series, slot standard, alloy temper, anodized finish specification, and end machining details remain unresolved for both rows."
---

# Merge Review

Rows 235 and 236 should merge into one 60 x 60 aluminum slotted structural profile closure item. The row-specific cut lengths, quantities, masses, and proxy-CAD uncertainty should be carried forward as BOM mapping details.
