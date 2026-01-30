# Self‑Reproduction Demo

This demo shows SERES reaching a **self‑reproducing machine set**: the machines
we request are the machines the simulation produces. It’s a milestone for the
model’s internal closure, not a claim of real‑world feasibility.

## What “self‑reproduction” means here

- **Requested**: the target machine list we ask the simulator to build.
- **Produced**: machines created by process outputs or BOM builds.
- **Imported**: machines pulled in as dependencies.

The demo is successful when:
- **Requested == Produced**
- **Imports ⊆ Produced** (imports are not outside the produced set)

## One‑command run

```bash
.venv/bin/python scripts/analysis/run_self_reproduction_demo.py --reset
```

Default output folder:
```
out/self_repro_demo/
```

## What you’ll get

- `summary.md` — status and counts
- `requested_machines.txt` — canonical target list
- `produced_machines.txt` — what the sim built (process + build)
- `imported_machines.txt` — what the sim imported
- `requested_not_produced.txt` — should be empty at this milestone
- `imported_not_produced.txt` — should be empty at this milestone

## Assumptions & limitations

- Imports are a boundary condition: anything not locally manufacturable is
  imported to keep gaps visible.
- BOM assembly (build events) is still used in some places; it is tracked as
  production for the demo.
- Numbers are coarse; structure and closure are the point.

## The canonical machine list

The demo uses:
```
docs/self_reproducing_set.txt
```

This is the current canonical target list for the self‑reproduction demo.

## How to validate

After running the demo:
```bash
cat out/self_repro_demo/summary.md
```

Expected:
- Requested == Produced
- Imported ⊆ Produced

If you want deeper inspection, compare the text files in the output folder.
