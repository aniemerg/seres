# Research System Design

## Purpose

The research system is a parallel research task system independent from the existing KB work queue. Its purpose is to let many Codex agents process a large set of research items concurrently, inspect related files, screenshots, documents, or external sources, and produce structured results that can be validated and aggregated.

The existing KB queue is driven by the indexer: the indexer detects KB gaps, an agent fixes the KB, and the gap is complete when it disappears. The research system is driven by a user-defined research mission: the system turns input data into tasks, many agents analyze those tasks in parallel, and an aggregator produces research outputs, KB candidate data, or follow-up queue items.

## Core Concepts

### Research Mission

A research mission is one concrete research effort, for example:

- Analyze every part in a BOM and determine mass, function, material composition, and how to make it.
- Extract process conditions, energy use, inputs, outputs, and uncertainties from a batch of papers.
- Review vendor components and decide which should be reused, imported, folded into a parent assembly, or promoted as KB candidates.

Each mission has its own input, instructions, schemas, tasks, outputs, and aggregate results.

### Mission Manifest

`mission_manifest.yaml` is the entrypoint configuration file for a mission. It describes the research mission: what the goal is, where the data is, what agents should do, and what valid results look like, while keeping the professional software term `manifest`.

`manifest` usually means a machine-readable list or configuration file. The `mission_` prefix keeps the user-facing meaning clear: this is not a generic program manifest, but the manifest for a specific research mission.

## Recommended Directory Layout

```text
research_system/
  docs/
    research_system_design.zh.md
    research_system_design.en.md
  templates/
    mission_manifest.yaml
    instructions/
    schemas/

research_missions/
  mission_bom_parts_001/
    mission_manifest.yaml
    input/
    instructions/
    schemas/
    tasks/
    state.sqlite
    outputs/
    logs/
    aggregate/
```

`research_system/` contains system code, documentation, and templates. `research_missions/` contains the data and results for concrete research missions.

## Required Mission Files

Each research mission should provide at least:

```text
mission_manifest.yaml
input/
instructions/
schemas/
```

### `mission_manifest.yaml`

This file describes the whole mission:

- mission id
- objective
- input files
- task generation strategy
- worker prompt
- output schema
- execution settings
- completion rule
- aggregation outputs

Example:

```yaml
id: mission_bom_parts_001
mission_type: bom_part_research
objective: >
  For each unique BOM part, determine mass, function, material composition,
  and how it could be manufactured or modeled in SERES KB.

input:
  primary_file: input/bom.csv
  source_catalog: input/source_catalog.csv

task_generation:
  strategy: unique_part_or_part_family
  rules_file: instructions/task_generation_rules.md

worker:
  prompt_file: instructions/worker_prompt.md
  output_schema: schemas/part_research_result.schema.yaml
  max_attempts: 3

execution:
  max_workers: 20
  lease_ttl_seconds: 1800

completion_rule:
  type: schema_valid_result
  require_evidence: true

aggregation:
  policy_file: instructions/aggregation_policy.md
  outputs:
    - aggregate/parts_master.csv
    - aggregate/needs_review.csv
    - aggregate/kb_candidates.csv
    - aggregate/summary.md
```

### `input/`

This directory stores immutable source data: BOMs, PDFs, screenshots, datasheets, papers, OCR text, source catalogs, or other mission-specific files. Workers should not overwrite source inputs.

### `instructions/`

This directory stores task semantics and research rules, for example:

- `worker_prompt.md`
- `task_generation_rules.md`
- `evidence_policy.md`
- `aggregation_policy.md`

This layer is what lets the same research system handle very different research missions.

### `schemas/`

This directory defines the required structure for each worker result. Schemas make automatic validation and aggregation possible and prevent workers from producing only unstructured prose.

## Execution Flow

```text
1. Create mission directory
2. Write mission_manifest.yaml, input, instructions, schemas
3. Ingest input into task files
4. Initialize state.sqlite
5. Launch N Codex workers
6. Workers lease tasks and write structured outputs
7. Validate each output against schema
8. Aggregate completed results
9. Review conflicts and low-confidence outputs
10. Optionally promote results to KB candidates or KB queue items
```

## CLI Commands

