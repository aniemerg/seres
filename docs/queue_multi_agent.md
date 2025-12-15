# Multi-Agent Queue Usage

## REQUIRED READING FIRST

**Before working on the queue, you MUST read:**
1. `design/meta-memo.md` — Project overview and goals
2. `design/memo_a.md` — Specification and design principles
3. `design/memo_b.md` — Knowledge acquisition methodology

See `docs/README.md` for full onboarding documentation.

## Queue Operations

- IDs are stable: `id = "<gap_type>:<item_id>"` with `gap_type`, `item_id`, `reason`, `context`, `status`, `lease_id`, `lease_expires_at`.
- Always lease before editing:
  - Lease: `.venv/bin/python -m kbtool queue lease --agent <name> [--ttl 900] [--priority gap1,gap2]`
    - Only one lease per `item_id` is allowed; if another entry with the same `item_id` is leased, the request is denied.
  - Complete: `.venv/bin/python -m kbtool queue complete --id <gap_type:item_id> --agent <name>`
  - Release: `.venv/bin/python -m kbtool queue release --id <gap_type:item_id> --agent <name>`
  - GC expired leases: `.venv/bin/python -m kbtool queue gc [--prune-done-older-than N]`
  - List: `.venv/bin/python -m kbtool queue ls`
- Do not edit items you haven’t leased. If you find another agent’s edits, reconcile rather than overwrite; leave context in `notes`.
- Indexer rebuilds the queue each run, preserving leases/done status; gaps resurface if fixes are incomplete.
- Pruning only removes items marked `resolved`/`superseded`; gaps persist until fixes land.
