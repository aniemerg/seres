# ADR-008: Manual Queue Item Addition

**Status:** Proposed
**Date:** 2024-12-28
**Authors:** Claude Sonnet 4.5

## Context

Agents working on queue items frequently discover new issues while researching and fixing gaps:
- Quality concerns (incorrect data, unrealistic estimates)
- Missing related items not caught by indexer
- Consolidation opportunities
- Data inconsistencies
- Issues requiring specialized knowledge or tools the current agent lacks

Currently, there's no mechanism for agents to add discovered issues to the work queue. The queue is **rebuilt from scratch** by the indexer on each run, which auto-detects structural gaps (missing references, circular dependencies, etc.) but cannot detect semantic issues like incorrect data or quality concerns.

Agents need a way to:
1. **Report discovered issues** for other agents to address
2. **Defer complex problems** beyond their current task scope
3. **Queue follow-up work** discovered during research

## Decision

Implement a **manual queue addition system** that allows agents (and humans) to add work items to the queue programmatically or via CLI, with the following design:

### 1. Manual Item Preservation

**Problem:** The indexer rebuilds `out/work_queue.jsonl` from scratch on each run, which would wipe out manually-added items.

**Solution:** Add `source` field to queue items:
- `"source": "indexer"` - Auto-detected by indexer (default)
- `"source": "manual"` - Manually added by agent or human
- `"source": "agent"` - Alias for manual (more semantic for agent additions)

**Indexer merge logic** preserves manual items:
```python
# In indexer.py _update_work_queue()
for eid, prev in existing.items():
    # Preserve manual items that aren't in the new gap list
    if eid not in merged_ids and prev.get("source") in ("manual", "agent"):
        merged.append(prev)
```

Manual items persist until explicitly completed/released, surviving indexer rebuilds.

### 2. Dynamic Gap Type Registry

**Problem:** We don't know all gap types agents will need upfront. Hard-coding types limits agent flexibility.

**Solution:** Create a **gap type registry** that agents can read and extend:

**File:** `queue/gap_type_registry.json`

**Structure:**
```json
{
  "quality_concern": {
    "description": "Item has quality/accuracy issues that need review",
    "created_by": "claude-worker-1",
    "created_at": 1735401234,
    "usage_count": 5,
    "examples": [
      "Energy model doesn't match paper",
      "Mass estimate unrealistic"
    ]
  },
  "needs_consolidation": {
    "description": "Multiple similar items should be merged",
    "created_by": "agent-3",
    "created_at": 1735401456,
    "usage_count": 2
  }
}
```

**Auto-registration:** When an agent uses a new gap_type, it's automatically added to the registry.

**List gap types:** `kbtool queue gap-types` shows all registered types (both indexer-defined and agent-created).

**Why `queue/` directory:**
- Not ephemeral output (`out/` is for generated files cleared on rebuild)
- Not KB data (`kb/` is for domain knowledge)
- Queue-related persistent metadata deserves its own directory
- Future queue config/metadata can live here

### 3. Freeform Context

Queue items include a `context` field that accepts **arbitrary JSON** with no validation:

```json
{
  "id": "quality_concern:steel_process_v0",
  "gap_type": "quality_concern",
  "item_id": "steel_process_v0",
  "source": "agent",
  "context": {
    "description": "Energy model doesn't match paper references",
    "discovered_by": "claude-worker-1",
    "discovered_at": 1735401234,
    "paper_ref": "ellery_2023.pdf",
    "expected_value": "3.5 kWh/kg",
    "actual_value": "1.2 kWh/kg",
    "notes": "Found while fixing recipe_steel_v0"
  }
}
```

**Recommended context fields:**
- `description` (string) - Clear description of the issue
- `discovered_by` (string) - Agent name
- `discovered_at` (timestamp) - When discovered
- `notes` (string) - Additional context

But agents can include any fields they find useful.

### 4. CLI Interface

**Design for bash usage** (Claude Code and scripts):

**Simple addition:**
```bash
kbtool queue add \
  --gap-type quality_concern \
  --item-id steel_process_v0 \
  --description "Energy model doesn't match paper references"
```

