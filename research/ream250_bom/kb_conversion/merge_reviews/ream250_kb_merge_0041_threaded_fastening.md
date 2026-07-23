---
group_id: ream250_kb_merge_0041_threaded_fastening
candidate_rows:
  - source_row_number: 111
    item: "2AVC"
    path: research/ream250_bom/ream250_bom_row_0111_2AVC.md
    conversion_section_present: true
  - source_row_number: 107
    item: "2AV8"
    path: research/ream250_bom/ream250_bom_row_0107_2AV8.md
    conversion_section_present: true
  - source_row_number: 102
    item: "2AV3"
    path: research/ream250_bom/ream250_bom_row_0102_2AV3.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0111_2AVC.md
    - research/ream250_bom/ream250_bom_row_0107_2AV8.md
    - research/ream250_bom/ream250_bom_row_0102_2AV3.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0111_2AVC.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0107_2AV8.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0102_2AV3.md#kb-conversion
  notes: "Read each row's original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence in the row research established DIN 912 M8 cylindrical socket-head cap screw geometry in each row; no additional image inspection was needed for this merge decision."
rough_match_basis:
  functional_purpose_key: threaded_fastening
  mass_window_kg:
    - 0.01497
    - 0.0229
merge_decision:
  decision: merge
  rationale: "All three rows are mild-steel DIN 912 M8 socket-head cap screws used for removable threaded fastening. They differ by pitch, length, per-unit mass, and BOM quantity, but those are normal standard-fastener variants within the project's reuse policy and should be preserved as BOM mapping guardrails rather than staged as row-specific closure items."
  proposed_closure_items:
    - item_id: fastener_kit_medium
      member_rows:
        - 111
        - 107
        - 102
      functional_purpose: "medium removable threaded fastening for machine assemblies"
      material: mild_steel
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.01497
          - 0.0229
        bom_quantity_range:
          - 4
          - 30
        row_total_mass_range_kg:
          - 0.0599
          - 0.687
        nominal_thread: M8
        pitch_variants_mm:
          - 1.0
          - 1.25
        length_variants_mm:
          - 20
          - 25
          - 40
        scale_class: small
      geometry_form: din_912_m8_socket_head_cap_screw_variants
      process_family: fastener_forming_thread_rolling
material_review:
  can_unify: true
  rationale: "Each row resolves to mild steel from STEP material metadata at 7850 kg/m3. Exact steel grade, property class, coating, and heat treatment are unresolved across the group, so no row has material evidence that forces a separate closure item at merge-review stage."
process_review:
  can_unify: true
  rationale: "All three conversions select fastener_forming_thread_rolling with forming, thread forming, socket or feature machining, deburring, inspection, and possible heat treatment. Existing KB process fastener_kit_medium_production_v0 provides the closest aggregate closure handle for M6-M12 fastener production and kitting."
geometry_review:
  can_unify: true
  rationale: "The shared geometry is DIN 912 M8 cylindrical socket-head cap screw hardware. The 20 mm, 25 mm, and 40 mm length variants and M8x1 versus M8x1.25 pitch details affect installation fit and must remain Phase 3 mappings, but they do not defeat a kit-level medium-fastener merge."
precision_review:
  blocks_merge: false
  rationale: "Thread pitch and fit, screw length, socket-drive fit, head form, property class, coating, and heat treatment remain guardrails. Current row evidence does not identify a sealing-critical, vacuum-critical, ultra-high-strength, or precision-only duty that requires a unique fastener item before staging."
assumptions:
  - "A kit-level closure item is acceptable for these standard M8 screws because the KB already models grouped fasteners and fastener_kit_medium covers the M6-M12 size range."
  - "Phase 3 can preserve row-specific DIN standard, pitch, length, quantity, and row mass while mapping all rows to one medium-fastener closure item."
  - "Mild-steel material metadata is adequate for merge review, while unresolved grade, property class, coating, and heat treatment remain promotion guardrails."
unresolved:
  - "Phase 3 must decide whether these rows map directly to existing fastener_kit_medium or need a more specific staged subentry for M8 DIN 912 socket-head cap screws."
  - "Property class, coating, heat treatment, exact thread tolerance, socket tolerance, and installed joint duty remain unknown."
  - "Per-row BOM mapping must preserve row 111 as four DIN 912 M8 x 1.25 x 20 socket-head cap screws, row 107 as sixteen DIN 912 M8 x 1 x 25 socket-head cap screws, and row 102 as thirty DIN 912 M8 x 1.25 x 40 socket-head cap screws."
---

# Merge Review

Rows 111, 107, and 102 merge into the existing medium-fastener abstraction for KB staging. Preserve the DIN 912 form, M8 pitch and length variants, BOM quantities, row masses, and unresolved property-class/coating details as Phase 3 guardrails rather than separate closure items.
