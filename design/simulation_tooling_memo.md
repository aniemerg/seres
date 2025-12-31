# Simulation Tooling Memo (Agent UX)

Goal: reduce manual file spelunking and speed up useful simulations by adding CLI helpers under `src.cli` that surface dependencies, ISRU feasibility, and runtime blockers.

## Observed Pain Points

1. Manual dependency mapping
   - To run a single recipe/process, I had to inspect multiple YAML files for inputs, required machines, and upstream processes.
   - This is slow and error-prone, especially for BOM-heavy machines or multi-step recipes.

2. Missing or hidden runtime requirements
   - `resource_requirements` and `requires_ids` are not summarized before execution.
   - I often discover missing machines only after a simulation fails.

3. ISRU feasibility is opaque
   - Determining what can be produced locally vs. must be imported requires manual KB traversal.
   - There is no quick "what must I import" or "what can be built locally" summary.

4. Recipe/process overrides and calculated duration are hard to reason about
   - It is not obvious whether a process duration will calculate correctly, or if a recipe step override is partial vs. complete.

5. Simulation setup is repetitive
   - Repeatedly creating sims, importing bootstrap machines, and staging materials is boilerplate.

## Conventions and Schemas to Respect

These are the relevant rules that tooling should follow and surface:

- Process schema and time/energy models are defined by ADR-012/014/016/017 in `docs/kb_schema_reference.md`.
- Processes must declare `process_type` and valid `time_model`/`energy_model`.
- Recipes can partially override time/energy models; if `type` is present, the override is complete.
- Machines and process requirements must be expressed via `resource_requirements` and `requires_ids`.
- Units use compound syntax like `kg/hr` and `kWh/kg`.
- Simulation naming guidance and best practices live in `docs/simulation_best_practices.md`.

Tooling should not invent new schemas; it should read and report from current KB and ADR rules.

## Proposed CLI Additions (Agent UX)

All commands should live under `python -m src.cli sim ...` unless noted.

### 1) `sim plan`
**Purpose:** Preflight a process or recipe and show all dependencies.

Example:
```
python -m src.cli sim plan --process crushing_basic_v0
python -m src.cli sim plan --recipe recipe_labor_bot_basic_v0
```

Output:
- Required machines/resources (flattened list)
- Required input items and quantities (per batch or scaled)
- Output items and quantities
- Duration/energy calculation readiness (OK/ERROR + reason)
- Suggested imports (items not producible from local KB graph)

### 2) `sim deps`
**Purpose:** Expand dependency tree of an item/recipe/process.

Example:
```
python -m src.cli sim deps --item labor_bot_basic_v0 --depth 2
```

Output:
- Tree of recipes/processes required
- Highlight nodes with missing recipes
- Flag ambiguous or missing conversions

### 3) `sim isru`
**Purpose:** Quick ISRU feasibility summary for a target item or machine.

Example:
```
python -m src.cli sim isru --item labor_bot_basic_v0
```

Output:
- Percent ISRU vs. import (by mass)
- List of import-only items
- Minimal import set

### 4) `sim check`
**Purpose:** Dry-run validation of a process/recipe without executing it.

Example:
```
python -m src.cli sim check --process motor_final_assembly_v0
python -m src.cli sim check --recipe recipe_motor_electric_small_v0
```

Output:
- All validation errors/warnings (ADR-017)
- Missing machines and inputs
- Whether duration/energy can be calculated

### 5) `sim scaffold`
**Purpose:** Create a simulation with sensible defaults and optional bootstraps.

Example:
```
python -m src.cli sim scaffold --sim-id labor_bot_basic_isru --bootstrap labor_bot_general_v0,assembly_tools_basic
```

Output:
- New simulation
- Imported bootstrap items
- Optional metadata note in simulation event log

### 6) `sim import-plan`
**Purpose:** Generate and apply a minimal import plan.

Example:
```
python -m src.cli sim import-plan --sim-id labor_bot_basic_isru --item labor_bot_basic_v0 --apply
```

Output:
- List of items to import and quantities
- Optional `--apply` to import directly

### 7) `sim runchain`
**Purpose:** Execute a small chain of processes with consistent durations and reporting.

Example:
```
python -m src.cli sim runchain --sim-id labor_bot_basic_isru --processes regolith_mining_simple_v0,ilmenite_extraction_from_regolith_v0,iron_pure_production_from_ilmenite_v0
```

Output:
- Process list
- Duration/energy summary
- Inventory changes

### 8) `sim diagnose`
**Purpose:** One-shot diagnosis when a sim command fails.

Example:
```
python -m src.cli sim diagnose --last --sim-id labor_bot_basic_isru
```

Output:
- Last error and stack trace summary
- Likely missing inputs/machines
- Suggested fixes

## Optional: CLI Output Improvements

- Add `--explain` to `sim start-process` to show how duration and energy were calculated.
- Add `--list-requires` to `sim start-process` to print required machines and resources.

## Why These Help Agent UX

These commands remove the need for manual `rg` + `cat` across KB directories to answer basic questions:
- What do I need to run this process/recipe?
- Can I make it locally, and if not, what should I import?
- Why did the simulation fail?

They also align with existing documentation and ADRs, and avoid new schema changes.

## Implementation Notes

- Use existing KB loaders and validators (ADR-017) to avoid duplicating validation logic.
- Where possible, reuse closure analysis logic for ISRU reporting.
- Keep outputs compact and consistent with current CLI style.

## Next Steps

1. Agree on the minimal set of commands to implement first (`sim plan`, `sim check`, `sim import-plan`).
2. Decide output formats (stdout tables vs. JSON for scripting).
3. Add small integration tests for each command.
