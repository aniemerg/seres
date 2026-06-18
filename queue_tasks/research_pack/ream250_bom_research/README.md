# reAM250 BOM Research Task Pack

This folder contains one-off support files for the reAM250 BOM research run. It
is not part of the generic research queue system.

## Files

- `agent.md` - Prompt/instructions for a Codex agent processing
  reAM250 BOM research queue items.
- `acceptance_criteria.md` - Result-quality acceptance rules for evidence
  classification, web-search fallback, route audits, material/mass judgment,
  field semantics, and item granularity.
- `research_result.schema.yaml` - Expected structured result shape.
- `image_token_optimization_for_agents.md` - Token-budget guidance for CAD
  preview image inspection, including when API `detail: "low"` is appropriate.
- `research_scripts/generate_queue_tasks.py` - Build queue items from the gold
  CSV/manifest package, optionally extracting STEP metadata with FreeCAD.
- `research_scripts/render_step_views.py` - Render a compact 2x2 PNG CAD preview
  from a STEP file for low-token visual inspection.
- `research_scripts/render_step_views.sh` - FreeCAD wrapper for the preview
  renderer; use this script from agent prompts.
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
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/generate_queue_tasks.py \
  --replace-queue-prefix
```

This replaces only existing queue entries whose IDs start with
`research_task:ream250_bom_row_`.

CAD geometry is intentionally read by the agent after it leases a specific row.
Use `--extract-cad-metadata` only for offline diagnostics, not for the normal
research queue run. When writing CAD-derived values into the result, round volume
to about 0.001 mm^3 for small parts, bounding-box dimensions to about 0.01 mm,
and mass to a precision appropriate for the row scale; do not paste excessive
floating-point precision unless it changes the interpretation.

Agents should also render the leased row's canonical STEP file to one compact
2x2 contact sheet for visual triage:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/<CAD file>.step" \
  --output-dir research/ream250_bom \
  --output-stem ream250_bom_row_<row>_<item>
```

This writes `research/ream250_bom/ream250_bom_row_<row>_<item>__views_2x2.png`
next to the Markdown result. Inspect the contact sheet first; generate
a selected individual view only when the compact preview is insufficient:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/<CAD file>.step" \
  --output-dir research/ream250_bom \
  --output-stem ream250_bom_row_<row>_<item> \
  --view front
```

Allowed selected views are `iso`, `front`, `top`, and `right`. Use
`--individual-views` only when all four individual orientations are needed.

## Research Evidence Rules

The authoritative result-quality rules live in
`acceptance_criteria.md`. `agent.md` is the worker SOP, this README is the human
operation manual, `research_result.schema.yaml` is the structural contract, and
`validate_results.py` enforces the mechanically checkable subset.

At a high level:

- Lock row identity from BOM + manifest before using web/vendor evidence.
- Treat BOM row fields, manifest data, supplied CAD/STEP files, local metadata,
  rendered previews, and BOM-provided URL routes as `bom_provided`.
- Use independent vendor/web research only when BOM-side evidence does not
  directly resolve the value, or when BOM-side evidence is
  placeholder/generic/conflicting.
- Before writing `engineering_hypothesis` or `unresolved`, perform targeted
  web/search checks and include `targeted_web_search:` in that same section.
- Use `official_alternate_route_check:` for different-domain official routes
  kept as `bom_provided`.
- Use `bom_url_route_check:` before relying on different-domain
  `independent_vendor_spec` when the BOM row had a Link URL.
- Follow the acceptance rules for material precision, mass evidence,
  common-density handling, field semantics, and item granularity.

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
codex --search -C /home/eastrolinux/seres -s danger-full-access -a on-request
```

This task needs local DNS/network access for vendor pages. In the current Codex
environment, `workspace-write` can make local `curl`/DNS fail before the agent
reaches the product page. Use `workspace-write` only for local-only debugging.

Then tell the agent:

