---
group_id: ream250_kb_merge_0020_mechanical_fastening
candidate_rows:
  - source_row_number: 106
    item: "2AV7"
    path: research/ream250_bom/ream250_bom_row_0106_2AV7.md
    conversion_section_present: true
  - source_row_number: 355
    item: "619"
    path: research/ream250_bom/ream250_bom_row_0355_619.md
    conversion_section_present: true
  - source_row_number: 267
    item: "61B"
    path: research/ream250_bom/ream250_bom_row_0267_61B.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0106_2AV7.md
    - research/ream250_bom/ream250_bom_row_0355_619.md
    - research/ream250_bom/ream250_bom_row_0267_61B.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0106_2AV7.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0355_619.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0267_61B.md#kb-conversion
  notes: "Read each row's original frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence in the row research established socket-head cap screw and countersunk socket screw geometry; no additional image inspection was needed for this merge decision."
rough_match_basis:
  functional_purpose_key: mechanical_fastening
  mass_window_kg:
    - 0.00351
    - 0.00521
merge_decision:
  decision: merge
  rationale: "All three rows are mild-steel socket-drive screws used for removable mechanical fastening. They differ by DIN head form, nominal thread size, length, per-unit mass, and BOM quantity, but those variations are normal small-fastener variants within the project's reuse policy and should be preserved as BOM mapping guardrails rather than staged as row-specific closure items."
  proposed_closure_items:
    - item_id: fastener_kit_small
      member_rows:
        - 106
        - 355
        - 267
      functional_purpose: "small removable threaded fastening for machine assemblies"
      material: mild_steel
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.00351
          - 0.00521
        bom_quantity_range:
          - 1
          - 8
        row_total_mass_range_kg:
          - 0.00367
          - 0.0281
        nominal_thread_variants:
          - M4x0.7
          - M5
        length_variants_mm:
          - 20
          - 25
          - 30
        scale_class: small
      geometry_form: small_mild_steel_socket_screw_variants
      process_family: fastener_forming_thread_rolling
material_review:
  can_unify: true
  rationale: "Each row resolves to mild steel from STEP material metadata at 7850 kg/m3. Exact property class, coating, heat treatment, and steel grade are unresolved across the group, so no row has material evidence that forces a separate closure item at merge-review stage."
process_review:
  can_unify: true
  rationale: "All three conversions select fastener_forming_thread_rolling. The row routes use standard fastener stock preparation, heading or forming, socket formation, thread rolling, optional heat treatment or coating, and dimensional inspection. Existing KB process fastener_kit_small_fabrication_v0 is the appropriate aggregate process anchor for a kit-level small-fastener closure item."
geometry_review:
  can_unify: true
  rationale: "The rows share small socket-drive screw geometry but include two head families: DIN 912 cylindrical socket-head cap screw for row 106 and DIN 7991 countersunk socket screws for rows 355 and 267. The head form, thread size, and length differences affect installation fit and must be retained in Phase 3 mappings, but they do not defeat a kit-level small-fastener merge."
precision_review:
  blocks_merge: false
  rationale: "Thread size, screw length, head form, socket fit, countersink fit, strength grade, coating, and heat treatment remain guardrails. Current row evidence does not identify any high-strength, sealing-critical, vacuum-critical, or precision-only duty that requires a unique fastener item before staging."
assumptions:
  - "A kit-level closure item is acceptable for these gram-scale standard screws because the KB already contains fastener_kit_small and prior reAM250 merge review precedent uses it for small screw variants."
  - "Phase 3 can preserve row-specific DIN standard, nominal thread, length, quantity, and row mass while mapping all rows to the same small-fastener closure item."
  - "Mild-steel material metadata is adequate for merge review, while unresolved property class and coating details remain promotion guardrails."
unresolved:
  - "Phase 3 must decide whether these rows map directly to existing fastener_kit_small or need a more specific staged subentry for M4 and M5 socket screws."
  - "Property class, coating, heat treatment, exact thread tolerance, socket tolerance, and installed joint duty remain unknown."
  - "Per-row BOM mapping must preserve row 106 as eight DIN 912 M4 x 0.7 x 25 socket-head cap screws, row 355 as one DIN 7991 M5 x 20 countersunk socket screw, and row 267 as one DIN 7991 M5 x 30 countersunk socket screw."
---

# Merge Review

Rows 106, 355, and 267 merge into the existing small-fastener abstraction for KB staging. Preserve the DIN standard, head form, thread size, length, quantity, and unresolved strength/coating details as Phase 3 guardrails.
