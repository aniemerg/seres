# Queue Filtering Usage Guide

## Overview

The indexer now supports configuration-based queue filtering. This allows you to control which gaps are added to the work queue during indexing, enabling phased development (e.g., "focus on BOMs and recipes first, then tackle processes and machines later").

## Quick Start

### Enable BOMs/Recipes/Parts Mode

```bash
# 1. Create local config file (gitignored)
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

# 2. Run indexer (filtering applies automatically)
python -m src.cli index

# 3. Check what was filtered
grep "Queue Filtering" out/validation_report.md -A 10

# 4. Run agents (they work on the filtered queue)
python -m queue_agents.parallel_launcher --workers 10
```

### Check Current Configuration

```bash
# Show current config
.venv/bin/python -m kbtool config show

# List available modes
.venv/bin/python -m kbtool config modes
```

## Configuration Files

### Default Config: `config/queue_filters.yaml`

This file is committed to git and provides default filter modes for the team.

**Default state**: Filtering disabled (`filtering_enabled: false`)

### Local Override: `.kbconfig.yaml`

This file is **gitignored** and allows personal/local filtering preferences.

**Priority**: Local config overrides default config.

### Example Workflow

```bash
# Copy example to start
cp .kbconfig.example.yaml .kbconfig.yaml

# Edit to enable filtering
vim .kbconfig.yaml
# Change: filtering_enabled: true
# Change: current_mode: boms_recipes_parts_only

# Run indexer
python -m src.cli index
```

## Available Modes

### `full_queue` (default)

No filtering - all gaps added to queue.

```yaml
current_mode: full_queue
```

### `boms_recipes_parts_only`

Focus on completing existing items. Excludes:
- Machine capabilities (requires process design work)
- Orphan resources (requires creating machines)

**Typical reduction**: ~36% of gaps filtered (379 of 1,063 items)

**Use case**: "Let's finish BOMs and recipes for existing items before designing new processes/machines"

```yaml
current_mode: boms_recipes_parts_only
```

### `recipes_only`

Only create/fix recipes. Excludes everything except:
- Items without recipes (`no_recipe`)
- Import stubs needing replacement (`import_stub`)
- Invalid recipe schemas (`invalid_recipe_schema`)

**Use case**: "Just create manufacturing recipes, no new items"

```yaml
current_mode: recipes_only
```

### `seed_references_only`

Only create items referenced by seed files. Useful for focused work on specific requirements.

**Use case**: "Only work on items needed by my current seed analysis"

```yaml
current_mode: seed_references_only
```

## Filter Rules

Filters use pattern matching on gap items:

```yaml
exclude:
  - gap_type: missing_field
    kind: machine
    field: capabilities
    reason: "Requires process design work"

  - gap_type: no_provider_machine
    reason: "Requires creating machines"
```

### Available Match Criteria

- `gap_type`: e.g., `missing_field`, `no_recipe`, `referenced_only`
- `kind`: e.g., `machine`, `part`, `material`, `process`
- `field`: For `missing_field` gaps, which field is missing
- `context_has`: Check if gap context contains a key (e.g., `seed_files`)

### Exclude vs Include

**Exclude rules**: Blacklist - items matching are filtered out

**Include rules**: Whitelist - ONLY items matching are kept (all others filtered)

```yaml
# Blacklist approach (exclude specific patterns)
exclude:
  - gap_type: missing_field
    kind: machine

# Whitelist approach (only allow specific patterns)
include:
  - gap_type: no_recipe
  - gap_type: import_stub
```

## Checking Filter Results

### Validation Report

After running the indexer, check `out/validation_report.md`:

```markdown
## Queue Filtering

**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Total gaps found**: 1063
**Filtered out**: 379
**Added to queue**: 684
**Filtering rate**: 35.7%
```

### Queue Stats

```bash
# Check queue counts
python -m src.cli queue ls

# Output:
{
  "pending": 684  # Down from 1063 with filtering
}
```

### Gap Type Breakdown

```bash
# See what's in the filtered queue
python -c "
import json
from collections import Counter
items = [json.loads(line) for line in open('out/work_queue.jsonl')]
for gap_type, count in Counter(i['gap_type'] for i in items).most_common():
    print(f'{gap_type}: {count}')
"
```

## Switching Modes

### During Development

```bash
# Start with BOMs/recipes/parts
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

python -m src.cli index
python -m queue_agents.parallel_launcher --workers 10

# ... work until queue empty ...

# Switch to full queue for next phase
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: false
EOF

python -m src.cli index
```

### Disable Filtering Temporarily

```bash
# Just comment out or set to false
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: false  # Temporarily disabled
# current_mode: boms_recipes_parts_only
EOF

python -m src.cli index
```

## Creating Custom Modes

Add new modes to `config/queue_filters.yaml` or `.kbconfig.yaml`:

```yaml
modes:
  my_custom_mode:
    description: "Only work on materials"
    include:
      - kind: material

  high_priority_only:
    description: "Only items from seed files"
    include:
      - gap_type: referenced_only
        context_has: seed_files
```

Then activate:

```yaml
current_mode: my_custom_mode
```

## Simple Global Exclusions

For simple filtering, skip modes and use global exclusions:

```yaml
version: 1
filtering_enabled: true

# Simple approach - no modes
exclude_kinds: ["process"]  # Never add processes
exclude_gap_types: ["no_provider_machine"]  # Never add orphan resources
```

## Workflow Example: Phased Development

```bash
# Phase 1: Complete BOMs and recipes (684 items)
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

python -m src.cli index
# Queue: 684 items (BOMs, recipes, parts)

python -m queue_agents.parallel_launcher --workers 20
# ... agents work until queue empty ...

# Phase 2: Add missing machines (full queue)
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: false
EOF

python -m src.cli index
# Queue: ~379 items (previously filtered items return)

python -m queue_agents.parallel_launcher --workers 20
# ... agents work on machines and processes ...
```

## Troubleshooting

### "Filtering not working"

- Check config file exists: `ls -la .kbconfig.yaml config/queue_filters.yaml`
- Verify syntax: `cat .kbconfig.yaml`
- Check mode name matches: `.venv/bin/python -m kbtool config modes`
- Confirm filtering enabled: `.venv/bin/python -m kbtool config show`

### "Want to see what was filtered"

Currently filtered items are silently excluded. To see what would be filtered, compare queue counts before/after:

```bash
# Disable filtering
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: false
EOF

python -m src.cli index
wc -l out/work_queue.jsonl  # Note the count

# Enable filtering
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only
EOF

python -m src.cli index
wc -l out/work_queue.jsonl  # Compare the count
```

### "Filtered items returned after re-indexing"

This is expected! Filtering only affects which items are added to the queue. When you disable filtering, previously excluded gaps will reappear.

## Best Practices

1. **Start focused**: Enable filtering to tackle high-value work first
2. **Commit default config**: Share standard modes with team via `config/queue_filters.yaml`
3. **Local experimentation**: Use `.kbconfig.yaml` (gitignored) for personal filtering
4. **Check validation report**: Always review filter stats after indexing
5. **Disable for analysis**: Periodically run with filtering disabled to see full picture
6. **Document custom modes**: Add clear descriptions to help others understand your filters
