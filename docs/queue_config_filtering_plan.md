# Queue Filtering via Configuration File

## Problem Statement

The indexer rebuilds `out/work_queue.jsonl` from scratch on every run. We need filtering to:
1. **Persist across indexer runs** - Config-driven, not command-line driven
2. **Be transparent to agents** - Agents just lease from the queue normally
3. **Be easily changeable** - Update config file to change filtering strategy
4. **Be auditable** - Track what's being filtered and why

## Proposed Solution: Configuration File

### Config File Location

**Option 1: Repo root (Recommended)**
```
.kbconfig.yaml  (or kbconfig.yaml)
```
- Standard location for project config
- Gitignored by default (can override with `kbconfig.example.yaml`)
- Easy to find and edit

**Option 2: Config directory**
```
config/queue_filters.yaml
```
- More organized (all config in one place)
- Committed to git (team shares same config)

**Recommendation: Use both**
- `config/queue_filters.yaml` - Default config (committed to git)
- `.kbconfig.yaml` - Optional override (gitignored, local customization)
- Indexer reads default, then overlays local override if present

### Config File Structure

```yaml
# config/queue_filters.yaml
version: 1
description: "Queue filtering configuration for KB indexer"

# Global toggle - set to false to disable all filtering
filtering_enabled: true

# Current phase/mode
current_mode: boms_recipes_parts_only

# Named filter modes (can switch between them)
modes:
  # Mode 1: No filtering (process everything)
  full_queue:
    description: "Process all gaps - no filtering"
    exclude: []

  # Mode 2: Focus on BOMs, recipes, and parts only
  boms_recipes_parts_only:
    description: "Exclude process/machine creation, focus on completing existing items"
    exclude:
      # Exclude machine capabilities (requires understanding machine function)
      - gap_type: missing_field
        kind: machine
        field: capabilities
        reason: "Requires defining machine capabilities (process design work)"

      # Exclude orphan resources (requires creating machines)
      - gap_type: no_provider_machine
        reason: "Requires creating or updating machines to provide resources"

    # Optional: explicitly include certain patterns (whitelist)
    include:
      - gap_type: missing_field
        kind: machine
        field: bom
        reason: "Creating BOMs is allowed"

  # Mode 3: Only recipes (no new items at all)
  recipes_only:
    description: "Only fix/create recipes, no new items"
    include:
      - gap_type: no_recipe
      - gap_type: import_stub
      - gap_type: invalid_recipe_schema

  # Mode 4: Referenced items from seeds only
  seed_references_only:
    description: "Only create items referenced by seed files"
    include:
      - gap_type: referenced_only
        context_has: seed_files  # Only if context.seed_files is present

# Exclusion by kind (simpler alternative to mode-based filtering)
# If set, these kinds are never added to queue regardless of gap_type
exclude_kinds: []  # e.g., ["process", "machine"]

# Exclusion by gap_type (global exclusions across all modes)
exclude_gap_types: []  # e.g., ["no_provider_machine"]

# Statistics tracking
track_filtered_stats: true  # Log filtered items to out/filtered_items.jsonl
```

### Config File Examples

**Example 1: Current request (BOMs/recipes/parts only)**
```yaml
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only

modes:
  boms_recipes_parts_only:
    description: "Exclude processes and machines, focus on BOMs/recipes/parts"
    exclude:
      - gap_type: missing_field
        kind: machine
        field: capabilities
      - gap_type: no_provider_machine

track_filtered_stats: true
```

**Example 2: Simple kind-based filtering**
```yaml
version: 1
filtering_enabled: true
exclude_kinds: ["process"]  # Never add processes to queue
exclude_gap_types: ["no_provider_machine"]  # Never add orphan resources
```

**Example 3: Recipes only**
```yaml
version: 1
filtering_enabled: true
current_mode: recipes_only

modes:
  recipes_only:
    include:
      - gap_type: no_recipe
      - gap_type: import_stub
      - gap_type: invalid_recipe_schema
```

## Implementation Plan

### Step 1: Create Config Module (`kbtool/config.py`)

