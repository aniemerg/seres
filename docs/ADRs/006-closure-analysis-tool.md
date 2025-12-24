# ADR 006 — Closure Analysis Tool

**Status:** Proposed
**Date:** 2025-12-22
**Owner:** kbtool/analysis

## Context / Problem

The primary goal of this KB is to model a self-replicating lunar base and determine **tech tree closure** - whether a system can fully replicate itself using only local resources plus a minimal import set.

**Current gaps in capability:**
1. **No systematic closure analysis** - Can't determine which machines/parts form a closed replication loop
2. **No import set identification** - Don't know the minimum items that must be imported from Earth
3. **No dependency depth tracking** - Can't identify which machines are foundational vs leaf nodes
4. **No element-level tracing** - Can't verify all required elements are available on the Moon
5. **Manual KB validation** - Closure checking requires manual inspection of BOMs/recipes

**Current validation tools:**
- ✅ `kbtool index` - Detects missing references, null values, orphan resources
- ✅ `base_builder` simulation - Validates end-to-end production chains
- ❌ No tool to answer: "Can this system replicate itself?"

**The core questions we can't answer systematically:**
1. Which machines can manufacture copies of themselves (direct closure)?
2. Which machines can be manufactured using other machines in the KB (indirect closure)?
3. What's the minimum import set to bootstrap a self-replicating base?
4. Which elements are required and are they available on the Moon?
5. What's the dependency depth of the tech tree (longest manufacturing chain)?
6. Which machines are on the critical path for replication?

**Use cases:**
- **Scenario planning**: "Can we bootstrap with just labor bots + tools?"
- **Import optimization**: "What's the minimum mass we need to import?"
- **KB validation**: "Are there circular dependencies or dead-end branches?"
- **Bottleneck identification**: "Which machines are single points of failure?"
- **Element availability**: "Do we need carbon? Nitrogen? Rare earths?"

## Decision / Direction

Build a **Closure Analysis Tool** (`kbtool analyze-closure`) that performs multi-level dependency analysis:

1. **Machine-level closure**: Trace machine → BOM → parts → recipes → processes → materials
2. **Import set identification**: Flag items with no local manufacturing route
3. **Dependency graph**: Build complete tech tree with depth annotations
4. **Element analysis**: Decompose all materials to elemental composition
5. **Closure metrics**: Quantify self-sufficiency (local mass / imported mass ratio)

### Core Design Principles

1. **Work with incomplete data** - Report gaps, don't fail on missing information
2. **Multiple closure definitions** - Support strict/partial/economic closure
3. **Explicit import tracking** - Clear distinction between "can't make" vs "haven't defined yet"
4. **Actionable output** - Generate work items for filling gaps
5. **Visualization ready** - Output formats suitable for graph rendering
6. **Incremental refinement** - Re-run as KB improves, track progress

### Closure Definitions

**Strict Closure**: All machines can manufacture copies of themselves using only:
- Local resources (regolith, solar energy)
- Other machines in the closed set
- Zero imports (except bootstrap)

**Partial Closure**: All machines can be manufactured, but some consumable parts must be imported:
- Example: Electronics imported, but all mechanical/structural parts local
- Target: High local-to-import mass ratio (e.g., 100:1)

**Economic Closure**: System growth rate > 1x per cycle with acceptable import costs:
- Can replicate faster than parts wear out
- Import cost sustainable over mission lifetime

**Bootstrap Closure**: Closure achieved after initial import set:
- Example: Import 1 labor bot + tools → can manufacture everything else

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│ CLI: kbtool analyze-closure                             │
│  Options: --output-dir, --closure-type, --max-depth     │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│ Closure Analyzer                                         │
│  1. Load KB index (index.json)                          │
│  2. Build machine dependency graph                      │
│  3. Identify import set                                 │
│  4. Calculate closure metrics                           │
│  5. Generate reports & visualizations                   │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┬──────────────┐
        │                             │              │
┌───────▼────────┐  ┌────────────────▼──┐  ┌────────▼─────────┐
│ Machine Graph  │  │ Element Tracer   │  │ Metrics Engine   │
│ Builder        │  │                  │  │                  │
│                │  │ - Trace to       │  │ - Closure score  │
│ - BOM → parts  │  │   elements       │  │ - Import ratio   │
│ - Recipe →     │  │ - Check lunar    │  │ - Depth stats    │
│   materials    │  │   availability   │  │ - Coverage %     │
│ - Depth calc   │  │ - Flag imports   │  │                  │
└───────┬────────┘  └──────────────────┘  └──────────────────┘
        │
