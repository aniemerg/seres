# Self-Replicating System Modeling (v0)

Minimal setup to run the KB indexer and iterate on YAML data.

## ⚠️ REQUIRED READING BEFORE WORKING ON QUEUE

**Before working on the work queue, you MUST read these documents:**
1. `docs/project_overview.md` — Project overview and high-level goals
2. `docs/kb_schema_reference.md` — Current schema reference (ADR-012+)
3. `docs/knowledge_acquisition_protocol.md` — Knowledge acquisition workflow
4. `docs/parts_and_labor_guidelines.md` — Parts, BOMs, and labor modeling policy
5. **`docs/conservative_mode_guide.md` — Queue work philosophy (Conservative Mode)**

See `docs/README.md` for complete onboarding documentation.

## Conservative Mode: Default Approach for Queue Work

**Core Principle:** Treat queue items as potential symptoms, not direct fix requests.

Before creating any new item:
- **Check if it already exists** under a different name (search variations)
- **Check for equivalents** within 5× magnitude (same function, compatible materials)
- **Consider adaptations** of existing items (phase changes, recipe modifications)
- **Evaluate labor bot + tools** instead of special-purpose machines
- **Verify the reference** isn't erroneous or based on outdated assumptions

**See `docs/conservative_mode_guide.md` for complete decision trees and examples.**

Quick examples:
- ❌ Don't create `water_vapor_v0` → ✅ Use `water` + add boiling step to recipe
- ❌ Don't create `hose_crimping_station_v0` → ✅ Use `labor_bot_general_v0` + `crimping_tool_manual`
- ❌ Don't create `steel_plate_large` if `steel_plate` exists within 5× size → ✅ Reuse existing, note variation

## Quick start
- Install deps with uv: `uv sync` (creates `.venv`).
- **KB Core Tools** (new unified CLI):
  - Run indexer: `python -m src.cli index`
    - Outputs: `out/index.json`, `out/validation_report.md`, `out/work_queue.jsonl`, etc.
  - Validate specific item: `python -m src.cli validate --id process:regolith_mining_highlands_v0`
    - (Find process IDs: `ls kb/processes/` or `grep "^id:" kb/processes/*.yaml`)
  - Auto-fix validation issues: `python -m src.cli auto-fix --dry-run`
  - Analyze material closure: `python -m src.cli closure --machine <machine_id>` or `--all`
- Queue helpers (legacy kbtool):
  - Lease next item: `.venv/bin/python -m kbtool queue lease --agent <name> [--ttl 900]`
  - Complete/release: `queue complete|release --id <gap_type:item_id> --agent <name> [--verify]`
  - GC expired leases: `queue gc`
  - Prune explicit resolved/superseded: `queue prune`
  - List counts: `queue ls`
- Autonomous agents:
  - Run single agent: `python -m queue_agents.worker --agent <name>`
  - Run parallel agents: `python -m queue_agents.launcher --workers <n>`
  - Run with live dashboard: `python -m queue_agents.parallel_launcher --workers <n>`
  - See `queue_agents/README.md` for details
- See `docs/` for onboarding and workflow details.
  - When fixing a queue item, also fix any other validation issues in that same file, then run `python -m src.cli validate --id <type:id>` before completing the queue item.

## Simulation

### Base Builder Simulation (Current)

**Status**: ✅ **IMPLEMENTED AND VALIDATED** (2025-12-20)

Interactive simulation mode for validating KB completeness by building a lunar base from scratch:

⚠️ **Note**: New simulation engine with ADR-012/014 support is implemented (`src/simulation/engine.py`) but CLI interface (Phase 3.3) is not yet complete. Continue using base_builder CLI below for now.

**Key Features**:
- Start with nothing, bootstrap from regolith mining
- Material class matching enables generic substitution (e.g., iron → raw_metal_block)
- JSONL event logging for full audit trail
- Interactive mode: Direct function calls from Claude

**Proven Results**:
- ✅ Complete iron production chain: regolith → iron ore → pure iron → parts
- ✅ 425 kg regolith → 25 kg manufactured parts (2% yield)
- ✅ 315 kg Earth imports (bootstrap only), 12.6:1 local-to-import ratio
- ✅ Material class system unlocked 66+ manufacturing processes

**Usage**:

⭐ **Recommended: CLI Commands (for Claude Code and manual control)**
```bash
# Complete guide in docs/CLI_COMMANDS_GUIDE.md
# Quick reference in CLI_QUICK_REFERENCE.md

SIM="my_sim"

# View state
python -m base_builder.cli_commands view-state --sim-id $SIM

# Import bootstrap
python -m base_builder.cli_commands import --sim-id $SIM --item labor_bot_general_v0 --quantity 1 --unit unit

# Start process
python -m base_builder.cli_commands start-process --sim-id $SIM --process regolith_mining_highlands_v0 --duration 8

# Preview & execute
python -m base_builder.cli_commands preview --sim-id $SIM --hours 8
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 8
```