```text
Read queue_tasks/research_pack/ream250_bom_research/agent.md and follow it as ream250-bom-agent-01.
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

### Runner Option Specification

Use this section as the authoritative runner contract. Examples below are only
common invocations of these options.

| Option | Default | Meaning |
|---|---:|---|
| `--repo-root PATH` | `/home/eastrolinux/seres` | Repository root used as `codex exec -C`. |
| `--agent-prefix NAME` | `ream250-bom-agent` | Prefix used to form worker agent names like `ream250-bom-agent-01`. |
| `--workers N` | `1` | Number of parallel worker loops. |
| `--max-items N` | `3` | Maximum queue items handled by each fresh Codex session. |
| `--max-batches N` | `0` | Maximum Codex sessions per worker; `0` means run until no matching pending items remain. |
| `--ttl SECONDS` | `7200` | Queue lease TTL passed to `queue lease`. |
| `--id-prefix PREFIX` | `research_task:ream250_bom_row_` | Queue id prefix used by `queue lease --id-prefix`; a complete task id acts as an exact single-row filter. |
| `--log-dir PATH` | `out/ream250_bom_runner_logs` | Directory for batch logs. Relative paths are resolved under the repo root. |
| `--codex-bin PATH` | `codex` or `$CODEX_BIN` | Codex executable. |
| `--codex-model MODEL` | `$CODEX_MODEL` or Codex config default | Model passed to `codex --model/-m`. Use `codex debug models` to list model ids available to the current account. |
| `--codex-reasoning-effort EFFORT` | `$CODEX_REASONING_EFFORT` or Codex config default | Reasoning level passed as `model_reasoning_effort`; valid values are `low`, `medium`, `high`, `xhigh`. Only applies to models that support reasoning levels. |
| `--codex-sandbox MODE` | `danger-full-access` or `$CODEX_SANDBOX` | Sandbox passed to Codex; valid values are `read-only`, `workspace-write`, `danger-full-access`. |
| `--batch-timeout SECONDS` | `0` | Optional timeout for each `codex exec` batch; `0` disables the timeout. A timed-out batch exits nonzero and is recorded in the run events file. |
| `--validate-at-end` | off | Runs queue/output audit after all workers exit. It validates only outputs for queue entries currently marked `done`; it does not validate every Markdown file in `research/ream250_bom`. |
| `--dry-run` | off | Prints the generated prompt and Codex command without starting Codex. |

Execution count is bounded by `workers * max-items * max-batches` when
`--max-batches` is greater than zero. For example, `--workers 2 --max-items 3
--max-batches 1` runs at most six rows. With `--max-batches 0`, each worker keeps
starting fresh Codex sessions until no matching pending queue items remain.

The default sandbox is `danger-full-access` because web research rows need local
DNS/network access. Use `workspace-write` only for local-only debugging where
web access is not needed.

`--validate-at-end` is intentionally queue-aware. During partial reruns, pending
older output files may fail the latest validator while waiting for rerun; the
runner therefore audits only outputs currently marked `done`. Use full-directory
validation only after all files in `research/ream250_bom` are expected to satisfy
the current rules.

Each real runner invocation writes run-level diagnostics under `--log-dir`.
The default run id is `<YYYYmmdd_HHMMSS>_<runner-pid>` and can be overridden with
`REAM250_BOM_RUN_ID`.

| Diagnostic file | Meaning |
|---|---|
| `run_<run_id>.log` | Master stdout/stderr log for the runner itself, including worker launch messages and final audit output. |
| `run_<run_id>_events.tsv` | Parseable event log with `runner_start`, `batch_start`, `batch_exit`, `signal`, and `runner_exit` records. |
| `run_<run_id>.heartbeat` | Last heartbeat timestamp. If this becomes stale and no `runner_exit` event exists, the process was likely killed externally or the host/session stopped. |
| `run_<run_id>_status/*.active` | Active batch marker files. Leftover files after an abrupt stop identify which worker/batch was running and which per-batch log to inspect. |
| `run_<run_id>_queue_start.json`, `run_<run_id>_queue_exit.json` | Queue count snapshots at start and exit. Signal exits also write `run_<run_id>_queue_signal_<SIG>.json`. |

If the runner receives `INT`, `TERM`, or `HUP`, it records a `signal` event,
writes a queue snapshot, and exits with the conventional signal status. If the
process is killed with `SIGKILL`, the machine powers off, or the WSL/session is
terminated hard, no shell trap can run; diagnose that case by the stale
heartbeat, missing `runner_exit`, and leftover active batch markers.

When writing commands across multiple lines, keep the trailing `\` on every
continued line. If a continuation is missing, the shell starts the runner early
and treats the following option as a separate command.

### Runner Examples

Standard bounded run:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3 \
  --max-batches 1 \
  --validate-at-end
```

Single-worker full run until queue empty:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh
```

Smoke test one Codex session with GPT-5.5 medium reasoning:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --validate-at-end
```

Smoke test one Codex session with GPT-5.3 Codex Spark:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.3-codex-spark \
  --validate-at-end
```

Print the generated prompt and Codex command without running:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --dry-run
```

### Targeted Reruns

The runner has an optional `--id-prefix` filter. If it is omitted, the runner
uses the normal broad prefix:

```text
research_task:ream250_bom_row_
```

That default means "any reAM250 BOM research row". Normal runs do not need to
pass `--id-prefix`.

The option is named `--id-prefix` because the queue lease API filters with
`startswith(...)`, not exact-id matching. Passing a complete queue id still works
as an exact single-row filter because the complete id is also a valid prefix of
itself.

To rerun a completed row, first release it back to `pending`, then run one
single-item batch with the complete queue id as the prefix:

```bash
.venv/bin/python -m src.cli queue release \
  --id research_task:ream250_bom_row_0195_6Q \
  --agent rerun-targeted

queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --id-prefix research_task:ream250_bom_row_0195_6Q
```

The runner prompt requires the agent to overwrite an existing output file after
re-checking evidence. If you are testing that behavior, verify the file mtime or
inspect the log for an actual file write.

`queue release --id` accepts one id at a time, and runner `--id-prefix` accepts
one prefix at a time. To rerun multiple exact rows, loop over complete queue ids
and run one single-item batch per id:

```bash
for id in \
  research_task:ream250_bom_row_0117_3F \
  research_task:ream250_bom_row_0144_3R2
do
  .venv/bin/python -m src.cli queue release \
    --id "$id" \
    --agent rerun-targeted

  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
    --workers 1 \
    --max-items 1 \
    --max-batches 1 \
    --id-prefix "$id"
done
```

Avoid using a shared broad prefix such as `research_task:ream250_bom_row_01` for
targeted reruns because it can lease unrelated pending rows.

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
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py \
  --file research/ream250_bom/ream250_bom_row_0001_11.md
```

Validate a directory:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py \
  --dir research/ream250_bom
```

Use full-directory validation only after all files in the directory are expected
to satisfy the current rules. During partial reruns, prefer the queue/output
audit because pending older files may intentionally fail the latest validator.

Audit queue/output consistency:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/audit_queue_outputs.py
```

This audit validates current output files and checks done queue entries against
their `context.output_path`. Historical done entries completed before the
strict output-validation baseline may have missing artifacts; those are reported
as `legacy_done_without_output_accepted` and do not fail the audit. Missing
outputs for newer done items still fail.

The validator checks that the first top-level frontmatter key is `row_identity`.
This section must preserve only the minimal BOM table identity before
interpretation. It must contain only these keys:

- `item`
- `cad_file`
- `source_row_number`
- `source_csv`: `design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv`
- `link_url`: include only when the BOM row has a Link URL; this is the original
  BOM table Link URL, not the redirected/canonical final vendor URL.

The validator also checks that `function`, `mass`, `material`, and `how_to_make`
each have their own source object containing:

- `url_or_path`
- `cited_fact_or_basis`
- `evidence_basis`

Those same sections must also each contain section-local lists:

- `assumptions`
- `uncertainty_notes`

Use section-local notes so material uncertainty stays under `material`, CAD mass
caveats stay under `mass`, and fabrication-route assumptions stay under
`how_to_make`. `kb_implications` remains a top-level list.

The validator also checks selected acceptance markers such as
`targeted_web_search:`, `official_alternate_route_check:`, and
`bom_url_route_check:` when the corresponding evidence basis and URL conditions
apply. It cannot check every judgment rule. Use `acceptance_criteria.md` for the
authoritative field semantics, evidence-basis decisions, material/mass
judgment, and item granularity rules.

## Completion

Complete research tasks without `--verify`:

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```

Do not run `python -m src.cli index` during this one-off research workflow.
