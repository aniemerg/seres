# Reports Generation Guide

## Generating Inventory Reports

The inventory report provides a comprehensive listing of all items in the knowledge base, organized by type (machines, parts, materials, processes, etc.).

### Command

```bash
.venv/bin/python -m kbtool report inventory
```

### Output

- **File location:** `out/reports/inventory.md`
- **Format:** Markdown with summary statistics and categorized item lists
- **Contents:**
  - Summary statistics (total counts by item type)
  - Complete listings organized by:
    - BOMs
    - Machines
    - Materials
    - Parts
    - Processes
    - Recipes
    - Resources
    - And other KB entity types

### When to Generate

- **After major KB updates:** When adding many new machines, parts, or processes
- **Before dedupe reviews:** To get a fresh view of all items for consolidation analysis
- **For quality audits:** To review naming consistency and identify gaps
- **After running the indexer:** Reports use the index, so run `python -m src.cli index` first

### Using Reports for Dedupe Analysis

The inventory report is essential for identifying consolidation opportunities:

1. **Generate fresh inventory:**
   ```bash
   python -m src.cli index
   .venv/bin/python -m kbtool report inventory
   ```

2. **Search for patterns:**
   ```bash
   # Look for similar furnaces/ovens
   grep -i "furnace\|kiln\|oven" out/reports/inventory.md

   # Look for similar mills/grinders
   grep -i "mill\|grind\|crush" out/reports/inventory.md

   # Look for similar pumps
   grep -i "pump" out/reports/inventory.md
   ```

3. **Identify candidates:**
   - Multiple items with similar names (e.g., `furnace_basic` + `furnace_high_temp` + `high_temp_furnace_v0`)
   - Items with overlapping capabilities
   - Size variants that might be consolidatable (e.g., `_small`, `_medium`, `_large`)

4. **Create dedupe tasks:**
   - Create JSON/JSONL files in `dedupe_tasks/` with consolidation candidates
   - Add to queue with: `.venv/bin/python -m kbtool dedupe add --file dedupe_tasks/<filename>`

### Example Dedupe Task Creation

After finding overlapping furnaces in the inventory:

```json
{
  "id": "dedupe:furnace_family_high_temp",
  "kind": "machine",
  "reason": "overlap",
  "candidate_ids": ["furnace_high_temp", "high_temp_furnace_v0", "heat_treatment_furnace"],
  "notes": "Consolidate high-temperature furnaces; assess if distinct thermal capabilities exist or if naming differences only.",
  "hints": {
    "prefer": "furnace_high_temp",
    "assess": "temperature ranges and specialized treatments"
  },
  "category": "furnaces"
}
```

Save to `dedupe_tasks/furnaces_high_temp.json` and add:
```bash
.venv/bin/python -m kbtool dedupe add --file dedupe_tasks/furnaces_high_temp.json
```

## Workflow Integration

**Recommended periodic workflow:**

1. Index KB: `python -m src.cli index`
2. Generate inventory: `.venv/bin/python -m kbtool report inventory`
3. Review for duplicates (grep patterns or manual scan)
4. Create dedupe tasks for consolidation opportunities
5. Work dedupe queue: `.venv/bin/python -m kbtool dedupe lease --agent <name>`
6. Document decisions in `docs/dedupe_decisions.md`

This keeps the knowledge base clean and prevents proliferation of near-duplicate items.
