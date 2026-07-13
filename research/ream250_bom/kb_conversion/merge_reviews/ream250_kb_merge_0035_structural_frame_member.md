---
group_id: ream250_kb_merge_0035_structural_frame_member
candidate_rows:
  - source_row_number: 298
    item: "95"
    path: research/ream250_bom/ream250_bom_row_0298_95.md
    conversion_section_present: true
  - source_row_number: 30
    item: "2A7"
    path: research/ream250_bom/ream250_bom_row_0030_2A7.md
    conversion_section_present: true
  - source_row_number: 29
    item: "2A6"
    path: research/ream250_bom/ream250_bom_row_0029_2A6.md
    conversion_section_present: true
  - source_row_number: 213
    item: "9B"
    path: research/ream250_bom/ream250_bom_row_0213_9B.md
    conversion_section_present: true
  - source_row_number: 300
    item: "97"
    path: research/ream250_bom/ream250_bom_row_0300_97.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0298_95.md
    - research/ream250_bom/ream250_bom_row_0030_2A7.md
    - research/ream250_bom/ream250_bom_row_0029_2A6.md
    - research/ream250_bom/ream250_bom_row_0213_9B.md
    - research/ream250_bom/ream250_bom_row_0300_97.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0298_95.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0030_2A7.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0029_2A6.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0213_9B.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0300_97.md#kb-conversion
  notes: "Read every candidate row's original function, mass, material, how_to_make, kb_implications, and KB Conversion section. The row-level CAD preview evidence was sufficient for geometry: rows 298, 213, and 300 are constant-section 60 x 60 slotted profiles, while rows 29 and 30 are mirrored ribbed Z-axis side plates."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 2.889
    - 3.982
merge_decision:
  decision: partial_merge
  rationale: "The rough key grouped all rows as structural frame members, but the evidence supports two closure items rather than one. Rows 298, 213, and 300 are Bosch-style 60 x 60 aluminum slotted extrusion cut lengths and should share one reusable profile-stock closure item with length and quantity preserved as guardrails. Rows 29 and 30 are left and right handed machined Z-axis side plates with ribbed plate geometry, guide and bearing alignment duties, and a subtractive machining route. The profile rows should not merge with the machined side plates because material certainty, process family, geometry, and precision interfaces differ."
  proposed_closure_items:
    - item_id: ream250_aluminum_structural_profile_60x60_v0
      member_rows:
        - 298
        - 213
        - 300
      functional_purpose: "modular machine-frame structural support member"
      material: aluminum_alloy_profile_family
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 2.889
          - 3.982
        bom_quantity_range:
          - 1
          - 2
        row_total_mass_range_kg:
          - 3.747
          - 7.963
        profile_size_mm: "60 x 60"
        cut_length_variants_mm:
          - 740
          - 960
          - 1020
        scale_class: medium
      geometry_form: slotted_square_structural_profile_60x60_cut_length_variants
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_z_axis_side_plate_machined_v0
      member_rows:
        - 29
        - 30
      functional_purpose: "handed structural side support for Z-axis guide and bearing assembly interfaces"
      material: structural_metal_alloy_planning_aluminum
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 3.49
          - 3.5
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 3.49
          - 3.5
        envelope_mm: "240 x 400 x 23"
        scale_class: medium
      geometry_form: mirrored_triangular_ribbed_machined_side_plate_with_mounting_hole_edge
      process_family: general_subtractive_machining
material_review:
  can_unify: false
  rationale: "Material can unify within each subgroup but not across the full five-row pool. The profile rows resolve to Bosch-style aluminum extrusion stock. Row 29 uses aluminum alloy as the planning material, while row 30 remains unresolved structural metal with aluminum and steel scenarios; those two can stay together as a structural metal side-plate family with a material guardrail. The side plates should not merge into the profile closure item because the profile material evidence is vendor-family aluminum extrusion, while the plates are custom machined structural metal parts with unresolved alloy and different stock form."
process_review:
  can_unify: false
  rationale: "Rows 298, 213, and 300 share structural_profile_stock_fabrication_cutting: aluminum extrusion, cut-to-length, deburring, finish, and inspection. Rows 29 and 30 share general_subtractive_machining from thick plate or billet stock with cutting, drilling, precision machining, finishing, and dimensional inspection. These process families are different closure handles and should stay split for lunarized process accounting."
geometry_review:
  can_unify: false
  rationale: "The three profile rows are the same 60 x 60 mm slotted square extrusion family with different lengths. The two plate rows are mirrored 240 x 400 x 23 mm ribbed wedge or triangular side plates with mounting-hole rows and datum faces. Length variation among profiles is merge-compatible, and handedness between the plates is merge-compatible, but profile-stock geometry and machined side-plate geometry are not one closure item."
precision_review:
  blocks_merge: true
  rationale: "Precision does not block the two subgroup merges, but it blocks a single five-row merge. Profile guardrails are cut length, end squareness, slot geometry, straightness, and connector fit. Z-axis plate guardrails are guide interface alignment, bearing interface alignment, datum face flatness, hole location accuracy, and unresolved material. The side-plate alignment role is substantially tighter and more application-specific than ordinary profile cut lengths."
assumptions:
  - "Rows 298, 213, and 300 can be represented by one reusable 60 x 60 aluminum slotted profile closure item, with cut length and BOM quantity carried in downstream BOM or staging notes."
  - "Rows 29 and 30 are a mirrored pair despite small geometry and mass differences; handedness should be a variant note rather than two separate closure items at this stage."
  - "Existing KB structural frame items are frame assemblies or steel frame abstractions, not direct equivalents for a 60 x 60 aluminum slotted profile stock item or these Z-axis side plates."
  - "Existing KB generic machined parts and fixture plates are too broad or materially different to replace the staged Z-axis side-plate closure item without losing alignment guardrails."
unresolved:
  - "Final staging should decide whether the 60 x 60 profile item should be a reAM250-specific staged item or a broader KB aluminum structural profile stock item."
  - "Exact Bosch Rexroth material number, alloy, temper, anodized finish, slot tolerance, and connector compatibility remain unresolved for the profile rows."
  - "Exact alloy, heat treatment, coating, thread details, datum scheme, and inspection tolerances remain unresolved for the Z-axis side plates, especially row 30's material family."
  - "A later KB edit should search again for any newly added aluminum profile stock or machined Z-axis plate equivalents before promoting these staged item IDs."
---

# Merge Review

This candidate set should split into two staged closure items: one for the 60 x 60 aluminum slotted profile cut lengths, and one for the mirrored machined Z-axis side plates. The shared rough key is useful for candidate discovery, but it is too broad for a single KB closure item.
