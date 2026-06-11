# Agent Instructions: reAM250 BOM Research

You are processing one-off reAM250 BOM research tasks.

## Lease Only Matching Research Tasks

If the user or batch runner provides an exact lease command, use that exact
command. Otherwise, use this default hard-filtered lease command:

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
the lease command's `--id-prefix`, release it immediately and stop.

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

For material, use this evidence order:

1. Check local CAD/STEP material metadata first. The per-part STEP often omits
   material, but the full assembly may contain it. If
   `design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step`
   exists, run:

   ```bash
   .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py \
     --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step \
     --product-name "<cad_file>"
   ```

   Cite the material and density from this output when present.
2. Check the BOM row fields, manufacturer, `description_or_product_id`, and
   `third_party_link_url`.
3. Use web search/product pages when a manufacturer, product ID, or vendor URL
   is available and local CAD/BOM evidence does not state material or conflicts
   with surrounding evidence.
4. If none of those sources states the material, do not name a specific metal
   or polymer from function alone. Use a broader value such as
   `unknown metal/alloy` with low confidence, and record any mass estimate as a
   scenario in `mass.basis`.

Do not write values like `steel, assumed`, `aluminum, assumed`, or
`stainless steel, assumed` in `material.primary_material`. A function-based
guess is an uncertainty note, not a sourced material.

Keep research concise. Use at most 4 external sources per result unless the row
cannot be resolved without more.

## Result Format

Write each result to `context.output_path`.

If `context.output_path` already exists, treat it as a stale prior draft. You
may read it for comparison, but you must re-check the leased row's current BOM,
CAD geometry, assembly material metadata, and web/vendor evidence as applicable,
then overwrite the result file. Do not complete a leased task by validating an
existing output file as-is.

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
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py --file <output_path>
```

Do not complete the queue item if validation fails.

Complete without `--verify`:

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```
