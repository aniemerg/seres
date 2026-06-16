# reAM250 BOM Research Task Pack

This folder contains one-off support files for the reAM250 BOM research run. It
is not part of the generic research queue system.

## Files

- `agent.md` - Prompt/instructions for a Codex agent processing
  reAM250 BOM research queue items.
- `research_result.schema.yaml` - Expected structured result shape.
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
`--individual-views` only when the compact preview is insufficient.

## Research Evidence Rules

Evidence decision order:

- First lock row identity from BOM + manifest. Web/vendor evidence may fill
  missing attributes for that identity, but should not reinterpret the row as a
  different product.
- Treat BOM row fields, manifest data, the supplied CAD/STEP package, local
  metadata extracted from that package, rendered CAD previews, and the
  BOM-provided vendor/product URL route as one evidence class: `bom_provided`.
  That route includes the exact BOM `link_url`, redirects, official canonical
  replacements, and first-party support/product pages reached by following links
  or navigation from the BOM-provided product page for the same row.
- Use independent vendor/web research when BOM-side evidence does not directly
  resolve the needed value, or when BOM-side evidence is placeholder/generic/
  conflicting.
- If BOM-side evidence does not resolve the needed value, do at least one
  targeted web/search sanity check before falling back to
  `engineering_hypothesis`, even when the row has no manufacturer, product ID,
  standard designation, or URL. Build low-cost queries from `cad_file`,
  `description_or_product_id`, BOM item, parent assembly, sibling row names,
  part-family nouns, and terms such as `material`, `datasheet`, `catalog`,
  `drawing`, `technical data`, or `weight`. If no row-specific usable source is
  found, keep the result conservative and make that absence visible in the
  relevant section's uncertainty when it affects downstream trust.
- A row-matched official canonical replacement derived from a BOM-provided URL
  is still BOM-side evidence. Do not downgrade it to independent research.
- First-party support/product-family/technology/download pages reached from the
  BOM-provided product page route are also BOM-side evidence for the same row.
  Example: if a BOM-provided Karl Hipp product-family page leads to the vendor's
  ballscrew page that states spindle material, that material is `bom_provided`,
  not `independent_vendor_spec`.
- If a section value depends on multiple evidence classes, use the least reliable
  evidence class needed for that conclusion.

Evidence basis labels:

Allowed `evidence_basis` values, in reliability order:

- BOM-side supplied evidence states or measures the value -> `bom_provided`
- Agent-initiated web search finds a vendor/catalog/drawing/product-page fact -> `independent_vendor_spec`
- DIN/ISO/SKF/SMC/etc. designation or standard part family supports the fact -> `standard_part_convention`
- Function, assembly context, visible shape, or manufacturing route inference -> `engineering_hypothesis`
- Checked evidence does not support even a defensible broad engineering hypothesis -> `unresolved`

For mass, arithmetic does not by itself lower the evidence class. A value
computed from BOM-provided CAD/STEP volume and BOM-provided material identity is
still `bom_provided`. Once the material grade/family is resolved from BOM-side
evidence, including the BOM-provided URL route, a standard/common density for
that material is a calculation constant, not a separate evidence class; record
the density value in `mass.basis` or `mass.assumptions`, but do not add a generic
density datasheet solely to set `evidence_basis`. For a multi-material part,
distinguish source facts from the
composition estimate. If the component materials and total CAD volume are
BOM-side facts but the material volume fractions or effective density are
guessed without a cited source, set `mass.source.evidence_basis:
engineering_hypothesis`. Put the guessed fraction/effective-density choice in
`mass.assumptions`, and keep the residual consequence in
`mass.uncertainty_notes`. Keep `mass.source.evidence_basis: bom_provided` for
multi-material parts only when the mass itself, material fractions, split-volume
CAD, or another sourced physical input resolves the composition closely enough
that the mass no longer depends on an unsupported ratio guess.

For common material densities, check `kb/materials/properties.yaml` before web
search. If the resolved BOM-side material maps to that local table, treat the
density as a calculation constant and keep the mass evidence class determined by
the BOM-side material and CAD/STEP evidence. Do not add an external density
datasheet solely for common stainless steel, aluminum, steel, copper, brass,
NBR, FKM, or silicone rubber densities.

For `standard_part_convention`, record parameter completeness in
`cited_fact_or_basis`. Standard family alone may support broad function or
interface, but should not support material unless the designation, suffix, class,
or cited convention encodes material.

Prefer a conservative `engineering_hypothesis` over `unresolved` whenever the
row identity, geometry, standard family, or function supports a broad conclusion.
For material, do not write `unresolved ...` as the primary material; use a broad
hypothesized family such as `elastomer seal material` or `unknown metal/alloy`
with `evidence_basis: engineering_hypothesis`.

Vendor/product page parsing rules:

- Follow redirects and cite the final loaded URL. If the original URL came from
  the BOM context, redirected-page facts are still `bom_provided`.
- For Pfeiffer Vacuum legacy product URLs like
  `https://www.pfeiffer-vacuum.com/.../shop/products/<product_id>`, HTTP 403/406
  or a challenge page is not enough to conclude the BOM-provided URL failed.
  Try the official Busch Group canonical URL
  `https://www.shop.buschgroup.com/global/en/products/<product_id>/` before
  independent search. If it matches the BOM product ID or legacy number, cite
  that final URL and keep `evidence_basis: bom_provided`.
- If the official canonical page is large or minified, extract targeted snippets
  for the product ID, legacy number, material fields, material words, part-family
  nouns, and download links instead of abandoning the canonical source. Do not
  replace a row-matched BOM-provided/canonical source with an independent PDF or
  catalog only because that source is easier to parse.
