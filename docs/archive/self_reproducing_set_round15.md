# Self-Reproducing Machine Set (Round 15)

This is the first run where the **requested machine set equals the produced machine set**.
We treat production as:
- `process_complete` outputs (process/recipe production)
- `build` events (BOM assembly)

Run: `minimal_self_repro_seq_7`  
Requested list: `out/next_round_machines_round15.txt` (135 machines)

## Outcome

- Requested machines: 135
- Produced machines: 135
- Imported machines: 117
- Produced but not imported: 18 (acceptable for this milestone)
- Imported but not produced: 0

Artifacts:
- Produced list: `out/minimal_self_repro_seq_7_produced_machines.txt`
- Imported list: `out/minimal_self_repro_seq_7_imported_machines.txt`
- Requested list: `out/next_round_machines_round15.txt`
- Requested not imported: `out/minimal_self_repro_seq_7_requested_not_imported.txt`

## How it was made

We iterated the target machine list by closing gaps between:
- machines requested
- machines produced
- machines imported

At Round 14 we added the "imported but not produced" machines to the target list.
Round 15 used that expanded list to converge on **requested == produced**.

## How to reproduce

1) Run the sequence:
```
.venv/bin/python scripts/analysis/simplan_run_sequence_checkpointed.py \
  --machine-list out/next_round_machines_round15.txt \
  --sim-id minimal_self_repro_seq_7 \
  --reset
```

2) Generate machine reports (production includes build events):
```
.venv/bin/python scripts/analysis/sim_machine_report.py --sim-id minimal_self_repro_seq_7
```

3) Compare requested vs produced vs imported:
```
.venv/bin/python - <<'PY'
from pathlib import Path

sim_id = "minimal_self_repro_seq_7"
requested = set(Path("out/next_round_machines_round15.txt").read_text().split())
imported = set(Path(f"out/{sim_id}_imported_machines.txt").read_text().split())
produced = set(Path(f"out/{sim_id}_produced_machines.txt").read_text().split())

print("requested:", len(requested))
print("produced:", len(produced))
print("imported:", len(imported))
print("requested_not_produced:", len(requested - produced))
print("produced_not_requested:", len(produced - requested))
print("imported_not_produced:", len(imported - produced))
print("produced_not_imported:", len(produced - imported))
PY
```

Expected at this milestone:
- `requested_not_produced = 0`
- `produced_not_requested = 0`
- `imported_not_produced = 0`
- `produced_not_imported = 18`

## Feature plan (make this obvious)

1) Add a short callout in `docs/README.md` pointing to this artifact.
2) Add a `self_repro` section to `docs/minimal_self_reproducing_set.md`.
3) Add a one-command script that:
   - runs the sequence
   - writes the report
   - prints a green/red status summary

## Refactor opportunities

1) **Deprecate BOM-only builds** and require explicit recipe/process production.
   - This aligns production accounting with `process_complete`.
2) **SimPlan generation** should prefer target recipes and avoid `build_machine`.
3) **Canonical machine-set file** in `docs/` (or `kb/`) with a stable name:
   - e.g. `docs/self_reproducing_set_latest.txt`
4) **One CLI command** to:
   - build the set
   - verify it
   - emit a report and summary diff
