# reAM250 BOM Research Task Pack

This folder contains one-off support files for the reAM250 BOM research run. It
is not part of the generic research queue system.

## Files

- `research_instructions/agent.md` - Prompt/instructions for a Codex agent processing
  reAM250 BOM research queue items.
- `research_schemas/research_result.schema.yaml` - Expected structured result shape.
- `research_scripts/generate_queue_tasks.py` - Build queue items from the gold
  CSV/manifest package, optionally extracting STEP metadata with FreeCAD.
- `research_scripts/validate_results.py` - Local validator for result Markdown/YAML/JSON
  files.
- `research_scripts/run_codex_batches.sh` - Optional batch runner that repeatedly starts
  fresh `codex exec` sessions.

## Queue Requirements

The queue should contain research tasks with:

- `kind: research`
- `gap_type: research_task`
- IDs starting with `research_task:ream250_bom_row_`
- `context.output_path` under `research/ream250_bom/`
- `context.output_validator` pointing to this task pack validator

Generate or refresh the 401 queue items from the gold CSV/manifest:

```bash
.venv/bin/python queue_tasks/research_mission/ream250_bom_research/research_scripts/generate_queue_tasks.py \
  --replace-queue-prefix
```

This replaces only existing queue entries whose IDs start with
`research_task:ream250_bom_row_`.

CAD geometry is intentionally read by the agent after it leases a specific row.
Use `--extract-cad-metadata` only for offline diagnostics, not for the normal
research queue run.

Lease with hard filters:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-bom-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_bom_row_
```

## Agent Usage

Open Codex from the repo root:

```bash
cd /home/eastrolinux/seres
codex --search -C /home/eastrolinux/seres -s workspace-write -a on-request
```

Then tell the agent:

```text
Read queue_tasks/research_mission/ream250_bom_research/research_instructions/agent.md and follow it as ream250-bom-agent-01.
```

Use a different agent name in each terminal, such as `ream250-bom-agent-02`.

## Session Limit

Each agent session should process at most 3 queue items. Restart or clear the
session for the next batch. This keeps web research context bounded and makes
failures easier to resume.

## Automated Batch Runner

For larger runs, use the task-local runner instead of manually clearing Codex or
opening new terminals. The runner starts a fresh `codex exec` session for each
small batch, so context does not accumulate across the whole BOM.

Conservative default:

```bash
queue_tasks/research_mission/ream250_bom_research/research_scripts/run_codex_batches.sh
```

Two workers, three rows per fresh Codex session:

```bash
queue_tasks/research_mission/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3
```

Smoke test one Codex session:

```bash
queue_tasks/research_mission/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --max-batches 1
```

Print the generated prompt without running Codex:

```bash
queue_tasks/research_mission/ream250_bom_research/research_scripts/run_codex_batches.sh --dry-run
```

Logs are written to `out/ream250_bom_runner_logs/` by default.

### Runner Risks

- If a Codex session crashes after leasing an item, that item remains leased
  until its TTL expires. Run `.venv/bin/python -m src.cli queue gc` after the TTL
  to return expired leases to pending.
- Parallel workers increase web-search/API usage and can hit external rate
  limits. Start with `--workers 1` or `--workers 2`.
- Do not run `python -m src.cli index` while the runner is active. This workflow
  relies on the research queue as the state source.
- The runner does not guarantee research quality. It only bounds context and
  automates fresh Codex sessions; use `research_scripts/validate_results.py` to check
  required result structure and source fields.

## Validate Results

Validate one file:

```bash
.venv/bin/python queue_tasks/research_mission/ream250_bom_research/research_scripts/validate_results.py \
  --file research/ream250_bom/ream250_bom_row_0001_11.md
```

Validate a directory:

```bash
.venv/bin/python queue_tasks/research_mission/ream250_bom_research/research_scripts/validate_results.py \
  --dir research/ream250_bom
```

The validator checks that `function`, `mass`, `material`, and `how_to_make`
each have their own source object containing:

- `url_or_path`
- `cited_fact_or_basis`
- `confidence`

## Completion

Complete research tasks without `--verify`:

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```

Do not run `python -m src.cli index` during this one-off research workflow.
