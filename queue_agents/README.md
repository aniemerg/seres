# Autonomous Queue Agent System

Implementation of [ADR 002](../docs/ADRs/002-autonomous-queue-agent.md) - autonomous agents that process KB work queue items in parallel.

## Quick Start

### 1. Build Cached Context (One-Time Setup)

```bash
python -m queue_agents.build_context
```

This generates `queue_agents/cached_context.md` containing:
- Agent reference memo (condensed schema guide)
- KB schema and structure
- Complex examples of each KB type
- Paper directory listing
- Queue workflow documentation

The agent reference memo is optimized for agents, containing only operational guidance:
schema, validation rules, naming conventions, and common patterns (not project philosophy).

### 2. Run Single Agent

```bash
python -m queue_agents.worker --agent test-agent-1
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

### 3. Run Multiple Agents in Parallel (Simple)

```bash
python -m queue_agents.launcher --workers 5
```

This spawns 5 agents in parallel, each processing items from the queue until empty.

### 4. Run Parallel Agents with Live Dashboard

```bash
python -m queue_agents.parallel_launcher --workers 20
```

This launches agents with a live progress dashboard showing:
- Overall metrics (completed, success/fail rate, items/min)
- Individual worker events (rotating display)
- Detailed logs saved to `/tmp/claude/tasks/worker-*.output`

Key features:
- **Clean console**: Only progress dashboard visible
- **Event rotation**: Shows one worker event at a time, updating every 3-4 seconds
- **Graceful shutdown**: Ctrl+C stops workers and releases all leased items
- **Configurable workers**: Use `--workers N` to set worker count
- **Detailed logs**: All worker output captured to files for review

Example with 50 workers:
```bash
python -m queue_agents.parallel_launcher --workers 50 --limit 100
```

## Cost Tracking

All agent runs are automatically logged to `out/agent_usage.jsonl` with:
- Token usage (input, output, cached)
- Cost in USD (based on gpt-5-nano pricing)
- Agent name, item processed, status

View summary:
```bash
python -c "from queue_agents import cost_tracker; cost_tracker.print_usage_summary()"
```

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
queue_agents/
├── __init__.py            # Module init
├── README.md              # This file
├── build_context.py       # Generates cached context
├── cached_context.md      # Generated cached context (not in git)
├── kb_tools.py            # Tool implementations
├── worker.py              # Main agent script
├── launcher.py            # Simple parallel runner
├── parallel_launcher.py   # Parallel runner with live dashboard
└── cost_tracker.py        # Token usage and cost tracking
```

## Examples

### Process a few items with one agent

```bash
python -m queue_agents.worker --agent worker-1 --max-items 5
```

### Use a different model

```bash
python -m queue_agents.worker --agent worker-1 --model claude-opus-4
```

### Launch multiple agents with custom prefix

```bash
python -m queue_agents.launcher --workers 10 --prefix batch-worker
```

### Run many agents with live dashboard

```bash
# Launch 30 workers with live progress display
python -m queue_agents.parallel_launcher --workers 30

# Process first 200 items with 50 workers
python -m queue_agents.parallel_launcher --workers 50 --limit 200
```

The dashboard shows:
```
Completed: 45/200 | Success: 42 | Failed: 3 | Active: 28 | Rate: 12.3/min
Worker 12: steel_tube_bending_v0 succeeded. Created 1 process, 1 recipe
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
For manual verification, use: `.venv/bin/python -m kbtool validate --id <gap_type:item_id>` or `queue complete --verify`.

## Common Workflows

### After KB Changes

If you've updated memos or significantly changed KB structure:

```bash
# Rebuild cached context
python -m queue_agents.build_context

# Re-run indexer to update queue
.venv/bin/python -m kbtool index

# Launch agents
python -m queue_agents.launcher --workers 5
```

### Testing on Specific Gap Types

```bash
# Run indexer to see current gaps
.venv/bin/python -m kbtool queue ls

# Launch agents (they'll pick items FIFO)
python -m queue_agents.launcher --workers 3
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

Run: `python -m queue_agents.build_context`

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
python -m queue_agents.worker --agent test
```

## Implementation Notes

See [ADR 002](../docs/ADRs/002-autonomous-queue-agent.md) for design decisions and rationale.

Key design points:
- Heavy cached context for token efficiency
- Auto-lease pattern (no wasted turns)
- Supervisor-managed lifecycle (auto-complete/release)
- Generalist agents (handle any gap type)
- Best-effort approach (follow existing patterns)
