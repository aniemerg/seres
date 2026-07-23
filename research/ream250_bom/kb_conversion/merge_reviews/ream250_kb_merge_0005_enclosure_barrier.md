---
group_id: ream250_kb_merge_0005_enclosure_barrier
candidate_rows:
  - source_row_number: 310
    item: "181"
    path: research/ream250_bom/ream250_bom_row_0310_181.md
    conversion_section_present: true
  - source_row_number: 306
    item: "172"
    path: research/ream250_bom/ream250_bom_row_0306_172.md
    conversion_section_present: true
evidence_reviewed:
  original_research_files_read:
    - research/ream250_bom/ream250_bom_row_0310_181.md
    - research/ream250_bom/ream250_bom_row_0306_172.md
  conversion_sections_read:
    - research/ream250_bom/ream250_bom_row_0310_181.md#kb-conversion
    - research/ream250_bom/ream250_bom_row_0306_172.md#kb-conversion
  notes: "Read both rows' original function, mass, material, how_to_make, kb_implications, and KB Conversion sections. Also inspected the referenced CAD preview PNGs: row 310 is a 580 x 30 x 460 mm right side plate with one large central port, diagonal pocket/rib geometry, and perimeter fastening features; row 306 is a 418 x 21.7 x 560.5 mm changeable top plate with multiple circular openings, similar rib/pocket geometry, and perimeter interface features."
rough_match_basis:
  functional_purpose_key: enclosure_barrier
  mass_window_kg:
    - 19.0
    - 31.1
merge_decision:
  decision: merge
  rationale: "The two rows should converge to one large chamber barrier plate closure item. Both are monolithic removable enclosure/chamber plates, both are large rectangular plate-stock parts with circular pass-throughs and local rib/pocket machining, both use sheet_plate_cutting_drilling with finish machining and inspection, and both carry flatness, port location, and sealing or mating-interface guardrails. Top-versus-side placement, opening count, handedness, and exact hole patterns are BOM mapping guardrails rather than separate closure items under the project's reuse policy."
  proposed_closure_items:
    - item_id: ream250_chamber_barrier_plate_large_v0
      member_rows:
        - 310
        - 306
      functional_purpose: "large removable chamber or enclosure barrier plate with service and port openings"
      material: structural_metal_plate_alloy_unresolved
      scale_or_capacity:
        per_unit_mass_range_kg:
          - 19.0
          - 31.1
        bom_quantity: 1
        row_total_mass_range_kg:
          - 19.0
          - 31.1
        envelope_mm:
          - "580 x 30 x 460"
          - "418 x 21.7 x 560.5"
        scale_class: large
      geometry_form: large_rectangular_machined_chamber_barrier_plate_with_port_openings
      process_family: sheet_plate_cutting_drilling
material_review:
  can_unify: true
  rationale: "Material does not currently block a Phase 2 merge. Row 310 has positive aluminum-side-plate context from sibling STEP metadata and the public sealed-aluminum-plate description. Row 306 has only broad metal plate evidence; its steel/stainless mass basis is an engineering scenario, not confirmed source evidence. A shared unresolved structural-metal plate closure item preserves this uncertainty for staging. Existing KB items such as chamber_shell_sealed, enclosure_steel_large, panel_or_door_assembly, protective_cover_set, fixture_mounting_plate_set, and metal_sheet_or_plate were considered but are sealed shell assemblies, electronics enclosures, frame assemblies, protective cover sets, fixture plate sets, or raw stock rather than finished reAM250-sized chamber barrier plates with port and sealing-interface guardrails."
process_review:
  can_unify: true
  rationale: "Both row conversions select sheet_plate_cutting_drilling as the primary closure bucket, with stock preparation, cutting, drilling, precision machining, deburring, cleaning, surface finishing, and dimensional inspection as supporting work. The same existing process anchors apply: cutting_basic_v0 and sheet_metal_fabrication_v0 for blanking and cutouts, machining_basic_v0 for ports, pockets, counterbores, seal lands, and local mating features, and inspection_basic_v0 for flatness and hole or port locations."
geometry_review:
  can_unify: true
  rationale: "The CAD previews show the same broad geometry family: large rectangular plate-stock parts with shallow thickness relative to length and width, diagonal rib or pocket geometry, circular service openings, and perimeter interface features. Row 310 has one dominant central port and side-wall orientation; row 306 has multiple circular openings and top-plate orientation. Those differences are row-specific geometry guardrails that can be preserved in BOM mappings without requiring separate closure items."
precision_review:
  blocks_merge: false
  rationale: "Both rows share flatness, port location, hole pattern, sealing or mating-surface, and cleanliness/finish review needs. No row has a distinct laser-safety, optical-element, calibrated sensor, or high-precision motion-interface requirement that would force a split at merge review. Staging should split only if later evidence proves incompatible material, surface treatment, leak-rate, or port-interface requirements."
assumptions:
  - "BOM quantity is 1 for both rows, so row total mass equals each per-unit planning mass."
  - "The row 310 aluminum evidence is stronger than the row 306 material evidence, but row 306's steel/stainless assumption is not source-confirmed."
  - "Top, side, opening count, handedness, and local rib/pocket geometry are compatible variants for one closure item because function, scale, stock form, and process family match."
  - "No existing KB item is close enough to replace the staged closure item without losing the large removable chamber-plate role and port/sealing guardrails."
unresolved:
  - "Actual alloy, grade, temper, coating, and surface treatment for each row."
  - "Whether row 306 is aluminum, steel, stainless steel, or another structural metal."
  - "Flatness, seal land, leak-rate, cleanliness, thread, counterbore, and port-interface tolerances for both rows."
  - "Whether mounted hardware around the row 310 central penetration or row 306 circular openings should map to separate BOM rows during Phase 3 staging."
---

# Merge Review

Merge rows 310 and 306 into one staged large chamber barrier plate family. Preserve row-specific position, opening pattern, material uncertainty, and sealing/interface requirements as Phase 3 guardrails.
