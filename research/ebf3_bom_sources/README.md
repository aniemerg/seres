# EBF3 BOM Source Staging

Use this directory for source material, organized extraction, and modeling
decisions for the EBF3 3D printer BOM refinement.

## Folder Roles

- `sources/`: source location registries and colocated raw source files only.
  - `sources/level_0_machine/<machine>/`: whole-machine source registry plus optional
    `raw/` files.
  - `sources/level_1_subsystems/<subsystem>/`: subsystem source registry plus optional
    `raw/` files.
  - `sources/level_2_parts/<part_family>/`: part-family source registry plus optional
    `raw/` files.
  - `sources/level_3_parts/<child_part_family>/`: child-part or child-assembly
    source registry plus optional `raw/` files.
- `organized/`: extracted claims, comparison tables, candidate components,
  adopted/deferred/rejected decisions, unresolved-candidate registers, and
  reviewer reasoning.
- `derived/`: final boundary documents, KB mapping summaries, and other
  Codex-generated modeling artifacts.

Do not put extracted claims or modeling decisions in `sources/`. Keep source
registries limited to source IDs, titles, URLs, local file paths, and basic
location metadata. If multiple registries use one raw source, keep one physical
copy in its primary level folder and link to that path from the other
registries.

## EBF3 Modeling Goal

This directory supports high-fidelity EBF3 BOM refinement, not a local-closure
push. The goal is to make the machine structure clearer while preserving known
unknowns.

Target state for the whole EBF3 machine:

- Level-0 machine BOM exists for `ebf3_3d_printer`.
- Seven Level-1 subsystem BOMs exist: controls, power supplies, high-voltage
  tank, fixed electron beam gun, wire feeder, four-axis positioning system, and
  manufacture cabin.
- Each subsystem has a Level-2 audit or decomposition plan before deeper child
  BOMs are created.
- Cross-subsystem interfaces have one owner and visible unresolved rows when the
  physical boundary is not source-fixed.
- Simviewer shows a concise structure, while research files preserve the deeper
  evidence trail.
- Closure gaps are allowed. Validation errors are not.

Current whole-machine Level-2 status is summarized in
`organized/ebf3_machine_level_2_status.md`.
Current cross-subsystem interface ownership is summarized in
`organized/ebf3_interface_architecture.md`.
Current whole-machine leaf material/process readiness is tracked in
`derived/ebf3_leaf_material_process_readiness.csv`.
Approved existing-item substitutions and their retained modeling issues are
tracked in `derived/ebf3_existing_item_replacement_register.md`.
Source-first review for leaves marked `split_before_route` is tracked in
`organized/split_before_route_leaf_decomposition_plan.md`.

## Trust Tag Policy

For this EBF3 fitting pass, the existing global KB is treated as dirty evidence
rather than trusted design ground truth. Item trust is explicit:

- `trust_tags: [trusted_ebf3_unreplaced]` means the item is a newly introduced
  EBF3 item and has not been replaced by an existing KB item.
- `trust_tags: [untrusted_global_kb]` means the item is not trusted as
  high-fidelity EBF3 evidence. This includes all pre-existing non-EBF3 KB items
  and EBF3 leaf items that were replaced by an approved existing-item reuse.

Do not infer trust from an empty tag list while doing EBF3 fitting. EBF3 fitting
outputs should treat empty or absent trust tags as unknown/untrusted unless a
local review explicitly says otherwise. This policy is not a request to migrate
every existing KB item immediately. Approved EBF3 replacements remain useful for
BOM simplification, but the replacement item itself is still treated as
`untrusted_global_kb` for high-fidelity EBF3 evidence.

## Standard Work Packet

Use this short sequence for each EBF3 modeling pass:

1. Pick one blocking boundary, subsystem, or parent assembly.
2. Read existing source registry, organized plans, mappings, and unresolved
   registers for that scope.
3. Add or update the source registry only with source locations.
4. Write or update the organized review with evidence, use, decisions, and
   unresolved blockers.
