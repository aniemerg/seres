# ADR 003: Process-Machine Schema Harmonization

**Status:** Partially Implemented
**Date:** 2025-12-18 (Draft), 2026-01-08 (Partial Implementation)

---

## Implementation Update (2026-01-08)

**Implemented:** Machine reference consolidation (`requires_ids` migration)

This update implements a key subset of ADR-003's goals: consolidating machine references from the legacy `requires_ids` field into `resource_requirements` with explicit `machine_id` fields. This furthers ADR-003's core principle of using concrete machine references instead of abstract types.

### Changes Made:

1. **Migration completed**: All 463 processes with `requires_ids` have been migrated to `resource_requirements`
2. **Schema updated**: `requires_ids` marked as deprecated in `src/kb_core/schema.py`
3. **Simulation updated**: Engine now reads from `resource_requirements.machine_id` instead of `requires_ids`
4. **Validation updated**: New warning rule `requires_ids_deprecated` added (WARNING level)
5. **Documentation updated**: All examples now use `resource_requirements` format

**Migration script**: `scripts/migrate_requires_ids.py`

**Format after migration:**
```yaml
resource_requirements:
  - machine_id: ball_mill_v0      # Migrated from requires_ids
    qty: 1
    unit: count
  - machine_id: labor_bot_general_v0
    qty: 1
    unit: count
```

### Still To Implement (Future Work):

- [ ] Add `processes_supported` field to machine definitions
- [ ] Remove `capabilities` field from machines (deprecated)
- [ ] Delete `kb/resources/*.yaml` files (73 files)
- [ ] Move consumables from `resource_requirements` to `inputs` where appropriate
- [ ] Build bidirectional machine ↔ process linkage

This partial implementation removes the `requires_ids` / `resource_requirements` duplication discovered during the original investigation, establishing `resource_requirements` as the single source of truth for machine requirements.

---

## Context

### Current State

**What's already working:**
- ✅ Process schema has `inputs`, `outputs`, `byproducts` (71% use inputs, 83% use outputs)
- ✅ Process schema has `resource_requirements` (92% use them)
- ✅ All data models exist in `kbtool/models.py`

**Problems identified:**

1. **Disconnected naming**: Processes reference abstract "resource_types", machines have "capabilities"
   - Only 24/76 resource requirements match machine capabilities
   - Example: process needs `assembly_station`, machine provides `assembly` capability
   - Result: 52 resource requirements have NO provider machines

2. **Redundant files**: 73 `kb/resources/*.yaml` files (resource_type definitions)
   - Add no value beyond duplicating capability names
   - 351/375 machine capabilities are never referenced by any process

3. **Inconsistent field usage**:
   - resource_requirements use both `amount` (317 occurrences) and `qty` (278 occurrences)
   - Need to standardize on one

4. **No bidirectional linkage**:
   - Can't navigate from machine → processes it supports
   - Must scan all processes to find what a machine can do

5. **Unclear consumables vs machines**:
   - Should consumables (wire, gas, fasteners) be in `inputs` or `resource_requirements`?

## Decision

### Core Principle

**Processes define transformations:**
`inputs (consumed) + machines (reusable) + energy → outputs`

- **inputs**: Items consumed/transformed (materials, consumables)
- **resource_requirements**: Reusable resources (machines, tools, labor bots)
- **outputs**: Items produced
- **byproducts**: Secondary outputs (waste, dust, heat)

### Schema Changes

#### 1. Requirement Model (kbtool/models.py)

**BEFORE:**
```python
class Requirement(_BaseModel):
    resource_type: Optional[str] = None  # ← abstract type
    amount: Optional[float] = None       # ← inconsistent with qty
    unit: Optional[str] = None
    notes: Optional[str] = None
```

**AFTER:**
```python
class Requirement(_BaseModel):
    machine_id: str                      # ← direct machine reference (required)
    qty: Optional[float] = None          # ← standardized (was amount/qty)
    unit: Optional[str] = None
    notes: Optional[str] = None
```

**Changes:**
- `resource_type` → `machine_id` (concrete machine, not abstract type)
- `amount` → `qty` (standardize on one field name)
- `machine_id` is required (not optional)

