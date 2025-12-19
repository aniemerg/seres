# Research Question: Measuring Knowledge Base Compactness After Deduplication

## Executive Summary

We need metrics to measure the success of our deduplication efforts in the knowledge base (KB). The goal is to quantify "compactness" - the reduction in redundancy while preserving all manufacturing capabilities. This document defines the research question, provides full context, and requests specific deliverables.

---

## Context: The Knowledge Base System

### Purpose
The KB models a self-replicating manufacturing system as a directed graph representing:
- **What can be made** (items: machines, parts, materials)
- **How to make things** (processes, recipes, BOMs)
- **What resources are needed** (machine capabilities, energy, time)

The ultimate goal: Calculate the minimum imported mass, energy, and time needed to bootstrap a manufacturing capability from local resources.

### Data Model

#### Entities

**Items** (nodes in product structure graph):
- **Materials**: Raw/processed materials (regolith, metals, glass, gases)
  - Fields: `id`, `name`, `kind: material`, `unit`, `density`, `state`
- **Parts**: Components (bearings, electrodes, housings)
  - Fields: `id`, `name`, `kind: part`, `mass`, `material_class`
- **Machines**: Manufacturing equipment
  - Fields: `id`, `name`, `kind: machine`, `mass`, `capabilities[]`, `bom` reference

**Processes** (nodes in transformation graph):
- Unit operations transforming inputs → outputs
- Fields: `id`, `inputs[]`, `outputs[]`, `byproducts[]`, `resource_requirements[]`, `energy_model`, `time_model`

**Recipes** (paths through process graph):
- Ordered lists of processes to manufacture an item
- Fields: `id`, `target_item_id`, `steps[]` (process IDs)

**BOMs** (component trees):
- Hierarchical decomposition of machines/parts into components
- Fields: `id`, `owner_item_id`, `components[]` (item_id + qty)

**Resources**:
- Capabilities provided by machines (e.g., "grinding", "casting")
- Fields: `id`, `resource_type`

#### Graph Structure

Two interconnected graphs:

1. **Product Structure (BOM) Graph**:
   ```
   Machine --has--> Subassembly --has--> Part --has--> Material
   ```

2. **Process Network Graph**:
   ```
   Item(s) --process--> Item(s)
          (requires resources + energy/time)
   ```

**References** (edges):
- Recipe → Process (recipe.steps[])
- Process → Item (process.inputs[], outputs[], byproducts[])
- Process → Resource (process.resource_requirements[])
- BOM → Item (bom.components[])
- Machine → BOM (machine.bom)
- Resource → Machine (implicit: machine.capabilities[])

#### Import Policy

Items without recipes are treated as **imports** with mass penalties. The system aims to minimize imports by:
1. Creating recipes for items (local manufacturing)
2. Removing redundant items (deduplication)

---

## The Deduplication Problem

### What We're Consolidating

Over time, the KB accumulates overlapping/duplicate items:
- Multiple crushers: `crusher_basic`, `rock_crusher_basic`, `jaw_crusher_v0`
- Multiple presses: `hydraulic_press`, `hydraulic_press_small`, `press_hydraulic`, `power_hammer_or_press_v0`
- Multiple furnaces with similar temp ranges and capabilities

### Deduplication Process

