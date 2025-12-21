# Queue Filtering Implementation Summary

## What Was Implemented

Configuration-based queue filtering that persists across indexer runs. The indexer now reads a config file to determine which gaps should be excluded from the work queue.

## Files Created/Modified

### New Files
- `kbtool/config.py` - Config loading and filtering logic (150 lines)
- `config/queue_filters.yaml` - Default filter modes (committed to git)
- `.kbconfig.example.yaml` - Example local config
- `.gitignore` - Added `.kbconfig.yaml` (local overrides)
- `docs/queue_filtering_usage.md` - Complete usage guide
- `docs/queue_config_filtering_plan.md` - Design document

### Modified Files
- `kbtool/indexer.py` - Integrated filtering into `_update_work_queue()`
- `kbtool/__main__.py` - Added `config show` and `config modes` commands
- `out/validation_report.md` - Now shows filtering stats when enabled

## How It Works

1. **Indexer loads config** from `config/queue_filters.yaml` (default) and `.kbconfig.yaml` (local override)
2. **Applies filter rules** during work queue generation
3. **Filtered items never enter queue** - they're silently excluded
4. **Stats shown in validation report** when filtering is enabled
5. **Agents work normally** - they don't need to know about filtering

## Quick Start

### Enable BOMs/Recipes/Parts Mode

```bash
# Create local config file
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

# Run indexer (filtering happens automatically)
.venv/bin/python -m kbtool index

# Check results
.venv/bin/python -m kbtool config show
grep "Queue Filtering" out/validation_report.md -A 10

# Run agents (they work on filtered queue - 684 items instead of 1,063)
python -m queue_agents.parallel_launcher --workers 10
```

### Expected Results

**Before filtering** (full queue):
- Total gaps: 1,063
- Queue breakdown:
  - 291: `missing_field` (machine capabilities) ← EXCLUDED
  - 88: `no_provider_machine` ← EXCLUDED
  - 168: `invalid_recipe_schema` ✓
  - 149: `no_recipe` (parts) ✓
  - 114: `referenced_only` (mostly BOMs) ✓
  - 111: `no_recipe` (materials) ✓
  - 62: `import_stub` ✓
  - 59: `no_recipe` (machines) ✓
  - 21: `missing_field` (machine BOMs) ✓

**After filtering** (boms_recipes_parts_only mode):
- Total gaps found: 1,063
- Filtered out: 379 (36%)
- Added to queue: 684

The filtered queue focuses on:
- Creating recipes for existing items
- Fixing invalid recipes
- Creating BOMs for machines
- Creating parts and materials
- No process design work
- No new machine creation

## CLI Commands

```bash
# Show current configuration
.venv/bin/python -m kbtool config show

# List available modes
.venv/bin/python -m kbtool config modes

# Check queue status
.venv/bin/python -m kbtool queue ls
```

## Available Filter Modes

1. **`full_queue`** - No filtering (default)
2. **`boms_recipes_parts_only`** - Focus on completing existing items (excludes processes/machines)
3. **`recipes_only`** - Only create/fix recipes
4. **`seed_references_only`** - Only items referenced by seed files

## Configuration Structure

### Default Config (`config/queue_filters.yaml`)
```yaml
version: 1
filtering_enabled: false  # Disabled by default
current_mode: null

modes:
  boms_recipes_parts_only:
    exclude:
      - gap_type: missing_field
        kind: machine
        field: capabilities
      - gap_type: no_provider_machine
```

### Local Override (`.kbconfig.yaml`)
```yaml
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
```

Local config takes precedence over default config.

## Validation Report Example

When filtering is enabled, `out/validation_report.md` shows:

```markdown
## Queue Filtering

**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 1063
**Filtered out**: 379
**Added to queue**: 684
**Filtering rate**: 35.7%
```

## Workflow: Phased Development

```bash
# Phase 1: Complete BOMs and recipes
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

.venv/bin/python -m kbtool index
# Queue: 684 items (BOMs, recipes, parts)

python -m queue_agents.parallel_launcher --workers 20
# Work until queue empty

# Phase 2: Full queue (processes and machines)
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: false
EOF

.venv/bin/python -m kbtool index
# Queue: 1,063 items (full queue - filtered items return)

python -m queue_agents.parallel_launcher --workers 20
```

## Creating Custom Modes

Add to `config/queue_filters.yaml` or `.kbconfig.yaml`:

```yaml
modes:
  my_custom_mode:
    description: "Custom filtering strategy"
    exclude:
      - gap_type: missing_field
        kind: process
    include:
      - kind: material
```

## Key Design Decisions

1. **Config file location**: Both `config/queue_filters.yaml` (default, committed) and `.kbconfig.yaml` (local, gitignored)
2. **Named modes**: Switch strategies by changing `current_mode`
3. **No logging of filtered items**: They just don't get added (turn off filtering to see them again)
4. **No CLI override**: Just edit config file
5. **Transparent to agents**: Agents don't need modification

## Testing

```bash
# Test config loading
.venv/bin/python -m kbtool config show

# Test modes list
.venv/bin/python -m kbtool config modes

# Test indexer with filtering disabled (default)
.venv/bin/python -m kbtool index
wc -l out/work_queue.jsonl  # Should show 1063

# Test with filtering enabled
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

.venv/bin/python -m kbtool index
wc -l out/work_queue.jsonl  # Should show ~684

# Verify stats in validation report
grep "Queue Filtering" out/validation_report.md -A 10
```

## Next Steps

1. **Try it out**: Enable `boms_recipes_parts_only` mode and run indexer
2. **Review filtered queue**: Check what gaps remain
3. **Run agents**: Process the filtered queue (684 items)
4. **Iterate**: Adjust filter rules based on results
5. **Create custom modes**: Define filters for your specific workflow

## Documentation

- **Usage guide**: `docs/queue_filtering_usage.md` - Complete user guide
- **Design doc**: `docs/queue_config_filtering_plan.md` - Full design rationale
- **Example config**: `.kbconfig.example.yaml` - Copy to `.kbconfig.yaml` to use

## Summary

You can now control what goes into the work queue by:
1. Creating a `.kbconfig.yaml` file
2. Setting `filtering_enabled: true`
3. Choosing a `current_mode`
4. Running the indexer

The filtering persists across indexer runs and is completely transparent to agents. Turn off filtering by setting `filtering_enabled: false` and all previously filtered items will return to the queue.
