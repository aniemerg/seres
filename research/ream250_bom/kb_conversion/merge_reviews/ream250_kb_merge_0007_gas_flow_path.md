---
group_id: ream250_kb_merge_0007_gas_flow_path
candidate_rows:
  - source_row_number: 147
    item: "3S31"
    path: research/ream250_bom/ream250_bom_row_0147_3S31.md
    conversion_section_present: true
  - source_row_number: 152
    item: "3S41"
    path: research/ream250_bom/ream250_bom_row_0152_3S41.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0147_3S31.md
    - research/ream250_bom/ream250_bom_row_0152_3S41.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0147_3S31.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0152_3S41.md#kb-conversion
  notes: "Read both rows' original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected the referenced CAD preview PNGs: row 147 is a 60 x 60 x 115 mm short hollow square duct segment, and row 152 is a 50 x 460 x 44 mm long hollow rectangular duct segment."
rough_match_basis:
  functional_purpose_key: gas_flow_path
  mass_window_kg:
    - 0.381
    - 0.507
merge_decision:
  decision: merge
  rationale: "Both rows should converge to one fabricated gas-outlet duct-segment closure item. They share the gas outlet path function, unresolved metal sheet or thin-wall duct material, small scale, plumbing_connector_fabrication_testing process family, and cleanliness, seam integrity, mating-fit, and leak-test guardrails. The length and square-versus-rectangular cross section differences are compatible row-specific duct variants under the project's reuse policy rather than reasons to create separate closure items."
  proposed_closure_items:
    - item_id: ream250_fabricated_gas_outlet_duct_segment_v0
      member_rows:
        - 147
        - 152
      functional_purpose: "fabricated duct segment guiding process gas through the reAM250 gas outlet path"
      material: metal_alloy_unresolved
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.381
          - 0.507
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 0.381
          - 0.507
        envelope_mm:
          - "60 x 60 x 115"
          - "50 x 460 x 44"
        scale_class: small
      geometry_form: hollow_rectangular_or_square_thin_wall_gas_duct_segment
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: true
  rationale: "Both rows lack source-resolved alloy metadata and are normalized as broad metal/alloy sheet or thin-wall duct material. Row 147 uses stainless steel only as a planning density, while row 152 uses generic steel with stainless as a nearby scenario. This uncertainty should remain a staging guardrail, but it does not block one closure item because both rows need the same broad rigid metal gas-path material family."
process_review:
  can_unify: true
  rationale: "Both conversions select plumbing_connector_fabrication_testing with cutting, forming, joining, deburring, cleaning, dimensional inspection, and leak testing. Existing process anchors such as sheet_metal_fabrication_v0, sheet_metal_bending_and_forming_v0, tube_stock_forming_v0, welding_brazing_basic_v0, plumbing_and_pneumatics_v0, leak_testing_v0, cleaning_basic_v0, and inspection_basic_v0 support the same closure route for both duct variants."
geometry_review:
  can_unify: true
  rationale: "The CAD previews show the same broad geometry family: small hollow thin-wall duct segments for the gas outlet path. Row 147 is shorter with an approximately square 60 mm section; row 152 is longer with an approximately 50 x 44 mm rectangular section. Those differences affect BOM mapping, cut length, bend/form details, and mating interfaces, but do not require separate closure items at Phase 2."
precision_review:
  blocks_merge: false
  rationale: "Both rows share the same unresolved guardrails: internal cleanliness, seam or edge joining quality, mating-interface fit, and leak tightness after assembly. No row has a distinct calibrated sensor, optical, motion-bearing, standard ISO flange, bellows compliance, or valve-sealing behavior that would force a split."
assumptions:
  - "BOM quantity is 1 for both rows, so row total mass equals per-unit mass."
  - "The previews are treated as stronger geometry evidence than the ambiguous row 152 wording that could read as a wall or flow-guide segment; visually, both rows are hollow duct-like pieces."
  - "Existing KB abstractions such as piping_and_fittings_set, pipe_and_fittings_set, fittings_and_valves, metal_fittings_raw, and the staged gas_outlet_flange_plate_v0 precedent were considered. They are useful context but are too broad or represent different geometry to replace this staged custom duct-segment closure item while preserving gas-path geometry and cleanliness guardrails."
  - "The proposed item ID is a staging suggestion only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Actual alloy, grade, coating, wall thickness, bend allowances, seam method, internal finish, cleaning requirement, and gas leak-rate threshold remain unresolved for both rows."
  - "Mating details to the neighboring 3S31-3S35 and 3S41-3S48 gas outlet groups remain unresolved and should be preserved as Phase 3 BOM mapping guardrails."
  - "Later KB staging should decide whether this custom duct segment reuses a broader local piping or formed-sheet item, or whether the reAM250 gas outlet assembly needs a dedicated staged item with row-specific mappings."
  - "Final local manufacture versus import decision is deferred."
---

# Merge Review

Merge rows 147 and 152 into one staged fabricated gas-outlet duct-segment item. Preserve row-specific length, cross section, material uncertainty, seam details, and mating-interface requirements for Phase 3.
