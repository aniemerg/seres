---
group_id: ream250_kb_merge_0037_structural_frame_member
candidate_rows:
  - source_row_number: 361
    item: "917"
    path: research/ream250_bom/ream250_bom_row_0361_917.md
    conversion_section_present: true
  - source_row_number: 290
    item: "91E"
    path: research/ream250_bom/ream250_bom_row_0290_91E.md
    conversion_section_present: true
  - source_row_number: 301
    item: "98"
    path: research/ream250_bom/ream250_bom_row_0301_98.md
    conversion_section_present: true
  - source_row_number: 316
    item: "261"
    path: research/ream250_bom/ream250_bom_row_0316_261.md
    conversion_section_present: true
  - source_row_number: 318
    item: "271"
    path: research/ream250_bom/ream250_bom_row_0318_271.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0361_917.md
    - research/ream250_bom/ream250_bom_row_0290_91E.md
    - research/ream250_bom/ream250_bom_row_0301_98.md
    - research/ream250_bom/ream250_bom_row_0316_261.md
    - research/ream250_bom/ream250_bom_row_0318_271.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0361_917.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0290_91E.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0301_98.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0316_261.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0318_271.md#kb-conversion
  notes: "Read every candidate row's original function, mass, material, how_to_make, kb_implications, KB Conversion section, and CAD preview. The evidence separates a mild-steel square hollow profile, a stainless angle-stock frame, a plain large plate, and a matching pair of Aluminum 6061 machined side plates."
rough_match_basis:
  functional_purpose_key: structural_frame_member
  mass_window_kg:
    - 18.82
    - 24.02
merge_decision:
  decision: partial_merge
  rationale: "The rough structural-frame key and similar per-unit masses are useful for discovery, but they do not support one closure item. Rows 316 and 318 should merge because they are counterpart large Aluminum 6061 side plates with the same 398 x 960 x 25 mm envelope, nearly identical mass, integral rib or pocket geometry, and the same plate machining closure path. Rows 361, 290, and 301 should stay separate because they differ by material family, stock form, geometry, quantity context, and process guardrails: long mild-steel square hollow section, closed stainless L-angle frame, and plain 10 mm structural plate."
  proposed_closure_items:
    - item_id: ream250_steel_square_hollow_structural_profile_80x80_v0
      member_rows:
        - 361
      functional_purpose: "machine-frame structural support member"
      material: mild_steel_structural_hollow_section
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 18.82
          - 18.82
        bom_quantity_range:
          - 22
          - 22
        row_total_mass_range_kg:
          - 414.0
          - 414.0
        profile_size_mm: "80 x 80 x 5"
        cut_length_variants_mm:
          - 1670
        scale_class: large
      geometry_form: square_hollow_structural_profile_cut_to_length
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_stainless_angle_profile_frame_v0
      member_rows:
        - 290
      functional_purpose: "stiff structural perimeter frame and mounting support"
      material: stainless_steel_angle_stock_family
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 18.9
          - 18.9
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 18.9
          - 18.9
        profile_size_mm: "50 x 50 x 5 angle"
        frame_envelope_mm: "900 x 1670"
        scale_class: large
      geometry_form: closed_rectangular_l_angle_profile_frame
      process_family: structural_profile_stock_fabrication_cutting
    - item_id: ream250_large_plain_structural_plate_v0
      member_rows:
        - 301
      functional_purpose: "large structural plate or panel for machine frame group"
      material: structural_metal_unknown_aluminum_planning
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 22.766
          - 22.766
        bom_quantity_range:
          - 4
          - 4
        row_total_mass_range_kg:
          - 91.064
          - 91.064
        envelope_mm: "900 x 960 x 10"
        scale_class: large
      geometry_form: large_plain_rectangular_plate
      process_family: sheet_plate_cutting_drilling
    - item_id: ream250_large_machined_aluminum_side_plate_v0
      member_rows:
        - 316
        - 318
      functional_purpose: "large structural side support and stiffening member for machine frame interfaces"
      material: aluminum_6061
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 23.99
          - 24.02
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 23.99
          - 24.02
        envelope_mm: "398 x 960 x 25"
        handedness_or_counterpart_variants:
          - left
          - right
        scale_class: large
      geometry_form: counterpart_large_ribbed_or_pocketed_machined_side_plate
      process_family: general_subtractive_machining
