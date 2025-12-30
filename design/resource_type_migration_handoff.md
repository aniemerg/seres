NOTE: Historical document predating ADR-012+; references deprecated schema. See docs/kb_schema_reference.md for current rules.

# Resource Type Migration - Work Handoff

**Date**: 2025-12-22
**Status**: Ready for implementation
**Priority**: High (blocks closure analysis)
**Estimated Effort**: 2-4 hours

## Executive Summary

The KB has 98 "orphan resource types" blocking tech tree closure analysis. This is a migration artifact from an incomplete schema refactor (ADR-003, Dec 18, 2025). The migration from abstract `resource_type` references to concrete `machine_id` references was started but never completed.

**Quick Fix Recommended**: Create generic machines for common resource types rather than completing full migration. This unblocks closure analysis while preserving flexibility for future refactoring.

---

## Background

### Original Design (Before ADR-003)

Processes referenced abstract "resource types":
```yaml
# Process file (OLD schema)
resource_requirements:
  - resource_type: assembly_station
    amount: 2.0
    unit: hr
```

Separate resource type definition files existed:
```yaml
# kb/resources/assembly_station.yaml
id: assembly_station
kind: resource_type
capabilities: ["assembly"]
```

Machines declared abstract capabilities:
```yaml
# Machine file (OLD schema)
capabilities:
  - assembly
  - welding
```

### Intended Design (ADR-003 - Incomplete)

Processes should reference specific machines:
```yaml
# Process file (NEW schema)
resource_requirements:
  - machine_id: labor_bot_general_v0  # concrete machine reference
    qty: 2.0
    unit: hr
```

Machines should declare supported processes:
```yaml
# Machine file (NEW schema)
processes_supported:
  - assembly_process_v0
  - welding_process_v0
```

Resource type files should be deleted (no longer needed).

### Current State (Migration Stalled)

- ✅ Schema updated in `kbtool/models.py` (accepts both old and new via alias)
- ❌ 73 resource type files still exist in `kb/resources/`
- ❌ Many process files still use `resource_type:` field
- ❌ Indexer still reports "orphan resources"
- ❌ Migration never completed

**Result**: 98 resource types have no machine provider, blocking validation.

---

## The Problem

The indexer reports 98 "orphan resource types" - these are abstract resource definitions that no concrete machine claims to provide. This blocks:

1. **Closure analysis** - Can't determine which machines are needed
2. **Simulation validation** - Can't verify all processes have available machines
3. **Dependency graphing** - Can't trace machine → process relationships

### Why This Happened

ADR-003 proposed a breaking schema change but:
- Migration script was never written
- Process files were never updated
- Resource files were never deleted
- Work was paused mid-migration

---

## Files to Review (MUST READ BEFORE STARTING)

### Documentation Files

**Primary:**
1. **`docs/ADRs/003-process-machine-refactor.md`** (386 lines)
   - Complete specification of intended migration
   - Schema changes, examples, migration strategy
   - Read this FIRST - it's the source of truth

**Supporting:**
2. **`docs/parts_and_labor_guidelines.md`** (479 lines)
   - Official policy on parts/machines
   - Section on "consumables vs machines"
   - Understand what goes in inputs vs resource_requirements

3. **`design/memo_a.md`** (645 lines)
   - Core KB specification
   - Search for "Process" and "resource_requirements"
   - Understand the data model

4. **`docs/README.md`**
   - Workflow overview
   - How agents interact with KB

### Python Code Files

5. **`kbtool/models.py`** (157 lines)
   - Data models (Pydantic)
   - Lines 37-48: `Requirement` class - note the alias on line 43
   - Lines 100-117: `Item` class - see capabilities vs processes_supported
   - Lines 119-128: `ResourceType` class

6. **`kbtool/indexer.py`** (680 lines)
   - Lines 313-325: Orphan resource detection logic
   - Lines 112-114: BOM reference extraction
   - Understand how refs_in/refs_out work

### KB Data Files (Sample)

7. **`kb/resources/assembly_station.yaml`** (any file from kb/resources/)
   - See what resource type definitions look like
   - 73 total files to eventually handle

8. **`kb/processes/` (sample 3-5 files)**
   - Search for `resource_type:` to see old schema usage
   - Example: `kb/processes/ball_milling_v0.yaml`

9. **`kb/items/machines/3d_printer_basic_v0.yaml`**
   - Example machine with `capabilities` and `processes_supported`
   - Shows current machine schema

### Output Files (Generated)

10. **`out/orphan_resources.jsonl`**
    - List of all 98 orphan resource types
    - Each entry shows which processes need it

11. **`out/validation_report.md`**
    - Current gap summary
    - Section on "Orphan resources"

12. **`out/index.json`** (2.6 MB)
    - Full dependency graph
    - Search for a specific resource_type to see refs_in

---

## Proposed Solution: Quick Fix (Recommended)

**Instead of completing full ADR-003 migration**, create generic machines to satisfy orphan resource types.

### Approach

1. **Analyze the 98 orphan resources** - group by pattern:
   - `assembly_*` → Assembly-related resources
   - `reactor_*` → Chemical reactor types
   - `labor_bot_*` → Labor bot types
   - `tools_*` → Tool sets

