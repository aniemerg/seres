# reAM250 BOM Research Task Pack

This folder contains one-off support files for the reAM250 BOM research run. It
is not part of the generic research queue system.

## Files

- `instructions/agent.md` - Prompt/instructions for a Codex agent processing
  reAM250 BOM research queue items.
- `schemas/research_result.schema.yaml` - Expected structured result shape.
- `scripts/validate_results.py` - Local validator for result Markdown/YAML/JSON
  files.

## Queue Requirements

The queue should contain research tasks with:

- `kind: research`
- `gap_type: research_task`
- IDs starting with `research_task:ream250_bom_row_`
- `context.output_path` under `research/ream250_bom/`

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
Read queue_tasks/ream250_bom_research/instructions/agent.md and follow it as ream250-bom-agent-01.
```

Use a different agent name in each terminal, such as `ream250-bom-agent-02`.

## Session Limit

Each agent session should process at most 3 queue items. Restart or clear the
session for the next batch. This keeps web research context bounded and makes
failures easier to resume.

## Validate Results

Validate one file:

```bash
.venv/bin/python queue_tasks/ream250_bom_research/scripts/validate_results.py \
  --file research/ream250_bom/ream250_bom_row_0001_11.md
```

Validate a directory:

```bash
.venv/bin/python queue_tasks/ream250_bom_research/scripts/validate_results.py \
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
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name>
```

Do not run `python -m src.cli index` during this one-off research workflow.
