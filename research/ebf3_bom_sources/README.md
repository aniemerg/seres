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
- `organized/`: extracted claims, comparison tables, candidate components,
  adopted/deferred/rejected decisions, and reviewer reasoning.
- `derived/`: final boundary documents, KB mapping summaries, and other
  Codex-generated modeling artifacts.

Do not put extracted claims or modeling decisions in `sources/`. Keep source
registries limited to source IDs, titles, URLs, local file paths, and basic
location metadata. If multiple registries use one raw source, keep one physical
copy in its primary level folder and link to that path from the other
registries.

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
- Extracted source claims grouped by source ID.
- Candidate decision matrix.
- Adopted child BOM shape.
- Explicit defer/reject/split-boundary rationale for candidates that could
  otherwise be mistaken as omissions.
- Manufacturing readiness statement. The default is not-local-ready unless a
  separate material/process review says otherwise.

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

## Review Standard

For each proposed child item, reviewers should be able to answer:

- Which source introduced this candidate?
- Is the source EBF3-specific, subsystem-specific, or generic?
- Why was the candidate adopted, deferred, rejected, or split across a boundary?
- Does the child item increase fidelity without hiding unresolved material,
  precision, vacuum, high-voltage, electronics, or manufacturability questions?

Closure gaps are acceptable during this phase. Validation errors are not.
