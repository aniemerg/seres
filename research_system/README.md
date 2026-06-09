# Research System

Parallel research mission tooling for SERES.

Use this system for research tasks, such as BOM-wide part research or paper extraction missions.

## Where The Code Lives

The runnable Python implementation lives under:

- `src/research_system/core.py` - mission ingest, SQLite state, lease/complete,
  schema validation, and aggregation logic
- `src/research_system/cli.py` - `python -m src.cli research ...` command wiring

This `research_system/` directory contains user-facing documentation, templates,
and example/test missions:

- `docs/` - design notes
- `templates/` - reusable mission manifest, instruction, and schema templates
- `research_missions/` - concrete research mission directories such as
  `test_mission`

Start with:

```bash
python -m src.cli research --help
```

## CLI Command Reference

All commands operate on one research mission directory:

```bash
python -m src.cli research <command> --mission research_missions/<mission_id>
```

### `ingest`

Generate task files from `mission_manifest.yaml` and initialize
`state.sqlite`.

```bash
python -m src.cli research ingest --mission research_missions/mission_bom_parts_001
```

Use `--reset` to replace existing mission tasks and clear prior state:

```bash
python -m src.cli research ingest --mission research_missions/mission_bom_parts_001 --reset
```

### `status`

Show task counts by status, such as `pending`, `leased`, `completed`, and
`needs_review`.

```bash
python -m src.cli research status --mission research_missions/mission_bom_parts_001
```

### `lease`

Lease the next pending task for one agent. The returned JSON includes the task
payload, source files, lease owner, and lease expiration time.

```bash
python -m src.cli research lease --mission research_missions/mission_bom_parts_001 --agent codex-01
```

Optional lease TTL:

```bash
python -m src.cli research lease --mission research_missions/mission_bom_parts_001 --agent codex-01 --ttl 1800
```

### `validate-result`

Validate a worker result file against the mission output schema without changing
task state.

```bash
python -m src.cli research validate-result --mission research_missions/mission_bom_parts_001 --result outputs/task_x.result.yaml
```

### `complete`

Mark a leased task as completed. This command validates the result file first.
The result must include the matching `task_id`.

```bash
python -m src.cli research complete \
  --mission research_missions/mission_bom_parts_001 \
  --task task_x \
  --agent codex-01 \
  --result outputs/task_x.result.yaml
```

### `release`

Release a leased task back to `pending`.

```bash
python -m src.cli research release \
  --mission research_missions/mission_bom_parts_001 \
  --task task_x \
  --agent codex-01
```

Use `--failed` to move the task to `needs_review` instead of returning it to the
pending pool:

```bash
python -m src.cli research release \
  --mission research_missions/mission_bom_parts_001 \
  --task task_x \
  --agent codex-01 \
  --failed \
  --message "Could not find enough evidence for material composition."
```

### `gc`

Expire stale leases whose TTL has passed and return those tasks to `pending`.

```bash
python -m src.cli research gc --mission research_missions/mission_bom_parts_001
```

### `aggregate`

Aggregate completed result files into `aggregate/master_table.csv`,
`aggregate/needs_review.csv`, detail tables, and `aggregate/summary.md`.

```bash
python -m src.cli research aggregate --mission research_missions/mission_bom_parts_001
```

Aggregate outputs:

- `master_table.csv`: one readable summary row per completed task.
- `needs_review.csv`: the subset of `master_table.csv` where `needs_human_review` is true.
- `materials_table.csv`: one row per material entry, including its own `source_file`.
- `evidence_table.csv`: one row per evidence claim.
- `manufacturing_steps_table.csv`: one row per manufacturing step, including the `how_to_make.source_file`.
- `summary.md`: counts and output file list.

Design docs:

- `docs/research_system_design.zh.md`
- `docs/research_system_design.en.md`

Templates:

- `templates/mission_manifest.yaml`
- `templates/instructions/`
- `templates/schemas/`
