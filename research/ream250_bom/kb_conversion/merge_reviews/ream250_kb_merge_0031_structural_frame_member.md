---
group_id: ream250_kb_merge_0031_structural_frame_member
candidate_rows:
  - source_row_number: 232
    item: "17AD"
    path: research/ream250_bom/ream250_bom_row_0232_17AD.md
    conversion_section_present: true
  - source_row_number: 225
    item: "17A6"
    path: research/ream250_bom/ream250_bom_row_0225_17A6.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0232_17AD.md
    - research/ream250_bom/ream250_bom_row_0225_17A6.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0232_17AD.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0225_17A6.md#kb-conversion
  notes: "Read both rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Both rows cite CAD preview evidence showing short constant-section 20 x 20 mm slotted aluminum strut profiles. Row 232 is a 110 mm Bosch Rexroth profile-family cut length with quantity 2; row 225 is a 131 mm cut length with quantity 1 and STEP material Aluminum 6061."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 0.0492
    - 0.0604
merge_decision:
  decision: merge
  rationale: "The two candidates are the same closure-level item: short 20 x 20 slotted aluminum structural profile stock cut to different lengths. The 110 mm and 131 mm lengths, BOM quantities, and row-total masses should be preserved in later BOM mappings, but they do not require separate KB closure items. Material evidence differs in specificity, with row 232 using the Bosch Rexroth 6060 or 6063 profile family and row 225 using STEP material Aluminum 6061, but both are aluminum alloy modular framing profiles within the project equivalence rule."
  proposed_closure_items:
    - item_id: ream250_aluminum_structural_profile_20x20_v0
      member_rows:
        - 232
        - 225
      functional_purpose: "modular light structural framing member for machine support, spacing, and connector-compatible fastening"
      material: aluminum_alloy_profile_family
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.0492
          - 0.0604
        bom_quantity_range:
          - 1
          - 2
        row_total_mass_range_kg:
          - 0.0604
          - 0.0984
        profile_size_mm: "20 x 20"
        cut_length_variants_mm:
          - 110
          - 131
        scale_class: small
      geometry_form: slotted_square_structural_profile_20x20_cut_length_variants
      process_family: structural_profile_stock_fabrication_cutting
material_review:
  can_unify: true
  rationale: "Both rows are aluminum alloy slotted profile stock. Row 232 is supported by Bosch Rexroth profile-family evidence for EN AW Al MgSi, EN AW-6060, and AW-6063-T66 family properties with anodized finish. Row 225 is supported by local STEP metadata for Aluminum 6061. For closure analysis these are compatible aluminum extrusion materials; final staging can carry alloy and finish as guardrails rather than splitting the item."
process_review:
  can_unify: true
  rationale: "Both conversions select structural_profile_stock_fabrication_cutting with extrusion, cutting, deburring, optional surface finishing, and dimensional inspection. The same process family covers producing 20 x 20 slotted profile stock, cutting to each row length, checking slot geometry and connector fit, and applying anodized-equivalent protection when needed."
geometry_review:
  can_unify: true
  rationale: "Both candidates are short 20 x 20 mm slotted square extrusion profiles. The 110 mm and 131 mm cut lengths are ordinary length variants of the same profile stock. The available row evidence does not show a different slot family, end feature, handedness, or installed geometry that would require separate closure items."
precision_review:
  blocks_merge: false
  rationale: "Precision does not block the merge. Both rows need cut length, end squareness, straightness, profile slot geometry, and connector-fit checks. These are shared profile-family guardrails, not row-specific precision interfaces. Exact Bosch profile slot dimensions and finish thickness remain downstream staging details."
assumptions:
  - "The two row files represent cut segments of the same 20 x 20 modular slotted aluminum profile family, with different cut lengths and BOM quantities."
  - "Aluminum 6061 and Bosch Rexroth 6060 or 6063 profile-family evidence are close enough for one closure material family at this stage."
  - "Anodizing is treated as a finish guardrail and supporting process, not a reason to split the closure item."
  - "Existing KB structural frame items are broad assemblies or nonmatching profile abstractions; the later staging pass should still search KB again before promoting this reAM250-specific proposed item ID."
unresolved:
  - "Exact Bosch Rexroth catalog part number, slot dimensions, alloy temper, anodizing thickness, cut tolerance, and any end-machining requirements are not resolved from the row evidence."
  - "Final staging should decide whether this becomes a reAM250-specific 20 x 20 profile item or reuses a broader generic aluminum slotted profile stock item."
  - "Local closure may need to model extrusion die tooling explicitly if aluminum profile stock fabrication is promoted beyond an import boundary."
---

# Merge Review

Rows 232 and 225 should merge into one 20 x 20 slotted aluminum structural profile closure item. Preserve length, quantity, row-total mass, alloy evidence, and finish requirements in later staging and BOM mappings.