┌───────▼──────────────────────────────────────────────────┐
│ Outputs (out/closure/)                                    │
│  - closure_report.md - Human-readable summary            │
│  - machine_graph.json - Full dependency tree             │
│  - import_set.jsonl - Items requiring import             │
│  - closure_metrics.json - Quantitative metrics           │
│  - element_requirements.json - Elemental analysis        │
│  - work_queue_closure.jsonl - Gaps blocking closure      │
└───────────────────────────────────────────────────────────┘
```

## Implementation

### Phase 1: Machine Dependency Graph (Core)

**Input**: `out/index.json` (existing KB index)

**Algorithm**:
```python
def build_machine_graph(index_data):
    """
    For each machine:
    1. Load BOM → get parts list
    2. For each part:
       a. Find recipe (or mark as import)
       b. For each recipe step → process
       c. For each process → inputs (materials)
       d. For each material → trace recursively
    3. Calculate dependency depth (longest chain to leaf)
    4. Mark as self-replicating if all dependencies satisfied
    """

    graph = {}
    for machine_id in get_all_machines():
        deps = trace_dependencies(machine_id, depth=0, max_depth=50)
        graph[machine_id] = {
            'dependencies': deps,
            'depth': calculate_depth(deps),
            'import_required': has_import_dependency(deps),
            'closure_status': classify_closure(deps)
        }
    return graph
```

**Dependency types tracked**:
- `local` - Can be manufactured or extracted locally
- `import` - Must be imported (no recipe exists)
- `undefined` - Referenced but not defined in KB
- `circular` - Circular dependency detected

**Depth calculation**:
```
depth(regolith) = 0  # Freely available
depth(part) = 1 + max(depth of all materials needed)
depth(machine) = 1 + max(depth of all parts in BOM)
```

### Phase 2: Import Set Identification

**Import classification**:
1. **Fundamental imports** - Can't manufacture on Moon (complex electronics, etc.)
2. **Missing recipes** - Could manufacture but recipe not defined
3. **Missing machines** - Recipe exists but required machine unavailable
4. **Elemental constraints** - Material requires unavailable elements

**Output**: `out/closure/import_set.jsonl`
```json
{
  "item_id": "microcontroller_advanced",
  "kind": "part",
  "import_reason": "no_recipe",
  "import_type": "fundamental",
  "mass_per_unit": 0.05,
  "notes": "Complex fabrication requires Earth semiconductor fabs"
}
```

### Phase 3: Closure Metrics

**Metrics calculated**:
```json
{
  "total_machines": 317,
  "machines_with_boms": 317,
  "machines_with_recipes": 300,
  "self_replicating_machines": 250,
  "machines_requiring_imports": 67,
  "closure_percentage": 78.9,
  "max_dependency_depth": 15,
  "median_dependency_depth": 7,
  "total_import_items": 45,
  "estimated_import_mass_kg": 1250,
  "local_to_import_ratio": 127.5
}
```

**Closure percentage**:
```
closure_% = (machines with complete local supply chain) / (total machines) × 100
```

**Local-to-import ratio**:
```
ratio = (total local mass produced) / (total import mass required)
```
Higher is better. Target: >100:1 for viable self-replication.

### Phase 4: Element Analysis

**Trace to elemental composition**:
```python
def trace_to_elements(item_id):
    """
    For material items with composition field:
    - Aggregate elemental requirements
    - Check against lunar abundance data
    - Flag imports for scarce elements
    """
    elements = {}
    material = load_material(item_id)
    for element, fraction in material.composition.items():
        elements[element] = elements.get(element, 0) + fraction
    return elements
```

**Lunar element availability** (from regolith):
```python
LUNAR_ABUNDANT = {
    'O', 'Si', 'Fe', 'Al', 'Ca', 'Mg', 'Ti'
}

LUNAR_TRACE = {
    'C', 'N', 'H', 'Cu', 'Ni', 'Cr', 'Mn'
}

