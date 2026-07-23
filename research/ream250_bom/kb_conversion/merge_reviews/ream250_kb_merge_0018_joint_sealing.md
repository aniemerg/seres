---
group_id: ream250_kb_merge_0018_joint_sealing
candidate_rows:
  - source_row_number: 307
    item: "173"
    path: research/ream250_bom/ream250_bom_row_0307_173.md
    conversion_section_present: true
  - source_row_number: 218
    item: "14"
    path: research/ream250_bom/ream250_bom_row_0218_14.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0307_173.md
    - research/ream250_bom/ream250_bom_row_0218_14.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0307_173.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0218_14.md#kb-conversion
  notes: "Reviewed function, mass basis, material evidence, manufacturing route, KB implications, CAD-derived geometry summaries, and KB Conversion decisions for both candidate rows."
rough_match_basis:
  functional_purpose_key: joint_sealing
  mass_window_kg:
    - 0.0505
    - 0.0956
merge_decision:
  decision: merge
  rationale: "Both rows are applied black silicone sealant beads for elastic sealing of reAM250 plate or housing joints. The material families, process abstraction, scale class, and precision needs are compatible with one closure item. The different bead envelopes and BOM quantities should remain row-specific mapping details during Phase 3 rather than forcing separate closure items."
  proposed_closure_items:
    - item_id: dispensed_silicone_joint_sealant_application_v0
      member_rows:
        - 307
        - 218
      functional_purpose: "Applied elastomeric sealant bead for sealing mating machine panel, plate, and housing joints."
      material: silicone_elastomer_sealant
      scale_or_capacity:
        per_application_mass_kg_range:
          - 0.0505
          - 0.0956
        bom_quantity_range:
          - 1
          - 2
        row_total_mass_kg_range:
          - 0.0505
          - 0.191
        scale_class: small
      geometry_form: "Thin dispensed rectangular perimeter bead; exact path, envelope, bead height, and installed volume remain BOM-row attributes."
      process_family: polymer_elastomer_forming_dispensing
material_review:
  can_unify: true
  rationale: "Rows 307 and 218 both identify Liqui Moly 6185 black silicone sealing compound, with row 218 adding neutral-crosslinked no-MEKO detail. For closure modeling these are compatible as silicone elastomer sealant. Exact formulation, filler package, and cure chemistry remain import and promotion guardrails."
process_review:
  can_unify: true
  rationale: "Both conversions select polymer_elastomer_forming_dispensing and describe the same practical route: clean mating surfaces, dispense continuous bead, join parts, cure, and inspect. Candidate KB anchors include sealing_and_assembly_basic_v0, potting_and_sealing_v0, seal_installation_v0, silicone_rubber_vulcanization_v0, cleaning_basic_v0, leak_testing_v0, and inspection_basic_v0."
geometry_review:
  can_unify: true
  rationale: "The CAD-derived bead shapes are different rectangular perimeter applications, but both are thin dispensed gasket beads. Geometry differences affect per-row quantity, bead path, bead height, and mass, not the closure item identity."
precision_review:
  blocks_merge: false
  rationale: "Precision concerns are shared sealing guardrails: continuous coverage, bead thickness or height, surface cleanliness, compression state, cure condition, and chemical compatibility. These guardrails do not require separate closure items."
assumptions:
  - "Both STEP solids represent installed or cured sealant volume rather than procurement package mass."
  - "The closure item should represent consumed sealant application material and process capability, not a reusable discrete gasket."
  - "Phase 3 should preserve row 218 quantity two and row-specific total mass while using the shared closure item."
unresolved:
  - "Final import/local manufacture decision for silicone sealant chemistry remains deferred to Phase 3."
  - "Exact cured formulation, filler content, cure time, compression load, service environment, and leak-test acceptance criteria are not specified by the row evidence."
---

Merge review for `ream250_kb_merge_0018_joint_sealing`.
