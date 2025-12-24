# Indexer Lease Preservation Fix - 2024-12-24

## Problem

When agents fixed queue items and ran the indexer to validate, the fixed items would disappear from the queue entirely, preventing agents from successfully marking them as complete.

### Original Broken Flow

1. Agent leases item `gap:item_x` (status=`leased`, lease_id=`agent1`)
2. Agent fixes the gap
3. Agent runs indexer to validate
4. **Indexer rebuilds queue from scratch:**
   - Scans KB for current gaps
   - Creates `gap_items` list containing only CURRENT gaps
   - Merges with existing queue, but ONLY preserves state for items in `gap_items`
   - Fixed item is not in `gap_items` → **item vanishes from queue**
5. Agent calls `queue complete --id gap:item_x`
6. Complete function looks for item in queue → **not found** → returns `False`
7. Agent sees "Failed to complete" error and is confused

### Root Cause

The indexer's merge logic (`kbtool/indexer.py` lines 945-957) only preserved state for items that STILL had gaps. When a gap was resolved, the item disappeared completely from the queue, even if it was actively leased by an agent.

## Solution

Implemented "resolved" status to preserve leased items that have been fixed.

### Changes Made

#### 1. Indexer Merge Logic (kbtool/indexer.py:959-968)

Added logic to preserve leased items that are no longer in the gap list:

```python
# Preserve leased items that are no longer in gap_items (they were resolved)
# This allows agents to successfully complete items they fixed
merged_ids = {obj["id"] for obj in merged}
for eid, prev in existing.items():
    if eid not in merged_ids and prev.get("status") == "leased":
        # Gap was resolved while leased - mark as resolved so agent can complete it
        if prev.get("lease_expires_at", 0) >= now:
            # Only preserve if lease is still valid
            prev["status"] = "resolved"
            merged.append(prev)
```

**Key Points:**
- Only preserves items with valid (non-expired) leases
- Sets status to `"resolved"` to indicate gap is fixed but completion pending
- Preserves all lease metadata (lease_id, lease_expires_at)

#### 2. Queue Complete Function (kbtool/queue_tool.py:172-188)

Updated to handle both "leased" and "resolved" statuses:

```python
def complete(id_value: str, agent: str) -> bool:
    with _locked_queue():
        items = _load_queue()
        updated = False
        for obj in items:
            if obj.get("id") == id_value:
                # Check lease ownership for leased and resolved items
                status = obj.get("status")
                if status in ("leased", "resolved") and obj.get("lease_id") != agent:
                    continue
                obj["status"] = "done"
                obj["completed_at"] = time.time()
                updated = True
                break
        if updated:
            _save_queue(items)
        return updated
```

**Key Points:**
- Accepts both `"leased"` and `"resolved"` statuses
- Validates lease ownership for both statuses
- Marks as `"done"` on successful completion

#### 3. Queue GC Function (kbtool/queue_tool.py:209-233)

Added handling for expired "resolved" items:

```python
# Expire resolved items with expired leases (agent failed to complete)
if obj.get("status") == "resolved" and obj.get("lease_expires_at", 0) < now:
    obj["status"] = "pending"
    obj.pop("lease_id", None)
    obj.pop("lease_expires_at", None)
```

**Key Points:**
- If an agent marks something as resolved but fails to complete it before lease expires
- The item reverts to "pending" status
- Allows another agent to re-lease and complete it

## New Flow (Fixed)

1. Agent leases item `gap:item_x` (status=`leased`, lease_id=`agent1`)
2. Agent fixes the gap
3. Agent runs indexer to validate
4. **Indexer rebuilds queue:**
   - Scans KB for current gaps
   - `item_x` not in gaps (it's fixed)
   - Merge logic detects `item_x` is leased but not in gap list
   - **Preserves item with status=`"resolved"`**
5. Agent calls `queue complete --id gap:item_x`
6. Complete function finds item with status=`"resolved"`, validates lease ownership
7. Marks as status=`"done"` → **Success!**
8. Agent sees "✓ Completed"

## Queue Status States

After this fix, queue items can have these statuses:

| Status | Meaning | Transitions |
|--------|---------|-------------|
| `pending` | Available to be leased | → `leased` (via queue lease) |
| `leased` | Actively being worked on | → `resolved` (indexer detects fix)<br>→ `done` (via queue complete)<br>→ `pending` (lease expires) |
| `resolved` | Fixed but awaiting completion | → `done` (via queue complete)<br>→ `pending` (lease expires) |
| `done` | Completed, ready for GC | (terminal, pruned by GC) |

## Benefits

1. **Agents can successfully complete their work** - No more "Failed to complete" errors
2. **Clean audit trail** - Items stay in queue until explicitly completed
3. **Lease expiration still works** - Resolved items revert to pending if not completed in time
4. **Backward compatible** - Existing queue items continue to work
5. **Minimal code change** - Only ~20 lines added/modified across 2 files

## Edge Cases Handled

### Case 1: Agent fixes item but crashes before completing
- Item marked as `resolved` by indexer
- Lease expires
- GC reverts to `pending`
- Another agent can lease and complete it

### Case 2: Gap reappears after being marked resolved
- Next indexer run detects gap again
- Item shows up in `gap_items` with current gap data
- Merge logic updates item with new gap context
- Status reverts to `leased` (preserving lease) or `pending` (if different gap)

### Case 3: Multiple indexer runs while agent works
- First run: Item still `leased` (gap exists)
- Agent fixes gap
- Second run: Item marked `resolved`
- Agent completes: Success
- Third run: Item not in queue (was marked `done`)

## Testing Recommendation

Test scenario:
1. Manually lease a queue item: `.venv/bin/python -m kbtool queue lease --agent test-agent`
2. Fix the gap (e.g., create the missing file)
3. Run indexer: `.venv/bin/python -m kbtool index`
4. Check queue: `grep "test-agent" out/work_queue.jsonl` → should show status="resolved"
5. Complete item: `.venv/bin/python -m kbtool queue complete --id <item_id> --agent test-agent`
6. Verify success (should return 0 exit code)
7. Check queue: Item should have status="done"

## Files Modified

1. **kbtool/indexer.py** - Added preserve leased items logic (lines 959-968)
2. **kbtool/queue_tool.py** - Updated complete() to handle "resolved" status (lines 178-188)
3. **kbtool/queue_tool.py** - Updated gc() to expire resolved items (lines 221-225)

## Backward Compatibility

✅ **Fully backward compatible**
- Existing queue items continue to work
- No changes to queue file format
- Only adds new status value, doesn't change existing logic

## Related Issues

This fixes the agent confusion where they would:
- Fix a gap successfully
- Run validation (indexer passes)
- Attempt to complete the item
- See "Failed to complete" error
- Report failure despite successful fix

Now agents will:
- Fix a gap successfully
- Run validation (indexer passes, marks as "resolved")
- Successfully complete the item
- Report success ✓
