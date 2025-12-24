# Closure Analysis Integration Summary - 2024-12-24

## Overview

Integrated closure analysis errors into the work queue so that material flow problems detected during closure analysis are automatically added as queue items for fixing.

## Changes Made

### 1. Added Closure Error Collection (kbtool/indexer.py:628-723)

Created `_collect_closure_errors()` function that:
- Runs closure analysis on all machines in the KB
- Collects all errors generated during material flow tracing
- Deduplicates errors by signature (gap_type + item_id)
- Categorizes errors into specific gap types
- Writes results to `out/closure_errors.jsonl`

### 2. Error Classification

Closure errors are classified into specific gap types:

| Gap Type | Description | Example |
|----------|-------------|---------|
| `null_quantity` | Process input/output has null/zero qty | "Process 'welding_v0' input 'metal' has null quantity" |
| `item_not_found` | Item referenced but not defined in KB | "Item 'xyz' not found in KB" |
| `no_recipe` | Item has no recipe and is not raw material | "Item 'part_a' has no recipe and is not a raw material" |
| `recipe_not_found` | Recipe referenced but not found | "Recipe 'recipe_xyz' not found for item 'abc'" |
| `process_not_found` | Process referenced but not found | "Process 'machining_v0' referenced in recipe not found" |
| `recipe_no_inputs` | Recipe has no material inputs defined | "Recipe 'recipe_abc' has no inputs" |
| `closure_error` | Other closure analysis errors | (catch-all) |

### 3. Deduplication Strategy

Each error is deduplicated by signature:
```python
signature = f"{gap_type}:{item_id or recipe_id or process_id}"
```

This ensures that if the same process has null quantities and is used in 100 different machines, it only appears once in the queue.

### 4. Queue Item Format

Each closure error queue item includes:

```json
{
  "id": "closure:null_quantity:process_name",
  "kind": "gap",
  "reason": "null_quantity",
  "gap_type": "null_quantity",
  "item_id": "process_name",
  "context": {
    "error_message": "Full error message from closure analyzer",
    "detected_in_machine": "machine_id_where_error_occurred",
    "item_id": "extracted_item_id",
    "recipe_id": "extracted_recipe_id",
    "process_id": "extracted_process_id"
  }
}
```

### 5. Integration into Indexer

Modified `build_index()` to:
1. Load KB with `KBLoader` (line 568-569)
2. Run closure analysis on all machines (line 572-574)
3. Pass closure errors to `_update_work_queue()` (line 580)

Modified `_update_work_queue()` to:
1. Accept `closure_errors` parameter (line 745)
2. Add closure errors to `gap_items` list (line 772-773)

## Results

### Before Integration
- Queue: 20 items
- Only structural gaps detected (circular deps, missing recipes, etc.)
- Closure analysis errors printed to stdout but not actionable

### After Integration
- Queue: 305 items
- **287 new closure errors** added to queue
- All closure problems now trackable and fixable

### Queue Breakdown

```
recipe_no_inputs      148  (recipes with no inputs detected by closure)
null_quantity          54  (process inputs/outputs with null quantities)
item_not_found         35  (items referenced but not defined)
no_recipe              26  (items with no recipe and not raw materials)
closure_error          24  (other closure analysis errors)
circular_dependency     7  (recycling loops and chemistry cycles)
recipe_not_found        4  (recipes referenced but not found)
import_stub             4  (import placeholders)
process_not_found       2  (processes referenced but not found)
referenced_only         1  (items referenced but not defined)
```

## Output Files

1. **out/closure_errors.jsonl** - All unique closure errors (287 items)
2. **out/work_queue.jsonl** - Complete work queue including closure errors (305 items)
3. **out/material_closure_analysis.txt** - Full closure analysis report

## Example Errors Captured

### Null Quantity Error
```json
{
  "gap_type": "null_quantity",
  "item_id": "welding_brazing_basic_v0",
  "context": {
    "error_message": "Process 'welding_brazing_basic_v0' (in recipe 'recipe_printer_frame_generic_v0') input 'cast_metal_parts' has null/zero quantity",
    "detected_in_machine": "3d_printer_basic_v0",
    "process_id": "welding_brazing_basic_v0"
  }
}
```

### Recipe No Inputs Error
```json
{
  "gap_type": "recipe_no_inputs",
  "item_id": "recipe_abc_v0",
  "context": {
    "error_message": "Recipe 'recipe_abc_v0' for 'item_abc' has no inputs",
    "detected_in_machine": "machine_xyz"
  }
}
```

## Performance

- **Indexing time**: ~2-3 seconds (including closure analysis)
- **Machines analyzed**: 344 machines
- **Errors found**: 287 unique errors
- **Deduplication**: Thousands of duplicate errors reduced to 287 unique items

## Benefits

1. **Visibility**: Closure errors no longer hidden in stdout, now in actionable queue
2. **Prioritization**: Can filter and prioritize closure errors by gap type
3. **Tracking**: Each error is tracked with full context (machine, recipe, process)
4. **Deduplication**: No duplicate work - each root cause appears once
5. **Integration**: Works seamlessly with existing queue workflow

## Next Steps

1. ✅ Closure errors integrated into queue
2. Work through queue systematically (305 items)
3. Focus on high-impact gaps (null_quantity, recipe_no_inputs)
4. Use autonomous queue agents to process items
5. Track progress via queue status

## Conservative Mode Compliance

All changes follow Conservative Mode principles:
- ✅ Minimal code changes (added one function, modified two call sites)
- ✅ Non-breaking (added optional parameter to existing function)
- ✅ Deduplicated (no redundant queue items)
- ✅ Context-rich (full error messages and source tracking)
- ✅ Documented (this summary + code comments)
