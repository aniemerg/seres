---
group_id: ream250_kb_merge_0008_gas_flow_routing
candidate_rows:
  - source_row_number: 158
    item: "3S47"
    path: research/ream250_bom/ream250_bom_row_0158_3S47.md
    conversion_section_present: true
  - source_row_number: 153
    item: "3S42"
    path: research/ream250_bom/ream250_bom_row_0153_3S42.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0158_3S47.md
    - research/ream250_bom/ream250_bom_row_0153_3S42.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0158_3S47.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0153_3S42.md#kb-conversion
  notes: "Read both rows' original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected the referenced CAD preview PNGs: row 158 is a narrow 8 x 50 x 90.7 mm formed panel with lips and creases, while row 153 is a wider 43 x 50 x 90.7 mm folded sheet duct segment."
rough_match_basis:
  functional_purpose_key: gas_flow_routing
  mass_window_kg:
    - 0.0359
    - 0.041
merge_decision:
  decision: merge
  rationale: "Both rows should converge to one formed gas-outlet routing panel closure item. They share the same role as passive sheet-metal segments in the reAM250 gas outlet subassembly, nearly identical 90.7 mm height and 50 mm width scale, unresolved corrosion-resistant metal sheet material family, sheet_plate_cutting_drilling process bucket with forming and cleaning support, and comparable guardrails for bend geometry, mating-edge fit, gas-path cleanliness, and assembly sealing. The 8 mm versus 43 mm depth difference and fold-pattern details are row-specific panel variants, not blockers for one closure item under the project's reuse policy."
  proposed_closure_items:
    - item_id: ream250_formed_gas_outlet_routing_panel_v0
      member_rows:
        - 158
        - 153
      functional_purpose: "formed passive panel that routes gas through a segment of the reAM250 gas outlet assembly"
      material: metal_sheet_alloy_unresolved
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.0359
          - 0.041
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 0.0359
          - 0.041
        envelope_mm:
          - "8 x 50 x 90.7"
          - "43 x 50 x 90.7"
        scale_class: small
      geometry_form: formed_thin_sheet_gas_outlet_routing_panel
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: true
  rationale: "Both rows have unresolved STEP material metadata and use stainless-density planning masses only as conservative estimates. Row 158 normalizes to unresolved corrosion-resistant metal, and row 153 normalizes to unresolved metal sheet. This uncertainty should remain a Phase 3 material guardrail, but it does not block one closure item because both rows need the same broad rigid metal sheet family for a gas outlet panel exposed to powder-bed-fusion gas-path conditions."
process_review:
  can_unify: true
  rationale: "Both row conversions keep the original sheet-metal cutting and forming family, selecting sheet_plate_cutting_drilling with stock preparation, cutting, forming, deburring, cleaning, joining, and dimensional inspection support. Row 153 additionally flags leak testing, while row 158 flags assembly-level joining; both are compatible assembly-level guardrails for the same coarse closure route."
geometry_review:
  can_unify: true
  rationale: "The CAD previews show the same broad geometry family: thin folded panels in the neighboring 3S41 through 3S48 gas outlet part set. Row 158 is narrower in depth with lip and crease features, while row 153 is deeper and more duct-like. Those differences should be preserved in BOM mappings, bend details, and outlet-fit guardrails, but they do not require separate closure items at merge review."
precision_review:
  blocks_merge: false
  rationale: "Neither row shows evidence of calibrated sensing, optical alignment, bearing contact, standardized vacuum-flange geometry, or a unique precision interface that would force a split. Both rows share review-level requirements for bend accuracy, mating-edge fit, surface cleanliness, and gas-path assembly sealing."
assumptions:
  - "BOM quantity is 1 for both rows, so row total mass equals per-unit mass."
  - "The CAD previews are treated as sufficient geometry evidence for Phase 2 because both source rows explicitly reference the rendered views and the forms are visually comparable."
  - "Steel-density mass estimates are retained as conservative planning values, not resolved material evidence."
  - "Existing KB abstractions such as formed_sheet_metal_parts, gas_outlet_manifold, air_ducting_system, and ductwork_and_fittings were considered. They are useful context but too broad or bulk-modeled to preserve row-level gas-outlet geometry, bend, and cleanliness guardrails."
  - "The proposed item ID is a staging suggestion only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Actual alloy, thickness, bend radii, bend sequence, edge treatment, coating, surface finish, attachment method, and allowable gas-path contamination level remain unresolved for both rows."
  - "The exact installed positions and mating interfaces within the larger 3S41 through 3S48 gas outlet subassembly remain unresolved and should be retained as Phase 3 BOM mapping guardrails."
  - "Later KB staging should compare this staged routing-panel item with ream250_kb_merge_0006_gas_flow_guidance before promotion, because those rows appear to be adjacent variants in the same gas outlet sheet-panel family."
  - "Final local manufacture versus import decision is deferred."
---

# Merge Review

Merge rows 158 and 153 into one staged formed gas-outlet routing panel item. Preserve row-specific depth, fold profile, material uncertainty, edge fit, cleanliness, and assembly-sealing requirements for Phase 3.