2. **Create generic machines** for each common pattern:
   - `machine_assembly_station_v0` → provides assembly capability
   - `machine_chemical_reactor_basic_v0` → provides chemical processing
   - `machine_labor_bot_general_v0` → provides general labor

3. **Link machines to resource types** via `processes_supported`:
   - Scan all processes that need each resource_type
   - Add those process IDs to the machine's `processes_supported` list

4. **Create minimal BOMs** for generic machines:
   - Simple placeholder BOMs (will be refined later)
   - Mark as `notes: "Generic machine - BOM needs refinement"`

5. **Re-index and validate**:
   - Orphan resource count should drop to near zero
   - Some may remain as truly missing machines

### Why This Approach?

- ✅ **Fast** - Can be done in 2-4 hours
- ✅ **Unblocks closure analysis** - Machines now exist for all processes
- ✅ **Preserves flexibility** - Can refactor to specific machines later
- ✅ **Non-breaking** - Old process files still work (alias in schema)
- ✅ **Incremental** - Can migrate specific processes over time

---

## Implementation Steps

### Step 1: Analyze Orphan Resources (30 min)

```bash
# Load orphan resources
cat out/orphan_resources.jsonl | jq -r '.id' | sort > /tmp/orphans.txt

# Group by pattern
grep "assembly" /tmp/orphans.txt
grep "reactor" /tmp/orphans.txt
grep "labor" /tmp/orphans.txt
grep "tools" /tmp/orphans.txt
# ... etc
```

**Output**: Create `design/orphan_resource_analysis.md` with:
- List of all 98 resources
- Grouped by pattern (assembly, reactor, labor, tools, etc.)
- Count of how many processes need each
- Proposed generic machine for each group

### Step 2: Create Generic Machines (1-2 hours)

For each generic machine:

**Create machine YAML** in `kb/items/machines/`:
```yaml
# kb/items/machines/machine_assembly_station_v0.yaml
id: machine_assembly_station_v0
name: Generic Assembly Station
kind: machine
mass: 500.0
unit: kg
bom: bom_assembly_station_v0

# List all processes that need "assembly_station" resource_type
processes_supported:
  - assembly_process_basic_v0
  - fastener_assembly_v0
  # ... (get from orphan_resources.jsonl refs_in)

capabilities:  # deprecated but keep for compatibility
  - assembly

notes: |
  Generic machine created to satisfy resource_type: assembly_station.
  This is a placeholder machine - refine BOM and specifications as needed.
  Supports all processes that previously referenced assembly_station resource.
```

**Create BOM** in `kb/boms/`:
```yaml
# kb/boms/bom_assembly_station_v0.yaml
id: bom_assembly_station_v0
target_item_id: machine_assembly_station_v0
variant_id: v0

parts:
  - item_id: structural_frame_medium
    qty: 1
    unit: ea
  - item_id: motor_electric_small
    qty: 2
    unit: ea
  - item_id: controller_basic
    qty: 1
    unit: ea
  - item_id: fastener_kit_medium
    qty: 1
    unit: ea

notes: |
  Placeholder BOM for generic assembly station.
  Needs refinement based on actual assembly requirements.
```

**Create recipe** in `kb/recipes/` (optional but recommended):
```yaml
# kb/recipes/recipe_assembly_station_v0.yaml
id: recipe_assembly_station_v0
target_item_id: machine_assembly_station_v0
variant_id: v0

steps:
  - process_id: frame_fabrication_medium_v0
    est_time_hr: 4.0
  - process_id: motor_assembly_small_v0
    est_time_hr: 2.0
  - process_id: machine_assembly_basic_v0
    est_time_hr: 6.0

notes: |
  Placeholder recipe for generic assembly station.
  Refine based on actual manufacturing process.
```

### Step 3: Build processes_supported Lists (30 min)

For each generic machine, populate `processes_supported`:

```python
# Helper script: scripts/build_processes_supported.py
import json

# Load orphan resources
with open('out/orphan_resources.jsonl') as f:
    orphans = [json.loads(line) for line in f]

# For each orphan, get processes that need it
for orph in orphans:
    resource_id = orph['id']
    needed_by = orph.get('refs_in', [])

    print(f"\n# {resource_id}")
    print(f"# Needed by {len(needed_by)} processes")
    print("processes_supported:")
    for proc_id in needed_by[:20]:  # limit to first 20
        print(f"  - {proc_id}")
```

**Run script and copy output into machine YAML files.**

### Step 4: Re-index and Validate (10 min)

```bash
# Re-run indexer
.venv/bin/python -m kbtool index

# Check results
cat out/validation_report.md

# Expected: Orphan resource count should be 0 or near-zero
# Remaining orphans = truly missing machines that need definition
```

### Step 5: Document Results (20 min)

Create `docs/generic_machines_created.md`:
- List of all generic machines created
- Mapping from resource_type → machine_id
- Known limitations (placeholder BOMs, etc.)
- Future work (refine BOMs, split into specific machines)

---

## Success Criteria

