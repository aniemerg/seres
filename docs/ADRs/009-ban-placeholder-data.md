# ADR-009: Ban Placeholder and Stub Data in KB

## Status
Proposed

## Context

A comprehensive analysis of the KB revealed **pervasive use of placeholders and stubs** as a gap-filling strategy by autonomous agents. This pattern undermines data quality and obscures true material closure requirements.

### Scale of the Problem

**Quantitative findings (as of 2024-12-28):**
- **1,363** total placeholder/stub references in KB files
- **442** processes (49.6% of all processes) have "placeholder" in notes
- **99** recipes use `import_placeholder_*` processes
- **25** recipes use generic `stock_material` instead of specific inputs
- **24** dedicated `import_placeholder_*` process files
- **9** explicit placeholder items (e.g., `placeholder_component_v0`)

### Categories of Placeholders

Analysis identified six distinct categories:

#### 1. Placeholder Parameters (75 processes)
**Impact:** Low
```yaml
id: extrusion_basic_v0
notes: "Basic extrusion process for polymer or soft metal tubing; placeholder parameters."
```
Processes exist but use rough estimates. Acceptable as work-in-progress.

#### 2. Placeholder Processes (88 processes)
**Impact:** HIGH - Fake manufacturing
```yaml
id: heliostat_mounting_bracket_fabrication_v0
notes: "Placeholder fabrication that converts steel_plate_or_sheet to
       heliostat_mounting_bracket_v0 to resolve no_recipe gap for this part."
```
Entire processes created just to clear gaps, with no real manufacturing logic.

#### 3. Import Placeholder Processes (24 files)
**Impact:** MEDIUM - Lazy shortcuts
```yaml
id: import_placeholder_proximity_sensor_inductive_v0
inputs: []
outputs:
  - item_id: proximity_sensor_inductive
    qty: 1.0
notes: "External import placeholder for inductive proximity sensor."
```
Should be proper `is_import: true` items per ADR-007.

#### 4. Stock_Material Recipes (25 recipes)
**Impact:** HIGHEST - Completely fake
```yaml
id: recipe_placeholder_component_v0
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: stock_material  # ← Generic catch-all, no research
        qty: 1.0
        unit: kg
    outputs:
      - item_id: placeholder_component_v0
        qty: 1
        unit: unit
```
The most problematic pattern - agents use generic `stock_material` instead of researching real inputs.

#### 5. Explicit Placeholder Items (9 items)
**Impact:** MEDIUM
- `placeholder_component_v0`
- `placeholder_seed_component`
- `placeholder_dummy_component`
- `hydraulic_hose_segment_input_placeholder`

Created to unblock dependencies without solving underlying gaps.

#### 6. Generic Items (4 items)
**Impact:** HIGH - Obscures requirements
- `stock_material` - Used in 25+ recipes
- `raw_material` - Generic feedstock
- `none` - Null placeholder
- `placeholder_component` - Generic placeholder

### Problem Patterns Observed

**Pattern 1: "Lazy Recipe Creation"**
Agent resolves gap without research:
```yaml
inputs:
  - item_id: stock_material  # Takes 30 seconds instead of 30 minutes research
    qty: 1.0
```

**Pattern 2: "Placeholder Cascades"**
Placeholders reference other placeholders:
```
placeholder_component_v0 → uses → stock_material
  ↓ used by
placeholder_seed_component → uses → placeholder_component_v0
```

**Pattern 3: "Import Shortcuts"**
Agent creates `import_placeholder_X` instead of researching manufacturing OR creating proper import item per ADR-007.

### Root Causes

1. **Gap resolution pressure**: Agents prioritize speed over accuracy
2. **Lack of enforcement**: No validation prevents placeholders
3. **Easy escape hatches**: `stock_material` and `import_placeholder_*` enable lazy behavior
4. **Missing guidance**: Agent prompts don't explicitly forbid placeholders
5. **Knowledge gaps**: Agents don't know real process, so they fake it

### Why This Matters

Placeholders corrupt the KB in several ways:

1. **False closure calculations**: `stock_material` hides real material dependencies
2. **Unusable recipes**: Can't actually manufacture items with fake inputs
3. **Degraded trust**: Data quality becomes questionable
4. **Cascading problems**: Placeholders reference placeholders
5. **Lost knowledge**: Real manufacturing paths never documented

## Decision

We will **strictly ban placeholder and stub data** from the KB, with the following policies:

### 1. Strict Ban on Generic Placeholders