#### 2. Machine Model (Item with kind=machine)

**BEFORE:**
```python
class Item(_BaseModel):
    id: str
    kind: str  # "machine"
    capabilities: List[str] = []  # ← abstract capability strings
    # ... other fields
```

**AFTER:**
```python
class Item(_BaseModel):
    id: str
    kind: str  # "machine"
    processes_supported: List[str] = []  # ← NEW: process IDs this machine can perform
    # capabilities: deprecated, remove
    # ... other fields
```

**Changes:**
- Add `processes_supported: List[str]` field
- Deprecate `capabilities` field (to be removed)

#### 3. Process Schema (already exists, minimal changes)

**Clarification on inputs vs resource_requirements:**

```yaml
id: welding_process_v0
kind: process
name: Basic arc welding

# Consumed items (destroyed/transformed in process)
inputs:
  - item_id: steel_workpiece
    qty: 2.0
    unit: kg
  - item_id: welding_wire_steel  # ← consumable
    qty: 0.05
    unit: kg
  - item_id: shielding_gas_argon  # ← consumable
    qty: 0.1
    unit: kg

outputs:
  - item_id: welded_assembly
    qty: 2.04
    unit: kg

# Reusable machines/tools (not consumed)
resource_requirements:
  - machine_id: welding_power_supply_v0  # ← specific machine reference
    qty: 0.5
    unit: hr
  - machine_id: labor_bot_welder_v0      # ← specific labor bot
    qty: 0.5
    unit: hr

energy_model:
  type: kWh_per_kg
  value: 2.0

time_model:
  type: linear_rate
  hr_per_kg: 0.25
```

**Key points:**
- Use **specific machine IDs** (e.g., `labor_bot_welder_v0` not `labor_bot_welder`)
- Consumables go in **inputs** (wire, gas, fasteners, etc.)
- Machines/tools go in **resource_requirements** (reusable)
- If multiple of same machine needed, duplicate the entry:
  ```yaml
  resource_requirements:
    - machine_id: welder_v0
      qty: 2.0
      unit: hr
    - machine_id: welder_v0  # second welder
      qty: 2.0
      unit: hr
  ```

#### 4. Delete Resource Type Files

**Action:** Remove all 73 files in `kb/resources/*.yaml`

Information is now embedded in:
- Process `resource_requirements` (which machines are needed)
- Machine `processes_supported` (which processes this machine can do)

## Migration Strategy

### Phase 1: Schema Updates

1. **Update `kbtool/models.py`:**
   ```python
   # In Requirement class:
   - resource_type → machine_id (rename, make required)
   - Remove amount field (standardize on qty)

   # In Item class (for machines):
   - Add processes_supported: List[str] = Field(default_factory=list)
   - Mark capabilities as deprecated
   ```

2. **Update indexer validation:**
   - Check `machine_id` references exist
   - Warn on deprecated `capabilities` usage
   - Warn on `amount` field usage (should be `qty`)
   - Check all consumables are in `inputs` (heuristic: items with "wire", "gas", "fastener" in name)

### Phase 2: File Migration

**Automated migration script: `scripts/migrate_resources.py`**

```python
# For each process file:
# 1. Rename resource_type → machine_id
# 2. Rename amount → qty (if exists)
# 3. Standardize on qty field

# For each machine file:
# 2. Scan all processes to find which reference this machine
# 3. Add processes_supported list
# 4. Remove capabilities field
```

**Manual review needed for:**
- Processes with resource_requirements that don't map to real machines
  - Either create the machine or change to existing equivalent
- Consumables that should move from resource_requirements to inputs
  - Wire, gas, lubricants, fasteners, etc.

### Phase 3: Cleanup

1. Delete `kb/resources/*.yaml` files (73 files)
2. Remove `capabilities` from all machine YAML files
3. Re-index and validate
4. Fix any broken references

### Phase 4: Documentation Updates

1. `design/memo_a.md` - update process/machine schema
2. `docs/README.md` - update examples
3. `design/memos/parts_and_labor_guidelines.md` - clarify consumables vs machines

## Open Questions & Decisions

### 1. Field naming: qty vs amount?

**Decision:** Use `qty` consistently
- Already used in inputs/outputs
- Shorter, clearer
- Most processes already use it (278 vs 317)

