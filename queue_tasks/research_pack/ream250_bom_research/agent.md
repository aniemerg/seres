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
2. Treat BOM-side supplied evidence as one evidence class:
   `bom_provided`. This includes BOM row fields, manifest mappings, the CAD/STEP
   package provided with the BOM, local metadata extracted from those CAD files,
   rendered CAD previews, and the BOM-provided vendor/product URL route. That
   route includes the exact BOM `link_url`, redirects, official canonical
   replacements, and first-party support/product pages reached by following
   links or navigation from the BOM-provided product page for the same row.
3. If BOM-side supplied evidence directly states or measures the value needed
   for a section, use it with `evidence_basis: bom_provided`. Do not web-search
   just to second-guess directly provided BOM-side evidence.
4. Use independent vendor/web research only to fill a value that BOM-side
   evidence did not directly resolve, or to resolve a placeholder/conflict. Use
   `evidence_basis: independent_vendor_spec` only when the vendor/catalog/drawing
   fact came from agent-initiated web search rather than from the BOM-provided
   URL route. Facts obtained through the BOM-provided URL route remain
   `bom_provided`.
   If BOM-side evidence does not resolve the needed value, perform at least one
   targeted web/search sanity check before falling back to
   `engineering_hypothesis`, even when the row has no manufacturer, product ID,
   standard designation, or URL. Build low-cost queries from the strongest
   available row clues: `cad_file`, `description_or_product_id`, manufacturer,
   product ID, BOM item, parent assembly, sibling row names, part-family nouns,
   and terms such as `material`, `datasheet`, `catalog`, `drawing`, `technical
   data`, or `weight`. If those searches produce no row-specific usable facts,
   keep the value as `engineering_hypothesis` and make the absence of
   row-specific web/vendor evidence visible in the relevant section's
   `uncertainty_notes` when it affects downstream trust.
5. Use `standard_part_convention` only after BOM-side evidence and row-matched
   independent vendor/web evidence do not resolve the value, but a standard
   designation or part family supports a generic conclusion.
6. Use `engineering_hypothesis` only when the value is inferred from function,
   assembly context, visible shape, or plausible manufacturing route.
7. Use `unresolved` when the relevant checks do not support a reliable value.

When a section value is derived from multiple evidence classes, set
`evidence_basis` to the least reliable evidence class needed for the conclusion.
Reliability order, highest to lowest:

1. `bom_provided`
2. `independent_vendor_spec`
3. `standard_part_convention`
4. `engineering_hypothesis`

`unresolved` is not a reliability tier. Prefer a conservative
`engineering_hypothesis` whenever the row identity, geometry, standard family, or
function supports a defensible broad conclusion. Use `unresolved` only when even
that broad engineering hypothesis would be misleading.

For mass, do not downgrade solely because arithmetic is involved. If the mass is
computed from BOM-provided CAD/STEP volume and BOM-provided material identity,
keep `evidence_basis: bom_provided`. Once the material grade/family is resolved
from BOM-side evidence, including the BOM-provided URL route, using a
standard/common density for that material is a calculation constant, not a
separate evidence class; cite the density value in `mass.basis` or
`mass.assumptions`, but do not add a generic density datasheet solely to
determine `evidence_basis`. For a multi-material part, distinguish
source facts from the composition estimate. If the component materials and total
CAD volume are BOM-side facts but the material volume fractions or effective
density are guessed without a cited source, set
`mass.source.evidence_basis: engineering_hypothesis`. Put the guessed
fraction/effective-density choice in `mass.assumptions`, and keep the residual
consequence in `mass.uncertainty_notes`. Keep `mass.source.evidence_basis:
bom_provided` for multi-material parts only when the mass itself, material
fractions, split-volume CAD, or another sourced physical input resolves the
composition closely enough that the mass no longer depends on an unsupported
ratio guess.

Before searching the web for a common density, check the local standard density
table at `kb/materials/properties.yaml`. If that table contains the resolved
material family/grade or an obvious alias, use that density as the calculation
constant. Do not add an external density source solely for common materials such
as stainless steel 304/1.4301, aluminum, steel, copper, brass, NBR, FKM, or
silicone rubber.