material_review:
  can_unify: false
  rationale: "Material can unify only within the side-plate pair. Rows 316 and 318 both have STEP metadata for Aluminum 6061 at about 2700 kg/m3. Row 361 is mild steel hollow section, row 290 is a stainless DIN 59370 angle-stock family inference, and row 301 has unresolved structural metal with aluminum used only as a mass-planning assumption. Treating all five as one material family would erase steel versus stainless versus aluminum stock choices that affect forming, joining, corrosion, mass, and machining."
process_review:
  can_unify: false
  rationale: "Rows 361 and 290 both use structural profile stock fabrication and cutting at the broad bucket level, but one is cut mild-steel square hollow stock and the other is a joined rectangular angle-stock frame, so they still need separate closure items. Row 301 uses sheet or plate cutting and edge finishing. Rows 316 and 318 share a large Aluminum 6061 plate machining route with rough blank cutting, CNC milling of pockets, ribs, central or interface features, deburring, and inspection; those two can share one process family. A single five-row process closure item would mix profile production, joined frame fabrication, plain plate cutting, and machined side-plate work."
geometry_review:
  can_unify: false
  rationale: "Geometry unifies only for rows 316 and 318. Their previews show matching 398 x 960 x 25 mm counterpart side plates with integral rib or pocket patterns and similar mass. Row 361 is a long 80 x 80 x 5 mm square hollow section cut to 1670 mm, row 290 is a 900 x 1670 mm closed rectangular frame made from 50 x 50 x 5 L-angle stock, and row 301 is a plain 900 x 960 x 10 mm rectangular plate. These are different closure geometries rather than length or handedness variants of one item."
precision_review:
  blocks_merge: true
  rationale: "Precision and interface guardrails block a single merge. The square hollow profile needs cross-section size, wall thickness, straightness, cut length, and end squareness. The angle frame needs frame squareness, flatness, profile cross-section, and joint quality. The plain plate needs material resolution, flatness, edge squareness, and attachment method. The side plates need flatness, pocket or rib geometry, central feature and attachment feature positions, datum or interface alignment, and 6061 plate stock control. These guardrails are compatible within the side-plate pair but not across the full candidate pool."
assumptions:
  - "Rows 316 and 318 are left and right or counterpart side plates; their handedness and local pocket or rib differences should be preserved in BOM mappings rather than forcing two closure items."
  - "Row 361 should align with the previously proposed 80 x 80 mild-steel square hollow structural profile family when Phase 3 reviews cross-merge-review duplicates."
  - "Row 301 remains separate from the machined side-plate pair because its 10 mm plain plate geometry, unresolved material, and quantity-four frame-panel role lack the machining and alignment evidence carried by rows 316 and 318."
  - "No row in this group is a complex vendor module requiring decomposition before merge; all are simple structural parts or fabricated frames."
unresolved:
  - "Final staging should search the KB and earlier reAM250 staging outputs for existing equivalents before promoting the proposed item IDs, especially the 80 x 80 steel square hollow profile family."
  - "Row 361 still lacks exact steel grade, tolerance class, coating, and frame load-path context."
  - "Row 290 still lacks exact stainless grade, corner joint type, weld or braze detail, and final flatness tolerance."
  - "Row 301 still lacks material family and attachment method; if later evidence proves Aluminum 6061 and machined features, staging may reconsider whether it belongs nearer the side-plate family."
  - "Rows 316 and 318 still lack temper, surface finish, hole and thread specifications, datum scheme, and flatness or alignment tolerances."
---

# Merge Review

This candidate set should partially merge. Rows 316 and 318 form one large machined Aluminum 6061 side-plate closure item. Rows 361, 290, and 301 remain separate because their material, stock form, process route, and precision guardrails are closure-relevant.