5. Decide ownership before creating or moving KB items.
6. Create KB items/BOMs only for `adopt` decisions.
7. Add concise item/BOM notes pointing back to the organized review.
8. Update affected unresolved registers.
9. Validate affected items and run full index.
10. Export Simviewer data when the user needs to inspect the result visually.

## Recommended Work Order

Preferred order for completing the EBF3 machine scaffold:

1. Keep `organized/ebf3_machine_level_2_status.md` current as the concise
   whole-machine status index.
2. Use `organized/ebf3_interface_architecture.md` as the current
   cross-subsystem interface entry point across cabin, gun, wire feeder,
   positioning, controls, power supplies, and high-voltage tank.
3. Return to electron-gun Level-3 items only where a selected source or design
   decision unlocks them.
4. Fit leaf items into the existing KB using the leaf fitting gate below and
   record whole-machine review categories in the generated readiness matrix
   under `derived/`.
5. Material/process readiness reviews for selected leaves.
6. Local recipes only for leaves that pass readiness review.

## Leaf Item KB Fitting Gate

Use this gate after decomposition and before adding manufacturing recipes. The
goal is to fit EBF3 leaves into the existing KB without losing the fidelity that
the EBF3 work added.

| Case | Decision | Action |
| --- | --- | --- |
| Existing item, sufficient resolution | `reuse_existing` | Link the EBF3 leaf to the existing item. Record why the existing resolution is enough. |
| Existing item, insufficient resolution | `reuse_with_accuracy_risk` | Existing KB item may replace the EBF3 leaf as a coarse structural fit, but record `not enough accuracy` and do not use the replacement as local-closure evidence until the hidden material/process assumptions are upgraded. |
| No existing item, no further decomposition needed | `create_leaf` | Create a high-fidelity leaf. Select material from source evidence, lunar material guidance, and existing KB material classes. Recipe is optional. |
| No existing item, further decomposition needed | `needs_decomposition` | Keep unresolved and handle after simpler leaf fitting is complete. |

Core rule: a lower-resolution existing item can simplify the BOM graph only if
the accuracy risk remains visible. If the replacement hides lunar resource
assumptions or manufacturing process assumptions, mark it `not enough accuracy`
and treat it as an import/deferred closure path until the missing detail is
upgraded.

Direct replacement must also pass a performance and scale check: same functional
role, compatible material/process assumptions, compatible unit kind or explicit
quantity normalization, and enough performance detail for the EBF3 role. Check
tolerance, stiffness, voltage/current rating, thermal load, vacuum/leak
requirements, surface finish, lubrication, and environmental compatibility where
they matter. Record precision-sensitive item requirements under
`performance_requirements` using the fields that apply:
`tolerance`, `surface_finish`, `sealing_quality`, and
`alignment_accuracy`. Mass must be reviewed as a range, not a single equality
test: estimate low/nominal/high mass when possible and compare any candidate
replacement against that range. If scale, performance, or manufacturing
assumptions are unknown, mark it `not enough accuracy`.

If no existing item is suitable and the leaf does not need further
decomposition, select the material first. Do not attach a generic existing
process only to make closure look better; EBF-based or EBF-assisted
manufacturing routes can replace many provisional existing processes later.

Use the generated material/process readiness matrix as the working review
surface before editing YAML:

```bash
python scripts/analysis/ebf3_leaf_readiness_matrix.py
```

Outputs:

- `derived/ebf3_leaf_material_process_readiness.csv`

The matrix records current mass, low/high mass brackets, readable performance
checks, explicit `performance_requirements` review fields, one default material
candidate with optional alternates, existing-KB candidates, and a suggested
review decision. Treat the decision as a review prompt, not an automatic
replacement instruction.

