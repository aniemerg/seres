# Test Mission Aggregation Policy

Aggregate completed fake result files into a flat master table and a review
table.

Expected outputs:
- `aggregate/master_table.csv`
- `aggregate/needs_review.csv`
- `aggregate/materials_table.csv`
- `aggregate/evidence_table.csv`
- `aggregate/manufacturing_steps_table.csv`
- `aggregate/summary.md`

Table meanings:
- `master_table.csv`: one readable summary row per completed part task.
- `needs_review.csv`: the subset of master rows where `needs_human_review` is true.
- `materials_table.csv`: one row per material, including material-specific `source_file`.
- `evidence_table.csv`: one row per evidence note.
- `manufacturing_steps_table.csv`: one row per manufacturing step, using `how_to_make.source_file`.

Flag results for review when:
- Required evidence is missing.
- Confidence is low.
- `needs_human_review` is true.
- The item is electronics or another high-complexity component.

Do not create or modify KB YAML. This mission only validates the research
system workflow.
