---
group_id: ream250_kb_merge_0001_bearing_support
candidate_rows:
  - source_row_number: 43
    item: "2AC9"
    path: research/ream250_bom/ream250_bom_row_0043_2AC9.md
    conversion_section_present: true
  - source_row_number: 384
    item: "4131"
    path: research/ream250_bom/ream250_bom_row_0384_4131.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0043_2AC9.md
    - research/ream250_bom/ream250_bom_row_0384_4131.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0043_2AC9.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0384_4131.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected both referenced CAD preview PNGs: row 43 is an 86 x 24 x 58 mm footed bearing support block with a central bore and side mounting holes, while row 384 is a 72 x 72 x 35 mm round flanged bearing pedestal with a central bore and bolt circle."
rough_match_basis:
  functional_purpose_key: bearing_support
  mass_window_kg:
    - 0.49
    - 0.72
merge_decision:
  decision: split
  rationale: "The rough bearing_support key correctly grouped two small metal bearing-location parts, but the rows should not collapse into one closure item. Row 43 is a compact footed bracket/block for a lower-axis bearing with side mounting features. Row 384 is a round flanged pedestal with a bolt circle and axisymmetric bearing-seat geometry. They share broad process and material assumptions, but their mounting interfaces and geometry forms are distinct enough to preserve separate staged closure items."
  proposed_closure_items:
    - item_id: ream250_axis_bearing_support_block_v0
      member_rows:
        - 43
      functional_purpose: "support and locate a lower-axis bearing around a shaft bore"
      material: unknown_metal
      scale_or_capacity:
        per_unit_mass_kg: 0.49
        bom_quantity: 1
        row_total_mass_kg: 0.49
        envelope_mm: "86 x 24 x 58"
        scale_class: small
      geometry_form: compact_footed_bearing_support_block_with_central_bore_and_side_mounting_holes
      process_family: general_subtractive_machining
    - item_id: ream250_round_bearing_pedestal_v0
      member_rows:
        - 384
      functional_purpose: "bearing and rotating shaft support pedestal for bolted mounting"
      material: unknown_bearing_housing_metal_alloy
      scale_or_capacity:
        per_unit_mass_kg: 0.72
        bom_quantity: 1
        row_total_mass_kg: 0.72
        envelope_mm: "72 x 72 x 35"
        scale_class: small
      geometry_form: compact_round_flanged_pedestal_with_central_bore_and_bolt_circle
      process_family: general_subtractive_machining
material_review:
  can_unify: true
  rationale: "Both rows have unresolved metal or bearing-housing alloy evidence and use steel-density mass as a conservative planning basis. Material does not block a merge by itself, but it also does not justify one item because neither row resolves alloy grade, bearing fit material, coating, or heat treatment."
process_review:
  can_unify: true
  rationale: "Both row conversions select general_subtractive_machining with stock preparation, cutting, precision machining or boring, drilling, deburring, and dimensional inspection. A later recipe family can likely reuse the same process anchors, but process-family unification is not the same as item unification."
geometry_review:
  can_unify: false
  rationale: "The row 43 CAD preview shows a blocky footed bracket with a large central bore, angled reliefs, and side mounting holes along a narrow 86 x 24 mm footprint. The row 384 preview shows a round flanged pedestal with annular shoulders, a central bore, and a circular bolt pattern. These are different mounting-interface classes, not minor scale variants of one bearing support."
precision_review:
  blocks_merge: true
  rationale: "Both rows need bore diameter, bore or seat alignment, mounting-face flatness, and hole-pattern checks, but the precision stack is tied to different geometry. Row 43 depends on foot and side-hole alignment for a lower-axis bracket; row 384 depends on bore concentricity, bearing-seat fit, and bolt-circle accuracy for a round pedestal. Merging would hide those distinct guardrails."
assumptions:
  - "The steel-density masses from the row research are retained for grouping because exact materials are unresolved."
  - "Existing KB bearing items such as bearing_set_medium, bearing_set, bearing_set_heavy, shaft_and_bearing_set, and mount_frame_bearing_bores were considered as conservative reuse candidates. They model bearings, assemblies, or mock bore features rather than these one-piece machined support bodies, so they are not close enough replacements for staging."
  - "A later KB staging pass may still use a shared generic recipe or process family for both proposed items, even though the closure item identities remain split."
  - "The proposed item IDs are staging suggestions only; this task does not write KB YAML and final import/local manufacture remains deferred."
unresolved:
  - "Exact alloy, bearing insert relationship, shaft interface, bore tolerance, surface finish, coating, and heat treatment remain unknown for both rows."
  - "Row 43 mating assembly position and fastener details are unresolved beyond the lower-axis bearing support context."
  - "Row 384 bearing-seat specification, bolt standard, and whether the pedestal was machined from stock or from a near-net blank remain unresolved."
  - "Later staging should re-check for newly added generic machined bearing-housing items before promoting either proposed closure item."
---

# Merge Review

Split the bearing_support candidate pool into two staged closure items. The rows can share a broad subtractive-machining process strategy, but their CAD geometry and bearing-interface guardrails are different enough to keep separate item identities for staging.