```python
"""Configuration management for KB indexer."""
from pathlib import Path
from typing import Dict, List, Optional
import yaml

DEFAULT_CONFIG_PATH = Path("config/queue_filters.yaml")
LOCAL_CONFIG_PATH = Path(".kbconfig.yaml")

class QueueFilterConfig:
    def __init__(self):
        self.enabled = True
        self.current_mode = None
        self.modes = {}
        self.exclude_kinds = []
        self.exclude_gap_types = []
        self.track_stats = True

    @classmethod
    def load(cls) -> 'QueueFilterConfig':
        """Load config from default and local override files."""
        config = cls()

        # Load default config
        if DEFAULT_CONFIG_PATH.exists():
            config._merge_from_file(DEFAULT_CONFIG_PATH)

        # Overlay local config (takes precedence)
        if LOCAL_CONFIG_PATH.exists():
            config._merge_from_file(LOCAL_CONFIG_PATH)

        return config

    def _merge_from_file(self, path: Path):
        """Merge config from YAML file."""
        with path.open() as f:
            data = yaml.safe_load(f) or {}

        self.enabled = data.get('filtering_enabled', self.enabled)
        self.current_mode = data.get('current_mode', self.current_mode)
        if 'modes' in data:
            self.modes.update(data['modes'])
        self.exclude_kinds.extend(data.get('exclude_kinds', []))
        self.exclude_gap_types.extend(data.get('exclude_gap_types', []))
        self.track_stats = data.get('track_filtered_stats', self.track_stats)

    def should_exclude(self, gap_item: dict) -> tuple[bool, str]:
        """
        Check if a gap item should be excluded from the queue.
        Returns (should_exclude, reason).
        """
        if not self.enabled:
            return False, ""

        gap_type = gap_item.get('gap_type')
        kind = gap_item.get('kind')

        # Global kind exclusions
        if kind in self.exclude_kinds:
            return True, f"kind={kind} globally excluded"

        # Global gap_type exclusions
        if gap_type in self.exclude_gap_types:
            return True, f"gap_type={gap_type} globally excluded"

        # Mode-based filtering
        if self.current_mode and self.current_mode in self.modes:
            mode = self.modes[self.current_mode]

            # Check exclusions first
            for rule in mode.get('exclude', []):
                if self._matches_rule(gap_item, rule):
                    reason = rule.get('reason', 'matches exclusion rule')
                    return True, reason

            # Check inclusions (if present, acts as whitelist)
            includes = mode.get('include', [])
            if includes:
                for rule in includes:
                    if self._matches_rule(gap_item, rule):
                        return False, ""  # Explicitly included
                # If includes are defined but item doesn't match, exclude it
                return True, "not in include whitelist"

        return False, ""

    def _matches_rule(self, gap_item: dict, rule: dict) -> bool:
        """Check if a gap item matches a filter rule."""
        # Match gap_type
        if 'gap_type' in rule and gap_item.get('gap_type') != rule['gap_type']:
            return False

        # Match kind
        if 'kind' in rule and gap_item.get('kind') != rule['kind']:
            return False

        # Match field (for missing_field gaps)
        if 'field' in rule:
            context_field = gap_item.get('context', {}).get('field')
            if context_field != rule['field']:
                return False

        # Match context_has (check if context contains a key)
        if 'context_has' in rule:
            if rule['context_has'] not in gap_item.get('context', {}):
                return False

        return True
```

### Step 2: Modify Indexer (`kbtool/indexer.py`)

Update `_update_work_queue()` to apply filtering:

```python
def _update_work_queue(...) -> None:
    """Rebuild work queue with filtering applied."""
    from .config import QueueFilterConfig

    config = QueueFilterConfig.load()

    gap_items: List[dict] = []
    filtered_items: List[dict] = []  # Track what was filtered

    # ... (existing gap collection code) ...

    # Apply filtering before merging with existing queue
    if config.enabled:
        for gap in gap_items[:]:  # Copy to modify during iteration
            should_exclude, reason = config.should_exclude(gap)
            if should_exclude:
                gap_items.remove(gap)
                if config.track_stats:
                    filtered_items.append({
                        **gap,
                        'filtered_reason': reason,
                        'filtered_at': time.time()
                    })

    # ... (existing merge logic) ...

    # Write filtered items log
    if config.track_stats and filtered_items:
        with (OUT_DIR / "filtered_items.jsonl").open("w") as f:
            for item in filtered_items:
                f.write(json.dumps(item) + "\n")
```

### Step 3: Add CLI Commands

Add commands to manage config:

```bash
# Show current config
.venv/bin/python -m kbtool config show

# Switch modes
.venv/bin/python -m kbtool config set-mode boms_recipes_parts_only

# Disable filtering temporarily
.venv/bin/python -m kbtool config disable

# Enable filtering
.venv/bin/python -m kbtool config enable

# Validate config file
.venv/bin/python -m kbtool config validate
```

### Step 4: Update Validation Report

Add filtering stats to `out/validation_report.md`:

```markdown
## Queue Filtering

**Status**: Enabled
**Mode**: boms_recipes_parts_only
**Items filtered**: 379 (36% of total gaps)

### Filtered Breakdown
- missing_field + machine + capabilities: 291
- no_provider_machine: 88

See `out/filtered_items.jsonl` for details.
```

### Step 5: Create Default Config

Create `config/queue_filters.yaml` with sensible defaults:

```yaml
version: 1
filtering_enabled: false  # Disabled by default (opt-in)
current_mode: full_queue

modes:
  full_queue:
    description: "No filtering - process all gaps"
    exclude: []

track_filtered_stats: true
```

## Usage Workflow

### Switching to BOMs/Recipes/Parts Mode

```bash
# 1. Create config file
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: true
current_mode: boms_recipes_parts_only

modes:
  boms_recipes_parts_only:
    exclude:
      - gap_type: missing_field
        kind: machine
        field: capabilities
      - gap_type: no_provider_machine

track_filtered_stats: true
EOF

# 2. Run indexer (filtering applies automatically)
.venv/bin/python -m kbtool index

# 3. Check queue stats
.venv/bin/python -m kbtool queue ls

# 4. Check what was filtered
cat out/filtered_items.jsonl | jq -r .gap_type | sort | uniq -c

# 5. Run agents (no special flags needed!)
python -m queue_agents.parallel_launcher --workers 10
```

### Switching Back to Full Queue

```bash
# Edit config
cat > .kbconfig.yaml <<EOF
version: 1
filtering_enabled: false
EOF

# Re-run indexer
.venv/bin/python -m kbtool index
```

## Benefits

1. **Persistent**: Filtering survives indexer runs
2. **Transparent**: Agents don't need to know about filtering
3. **Auditable**: `out/filtered_items.jsonl` shows what was excluded
4. **Flexible**: Easy to switch modes by editing one file
5. **Versioned**: Config can be committed to git (team alignment)
6. **Overridable**: Local `.kbconfig.yaml` for personal experimentation
7. **Documented**: Config file is self-documenting with `reason` fields

## Questions

1. **Config file location**: Prefer `.kbconfig.yaml` (local, gitignored) or `config/queue_filters.yaml` (shared, committed)?
   - Or both (default + override)?

2. **Filtering granularity**: Is the proposed rule matching sufficient?
   - Match by: gap_type, kind, field, context_has
   - Need more sophisticated matching (regex, multiple values)?

3. **Mode vs simple exclusions**: Prefer named modes or just simple exclude lists?
   - Modes: More flexible, can switch between strategies
   - Simple: Easier to understand, less configuration

4. **Validation**: Should indexer fail if config is invalid, or just warn?

5. **Statistics**: Where should filtered items be logged?
   - `out/filtered_items.jsonl` (separate file)
   - `out/validation_report.md` (summary only)
   - Both?

6. **Override mechanism**: Should CLI flags override config file?
   ```bash
   # Temporarily disable filtering for one run
   .venv/bin/python -m kbtool index --no-filter
   ```

## Implementation Estimate

- **Config module** (`kbtool/config.py`): ~200 lines, 2 hours
- **Indexer integration**: ~100 lines, 1 hour
- **CLI commands**: ~150 lines, 1.5 hours
- **Default config file**: ~50 lines, 30 minutes
- **Documentation updates**: ~100 lines, 1 hour
- **Testing**: 1 hour

**Total: ~6 hours**

## Rollout Plan

1. **Phase 1**: Implement config system (filtering disabled by default)
2. **Phase 2**: Test with local `.kbconfig.yaml` override
3. **Phase 3**: Create shared `config/queue_filters.yaml` with default modes
4. **Phase 4**: Enable filtering for BOMs/recipes/parts mode
5. **Phase 5**: Monitor and adjust filters based on results

## Alternative: Simpler Approach

If the mode-based system is too complex, we could simplify to:

```yaml
# .kbconfig.yaml (simple version)
version: 1
filtering_enabled: true

# Just list what to exclude (no modes)
exclude:
  - gap_type: missing_field
    kind: machine
    field: capabilities
  - gap_type: no_provider_machine
```

This is simpler but less flexible (can't switch between predefined modes quickly).

---

## Recommendation

Implement the full solution with:
- Both `config/queue_filters.yaml` (default, committed) and `.kbconfig.yaml` (local override)
- Mode-based filtering (named strategies)
- Simple exclusion lists also supported (for quick filtering)
- Detailed logging to `out/filtered_items.jsonl`
- CLI commands to manage config

This gives maximum flexibility while keeping the common case (switching modes) simple.
