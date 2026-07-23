---
group_id: ream250_kb_merge_0030_rolling_element
candidate_rows:
  - source_row_number: 51
    item: "2AD8"
    path: research/ream250_bom/ream250_bom_row_0051_2AD8.md
    conversion_section_present: true
  - source_row_number: 47
    item: "2AD4"
    path: research/ream250_bom/ream250_bom_row_0047_2AD4.md
    conversion_section_present: true
  - source_row_number: 50
    item: "2AD7"
    path: research/ream250_bom/ream250_bom_row_0050_2AD7.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0051_2AD8.md
    - research/ream250_bom/ream250_bom_row_0047_2AD4.md
    - research/ream250_bom/ream250_bom_row_0050_2AD7.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0051_2AD8.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0047_2AD4.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0050_2AD7.md#kb-conversion
  notes: "Read all three rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected the three referenced CAD preview PNGs; each shows a visually identical smooth sphere with about a 4.9 x 4.9 x 5.0 mm displayed bounding box in the top-axis bearing context."
rough_match_basis:
  functional_purpose_key: rolling_element
  mass_window_kg:
    - 0.000499
    - 0.0005
merge_decision:
  decision: merge
  rationale: "All three rows represent one loose spherical rolling element in the same top-axis bearing group. The CAD-derived volumes and displayed bounding boxes match, per-row masses differ only by rounding, and each row uses the same bearing-steel material assumption with unresolved grade. Their conversion sections select the same precision-component import/decompose-later bucket because roundness, hardness, lapping, surface finish, and ball grade are the dominant closure risks. Those unresolved precision details are shared guardrails, not evidence for separate item identities."
  proposed_closure_items:
    - item_id: ream250_precision_bearing_ball_4p95mm_v0
      member_rows:
        - 51
        - 47
        - 50
      functional_purpose: "provide low-friction rolling contact and load transfer in a top-axis bearing stack"
      material: bearing_steel
      scale_or_capacity:
        per_unit_mass_kg_range:
          - 0.000499
          - 0.0005
        bom_quantities_by_row:
          "51": 1
          "47": 1
          "50": 1
        row_total_mass_kg_by_row:
          "51": 0.000499
          "47": 0.0005
          "50": 0.0005
        nominal_diameter_mm: 4.95
        scale_class: tiny
      geometry_form: small_precision_spherical_bearing_ball
      process_family: precision_component_import_decompose_later
material_review:
  can_unify: true
  rationale: "The row-specific STEP metadata is placeholder-only for all three candidates. Each research file infers hardened bearing steel or chrome bearing-steel family from the spherical CAD geometry and axis-bearing function. For closure analysis, one bearing-steel planning material is sufficient, with exact alloy, stainless or ceramic alternatives, hardness, and corrosion class deferred to staging."
process_review:
  can_unify: true
  rationale: "All three rows describe the same standard bearing-ball route: bearing-steel wire or slug preparation, forming or cold heading, heat treatment, precision grinding/lapping/polishing, cleaning, and inspection. The conversion sections all map this to precision_component_import_decompose_later because current generic KB process buckets do not fully represent ball-grade roundness, hardness, surface finish, and metrology. Candidate process anchors vary slightly by row, but the closure process family and precision blockers are the same."
geometry_review:
  can_unify: true
  rationale: "The original measurements report the same 63.506 mm^3 volume and about 4.95 mm cubic bounding box for all three rows. The inspected previews are visually identical smooth spheres with no handedness, bore, thread, mounting face, cage, race, or other geometry that would separate one row from the others."
precision_review:
  blocks_merge: false
  rationale: "Precision blocks a simple local manufacturing decision, but it does not block merging these rows. Each candidate carries the same diameter, roundness, hardness, lapped surface finish, material grade, and ball-grade guardrails, so a single closure item can preserve the shared risk without hiding row-specific evidence."
assumptions:
  - "Rows 47, 50, and 51 are separate BOM occurrences of the same loose top-axis bearing ball rather than distinct bearing subtypes."
  - "Bearing steel remains the planning material because every row infers standard bearing-ball practice and no row-specific material metadata contradicts it."
  - "Existing KB items bearing_ball_precision and bearing_ball_steel were checked as conservative reuse candidates; their current KB definitions are bulk placeholder materials with 0.02 kg and 0.3 kg masses, so they are not direct per-unit matches for a 0.0005 kg loose ball without a later staging normalization decision."
  - "Existing KB part ball_bearing_steel_v0 was checked; it represents a placeholder bearing assembly rather than a loose bearing ball and is not a direct merge target."
  - "The completed bottom-axis merge review ream250_kb_merge_0029_rolling_contact proposes a 5.4 mm precision bearing ball; Phase 3 should consider unifying that staged identity with this 4.95 mm top-axis ball under the project's 5x equivalence policy unless bearing-fit guardrails require preserving diameter variants."
  - "The proposed item ID is a staging suggestion only; this task does not write KB YAML and final import/local manufacture remains deferred to Phase 3."
unresolved:
  - "Exact material grade, bearing-ball grade, diameter tolerance, roundness, hardness, heat-treatment specification, surface finish, cleanliness requirement, and lubrication context remain unknown."
  - "Later staging should decide whether to reuse or upgrade the existing bearing_ball_precision concept instead of promoting a reAM250-specific item."
  - "The top-axis bearing assembly context may contain additional neighboring loose balls that should map to the same closure item in a later BOM mapping pass."
  - "Import versus local manufacture remains unresolved because the precision ball-making route is not fully represented by current generic KB processes."
---

# Merge Review

Merge the three rolling_element rows into one staged closure identity for a 4.95 mm loose precision bearing ball in the top-axis bearing group. The rows share function, geometry, scale, material assumptions, process abstraction, and precision guardrails; Phase 3 should decide whether this identity can also collapse into a broader small precision bearing-ball item used by the previously reviewed 5.4 mm bottom-axis balls.
