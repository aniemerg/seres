# Queue Agent Prompt Structure Analysis

## Overview

The queue worker agent is rebuilt **fresh for each queue item** (after the optimization), but still accumulates conversation history across iterations within a single item.

## Prompt Structure Breakdown

### 1. SYSTEM MESSAGE (Static, Cached)

Built in `build_agent()` at line 394-416:

```python
full_instructions = f"{cached_context}\n\n---\n\n{AGENT_INSTRUCTIONS}"
```

**Components:**

#### A. cached_context.md (~1,039 lines)
- **Static content**: Loaded once from `queue_agents/cached_context.md`
- **Size**: ~7,000-8,000 tokens (estimated)
- **Contents**:
  - Agent reference memo (KB creation guide)
  - Core principles and design philosophy
  - Schema reference for all KB item types (materials, parts, machines, processes, BOMs, recipes)
  - Complex examples showing proper YAML structure
  - Papers directory reference
  - Queue workflow documentation

#### B. AGENT_INSTRUCTIONS (~112 lines)
- **Static content**: Hardcoded in worker.py lines 66-112
- **Size**: ~300-400 tokens (estimated)
- **Contents**:
  - Goal: "Make necessary changes to resolve this gap completely"
  - Process steps (research, edit, validate, check, give up)
  - Note: validation runs the indexer internally (same as `queue complete --verify`)
  - Output format instructions
  - Important notes

**Total Static System Message**: ~7,500-8,500 tokens ✓ CACHED

---

### 2. USER MESSAGE - ITERATION 1 (Variable)

Constructed at lines 482-487:

```python
if iteration == 1:
    input_with_lease = (
        f"{user_input}\n\n"
        f"Queue item leased:\n```json\n{json.dumps(lease_result, indent=2)}\n```"
    )
```

**Components:**

#### A. Static Prefix
```
Please process the queue item that has been leased for you.
```
- **Size**: ~15 tokens ✓ STATIC (but in user message, so not fully cacheable)

#### B. Variable Lease Data
```json
{
  "available": true,
  "id": "no_recipe:knob_control_dial_v0",
  "gap_type": "no_recipe",
  "context": {
    "file": "kb/items/parts/knob_control_dial_v0.yaml"
  },
  "item_id": "knob_control_dial_v0",
  "kind": "part",
  "status": "pending"
}
```
- **Size**: ~100-300 tokens ✗ VARIABLE (changes per item)
- **Content**: item_id, gap_type, context (file path, description, etc.)

**Total User Message 1**: ~115-315 tokens (mostly variable)

---

### 3. ASSISTANT RESPONSE - ITERATION 1 (Variable)

The agent's response to the first user message.

**Components:**
- Reasoning output (if enabled)
- Text responses explaining plan
- Tool calls (rg_search, read_file, write_file, run_indexer)
- Each tool call has arguments

**Size**: ~1,000-5,000 tokens ✗ VARIABLE

---

### 4. TOOL RESULTS - ITERATION 1 (Variable)

Results from all tool calls made in iteration 1.

**Components:**
- Search results (file paths, matches)
- File contents (YAML files can be 50-500 lines each)
- Indexer output (validation results, errors)

**Size**: ~500-10,000 tokens ✗ VARIABLE
- Simple items: 500-2,000 tokens
- Complex items with many searches/reads: 5,000-10,000 tokens

---

### 5. USER MESSAGE - ITERATION 2 (Variable, if needed)

If indexer fails OR gap persists, constructed at lines 524-527 or 542-545:

**Case A: Indexer failed**
```python
user_input = (
    f"The indexer failed with errors. Please fix them:\n"
    f"{chr(10).join(indexer_result['errors'][:10])}"
)
```

**Case B: Gap persists**
```python
user_input = (
    "The indexer passed but the gap still exists in out/work_queue.jsonl. "
    "Please continue working to fully resolve it."
)
```

**Size**: ~50-500 tokens ✗ VARIABLE
- Case A: Includes error messages (can be large)
- Case B: Static message (~50 tokens)

---

### 6. ASSISTANT RESPONSE - ITERATION 2 (Variable, if needed)

More reasoning, tool calls, and text responses.

**Size**: ~1,000-5,000 tokens ✗ VARIABLE

---

### 7. TOOL RESULTS - ITERATION 2 (Variable, if needed)

More search results, file reads, etc.

**Size**: ~500-10,000 tokens ✗ VARIABLE

---

### 8. USER MESSAGE - ITERATION 3 (Variable, if needed)

Same pattern as iteration 2.

**Size**: ~50-500 tokens ✗ VARIABLE

---

### 9. ASSISTANT RESPONSE + TOOL RESULTS - ITERATION 3 (Variable, if needed)

Final attempt.

**Size**: ~1,500-15,000 tokens ✗ VARIABLE

---

## Summary by Iteration Count

### Successful Item (1 iteration)

```
┌─────────────────────────────────────────────┐
│ SYSTEM: cached_context + instructions      │
│ Size: ~8,000 tokens                        │
│ Cacheable: ✓ YES (100%)                    │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ USER 1: "Please process..." + lease JSON   │
│ Size: ~200 tokens                          │
│ Cacheable: ✗ NO (variable lease data)      │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ ASSISTANT 1: reasoning + tool calls        │
│ Size: ~2,000 tokens                        │
│ Cacheable: ✗ NO (variable)                 │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ TOOL RESULTS 1: search/read outputs        │
│ Size: ~3,000 tokens                        │
│ Cacheable: ✗ NO (variable)                 │
└─────────────────────────────────────────────┘

Total: 8,000 + 200 + 2,000 + 3,000 = 13,200 tokens
Cached: 8,000 tokens
Cache rate: 8,000 / 13,200 = 60.6%
```