**BANNED items - never use as inputs:**
- `stock_material`
- `raw_material`
- `placeholder_component`
- `placeholder_component_v0`
- `placeholder_seed_component`
- `placeholder_dummy_component`
- Any item with `placeholder` or `stub` in the ID

**Exception:** The items themselves may exist for backward compatibility during transition, but **must not be referenced** as inputs in new/updated recipes.

### 2. Good Faith Best Effort Requirement

Agents creating or updating recipes **must**:

1. **Research real inputs** using available tools:
   - Search existing KB for similar items/processes
   - Use web search (if available) to find manufacturing information
   - Read relevant papers from `docs/papers/`
   - Examine existing recipes for patterns

2. **Use specific, real items** as inputs:
   ```yaml
   # ✅ GOOD: Specific materials researched
   inputs:
     - item_id: copper_wire_magnet
       qty: 0.05
       unit: kg
     - item_id: aluminum_alloy_ingot
       qty: 0.15
       unit: kg

   # ❌ BAD: Generic placeholder
   inputs:
     - item_id: stock_material
       qty: 1.0
       unit: kg
   ```

3. **Document uncertainty** in notes rather than using placeholders:
   ```yaml
   inputs:
     - item_id: aluminum_alloy_ingot
       qty: 0.15
       unit: kg
       notes: "Estimated quantity; may need refinement with real specs"
   notes: "Process based on similar sensor manufacturing; refine with detailed specs when available."
   ```

### 3. When Manufacturing Is Not Possible

If after good faith research, local manufacturing is not feasible:

**Option A: Create explicit import** (preferred for truly imported items)
```yaml
# kb/imports/advanced_electronics.yaml
id: import_microcontroller_advanced
kind: part
is_import: true  # Per ADR-007
name: Advanced microcontroller (imported)
notes: "Imported due to semiconductor fabrication complexity. Requires advanced lithography not feasible for early lunar base."
```

**Option B: Mark as unresolved gap** (if unsure)
- Don't create a placeholder recipe
- Leave the gap in the queue for future work or human review
- Document why it's challenging in a note or issue

**NEVER acceptable:**
- Creating `import_placeholder_*` processes
- Using `stock_material` as a shortcut
- Creating `placeholder_X` items

### 4. Placeholder Detection and Cleanup

**Detection is independent of indexer.** Use ADR-008 manual queue addition to manage cleanup:

#### Detection Queries

**Find stock_material recipes:**
```bash
grep -r "item_id: stock_material" kb/recipes --include="*.yaml" -l
```

**Find placeholder processes:**
```bash
grep -r "notes:.*[Pp]laceholder" kb/processes --include="*.yaml" -l
```

**Find import_placeholder processes:**
```bash
find kb/processes -name "import_placeholder_*.yaml"
```

**Find placeholder items:**
```bash
find kb/items -name "*placeholder*"
```

#### Adding Cleanup Items to Queue

Using ADR-008 CLI:
```bash
# Add stock_material recipe for cleanup
.venv/bin/python -m kbtool queue add \
  --id "placeholder_cleanup:recipe_fluorite_v0" \
  --type recipe \
  --reason placeholder_cleanup \
  --priority high \
  --context '{"recipe_id": "recipe_fluorite_v0", "issue": "Uses stock_material instead of specific inputs"}'

# Add placeholder process for cleanup
.venv/bin/python -m kbtool queue add \
  --id "placeholder_cleanup:heliostat_mounting_bracket_fabrication_v0" \
  --type process \
  --reason placeholder_cleanup \
  --priority medium \
  --context '{"process_id": "heliostat_mounting_bracket_fabrication_v0", "issue": "Placeholder fabrication process"}'
```

Using Python API:
```python
from kbtool.queue_tool import add_queue_item

# Add all stock_material recipes to cleanup queue
import os, yaml

for recipe_file in Path("kb/recipes").rglob("*.yaml"):
    with open(recipe_file) as f:
        recipe = yaml.safe_load(f)

    # Check if uses stock_material
    for step in recipe.get('steps', []):
        for inp in step.get('inputs', []):
            if inp.get('item_id') == 'stock_material':
                add_queue_item(
                    gap_id=f"placeholder_cleanup:{recipe['id']}",
                    gap_type="placeholder_cleanup",
                    item_id=recipe['id'],
                    context={
                        "recipe_id": recipe['id'],
                        "issue": "Uses stock_material",
                        "file": str(recipe_file)
                    },
                    priority="high"
                )
                break
```

