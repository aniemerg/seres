# Phase 3 Pilot Findings

Date: 2026-06-29

## What Phase 3 Does

Phase 3 converts a Phase 2 merge review into a KB staging package. It does not
promote data into `kb/` during this pilot.

Its required job is to decide, for each Phase 2 proposed closure item:

- whether to reuse an existing KB item, create a new staged item, or defer;
- whether the item is an import, locally manufacturable now, or a local
  manufacture candidate with blockers;
- which source BOM rows map to which closure item;
- which row-specific quantities, masses, lengths, variants, and guardrails must
  survive the merge;
- which existing KB processes are candidate recipe anchors;
- which blockers prevent immediate promotion to final KB YAML.

## Pilot Outputs

Three representative Phase 2 results were staged:

- `ream250_kb_merge_0025_plumbing_connection.stage.yaml`
  - partial merge;
  - creates staged ISO-K/KF vacuum/fluid connection items instead of collapsing
    all rows into a broad fitting kit;
  - marks the staged items as local-manufacture candidates with sealing,
    cleanliness, inspection, and precision blockers;
  - preserves nominal interface, adapter direction, flange size, quantity, and
    row mass mappings.
- `ream250_kb_merge_0035_structural_frame_member.stage.yaml`
  - partial merge;
  - creates one 60 x 60 aluminum profile staging item;
  - creates one machined Z-axis side-plate staging item;
  - marks both staged items as local-manufacture candidates rather than imports;
  - preserves row-level length, handedness, quantity, and mass mappings.
- `ream250_kb_merge_0040_threaded_fastening.stage.yaml`
  - clean merge;
  - reuses existing `fastener_kit_small`;
  - marks the item as local through the existing fastener-kit fabrication path;
  - preserves M4/DIN 912 length variants and quantity as mapping guardrails.

All staged YAML files pass the Phase 3 schema validator.

## Findings

1. Phase 3 needs an explicit `action` field.

`merge`, `partial_merge`, and `split` are Phase 2 decisions. Phase 3 needs a
separate action per staged item:

- `reuse_existing`
- `create_new`
- `defer`

Without this field, workers may create new reAM250-specific items when a KB item
already exists, especially for fasteners, generic panels, brackets, stock, and
plumbing kits.

2. Row-to-item mapping is mandatory.

Phase 2 proposed closure items are not enough. Phase 3 must preserve:

- source row number;
- source item code;
- closure item ID;
- quantity;
- row total mass;
- length or variant fields when relevant;
- notes explaining what was collapsed.

The structural profile case shows why. One item identity can represent 740 mm,
960 mm, and 1020 mm cut lengths, but the BOM still needs those lengths later.

3. Stock items need a modeling decision before promotion.

The 60 x 60 aluminum profile is naturally a stock item measured by length, but
current part schema commonly expects a discrete part with `mass_kg`.

Phase 3 should force one of these promotion choices:

- model as stock with `unit: m` and `mass_kg_per_m`;
- model as discrete nominal cut-length variants;
- model as a kit or profile family with BOM mapping notes.

This cannot be left implicit.

4. Existing KB reuse reveals schema drift.

`fastener_kit_small.yaml` exists and is the right reuse target, but it uses
`mass: 1.3` while the current schema reference expects `mass_kg`.

Phase 3 should record this as a promotion blocker or follow-up task, rather than
silently accepting a schema mismatch.

5. Process buckets are not recipes.

Phase 1/2 process buckets are useful closure handles, but Phase 3 promotion
still needs recipe binding decisions:

- whether `metal_extrusion_process_v0` can bind to structural profile output;
- whether a new structural-profile recipe is needed;
- whether fastener kit consumption should be by unit, mass, or nested kit
  composition;
- whether precision inspection is part of the recipe or only a guardrail.

6. Import/local manufacture belongs in Phase 3.

The first draft of this pilot underweighted import/local decision making. That
was wrong for the phase boundary. Row conversion explicitly defers final
import/local decisions, and merge review only records manufacturing
implications. Phase 3 is the first phase that should make the staged decision.

