---
group_id: ream250_kb_merge_0040_threaded_fastening
candidate_rows:
  - source_row_number: 349
    item: "613"
    path: research/ream250_bom/ream250_bom_row_0349_613.md
    conversion_section_present: true
  - source_row_number: 348
    item: "612"
    path: research/ream250_bom/ream250_bom_row_0348_612.md
    conversion_section_present: true
  - source_row_number: 109
    item: "2AVA"
    path: research/ream250_bom/ream250_bom_row_0109_2AVA.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0349_613.md
    - research/ream250_bom/ream250_bom_row_0348_612.md
    - research/ream250_bom/ream250_bom_row_0109_2AVA.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0349_613.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0348_612.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0109_2AVA.md#kb-conversion
  notes: "Read each row's original function, mass, material, how_to_make, kb_implications, and KB Conversion section. CAD preview evidence had already established DIN 912 M4 socket-head screw geometry in each row; no additional image inspection was needed for this merge decision."
rough_match_basis:
  functional_purpose_key: threaded_fastening
  mass_window_kg:
    - 0.00184
    - 0.00302
merge_decision:
  decision: merge
  rationale: "All three rows are mild-steel DIN 912 M4 socket-head cap screws used for removable threaded fastening. They differ by screw length, per-unit mass, and BOM quantity, but those variations are within the project's reuse policy and are better handled as kit/member guardrails than as row-specific closure items."
  proposed_closure_items:
    - item_id: fastener_kit_small
      member_rows:
        - 349
        - 348
        - 109
      functional_purpose: "small removable threaded fastening for machine assemblies"
      material: mild_steel
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 0.00184
          - 0.00302
        bom_quantity_range:
          - 1
          - 20
        row_total_mass_range_kg:
          - 0.00184
          - 0.0604
        nominal_thread: M4x0.7
        length_variants_mm:
          - 8
          - 16
          - 20
        scale_class: small
      geometry_form: din_912_m4_socket_head_cap_screw_variants
      process_family: fastener_forming_thread_rolling
material_review:
  can_unify: true
  rationale: "Each row resolves to mild steel from STEP metadata at 7850 kg/m3. Exact grade, coating, heat treatment, and property class are unresolved in all three rows, so no material distinction blocks a shared small-fastener abstraction."
process_review:
  can_unify: true
  rationale: "All three conversions select fastener_forming_thread_rolling with forming, thread forming, deburring, inspection, and possible heat treatment. Existing KB process fastener_kit_small_fabrication_v0 already provides an aggregate closure handle for small fastener production and kitting."
geometry_review:
  can_unify: true
  rationale: "The shared geometry is DIN 912 M4 socket-head cap screw hardware. Length differs across 8 mm, 16 mm, and 20 mm variants, but the head style, thread size, socket drive role, and small-fastener use are compatible with one closure item or kit-level abstraction."
precision_review:
  blocks_merge: false
  rationale: "Thread size, pitch, socket fit, head style, length, coating, and property class must remain staging guardrails, but none is currently known to require a unique precision item. If later evidence assigns high-strength or sealed/vacuum-critical duty to one row, it can split at staging."
assumptions:
  - "A kit-level closure item is acceptable for these small M4 screws because the KB already models grouped small fasteners and the rows are below the mass/complexity threshold for individual screw recipes."
  - "The existing fastener_kit_small item is a better staging target than inventing a new M4 socket-head screw item unless later reAM250-specific staging needs exact per-size inventory."
  - "Mild-steel material metadata is sufficient for merge review even though supplier grade and strength class are not specified."
unresolved:
  - "Final staging must decide whether to represent these as consumed mass from fastener_kit_small or as a more specific M4 socket-head subentry inside a kit."
  - "Fastener property class, coating, exact steel grade, thread tolerance, socket tolerance, and installed joint duty remain unknown."
  - "Row 109 has quantity 20 and 0.0604 kg row total; staging should preserve that quantity even if it uses a shared closure item."
---

# Merge Review

Rows 349, 348, and 109 merge into the existing small fastener abstraction for KB staging. Preserve M4 DIN 912 length variants and unresolved property-class/coating details as guardrails rather than separate closure items.