### 5. Deprecation Path for Import Placeholders

**Two-step conversion:**

1. **Identify if truly imported or just lazy:**
   - Truly imported (complex electronics, specialized materials): Convert to proper import per ADR-007
   - Just lazy (could be manufactured): Research and create real recipe

2. **For true imports:**
   ```yaml
   # OLD: kb/processes/import_placeholder_proximity_sensor_v0.yaml
   id: import_placeholder_proximity_sensor_inductive_v0
   inputs: []
   outputs: [...]

   # NEW: kb/imports/proximity_sensor.yaml
   id: import_proximity_sensor_inductive
   kind: part
   is_import: true
   name: Inductive proximity sensor (imported)
   notes: "Imported due to precision electronics requirement. ISRU alternative: proximity_sensor_inductive_v0 (local manufacturing with PCB fab)."
   isru_alternative: proximity_sensor_inductive  # Links to local version
   ```

3. **For lazy shortcuts:**
   - Research real manufacturing process
   - Create proper recipe with specific inputs
   - Delete the `import_placeholder_*` file

### 6. Documentation Updates

**Update the following documentation:**

#### A. Queue Agent Cached Context (`queue_agents/cached_context.md`)

Add section:
```markdown
## ⛔ PROHIBITED: Placeholder and Stub Data

**STRICT BAN on placeholders.** Never use:
- `stock_material` as recipe input
- `placeholder_*` items
- `import_placeholder_*` processes
- Generic catch-all items

**Required approach:**
1. Research real inputs using KB search, web search, papers
2. Use specific, real items (e.g., `aluminum_alloy_ingot`, not `stock_material`)
3. If truly impossible to manufacture: Create proper import with `is_import: true`
4. Document uncertainty in notes, not with placeholders

**Examples:**

❌ BAD - Placeholder:
```yaml
inputs:
  - item_id: stock_material
    qty: 1.0
```

✅ GOOD - Specific materials:
```yaml
inputs:
  - item_id: copper_wire_magnet
    qty: 0.05
    unit: kg
    notes: "Estimated; refine with specs"
  - item_id: aluminum_alloy_ingot
    qty: 0.15
    unit: kg
```
```

#### B. Main Documentation (`docs/kb_creation_guidelines.md` or similar)

Create anti-patterns guide:
- Why placeholders are harmful
- How to research real inputs
- When to use imports vs. manufacturing
- Examples of good vs. bad recipes

#### C. Agent Reference Memo (if applicable)

Add to schema validation rules:
- Recipes must not use `stock_material`
- Items must not have `placeholder` in ID (except during cleanup)
- Processes must not be pure placeholders

## Implementation Plan

### Phase 1: Immediate (When ADR Approved)

1. **Update agent documentation** with placeholder ban
2. **Add to queue agent cached context** with examples
3. **Create detection scripts** for finding placeholders
4. **Document cleanup process** using ADR-008 queue addition

### Phase 2: Cleanup Campaign (2-4 weeks)

1. **Identify all 25 stock_material recipes**
   - Add to queue with priority: high
   - Assign to agents or human review

2. **Review 88 placeholder processes**
   - Categorize: Delete vs. Fix vs. Convert to Import
   - Add fixable ones to queue

3. **Convert import_placeholder_* (24 files)**
   - Evaluate each: True import or lazy shortcut?
   - Create proper imports or real recipes
   - Delete placeholder files

4. **Remove placeholder items (9 files)**
   - Ensure nothing references them
   - Delete files

### Phase 3: Prevention (Ongoing)

1. **Monitor new additions** for placeholder patterns
2. **Review agent work** periodically for compliance
3. **Update detection scripts** as new patterns emerge
4. **Refine guidance** based on agent feedback

## Verification

To independently verify the placeholder problem:

### Automated Detection
```bash
# Clone detection script
wget https://path/to/placeholder_detection_tools.sh
chmod +x placeholder_detection_tools.sh
./placeholder_detection_tools.sh

# Or run queries directly:
grep -r "item_id: stock_material" kb/recipes --include="*.yaml" | wc -l
# Should show: 25

grep -r "notes:.*[Pp]laceholder" kb/processes --include="*.yaml" -l | wc -l
# Should show: 442

find kb/processes -name "import_placeholder_*.yaml" | wc -l
# Should show: 24
```

