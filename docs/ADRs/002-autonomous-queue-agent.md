# ADR 002 — Autonomous Queue Agent Architecture

**Status:** Proposed
**Date:** 2024-12-16
**Owner:** kb/ops

## Context / Problem

The KB work queue contains ~209 gaps across multiple types (missing recipes, missing fields, unresolved references, etc.). Manual processing is slow and doesn't scale. We need an autonomous agent system that can:

- Process queue items in parallel (leveraging multiple concurrent agents)
- Work autonomously on diverse gap types (missing_field, no_recipe, unresolved_ref, etc.)
- Validate changes using the indexer before completion
- Maximize token efficiency through prompt caching
- Provide verbose, auditable output for monitoring and review
- Follow existing KB patterns and conventions (as documented in memos A & B)

The agent must be a generalist capable of handling any queue item type, using research from papers and existing KB examples to make best-effort additions/corrections.

## Decision / Direction

Build an autonomous agent system with the following architecture:

### Agent Design
- **Single agent processes one item, then recycles**: Each agent instance handles one queue item at a time, validates the fix, then resets to cached state and gets the next item
- **Heavy cached context**: Static context (memos, KB schema, paper summaries, examples) is cached and reused across all items
- **Auto-lease pattern**: Queue lease is executed automatically before agent starts (no wasted turn)
- **Supervisor-managed lifecycle**: A runner process manages queue operations (lease, complete, release) based on agent outcomes

### Token Efficiency Strategy
- **Cached context** (~50-100K tokens, reused):
  - Project memos (meta-memo.md, memo_a.md, memo_b.md)
  - KB schema and structure guide
  - Complex examples of each KB type (processes, recipes, BOMs, machines)
  - Paper directory listing with brief summaries
  - Queue workflow documentation
- **Per-item context** (small, varies):
  - Queue item details injected as auto-executed tool response
  - Agent work and tool calls
  - Truncated after item completion

### Workflow Per Item
1. **Auto-lease**: Runner executes `queue lease` before agent starts, injects result into message history
2. **Agent works**: Research (rg_search, read_file), make edits (write_file), validate (run_indexer)
3. **Success detection**: Runner checks if indexer passed AND gap no longer appears in work_queue.jsonl
4. **Auto-complete**: If success detected, runner executes `queue complete` and resets agent to cached state
5. **Error handling**: If indexer fails or gap persists, errors returned to agent for fixing (up to 3 iterations)
6. **Auto-release**: If unresolved after max iterations, runner executes `queue release`
7. **Recycle**: Reset to cached state, auto-lease next item, repeat

### Tools
Agent has access to standard, generic tools:
- `rg_search(pattern, path, max_matches)` - Search repo using ripgrep
- `read_file(path)` - Read any file in repo
- `write_file(path, content)` - Write/overwrite files (shows diff if existing)
- `run_indexer()` - Run kbtool index, return structured validation results
- `queue_release(item_id, agent_name)` - Explicitly give up on an item

Agent does NOT call `queue_lease` or `queue_complete` - these are auto-executed by the runner.

### Parallel Execution
- Launcher spawns N agent processes in parallel
- Each agent manages its own queue leases (no centralized work distribution)
- Agents exit gracefully when queue is empty
- No priority system in v0 (FIFO via queue lease)

### Output Format
Agent produces verbose output suitable for monitoring:
- Print each tool call and result
- Show full file contents for new files
- Show diffs for edited files
- List search queries and result counts
- List all files read (for audit trail)
- Explain reasoning between actions
- Clear success/failure status

## Implementation Components

### 1. Context Builder (`design/agent/build_context.py`)
Generates the static cached context file:
- Reads project memos
- Scans KB structure
- Auto-selects complex examples of each kind
- Lists papers with brief summaries
- Outputs to `design/agent/cached_context.md`

### 2. Agent Tools (`design/agent/kb_tools.py`)
Implements function tools following existing patterns from `design/agent/tools.py`:
- Generic file operations (read_file, write_file)
- Generic search (rg_search)
- Queue operations (queue_release)
- Indexer execution (run_indexer)

All tools shell out to system commands (rg, python -m kbtool) and parse results.

### 3. Agent Worker (`design/agent/worker.py`)
Main agent logic:
- Loads cached context
- Constructs agent with instructions
- Implements the item processing loop with state reset
- Manages auto-lease injection
- Detects success conditions (indexer pass + gap resolved)
- Auto-executes queue operations
- Handles max iteration limits

### 4. Parallel Launcher (`design/agent/launcher.py`)
Spawns and monitors multiple agent processes:
- Launch N workers in parallel
- Stream their stdout/stderr
- Report summary statistics
- Handle graceful shutdown

## Success Criteria

An item is considered successfully resolved when:
1. `run_indexer()` returns `success: true` (no hard validation errors)
2. The gap item_id no longer appears in `out/work_queue.jsonl`

Both conditions must be met. If indexer passes but gap persists, agent continues working.

## Quality & Conventions

- **Best effort**: Agents make reasonable assumptions based on existing patterns
- **Follow existing conventions**: Use KB examples as templates
- **Provenance**: Changes should follow existing provenance patterns (sources, notes)
- **Focus on quality**: Better to do one item well than many items poorly
- **Let indexer find implied work**: Don't try to anticipate downstream gaps

## Out of Scope (for now)

- Confidence levels or uncertainty annotations
- Explicit validation gates beyond indexer success
- Priority system for gap types
- Web search for external research (papers only)
- Multi-agent coordination or work stealing
- Automatic retry of previously failed items
- Metrics/analytics beyond basic success/failure counts

## Future Enhancements (potential)

- Per-gap-type specialized strategies
- Automatic seeding of new papers into cached context
- Incremental context updates without full cache invalidation
- Learning from successful patterns (few-shot examples)
- Human-in-the-loop approval for complex changes
- Parallel validation (run indexer in background while agent continues)
