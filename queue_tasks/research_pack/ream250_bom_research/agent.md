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
inference.

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

If the contact sheet is too small or important details are not visible, rerun
the renderer with individual views and inspect only the needed view(s):

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem" \
  --individual-views
```

When using an image-capable model/API for this inspection, send the 2x2 contact
sheet with `detail: "low"` first. Escalate to higher detail or individual views
only when the low-detail contact sheet is insufficient. Include the CAD filename
in the prompt because the image itself does not carry source metadata.

Use the CAD geometry and preview together as row-specific evidence for function,
mass, and manufacturing inference. If `cad_export_status` is `assembly_only`,
`ambiguous`, or `missing_in_cad`, or if rendering fails, explain the CAD evidence
limitation in the affected section's `uncertainty_notes`.

Use this evidence decision order for each result section:

1. Lock the row identity from the BOM and manifest first. The BOM row, item,
   CAD file, quantity, manufacturer, product ID/description, and manifest
   mapping define which part this task is about. Do not use web results to
   reinterpret the row as a different product.
2. If the BOM row directly states the value needed for a section, use that value
   and set `evidence_basis: bom_row`. Do not web-search just to second-guess a
   directly stated BOM value.
3. If local CAD geometry, STEP metadata, CAD preview, manifest fields, or local
   extracted metadata directly states or measures the value, use it with
   `evidence_basis: cad_or_local_metadata`.
4. Use vendor/web research only to fill a value that BOM/CAD/local evidence did
   not directly resolve, or to resolve a placeholder/conflict. Vendor/web sources
   are attribute sources for the already-locked row identity; they do not
   override the BOM identity.
5. Use `standard_part_convention` only after BOM/CAD/local evidence and
   row-matched vendor/web evidence do not resolve the value, but a standard
   designation or part family supports a generic conclusion.
6. Use `engineering_hypothesis` only when the value is inferred from function,
   assembly context, visible shape, or plausible manufacturing route.
7. Use `unresolved` when the relevant checks do not support a reliable value.

For material specifically:

1. Check the BOM row material fields, notes, manufacturer, product ID,
   `description_or_product_id`, and `third_party_link_url`. If a BOM material
   family or grade field directly states material, use it and stop material
   lookup unless another local source clearly conflicts.
2. Check local CAD/STEP material metadata. The per-part STEP often omits
   material, but the full assembly may contain it. If
   `design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step`
   exists, run:

   ```bash
   .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py \
     --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step \
     --product-name "<cad_file>"
   ```

   Cite the material and density from this output when present, but do not treat
   placeholder values such as `Generic`, `Default`, `Material`, `None`,
   `unspecified`, empty strings, or density `1000.0` without a real material
   name as resolved material evidence.
3. If BOM and local CAD/STEP material evidence are missing, placeholder/generic,
   or conflicting, continue to web/vendor research before assigning
   `material.primary_material` whenever any of these row clues exist:
   manufacturer, product ID, standard designation, DIN/ISO/SKF/SMC/etc. part
   name, or `third_party_link_url`.
4. Use the vendor/product URL first when present. Otherwise search the web using
   targeted queries built from manufacturer + product ID/designation + words
   such as `material`, `datasheet`, `catalog`, `drawing`, `seal material`,
   `body material`, or `housing material`. Use at most 4 external sources unless
   the row cannot be resolved without more.
5. Record the web/vendor outcome in the result even when it fails. If the search
   finds no material source, add a `material.uncertainty_notes` bullet naming
   the query or vendor/product page checked and why it did not resolve material.
   If network access fails, record the failure concretely instead of silently
   stopping at `Generic`.
6. If none of those sources states the material, do not name a specific metal
   or polymer from function alone. Use a broader value such as
   `unknown metal/alloy` with `evidence_basis: engineering_hypothesis` or
   `unresolved`, and record any mass estimate as a scenario in `mass.basis`.

Do not write values like `steel, assumed`, `aluminum, assumed`, or
`stainless steel, assumed` in `material.primary_material`. A function-based
guess belongs in `material.uncertainty_notes`, not in a sourced material value.

Keep research concise. Use at most 4 external sources per result unless the row
cannot be resolved without more.

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

The `function`, `mass`, `material`, and `how_to_make` sections must each have
their own source object with:

- `url_or_path`
- `cited_fact_or_basis`
- `evidence_basis`

Those same four sections must each also include section-local lists:

- `assumptions`
- `uncertainty_notes`

Put assumptions and uncertainty notes in the section they affect. For example,
material search failures belong under `material.uncertainty_notes`, CAD-density
mass caveats belong under `mass.uncertainty_notes`, and inferred fabrication
routes belong under `how_to_make.assumptions` or `how_to_make.uncertainty_notes`.

After following the evidence decision order above, use exactly one
`evidence_basis` value. This is a source type, not a global truth ranking:

- `bom_row` - BOM row fields, labels, material hints, or notes state the fact.
- `vendor_spec` - vendor datasheet/catalog/drawing or product page states the fact.
- `cad_or_local_metadata` - local STEP/CAD metadata, CAD geometry, CAD preview, or local extracted data states the fact.
- `standard_part_convention` - standard designation or part family supports the fact, but no row-specific vendor material source was found.
- `engineering_hypothesis` - inference from function, CAD shape, assembly context, or manufacturing route.
- `unresolved` - evidence was checked but does not support even a material family or firm functional claim.

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
