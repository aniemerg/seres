# Minimal Self-Reproducing Machine Set (Current)

This document describes the current **converged imported-machine set** after
iterative SimPlan optimization and provenance-based import extraction. It
represents the machine set that remains imported or required for the current KB
to self-reproduce its machine dependency graph.

**Canonical list:** `docs/self_reproducing_set.txt`

**Current canonical count:** 136 machine ids.

The canonical list is intentionally kept in one plain-text file so scripts,
documentation, and review diffs all use the same source of truth. Do not
duplicate the full list here; update `docs/self_reproducing_set.txt` and then
refresh any demo/report metrics that depend on it.

## Scope

This target list is **not** the full KB machine catalog. It is the current
self-reproduction target set: the machines the demo asks the simulator to
produce and compare against. The KB may contain many more machine entries,
including alternatives, versioned variants, research placeholders, deprecated
items, and machines that are not on the current self-reproduction path.

Use `docs/self_reproducing_set.txt` for the demo target count. Use the KB item
index or `kind: machine` queries when you need the full machine catalog count.

To verify the current count:

```bash
python - <<'PY'
from pathlib import Path

machines = [
    line.strip()
    for line in Path("docs/self_reproducing_set.txt").read_text().splitlines()
    if line.strip() and not line.strip().startswith("#")
]
print(len(machines))
PY
```

For the self-reproduction demo and validation steps, see:
- `docs/self_reproduction_demo.md`