For material specifically:

1. Check the BOM row material fields, notes, manufacturer, product ID,
   `description_or_product_id`, and `third_party_link_url`. If a BOM material
   family or grade field directly states material, use it and stop material
   lookup unless another local source clearly conflicts.
2. Check local CAD/STEP material metadata. The per-part STEP often omits
   material, but the full assembly may contain it. Do this before using a
   vendor/product link unless the BOM row's own material fields already directly
   state the material. If
   `design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step`
   exists, run:

   ```bash
   .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py \
     --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step \
     --product-name "<cad_file>"
   ```

   Cite the material and density from this output as `bom_provided` when present,
   but do not treat
   placeholder values such as `Generic`, `Default`, `Material`, `None`,
   `unspecified`, empty strings, or density `1000.0` without a real material
   name as resolved material evidence.
3. If BOM and local CAD/STEP material evidence are missing, placeholder/generic,
   or conflicting, continue to web/vendor research before assigning
   `material.primary_material`. Use row-matched vendor/product routes first when
   manufacturer, product ID, standard designation, DIN/ISO/SKF/SMC/etc. part
   name, or `third_party_link_url` exists. If those stronger identifiers do not
   exist, still do a low-cost targeted search using `cad_file`,
   `description_or_product_id`, BOM item, parent assembly, sibling row names,
   and part-family nouns. If no row-specific source is found, record a broad
   material family as an `engineering_hypothesis` and keep the material
   uncertainty explicit.
4. Use the vendor/product URL first when present in the leased BOM context. Facts
   retrieved by opening that provided URL are still `bom_provided` because the
   BOM supplied the path to the matched product. If no provided URL resolves the
   needed value, try any official canonical replacement described in the
   vendor/product page parsing rules below. Only after the BOM-provided URL and
   its official row-matched canonical replacement do not resolve the value,
   search the web using targeted queries built from manufacturer + product
   ID/designation + words such as `material`, `datasheet`, `catalog`, `drawing`,
   `seal material`, `body material`, or `housing material`. Facts found through
   those agent-initiated searches are `independent_vendor_spec`. Use at most 4
   external sources unless the row cannot be resolved without more.
   Example: if a BOM-provided product page title or product information says
   "aluminum outer ring" or "NBR", record those materials as `bom_provided`;
   do not report the material as unresolved.
5. Failed material checks are not automatically result uncertainties. Mention a
   failed provided URL, targeted search, or network access problem only if the
   material section remains less specific or less reliable because of it. If
   another BOM-provided source resolves the material, do not record the failed
   check as `material.uncertainty_notes`.
6. If none of those sources states the material, prefer a broad
   `engineering_hypothesis` over `unresolved` when the part function or geometry
   supports one, such as `elastomer seal material`, `unknown metal/alloy`,
   `ceramic insulation material`, or `polymer cable jacket material`. Do not
   claim a specific grade from function alone. Record any mass estimate as a
   scenario in `mass.basis`.
7. Use `unresolved` for material only when the evidence does not support even a
   broad material family. Do not write `unresolved ...` in
   `material.primary_material`; use a broad hypothesized family or `unknown
   material` with clear uncertainty notes.

For vendor/product page parsing:

- Follow redirects and cite the final loaded URL in `source.url_or_path` when it
  differs from the BOM URL. It is still `bom_provided` if the original URL came
  from the BOM context.
- Pfeiffer Vacuum legacy URLs under
  `https://www.pfeiffer-vacuum.com/.../shop/products/<product_id>` may return
  HTTP 403/406 or an anti-bot/challenge page even when the official migrated
  product page exists. Before treating that as an unresolved provided URL, try
  the official Busch Group canonical URL
  `https://www.shop.buschgroup.com/global/en/products/<product_id>/`. If that
  page matches the BOM product ID or legacy number, cite it as the final loaded
  URL and keep `evidence_basis: bom_provided`; do not downgrade it to
  `independent_vendor_spec`.
