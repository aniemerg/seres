---
group_id: ream250_kb_merge_0011_interface_clamping
candidate_rows:
  - source_row_number: 364
    item: "1751"
    path: research/ream250_bom/ream250_bom_row_0364_1751.md
    conversion_section_present: true
  - source_row_number: 173
    item: "6C3"
    path: research/ream250_bom/ream250_bom_row_0173_6C3.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0364_1751.md
    - research/ream250_bom/ream250_bom_row_0173_6C3.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0364_1751.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0173_6C3.md#kb-conversion
  notes: "Read both rows' frontmatter, function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected both referenced CAD preview PNGs: row 364 is a 95 x 10 x 95 mm annular optical-window cover/retainer with central aperture and four mounting holes, while row 173 is a 265 x 3.5 x 20 mm long profiled stainless blade-mount strip with angled end features."
rough_match_basis:
  functional_purpose_key: interface_clamping
  mass_window_kg:
    - 0.0748
    - 0.133
merge_decision:
  decision: split
  rationale: "The rough interface_clamping key correctly grouped two small plate or strip parts that retain an interface, but the rows should not collapse into one closure item. Row 364 clamps or shields an optical FLIR-window and seal stack around a central aperture. Row 173 is a recoater blade mount clamp, spacer, or backing strip along a blade span. Their material evidence, geometry form, mating interfaces, and precision guardrails are different enough to preserve separate staged closure items."
  proposed_closure_items:
    - item_id: ream250_optical_window_retainer_plate_v0
      member_rows:
        - 364
      functional_purpose: "retain or clamp an optical window and seal stack while leaving the viewing aperture open"
      material: unresolved_machined_metal
      scale_or_capacity:
        per_unit_mass_kg: 0.0748
        bom_quantity: 1
        row_total_mass_kg: 0.0748
        envelope_mm: "95 x 10 x 95"
        scale_class: small
      geometry_form: thick_annular_plate_with_central_aperture_and_mounting_holes
      process_family: sheet_plate_cutting_drilling
    - item_id: ream250_recoater_blade_mount_strip_v0
      member_rows:
        - 173
      functional_purpose: "clamp, space, or back a recoater blade along its mounting span"
      material: stainless_steel
      scale_or_capacity:
        per_unit_mass_kg: 0.133
        bom_quantity: 1
        row_total_mass_kg: 0.133
        envelope_mm: "265 x 3.5 x 20"
        scale_class: small
      geometry_form: long_thin_profiled_strip_with_angled_end_features
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: false
  rationale: "Row 364 has unresolved machined metal evidence with an aluminum planning-density mass and possible optical/vacuum compatibility requirements. Row 173 has BOM/STEP-supported stainless steel evidence. A future lunarized design might choose one metal family for both, but the current evidence does not support treating them as one material item because the optical window retainer and blade-contact strip have different corrosion, cleanliness, and contact-surface risks."
process_review:
  can_unify: true
  rationale: "Both row conversions select sheet_plate_cutting_drilling with supporting cutting, local machining, deburring, cleaning, surface finishing, and dimensional inspection. They can share broad process anchors in Phase 3, but process-family reuse does not imply one closure item because the functional interfaces and geometry are unrelated."
geometry_review:
  can_unify: false
  rationale: "The CAD previews show different geometry classes: row 364 is a thick annular/square cover plate with central aperture and four-hole pattern; row 173 is a long, very thin strip with angled ends. These are not scale variants of one part family and would map to different BOM interfaces."
precision_review:
  blocks_merge: true
  rationale: "Row 364 carries aperture clearance, hole pattern, flatness, sealing quality, and optical cleanliness guardrails for a window/seal stack. Row 173 carries blade-contact flatness, straightness, and edge-condition guardrails for recoater blade hardware. Merging would hide the distinct precision stacks and could mislead later staging about sealing versus blade-contact requirements."
assumptions:
  - "Both candidate rows were included only because their broad functional key is interface_clamping and their masses fall within the generated 2x window."
  - "Existing KB entries checked by keyword include broad cover, strip, recoater, blade, spacer, optical, and retainer terms. Items such as protective_cover_set, powder_recoater_module_v0, steel_strip_thin, and shear_blade_or_saw_band are too broad, too material-like, or represent different assemblies/functions, so they are not close enough replacements for these staged one-piece items."
  - "Both proposed item IDs are staging suggestions only; this task does not write KB YAML and final import/local manufacture remains deferred."
  - "A later staging pass may still map both items to shared sheet/plate cutting and finishing processes while keeping item identities split."
unresolved:
  - "Row 364 exact alloy, surface finish, window/seal interface requirement, flatness tolerance, vacuum compatibility, and optical cleanliness class remain unresolved."
  - "Row 173 exact stainless grade, hardness, passivation requirement, blade-contact tolerance, and assembly-side clamp/spacer/backing role remain unresolved."
  - "Phase 3 should re-check existing KB items before promotion, especially if a generic optical-window retainer or recoater blade mount family has been staged by then."
---

# Merge Review

Split the interface_clamping candidate pool into two staged closure items. The rows can share a broad sheet/plate fabrication strategy, but their optical-window sealing interface and recoater blade-contact interface should remain separate for Phase 3.