**With full context (heredoc for complex JSON):**
```bash
kbtool queue add \
  --gap-type quality_concern \
  --item-id steel_process_v0 \
  --description "Energy model conflicts with Ellery 2023 paper" \
  --context "$(cat <<'EOF'
{
  "paper_ref": "ellery_2023.pdf",
  "expected_value": "3.5 kWh/kg",
  "actual_value": "1.2 kWh/kg"
}
EOF
)"
```

**Batch addition from file:**
```bash
kbtool queue add --file discovered_gaps.jsonl
```

Where `discovered_gaps.jsonl` contains:
```jsonl
{"gap_type": "quality_concern", "item_id": "foo_v0", "description": "..."}
{"gap_type": "needs_review", "item_id": "bar_v0", "description": "..."}
```

**List gap types:**
```bash
kbtool queue gap-types
```

Output:
```
Registered Gap Types (15 total)
===============================

Indexer-Detected Types:
  referenced_only        - IDs referenced but not defined
  no_recipe              - Items without recipes
  null_quantity          - Process inputs/outputs with null quantities
  ...

Agent-Created Types:
  quality_concern        - Item has quality/accuracy issues (used 5 times)
  needs_consolidation    - Multiple similar items should be merged (used 2 times)
  needs_expert_review    - Requires domain expertise to validate (used 1 time)
```

### 5. Python API

**Add to `kbtool/queue_tool.py`:**

```python
def add_gap(
    gap_type: str,
    item_id: str,
    description: str = None,
    context: dict = None,
    kind: str = "gap",
    source: str = "manual"
) -> str:
    """
    Add a manual gap to the work queue.

    Args:
        gap_type: Type of issue (existing or new type)
        item_id: The item/recipe/process ID this relates to
        description: Clear description for fixing agent (goes in context)
        context: Optional dict with additional metadata
        kind: Item kind (default "gap")
        source: Source of gap (default "manual", can use "agent")

    Returns:
        The generated gap ID (format: "gap_type:item_id")

    Example:
        gap_id = add_gap(
            gap_type="quality_concern",
            item_id="steel_process_v0",
            description="Energy model doesn't match paper",
            context={"paper_ref": "ellery_2023.pdf"}
        )
    """
    import time

    gap_id = f"{gap_type}:{item_id}"

    # Build context with description
    ctx = context or {}
    if description:
        ctx["description"] = description
    ctx["added_at"] = time.time()

    item = {
        "id": gap_id,
        "kind": kind,
        "reason": gap_type,
        "gap_type": gap_type,
        "item_id": item_id,
        "source": source,
        "context": ctx,
        "status": "pending"
    }

    # Add to queue
    with _locked_queue():
        items = _load_queue()
        items.append(item)
        _save_queue(items)

    # Register gap type
    _register_gap_type(gap_type, source)

    return gap_id


def _register_gap_type(gap_type: str, created_by: str = "unknown"):
    """Auto-register new gap types in the registry."""
    import json
    from pathlib import Path
    import time

    registry_path = Path("queue/gap_type_registry.json")
    registry_path.parent.mkdir(exist_ok=True)

    # Load existing
    if registry_path.exists():
        registry = json.loads(registry_path.read_text())
    else:
        registry = {}

    # Add or update
    if gap_type in registry:
        registry[gap_type]["usage_count"] += 1
    else:
        registry[gap_type] = {
            "description": "",  # Agent can document later
            "created_by": created_by,
            "created_at": time.time(),
            "usage_count": 1
        }

    registry_path.write_text(json.dumps(registry, indent=2))


def list_gap_types() -> dict:
    """List all registered gap types."""
    import json
    from pathlib import Path

    registry_path = Path("queue/gap_type_registry.json")
    if not registry_path.exists():
        return {}

    return json.loads(registry_path.read_text())
```

### 6. Agent Tool Integration

**Add to `queue_agents/kb_tools.py`:**

