# Agent Instructions: reAM250 BOM to KB Conversion

You are processing reAM250 BOM-to-KB conversion tasks. These tasks use the
completed research files under `research/ream250_bom/` as their source evidence.

## Lease Only Matching Tasks

Use the exact lease command provided by the user or runner. If none is provided,
choose the phase-specific command:

Row conversion:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_row_
```

Merge review:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_merge_
```

Phase 3 staging:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_stage_
```

If the queue is empty, stop.

## Allowed Edits

For `row_conversion` tasks, only edit the leased source row file under:

```text
research/ream250_bom/ream250_bom_row_*.md
```

You may only add or replace the bottom section headed exactly:

```markdown
## KB Conversion
```

Do not edit YAML frontmatter, original research text, image files, KB YAML,
source code, docs, queue tasks, or generated index files.

For `merge_review` tasks, only create or update the task output file under:

```text
research/ream250_bom/kb_conversion/merge_reviews/
```

For Phase 3 staging work, only create or update staging files under:

```text
research/ream250_bom/kb_conversion/phase3_staging/
```

The sibling `phase3_staging_pilot/` directory contains maintainer-written
examples and findings. Do not overwrite pilot examples while processing queue
tasks.

Do not run:

```bash
python -m src.cli index
```

## Row Conversion Objective

Read the full original row research file and write a `## KB Conversion` section
containing fenced YAML. The section records conversion decisions, not a summary
of the source research.

You must use the original row evidence before making conversion decisions:

- `function.summary`, assumptions, and uncertainty notes;
- `mass.value_kg` and mass basis;
- source BOM quantity and row total mass when available;
- `material.primary_material` and material evidence;
- `how_to_make.summary` and manufacturing steps;
- `kb_implications`;
- CAD preview/image evidence if the original research references it and the
  conversion decision depends on geometry.

You must decide:

- whether the row is a simple part, complex module, decomposition candidate,
  import candidate, or needs human review;
- the process abstraction for closure analysis. Start from the original
  `how_to_make`, then choose one primary shared lunar process bucket. The
  primary bucket is a coarse closure handle, not a full manufacturing recipe.
  Add supporting process tags for secondary work such as cutting, drilling,
  finishing, leak testing, calibration, and inspection. Reference existing
  `kb/processes/*.yaml` process IDs as candidates when they are relevant;
- `process_abstraction.primary_process_bucket` must be exactly one of:
  `general_metal_additive_with_finish_machining`,
  `general_subtractive_machining`, `sheet_plate_cutting_drilling`,
  `structural_profile_stock_fabrication_cutting`,
  `polymer_elastomer_forming_dispensing`,
  `manual_assembly_with_general_tools`,
  `fastener_forming_thread_rolling`,
  `plumbing_connector_fabrication_testing`,
  `precision_component_import_decompose_later`, `not_applicable`,
  `needs_human`;
- use `keep_original_family` only when the original route already belongs to
  the selected canonical bucket. If the row-specific source route is being
  generalized into a shared bucket, use `substitute_process_family` or
  `add_post_processing`;
- for plate-like covers, panels, guards, and shallow sheet/plate parts, prefer
  `sheet_plate_cutting_drilling` as the primary bucket. Put pockets, recesses,
  lips, ribs, counterbores, and local milled features in supporting processes
  such as `precision_machining`; do not choose `general_subtractive_machining`
  merely because the source route mentions CNC machining on plate stock;
- `process_abstraction.supporting_processes` should use only the vocabulary in
  `conversion_section.schema.yaml`. Use it to record the expected process chain
  without expanding Phase 1 into recipe authoring;
- `process_abstraction.candidate_existing_processes` must point to real
  existing KB process IDs. Mark each fit as `direct`, `partial`, `supporting`,
  or `poor_fit`. A weak fit is acceptable when the reason explains what is
  missing;
- the normalized identity for later merge review:
  function, material, scale/capacity, and geometry form. Keep these axes
  separate: do not put material, dimensions, or geometry into
  `identity_for_merge.functional_purpose`;
- whether the row enters the merge candidate pool. The
  `merge_pool.functional_purpose_key` must describe function only. Do not put
  material, process family, geometry form, exact dimensions, or mass class in
  this key;
- make `merge_pool.functional_purpose_key` broad enough for Phase 2 candidate
  generation. Prefer `plumbing_connection` over
  `rigid_flanged_plumbing_connection_section`, `structural_frame_member` over
  `structural_frame_rail_member`, `linear_guidance` over
  `linear_guidance_carriage`, and `enclosure_barrier` over
  `machine_enclosure_barrier_panel`. Keep narrower geometry and interface
  details in `identity_for_merge.geometry_form` and `merge_pool.precision_guardrails`;
