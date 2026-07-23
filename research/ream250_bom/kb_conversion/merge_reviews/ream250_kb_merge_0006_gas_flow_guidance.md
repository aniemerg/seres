---
group_id: ream250_kb_merge_0006_gas_flow_guidance
candidate_rows:
  - source_row_number: 157
    item: "3S46"
    path: research/ream250_bom/ream250_bom_row_0157_3S46.md
    conversion_section_present: true
  - source_row_number: 154
    item: "3S43"
    path: research/ream250_bom/ream250_bom_row_0154_3S43.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0157_3S46.md
    - research/ream250_bom/ream250_bom_row_0154_3S43.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0157_3S46.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0154_3S43.md#kb-conversion
  notes: "Read both rows' original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected the referenced CAD preview PNGs: row 157 is a narrow 14 x 50 x 90.7 mm folded vane panel, and row 154 is a wider 35 x 50 x 90.7 mm folded/faceted gas outlet panel."
rough_match_basis:
  functional_purpose_key: gas_flow_guidance
  mass_window_kg:
    - 0.0362
    - 0.039
merge_decision:
  decision: merge
  rationale: "Both rows should converge to one formed gas-outlet flow-guide panel closure item. They share the same passive gas-flow guidance function, small scale, unresolved metal sheet material family, sheet_plate_cutting_drilling process bucket with forming and cleaning support, and similar bend/profile, edge-quality, outlet-fit, and gas-path-cleanliness guardrails. The width and fold-pattern differences are row-specific panel variants within the project's reuse policy rather than blockers for a shared closure item."
  proposed_closure_items:
    - item_id: ream250_formed_gas_outlet_flow_guide_panel_v0
      member_rows:
        - 157
        - 154
      functional_purpose: "formed passive panel that deflects, shields, or guides gas flow inside the reAM250 gas outlet path"
      material: metal_sheet_alloy_unresolved
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.0362
          - 0.039
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 0.0362
          - 0.039
        envelope_mm:
          - "14 x 50 x 90.7"
          - "35 x 50 x 90.7"
        scale_class: small
      geometry_form: formed_thin_sheet_gas_outlet_vane_panel
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: true
  rationale: "Both rows have unresolved STEP material metadata and use steel-density planning masses only as conservative estimates. Row 157 is normalized as unknown sheet metal/alloy, while row 154 is normalized as unknown structural metal with steel assumed for mass. This should remain a Phase 3 material guardrail, but it does not block one closure item because both rows need the same broad rigid metal sheet family for a gas-path guide panel."
process_review:
  can_unify: true
  rationale: "Both row conversions keep the original sheet metal cutting and forming family, selecting sheet_plate_cutting_drilling with stock preparation, cutting, forming, deburring, cleaning, and dimensional inspection. The candidate process anchors differ slightly by row, but cutting_basic_v0 or sheet_metal_cutting_v0 plus sheet_metal_bending_and_forming_v0, cleaning_basic_v0, surface_finishing_basic_v0, and inspection_basic_v0 support the same coarse closure route."
geometry_review:
  can_unify: true
  rationale: "The CAD previews show the same broad geometry family: small thin bent or faceted panels in the gas outlet assembly. Row 157 is narrower and vane-like, while row 154 is wider with a similar height and faceted fold structure. Those geometry differences should be preserved in BOM mappings, bend details, and outlet-fit guardrails, but they do not require separate closure items at merge review."
precision_review:
  blocks_merge: false
  rationale: "Neither row shows evidence of calibrated sensing, optical alignment, bearing motion, precision sealing hardware, standard flange geometry, or other precision behavior that would force a split. Both rows share review-level requirements for formed profile, edge quality, fit against neighboring outlet pieces, surface finish, and gas-path cleanliness."
assumptions:
  - "BOM quantity is 1 for both rows, so row total mass equals per-unit mass."
  - "The CAD previews are treated as sufficient geometry evidence for Phase 2 merge review because both source rows explicitly reference the rendered views and the forms are visually comparable."
  - "Steel-density mass estimates are retained as conservative planning values, not resolved material evidence."
  - "The proposed item ID is a staging suggestion only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Actual alloy, thickness, bend radii, coating, surface finish, edge treatment, attachment method, and allowable gas-path contamination level remain unresolved for both rows."
  - "The exact position and mating interfaces within the larger 3S41 through 3S48 gas outlet subassembly remain unresolved and should be retained as Phase 3 BOM mapping guardrails."
  - "Later KB staging should decide whether this staged closure item reuses a broader existing formed-sheet component, creates a reAM250-specific formed gas outlet guide item, or is folded into a larger gas outlet subassembly."
  - "Final local manufacture versus import decision is deferred."
---

# Merge Review

Merge rows 157 and 154 into one staged formed gas-outlet flow-guide panel item. Preserve row-specific width, fold profile, material uncertainty, edge condition, cleanliness, and outlet-fit requirements for Phase 3.
