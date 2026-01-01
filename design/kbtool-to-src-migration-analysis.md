# kbtool/ to src/ Migration Analysis

**Date:** 2025-12-30
**Status:** Critical - Incomplete Migration Discovered
**Related Issues:** Abstract inputs/outputs, reference validation gaps

## Executive Summary

The codebase has TWO parallel implementations:
- **kbtool/** - Original implementation (DEPRECATED but still in use!)
- **src/** - New Pydantic-based implementation (INCOMPLETE)

**Critical Issue:** The CLI (`src/cli.py`) still calls the deprecated `kbtool/indexer.py`, which means:
1. We're not using the new src/ infrastructure fully
2. Reference validation logic is split between old and new code
3. Migration is incomplete and inconsistent

## Current State Analysis

### What's in kbtool/ (Deprecated)

| File | Size | Purpose | Migration Status |
|------|------|---------|------------------|
| **indexer.py** | 55KB | Main indexer, reference tracking, gap detection | ❌ NOT MIGRATED |
| **queue_tool.py** | 14KB | Work queue management, add_gap(), lease system | ❌ NOT MIGRATED |
| **circular_dependency_fixer.py** | 14KB | Circular dependency detection and fixing | ❌ NOT MIGRATED |
| **closure_analysis.py** | 25KB | Material closure analysis for machines | ✅ MIGRATED to src/indexer/closure_analysis.py |
| **auto_fix.py** | 6KB | Auto-fix CLI for validation issues | ✅ MIGRATED to src/kb_core/auto_fixer.py |
| **dedupe_tool.py** | 5KB | Deduplication queue management | ❌ NOT MIGRATED |
| **config.py** | 5KB | Configuration management | ❌ NOT MIGRATED |
| **models.py** | 5KB | Data models (likely superseded by schema.py) | ✅ SUPERSEDED by src/kb_core/schema.py |
| **report.py** | 2KB | Report generation | ❌ NOT MIGRATED |

### What's in src/ (New)

| Directory | Files | Purpose |
|-----------|-------|---------|
| **kb_core/** | kb_loader.py | KB loading with Pydantic models |
| | schema.py | Pydantic schemas (RawProcess, Process, etc.) |
| | validators.py | ADR-017 validation rules |
| | unit_converter.py | Unit conversion logic |
| | auto_fixer.py | Auto-fix engine (migrated) |
| | calculations.py | Energy/time calculations |
| **indexer/** | closure_analysis.py | Closure analyzer (migrated) |
| **simulation/** | engine.py | Simulation engine with recipe resolution |
| | models.py | Simulation data models |

## Critical Gap: Indexer Not Migrated

### The Problem

`src/cli.py:155-157`:
```python
if args.command == 'index':
    from kbtool.indexer import main as index_main  # ← CALLS DEPRECATED CODE!
    return index_main()
```

**The CLI is still calling the old kbtool/indexer.py!**

### What kbtool/indexer.py Does (That's Missing in src/)

1. **Reference Tracking** (lines 373-471):
   - Builds graph of all item references
   - Identifies "referenced_only" items (referenced but not defined)
   - Creates entries with `status: "referenced_only"`

2. **Recipe Item Analysis** (lines 207-308):
   - `_analyze_recipe_items()` - Finds items referenced in recipes but not defined
   - Classifies missing items:
     - `missing_recipe_target` - recipe target not defined
     - `missing_intermediate_part` - used in multiple recipes but not defined
     - `pure_intermediate` - used in one recipe
     - `missing_recipe_input` - consumed but not produced
     - `unused_recipe_output` - produced but not consumed

3. **Gap Detection and Work Queue** (lines 993-1025):
   - Enqueues "no_recipe" gaps for items without manufacturing routes
   - Enqueues "import_stub" gaps for import-only recipes
   - Filters out `is_import: true` items from gaps (lines 480-498)
   - **This is where is_template filtering should go!**

4. **Validation Integration** (lines 578-580):
   - Calls `_collect_validation_issues()` using src/kb_core/validators.py
   - Merges ADR-017 validation with indexer gaps

5. **Output File Generation**:
   - `out/index.json` - Full KB index with references
   - `out/unresolved_refs.jsonl` - Unresolved reference strings
   - `out/missing_recipe_items.jsonl` - Recipe items not defined
   - `out/work_queue.jsonl` - All gaps needing attention
   - `out/validation_report.md` - Human-readable report

### What's NOT in src/ Yet

**Missing components:**

1. **Index Builder** (should be `src/kb_core/index_builder.py` or `src/indexer/index_builder.py`):
   - Reference graph construction
   - "referenced_only" node creation
   - Recipe item analysis
   - Gap detection logic

2. **Queue Manager** (should be `src/kb_core/queue_manager.py`):
   - Work queue persistence
   - `add_gap()` function
   - Queue filtering logic
   - Lease system for distributed workers

3. **Dependency Analyzer** (should be `src/kb_core/dependency_analyzer.py`):
   - Circular dependency detection
   - Automatic import marking
   - Dependency graph analysis

4. **Deduplicator** (should be `src/kb_core/deduplicator.py`):
   - Duplicate detection
   - Dedupe queue management

## Reference Validation: Where Is It?

### Current State (Fragmented)

**In kbtool/indexer.py:**
- Line 270-273: Checks if items in recipes are defined
- Line 456-471: Creates "referenced_only" nodes for undefined items
- **Does NOT validate process inputs/outputs in isolation**

**In src/indexer/closure_analysis.py:**
- Line 315-316: Checks if process exists when expanding recipe
- Line 341-343: Recursively validates process inputs during expansion
- Line 345-346: Reports missing process
- **Only runs during machine closure analysis!**

**In src/kb_core/validators.py:**
- Line 401-414: Validates `scaling_basis` exists in process inputs/outputs
- **Does NOT check if those item_ids exist in KB!**

### The Gap

**Process inputs/outputs are NOT validated for item existence unless:**
1. The process is used in a recipe, AND
2. The recipe is used in a machine BOM, AND
3. Closure analysis is run on that machine

**Standalone processes** with undefined items are never caught!

## Migration Priority and Plan

### Phase 1: Critical - Index Builder (URGENT)

**Create `src/kb_core/index_builder.py`:**

1. **Migrate reference tracking from kbtool/indexer.py:373-471**
   - Port `_build_entry_graph()` logic
   - Port "referenced_only" node creation
   - Use src/kb_core/kb_loader.py for loading

2. **Migrate recipe item analysis from kbtool/indexer.py:207-308**
   - Port `_analyze_recipe_items()`
   - Use Pydantic models from schema.py

3. **Integrate with validation**
   - Use src/kb_core/validators.py for ADR-017 validation
   - Merge validation issues with gap detection

4. **Add process input/output validation (NEW)**
   - For each process, check if all input/output item_ids exist in KB
   - Respect `is_template` flag (allow undefined items in templates)
   - Report as ERROR-level validation issue

**Effort:** 2-3 days
**Risk:** Medium (core functionality but well-understood)
**Value:** Critical - enables proper reference validation

### Phase 2: Important - Queue Manager

**Create `src/kb_core/queue_manager.py`:**

1. **Migrate queue management from kbtool/queue_tool.py**
   - Port `add_gap()`, `_load_queue()`, `_save_queue()`
   - Port `_locked_queue()` context manager
   - Keep JSONL format for backward compatibility

2. **Migrate gap detection from kbtool/indexer.py:993-1025**
   - Port `_update_work_queue()` logic
   - Port is_import filtering (lines 480-498)
   - Add is_template filtering (new)

3. **Migrate filtering logic**
   - Port priority filtering
   - Port gap type categorization

**Effort:** 1-2 days
**Risk:** Low (mostly data management)
**Value:** High - needed for workflow automation

### Phase 3: Medium - Dependency Analyzer

**Create `src/kb_core/dependency_analyzer.py`:**

1. **Migrate from kbtool/circular_dependency_fixer.py**
   - Port circular dependency detection
   - Port automatic import marking
   - Integrate with queue manager

**Effort:** 1-2 days
**Risk:** Medium (complex graph algorithms)
**Value:** Medium - nice to have but not critical

### Phase 4: Low - Deduplicator

**Create `src/kb_core/deduplicator.py`:**

1. **Migrate from kbtool/dedupe_tool.py**
   - Port dedupe detection
   - Port dedupe queue management

**Effort:** 1 day
**Risk:** Low
**Value:** Low - optimization feature

### Phase 5: Cleanup

1. **Remove kbtool/** entirely
2. **Update all imports** to use src/
3. **Update documentation** and ADRs
4. **Delete deprecated code**

## Validation Approaches Comparison

### Old (kbtool/indexer.py)

**Approach:**
- Parse all YAML files permissively
- Build reference graph
- Detect gaps and missing items
- Generate work queue

**Strengths:**
- Comprehensive gap detection
- Reference tracking across entire KB
- Work queue for automation

**Weaknesses:**
- Doesn't use Pydantic validation
- Mixes parsing, validation, and gap detection
- Hard to unit test

### New (src/kb_core/validators.py)

**Approach:**
- Validate individual entities against schema
- Check ADR-017 rules (process_type, energy/time models)
- Return structured ValidationIssue objects

**Strengths:**
- Clean separation of concerns
- Type-safe with Pydantic
- Easy to test individual rules
- Structured error reporting

**Weaknesses:**
- Doesn't track references across KB
- Doesn't validate item existence
- No gap detection

### Hybrid (Recommended)

**Combine both approaches:**

1. **src/kb_core/validators.py** - Entity-level validation
   - Schema compliance (ADR-017)
   - Internal consistency
   - Keep current rule-based system

2. **src/kb_core/index_builder.py** - KB-wide validation (NEW)
   - Reference tracking
   - Item existence validation
   - Gap detection
   - Work queue generation

3. **src/kb_core/queue_manager.py** - Queue management (NEW)
   - Persistent work queue
   - Filtering and prioritization
   - Integration with validators and index builder

## Impact on is_template Implementation

### What We Now Know

1. **is_template filtering must go in index_builder.py**
   - Follow the `is_import` pattern from kbtool/indexer.py:480-498
   - Check `is_template` when loading processes
   - Skip template processes from "no_recipe" gap enqueue

2. **Reference validation needs to be aware of templates**
   - Template processes can reference undefined items
   - Non-template processes should ERROR if items undefined
   - This check belongs in the new index_builder.py

3. **Queue API is in kbtool/queue_tool.py (deprecated)**
   - Need to migrate to src/kb_core/queue_manager.py first
   - Or use deprecated queue_tool.py temporarily

### Updated Implementation Plan for is_template

**Phase 1: Schema (Day 1)**
1. Add `is_template: Optional[bool] = None` to RawProcess and Process
2. Update schema.py

**Phase 2: Migrate Index Builder (Days 2-3)**
3. Create src/kb_core/index_builder.py
4. Migrate reference tracking from kbtool/indexer.py
5. Add process input/output validation with is_template awareness
6. Add is_template filtering for gap enqueue

**Phase 3: Migrate Queue Manager (Day 4)**
7. Create src/kb_core/queue_manager.py
8. Migrate queue management from kbtool/queue_tool.py
9. Integrate with index_builder

**Phase 4: Update CLI (Day 5)**
10. Update src/cli.py to use new src/kb_core/index_builder.py
11. Deprecate kbtool/indexer.py call
12. Test full indexing pipeline

**Phase 5: Mark Templates and Document (Day 5)**
13. Mark existing placeholder processes with is_template: true
14. Add ADR documenting the pattern
15. Update validation reports

## Immediate Next Steps

1. **Create migration plan ADR** documenting this analysis
2. **Decide on migration approach:**
   - Option A: Migrate everything now (1 week effort)
   - Option B: Migrate index_builder only, keep using kbtool temporarily
   - Option C: Implement is_template in kbtool first, migrate later

3. **Update src/cli.py** to show deprecation warning when using kbtool

4. **Create GitHub issues** for each migration component

## Questions for Discussion

1. **Should we migrate kbtool → src now, or implement is_template in kbtool first?**
   - Pro migrate: Clean architecture, future-proof
   - Pro kbtool: Faster implementation, less risky

2. **What's the migration deadline?**
   - Is this blocking other work?
   - Can we schedule dedicated migration sprint?

3. **Should we keep kbtool/ after migration?**
   - Delete entirely?
   - Keep as reference?
   - Archive to old/ directory?

4. **How to handle backward compatibility?**
   - Keep JSONL output format?
   - Keep queue file format?
   - Support both APIs during transition?

## Conclusion

The kbtool → src migration is **incomplete and critical**. The CLI still uses deprecated code, which explains why we found reference validation in unexpected places.

**Recommended path:**
1. Create src/kb_core/index_builder.py (3 days)
2. Create src/kb_core/queue_manager.py (2 days)
3. Update CLI to use new code (1 day)
4. Implement is_template in new code (1 day)
5. Delete kbtool/ (1 day)

**Total effort:** ~1.5 weeks for complete migration + is_template implementation

Alternative: Implement is_template in kbtool first (~2 days), schedule migration separately (~1 week).
