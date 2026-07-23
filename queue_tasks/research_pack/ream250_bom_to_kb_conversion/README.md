# reAM250 BOM to KB Conversion Task Pack

This task pack converts completed reAM250 BOM research rows into reviewed KB
staging decisions. It is intentionally separate from the original BOM research
pack.

The system has three phases:

1. `row_conversion`: one task per reAM250 BOM research row.
2. `merge_review`: one task per candidate merge group.
3. `phase3_staging`: one staging package per completed merge review selected
   for KB promotion testing.

Workers do not write directly to `kb/`, do not run the indexer, and do not edit
the original research evidence except for a single `## KB Conversion` section at
the bottom of each row file.

## Phase 1: Row Conversion

Generate row conversion tasks:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/generate_row_conversion_tasks.py \
  --replace-queue-prefix
```

Lease row conversion tasks:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-kb-row-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_row_
```

The worker reads the original row research file and appends or replaces only the
bottom `## KB Conversion` section. The validator compares a baseline hash for
the content before that section, so edits to the original evidence layer fail
validation.

Phase 1 exists to create a controlled decision layer before merge review. Each
row records decomposition, normalized merge identity, one primary process bucket,
supporting process tags, candidate existing KB process IDs, and precision
guardrails. It does not create final KB items, recipes, provider machines, or
import decisions.

Complete a row task with:

```bash
.venv/bin/python -m src.cli queue complete \
  --id <leased-id> \
  --agent <agent-name> \
  --require-output \
  --validate-output
```

Semantic-validate completed row conversions after a batch:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/semantic_validate_row_conversions.py \
  --output research/ream250_bom/kb_conversion/semantic_validate_report.md
```

Schema validate checks hard format and schema constraints. Semantic validate
runs schema validate, checks queue/conversion consistency, and reports semantic
warnings such as narrow functional keys, suspicious process buckets,
powder-containment rows grouped as enclosure barriers, and speculative local
manufacturing paths. Hard errors return non-zero. Warnings are reported without
failing the command unless `--fail-on-warning` is used.

The batch QA workflow is:

1. Schema validate every completed row conversion.
2. Review only new warnings listed under `New Semantic Warnings`.
3. Review the no-warning rows listed under `Random Review Sample` to discover
   new error patterns that semantic validate does not know yet.

## Phase 2: Merge Review

After row conversion tasks are complete, generate candidate merge tasks:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/generate_merge_candidate_tasks.py \
  --replace-queue-prefix
```

The generator reads all `## KB Conversion` sections and groups rows that have:

- `merge_pool.eligible: true`
- the same `merge_pool.functional_purpose_key`
- mass within a 2x range

It does not decide final merges. It only creates candidate groups. The
`functional_purpose_key` is a rough index for grouping; merge review workers
must read the original row research evidence and the `## KB Conversion` section
for every candidate row.

Phase 2 reviews whether rows from that rough pool can converge to the same
closure item after material, process, geometry, and precision checks. It should
use the detailed original research evidence, not only the Phase 1 functional key.

Lease merge review tasks:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-kb-merge-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_merge_
```

Merge review workers write group-level decisions under:

```text
research/ream250_bom/kb_conversion/merge_reviews/
```

## Phase 3: Staging

Phase 3 converts a completed merge review into a KB staging package. It does not
write to `kb/`. It decides, for each proposed closure item:

- whether to `reuse_existing`, `create_new`, or `defer`;
- whether the item should be import, locally manufacturable, or a local
  manufacture candidate with blockers;
- how source BOM rows map to closure item IDs, preserving quantity, mass,
  length, handedness, and variant guardrails;
- which existing KB processes are recipe anchors;
- which blockers prevent promotion to final KB YAML.

Generate Phase 3 staging tasks after merge review files exist:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/generate_phase3_staging_tasks.py \
  --replace-queue-prefix
```

Lease Phase 3 staging tasks:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-kb-stage-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_stage_
```

Phase 3 workers write staging files under:

```text
research/ream250_bom/kb_conversion/phase3_staging/
```

Maintainer-written pilot examples live under:

```text
research/ream250_bom/kb_conversion/phase3_staging_pilot/
```

Validate a Phase 3 staging file with:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/schema_validate_row_conversions.py \
  --kind phase3_stage \
  --file research/ream250_bom/kb_conversion/phase3_staging/<file>.stage.yaml
```

## Reviewer Feedback Loop

After reviewing worker outputs, the reviewer/maintainer updates this task pack
when a correction reveals a recurring rule gap. Output fixes and rule updates
should move together when the issue can repeat in later batches. Typical updates
belong in `agent.md`, `acceptance_criteria.md`,
`conversion_section.schema.yaml`, `research_scripts/schema_validate_row_conversions.py`,
and `research_scripts/semantic_validate_row_conversions.py`.

## Files

- `agent.md` - Worker SOP for all phases.
- `acceptance_criteria.md` - Quality and modeling rules.
- `conversion_section.schema.yaml` - Required `## KB Conversion` structure.
- `merge_review.schema.yaml` - Required merge review structure.
- `phase3_staging.schema.yaml` - Required Phase 3 staging structure.
- `research_scripts/generate_row_conversion_tasks.py` - Creates Phase 1 queue tasks and baseline hashes.
- `research_scripts/generate_merge_candidate_tasks.py` - Creates Phase 2 queue tasks from Phase 1 outputs.
- `research_scripts/generate_phase3_staging_tasks.py` - Creates Phase 3 staging tasks from merge review files.
- `research_scripts/schema_validate_row_conversions.py` - Validates row conversion sections, merge review files, and Phase 3 staging files.
- `research_scripts/semantic_validate_row_conversions.py` - Batch semantic warning report for row conversions and queue consistency.
- `research_scripts/run_codex_batches.sh` - Optional short-session Codex runner for row, merge, and stage phases.

## Optional Batch Runner

Run one small row-conversion batch:

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase row \
  --max-items 1 \
  --max-batches 1 \
  --semantic-validate-after
```

Run a larger row-conversion batch and write the semantic validate report after the workers finish:

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase row \
  --max-items 20 \
  --max-batches 1 \
  --semantic-validate-after \
  --semantic-validate-output research/ream250_bom/kb_conversion/semantic_validate_report.md \
  --semantic-validate-sample-size 5
```

Run one small merge-review batch:

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase merge \
  --max-items 1 \
  --max-batches 1
```

Run one small Phase 3 staging batch:

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase stage \
  --max-items 1 \
  --max-batches 1
```