For each dedupe task:
1. **Identify candidates**: List of overlapping items (e.g., 3 crushers)
2. **Analyze**: Compare mass, capabilities, usage in processes/BOMs
3. **Decide**: Choose one canonical item to keep
4. **Update references**: Change all process/BOM/recipe references to use canonical item
5. **Deprecate**: Mark deprecated items with `DEPRECATED` notes (don't delete - preserve provenance)
6. **Document**: Record decision and rationale

**Example: Press Family Consolidation**
- **Before**: 8 press machines (600-1200 kg), 15+ process references split across them
- **After**: 3 press machines (general hydraulic, hot press, sheet brake), all references canonicalized
- **Result**: 5 deprecated items, ~12 process files updated

### Why This Matters

**Benefits of consolidation**:
- Simpler dependency graph (fewer nodes)
- Clearer canonical paths (fewer recipe variants)
- Better mass accounting (fewer "undefined" references)
- Easier to reason about bottlenecks (fewer machines to track)

**Risks of over-consolidation**:
- Losing genuine capability distinctions (e.g., consolidating lathe into mill loses turning capability)
- Creating unrealistic super-machines (e.g., one furnace covering 200-3000°C)

---

## Research Question

### Primary Question

**How do we quantify the "compactness" of the KB graph after deduplication, such that we can:**
1. **Measure success**: Show that deduplication reduced redundancy
2. **Detect failure**: Identify over-consolidation (lost capabilities) or under-consolidation (missed duplicates)
3. **Guide future work**: Prioritize which dedupe tasks have highest impact

### Sub-Questions

1. **Node Reduction**: What's the simplest count of items before/after?
2. **Reference Consolidation**: How do we measure edge simplification in the graph?
3. **Canonical Coverage**: What fraction of references point to deprecated vs canonical items?
4. **Capability Preservation**: How do we verify we haven't lost manufacturing capabilities?
5. **Graph Complexity**: Can we measure structural simplification (diameter, clustering, centrality)?
6. **Mass Closure**: Does consolidation improve our ability to account for total system mass?

---

## Data Available for Metrics

### Files We Can Read

1. **`out/index.json`**: Complete KB index
   ```json
   {
     "entries": {
       "crusher_basic": {
         "id": "crusher_basic",
         "kind": "machine",
         "status": "ok",
         "file_path": "kb/items/machines/crusher_basic.yaml",
         "last_modified": 1234567890
       },
       ...
     },
     "summary": {
       "total_items": 450,
       "machines": 89,
       "parts": 212,
       "materials": 67,
       "processes": 82
     }
   }
   ```

2. **KB YAML files**: All items, processes, recipes, BOMs
   - Can be parsed to extract references
   - Can identify `DEPRECATED` markers

3. **`out/work_queue.jsonl`**: Current gaps (missing recipes, fields, etc.)

4. **`out/dedupe_queue.jsonl`**: Dedupe tasks and status

5. **`out/dedupe_decisions.md`**: Historical record of consolidations

### Metrics We Can Compute

From index.json + KB files, we can compute:
- **Node counts**: Total items by kind (machine, part, material)
- **Deprecated count**: Items marked `DEPRECATED`
- **Active count**: Items not deprecated
- **Reference counts**:
  - Process → item (inputs/outputs)
  - Process → resource
  - BOM → item
  - Recipe → process
  - Machine → BOM
- **Usage statistics**: How many processes/recipes reference each item
- **Graph structure**:
  - Connectivity (which items connect to which)
  - Path lengths (recipe complexity)
  - Clustering (related items)

---

## Constraints and Requirements

### Must-Haves

1. **Computable from existing data**: Don't require new instrumentation
2. **Before/after comparison**: Metrics should be comparable across dedupe runs
3. **Interpretable**: Results should clearly indicate "better" or "worse"
4. **Actionable**: Should guide which dedupe tasks to prioritize

### Nice-to-Haves

1. **Incremental**: Can be computed after each dedupe (not just full runs)
2. **Visual**: Could be plotted over time to show progress
3. **Predictive**: Could estimate impact of proposed dedupes before executing

### Validation

Metrics should detect known cases:
- **Good consolidation**: Press family (8→3 machines) should show improvement
- **Bad consolidation**: Hypothetical lathe→mill consolidation should show warning
- **No-op**: Consolidating items with zero usage should show minimal impact

---

## Proposed Metrics to Evaluate

Please analyze these candidate metrics and recommend which to implement:

### 1. Simple Node Count

**Definition**: Count of unique, non-deprecated items

**Formula**:
```
compactness_simple = (deprecated_items) / (total_items)
```

**Pros**: Trivial to compute, easy to interpret
**Cons**: Doesn't account for capability loss or reference consolidation

### 2. Reference Density

**Definition**: Ratio of unique items to total references

**Formula**:
```
reference_density = (unique_items_referenced) / (total_references)

Where:
- unique_items_referenced = distinct item IDs in all process inputs/outputs, BOM components
- total_references = sum of all input/output/component entries
```

**Pros**: Captures reference consolidation
**Cons**: May penalize legitimate multi-input processes

### 3. Canonical Coverage

**Definition**: Fraction of references pointing to non-deprecated items

**Formula**:
```
canonical_coverage = (refs_to_canonical_items) / (total_refs)
```

**Pros**: Directly measures cleanup progress
**Cons**: 100% achievable trivially (mark everything canonical)

### 4. Effective Machine Count

**Definition**: Weighted count of machines by usage

**Formula**:
```
effective_machines = sum(usage_weight(m) for m in machines)

Where usage_weight(m):
- 1.0 if used by processes
- 0.5 if has BOM but unused
- 0.1 if deprecated
- 0.0 if no BOM and unused
```

**Pros**: Distinguishes active from dead machines
**Cons**: Arbitrary weights, complex to explain

### 5. Graph Diameter / Average Path Length

**Definition**: Average shortest path length in dependency graph

**Formula**:
```
avg_path = mean(shortest_path(a, b) for all pairs a,b in graph)
```

**Pros**: Measures structural complexity
**Cons**: Expensive to compute (O(n²) or O(n³)), unclear interpretation

### 6. Capability Coverage

**Definition**: Ratio of distinct capabilities to machines providing them

**Formula**:
```
capability_coverage = (unique_capabilities) / (machines_providing_them)

e.g., if 3 machines all provide "grinding": coverage = 1/3 = 0.33
After consolidation to 1 machine: coverage = 1/1 = 1.0
```

**Pros**: Directly measures redundancy in capabilities
**Cons**: Requires parsing machine.capabilities[] lists

### 7. Recipe Simplicity

**Definition**: Average recipe length (number of steps)

**Formula**:
```
recipe_simplicity = mean(len(recipe.steps) for recipe in recipes)
```

**Pros**: Measures manufacturing complexity
**Cons**: Not directly related to deduplication (consolidation doesn't shorten recipes)

### 8. Mass Closure Ratio

**Definition**: Fraction of total system mass accounted for in BOMs

**Formula**:
```
mass_closure = (sum(bom_mass_recursive)) / (sum(machine.mass))

Where bom_mass_recursive computes full BOM tree including all components
```

**Pros**: Measures completeness of BOMs
**Cons**: Deduplication alone doesn't improve this (need BOM expansion)

---

## Expected Deliverables

Please provide:

### 1. Metric Recommendations (2-3 metrics)

Select 2-3 metrics from the list above (or propose new ones) that:
- Are practical to compute
- Clearly measure consolidation success
- Can detect over-consolidation or errors
- Are interpretable and actionable

For each metric, provide:
- **Name and definition**
- **Why it's useful** for measuring compactness
- **How to interpret** the values (higher/lower = better?)
- **Edge cases** or failure modes

### 2. Implementation Sketch

For each recommended metric, provide:
- **Pseudocode** or Python sketch showing how to compute it
- **Data sources** needed (which files to read, what to parse)
- **Computational complexity** (can it run in <1 second? <10 seconds?)

Example:
```python
def compute_canonical_coverage():
    """
    Measures what fraction of process/BOM references point to canonical (non-deprecated) items.
    Higher is better (1.0 = all refs cleaned up).
    """
    deprecated_ids = load_deprecated_items()  # Parse KB for DEPRECATED markers

    total_refs = 0
    canonical_refs = 0

    for process in load_all_processes():
        for input_item in process['inputs']:
            total_refs += 1
            if input_item['item_id'] not in deprecated_ids:
                canonical_refs += 1
        # ... same for outputs, byproducts

    for bom in load_all_boms():
        for component in bom['components']:
            total_refs += 1
            if component['item_id'] not in deprecated_ids:
                canonical_refs += 1

    return canonical_refs / total_refs if total_refs > 0 else 1.0
```

### 3. Validation Plan

Describe how to validate each metric using historical dedupe data:
- **Test case 1**: Press family consolidation (8→3 machines)
  - Expected metric change: [describe]
- **Test case 2**: Hypothetical bad consolidation (lathe→mill)
  - Expected metric change: [describe]
- **Test case 3**: No-op consolidation (unused duplicate)
  - Expected metric change: [describe]

### 4. Dashboard Mock

Propose a simple text-based dashboard showing metrics before/after dedupe runs:

```
KB Compactness Report (2024-12-18)
=====================================
Metric                    | Before | After  | Change
--------------------------|--------|--------|--------
Active Machines           | 89     | 67     | -22 (-24.7%)
Canonical Coverage        | 0.73   | 0.94   | +0.21
Capability Coverage       | 0.42   | 0.71   | +0.29
Deprecated Items          | 12     | 34     | +22
Total References          | 856    | 856    | 0

Interpretation:
- Consolidation removed 22 redundant machines
- 94% of references now point to canonical items (up from 73%)
- Each capability now averaged across fewer machines (less redundancy)
- No references were lost (total unchanged)
```

---

## Additional Context

### Example: Press Family Consolidation

**Before**:
```yaml
# 8 machines
- hydraulic_press (600 kg)
- hydraulic_press_small (150 kg)
- press_hydraulic (250 kg)
- hot_press_v0 (950 kg)
- power_hammer_or_press_v0 (200 kg)
- press_brake (1200 kg)
- press_brake_or_roller (300 kg)
- pressing_tools (150 kg)

# References scattered:
- bearing_installation_basic_v0: uses pressing_tools
- pressing_operations_basic_v0: uses power_hammer_or_press_v0
- metal_forming_basic_v0: uses press_hydraulic
- sintering_basic_v0: uses hot_press_v0
- sheet_metal_fabrication_v0: uses press_brake_or_roller
```

**After**:
```yaml
# 3 machines (5 deprecated)
- hydraulic_press (600 kg) - CANONICAL
- hot_press_v0 (950 kg) - CANONICAL (unique thermal capability)
- press_brake (1200 kg) - CANONICAL (unique sheet bending)

# References consolidated:
- bearing_installation_basic_v0: uses hydraulic_press
- pressing_operations_basic_v0: uses hydraulic_press
- metal_forming_basic_v0: uses hydraulic_press
- sintering_basic_v0: uses hot_press_v0
- sheet_metal_fabrication_v0: uses press_brake
```

**Metrics Change**:
- Active machines: 8 → 3 (62.5% reduction)
- References to deprecated: 5 → 0 (100% cleanup)
- Capabilities preserved: 3 distinct functions (general press, hot press, sheet brake)

### Example: Bad Consolidation (Hypothetical)

**If we incorrectly consolidated lathe into mill**:

**Before**:
```yaml
- milling_machine_cnc: capabilities [milling, drilling]
- precision_lathe: capabilities [turning, threading, boring]

# Processes using lathe:
- shaft_turning_v0: requires precision_lathe
- thread_cutting_v0: requires precision_lathe
```

**After (WRONG)**:
```yaml
- milling_machine_cnc: capabilities [milling, drilling, turning, threading]
- precision_lathe: DEPRECATED

# Processes now impossible:
- shaft_turning_v0: requires milling_machine_cnc (WRONG - mill can't do turning!)
- thread_cutting_v0: requires milling_machine_cnc (WRONG - mill can't thread!)
```

**Metric Detection**:
- A good metric should detect this by:
  - Flagging capability loss (turning, threading only on deprecated machine)
  - Warning about unrealistic super-machine (mill doing turning)
  - Noting that processes now reference wrong machine type

---

## Success Criteria for This Research

Your recommendations should:

1. **Be implementable** in <200 lines of Python
2. **Run quickly** (<30 seconds on full KB)
3. **Clearly show** impact of press consolidation (8→3) as positive
4. **Detect** hypothetical lathe→mill consolidation as suspicious/negative
5. **Guide prioritization** of remaining dedupe tasks

---

## Questions to Guide Your Analysis

1. Which metrics best balance **simplicity** (easy to compute) and **signal** (clearly indicate success)?

2. Should we use a **single composite metric** (e.g., weighted sum) or **multiple independent metrics** (dashboard)?

3. How do we **detect over-consolidation** (losing necessary distinctions)? Is this a separate metric or threshold on existing metrics?

4. Can any metrics **predict impact** of proposed dedupes before executing? (e.g., "consolidating these 3 crushers will improve canonical coverage by 5%")

5. Should metrics be **absolute** (counts) or **relative** (ratios/percentages)? Or both?

6. What **baselines** should we establish? (e.g., "ideal" compactness for a given manufacturing capability)

---

## Timeline and Next Steps

1. **Research Phase** (this document): Define metrics and validation plan
2. **Implementation Phase**: Code metrics computation script
3. **Baseline Phase**: Compute current KB metrics (before remaining dedupes)
4. **Validation Phase**: Verify metrics detect historical consolidations correctly
5. **Production Phase**: Integrate into dedupe agent workflow (agents report metrics before/after)

Please focus on Phase 1 (research and recommendations) in your response.

---

## References

- `design/meta-memo.md` - Project philosophy and goals
- `design/memo_a.md` - KB schema and data model
- `docs/dedupe_decisions.md` - Historical consolidation decisions
- `out/index.json` - Current KB index
- `kbtool/indexer.py` - How KB is validated and indexed
