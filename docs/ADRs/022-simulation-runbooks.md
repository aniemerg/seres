# ADR 022 — Simulation Runbooks (Markdown + YAML Cells)

**Status:** Proposed
**Date:** 2026-01-11
**Decision Makers:** Project team
**Related ADRs:** ADR-004 (Base Builder Simulation), ADR-020 (Recipe Orchestration and Scheduling), ADR-021 (Simulation State Persistence)

---

## Context

Simulation work often requires a linear, human-readable sequence of CLI steps (init, import, run recipe, advance time, inspect state). Today this is done manually in terminals or via ad-hoc notes. The project needs a structured runbook that:

- Is readable and editable by humans.
- Executes only through the simulation CLI (no internal shortcuts).
- Can be replayed to reproduce a simulation run.
- Supports common workflows like “set sim name” and “restart sim”.

This is distinct from `sim plan` (which attempts to infer production plans). Runbooks are explicit, user-authored steps that the CLI executes verbatim.

## Decision

Introduce **Markdown runbooks** with **YAML command cells**. A new CLI command will read these runbooks and execute the listed simulation commands in order.

Key constraints:
- Only simulation CLI commands are allowed.
- Command names mirror CLI subcommands.
- No variable substitution or templating (for now).

## Goals

- Provide a notebook-like runbook format with freeform text and executable cells.
- Execute runbooks entirely via the CLI (same validations, same side effects).
- Support “set default sim id” and “reset sim” within the runbook.

## Non-Goals (for now)

- Generating runbooks from existing simulations.
- Variables, templates, or branching logic.
- Non-simulation commands (queue/indexer/etc.).

## Runbook Format

Runbook files are Markdown. Executable content appears only in fenced code blocks
with info string `sim-runbook`.

Runbooks live under `runbooks/` at repo root (Markdown files, e.g., `runbooks/lunar_base_demo.md`).

Each `sim-runbook` block is YAML containing a list of commands:

```yaml
- cmd: sim.init
  args:
    sim-id: demo
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
```

Notes:
- `cmd` mirrors the CLI subcommand name (e.g., `sim.start-process`).
- `args` mirrors CLI flags without `--` (e.g., `sim-id`).
- All non-`sim-runbook` content is ignored by the runner.

## Available Commands (Current CLI)

These commands are currently exposed by the simulation CLI (`src/simulation/cli.py`):

- `sim.init`
- `sim.scaffold`
- `sim.import`
- `sim.start-process`
- `sim.run-recipe`
- `sim.build-machine`
- `sim.advance-time`
- `sim.preview`
- `sim.view-state`
- `sim.status`
- `sim.list`
- `sim.plan`
- `sim.visualize`

**References:** `docs/CLI_COMMANDS_GUIDE.md`, `docs/SIMULATION_GUIDE.md`, `src/simulation/cli.py`.

## New Commands (Proposed)

These are required to support the runbook workflow but are not implemented yet:

- `sim.use` — set a default `sim-id` for subsequent commands in the runbook.
  - Example: `sim.use --sim-id demo`
  - Behavior: runner stores `sim-id` and injects it into commands that omit it.
  - CLI parity: a new `sim use` command should be added for consistency.

- `sim.reset` — restart a simulation by removing existing state and re-initializing.
  - Example: `sim.reset --sim-id demo`
  - Behavior: delete `simulations/<sim-id>` and re-run `sim init`.
  - CLI parity: a new `sim reset` command should be added.

These are CLI-accessible actions; the runbook runner must only invoke CLI behaviors.

## Execution Semantics

Proposed CLI entry point:

```
python -m src.cli sim runbook --file <path>
```

Runner behavior:
- Parse Markdown, execute each `sim-runbook` block in order.
- Execute commands sequentially, stopping on the first error (default).
- `--continue-on-error` is optional for best-effort runs.
- Each command is executed via the same handlers as the CLI.
- The simulation engine loads/saves state per command (no special shortcuts).

## Example Runbook

```markdown
# Lunar Base Demo

This runbook bootstraps a minimal simulation and runs a short process.

```sim-runbook
- cmd: sim.use
  args:
    sim-id: demo
- cmd: sim.reset
  args:
    sim-id: demo
- cmd: sim.import
  args:
    item: labor_bot_general_v0
    quantity: 2
    unit: unit
- cmd: sim.start-process
  args:
    process: regolith_mining_highlands_v0
    duration: 24
- cmd: sim.advance-time
  args:
    hours: 24
- cmd: sim.status
  args: {}
```
```

## Risks and Mitigations

- **Command drift:** CLI changes could break runbooks.
  - Mitigation: document available commands in the runbook spec and keep
    `docs/CLI_COMMANDS_GUIDE.md` up to date.
- **Partial runs:** errors mid-run can leave a sim in a partial state.
  - Mitigation: recommend `sim.reset` at the top of a runbook for clean runs.

## Follow-ups

1) Implement `sim runbook` parser and executor.
2) Add `sim use` and `sim reset` to `src/simulation/cli.py`.
3) Document the runbook format in `docs/SIMULATION_GUIDE.md`.
4) (Future) Add “export runbook” from simulation logs.
