---
group_id: ream250_kb_merge_0013_interface_sealing
candidate_rows:
  - source_row_number: 13
    item: "1B42"
    path: research/ream250_bom/ream250_bom_row_0013_1B42.md
    conversion_section_present: true
  - source_row_number: 140
    item: "3Q3"
    path: research/ream250_bom/ream250_bom_row_0140_3Q3.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0013_1B42.md
    - research/ream250_bom/ream250_bom_row_0140_3Q3.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0013_1B42.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0140_3Q3.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. CAD preview evidence in the row research was used to compare the 210 x 297 x 3 mm flat rectangular frame gasket with the thin annular DN100 ISO-K centering ring and elastomer O-ring."
rough_match_basis:
  functional_purpose_key: interface_sealing
  mass_window_kg:
    - 0.0144
    - 0.0177
merge_decision:
  decision: split
  rationale: "The rough pool correctly groups two low-mass interface-sealing parts, but they should not converge to one closure item. Row 13 is a custom flat compressible sheet gasket cut to rectangular-frame geometry. Row 140 is standard DN100 ISO-K centering and sealing hardware with an aluminum locating ring plus NBR O-ring. The material stack, geometry form, standard flange interface, process route, and precision guardrails differ enough that one closure item would hide important staging decisions."
  proposed_closure_items:
    - item_id: ream250_flat_rectangular_frame_gasket_v0
      member_rows:
        - 13
      functional_purpose: "compressible perimeter seal between flat mating faces"
      material: gasket_elastomer_material_unresolved
      scale_or_capacity:
        per_unit_mass_kg: 0.0144
        bom_quantity: 2
        row_total_mass_kg: 0.0287
        thickness_mm: 3
        planar_size_mm: "210 x 297"
        scale_class: small
      geometry_form: flat_rectangular_frame_gasket_with_large_center_opening
      process_family: polymer_elastomer_forming_dispensing
    - item_id: ream250_dn100_iso_k_centering_ring_seal_v0
      member_rows:
        - 140
      functional_purpose: "center and seal a DN100 ISO-K flanged gas interface"
      material: aluminum_outer_ring_with_nbr_o_ring
      scale_or_capacity:
        per_unit_mass_kg: 0.0177
        bom_quantity: 2
        row_total_mass_kg: 0.0355
        nominal_interface: DN100_ISO-K
        scale_class: tiny
      geometry_form: thin_annular_centering_ring_with_elastomer_o_ring
      process_family: plumbing_connector_fabrication_testing
material_review:
  can_unify: false
  rationale: "Row 13 has unresolved LiSEMA flat-gasket material and may be silicone, EPDM, NBR, FKM, PTFE, fiber, graphite, foam, or another gasket-sheet compound. Row 140 has row-matched evidence for an aluminum outer ring with an NBR O-ring. Both contain elastomeric sealing behavior, but the metal centering-ring dependency and known NBR allocation make row 140 materially different from a sheet-cut flat gasket."
process_review:
  can_unify: false
  rationale: "Row 13 selects polymer_elastomer_forming_dispensing with gasket-sheet cutting, edge cleanup, and dimensional inspection. Row 140 selects plumbing_connector_fabrication_testing with aluminum ring machining, O-ring installation, cleaning, dimensional inspection, and leak-test context. Existing KB processes such as gasket_sheet_cut_to_part_v0, seal_installation_v0, elastomer_molding_basic_v0, machining_basic_v0, vacuum_seal_assembly_fabrication_v0, and leak_testing_v0 are useful anchors, but the two rows do not share a single primary process family."
geometry_review:
  can_unify: false
  rationale: "The CAD-derived geometry forms are not size variants of one part family. Row 13 is a flat rectangular frame gasket about 210 x 297 x 3 mm with a large central opening. Row 140 is a thin annular DN100 ISO-K centering ring with an elastomer O-ring and flange-standard interface dimensions."
precision_review:
  blocks_merge: true
  rationale: "Both parts need seal compression and material compatibility guardrails, but row 140 additionally carries flange-standard fit, centering accuracy, O-ring seating, mixed-material allocation, and leak-test context. Row 13 instead carries flat-sheet thickness, perimeter geometry, and unknown gasket-compound compatibility. These precision and interface differences block a single closure item."
assumptions:
  - "Existing KB items sealing_gaskets, gasket_sheet_part_v0, gasket_sheet, and seal_o_ring_rubber were considered as conservative reuse targets. They are relevant Phase 3 candidates, especially for row 13, but merge review keeps row 140 separate because a simple O-ring item does not include the aluminum centering ring and DN100 ISO-K interface."
  - "The two rows have similar per-unit masses only because both are small seal-related parts; mass similarity is not enough to merge across flat gasket and standard centering-ring geometries."
  - "Vacuum service is retained as sealing, flange-fit, cleanliness, and leak-test guardrails, not as a functional-purpose key axis."
  - "Proposed item IDs are staging suggestions only; this merge review does not write KB YAML and does not decide final import versus local manufacture."
unresolved:
  - "Row 13 exact gasket compound, hardness, compression set, temperature rating, chemical compatibility, and sealed medium remain unresolved."
  - "Row 140 aluminum alloy grade, actual aluminum-to-NBR mass split, O-ring specification beyond NBR family, seal compression, and leak-rate acceptance remain unresolved."
  - "Phase 3 should decide whether row 13 can reuse sealing_gaskets or gasket_sheet_part_v0 while preserving the 210 x 297 x 3 mm custom frame geometry and quantity."
  - "Phase 3 should decide whether row 140 becomes a new DN100 ISO-K centering-ring seal staged item, maps to a broader vacuum fittings abstraction, or remains an import due to standard flange-seal reliability requirements."
---

# Merge Review

Split the interface-sealing pool into two staged closure items. The rows share a broad sealing role and similar mass, but the flat sheet gasket and the DN100 ISO-K centering-ring seal differ in material stack, geometry, process family, and precision guardrails.
