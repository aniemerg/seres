# reAM250 BOM to KB Conversion Acceptance Criteria

## AC-001: Preserve Evidence Layer

For row conversion tasks, workers must not modify any content before
`## KB Conversion`. The validator compares this region against a baseline hash
generated when row conversion tasks are created.

## AC-002: Conversion Is a Decision Layer

The `## KB Conversion` section must not merely restate the research row. It must
record modeling decisions needed for KB staging:

- source evidence reviewed from the original row;
- decomposition decision;
- process abstraction for closure analysis;
- normalized merge identity;
- merge eligibility;
- inputs needed for the later import/local decision;
- source BOM quantity and row total mass when available;
- assumptions and unresolved issues.

## AC-003: Use Current Project Goal

The conversion goal is lunarized closure analysis, not faithful commercial BOM
replication and not free redesign. Preserve useful details only when they affect
closure, simulation, process capability, material choice, or precision risk.

## AC-004: Decompose Before Merge

Complex modules, vendor assemblies, electronics/control modules, motor/gearbox
assemblies, laser/optics subassemblies, and powder handling modules should be
marked for decomposition before merge review when internal closure dependencies
matter.

## AC-005: Process Abstraction

Process abstraction must start from the original `how_to_make` evidence and
then place the item into the simplest compatible shared lunar process bucket.
The primary bucket is a closure-analysis handle, not a complete manufacturing
recipe. Metal additive manufacturing is a preferred candidate for compatible
custom metal parts because it can reduce process diversity, but it is not a
blanket replacement for every row.

Use one of these canonical `process_abstraction.primary_process_bucket` values:

- `general_metal_additive_with_finish_machining`
- `general_subtractive_machining`
- `sheet_plate_cutting_drilling`
- `structural_profile_stock_fabrication_cutting`
- `polymer_elastomer_forming_dispensing`
- `manual_assembly_with_general_tools`
- `fastener_forming_thread_rolling`
- `plumbing_connector_fabrication_testing`
- `precision_component_import_decompose_later`
- `not_applicable`
- `needs_human`

The worker must explain why the primary bucket was chosen, list supporting
process tags from `conversion_section.schema.yaml`, and cite relevant existing
KB process IDs in `process_abstraction.candidate_existing_processes`. Candidate
processes are evidence anchors for later staging; they do not create recipes
and they do not force a final provider machine.

The abstraction must be checked against tolerance, surface finish, sealing
quality, and alignment accuracy needed by the item function. If the primary
bucket needs secondary work, record it in `supporting_processes` and in the
process candidate reasons. `keep_original_family` is allowed only when the
original route already falls inside the chosen canonical bucket.

Plate-like covers, panels, guards, and shallow sheet/plate parts should usually
use `sheet_plate_cutting_drilling` as the primary bucket. Local pockets, recesses,
lips, ribs, counterbores, and milled details are supporting work, not a reason by
themselves to make `general_subtractive_machining` the primary bucket.

## AC-006: Merge Eligibility

The merge candidate pool is a rough screening pool, not a merge decision. A row
may enter it only when it has a normalized functional purpose key, mass/scale
information, source BOM quantity when available, material identity, geometry
form, and no known reason it must stay unique before group-level review.

The `functional_purpose_key` is only an index for candidate generation. It must
not replace the full function summary, assumptions, uncertainty notes, material
evidence, mass basis, or manufacturing evidence from the original research row.
It should encode functional purpose only. Do not include material, process
family, geometry form, exact dimensions, or mass class in this key; those fields
are reviewed later in Phase 2.

The key should not be so narrow that it prevents obvious Phase 2 candidate
generation. Use broad function labels such as `plumbing_connection`,
`structural_frame_member`, `linear_guidance`, and `enclosure_barrier`. Put
component form details such as flanged section, rail, carriage, panel, cut
length, slot pattern, and interface shape in `identity_for_merge.geometry_form`
and `merge_pool.precision_guardrails`.

Use `powder_containment` for recoater, powder-bed, and powder-handling side
plates whose function is containment or guidance around powder-contact hardware.
Do not use `enclosure_barrier` for those rows solely because the item is a plate.

Do not use vacuum as a functional key axis. Preserve vacuum evidence in the
function summary, assumptions, guardrails, and notes when the source supports it,
but use the ordinary function for the key, such as `plumbing_connection`,
`interface_clamping`, `joint_clamping`, or `environment_barrier`.

Likewise, `identity_for_merge.functional_purpose` should describe the role the
item serves. Put material in `identity_for_merge.material`, mass/scale in
`identity_for_merge.scale_or_capacity`, and shape in
`identity_for_merge.geometry_form`.

`downstream_decision_inputs.local_manufacturing_paths_considered` should describe
the selected closure path, not every possible route implied by unresolved
material. Put speculative material-driven alternatives in assumptions,
unresolved, or import risk factors.

## AC-007: Merge Review

Merge review starts from same functional purpose and 2x mass/scale candidates.
The worker must then decide if material, process, and geometry can be adjusted
to the same closure item through lunarized design. Precision guardrails can
block a merge.

Merge review workers must read every candidate row's original research evidence
and its `## KB Conversion` section. They must not decide from
`functional_purpose_key` alone.

## AC-008: Conservative KB Creation

Before proposing a new closure item, consider existing KB equivalents. If the
candidate can reuse an existing item within project equivalence rules, record
that instead of inventing a new ID.

## AC-009: Staging Only

This task pack does not write to `kb/`. Staged KB-like YAML belongs under a
future staging directory and must be reviewed before promotion.

## AC-010: Defer Import/Local Decision

The final import/local manufacture decision happens after lunarized process
strategy and formal merge review, matching the BOM-to-KB plan. Row conversion
may record local manufacturing paths considered and import risk factors, but it
must not decide final import vs local manufacture. Merge review may note
manufacturing implications, but the final decision belongs to the later KB
staging phase.
