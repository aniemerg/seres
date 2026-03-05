---
id: runbook_queue_definition
title: Runbook Queue Sequential - Definition
type: article
related_kb_entries:
  - runbook_queue_sequential
  - labor_bot_general_v0
---

`runbooks/runbook_queue_sequential.md` is a top-level orchestration runbook that chains many machine runbooks into a single simulation build.

## What It Does

1. Selects and resets one shared simulation ID (`runbook_queue_sequential`).
2. Executes a long list of `sim.runbook` calls, one per machine-focused runbook file.
3. Uses `continue-on-error: true` for each child runbook, so failures are recorded but do not stop the global queue.

## Why This Matters

- The result is a broad stress test over manufacturing pathways, not a tightly optimized mission sequence.
- You can inspect partial progress even when specific machine runbooks fail.
- It is useful for regression testing because one run surfaces many KB/model gaps at once.

## How It Appears in Simviewer

- In **Timeline**, each successful or failed process is shown as a process run event.
- Failed process runs remain visible and are color-coded by status in `status` color mode.
- In drawer details, recipe context helps distinguish intermediate steps from final outputs in each recipe run.

## Related

- `[[simulation_overview]]`
- `runbook_queue_sequential` scenario/runbook identifier
