---
group_id: ream250_kb_merge_0025_plumbing_connection
candidate_rows:
  - source_row_number: 129
    item: "3O3"
    path: research/ream250_bom/ream250_bom_row_0129_3O3.md
    conversion_section_present: true
  - source_row_number: 130
    item: "3O4"
    path: research/ream250_bom/ream250_bom_row_0130_3O4.md
    conversion_section_present: true
  - source_row_number: 145
    item: "3S1"
    path: research/ream250_bom/ream250_bom_row_0145_3S1.md
    conversion_section_present: true
  - source_row_number: 253
    item: "37"
    path: research/ream250_bom/ream250_bom_row_0253_37.md
    conversion_section_present: true
  - source_row_number: 335
    item: "422"
    path: research/ream250_bom/ream250_bom_row_0335_422.md
    conversion_section_present: true
  - source_row_number: 119
    item: "3H"
    path: research/ream250_bom/ream250_bom_row_0119_3H.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0129_3O3.md
    - research/ream250_bom/ream250_bom_row_0130_3O4.md
    - research/ream250_bom/ream250_bom_row_0145_3S1.md
    - research/ream250_bom/ream250_bom_row_0253_37.md
    - research/ream250_bom/ream250_bom_row_0335_422.md
    - research/ream250_bom/ream250_bom_row_0119_3H.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0129_3O3.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0130_3O4.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0145_3S1.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0253_37.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0335_422.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0119_3H.md#kb-conversion
  notes: "Read every candidate row's frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence in the row research was used to compare annular bellows end pieces, the custom shallow gas-outlet plate, the DN63-to-DN50 reducer, the DN100 weld flange, and the DN63 straight full nipple."
rough_match_basis:
  functional_purpose_key: plumbing_connection
  mass_window_kg:
    - 0.412
    - 0.814
merge_decision:
  decision: partial_merge
  rationale: "The rough plumbing_connection pool correctly groups vacuum/gas plumbing hardware, but one closure item would erase standard-interface and geometry guardrails. Rows 129 and 130 are the same DN63 ISO-K stainless bellows end-piece geometry at the same mass and material, so they should merge. Rows 119, 253, 335, and 145 should stay separate staged items: a straight DN63 full nipple, a DN63 ISO-K to DN50 ISO-KF reducer, a DN100 ISO-K weld flange, and a custom gas-outlet flange plate are not length variants of one part."
  proposed_closure_items:
    - item_id: ream250_dn63_iso_k_bellows_end_fitting_v0
      member_rows:
        - 129
        - 130
      functional_purpose: "rigid flanged end connection for a DN63 flexible bellows assembly"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.412
        bom_quantity_range:
          - 1
          - 1
        row_total_mass_range_kg:
          - 0.412
          - 0.412
        nominal_interface: DN63_ISO-K
        scale_class: small
      geometry_form: annular_dn63_iso_k_bellows_end_fitting_with_stepped_bore
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn63_iso_k_full_nipple_v0
      member_rows:
        - 119
      functional_purpose: "rigid straight flanged connection section between DN63 ISO-K components"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.814
        bom_quantity: 1
        row_total_mass_kg: 0.814
        nominal_interface: DN63_ISO-K
        scale_class: small
      geometry_form: straight_cylindrical_tube_with_iso_k_flange_lips
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn63_to_dn50_vacuum_reducer_adapter_v0
      member_rows:
        - 253
      functional_purpose: "vacuum plumbing adapter reducing DN63 ISO-K to DN50 ISO-KF"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.605
        bom_quantity: 2
        row_total_mass_kg: 1.21
        nominal_interfaces:
          - DN63_ISO-K
          - DN50_ISO-KF
        scale_class: small
      geometry_form: short_axisymmetric_flanged_reducer_adapter
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_dn100_iso_k_weld_flange_v0
      member_rows:
        - 335
      functional_purpose: "clamp and seal interface welded to a DN100 vacuum line or chamber port"
      material: stainless_steel
      scale_or_capacity:
        per_unit_mass_kg: 0.637
        bom_quantity: 1
        row_total_mass_kg: 0.637
        nominal_interface: DN100_ISO-K
        scale_class: medium
      geometry_form: iso_k_dn100_weld_flange_ring
      process_family: plumbing_connector_fabrication_testing
    - item_id: ream250_gas_outlet_flange_plate_v0
      member_rows:
        - 145
      functional_purpose: "custom gas-outlet flange/interface plate joining local outlet hardware"
      material: unknown_structural_metal_alloy
      scale_or_capacity:
        per_unit_mass_kg: 0.48
        bom_quantity: 1
        row_total_mass_kg: 0.48
        envelope_mm: "130 x 8 x 130"
        scale_class: small
      geometry_form: shallow_round_square_flange_plate_with_central_square_aperture_radial_webs_and_mounting_holes
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: false
  rationale: "Rows 129, 130, 119, and 253 normalize to stainless_steel_304, and row 335 is a stainless vacuum-flange alloy family close enough for stainless planning. Row 145 remains unknown structural metal/alloy with stainless only inferred from gas-outlet context. Material does not block the row 129/130 merge, but the full six-row pool should not be forced into one material identity."
