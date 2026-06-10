# reAm250 BOM Research Queue Plan

## Purpose

Create one research queue task per unique BOM row in
`research/input/reAm250_BOM.csv`. Each task asks an agent to research one BOM
line item and write a standalone YAML result under `research/output/reAm250/`.

The goal is research output only. Agents must not edit KB files and must not
overwrite or modify files under `research/input/`.

## Input

- Source file: `research/input/reAm250_BOM.csv`
- Row count: 401 data rows
- Unique `Item` values: 400
- Known duplicate `Item`: `2AP6`
  - `2AP6_outer_seal`
  - `2AP6_inner_seal`

Columns:

- `Item`
- `Qty`
- `CAD file`
- `Description / Product ID`
- `Manufacturer`
- `Link URL`
- `Subsystem (suggested)`
- `Material family`
- `Specific material / grade`
- `Notes`
- `Page`
- `Raw row text`

## Task Granularity

Create one task per unique BOM row, not one task per unique `Item` value.

For most rows, the task ID can use the item number:

```text
reAm250_<Item>
```

For rows where `Item` is duplicated, use the CAD file name to disambiguate:

```text
reAm250_2AP6_outer_seal
reAm250_2AP6_inner_seal
```

If future duplicates appear, use the same rule: prefer the CAD file name when it
is clearer than the item number. Sanitize task IDs for filenames by replacing
spaces and unsafe punctuation with `_`.

## Queue Item Format

Use the normal queue with research task markers:

- `kind: research`
- `gap_type: research_task`
- `item_id: <task_id>`

Example queue item:

```json
{
  "kind": "research",
  "gap_type": "research_task",
  "item_id": "reAm250_70",
  "description": "Research reAm250 BOM item 70 and write a standalone YAML result file. Do not edit KB files or input files.",
  "context": {
    "source_file": "research/input/reAm250_BOM.csv",
    "source_row_number": 324,
    "output_path": "research/output/reAm250/reAm250_70.yaml",
    "bom_row": {
      "Item": "70",
      "Qty": "1",
      "CAD file": "70_dummy_laser_beam_source",
      "Description / Product ID": "AFX - 1000",
      "Manufacturer": "nLight",
      "Link URL": "https://static1.squarespace.com/static/628d22a4cced8544470496fe/t/654533e22ca7ac1dafd952e0/1699034082388/nLIGHT_AFX_Series_Product_Sheet_30AUG2023+version+1.pdf",
      "Page": "9",
      "Raw row text": "70 1 70_dummy_laser_beam_source AFX - 1000 nLight"
    },
    "done_criteria": "Write the YAML result at output_path. Include sources for web information. Mark uncertain estimates explicitly. Do not edit KB files."
  }
}
```

## Agent Instructions Per Task

Each queued task should instruct the agent to:

1. Treat the BOM row in `context.bom_row` as the source item to research.
2. Use the provided manufacturer, product ID, CAD file name, link URL, raw row
   text, and web search as needed.
3. Cite every web page, PDF, datasheet, or local source used.
4. Clearly separate source-backed facts from estimates or inference.
5. Write exactly one YAML file to `context.output_path`.
6. Do not write shared aggregate files.
7. Do not edit KB files.
8. Do not modify or overwrite files under `research/input/`.
9. Complete the queue item only after the YAML result has been written.

## Research Output Location

Each row gets its own file:

```text
research/output/reAm250/<task_id>.yaml
```

Examples:

```text
research/output/reAm250/reAm250_70.yaml
research/output/reAm250/reAm250_2AP6_outer_seal.yaml
research/output/reAm250/reAm250_2AP6_inner_seal.yaml
```

Agents must not write to a single shared result file.

## YAML Result Schema

Use this structure for each result file:

```yaml
task_id: reAm250_70
source:
  source_file: research/input/reAm250_BOM.csv
  source_row_number: 324
  item: "70"
  qty: "1"
  cad_file: "70_dummy_laser_beam_source"
  description_product_id: "AFX - 1000"
  manufacturer: "nLight"
  link_url: "https://..."
  page: "9"
  raw_row_text: "70 1 70_dummy_laser_beam_source AFX - 1000 nLight"

candidate_entry:
  candidate_id: laser_beam_source_afx_1000_v0
  candidate_name: AFX 1000 laser beam source
  item_category: part
  short_description: >
    Concise description of what this BOM item appears to be.

function:
  summary: >
    What the part does in the machine or subsystem.
  confidence: high|medium|low

mass:
  estimated_value: null
  unit: kg
  basis: >
    Source, datasheet value, dimensional estimate, analogous part, or unknown.
  confidence: high|medium|low

material_composition:
  summary: >
    Main materials or likely material families.
  materials:
    - material: null
      role: null
      evidence: null
  mixed_materials: true|false|null
  confidence: high|medium|low

manufacturing:
  basic_idea: >
    Basic idea of how this part is made industrially.
  additive_3d_printing_assessment:
    suitability: good|possible|poor|not_applicable|unknown
    rationale: >
      Whether additive manufacturing is plausible or useful.
  forming_or_machining_assessment:
    suitability: good|possible|poor|not_applicable|unknown
    rationale: >
      Whether machining, forming, casting, molding, cutting, extrusion, or
      similar methods are more appropriate.
  preferred_process_summary: >
    Best-fit manufacturing route for modeling purposes.
  confidence: high|medium|low

complexity:
  is_complex_part: true|false|null
  has_multiple_subparts: true|false|null
  has_mixed_material_subparts: true|false|null
  should_break_down_for_this_research: false
  reasoning: >
    Explain whether this appears to be a single material part, a simple
    purchased component, or a complex assembly with many subparts. Do not
    create a subpart breakdown; describe construction only as needed.

reuse:
  is_likely_reusable_kb_part: true|false|null
  reusable_as: null
  rationale: >
    Explain whether this part is likely generic/reusable across the KB or
    specific to this reAm250 design.
  confidence: high|medium|low

known_details:
  summary: >
    Detailed description of what is known, including dimensions, specs,
    product identifiers, supplier details, operating role, and uncertainty.
  open_questions:
    - null

sources:
  - title: null
    url_or_path: null
    accessed_or_used_date: null
    relevant_fields:
      - null
    notes: null

work_log:
  search_queries:
    - null
  pages_or_files_checked:
    - null
  reasoning_notes: >
    Briefly explain how conclusions were reached, especially where the result
    depends on inference from CAD filename, manufacturer naming, or analogous
    components.

warnings:
  - null
```

Use `null` when the information cannot be determined. Do not invent precise
values. Rough estimates are acceptable only when labeled with a basis and low or
medium confidence.

## Complex Parts Policy

These tasks should identify whether a BOM item appears complex, but should not
break complex parts into subparts. A complex part is one with multiple subparts,
multiple material families, or distinct construction processes.

For example, a laser module may contain optics, electronics, cooling, housing,
connectors, and control components. The research output should describe that
complexity and likely materials at a high level, but should not attempt to build
a detailed sub-BOM unless a future task explicitly asks for that.

## Completion

Research tasks are completed according to their instructions, not by indexer
verification. Use:

```bash
python -m src.cli queue complete --id research_task:<task_id> --agent <name>
```

Do not use `--verify` for these research tasks.

## Open Implementation Step

Before enqueueing, generate JSONL queue entries from
`research/input/reAm250_BOM.csv` using the task ID and output-path rules above.
Do not enqueue `.DS_Store` files or any input-file metadata as tasks.