### 2. Specific vs generic machine references?

**Decision:** Always use specific machine IDs with version
- `labor_bot_welder_v0` not `labor_bot_welder`
- Clearer what's actually needed
- Easier to track dependencies

### 3. What about multiple machines of same type?

**Decision:** Duplicate entries (no "count" field)
- Rare enough not to justify extra field
- Clear and explicit

```yaml
resource_requirements:
  - machine_id: welder_v0
    qty: 2.0
    unit: hr
  - machine_id: welder_v0  # if you need 2 welders
    qty: 2.0
    unit: hr
```

### 4. Consumables: inputs or resource_requirements?

**Decision:** Consumables go in `inputs`
- Anything consumed/destroyed: wire, gas, molds, lubricants, fasteners
- Anything reusable: machines, tools, labor bots

**Rule of thumb:** If it comes back unchanged → resource_requirement. If it's transformed/used up → input.

### 5. Migration: automated or manual?

**Decision:** Hybrid
- Automated: field renames (resource_type→machine_id, amount→qty)
- Manual review: consumables moving to inputs, fixing broken references
- Automated: building processes_supported from process scanning

## Consequences

### Positive

- **Clearer model**: Direct machine references, no abstract layer
- **Bidirectional navigation**: machine ↔ processes linkage
- **Less redundancy**: Remove 73 resource_type files
- **Better validation**: Can verify all machines exist
- **Consistent fields**: One way to specify quantity (`qty`)
- **Clear consumables**: Inputs vs machines distinction

### Negative

- **Breaking change**: Old processes won't validate after schema change
- **Migration work**: 593 processes + 291 machines need updates
- **Tighter coupling**: Processes reference specific machines (more realistic but less flexible)

### Neutral

- **Different abstraction**: Lose abstract capabilities, gain concrete machine references

## Implementation Checklist

- [ ] Finalize ADR
- [ ] Update `kbtool/models.py`:
  - [ ] Requirement: resource_type → machine_id, remove amount, keep qty
  - [ ] Item (machine): add processes_supported, deprecate capabilities
- [ ] Update indexer validation
- [ ] Write migration script `scripts/migrate_resources.py`
- [ ] Test migration on 10 sample processes
- [ ] Run migration on all processes
- [ ] Scan processes to build machine.processes_supported
- [ ] Delete kb/resources/*.yaml files
- [ ] Re-index and validate
- [ ] Update documentation
- [ ] Fix broken references

## Examples After Migration

### Process Example

```yaml
id: casting_basic_v0
kind: process
name: Basic metal casting
tags: [layer_3, metal_forming]

inputs:
  - item_id: molten_steel
    qty: 10.0
    unit: kg
  - item_id: sand_mold        # ← consumed in process
    qty: 1
    unit: ea
  - item_id: release_agent    # ← consumable
    qty: 0.1
    unit: kg

outputs:
  - item_id: steel_casting_rough
    qty: 9.5
    unit: kg

byproducts:
  - item_id: slag
    qty: 0.3
    unit: kg

resource_requirements:
  - machine_id: casting_furnace_v0  # ← specific machine
    qty: 2.0
    unit: hr
  - machine_id: labor_bot_general_v0
    qty: 0.5
    unit: hr

energy_model:
  type: kWh_per_kg
  value: 3.5

time_model:
  type: fixed_time
  hr_per_batch: 2.0
```

### Machine Example

```yaml
id: casting_furnace_v0
kind: machine
name: Basic casting furnace
mass: 500
unit: kg
bom: bom_casting_furnace_v0

# NEW: Which processes this machine can perform
processes_supported:
  - casting_basic_v0
  - metal_melting_v0
  - bronze_casting_v0

# REMOVED: capabilities field deleted

notes: |
  Induction or resistance furnace for melting metals.
  Temperature range: up to 1600°C
```

## Related Documents

- `design/memo_a.md` - Core specification
- `docs/README.md` - Workflow documentation
- `design/memos/parts_and_labor_guidelines.md` - Worker guidelines
- `ADR 001: Dedupe Initiative` - Related cleanup
- `ADR 002: Autonomous Queue Agent` - Queue workflow