- Scan page title/H1, breadcrumbs, Product Information bullets, overview bullets,
  collapsed accordions, downloads, snippets, and technical tables before saying
  material was not resolved.
- Preserve component material wording such as `aluminum outer ring` or `NBR`;
  do not collapse assemblies to a single material.
- If the provided URL does not resolve a value, broaden queries using
  manufacturer, product ID, BOM/CAD row name, part-family nouns, and terms such
  as `material`, `body material`, `seal material`, `datasheet`, `catalog`,
  `drawing`, and `technical data`.

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

Standard bounded run:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3 \
  --max-batches 1
```

This runs at most `2 * 3 * 1 = 6` rows:

- `--workers 2` starts two parallel worker loops.
- `--max-items 3` lets each fresh Codex session process at most three leased rows.
- `--max-batches 1` lets each worker start at most one fresh Codex session.

The runner defaults to `--codex-sandbox danger-full-access` because web research
rows need local DNS/network access. Override with
`--codex-sandbox workspace-write` only for no-network/local-only runs.

To test a specific Codex model, pass `--codex-model`. If omitted, the runner
uses the Codex CLI configured default model. To control reasoning level for
models that support it, pass `--codex-reasoning-effort low|medium|high|xhigh`.

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.3-spark \
  --validate-at-end
```

Example with GPT-5.5 medium reasoning:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --validate-at-end
```

When writing the command across multiple lines, keep the trailing `\` on every
continued line. If the `\` after `--max-items 3` is missing, the shell starts the
runner without `--max-batches`, and `--max-batches 1` is treated as a separate
command.

Single-worker full run until queue empty:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh
```

This uses the script defaults: one worker, at most three rows per fresh Codex
session, and no batch limit. It keeps running until no matching pending queue
items remain.

Smoke test one Codex session:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --max-batches 1
```

Print the generated prompt without running Codex:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --dry-run
```

Logs are written to `out/ream250_bom_runner_logs/` by default.

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

Use `kb_implications` to leave one machine-searchable item granularity signal for
later KB modeling. Do not add a new top-level field. Include exactly one bullet
starting with `item_granularity: <value> - ...`, choosing the best current value:

- `simple_part` - one main physical part that can plausibly be made from stock
  or bulk material by one dominant fabrication route.
- `assembly` - multiple physical parts joined together, with an eventual sub-BOM
  or assembly recipe likely needed.
- `purchased_module` - vendor functional module or calibrated subsystem, such as
  a laser module, sensor head, pump, controller, or other item that should be
  treated as purchased/imported until a sub-BOM and calibration workflow are
  modeled.
- `consumable` - replaceable operating or maintenance item such as a seal,
  filter, lubricant, adhesive, or cable tie.
- `raw_material_or_stock` - stock material, bulk material, fastener stock, sheet,
  bar, tube, wire, or other feedstock-like row.
- `unknown` - the row identity is too ambiguous to assign a useful granularity.

Keep this as a planning hint, not a hard schema claim. If the row could fit more
than one value, choose the one that best predicts how the KB should model it
next; explain the ambiguity after the dash.

Field semantics:

- `source.cited_fact_or_basis`: source facts only. Include what the cited URL,
  file, CAD measurement, local metadata extractor, or standard table directly
  says/measures. Do not include interpretations, guesses, caveats, or why the
  fact might be incomplete.
- `assumptions`: premises adopted to transform facts into the section value.
  These are chosen modeling choices, not source facts. Use this for unit
  interpretation, representative density choices, effective-density choices,
  using a single-solid CAD volume as a proxy, or an inferred manufacturing route.
  Use `[]` when no extra premise was needed beyond the cited facts.
- `uncertainty_notes`: residual limitations after applying the facts and
  assumptions. This is not an audit log of every failed lookup. Write a note
  only if removing it would make a downstream reader over-trust, over-specify,
  or misuse the section value. Do not include a failed check, missing field,
  rejected source, or redirect/blocking detail unless it still creates a real
  limitation for the final value. Use `[]` when no meaningful residual
  limitation remains.

Avoid duplicated wording across these fields. A fact goes in
`cited_fact_or_basis`; the modeling premise that uses that fact goes in
`assumptions`; the remaining consequence or risk goes in `uncertainty_notes`.

Do not list non-contributing source/audit details as uncertainties once the
section value is already resolved. Examples that should usually be omitted:
blank BOM material fields, rejected Generic/density-1000 CAD metadata, HTTP 403
from the original URL after a row-matched canonical source succeeds, and "No
catalog mass was found." Keep only the downstream consequence if it matters, such
as an unresolved material-volume split in a multi-material mass estimate.

Mass examples:

- Good `cited_fact_or_basis`: "FreeCAD measured 5586.124 mm^3; the BOM-provided
  vendor page states aluminum and NBR; the local density table lists aluminum
  and NBR densities."
- Good `assumptions`: "The single-solid STEP volume is used as a coarse combined
  material-volume proxy because the CAD does not expose separate aluminum and
  NBR regions."
- Good `uncertainty_notes`: "The aluminum-to-NBR volume fraction is not measured
  separately, so the mass remains an unsupported effective-density estimate."
- Bad `assumptions`: "The STEP volume is millimeter-based." That is a unit/fact
  basis, so put it in `mass.basis` or `source.cited_fact_or_basis`.
- Bad `uncertainty_notes`: a non-contributing audit detail that does not change
  how a downstream reader should trust, specify, or use the section value.

## Completion

Complete research tasks without `--verify`:

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```

Do not run `python -m src.cli index` during this one-off research workflow.