```python
@function_tool
def queue_add_gap(
    gap_type: str,
    item_id: str,
    description: str,
    context: dict = None
) -> Dict[str, Any]:
    """
    Add a discovered issue to the work queue for another agent to fix.

    Use this when you discover problems while working that you can't fix yourself
    or that should be handled separately. Common gap types:

    - quality_concern: Incorrect data, unrealistic estimates, conflicts with papers
    - needs_consolidation: Multiple similar items should be merged
    - needs_review: Requires domain expertise or verification
    - missing_dependency: Found reference to undefined item not caught by indexer
    - data_inconsistency: Values don't match across related items

    You can also create new gap types with descriptive names.

    Args:
        gap_type: Type of issue (use `queue gap-types` to see existing types,
                  or create new descriptive type like "energy_model_mismatch")
        item_id: The item/recipe/process ID this issue relates to
        description: Clear description of the issue for the fixing agent.
                     Explain WHAT is wrong and WHY it's a problem.
        context: Optional dict with additional details like paper references,
                 expected vs actual values, related item IDs, etc.

    Returns:
        {"success": bool, "gap_id": str, "message": str}

    Examples:
        # Report quality issue
        queue_add_gap(
            gap_type="quality_concern",
            item_id="steel_melting_v0",
            description="Energy model shows 1.2 kWh/kg but Ellery 2023 paper indicates 3.5 kWh/kg for steel melting",
            context={"paper_ref": "ellery_2023.pdf", "section": "Table 4"}
        )

        # Flag consolidation opportunity
        queue_add_gap(
            gap_type="needs_consolidation",
            item_id="motor_small_v0",
            description="Found motor_electric_small, motor_small_v0, and small_motor_v0 - likely duplicates",
            context={"similar_items": ["motor_electric_small", "small_motor_v0"]}
        )
    """
    import subprocess
    import json

    try:
        # Build context with description
        ctx = context or {}
        ctx["description"] = description
        ctx["discovered_by"] = "queue_agent"  # Will be overridden by agent name if in worker

        # Call kbtool queue add
        result = subprocess.run(
            [
                str(VENV_PYTHON),
                "-m", "kbtool", "queue", "add",
                "--gap-type", gap_type,
                "--item-id", item_id,
                "--description", description,
                "--context", json.dumps(context) if context else "{}"
            ],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            gap_id = f"{gap_type}:{item_id}"
            return {
                "success": True,
                "gap_id": gap_id,
                "message": f"Added gap to queue: {gap_id}"
            }
        else:
            return {
                "success": False,
                "error": result.stderr or "Failed to add gap to queue"
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
```

### 7. Validation

**Minimal validation** - trust the agent:
- NO validation of gap_type (allows new types)
- NO validation that item_id exists in KB
- NO duplicate detection
- NO automatic indexer run after addition

Agents are responsible for providing useful information. Invalid additions will be caught when agents try to work them.

### 8. CLI Implementation

**Add to `kbtool/__main__.py`:**

```python
# In queue subparser
add_p = q_sub.add_parser("add", help="Add manual gap to queue")
add_p.add_argument("--gap-type", required=True, help="Gap type (existing or new)")
add_p.add_argument("--item-id", required=True, help="Item/recipe/process ID")
add_p.add_argument("--description", help="Description of the issue")
add_p.add_argument("--context", help="JSON context string")
add_p.add_argument("--file", help="JSONL file with gap items to add")

gap_types_p = q_sub.add_parser("gap-types", help="List registered gap types")

# In command handling
elif args.qcmd == "add":
    if args.file:
        # Batch add from file
        from pathlib import Path
        added = queue_tool.add_from_file(Path(args.file))
        print(f"Added {added} items to queue")
    else:
        # Single add
        import json
        context = json.loads(args.context) if args.context else {}
        gap_id = queue_tool.add_gap(
            gap_type=args.gap_type,
            item_id=args.item_id,
            description=args.description,
            context=context,
            source="manual"
        )
        print(f"Added gap to queue: {gap_id}")

elif args.qcmd == "gap-types":
    types = queue_tool.list_gap_types()
    # Format and print (see section 4 for output format)
```

## Consequences