For EBF3, this means common low-risk hardware may reuse existing items when the
material and process path remain equivalent. High-voltage feedthroughs,
vacuum-compatible motors, precision electron-gun electrodes, cathodes,
electronics, sensors, and ceramic-to-metal interfaces should remain separate
unless the existing item already exposes the relevant material, precision,
vacuum, electrical, and manufacturing constraints.

## When To Resolve Unresolved Rows

Do not try to clear every unresolved row before moving to the next subsystem.
Resolve an unresolved row only when it:

- blocks the next BOM level,
- would cause duplicate ownership across subsystems,
- would make Simviewer misleading,
- or is unlocked by a new source or explicit design decision.

Otherwise, keep it in the relevant unresolved register with a blocker and next
unblock condition.

## Decomposition Workflow

All new EBF3 leaf assembly decomposition must follow this order:

1. Select one parent item or a tightly related pair of parent items.
2. Confirm or create the relevant source registry under `sources/`.
3. Create an organized decomposition planning file under `organized/` before
   editing KB YAML.
4. Extract candidate components and source claims into the planning file. Keep
   user-derived candidates separate from claims extracted from external or
   primary sources.
5. Build a decision matrix using the statuses, authority rules, and adoption
   gate below.
6. For `defer` or `needs_source_confirmation` candidates that materially affect
   fidelity, perform targeted follow-up source search before editing KB YAML.
   Add any useful sources to the same relevant source registry and record the
   extracted claims in the organized planning file. Do not label these as
   separate "secondary search" sources; they are simply additional sources.
7. Only create KB child items and child BOMs for `adopt` decisions.
8. Add short BOM notes linking back to the source registry and organized
   planning file. The KB note should point to the evidence trail; it should not
   restate unresolved claims as settled facts.
9. Do not add manufacturing recipes or local closure unless the item has already
   passed a separate material/process readiness review.
10. Run targeted validation for the parent item and then full index.

The organized planning file is the generation basis for the BOM, not a
post-hoc justification for an already-created BOM.

## Planning File Minimum Structure

Each organized decomposition planning file should include:

- Parent item(s) and target KB BOM(s).
- Source registry path.
- Source hierarchy and authority assessment.
- Source evidence and use grouped by source ID. Evidence should be short
  verbatim snippets when possible; interpretation belongs in `Use`.
- Candidate decision matrix.
- Adopted child BOM structure.
- Explicit defer/reject/split-boundary rationale for candidates that could
  otherwise be mistaken as omissions.
- Manufacturing readiness statement. The default is not-local-ready unless a
  separate material/process review says otherwise.

## Unresolved-Candidate Registers

When several decomposition plans have accumulated `defer` and `split_boundary`
rows, create an organized register that consolidates the unresolved candidates.
The register should point back to the source planning files, group candidates by
the work that can unblock them, and state the next review that owns each row.
Registers are tracking artifacts only; they do not justify creating KB child
items or recipes.

## Decision Status Glossary

- `adopt`: create the child item and include it in the child BOM.
- `defer`: keep the candidate in the planning file, but do not create a KB item
  yet because EBF3-specific support or required detail is missing.
- `reject`: do not model this candidate for this parent BOM.
- `split_boundary`: the candidate may be real and relevant, but it belongs to a
  different parent item or subsystem boundary. Do not duplicate it in this BOM;
  point to the owning item/subsystem instead.
- `needs_source_confirmation`: source hints at the candidate, but the evidence
  is too unclear to adopt, reject, or assign across a boundary.

## Source Authority Rules

- Treat source authority as an explicit field in every planning file.
- Typical authority classes:
  - `primary`: original source material directly about the specific machine,
    subsystem, or component being modeled. A source can be primary for one
    scope and external for another.
  - `external`: independent technical reference, vendor page, paper, patent, or
    educational source not specific to this EBF3 BOM.
  - `user_derived`: user-prepared table, inferred composition, or manually
    organized BOM table.
  - `engineering_inference`: a modeling inference required to make an assembly
    coherent, such as "a wound coil needs insulation"; this must be labeled as
    inference, not source evidence.
