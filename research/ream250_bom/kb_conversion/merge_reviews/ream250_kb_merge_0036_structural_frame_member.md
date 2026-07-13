---
group_id: ream250_kb_merge_0036_structural_frame_member
candidate_rows:
  - source_row_number: 362
    item: "918"
    path: research/ream250_bom/ream250_bom_row_0362_918.md
    conversion_section_present: true
  - source_row_number: 363
    item: "919"
    path: research/ream250_bom/ream250_bom_row_0363_919.md
    conversion_section_present: true
  - source_row_number: 358
    item: "914"
    path: research/ream250_bom/ream250_bom_row_0358_914.md
    conversion_section_present: true
  - source_row_number: 302
    item: "99"
    path: research/ream250_bom/ream250_bom_row_0302_99.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0362_918.md
    - research/ream250_bom/ream250_bom_row_0363_919.md
    - research/ream250_bom/ream250_bom_row_0358_914.md
    - research/ream250_bom/ream250_bom_row_0302_99.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0362_918.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0363_919.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0358_914.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0302_99.md#kb-conversion
  notes: "Read every candidate row's original function, mass, material, how_to_make, kb_implications, KB Conversion section, and CAD preview image. Rows 362, 363, and 358 are the same 80 x 80 x 5 mm square hollow mild-steel profile family in 740, 950, and 960 mm cut lengths. Row 302 is a lower/base hollow profile with a 900 x 100 x 80 mm envelope and CAD-implied 100 x 80 x 5 mm rectangular section."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 8.34
    - 12.01
merge_decision:
  decision: partial_merge
  rationale: "The rough structural-frame key correctly grouped cut hollow structural profiles, but the evidence supports two closure items rather than one. Rows 362, 363, and 358 should merge as 80 x 80 x 5 mild-steel square hollow structural profile cut-length variants; their length, quantity, and row-total mass should be preserved in downstream BOM mappings. Row 302 shares the broad structural-steel hollow-profile process family, but its CAD and conversion evidence identify a 100 x 80 x 5 rectangular lower/base profile, so it should stay separate from the 80 x 80 square profile item."
  proposed_closure_items:
    - item_id: ream250_steel_square_hollow_structural_profile_80x80_v0
      member_rows:
        - 362
        - 363
        - 358
      functional_purpose: "machine-frame structural support member"
      material: mild_steel_structural_hollow_section
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 8.34
          - 10.82
        bom_quantity_range:
          - 2
          - 4
        row_total_mass_range_kg:
          - 21.41
          - 43.28
        profile_size_mm: "80 x 80 x 5"
        cut_length_variants_mm:
          - 740
          - 950
          - 960
        scale_class: medium
      geometry_form: square_hollow_structural_profile_cut_to_length
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_steel_rectangular_hollow_bottom_profile_100x80_v0
      member_rows:
        - 302
      functional_purpose: "lower machine-frame or base structural support member"
      material: structural_steel_hollow_section_planning
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 12.01
          - 12.01
        bom_quantity_range:
          - 2
          - 2
        row_total_mass_range_kg:
          - 24.02
          - 24.02
        profile_size_mm: "100 x 80 x 5 inferred"
        cut_length_variants_mm:
          - 900
        scale_class: medium
      geometry_form: rectangular_hollow_structural_profile_cut_to_length
      process_family: structural_profile_stock_fabrication_cutting
material_review:
  can_unify: true
  rationale: "All four rows can be treated as structural steel hollow-section material at the broad closure-material level, with rows 362, 363, and 358 directly supported by Steel, Mild metadata or EN 10219 naming. Row 302 is less certain because its STEP material is generic, but its geometry and neighboring BOM context support structural steel as the planning material. This material unification does not by itself justify one item because cross-section geometry remains different."
process_review:
  can_unify: true
  rationale: "All four rows use the same high-level structural_profile_stock_fabrication_cutting closure handle: produce or source welded hollow structural section stock, cut to length, deburr, clean or coat as required, and inspect length, squareness, straightness, wall condition, and fit-up. Row 302 may require a rectangular rather than square hollow-section stock setup, but that is a size/profile variant within the same process family."
geometry_review:
  can_unify: false
  rationale: "Rows 362, 363, and 358 unify cleanly as 80 x 80 x 5 mm square hollow-section cut lengths. Their 740, 950, and 960 mm lengths are ordinary BOM cut-length variants. Row 302 is a 900 mm long hollow profile with a 100 x 80 mm outside envelope and CAD-implied 5 mm wall, so it is a rectangular lower-profile member rather than a length variant of the square 80 x 80 section."
precision_review:
  blocks_merge: true
  rationale: "Precision does not block the three-row square-profile merge, but it blocks a single four-row merge because profile size and cross-section are part of the frame fit-up guardrails. All rows need length tolerance, cut squareness, straightness, wall thickness, and frame alignment checks; row 302 additionally carries a 100 x 80 rectangular profile-size guardrail and unresolved material/coating evidence."
assumptions:
  - "Rows 362, 363, and 358 should align with the previously proposed reAM250 80 x 80 mild-steel square hollow structural profile closure item used by other merge reviews, with row-specific cut lengths and quantities preserved in BOM mappings."
  - "Row 302 is kept separate because the 100 x 80 rectangular cross-section affects stock selection and frame fit-up, even though it shares material and process family with the square-section rows."
  - "Existing KB structural frame items are broad frame assemblies or generic steel frame abstractions; they do not preserve row-level hollow-section cross-section, cut-length, and wall-thickness guardrails needed for this reAM250 staging work."
  - "No candidate row is a complex module requiring decomposition before merge; each is a simple cut structural profile."
unresolved:
  - "Final staging should search KB and all earlier reAM250 staging outputs again before promotion, especially for a generic steel hollow structural profile stock item."
  - "Rows 362, 363, and 358 still lack exact EN steel grade, coating, supplier route, cut-off method, and downstream welding or fastening details."
  - "Row 302 still lacks direct material metadata, exact steel grade, surface treatment, installed connection method, and confirmation that the inferred 100 x 80 x 5 mm section is the intended production profile."
  - "A later staging pass should decide whether the 80 x 80 square and 100 x 80 rectangular sections remain separate staged items or are represented by one broader steel hollow structural profile stock family plus profile-size BOM mappings."
---

# Merge Review

This candidate set should partially merge. Rows 362, 363, and 358 form one 80 x 80 x 5 mild-steel square hollow structural profile closure item with cut-length variants. Row 302 remains a separate 100 x 80 rectangular lower-profile closure item because cross-section geometry is closure-relevant for stock choice and frame fit-up.
