# Agent Instructions: reAM250 BOM Research

You are processing one-off reAM250 BOM research tasks.

## Lease Only Matching Research Tasks

Lease with hard filters:

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_bom_row_
```

If the command returns `queue empty`, stop.

If a leased item does not have `kind: research` or its `id` does not start with
`research_task:ream250_bom_row_`, release it immediately and stop.

## Process A Small Batch

Process at most the item limit given by the current user or runner prompt. If no
limit is provided, process at most 3 queue items in one Codex session. Stop when
that limit is reached even if more queue items remain.

## Allowed Edits

Only create or update result files under:

```text
research/ream250_bom/
```

Do not edit KB YAML, source code, docs, queue tasks, or generated index files.
Do not run:

```bash
python -m src.cli index
```

## Research Requirements

Use the leased item's `context` fields:

- `source_csv`
- `manifest_csv`
- `bom_row_number`
- `source_row_number`
- `quantity`
- `cad_file`
- `canonical_step_path`
- `cad_export_status`
- `description_or_product_id`
- `manufacturer`
- `third_party_link_url`
- `output_path`

After leasing a task, read the row's CAD file if `canonical_step_path` exists
and `cad_export_status` is not `missing_in_cad`. Use the local FreeCAD wrapper:

```bash
.tools/freecad/freecadcmd -c "import Part; p='<canonical_step_path>'; s=Part.Shape(); s.read(p); bb=s.BoundBox; print(len(s.Solids), s.Volume, s.Area, bb.XLength, bb.YLength, bb.ZLength)"
```

Use that geometry as row-specific evidence for mass and shape/function
inference. If `cad_export_status` is `assembly_only`, `ambiguous`, or
`missing_in_cad`, explain the CAD evidence limitation in `uncertainty_notes`.

Keep research concise. Use at most 4 external sources per result unless the row
cannot be resolved without more.

## Result Format

Write each result to `context.output_path`.

Each Markdown result must start with YAML frontmatter:

```yaml
---
function:
  summary:
  source:
    url_or_path:
    cited_fact_or_basis:
    confidence:
mass:
  value_kg:
  basis:
  source:
    url_or_path:
    cited_fact_or_basis:
    confidence:
material:
  primary_material:
  source:
    url_or_path:
    cited_fact_or_basis:
    confidence:
how_to_make:
  summary:
  manufacturing_steps: []
  source:
    url_or_path:
    cited_fact_or_basis:
    confidence:
assumptions: []
uncertainty_notes: []
kb_implications: []
---
```

Hard source rule: `function`, `mass`, `material`, and `how_to_make` must each
have their own source object with:

- `url_or_path`
- `cited_fact_or_basis`
- `confidence`

## Validate Before Completion

Run:

```bash
.venv/bin/python queue_tasks/research_mission/ream250_bom_research/research_scripts/validate_results.py --file <output_path>
```

Do not complete the queue item if validation fails.

Complete without `--verify`:

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```
