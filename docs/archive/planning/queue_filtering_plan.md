# Queue Filtering Plan: Focus on BOMs, Recipes, and Parts

## Goal

Create a mode that filters the work queue to exclude gaps that require creating or updating processes and machines, focusing only on completing BOMs, recipes, and parts.

## Current Queue Analysis (1,063 items)

### Items by Kind
- **machine**: 371 (35%)
- **recipe**: 230 (22%)
- **part**: 149 (14%)
- **gap** (referenced_only): 114 (11%)
- **material**: 111 (10%)
- **resource_type**: 88 (8%)

### Gap Type Breakdown

**Items to EXCLUDE (require process/machine work):**
- `missing_field + machine (capabilities)`: 291 - Requires defining machine capabilities
- `no_provider_machine + resource_type`: 88 - Requires creating/updating machines to provide resources

**Items to KEEP (BOMs, recipes, parts):**
- `invalid_recipe_schema + recipe`: 168 - Fix recipe schemas ✓
- `no_recipe + part`: 149 - Create recipes for parts ✓
- `referenced_only + gap`: 114 - Mostly BOMs (e.g., `bom_*`) ✓
- `no_recipe + material`: 111 - Create recipes for materials ✓
- `import_stub + recipe`: 62 - Replace import recipes with real ones ✓
- `no_recipe + machine`: 59 - Create recipes for machines ✓
- `missing_field + machine (bom)`: 21 - Create BOMs for machines ✓

## Proposed Solution

### Option A: Filter Command (Recommended)

Add a `kbtool queue filter` command that creates a filtered version of the work queue:

```bash
# Create filtered queue excluding processes and machines
.venv/bin/python -m kbtool queue filter \
  --exclude-kinds process \
  --exclude-gap-types missing_field:machine:capabilities,no_provider_machine \
  --output out/work_queue_filtered.jsonl

# Agents can then use the filtered queue
python -m queue_agents.worker --queue-file out/work_queue_filtered.jsonl
```

**Pros:**
- No changes to indexer (keeps full queue for analysis)
- Flexible filtering via CLI flags
- Easy to switch between full and filtered queues
- Can create multiple filtered views

**Cons:**
- Requires passing `--queue-file` to agents

### Option B: Indexer Flag

Add a `--exclude-kinds` flag to the indexer:

```bash
# Index with exclusions
.venv/bin/python -m kbtool index --exclude-kinds process,machine:capabilities

# Queue is pre-filtered
python -m queue_agents.worker --agent worker-1
```

**Pros:**
- Agents work without modification
- Queue is always filtered

**Cons:**
- Loses full queue data
- Less flexible (need to re-index to change filters)
- Harder to analyze what's being excluded

### Option C: Agent-Level Filtering

Add `--priority` flag filtering to agents:

```bash
# Agents only lease specific gap types
python -m queue_agents.worker \
  --agent worker-1 \
  --include-gap-types no_recipe,import_stub,invalid_recipe_schema \
  --exclude-kinds process,machine
```

**Pros:**
- No queue modification needed
- Very flexible per-agent
- Can run mixed agent pools

**Cons:**
- Agents waste time skipping items
- Queue still shows all items (confusing counts)

## Recommended Implementation: Option A

### Implementation Steps

1. **Create `kbtool/queue_filter.py`**
   - Load work_queue.jsonl
   - Apply exclusion filters based on:
     - `gap_type` (e.g., exclude `no_provider_machine`)
     - `kind` (e.g., exclude `process`)
     - `gap_type + kind + field` combinations (e.g., exclude `missing_field + machine + capabilities`)
   - Save filtered queue to output file
   - Preserve lease/status metadata

2. **Add CLI command in `kbtool/__main__.py`**
   ```python
   filter_cmd = queue_sub.add_parser("filter", help="Filter work queue")
   filter_cmd.add_argument("--exclude-gap-types", help="Comma-separated gap types to exclude")
   filter_cmd.add_argument("--exclude-kinds", help="Comma-separated kinds to exclude")
   filter_cmd.add_argument("--exclude-combos", help="gap_type:kind:field combos to exclude")
   filter_cmd.add_argument("--output", default="out/work_queue_filtered.jsonl")
   ```