LUNAR_SCARCE = {
    # Rare earths, volatile elements, etc.
}
```

**Output**: `out/closure/element_requirements.json`
```json
{
  "abundant": {"Fe": 1500.0, "Si": 800.0, "Al": 600.0},
  "trace": {"C": 50.0, "Cu": 30.0},
  "scarce": {"Nd": 5.0, "Eu": 2.0},
  "import_recommended": ["Nd", "Eu"],
  "substitution_opportunities": [
    {"element": "Cu", "usage": "wiring", "substitute": "Al"}
  ]
}
```

### Phase 5: Work Queue Generation

Generate actionable gaps for filling:

```json
{
  "id": "closure_gap:microcontroller_advanced:no_recipe",
  "gap_type": "blocks_closure",
  "priority": "high",
  "item_id": "microcontroller_advanced",
  "blocks_machines": ["robot_fab_station_v0", "pcb_fab_station"],
  "recommendation": "Create recipe or mark as permanent import",
  "impact": "Blocks 15 machines from closure"
}
```

**Priority scoring**:
- High: Blocks >10 machines or is on critical path
- Medium: Blocks 3-10 machines
- Low: Blocks <3 machines or has alternatives

## Command Interface

```bash
# Basic closure analysis
kbtool analyze-closure

# With options
kbtool analyze-closure \
  --closure-type partial \
  --max-depth 20 \
  --output-dir out/closure \
  --include-elements \
  --generate-graph

# Focus on specific subsystem
kbtool analyze-closure --seed battery_system_nife_v0

# Check specific machine
kbtool analyze-closure --machine labor_bot_general_v0
```

## Output Files

### 1. `out/closure/closure_report.md`

Human-readable summary:
```markdown
# Tech Tree Closure Analysis

**Date**: 2025-12-22
**Closure Type**: Partial
**KB Version**: v0

## Summary

- Total machines: 317
- Machines with complete supply chain: 250 (78.9%)
- Machines requiring imports: 67 (21.1%)
- Total import items: 45
- Estimated import mass: 1,250 kg
- Local-to-import ratio: 127.5:1

## Closure Status

✅ **Partial closure achieved**
- All structural/mechanical parts manufacturable locally
- Electronics require Earth imports (low mass, high value)
- Estimated bootstrap: 1 labor bot + tools + electronics kit

## Critical Path Machines

1. labor_bot_general_v0 (depth: 12)
   - Can manufacture: Yes (with imports)
   - Imports required: microcontroller (50g), sensors (100g)

2. smelting_furnace_v0 (depth: 8)
   - Can manufacture: Yes (fully local)
   - Self-replicating: Yes

## Blocking Gaps (Top 10)

1. microcontroller_advanced - blocks 15 machines
2. precision_sensor_suite - blocks 12 machines
...
```

### 2. `out/closure/machine_graph.json`

Full dependency tree (machine → parts → materials → elements):
```json
{
  "labor_bot_general_v0": {
    "depth": 12,
    "closure_status": "partial",
    "bom": "bom_labor_bot_general_v0",
    "parts": [
      {
        "item_id": "motor_electric_small",
        "quantity": 4,
        "recipe": "recipe_motor_electric_small_v0",
        "closure_status": "local",
        "depth": 8
      },
      {
        "item_id": "microcontroller_advanced",
        "quantity": 1,
        "recipe": null,
        "closure_status": "import",
        "import_reason": "no_recipe",
        "depth": 0
      }
    ],
    "total_mass_kg": 200,
    "import_mass_kg": 0.5,
    "local_ratio": 400.0
  }
}
```

### 3. `out/closure/import_set.jsonl`

All items requiring import (JSONL for easy filtering):
```jsonl
{"item_id": "microcontroller_advanced", "kind": "part", "mass_kg": 0.05, "reason": "no_recipe", "blocks_count": 15}
{"item_id": "precision_bearings_ceramic", "kind": "part", "mass_kg": 0.2, "reason": "precision_manufacturing", "blocks_count": 8}
```

### 4. `out/closure/closure_metrics.json`

Quantitative metrics (machine-readable):
```json
{
  "analysis_date": "2025-12-22T10:30:00Z",
  "kb_version": "v0",
  "closure_type": "partial",
  "machines": {
    "total": 317,
    "with_boms": 317,
    "with_recipes": 300,
    "fully_local": 250,
    "requires_imports": 67
  },
  "closure": {
    "percentage": 78.9,
    "max_depth": 15,
    "median_depth": 7,
    "mean_depth": 8.3
  },
  "imports": {
    "total_items": 45,
    "total_mass_kg": 1250,
    "local_to_import_ratio": 127.5
  }
}
```

### 5. `out/closure/element_requirements.json`

Elemental analysis:
```json
{
  "total_elements_required": ["O", "Si", "Fe", "Al", "Cu", "C", ...],
  "abundant_on_moon": ["O", "Si", "Fe", "Al", "Ca", "Mg", "Ti"],
  "trace_on_moon": ["C", "Cu", "Ni", "Cr"],
  "import_recommended": ["Nd", "Eu", "rare_earths"],
  "total_mass_by_element": {
    "Fe": 15000.0,
    "Al": 8000.0,
    "Cu": 500.0,
    "C": 200.0
  }
}
```

### 6. `out/closure/work_queue_closure.jsonl`

Gaps blocking closure (feeds into main work queue):
```jsonl
{"id": "closure:microcontroller_advanced", "priority": "high", "blocks": 15, "recommendation": "create_recipe_or_import"}
```

## Integration with Existing Tools

### With `kbtool index`

Closure analysis runs **after** indexing:
```bash
# Standard workflow
kbtool index                  # Generate index.json
kbtool analyze-closure        # Analyze closure using index.json
```

Work items from closure analysis feed into main work queue:
```python
# In indexer.py
def _update_work_queue(..., closure_gaps):
    # Add closure gaps to work queue with high priority
    for gap in closure_gaps:
        if gap['blocks_count'] > 10:
            gap['priority'] = 'critical'