- User-derived organized tables, including `LOCAL-EBF3-FG-TABLE`, can introduce
  candidate components and boundary hypotheses.
- User-derived tables cannot by themselves justify `adopt`.
- A candidate should become `adopt` only when supported by a primary source,
  external source, or a clearly documented boundary/assembly rule.
- Engineering inference may justify an unresolved note inside an assembly, but
  it should not create a separate KB child item unless the planning file also
  shows why the inferred feature must be independently represented at this BOM
  level.
- If `adopt` depends on an engineering inference rather than direct source
  wording, the decision matrix must say so, explain why a separate child item is
  needed, and keep material/geometry/process unresolved.
- If multiple adopted items are materially the same kind of component, use
  consistent names unless a source-supported distinction is being preserved.
- If a candidate materially affects fidelity and is currently `defer` or
  `needs_source_confirmation`, perform targeted follow-up source search before
  changing KB YAML.

## Adoption Gate

Before a candidate becomes a KB child item, the planning file must answer all of
these at the row level:

- What introduced the candidate: primary source, external source, user-derived
  table, or engineering inference?
- What supports keeping it in this parent BOM rather than another subsystem?
- Is it a physical part, an assembly placeholder, a function, or an interface?
- Does adoption preserve uncertainty by leaving material, geometry,
  manufacturing process, and local readiness unresolved where needed?
- Would adopting it duplicate another modeled item or collapse a boundary that
  should remain explicit?

If any answer is unclear, use `defer`, `split_boundary`, or
`needs_source_confirmation` instead of `adopt`.

## Mapping And Derived Document Rules

- `derived/*_mapping.md` files describe first-pass scaffold mappings from the
  user-derived subsystem tables into KB item IDs.
- Mapping files are not decomposition planning files and are not sufficient
  evidence for creating Level-2 child BOMs.
- Mapping files may preserve the original table wording, including uncertain
  composition text, but that wording remains candidate-only until reviewed in an
  organized planning file.
- Boundary documents in `derived/` can define ownership rules. They do not prove
  material composition or manufacturing readiness.

## Workflow Maintenance

- When a review reveals a general rule, update this README first or in the same
  change as the local plan.
- Avoid adding one-off explanations to a single plan when the rule should govern
  future decomposition work.
- Before editing KB YAML for a decomposition, check the relevant source registry,
  planning file, boundary rules, and existing naming conventions together.
- Prefer changing the shared workflow over accumulating local exceptions.
- Every local workflow improvement should be checked against the whole EBF3
  workflow: folder role, source authority, boundary ownership, naming,
  manufacturing readiness, and validation/closure behavior.
- Do not add a new status, folder convention, or evidence rule for one component
  unless it can be reused by future subsystem and part-family decompositions.
- If an existing plan conflicts with the shared workflow, update the shared
  workflow first, then revise the plan to match it.
- In human-facing review text, avoid internal prefixes such as "KB" or source
  filename versions such as "V2" unless they are part of an actual file path,
  source ID, or item ID. Prefer "current BOM", "source table", and
  "recommended item".

## Level Naming

- Use Level-0/Level-1/Level-2/Level-3 labels in research folders, planning
  files, and review notes.
- Do not put level numbers in KB item IDs or item names. KB structure should be
  expressed by BOM parent/child relationships, not by permanent level labels in
  identifiers.
- If level context is useful, add it to research notes or concise item notes,
  for example "created during the EBF3 fixed-gun Level-2 decomposition review."

## Review Standard

For each proposed child item, reviewers should be able to answer:

- Which source introduced this candidate?
- Is the source EBF3-specific, subsystem-specific, or generic?
- Why was the candidate adopted, deferred, rejected, or split across a boundary?
- Does the child item increase fidelity without hiding unresolved material,
  precision, vacuum, high-voltage, electronics, or manufacturability questions?

Closure gaps are acceptable during this phase. Validation errors are not.
