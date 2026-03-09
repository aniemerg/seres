# SRM2 Plan Quality Standard

Use this standard for all remaining per-result plans.

## Required quality bar
- Re-read the source result file(s) directly before drafting.
- Extract concrete architecture details into the plan (not just topic labels).
- Provide part-level decomposition for each major assembly.
- Map each BOM line to:
  - existing KB ID, or
  - explicit new ID with a clear spec role.
- Avoid placeholder modules like "generic subsystem" as final endpoints.
- Separate build modeling from operations modeling:
  - recipes = multi-step construction chains,
  - processes = executable operations with machine requirements.

## Import policy while planning
- Do not default whole assemblies to `is_import: true`.
- Semiconductor-level leaves may remain imported.
- Mechanical structures, harnessing, mounts, reducers, and packaging should be represented as locally buildable chains whenever feasible.

## Kapvik lesson learned
- High-value infrastructure (rovers) requires deep decomposition before edits.
- Existing KB rover entries can hide major inconsistencies (wheel count, subsystem omission, monolithic recipes).
- Start by normalizing existing IDs/recipes/BOMs before adding new modules.

## Deliverables per result
- A concise plan file.
- A detailed research-to-KB mapping report (citation-grade) for complex results.
- Clear implementation checklist in dependency order.