Existing KB patterns:

- true imports are marked directly on items with `is_import: true`;
- imports are preferred when the item is outside current capability, not a top
  contributor, or too costly to model relative to impact;
- advanced optics, electronics, precision reducers, high-grade sensors, and
  specialty materials are commonly imported;
- plausible structural and mechanical parts should remain local candidates when
  process anchors exist, even if recipes are incomplete.

Pilot decisions:

- `aluminum_structural_profile_60x60_v0`: local-manufacture candidate with a
  structural-profile recipe gap;
- `z_axis_side_plate_machined_pair_v0`: local-manufacture candidate with
  precision and material blockers;
- `fastener_kit_small`: reuse existing non-import local item and existing
  aggregate fabrication process.

7. reAM250-specific IDs should be challenged at Phase 3.

Phase 2 proposed `ream250_aluminum_structural_profile_60x60_v0`. Phase 3
changed the pilot proposal to `aluminum_structural_profile_60x60_v0` because it
looks reusable beyond reAM250.

Phase 3 should explicitly ask whether each staged item deserves a project prefix
or should become a general KB item.

8. Standard interfaces may be closure identity, not just BOM notes.

The plumbing pilot showed that broad existing items such as fitting kits are too
coarse for ISO-K/KF hardware when sealing quality, nominal bore, flange family,
adapter direction, and leak-test expectations affect closure. Phase 3 should
preserve these fields in mappings and proposed item notes. A future promotion
may need a structured `standard_interface` field instead of burying this data in
free-text notes.

9. Vacuum-related rows are not automatically import rows.

The plumbing pilot deliberately did not treat vacuum hardware as import-only.
If machining, joining, sealing, and leak-test process anchors exist, these rows
can be local-manufacture candidates with precision guardrails. Import remains a
valid decision for parts that require unavailable materials, cleanliness,
surface finish, or qualification capability, but that decision belongs in
Phase 3 evidence, not in a blanket rule.

## Concrete Recommendations

1. Add a Phase 3 staging schema.

Minimum required top-level fields:

- `stage_id`
- `stage_status`
- `source_merge_review`
- `source_phase2_decision`
- `evidence_inputs`
- `proposed_items`
- `import_local_decision` inside each proposed item
- `proposed_bom_mappings`
- `stage_findings`
- `unresolved`

2. Add a Phase 3 validator before scaling.

The pilot immediately exposed YAML quoting errors. A validator should check:

- YAML parses;
- each `proposed_item.action` is allowed;
- `reuse_existing` points to an existing KB file;
- `create_new` includes KB-like item fields;
- every proposed item has an import/local decision with `decision`,
  `is_import`, `rationale`, risk factors, and blockers when applicable;
- every candidate row from the merge review appears in `proposed_bom_mappings`;
- every mapping references one proposed item;
- each proposed item has promotion blockers or an explicit statement that none
  are known.

3. Add Phase 3 worker SOP only after the schema is fixed.

Worker instructions should say:

- do not write `kb/`;
- read the Phase 2 merge review and the original row files;
- search existing KB before proposing new items;
- prefer `reuse_existing` when a close enough KB item exists;
- decide import/local manufacture during staging, using existing KB import
  patterns and recording blockers;
- preserve row quantity, mass, length, handedness, and variant guardrails in the
  mapping table;
- separate item identity from BOM mapping details.

4. Continue pilot with an electronics, optics, or actuator hard case.

The next useful pilot case should test a likely import boundary, such as
electronics, optics, precision reducers, sensors, or proprietary actuator
modules. Plumbing tested local-manufacture ambiguity; the next case should test
when import is the more honest closure boundary.

## Current Assessment

Phase 3 is feasible, but it should not be treated as a direct conversion from
Phase 2 proposed items to KB YAML.

The correct intermediate artifact is a staging package with actions, mappings,
and promotion blockers. That package gives a human reviewer enough structure to
promote later without losing row-level evidence.
