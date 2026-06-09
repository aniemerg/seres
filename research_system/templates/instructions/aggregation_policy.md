# Aggregation Policy Template

Define how completed task results should be combined.

Recommended outputs:
- `aggregate/master_table.csv`
- `aggregate/needs_review.csv`
- `aggregate/materials_table.csv`
- `aggregate/evidence_table.csv`
- `aggregate/manufacturing_steps_table.csv`
- `aggregate/conflicts.csv`
- `aggregate/summary.md`

Table meanings:
- `master_table.csv`: one readable summary row per completed task.
- `needs_review.csv`: the subset of master rows where `needs_human_review` is true.
- Detail tables preserve one-to-many data that would make the master table hard
  to read.

Flag results for review when:
- Required evidence is missing.
- Confidence is low.
- Two tasks make conflicting recommendations.
- The result proposes a high-complexity import or new KB candidate.

Do not create or modify KB YAML directly unless the mission explicitly permits it.