The first implementation is mounted under the existing unified CLI:

```bash
python -m src.cli research ingest --mission research_missions/mission_bom_parts_001
python -m src.cli research status --mission research_missions/mission_bom_parts_001
python -m src.cli research lease --mission research_missions/mission_bom_parts_001 --agent codex-01
python -m src.cli research validate-result --mission research_missions/mission_bom_parts_001 --result outputs/task_x.result.yaml
python -m src.cli research complete --mission research_missions/mission_bom_parts_001 --task task_x --agent codex-01 --result outputs/task_x.result.yaml
python -m src.cli research release --mission research_missions/mission_bom_parts_001 --task task_x --agent codex-01
python -m src.cli research gc --mission research_missions/mission_bom_parts_001
python -m src.cli research aggregate --mission research_missions/mission_bom_parts_001
```

`ingest` generates `tasks/*.json` from the mission manifest and initializes `state.sqlite`. `lease` uses a SQLite transaction, so multiple workers can safely request work concurrently. `complete` validates the result against the mission schema before marking the task completed.

### Command Details

- `ingest`: Read `mission_manifest.yaml` and input files, generate `tasks/*.json`, and initialize or update `state.sqlite`. If the mission already has tasks, use `--reset` to clear prior state and rebuild.
- `status`: Show task counts by status, such as `pending`, `leased`, `completed`, and `needs_review`.
- `lease`: Let a named agent claim the next pending task. The returned JSON includes the task payload, source files, lease owner, and lease expiration.
- `validate-result`: Validate a result YAML/JSON file against the mission schema without changing task state.
- `complete`: Complete a leased task. This validates the result first, and the result's `task_id` must match `--task`.
- `release`: Return a leased task to `pending`. With `--failed`, move it to `needs_review`, which is useful when evidence is insufficient or the agent is stuck.
- `gc`: Expire stale leases and return tasks whose TTL has passed to `pending`.
- `aggregate`: Combine completed task results. `master_table.csv` is a readable one-row-per-task summary; `needs_review.csv` is the subset where `needs_human_review: true`; `materials_table.csv`, `evidence_table.csv`, and `manufacturing_steps_table.csv` preserve one-to-many details.

## Worker Behavior

Each worker follows this loop:

```text
lease task
read task payload
read relevant input/source files
follow worker_prompt
produce result YAML/JSON
validate result against schema
complete task
repeat
```

Workers should only write:

```text
outputs/<task_id>.result.yaml
logs/<agent>/<task_id>.log
```

Workers should not directly modify `kb/`, and they should not overwrite `input/`. Research outputs should be aggregated first, then a human reviewer or a downstream KB workflow can decide what should enter the KB.

## BOM Part Research Example

For a BOM-wide part research mission, the task grain should usually be unique part or part family, not one task per BOM row. This avoids having multiple agents research the same screw, washer, cable, or other repeated component.

Each part result should include at least:

- source BOM rows
- estimated mass
- function
- material composition
- how to make it
- evidence
- uncertainty
- KB modeling recommendation

Example recommendation:

```yaml
kb_modeling_recommendation:
  action: reuse_existing
  rationale: "Equivalent fastener family already exists within acceptable scale bounds."
```

Allowed actions:

- `reuse_existing`
- `create_candidate`
- `fold_into_parent`
- `import`
- `exclude`
- `needs_review`

## Relationship To The Existing KB Queue

The research system and KB queue should stay separate:

```text
Research system:
  Produce evidence-backed research results, candidate data, and recommendations.

KB queue:
  Fix concrete KB schema, closure, validation, and missing-reference gaps.
```

The aggregation stage can connect the two by producing:

- `aggregate/kb_candidates.csv`
- `aggregate/proposed_yaml/`
- `aggregate/followup_queue.jsonl`

This lets the research system provide evidence-backed candidate data without allowing many research workers to mutate the KB concurrently.

## Design Principles

- Keep research missions separate from the KB validation queue.
- Use mission-specific instructions and schemas.
- Use structured outputs, not free-form prose.
- Preserve source traceability.
- Make uncertainty explicit.
- Prefer aggregation and review before KB mutation.
- Let many agents work in parallel, but avoid concurrent writes to KB.
