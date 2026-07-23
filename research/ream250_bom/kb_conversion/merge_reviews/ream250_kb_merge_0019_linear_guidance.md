---
group_id: ream250_kb_merge_0019_linear_guidance
candidate_rows:
  - source_row_number: 189
    item: "6M1"
    path: research/ream250_bom/ream250_bom_row_0189_6M1.md
    conversion_section_present: true
  - source_row_number: 191
    item: "6N1"
    path: research/ream250_bom/ream250_bom_row_0191_6N1.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0189_6M1.md
    - research/ream250_bom/ream250_bom_row_0191_6N1.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0189_6M1.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0191_6N1.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected both referenced CAD preview PNGs: row 189 is a 60.00 x 15.20 x 122.00 mm machined carriage/table block for an SMC LEFG support guide, while row 191 is a 60.00 x 18.20 x 122.00 mm machined carriage/table block for an SMC LEFS slider actuator."
rough_match_basis:
  functional_purpose_key: linear_guidance
  mass_window_kg:
    - 0.243
    - 0.275
merge_decision:
  decision: merge
  rationale: "Both rows represent small anodized aluminum carriage/table bodies for SMC linear guidance hardware. Their measured envelopes differ mainly by width, their per-unit masses are within about 13 percent, both conversions choose general_subtractive_machining with precision machining, anodizing or surface finishing, and dimensional inspection, and their guide-face plus mounting-hole guardrails are compatible. The source contexts differ between passive support guide and driven slider actuator, but for closure analysis those are application placements of the same small linear-guide carriage body family rather than separate item identities."
  proposed_closure_items:
    - item_id: ream250_linear_guide_carriage_table_v0
      member_rows:
        - 189
        - 191
      functional_purpose: "support and align a moving mounting table on compact linear guide or slider hardware"
      material: anodized_aluminum_alloy
      scale_or_capacity:
        per_unit_mass_kg_range:
          - 0.243
          - 0.275
        bom_quantities_by_row:
          "189": 1
          "191": 6
        row_total_mass_kg_by_row:
          "189": 0.243
          "191": 1.65
        envelope_mm_range: "60 x 15.2-18.2 x 122"
        scale_class: small
      geometry_form: narrow_rectangular_machined_carriage_table_with_mounting_holes_and_guide_faces
      process_family: general_subtractive_machining
material_review:
  can_unify: true
  rationale: "Both rows identify the visible carriage/table body as aluminum alloy with anodized finish based on SMC LEF-family evidence and CAD-volume mass estimates. Row 191 carries an unresolved possibility of hidden steel guide inserts, and row 189 notes related rail, seal-band, bushing, and guide hardware outside the CAD-split row. Those unresolved elements should stay as precision and assembly guardrails, but they do not block merging the visible aluminum carriage/table bodies."
process_review:
  can_unify: true
  rationale: "Both conversion sections select general_subtractive_machining and list stock preparation, cutting, drilling, precision machining, deburring, surface finishing or anodizing, and dimensional inspection. Row 189 also records later assembly with the rail and guide hardware; row 191 records possible grinding or finishing for guide-contact surfaces. Those are compatible supporting operations for one closure item family."
geometry_review:
  can_unify: true
  rationale: "The CAD previews show nearly identical narrow rectangular carriage/table solids with the same 60 mm by 122 mm plan scale, similar mounting-hole positions, relieved side or guide features, and a minor width difference of 15.2 mm versus 18.2 mm. This is a close geometry variant within the 5x equivalence policy, not a distinct closure item."
precision_review:
  blocks_merge: false
  rationale: "Both rows require guide-face tolerance, mounting-hole position, sliding alignment, surface condition, and final dimensional inspection. The exact tolerance class and hidden bearing or insert details remain unresolved, but the guardrails are the same type and can be preserved on one staged item rather than forcing a split."
assumptions:
  - "The CAD-split solids in both rows represent the aluminum carriage/table body only, not complete SMC LEFG or LEFS guide and actuator assemblies."
  - "The 3 mm width difference is treated as a vendor or application variant of the same small carriage/table family under the project's 5x equivalence rule."
  - "Existing KB item linear_guide_rails was checked as a conservative reuse candidate; it is a roughly 20 kg hardened steel rail-and-carriage system, not a close replacement for these 0.24-0.28 kg isolated anodized aluminum carriage bodies."
  - "Existing KB item linear_actuator_precision was checked as a broader actuator candidate, but it represents an 8 kg precision actuator assembly rather than this small carriage/table component."
  - "The proposed item ID is a staging suggestion only; this task does not write KB YAML and final import/local manufacture remains deferred to Phase 3."
unresolved:
  - "Exact aluminum alloy grade, anodize specification, guide-face tolerance, surface finish, and mounting-hole position tolerance remain unknown for both rows."
  - "Whether row 191 includes hidden bearing or guide inserts not visible in the single-solid CAD export remains unresolved."
  - "Whether row 189 requires separate stainless seal-band or bushing interfaces when assembled into the complete LEFG support guide remains unresolved."
  - "Later staging should re-check for a newly added generic small linear-guide carriage item before promoting the proposed closure item."
---

# Merge Review

Merge the two linear_guidance candidate rows into one staged closure item for a small anodized aluminum linear-guide carriage/table body. The rows keep the same precision guardrails for guide faces, mounting holes, sliding alignment, and surface finish, while rail, actuator, seal-band, and hidden insert details remain downstream assembly or staging concerns.