process_review:
  can_unify: false
  rationale: "Rows 129, 130, 119, 253, and 335 all use plumbing_connector_fabrication_testing with turning/machining, cleaning, leak testing, and inspection. Row 145 uses sheet_plate_cutting_drilling with local precision machining because it is a shallow custom flange plate. Even among the plumbing connector rows, process unification should not imply one interchangeable closure item because the connector standards and geometry differ."
geometry_review:
  can_unify: false
  rationale: "Rows 129 and 130 share the same short annular DN63 bellows end-piece geometry and mass. The other rows are distinct geometry classes: a straight flanged tube, a stepped reducer adapter, a DN100 weld-flange ring, and a shallow square/round gas-outlet plate with a central square aperture and radial webs."
precision_review:
  blocks_merge: true
  rationale: "Standard-interface and sealing guardrails block one all-rows merge. DN63 ISO-K bellows end fit, DN63 ISO-K full-nipple length and lips, DN63-to-DN50 reducer concentricity, DN100 weld-flange dimensions, and the custom plate's hole pattern/flatness must remain separate until staging proves a broader kit-level abstraction is acceptable."
assumptions:
  - "Existing KB items such as piping_and_fittings_set, pipe_and_fittings_set, fittings_and_valves, hose_fittings, and metal_fittings_raw were considered as conservative equivalents; they are useful coarse context but too broad or bulk-modeled to preserve ISO-K/KF vacuum interface guardrails for these reAM250 rows."
  - "The row 129 and 130 end pieces are treated as duplicate/near-duplicate ends from the same Pfeiffer 320SFK063 bellows product family, not as left/right parts requiring separate closure items."
  - "The proposed item IDs are staging suggestions only; this task does not write KB YAML and final import/local manufacture remains deferred."
  - "Stainless 304 and stainless vacuum-flange alloy are close enough for process-family comparison, but exact alloy grade remains a staging guardrail where the row evidence is unresolved."
unresolved:
  - "Exact ISO-K/KF flange tolerances, sealing-face roughness, cleanliness/passivation requirements, weld procedures, and helium leak-rate thresholds remain unresolved for the vacuum connector rows."
  - "Row 145 material, mating seal type, and whether its radial web geometry is function-critical remain unresolved."
  - "Later KB staging should decide whether some connector rows can be represented by an ISO vacuum fittings kit while preserving quantities, nominal interfaces, and high-vacuum guardrails."
  - "Final local manufacture versus import decisions are deferred for all proposed closure items."
---

# Merge Review

Rows 129 and 130 merge into one DN63 ISO-K bellows end-fitting staged item. Keep rows 119, 253, 335, and 145 as separate staged plumbing/interface items because their standard interfaces, geometry forms, and precision guardrails are materially different.
