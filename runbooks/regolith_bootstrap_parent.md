# Regolith Bootstrap (Parent)

This runbook delegates to the existing regolith bootstrap runbook.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: regolith_bootstrap_v0
- cmd: sim.reset
  args:
    sim-id: regolith_bootstrap_v0
- cmd: sim.runbook
  args:
    file: regolith_bootstrap_runbook.md
- cmd: sim.status
  args: {}
```