3. **Update `queue_agents/worker.py`**
   - Add `--queue-file` parameter (default: `out/work_queue.jsonl`)
   - Use specified queue file for lease operations

4. **Create preset filter configs**
   - `filters/boms_recipes_parts_only.json`:
     ```json
     {
       "name": "BOMs, Recipes, and Parts Only",
       "exclude": [
         {"gap_type": "missing_field", "kind": "machine", "field": "capabilities"},
         {"gap_type": "no_provider_machine"}
       ]
     }
     ```

### Usage Workflow

```bash
# 1. Run indexer (full queue)
.venv/bin/python -m kbtool index

# 2. Create filtered queue
.venv/bin/python -m kbtool queue filter \
  --config filters/boms_recipes_parts_only.json \
  --output out/work_queue_filtered.jsonl

# 3. Check filtered queue stats
.venv/bin/python -m kbtool queue ls --queue-file out/work_queue_filtered.jsonl

# 4. Run agents on filtered queue
python -m queue_agents.parallel_launcher \
  --workers 10 \
  --queue-file out/work_queue_filtered.jsonl
```

## Filter Specification: BOMs, Recipes, Parts Mode

### Items to Exclude

| Filter Rule | Count | Reason |
|-------------|-------|--------|
| `gap_type=missing_field AND kind=machine AND field=capabilities` | 291 | Requires defining machine capabilities (process/machine work) |
| `gap_type=no_provider_machine` | 88 | Requires creating or updating machines |

**Total excluded: 379 items (36%)**

### Items to Keep

| Gap Type | Kind | Count | Reason |
|----------|------|-------|--------|
| `invalid_recipe_schema` | recipe | 168 | Fix recipe schemas |
| `no_recipe` | part | 149 | Create recipes for parts |
| `referenced_only` | gap | 114 | Create missing items (mostly BOMs) |
| `no_recipe` | material | 111 | Create recipes for materials |
| `import_stub` | recipe | 62 | Replace import recipes |
| `no_recipe` | machine | 59 | Create recipes for machines |
| `missing_field (bom)` | machine | 21 | Create BOMs for machines |

**Total kept: 684 items (64%)**

## Expected Benefits

1. **Focused agent work**: Agents only work on BOMs, recipes, and parts
2. **No process/machine creation**: Prevents scope creep into process design
3. **Measurable progress**: 684 items → 0 completes the current phase
4. **Reversible**: Can always switch back to full queue
5. **Clear phase boundary**: After filtered queue is done, move to next phase

## Next Phase (After Filtered Queue Completed)

After the filtered queue is cleared (684 items done):

1. **Review state**: Check what's left in full queue
2. **Plan process/machine phase**: Decide which processes/machines to add
3. **Run full queue**: Or create another filtered view

## Alternative: Tag-Based Filtering

Instead of hardcoded filters, tag items in the KB with `phase` tags:

```yaml
# kb/items/machines/ball_mill_v0.yaml
id: ball_mill_v0
kind: machine
phase_tags:
  - phase_0_seed  # Imported in seed
  - phase_1_bom   # BOM needed
  - phase_2_recipe # Recipe needed
```

Then filter queue by phase. This is more flexible but requires more upfront work.

## Questions for User

1. **Which option do you prefer?** A (filter command), B (indexer flag), or C (agent filtering)?
2. **Should we implement preset configs** for common filter patterns?
3. **Do you want to exclude referenced_only gaps** that might be processes/machines? (Currently keeping them as most seem to be BOMs)
4. **Should we add phase tags** to KB items for more sophisticated filtering in the future?

## Implementation Estimate

- **Option A (Filter command)**: ~150 lines of code, 2-3 hours
- **Option B (Indexer flag)**: ~100 lines of code, 1-2 hours (simpler but less flexible)
- **Option C (Agent filtering)**: ~50 lines of code, 1 hour (least disruptive)

**Recommendation**: Implement Option A for maximum flexibility.