**Actual observed**: 65-89% (better than expected, likely due to some tool result caching)

---

### Failed Item (3 iterations)

```
┌─────────────────────────────────────────────┐
│ SYSTEM: cached_context + instructions      │
│ Size: ~8,000 tokens                        │
│ Cacheable: ✓ YES (100%)                    │
└─────────────────────────────────────────────┘

Iteration 1:
┌─────────────────────────────────────────────┐
│ USER 1 + ASSISTANT 1 + TOOL RESULTS 1      │
│ Size: ~5,000 tokens                        │
│ Cacheable: ✗ NO (all variable)             │
└─────────────────────────────────────────────┘

Iteration 2:
┌─────────────────────────────────────────────┐
│ USER 2 + ASSISTANT 2 + TOOL RESULTS 2      │
│ Size: ~5,000 tokens                        │
│ Cacheable: Partial (depends on what changed)│
└─────────────────────────────────────────────┘

Iteration 3:
┌─────────────────────────────────────────────┐
│ USER 3 + ASSISTANT 3 + TOOL RESULTS 3      │
│ Size: ~5,000 tokens                        │
│ Cacheable: Partial (depends on what changed)│
└─────────────────────────────────────────────┘

Total: 8,000 + 5,000 + 5,000 + 5,000 = 23,000 tokens
Cached: 8,000 + partial iteration caching
Cache rate: ~45-75% (depends on iteration similarity)
```

**Actual observed**: 45-75%

---

## What's Variable?

### Per Queue Item (changes for each new item)
1. **Lease data in User Message 1** (~200 tokens)
   - item_id (e.g., "no_recipe:knob_control_dial_v0")
   - gap_type (e.g., "no_recipe", "missing_field")
   - context (file path, description)
   - kind (material/part/machine/process/bom/recipe)

### Per Iteration (changes within an item)
2. **Agent responses** (~2,000-5,000 tokens per iteration)
   - Reasoning about what to do
   - Plans and explanations
   - Tool calls with arguments

3. **Tool results** (~500-10,000 tokens per iteration)
   - Search results (file paths, line numbers, matches)
   - File contents (YAML, 50-500 lines each)
   - Indexer output (validation report, errors)

4. **Feedback messages** (~50-500 tokens per iteration)
   - Error messages from indexer
   - "Gap still exists" messages

---

## Cache Breaking Points

### Primary Break: Lease Data
The biggest cache break is **line 484-486** where we inject the lease result:

```python
input_with_lease = (
    f"{user_input}\n\n"
    f"Queue item leased:\n```json\n{json.dumps(lease_result, indent=2)}\n```"
)
```

This puts **variable content in the first user message**, which means:
- System message: ✓ Cached (8K tokens)
- User message prefix: Could be cached, but is followed by...
- Lease JSON: ✗ Variable (200 tokens) → **breaks the cache**

Everything after the lease JSON cannot be cached on first iteration.

### Secondary Break: Iteration Feedback
On iterations 2 and 3, the **feedback messages** are variable:
- Indexer errors (different each time)
- File contents (different as agent makes changes)
- Tool outputs (different searches, reads)

This means each iteration adds uncacheable content.

---

## Why Current Cache Rate is 61.35%

### Weighted Average Calculation

From test results:
- Item 1 (3 iter): 1.73M tokens, 74.6% cache rate
- Item 2 (1 iter): 194K tokens, 89.1% cache rate
- Item 3 (3 iter): 1.25M tokens, 72.1% cache rate
- Item 4 (3 iter): 2.71M tokens, 45.7% cache rate
- Item 5 (1 iter): 164K tokens, 65.8% cache rate

**Why item 4 is so low (45.7%)**:
- Likely had very large tool outputs (file reads)
- The variable content was so large it dominated the token count
- 2.71M total tokens means ~1.47M uncached variable content

**Why items 2 and 5 are high (65-89%)**:
- Single iteration = less accumulated variable content
- Simpler gaps with fewer file reads

**Overall**: The 61.35% rate is pulled down by the multi-iteration items (items 1, 3, 4) which use 5.69M of the 6.05M tokens (94%).

---

## Optimization Opportunities

### Priority 1: Move Lease Data to Tool Response Pattern (IMPLEMENTED ✗)
**Status**: Not yet implemented

Instead of putting lease in user message:
```python
# CURRENT (line 484-486):
input_with_lease = f"{user_input}\n\n{json.dumps(lease_result)}"
```

Use synthetic tool response:
```python
# PROPOSED:
initial_messages = [
    {"role": "user", "content": "Please process the next queue item."},
    {"role": "assistant", "content": "", "tool_calls": [...]},
    {"role": "tool", "tool_call_id": "...", "content": json.dumps(lease_result)}
]
```

**Expected improvement**: 61% → 80-85% cache rate

### Priority 2: Minimize Iteration Feedback Size (NOT IMPLEMENTED)
**Status**: Not yet implemented

Instead of including error text in user message:
```python
# CURRENT (line 524-527):
user_input = f"The indexer failed with errors:\n{errors}"
```

Write errors to file and reference:
```python
# PROPOSED:
write_file("out/last_errors.txt", errors)
user_input = "The indexer failed. See out/last_errors.txt for details."
```

**Expected improvement**: 80-85% → 85-90% cache rate

### Priority 3: Success Rate Improvement (OPERATIONAL)
**Status**: Ongoing work

If more items succeed on first iteration:
- Single-iteration items get 65-89% cache rates
- Multi-iteration items get 45-75% cache rates
- Improving success rate shifts weighted average upward

**Not a caching optimization**, but improves overall efficiency.