```

### With `base_builder` Simulation

Closure analysis informs simulation strategy:
1. **Pre-simulation**: Identify minimum import set
2. **During simulation**: Validate closure predictions
3. **Post-simulation**: Compare predicted vs actual imports

Agent can query closure data:
```python
# In simulation
closure_data = load_closure_analysis()
bootstrap_items = closure_data['import_set']
agent.import_items(bootstrap_items)  # Minimal imports
```

### With Seed Files

Closure analysis per seed:
```bash
# Analyze specific subsystem
kbtool analyze-closure --seed battery_system_nife_v0
# Output: Closure status for just battery-related machines
```

## Success Criteria

**Must have**:
- [ ] Analyze all 317 machines with BOMs
- [ ] Identify import set (items with no local recipe)
- [ ] Calculate closure percentage
- [ ] Generate dependency graph (JSON)
- [ ] Generate human-readable report (markdown)
- [ ] Flag gaps blocking closure

**Should have**:
- [ ] Element-level analysis
- [ ] Local-to-import mass ratio
- [ ] Dependency depth calculation
- [ ] Critical path identification
- [ ] Work queue integration

**Nice to have**:
- [ ] Graph visualization (DOT/Graphviz format)
- [ ] Sensitivity analysis (what if X is imported?)
- [ ] Alternative path detection (multiple recipes)
- [ ] Cost optimization (minimize import mass)

## Consequences

### Positive

1. **Systematic closure validation** - Can answer "is this self-replicating?" with data
2. **Import optimization** - Identifies minimum bootstrap set
3. **KB gap prioritization** - Focus work on items blocking closure
4. **Mission planning support** - Quantifies Earth import requirements
5. **Progress tracking** - Re-run to measure KB maturity over time
6. **Scenario comparison** - "What if we import X instead of Y?"

### Negative

1. **Complexity** - New tool to maintain, complex graph algorithms
2. **Performance** - May be slow on large KBs (317 machines × deep recursion)
3. **Incomplete data handling** - Must gracefully handle missing BOMs/recipes
4. **Definition ambiguity** - "Closure" means different things to different users

### Neutral

1. **New output directory** - `out/closure/` for analysis results
2. **Additional dependencies** - May need graph libraries (networkx?)
3. **Documentation burden** - Need to explain closure metrics

## Implementation Plan

### Phase 1: Core Graph Builder (Week 1)
- [ ] Load index.json, extract machines/BOMs/recipes
- [ ] Build machine → parts dependency tree
- [ ] Calculate dependency depth
- [ ] Identify items with no recipe (import set)
- [ ] Generate basic report

### Phase 2: Metrics & Analysis (Week 2)
- [ ] Calculate closure percentage
- [ ] Compute local-to-import ratio
- [ ] Identify critical path machines
- [ ] Generate work queue items
- [ ] Integration with main indexer

### Phase 3: Element Analysis (Week 3)
- [ ] Trace materials to elemental composition
- [ ] Check against lunar availability
- [ ] Flag import-requiring elements
- [ ] Suggest substitutions

### Phase 4: Visualization & Polish (Week 4)
- [ ] Generate graph visualization (Graphviz)
- [ ] Improve report formatting
- [ ] Add command-line options
- [ ] Performance optimization
- [ ] Documentation

## Open Questions

1. **How to handle alternative recipes?**
   - If item has multiple recipes, which to use for closure?
   - Take optimistic (any works) or pessimistic (all fail) approach?

2. **How to handle material_class substitution?**
   - If recipe needs `raw_metal`, can use `iron_pure` or `aluminum_pure`
   - Does this count as closure or requires import?

3. **How to handle probabilistic yields?**
   - If process has 50% yield, need 2x input
   - Does this affect closure calculation?

4. **How to define "fundamental import"?**
   - Manual tagging? Heuristic (no recipe for N months)? User decision?

5. **How to handle circular dependencies?**
   - Machine A needs Machine B to build, Machine B needs Machine A
   - Is this closure or deadlock?

## Related Documents

- **ADR-004**: Base Builder Simulation - Validates closure predictions
- **ADR-003**: Process-Machine Refactor - Affects dependency tracing
- **design/meta-memo.md**: Project philosophy on self-replication
- **docs/parts_and_labor_guidelines.md**: Parts policy affects closure
- **design/resource_type_migration_handoff.md**: Must complete before closure analysis

## Next Steps After Implementation

1. **Run first closure analysis** - Get baseline metrics
2. **Identify top blockers** - Which gaps most impact closure?
3. **Fill critical gaps** - Focus on high-impact missing recipes
4. **Re-run simulation** - Validate closure predictions
5. **Iterate KB** - Improve closure percentage over time

**Target**: Achieve 90%+ closure (partial) for v1.0 release.

---

## Addendum: Recipe-Level Input Support (2025-12-24)

**Issue Discovered**: The initial closure analysis implementation only checked for step-level and process-level inputs, missing recipe-level inputs entirely. This caused 133 recipes with explicit recipe-level inputs to be incorrectly flagged as having no inputs.

**Root Cause**: KB recipes follow three valid patterns:
1. **Recipe-level inputs** (~133 recipes): Explicit `inputs:` and `outputs:` at recipe level
2. **Process-derived inputs** (~1877 recipes): Material flow comes from referenced processes
3. **Step-level inputs** (rare/legacy): Inputs defined on individual steps

The closure analyzer only supported patterns 2 and 3, not pattern 1.

**Changes Made**:

1. **Updated `kbtool/closure_analysis.py:_expand_item()`** to check inputs in priority order:
   ```python
   # Priority order:
   # 1. Recipe-level inputs (explicit material flow)
   # 2. Step-level inputs (legacy/rare)
   # 3. Process-level inputs (derived from processes)
   ```

2. **Added recipe-level input handling** with proper scaling:
   ```python
   recipe_inputs = recipe.get('inputs', [])
   if recipe_inputs:
       # Calculate scale factor from recipe outputs
       recipe_outputs = recipe.get('outputs', [])
       # Scale inputs based on output quantity needed
   ```

3. **Enhanced null quantity detection** to flag gaps:
   - Recipe-level inputs with null/zero qty
   - Step-level inputs with null/zero qty
   - Process-level inputs with null/zero qty

   These are now reported in the errors list for potential work queue generation.

4. **Disabled old validation** in `kbtool/indexer.py:_validate_recipe_inputs()`:
   - Old validation incorrectly checked for step-level inputs only
   - Replaced with empty list (validation now happens in closure analyzer)
   - Removes 1877 false-positive queue items

**Impact**:

- ✅ 133 recipes with recipe-level inputs now properly traced
- ✅ Closure analysis can now resolve material flow for all valid recipe patterns
- ✅ Null quantities are flagged as errors (potential work queue items)
- ✅ Removes false-positive `recipe_no_inputs` validation

**Next Steps**:

1. Run closure analysis to identify actual material flow gaps
2. Generate work queue items for null quantities that block material tracing
3. Fill in null quantities in critical processes (83 processes affected)

**Schema Implications**:

Recipe `inputs:` and `outputs:` fields are **optional** per Memo A specification. Recipes can:
- Define explicit inputs/outputs at recipe level (preferred for clarity)
- Rely on process inputs/outputs (works for generic processes)
- Mix both approaches (recipe inputs override process inputs)

The closure analyzer now supports all three patterns correctly.
