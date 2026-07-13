---
group_id: ream250_kb_merge_0022_plumbing_connection
candidate_rows:
  - source_row_number: 210
    item: "8D1"
    path: research/ream250_bom/ream250_bom_row_0210_8D1.md
    conversion_section_present: true
  - source_row_number: 211
    item: "8D2"
    path: research/ream250_bom/ream250_bom_row_0211_8D2.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0210_8D1.md
    - research/ream250_bom/ream250_bom_row_0211_8D2.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0210_8D1.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0211_8D2.md#kb-conversion
  notes: "Read both candidate rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD preview and STEP-derived geometry evidence were used to compare the two thin annular stainless DN40 ISO-KF flexible-pipe end components."
rough_match_basis:
  functional_purpose_key: plumbing_connection
  mass_window_kg:
    - 0.00249
    - 0.00249
merge_decision:
  decision: merge
  rationale: "Rows 210 and 211 are same-product, same-mass stainless 304 annular end/flange subparts of the Pfeiffer 120SWG040-0250 DN40 ISO-KF flexible pipe. Both have the same CAD-derived volume, nearly identical envelope dimensions, same BOM quantity, same normalized plumbing-connection function, same plumbing_connector_fabrication_testing process family, and compatible sealing, concentricity, cleaning, and joining guardrails. Treating them as one closure item preserves the distinction from the complete flexible hose while avoiding duplicate end-ring items for the two hose ends."
  proposed_closure_items:
    - item_id: ream250_dn40_iso_kf_flexible_hose_end_ring_v0
      member_rows:
        - 210
        - 211
      functional_purpose: "provide the circular end connection interface for a DN40 flexible plumbing hose assembly"
      material: stainless_steel_304
      scale_or_capacity:
        per_unit_mass_kg: 0.00249
        bom_quantity_per_row: 1
        member_row_total_mass_kg:
          - 0.00249
          - 0.00249
        combined_row_total_mass_kg: 0.00498
        nominal_interface: DN40_ISO-KF
        scale_class: tiny
      geometry_form: thin_annular_hose_end_ring
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: true
  rationale: "Both rows normalize to stainless_steel_304 based on the same Pfeiffer 120SWG040-0250 product-family evidence. The source notes distinguish 316L bellows material for the complete hose, but these two exported annular end/flange subparts are assigned to the stainless 304 flange material."
process_review:
  can_unify: true
  rationale: "Both KB Conversion sections select plumbing_connector_fabrication_testing with supporting stock preparation, forming, precision machining, joining, cleaning, leak testing, and dimensional inspection. Any difference between turning and forming is a route-level option inside the same closure process family, not a reason to split the closure item."
geometry_review:
  can_unify: true
  rationale: "Both rows are thin annular hose-end rings from the same DN40 flexible pipe, with identical CAD-derived volume and matching approximately 5.32 x 56.28 x 56.28 mm bounding boxes. The labels part 1 and part 2 are best treated as two instances or counterpart ends of the same hose-end closure item rather than separate geometry classes."
precision_review:
  blocks_merge: false
  rationale: "The guardrails are compatible: DN40 ISO-KF mating fit, sealing/interface finish, concentricity, clean joining surfaces, hose integration, leak testing, and service cleanliness apply equally to both rows. These guardrails should remain on the merged staged item but do not block merging the two end-ring rows."
assumptions:
  - "Existing KB abstractions such as piping_and_fittings_set, metal_fittings_raw, coolant_piping, crimped_hydraulic_hose_v0, and hydraulic_hose_segment_v0 were considered as conservative reuse context; they are too broad, too massive, bulk-scoped, polymer-hose scoped, or otherwise mismatched for this tiny stainless DN40 ISO-KF hose-end ring while preserving row-specific mass and interface guardrails."
  - "Rows 210 and 211 are treated as counterpart end-ring parts from the same Pfeiffer flexible pipe rather than separate closure items, because their mass, material, geometry evidence, and process abstraction are effectively identical."
  - "The proposed item ID is a staging suggestion only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
  - "Vacuum service is preserved through sealing, cleanliness, leak-test, and interface guardrails rather than as a functional-purpose key axis."
unresolved:
  - "Exact DN40 ISO-KF profile tolerances, sealing-face roughness, passivation or cleaning specification, weld or joining procedure, and leak-rate acceptance threshold remain unresolved."
  - "The complete flexible hose still needs separate staging for bellows or corrugated hose fabrication, end joining, and hose-level leak testing."
  - "The source CAD may omit small weld beads, rolled edges, or end-piece details; staging should preserve the 0.00249 kg per-row mass as CAD-derived evidence with that uncertainty."
  - "Final local manufacture versus import decision is deferred to Phase 3 staging."
---

# Merge Review

Merge rows 210 and 211 as one DN40 ISO-KF flexible hose-end ring closure item. They are same-product stainless annular end components with identical mass and compatible process, geometry, and precision guardrails; the complete flexible hose remains a separate staging concern.
