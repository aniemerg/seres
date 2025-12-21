# Agent Prompt Cache Analysis

## Current Cache Hit Rate: 54.9% ⚠️

This is LOW. We should be getting 80-90%+ cache hit rate.

## Problem Identified

**The agent is NOT being reset between queue items**, causing conversation history to accumulate and break caching.

## Current Prompt Structure

### Agent Initialization (Once per worker launch)
```python
# Line 432 in worker.py
agent = build_agent(model)  # Built ONCE

while True:  # Process multiple items with SAME agent
    # Item 1, 2, 3, ... all use same agent instance
```

### Prompt Construction (Per Agent Build)

**Static Content (Should be 100% cached):**
```
┌─────────────────────────────────────────────┐
│ SYSTEM MESSAGE (agent.instructions)        │
│                                             │
│ 1. cached_context.md (~7,927 tokens)       │
│    - Agent reference memo                   │
│    - KB schema guide                        │
│    - Complex examples (processes, recipes)  │
│    - Papers directory                       │
│    - Queue workflow docs                    │
│                                             │
│ 2. AGENT_INSTRUCTIONS (~300 tokens)         │
│    - Your goal                              │
│    - Process steps                          │
│    - Output format                          │
│    - Important notes                        │
│                                             │
│ Total: ~8,227 tokens (STATIC) ✓            │
└─────────────────────────────────────────────┘
```

### Variable Content (Changes per item/iteration)

**Iteration 1:**
```
┌─────────────────────────────────────────────┐
│ USER MESSAGE 1                              │
│ "Please process the queue item..."         │
│ + Queue item JSON (lease_result)           │
│   - item_id (VARIABLE)                      │
│   - gap_type (VARIABLE)                     │
│   - context (VARIABLE)                      │
│ Total: ~100-500 tokens (VARIABLE) ✗        │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ AGENT RESPONSE 1                            │
│ - Text output (VARIABLE)                    │
│ - Tool calls (VARIABLE)                     │
│   - rg_search(...)                          │
│   - read_file(...)                          │
│   - write_file(...)                         │
│   - run_indexer()                           │
│ Total: ~1,000-5,000 tokens (VARIABLE) ✗    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ TOOL RESULTS 1                              │
│ - Search results (VARIABLE)                 │
│ - File contents (VARIABLE)                  │
│ - Indexer output (VARIABLE)                 │
│ Total: ~500-3,000 tokens (VARIABLE) ✗      │
└─────────────────────────────────────────────┘
```

**Iteration 2 (if needed):**
```
┌─────────────────────────────────────────────┐
│ USER MESSAGE 2                              │
│ "The indexer failed..." or                  │
│ "The gap still exists..."                   │
│ + Error details (VARIABLE)                  │
│ Total: ~100-1,000 tokens (VARIABLE) ✗      │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ AGENT RESPONSE 2 + TOOL RESULTS 2           │
│ More variable content...                    │
│ Total: ~1,000-8,000 tokens (VARIABLE) ✗    │
└─────────────────────────────────────────────┘
```

**Iteration 3 (if needed):**
```
┌─────────────────────────────────────────────┐
│ USER MESSAGE 3 + AGENT RESPONSE 3           │
│ Even more variable content...               │
│ Total: ~1,000-8,000 tokens (VARIABLE) ✗    │
└─────────────────────────────────────────────┘
```

## The Critical Problem: Agent Reuse Across Items

```python
# CURRENT CODE (BAD):
agent = build_agent(model)  # Line 432

while True:
    # Item 1 processing
    lease_item_1()
    run_agent_streamed(agent, input_1)  # Conversation: [system, user1, agent1, tools1]

    # Item 2 processing - SAME AGENT!
    lease_item_2()
    run_agent_streamed(agent, input_2)  # Conversation: [system, user1, agent1, tools1, user2, agent2, tools2]

    # Item 3 processing - SAME AGENT!
    lease_item_3()
    run_agent_streamed(agent, input_3)  # Conversation: [system, user1, agent1, tools1, user2, agent2, tools2, user3, agent3, tools3]
```

**Result:**
- Static content (8,227 tokens): Cached once ✓
- Item 1 variable content (~5,000 tokens): Not cached ✗
- Item 2 variable content (~5,000 tokens): Not cached ✗
- Item 3 variable content (~5,000 tokens): Not cached ✗
- ...
- Item 50 variable content (~5,000 tokens): Not cached ✗