- use `powder_containment` for recoater, powder-bed, and powder-handling side
  plates whose role is containing or guiding powder-contact hardware. Do not
  group those rows under `enclosure_barrier` solely because they are plate-like;
- do not use vacuum as a functional key axis. Keep vacuum evidence in source
  notes and precision guardrails when supported, but key by ordinary function
  such as plumbing connection, interface clamping, joint clamping, or environment
  barrier;
- inputs needed for the later import/local manufacture decision. Do not decide
  final import vs local manufacture during row conversion;
- keep `downstream_decision_inputs.local_manufacturing_paths_considered`
  focused on the selected closure path. Do not list unrelated process buckets
  only because the material is unresolved; record speculative material-driven
  alternatives in assumptions, unresolved, or import risk factors instead;
- assumptions and unresolved issues.

Do not assign a final closure item ID unless the row clearly cannot merge with
anything else. Most rows should leave `kb_staging.proposed_item_id: null` until
merge review.

## Row Conversion Output Format

Append or replace this section at the bottom of the source row file:

````markdown
## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0002_1A1.md
source_research_sha256: "<baseline hash from task context>"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read original function, mass basis, material evidence, manufacturing route, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "..."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machining
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers basic stock removal; row-specific tolerances remain guardrails."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant when bore, sliding, concentricity, and finish control matter."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks before staging selects the final recipe."
  abstraction_decision: substitute_process_family
  rationale: "..."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: structural support for machine frame and chamber interface
  material: aluminum_alloy
  scale_or_capacity:
    mass_kg: 41.21
    bom_quantity: 1
    row_total_mass_kg: 41.21
    scale_class: large
  geometry_form: machined_plate_frame
merge_pool:
  eligible: true
  functional_purpose_key: structural_machine_frame_member
  precision_guardrails:
    - flatness
    - alignment_accuracy
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors: []
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before final item ID."
assumptions:
  - "..."
unresolved:
  - "..."
```
````

## Merge Review Objective

Read all candidate row files listed in task context. Use the original research
and their `## KB Conversion` sections to decide whether the candidate rows
converge to one closure item.

A candidate group was generated only from same functional purpose key and a 2x
mass window. The `functional_purpose_key` is only a rough index for task
generation. Do not decide the merge from that key alone.

For every candidate row, read:

- the original row research frontmatter;
- the original `function`, `mass`, `material`, `how_to_make`, and
  `kb_implications` sections;
- the bottom `## KB Conversion` section;
- CAD preview/image evidence when geometry or precision is unclear.

Then review:

- material unification;
- process unification;
- geometry form unification;
- precision blockers.

Write one merge review Markdown file with YAML frontmatter matching
`merge_review.schema.yaml`.

## Phase 3 Staging Objective

Read one completed merge review and the original row files referenced by that
merge review. Write one YAML staging package matching
`phase3_staging.schema.yaml`.

Phase 3 does not write to `kb/`. It decides whether each Phase 2 proposed
closure item should:

- reuse an existing KB item;
- create a new staged KB-like item;
- defer because evidence is insufficient.

Phase 3 must also decide import/local manufacture for every proposed item. Use
existing KB patterns:

- items that cannot be manufactured locally are imports and should have
  `is_import: true` when promoted;
- advanced optics, electronics, precision reducers, high-grade sensors, and
  specialty materials are often imports;
- structural, machined, sheet, profile, and ordinary fastener items should stay
  local candidates when plausible process anchors exist;
- import/local is a boundary condition for closure analysis, not a feasibility
  guarantee.

Before proposing a new item, search existing KB items and imports. Prefer
`reuse_existing` when a close-enough item exists under project equivalence
rules. Preserve row-specific quantity, mass, length, handedness, nominal
interface, thread size, sealing, coating, and precision guardrails in
`proposed_bom_mappings`.

For every proposed item include:

- `action`;
- `proposed_item_id`;
- `reason_for_action`;
- `import_local_decision`;
- `promotion_blockers`.

For `reuse_existing`, include `existing_kb_path` when known. For `create_new`,
include a `kb_like_item` object with enough fields to evaluate promotion.

## Completion

Validate and complete with:

```bash
.venv/bin/python -m src.cli queue complete \
  --id <leased-id> \
  --agent <agent-name> \
  --require-output \
  --validate-output
```
