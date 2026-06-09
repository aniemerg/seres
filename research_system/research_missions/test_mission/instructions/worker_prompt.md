# Test Mission Worker Prompt

You will receive one fake BOM part research task from `test_mission`.

For the leased part, produce a structured YAML result that answers:

- What is the estimated mass per unit?
- What function does it serve in the parent assembly?
- What is its likely material composition?
- How would it be made industrially?
- Which claims are supported by which source files?

Use only the fake files in `input/` for this validation mission. Do not browse
the web for this test mission.

Return only a structured result matching `schemas/result.schema.yaml`.

Rules:
- Preserve source BOM row IDs in `source_bom_rows`.
- Put every factual claim in `evidence` as `{claim, source_file}`.
- Every `material_composition.materials` entry must include `source_file`.
- `how_to_make` must include `source_file`.
- If a material or manufacturing route cannot be sourced, write `source_file: unknown`
  and state the uncertainty clearly.
- State uncertainty explicitly in `uncertainty_notes`.
- Do not edit KB files.
- Do not overwrite input files.
- Write only `outputs/<task_id>.result.yaml`.