**Must Have:**
- [ ] Orphan resource count < 10 (down from 98)
- [ ] Generic machines created for all common patterns
- [ ] All generic machines have BOMs (even if placeholder)
- [ ] Re-index completes without errors
- [ ] Documentation updated

**Nice to Have:**
- [ ] Generic machines have realistic BOMs
- [ ] Recipes created for generic machines
- [ ] All 98 orphans resolved (not just common ones)

---

## Alternative: Full ADR-003 Migration (Not Recommended Now)

If you want to complete the full migration instead:

1. **Write migration script** `scripts/migrate_resource_types.py`:
   - Scan all process YAML files
   - Replace `resource_type:` → `machine_id:`
   - Replace `amount:` → `qty:`
   - For each resource_type, map to specific machine

2. **Define resource_type → machine_id mapping**:
   - `assembly_station` → `labor_bot_general_v0` (?)
   - `chemical_reactor_basic` → `chemical_reactor_v0` (?)
   - Requires domain knowledge / manual decisions

3. **Delete 73 resource files**:
   - `rm kb/resources/*.yaml`

4. **Update indexer**:
   - Remove orphan resource detection (lines 313-325)
   - Update validation to check machine_id refs

5. **Test and validate**:
   - Re-index
   - Fix broken references
   - Update documentation

**Estimated effort**: 8-16 hours (vs 2-4 for quick fix)

**Risk**: High - breaking change, many files to update, easy to introduce errors

**Recommendation**: Do quick fix now, full migration later when needed.

---

## Common Pitfalls

1. **Don't create machines without BOMs** - indexer will flag them
2. **Don't forget to link machine → processes** - populate processes_supported
3. **Don't delete resource files yet** - processes still reference them via alias
4. **Don't assume one resource = one machine** - some resources may need multiple machines
5. **Check for duplicates** - some generic machines may already exist

---

## Questions to Answer During Implementation

1. Which orphan resources can share a generic machine?
   - Example: `assembly_station`, `assembly_workbench`, `assembly_tools_basic` → one machine?

2. Should generic machines be v0 or have different naming?
   - Recommendation: Use v0 to indicate "placeholder/generic"

3. What should generic machine BOMs contain?
   - Minimum: frame, motors, controller, fasteners
   - Can be refined later based on actual requirements

4. Should we create recipes for generic machines?
   - Yes if time permits - helps with closure analysis
   - No if rushing - can add later

---

## After This Work Is Done

Next steps for closure analysis:

1. **Build analyze-closure tool** - trace machine → parts → materials
2. **Identify minimum import set** - which items can't be manufactured
3. **Run extended simulation** - validate end-to-end production
4. **Refine generic machines** - split into specific machines as needed

---

## Files You'll Create/Modify

**New Files:**
- `kb/items/machines/machine_assembly_station_v0.yaml` (and ~10-20 others)
- `kb/boms/bom_assembly_station_v0.yaml` (and ~10-20 others)
- `kb/recipes/recipe_assembly_station_v0.yaml` (optional, ~10-20 others)
- `design/orphan_resource_analysis.md` (analysis output)
- `docs/generic_machines_created.md` (documentation)

**Modified Files:**
- None (quick fix doesn't modify existing files)

**Deleted Files:**
- None (don't delete resource files yet - backward compatibility)

---

## Validation Commands

```bash
# Before starting - baseline metrics
.venv/bin/python -m kbtool index
cat out/validation_report.md | grep "Orphan resources"
# Should show: "Total: 98 resource_types have no provider machine"

# After creating machines - check progress
.venv/bin/python -m kbtool index
cat out/validation_report.md | grep "Orphan resources"
# Should show: "Total: < 10 resource_types have no provider machine"

# Check specific orphan
cat out/orphan_resources.jsonl | jq 'select(.id == "assembly_station")'

# Check machine was created
cat out/index.json | jq '.entries.machine_assembly_station_v0'
```

---

## Context for Understanding

**Why abstract resource types existed:**
- Early design when KB was small
- Easier to say "needs assembly station" than specify exact machine
- Flexibility to swap machines

**Why ADR-003 wanted to remove them:**
- Adds indirection layer
- Can't validate if machines actually exist
- Harder to trace dependencies
- Duplicates information (resource files + machine capabilities)

**Why we're doing quick fix instead:**
- Full migration is high effort, high risk
- Quick fix unblocks closure analysis (main goal)
- Can refactor later if needed
- Preserves backward compatibility

**The key insight:**
The schema already supports both old and new (via alias). We don't need to migrate process files - we just need to create the missing machines that resource types were pointing to.

---

## References

- ADR-003: Process-Machine Schema Harmonization (Draft)
- Material Class System Implementation (Dec 20, 2025)
- Parts and Labor Guidelines (Official Policy)
- Base Builder Simulation (ADR-004)

---

## Need Help?

If stuck:
1. Re-index and check `out/validation_report.md`
2. Read ADR-003 section on "Examples After Migration"
3. Look at existing machines for BOM/recipe patterns
4. Ask questions about resource_type → machine_id mapping

Good luck! This work directly enables closure analysis - the main goal.