### Positive

1. **Agents can report discovered issues** without blocking on fixing them
2. **Knowledge sharing** - agents document issues for others with specialized knowledge
3. **Flexible taxonomy** - gap type registry grows organically based on actual needs
4. **Persistent tracking** - manual items survive indexer rebuilds
5. **Simple API** - both CLI and Python, easy to use
6. **No false positives** - agents only add real issues they've verified

### Negative

1. **Manual items not validated** - could accumulate stale/invalid items
   - *Mitigation:* Queue GC can prune old manual items, agents can release invalid ones
2. **Duplicate gap types** - agents might create similar types with different names
   - *Mitigation:* `queue gap-types` makes existing types discoverable, agents should check first
3. **Queue growth** - manual additions could cause queue to grow indefinitely
   - *Mitigation:* Same as regular queue - complete/release items when done, GC for cleanup
4. **No automatic verification** - manual items might reference non-existent IDs
   - *Mitigation:* Fixing agent will discover this immediately, can release if invalid

### Migration

No breaking changes - this is purely additive:
1. Create `queue/` directory
2. Add gap type registry file
3. Add functions to `queue_tool.py`
4. Add CLI commands to `__main__.py`
5. Add tool to `kb_tools.py`
6. Update documentation

Existing queue items get `source: "indexer"` by default (missing field = indexer source).

## Implementation Checklist

- [ ] Create `queue/` directory
- [ ] Implement `add_gap()` in `queue_tool.py`
- [ ] Implement `_register_gap_type()` in `queue_tool.py`
- [ ] Implement `list_gap_types()` in `queue_tool.py`
- [ ] Implement `add_from_file()` in `queue_tool.py`
- [ ] Add CLI commands to `__main__.py`
- [ ] Update indexer merge logic to preserve manual items
- [ ] Add `queue_add_gap` tool to `kb_tools.py`
- [ ] Update `docs/README.md` with queue addition instructions
- [ ] Update `queue_agents/cached_context.md` with tool usage
- [ ] Add examples to both documentation locations
- [ ] Test manual addition workflow
- [ ] Test indexer preservation of manual items
- [ ] Test gap type registry auto-registration

## Examples

### Agent discovers quality issue while fixing recipe

```python
# Agent is fixing recipe_steel_v0 and notices energy model seems wrong

# Check existing gap types
gap_types = subprocess.run(["kbtool", "queue", "gap-types"], ...)

# Add issue to queue for another agent
queue_add_gap(
    gap_type="quality_concern",
    item_id="steel_melting_process_v0",
    description="Energy model shows 1.2 kWh/kg but Ellery 2023 paper Table 4 indicates 3.5 kWh/kg for steel melting. Current value is 3x too low.",
    context={
        "paper_ref": "design/papers/ellery_2023.pdf",
        "paper_section": "Table 4",
        "current_value": "1.2 kWh/kg",
        "expected_value": "3.5 kWh/kg",
        "discovered_while": "fixing recipe_steel_v0"
    }
)
```

### Human using CLI to add consolidation task

```bash
# Found duplicate items while browsing inventory
kbtool queue add \
  --gap-type needs_consolidation \
  --item-id motor_small_v0 \
  --description "Three similar motor items found: motor_small_v0, motor_electric_small, small_motor_v0. Should consolidate to one canonical item." \
  --context '{"similar_items": ["motor_electric_small", "small_motor_v0"], "masses": [12.0, 11.5, 12.5]}'
```

### Batch addition from agent analysis

```bash
# Agent analyzed inventory and found 10 quality issues
# Wrote them to discovered_issues.jsonl
kbtool queue add --file discovered_issues.jsonl
```

## References

- Queue system: `kbtool/queue_tool.py`
- Dedupe queue addition: `kbtool/dedupe_tool.py:149` (similar pattern)
- Indexer merge logic: `kbtool/indexer.py:932-968`
- Agent tools: `queue_agents/kb_tools.py`
- Conservative Mode: `docs/conservative_mode_guide.md`

## Status

**Proposed** - Awaiting approval before implementation.