**Effective cache rate:**
```
Cached: 8,227 tokens
Total: 8,227 + (50 items × 5,000 tokens) = 258,227 tokens
Cache rate: 8,227 / 258,227 = 3.2% 😱
```

But we're seeing 54.9%, which means the Agent SDK is doing SOME caching of the growing conversation, but not optimally.

## Why Cache Rate is Low

1. **Agent persists across items** - Conversation history accumulates
2. **Variable content accumulates** - Each item adds ~5K+ variable tokens
3. **Cache breaking** - Variable content in middle of conversation breaks prefix caching
4. **Long conversations** - Multi-iteration items create very long conversations

## Solution: Rebuild Agent for Each Item

**What we should do:**

```python
# PROPOSED CODE (GOOD):
while True:
    # Lease item
    lease_result = execute_queue_lease(agent_name)

    # BUILD FRESH AGENT FOR THIS ITEM
    agent = build_agent(model)  # Fresh conversation!

    # Process item
    run_agent_streamed(agent, input_with_lease)

    # After completion/release, agent is discarded
    # Next iteration gets a fresh agent
```

**Expected cache rate:**

For each item:
```
Static content: 8,227 tokens (100% cached after first item)
Variable content: ~5,000 tokens (not cached, but only per-item)

Cache rate: 8,227 / (8,227 + 5,000) = 62.2%
```

But with multi-iteration items (3 iterations max):
```
Static content: 8,227 tokens (cached)
Iteration 1 variable: ~5,000 tokens
Iteration 2 variable: ~5,000 tokens
Iteration 3 variable: ~5,000 tokens
Total: 8,227 + 15,000 = 23,227 tokens

Cache rate: 8,227 / 23,227 = 35.4% per item
```

But across many items, first-pass success (no iterations) should dominate:
```
Successful items (80%): 8,227 / 13,227 = 62.2% cache rate
Failed items (20%): 8,227 / 23,227 = 35.4% cache rate

Weighted average: 0.8 × 62.2% + 0.2 × 35.4% = 56.8%
```

Still not great! We need to go further...

## Further Optimization: Move Variable Content to Tool Response

Instead of putting queue item in user message, inject it as a "pseudo tool result":

```python
# BETTER APPROACH:
agent = build_agent(model)

# Inject lease as if it was a tool response
initial_messages = [
    {
        "role": "user",
        "content": "Please process the next queue item."
    },
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [{
            "id": "lease_1",
            "type": "function",
            "function": {
                "name": "queue_lease",
                "arguments": "{}"
            }
        }]
    },
    {
        "role": "tool",
        "tool_call_id": "lease_1",
        "content": json.dumps(lease_result)  # Variable content here
    }
]
```

This puts variable content AFTER the cacheable system message, allowing better caching.

## Theoretical Maximum Cache Rate

If we optimize perfectly:
```
Static system message: 8,227 tokens (always cached)
User prompt: ~50 tokens (always same: "Please process the next queue item")
Tool result: ~500 tokens (variable lease data)

Per item: 8,227 / (8,227 + 50 + 500) = 93.7% cache rate 🎯
```

## Recommendations

### Priority 1: Rebuild Agent Per Item (CRITICAL)
```python
# Change line 432 from:
agent = build_agent(model)
while True:
    # ... process item with same agent

# To:
while True:
    agent = build_agent(model)  # Fresh agent each item!
    # ... process item
```

**Expected improvement:** 3.2% → 56.8% cache rate

### Priority 2: Separate Static from Variable in User Message
Instead of:
```python
input_with_lease = f"{user_input}\n\n{json.dumps(lease_result)}"
```

Use:
```python
user_input = "Please process the next queue item."
# Pass lease_result as a tool response (requires Agent SDK changes)
```

**Expected improvement:** 56.8% → 85%+ cache rate

### Priority 3: Minimize Iteration Feedback Size
Current:
```python
user_input = f"The indexer failed with errors. Please fix them:\n{chr(10).join(errors[:10])}"
```

Better:
```python
user_input = "The indexer reported errors. Please review and fix them."
# Store errors in a file that agent can read_file()
```

**Expected improvement:** 85% → 90%+ cache rate

## Summary

| Optimization | Cache Rate | Effort |
|-------------|------------|--------|
| Current (broken) | 54.9% | - |
| Priority 1: Rebuild agent | 56.8% | 5 minutes |
| Priority 2: Tool response pattern | 85% | 1 hour |
| Priority 3: Minimize feedback | 90%+ | 30 minutes |

**Immediate action: Move `agent = build_agent(model)` inside the while loop.**
