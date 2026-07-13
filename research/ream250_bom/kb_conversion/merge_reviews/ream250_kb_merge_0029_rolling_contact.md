---
group_id: ream250_kb_merge_0029_rolling_contact
candidate_rows:
  - source_row_number: 39
    item: "2AC5"
    path: research/ream250_bom/ream250_bom_row_0039_2AC5.md
    conversion_section_present: true
  - source_row_number: 38
    item: "2AC4"
    path: research/ream250_bom/ream250_bom_row_0038_2AC4.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0039_2AC5.md
    - research/ream250_bom/ream250_bom_row_0038_2AC4.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0039_2AC5.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0038_2AC4.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected both referenced CAD preview PNGs: each row is a visually identical smooth sphere with a 5.4 x 5.4 x 5.4 mm bounding box in the bottom-axis bearing context."
rough_match_basis:
  functional_purpose_key: rolling_contact
  mass_window_kg:
    - 0.000644
    - 0.000647
merge_decision:
  decision: merge
  rationale: "Both candidates represent one loose spherical rolling/contact element in the same bottom-axis bearing family. Their geometry is identical at the CAD-preview level, their per-unit masses differ by less than one percent, both rows carry the same bearing-steel material assumption, and both conversions select the same precision-component bucket because roundness, hardness, lapping, and surface finish dominate closure risk. The unresolved grade and tolerance details are shared guardrails rather than evidence for separate item identities."
  proposed_closure_items:
    - item_id: ream250_precision_bearing_ball_5p4mm_v0
      member_rows:
        - 39
        - 38
      functional_purpose: "provide low-friction point rolling contact in a bottom-axis bearing stack"
      material: chrome_bearing_steel
      scale_or_capacity:
        per_unit_mass_kg_range:
          - 0.000644
          - 0.000647
        bom_quantities_by_row:
          "39": 1
          "38": 1
        row_total_mass_kg_by_row:
          "39": 0.000644
          "38": 0.000647
        nominal_diameter_mm: 5.4
        scale_class: tiny
      geometry_form: small_precision_spherical_bearing_ball
      process_family: precision_component_import_decompose_later
material_review:
  can_unify: true
  rationale: "Row 38 identifies chrome bearing steel from independent bearing-ball supplier evidence, while row 39 records an unknown bearing-ball metal with chrome bearing steel used for the mass and process assumption. The STEP metadata is placeholder-only for both rows. For closure analysis, both should share a chrome-bearing-steel planning material with unresolved grade, stainless or ceramic alternatives deferred to staging."
process_review:
  can_unify: true
  rationale: "Both conversion sections treat the original route as precision bearing-ball forming, heat treatment, grinding or lapping, polishing, and inspection, then substitute to precision_component_import_decompose_later because generic local process buckets do not capture bearing-ball grade roundness, hardness, and surface finish. Candidate process anchors differ slightly by row, but the closure process family and blockers are the same."
geometry_review:
  can_unify: true
  rationale: "The CAD previews for both rows show the same smooth 5.4 mm sphere from all rendered views, and the measured volume is effectively identical. No mounting interface, handedness, bore, thread, or seat geometry distinguishes one row from the other; they are repeated loose rolling elements."
precision_review:
  blocks_merge: false
  rationale: "Precision requirements block an easy local-manufacturing decision, but they do not block merging these two rows. Both require the same diameter control, roundness, hardness, lapped surface finish, wear resistance, and inspection guardrails, so one closure item can preserve the shared precision risk."
assumptions:
  - "Rows 38 and 39 are separate BOM occurrences of the same loose bottom-axis bearing ball rather than distinct bearing subtypes."
  - "Chrome bearing steel remains the planning material because both rows infer bearing-ball practice and no row-specific material metadata contradicts it."
  - "Existing KB items bearing_ball_precision and bearing_ball_steel were checked as conservative reuse candidates; their current KB definitions are bulk placeholder materials with 0.02 kg and 0.3 kg masses, so they are not close per-unit matches for a 0.00065 kg loose 5.4 mm ball without a later staging decision to normalize them."
  - "Existing KB part ball_bearing_steel_v0 was also checked; it represents a placeholder bearing assembly rather than a loose bearing ball and is not a direct merge target."
  - "The proposed item ID is a staging suggestion only; this task does not write KB YAML and final import/local manufacture remains deferred to Phase 3."
unresolved:
  - "Exact material grade, bearing-ball grade, diameter tolerance, roundness, hardness, heat-treatment specification, surface finish, and cleanliness requirement remain unknown."
  - "Later staging should decide whether to reuse or upgrade the existing bearing_ball_precision concept instead of promoting a reAM250-specific item."
  - "The bottom-axis bearing assembly context may contain additional neighboring loose balls that should map to the same closure item in a later BOM mapping pass."
  - "Import versus local manufacture remains unresolved because the precision ball-making route is not fully represented by current generic KB processes."
---

# Merge Review

Merge the two rolling_contact rows into one staged closure identity for a 5.4 mm loose precision bearing ball. The rows share function, scale, geometry, material assumptions, and precision guardrails; the main downstream decision is whether Phase 3 reuses or upgrades an existing generic bearing-ball item.
