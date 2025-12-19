# Autonomous Queue Agent System

Implementation of [ADR 002](../../docs/ADRs/002-autonomous-queue-agent.md) - autonomous agents that process KB work queue items in parallel.

## Quick Start

### 1. Build Cached Context (One-Time Setup)

```bash
python design/agent/build_context.py
```

This generates `design/agent/cached_context.md` containing:
- Project memos (meta, A, B)
- KB schema and structure
- Complex examples of each KB type
- Paper directory listing
- Queue workflow documentation

### 2. Run Single Agent

```bash
python -m design.agent.worker --agent test-agent-1
```

The agent will:
1. Lease the next available queue item
2. Research and fix the gap
3. Validate changes with the indexer
4. Auto-complete if successful, or release if stuck
5. Repeat with next item

Exit codes:
- `0` - Success (processed items)
- `1` - Failure (errors occurred)
- `2` - No work (queue empty)

### 3. Run Multiple Agents in Parallel

```bash
python -m design.agent.launcher --workers 5
```

This spawns 5 agents in parallel, each processing items from the queue until empty.

## Architecture

```
Agent Loop (per item):
1. Auto-lease queue item (before agent starts)
2. Agent researches and makes edits
3. Agent runs indexer to validate
4. Runner checks: indexer passed AND gap resolved?
   - Yes: Auto-complete, reset to cached state, lease next item
   - No: Return feedback to agent, retry (up to 3 iterations)
   - Stuck: Auto-release, reset, lease next item
```

## Tools Available to Agents

- `rg_search(pattern, path, max_matches)` - Search repo using ripgrep
- `read_file(path)` - Read any file in repo
- `write_file(path, content)` - Write/overwrite files with diff output
- `run_indexer()` - Run kbtool index, return validation results
- `queue_release(item_id, agent_name)` - Give up on an item

Agents do NOT call `queue_lease` or `queue_complete` - these are auto-executed by the runner.

## Token Efficiency

The agent uses prompt caching for maximum efficiency:

**Cached context** (~11K tokens, reused across all items):
- Project memos and KB schema
- Complex examples of each KB type
- Paper directory
- Queue workflow docs

**Per-item context** (varies):
- Queue item details (auto-injected)
- Agent's research and edits
- Validation feedback

The cached context is stable and only invalidated when:
- Memos are updated
- KB structure changes significantly
- Cached context is rebuilt

## File Structure

```
design/agent/
├── README.md              # This file
├── build_context.py       # Generates cached context
├── cached_context.md      # Generated cached context (not in git)
├── kb_tools.py           # Tool implementations
├── worker.py             # Main agent script
└── launcher.py           # Parallel batch runner
```

## Examples

### Process a few items with one agent

```bash
python -m design.agent.worker --agent worker-1 --max-items 5
```

### Use a different model

```bash
python -m design.agent.worker --agent worker-1 --model claude-opus-4
```

### Launch multiple agents with custom prefix

```bash
python -m design.agent.launcher --workers 10 --prefix batch-worker
```

## Monitoring Agent Work

Agents produce verbose output including:
- Each tool call with parameters
- Search queries and result counts
- File paths read
- File contents created/edited (with diffs)
- Indexer validation results
- Clear success/failure status

This makes it easy for monitoring agents (like Claude) to review the work done.

## Success Criteria

An item is marked complete when:
1. `run_indexer()` returns `success: true` (no hard errors)
2. The gap item_id no longer appears in `out/work_queue.jsonl`

Both conditions must be met.

## Common Workflows

### After KB Changes

If you've updated memos or significantly changed KB structure:

```bash
# Rebuild cached context
python design/agent/build_context.py

# Re-run indexer to update queue
.venv/bin/python -m kbtool index

# Launch agents
python -m design.agent.launcher --workers 5
```

### Testing on Specific Gap Types

```bash
# Run indexer to see current gaps
.venv/bin/python -m kbtool queue ls

# Launch agents (they'll pick items FIFO)
python -m design.agent.launcher --workers 3
```

### Reviewing Agent Work

After agents run, check:
- `out/validation_report.md` - Updated validation results
- `out/work_queue.jsonl` - Remaining gaps
- Git diff - Files created/modified

```bash
git status
git diff kb/
```

## Troubleshooting

### "Cached context not found"

Run: `python design/agent/build_context.py`

### "No pending items"

The queue is empty. Run indexer to rebuild it:

```bash
.venv/bin/python -m kbtool index
.venv/bin/python -m kbtool queue ls
```

### Agent stuck in loop

Agents will auto-release items after 3 iterations. Check:
- Agent output for error messages
- `out/validation_report.md` for validation issues
- Released items can be re-attempted manually

### Import errors

Ensure you're running from repo root:

```bash
cd /path/to/self-replicating-system-modeling
python -m design.agent.worker --agent test
```

## Implementation Notes

See [ADR 002](../../docs/ADRs/002-autonomous-queue-agent.md) for design decisions and rationale.

Key design points:
- Heavy cached context for token efficiency
- Auto-lease pattern (no wasted turns)
- Supervisor-managed lifecycle (auto-complete/release)
- Generalist agents (handle any gap type)
- Best-effort approach (follow existing patterns)