**Alternative: Python API (for custom scripts only)**
```bash
# ⚠️ NOT recommended for Claude Code - use CLI commands above instead
python -c "from base_builder.interactive import *; init_simulation('test_sim')"
# Then use: view_state(), start_process(), run_recipe(), build_machine(), etc.
```

**Documentation**:
- **`docs/CLI_COMMANDS_GUIDE.md`** — **⭐ Complete CLI reference (USE THIS IN CLAUDE CODE)**
- **`CLI_QUICK_REFERENCE.md`** — **Quick reference card**
- `base_builder/README.md` — Overview and architecture
- `base_builder/INTERACTIVE_MODE.md` — Python API guide (not for Claude Code)
- `docs/ADRs/004-base-builder-simulation.md` — Architecture decision record
- `docs/material_class_system.md` — Material class matching implementation
- `docs/iron_parts_discovery.md` — Production chain breakthrough
- `docs/session_accomplishments.md` — Complete session results

## Repo layout (current)
- `design/` — memos, notes, reference papers.
- `kb/` — YAML knowledge base (processes, items, resources, recipes, BOMs, scenarios).
- `kbtool/` — Python tooling (models + indexer CLI).
- `queue_agents/` — Autonomous queue agents for processing KB gaps.
- `base_builder/` — **Base builder simulation** for validating KB completeness through production chains.
- `simulations/` — Simulation runs and event logs.
- `docs/` — Documentation, ADRs, research questions, session accomplishments.
- `out/` — generated index, reports, work queue.

## Indexer outputs
| File | Description |
|------|-------------|
| `index.json` | Full dependency graph of all KB entries |
| `validation_report.md` | Comprehensive gap summary + warnings |
| `work_queue.jsonl` | All gaps needing attention (rebuilt each run) |
| `null_values.jsonl` | Fields with null data (qty, amount, mass) |
| `missing_recipes.jsonl` | Items (parts/materials) without recipes |
| `missing_fields.jsonl` | Required fields not populated (energy_model, time_model, material_class) |
| `orphan_resources.jsonl` | Resource types with no machine providing them |
| `unresolved_refs.jsonl` | Free-text `requires_text` entries needing resolution |
| `import_stubs.jsonl` | Recipes marked as imports (empty steps) |

## Work queue behavior
The work queue is **rebuilt from scratch** on each indexer run, reflecting all current gaps:
- `no_recipe` — parts/materials without manufacturing recipes (will be imports)
- `missing_field` — required fields not populated (energy_model, time_model, material_class)
- `no_provider_machine` — resource_types with no machine capability
- `referenced_only` — IDs referenced but not defined
- `unresolved_ref` — free-text requirements needing definition
- `import_stub` — machines/items with import recipes needing local manufacturing

When you fix a gap, the next indexer run automatically removes it from the queue.

## Current state (as of last index)
- **1531 validation issues** from ADR-012/014/017 implementation
  - 622 processes missing `process_type` (continuous vs batch)
  - 525 processes missing required fields (`scaling_basis`, `unit`, etc.)
  - 244 processes using old energy model format (`kWh_per_kg` → needs migration to `per_unit`)
  - 138 deprecated fields (`rate_kg_per_hr`, `hr_per_kg`, `fixed_time`)
- 1582 total gaps in work queue (validation errors + missing recipes/fields)

See `out/validation_report.md` and `out/validation_issues.jsonl` for details.

## Schema Migration Status

**⚠️ KB Schema Update In Progress**: Transitioning to ADR-012/014 process and energy models.

**New schemas** (see `docs/README.md` for details):
- **ADR-012**: Process types (`continuous`/`batch`) and new time_model with `scaling_basis`
- **ADR-014**: New energy_model with compound units (`kWh/kg`) and `scaling_basis`
- **ADR-016**: Implicit unit conversion system
- **ADR-017**: Comprehensive validation and error detection

**Documentation**:
- `docs/README.md` — **Complete schema reference** with examples (⭐ READ THIS FIRST)
- `docs/ADRs/` — Architecture decision records with full specifications
- `out/validation_report.md` — Current validation status

## Next steps
1. **Migrate processes to ADR-012/014 schemas** (see `docs/README.md` for new format)
   - Add `process_type: continuous` or `batch` to all processes
   - Update `time_model` to use `rate`/`rate_unit`/`scaling_basis` (not `rate_kg_per_hr`)
   - Update `energy_model` to use `type: per_unit`/`fixed_per_batch` with `unit` and `scaling_basis`
2. Add recipes for materials (most are outputs of processes, need to link them)
3. Add `material_class` to parts (e.g., steel, ceramic, glass)
4. Create machines for orphan resource_types (or mark as consumables)
5. Fill in null qty/amount values in processes

**For migration help**: See "Energy and Time Models" section in `docs/README.md`
