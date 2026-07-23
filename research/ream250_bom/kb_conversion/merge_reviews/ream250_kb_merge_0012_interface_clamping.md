---
group_id: ream250_kb_merge_0012_interface_clamping
candidate_rows:
  - source_row_number: 279
    item: "83"
    path: research/ream250_bom/ream250_bom_row_0279_83.md
    conversion_section_present: true
  - source_row_number: 390
    item: "4162"
    path: research/ream250_bom/ream250_bom_row_0390_4162.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0279_83.md
    - research/ream250_bom/ream250_bom_row_0390_4162.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0279_83.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0390_4162.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD evidence was reviewed through the row research: row 279 has a partial local exported subfeature but a complete official 120BSR040 STEP mass basis, while row 390 has a complete split clamping-ring preview with hinge and wingnut-side hardware."
rough_match_basis:
  functional_purpose_key: interface_clamping
  mass_window_kg:
    - 0.247
    - 0.265
merge_decision:
  decision: merge
  rationale: "Rows 279 and 390 are duplicate appearances of Pfeiffer Vacuum order number 120BSR040, an ISO-KF DN32-DN40 stainless 304 / EN 1.4301 clamping ring for elastomer-sealed small-flange vacuum hardware. The per-unit masses differ only because row 279 relies on the official complete product STEP after the local row export proved partial, while row 390 uses its complete local STEP. Function, material family, nominal interface, process abstraction, hardware form, and precision guardrails all support one staged closure item with per-row BOM quantity and mass retained."
  proposed_closure_items:
    - item_id: ream250_iso_kf_stainless_clamping_ring_v0
      member_rows:
        - 279
        - 390
      functional_purpose: "clamp an elastomer-sealed ISO-KF DN32-DN40 flange joint in gas or vacuum plumbing"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.247
          - 0.265
        bom_quantity_range:
          - 1
          - 12
        row_total_mass_range_kg:
          - 0.265
          - 2.96
        nominal_interfaces:
          - DN_32_40_ISO_KF
        vendor_order_number: 120BSR040
        scale_class: small
      geometry_form: split_or_hinged_annular_iso_kf_clamp_ring_with_wingnut_tightening_hardware
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: true
  rationale: "Both rows resolve material from the same official Pfeiffer/Busch product route for order number 120BSR040, which identifies stainless steel 1.4301/304. Local STEP material metadata was placeholder-only where mentioned, so both row conversions correctly use official product material evidence rather than embedded CAD material tags."
process_review:
  can_unify: true
  rationale: "Both row conversions select plumbing_connector_fabrication_testing with the same supporting operations: cutting or forming stainless clamp segments, drilling/thread-related hardware work, precision machining of hinge/lug details, assembly, cleaning/passivation, and dimensional inspection. A single process-family abstraction preserves the flange-fit, tightening, cleaning, and seal-interface guardrails."
geometry_review:
  can_unify: true
  rationale: "Both rows identify the same DN32-DN40 ISO-KF split or hinged clamp ring with wingnut-side tightening hardware. Row 279's local CAD preview is partial, but the official product STEP and row identity match row 390's complete split-ring geometry. The small mass difference is within CAD/export uncertainty for the same commercial part, not a geometry-family split."
precision_review:
  blocks_merge: false
  rationale: "Both rows carry the same precision guardrails: ISO-KF flange-standard fit, clamp closure geometry, hinge and tightening alignment, 2 Nm wingnut behavior, elastomer seal compatibility, cleaning/passivation, and leak-service acceptance. These are important Phase 3 guardrails but do not distinguish the two rows."
assumptions:
  - "The proposed item ID intentionally reuses the staged abstraction already used by related ISO-KF stainless clamping-ring merge review work rather than creating a duplicate row-specific item."
  - "Row 279 quantity 12 and row 390 quantity 1 should be preserved in later BOM mappings even though both map to the same closure item."
  - "Wingnut, screw, and hinge details remain inside the clamp hardware item for this merge pass; Phase 3 can split them only if standard fastener reuse materially improves closure accounting."
  - "Existing broad KB items such as fittings sets, hose fittings, and fastener kits are useful conservative context but too generic to preserve DN32-DN40 ISO-KF clamp geometry, seal-loading, and tightening guardrails."
  - "Final import/local manufacture remains deferred to Phase 3 staging."
unresolved:
  - "Exact hinge pin, screw, and wingnut submaterials and thread details."
  - "Vendor production route for the curved stainless clamp body and tightening hardware."
  - "Passivation or cleaning standard, ISO-KF dimensional tolerance class, and leak-rate acceptance threshold for local manufacture."
  - "Phase 3 should decide whether this maps to an existing broad vacuum fittings abstraction, a standard hardware import, or a local-manufacture candidate with precision guardrails."
---

# Merge Review

Rows 279 and 390 merge into the staged ISO-KF stainless clamping-ring abstraction. They are the same Pfeiffer 120BSR040 DN32-DN40 clamp; preserve the row quantities, mass bases, tightening hardware, and flange/seal guardrails for Phase 3.