- If the official canonical page is large or minified, do not abandon it just
  because a broad scan is slow. Save the HTML and extract targeted snippets with
  narrow patterns for the product ID, legacy number, `main material`, `O-ring
  material`, `material`, `aluminum`, `NBR`, `FKM`, `stainless`, the part-family
  nouns, and download links. If those snippets resolve the row material or
  function, cite the canonical page as `bom_provided`.
- If the BOM-provided product page links or navigates to first-party
  product-family, support, technology, or downloads pages from the same vendor
  and those pages resolve the same row's value, cite those pages as
  `bom_provided`. Example: if a BOM-provided Karl Hipp product-family page leads
  to the vendor's ballscrew page that states spindle material, that material is
  `bom_provided`, not `independent_vendor_spec`.
- Do not replace a row-matched BOM-provided/canonical source with an independent
  search result only because the independent PDF or catalog is easier to parse.
  Independent search results may be supplemental, but the `evidence_basis` stays
  `bom_provided` when the same fact was resolved from the BOM-provided URL or
  official canonical replacement.
- Do not search only for explicit `Material:` table labels. Product pages often
  encode material in the page title, H1, breadcrumbs, Product Information
  bullets, overview bullets, collapsed accordions, downloads, or short snippets.
  Scan those fields before declaring that a provided URL did not resolve
  material.
- Treat assembly wording as material evidence when it names components, such as
  "aluminum outer ring", "NBR", "stainless steel body", or "FKM seal". Preserve
  component-specific wording instead of collapsing it to one material.
- If the provided URL does not resolve the value, broaden search queries beyond
  `<product_id> material`. Combine manufacturer, product ID, `cad_file`,
  `description_or_product_id`, and part-family nouns from the row name such as
  `centering ring`, `outer ring`, `seal`, `clamp`, `flange`, `hose`, `valve`,
  `bearing`, or `sensor`, plus terms such as
  `material`, `body material`, `seal material`, `datasheet`, `catalog`,
  `drawing`, and `technical data`.

For standard part conventions specifically:

- The standard/designation input must be complete enough for the claimed fact.
- Standard family alone may support broad function, interface, or geometry, but
  it must not be used to claim material unless the designation, suffix, class, or
  cited standard convention encodes that material.
- Explain the parameter completeness in `source.cited_fact_or_basis`; e.g. state
  which DIN/ISO/SKF/SMC designation parameters were present and whether they are
  sufficient for function, interface, dimensions, material, or none of those.

Do not write values like `steel, assumed`, `aluminum, assumed`, or
`stainless steel, assumed` in `material.primary_material`. If material is based
on inference, put the broad material family in `material.primary_material`, set
`material.source.evidence_basis: engineering_hypothesis`, and put the inference
basis in `material.source.cited_fact_or_basis`.

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

Do not list non-contributing source/audit details as uncertainties. The
following are not uncertainty notes when the section value is already resolved:

- "BOM material family and specific material grade fields are blank."
- "Local assembly STEP material metadata found only Generic material with
  density 1000.0."
- "The original BOM-provided URL returned HTTP 403."
- "No catalog mass was found."

Only keep the downstream consequence if it matters. For example, for a
multi-material seal with total CAD volume but no split-volume CAD, the useful
mass uncertainty is that the aluminum-to-NBR volume fraction is unresolved; the
failed or missing checks that led there do not need separate notes.

Do not repeat the same idea across these fields with different wording. A fact
goes in `cited_fact_or_basis`; the modeling premise that uses that fact goes in
`assumptions`; the remaining consequence or risk goes in `uncertainty_notes`.

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

After following the evidence decision order above, use exactly one
`evidence_basis` value:

- `bom_provided` - BOM row fields, manifest data, BOM-provided CAD/STEP/local metadata/previews, or a BOM-provided vendor URL states or measures the fact.
- `independent_vendor_spec` - a vendor datasheet/catalog/drawing or product page found through agent-initiated web search states the fact.
- `standard_part_convention` - a sufficiently complete standard designation or part family supports the fact; explain parameter completeness in `cited_fact_or_basis`.
- `engineering_hypothesis` - inference from function, CAD shape, assembly context, or manufacturing route.
- `unresolved` - evidence was checked but does not support even a defensible broad engineering hypothesis.

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
