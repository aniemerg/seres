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

## Scale snapshot

This demo shows a **self‑reproduction chain** at scale: the simulation
**produced 135 machines**, executed **2,787 processes**, and accumulated
**~908,136 machine‑hours** of simulated work, consuming
**~3.53 million kWh** of energy. These metrics reflect the depth and
complexity of the modeled production system, while keeping the focus on
what the demo actually proves—machine self‑reproduction under the current
model assumptions.

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

## Produced‑machine ISRU (mass‑weighted)

From the current self‑reproduction demo run:

- Produced machines with provenance: 135
- In‑situ mass: 25,318.14 kg
- Imported mass: 437,038.42 kg
- Unknown mass: 0.0 kg
- Produced‑machines ISRU (mass‑weighted): 5.48%

So by mass, the produced machines are still dominated by imported material, even
though the overall inventory can be much more ISRU‑heavy. This is expected until
electronics and precision components have local manufacturing paths.

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
