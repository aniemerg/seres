# Agent Instructions: reAM250 BOM Research

You are processing one-off reAM250 BOM research tasks.

Each leased research task represents exactly one reAM250 BOM row. Process only
that row, using the row-specific context fields from the leased queue item.

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

## Research Objective

For each leased row, research and write one Markdown result at
`context.output_path`. The result must describe:

- `function`: what the row item does in the machine.
- `mass`: the best supported row-level mass estimate in kg, with calculation
  basis.
- `material`: the best supported material family, grade, or component material
  set.
- `how_to_make`: a plausible manufacturing, assembly, or procurement route.
- `kb_implications`: exactly one item granularity planning signal for later KB
  modeling.

Do not stop after gathering CAD evidence or web links. The task is complete only
after the result file is written, validated, and the queue item is completed.

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
inference. Round CAD-derived values before writing the research result: volume to
about 0.001 mm^3 for small parts, bounding-box dimensions to about 0.01 mm, and
mass to a sensible precision for the row scale. Keep full precision only when it
changes the interpretation.

Also render a compact CAD preview contact sheet for visual triage:

```bash
output_dir="$(dirname "<output_path>")"
output_stem="$(basename "<output_path>" .md)"
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem"
```

The renderer writes a 2x2 PNG contact sheet with iso, front, top, and right
views next to the Markdown result file, using the result basename plus
`__views_2x2.png`. Inspect that contact sheet before writing the result. Use it
to identify visible shape features such as plates, brackets, flanges, holes,
slots, shafts, pulleys, seals, and whether a machining, sheet cutting, or
assembly route is plausible. Treat the preview as visual triage only; do not use
it for exact measurement.

If the contact sheet is too small or important details are not visible, first
rerun the renderer for only the needed individual view(s) and inspect those
view(s):

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem" \
  --view front
```

Use `--view iso`, `--view front`, `--view top`, or `--view right`; repeat
`--view` if two orientations are needed. Use `--individual-views` only when all
four orientations are needed. Increase `--dpi` only as a rare fallback for a
selected individual view, not as the default 2x2 contact-sheet setting.

When using an image-capable API that supports image detail settings, inspect the
compact 2x2 contact sheet first with `detail: "low"` to reduce image-token cost.
When using a local tool that does not support `low` detail, such as the Codex
`view_image` tool, omit `detail` or use that tool's supported default instead.
Escalate to a selected individual view, then to higher detail only when the
compact contact sheet is insufficient. Include the CAD filename in the prompt
because the image itself does not carry source metadata. See
`queue_tasks/research_pack/ream250_bom_research/image_token_optimization_for_agents.md`
for the token-budget rationale.

Use the CAD geometry and preview together as row-specific evidence for function,
mass, and manufacturing inference. If `cad_export_status` is `assembly_only`,
`ambiguous`, or `missing_in_cad`, or if rendering fails, explain the CAD evidence
limitation in the affected section's `uncertainty_notes`.

Also check local CAD/STEP material metadata. The per-part STEP often omits
material, but the full assembly may contain row-specific material metadata. If
`design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step`
exists, run:

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py \
  --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step \
  --product-name "<cad_file>"
```

## Result Production Workflow

For each leased row:

1. Lock the row identity from the BOM row and manifest.
2. Collect BOM-side evidence: BOM fields, manifest mapping, CAD/STEP geometry,
   rendered preview, local STEP material metadata, and any BOM-provided URL
   route.
3. Resolve `function`, `material`, `mass`, and `how_to_make` section values for
   that row. Use CAD evidence for geometry/function/mass clues, but do not treat
   CAD inspection as a substitute for writing the result sections.
4. Use web/vendor research when BOM-side evidence does not resolve a needed
   section value, or when BOM-side evidence is placeholder, generic, or
   conflicting. Follow BOM-provided URL routes first when they exist. Use
   independent web/vendor search only as allowed by `acceptance_criteria.md`.
5. Before using `evidence_basis: engineering_hypothesis` or
   `evidence_basis: unresolved`, apply AC-WEB-001 and AC-WEB-002 in
   `acceptance_criteria.md`; the same section must include
   `targeted_web_search:` with the query terms tried and the result.
6. Write or overwrite the result file at `context.output_path`, validate it, and
   complete the queue item.

## Acceptance Checklist

Before writing each result section, apply:

```text
queue_tasks/research_pack/ream250_bom_research/acceptance_criteria.md
```

Use that file as the authority for result-quality decisions, especially:

- row identity locking
- evidence_basis selection
- targeted_web_search requirement before `engineering_hypothesis` or `unresolved`
- BOM URL, official alternate route, and independent-source route audits
- material precision and placeholder-material handling
- mass evidence rules, common density handling, and multi-material estimates
- manufacturing-route evidence for `how_to_make`
- standard part convention parameter completeness
- source / assumptions / uncertainty separation
- item_granularity selection

Keep research concise. Use at most 4 external sources per result unless the row
cannot be resolved without more. Follow BOM-provided URL routes first when they
exist; use independent web/vendor research only as allowed by the acceptance
criteria.

## Result Format

Write each result to `context.output_path`.

If `context.output_path` already exists, treat it as a stale prior draft. You
may read it for comparison, but you must re-check the leased row's current BOM,
CAD geometry, assembly material metadata, and web/vendor evidence as applicable,
then overwrite the result file. Do not complete a leased task by validating an
existing output file as-is.

Each Markdown result must start with YAML frontmatter matching:

```text
queue_tasks/research_pack/ream250_bom_research/research_result.schema.yaml
```

The first top-level key in the frontmatter must be `row_identity`. This section
must preserve only the minimal BOM row identity before any interpretation. Put
these keys here and no others:

- `item`: `context.item`
- `cad_file`: `context.cad_file`
- `source_row_number`: `context.source_row_number`
- `source_csv`: `design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv`
- `link_url`: include this only when the BOM row has a Link URL; use
  `context.bom_link_url` when present, otherwise `context.third_party_link_url`.
  This is the original BOM table Link URL, not the redirected/canonical final
  vendor URL.

Put `row_identity` before `function`, so readers see the BOM name before the
inferred function, material, mass, or manufacturing notes.

The `function`, `mass`, `material`, and `how_to_make` sections must each have
their own source object with:

- `url_or_path`
- `cited_fact_or_basis`
- `evidence_basis`

Those same four sections must each also include section-local lists:

- `assumptions`
- `uncertainty_notes`

Put assumptions and uncertainty notes in the section they affect. For example,
material limitations that still affect the final material value belong under
`material.uncertainty_notes`, CAD-density mass caveats belong under
`mass.uncertainty_notes`, and inferred fabrication routes belong under
`how_to_make.assumptions` or `how_to_make.uncertainty_notes`.

Use `kb_implications` to leave one machine-searchable item granularity signal for
later KB modeling. Do not add a new top-level field. Include exactly one bullet
starting with `item_granularity: <value> - ...`. Allowed values are listed in
`research_result.schema.yaml`; tie-breaker and judgment rules are defined in
`acceptance_criteria.md`.

Use exactly one `evidence_basis` value per section source. Allowed values and
decision rules are defined in `research_result.schema.yaml` and
`acceptance_criteria.md`.

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