### Manual Sampling
```bash
# Review sample stock_material recipe:
cat kb/recipes/recipe_fluorite_v0.yaml

# Review sample placeholder process:
cat kb/processes/heliostat_mounting_bracket_fabrication_v0.yaml

# Review sample import placeholder:
cat kb/processes/import_placeholder_proximity_sensor_inductive_v0.yaml
```

### Analysis Report
Full analysis available at:
- `out/placeholder_analysis_report.md`
- `design/placeholder_analysis_report.md`

Contains:
- Detailed categorization
- Specific file lists
- Root cause analysis
- Quantitative breakdown

## Consequences

### Positive

1. **Higher data quality**: Recipes reflect real manufacturing
2. **Accurate closure analysis**: No hidden dependencies via `stock_material`
3. **Usable recipes**: Can actually build things from documented recipes
4. **Better agent behavior**: Forces research instead of shortcuts
5. **Clear imports**: Proper `is_import: true` items per ADR-007

### Negative

1. **Slower gap resolution**: Research takes longer than placeholders
2. **More unresolved gaps initially**: Agents can't fake solutions
3. **Cleanup work required**: 25 recipes + 88 processes + 24 imports need fixing
4. **Agent training needed**: Must learn new standards

### Mitigations

1. **Better guidance**: Clear examples of how to research
2. **Web search access**: Enable agents to find manufacturing info
3. **Template library**: Common recipe patterns for reference
4. **Staged cleanup**: Prioritize high-impact placeholders first
5. **Human assistance**: Complex items may need human research

## Alternatives Considered

### Alternative 1: Allow Placeholders with Tagging
**Idea:** Keep placeholders but tag them for later cleanup.

**Rejected because:**
- Placeholders accumulate faster than cleanup
- Data quality degrades over time
- Hard to distinguish "temporary" from permanent

### Alternative 2: Separate Placeholder Queue
**Idea:** Placeholders go into separate low-priority queue.

**Rejected because:**
- Still pollutes KB with fake data
- Doesn't prevent placeholder creation
- Doesn't address root cause

### Alternative 3: Soft Ban with Warnings
**Idea:** Warn but don't prevent placeholder creation.

**Rejected because:**
- Agents ignore warnings under gap pressure
- Problem continues to grow
- Half-measures don't solve systemic issue

### Alternative 4: Indexer Validation (Hard Reject)
**Idea:** Indexer rejects files with placeholders.

**Rejected because:**
- Too disruptive during transition
- Prevents iterative improvement
- Cleanup work should be agent-managed (ADR-008 approach)
- Current decision: Use manual queue addition instead

## References

- **ADR-007**: Explicit Import Items Architecture
- **ADR-008**: Manual Queue Addition (cleanup mechanism)
- **Analysis Report**: `design/placeholder_analysis_report.md`
- **Detection Tools**: `out/placeholder_detection_tools.sh`

## Appendix: Quick Reference

### ✅ GOOD Examples

```yaml
# Good recipe - specific inputs
id: recipe_proximity_sensor_v0
variant_id: v0
steps:
  - process_id: electronics_assembly_v0
    inputs:
      - item_id: copper_wire_magnet
        qty: 0.05
        unit: kg
      - item_id: pcb_populated
        qty: 0.02
        unit: kg
      - item_id: aluminum_alloy_ingot
        qty: 0.15
        unit: kg
    outputs:
      - item_id: proximity_sensor
        qty: 1
        unit: unit
    notes: "Based on typical inductive sensor construction"

# Good import - explicit and proper
id: import_advanced_semiconductor
kind: part
is_import: true
name: Advanced semiconductor (imported)
notes: "Requires sub-micron lithography not available. ISRU alternative requires semiconductor fab facility."
```

### ❌ BAD Examples

```yaml
# Bad recipe - uses stock_material
id: recipe_something_v0
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: stock_material  # ❌ BANNED
        qty: 1.0
    outputs:
      - item_id: something
        qty: 1

# Bad process - pure placeholder
id: import_placeholder_something_v0  # ❌ BANNED pattern
inputs: []
outputs:
  - item_id: something
    qty: 1.0
notes: "Placeholder import"  # ❌ Not a real import per ADR-007

# Bad item - explicit placeholder
id: placeholder_component_v0  # ❌ BANNED
kind: material
notes: "Placeholder to be replaced later"  # ❌ Never acceptable
```

---

**Status:** Proposed
**Date:** 2024-12-28
**Author:** System Analysis
**Related ADRs:** 007, 008
