# Import Mass Calculation Not Working

## Problem

The simulation's `view-state` command shows `Total imported mass: ~0.0 kg` even when multiple items have been imported. This makes it impossible to track the ISRU (In-Situ Resource Utilization) ratio, which is a critical metric for lunar manufacturing scenarios.

## Observed Behavior

During simulation `echo_genesis_934` (2026-01-02):

```bash
$ python -m src.cli sim view-state --sim-id echo_genesis_934

=== Simulation: echo_genesis_934 ===
Time: 0.0 hours (0.0 days)
Energy Consumed: 0.00 kWh

Inventory (9 items):
  battery_backup_small: 1.00 unit
  cable_drag_chain: 2.00 unit
  force_torque_sensor_6axis: 1.00 unit
  harmonic_drive_reducer_medium: 6.00 unit
  labor_bot_general_v0: 1.00 unit
  led_ring_light: 2.00 unit
  safety_controller_plc: 1.00 unit
  servo_drive_controller: 6.00 unit
  touch_sensor_capacitive: 2.00 unit

Total Imports (9 items):
  battery_backup_small: 1.00 unit
  cable_drag_chain: 2.00 unit
  force_torque_sensor_6axis: 1.00 unit
  harmonic_drive_reducer_medium: 6.00 unit
  labor_bot_general_v0: 1.00 unit
  led_ring_light: 2.00 unit
  safety_controller_plc: 1.00 unit
  servo_drive_controller: 6.00 unit
  touch_sensor_capacitive: 2.00 unit
  Total imported mass: ~0.0 kg  ← WRONG!
```

## Expected Behavior

The system should calculate actual imported mass from item definitions. For example:
- `labor_bot_general_v0` has mass `120.0 kg` (from `kb/items/machines/labor_bot_general_v0.yaml`)
- `harmonic_drive_reducer_medium` has mass `2.0 kg` each × 6 units = 12 kg
- etc.

Expected output:
```
Total Imports (9 items):
  battery_backup_small: 1.00 unit (~1.0 kg)
  cable_drag_chain: 2.00 unit (~3.0 kg)
  ...
  labor_bot_general_v0: 1.00 unit (~120.0 kg)
  Total imported mass: ~148.5 kg  ← CORRECT
```

## Impact

**Severity**: Medium (Data Quality / Metrics)

**Use Cases Blocked**:
1. **ISRU Ratio Tracking** - Cannot calculate `local_production_mass / total_mass`
2. **Launch Mass Planning** - Cannot determine Earth-to-Moon transport requirements
3. **Mission Planning** - Cannot compare different manufacturing strategies by import mass
4. **Economic Analysis** - Cannot calculate cost based on launch mass ($X per kg to lunar surface)

**Example Metric**:
```python
isru_ratio = (total_mass - imported_mass) / total_mass * 100
# Goal for mature lunar base: >90% ISRU
```

Currently this calculation returns meaningless results.

## Root Cause Analysis

The issue is likely in the simulation state display code (`src/simulation/cli.py` or `src/simulation/engine.py`).

**Hypothesis 1**: Mass lookup failing
- Code tries to look up item mass but gets `None`
- Fallback to 0.0 instead of handling properly

**Hypothesis 2**: Unit conversion issue
- Items have mass in different units (kg vs unit vs L)
- Code doesn't know how to aggregate mixed units

**Hypothesis 3**: Missing mass data
- Many items don't have `mass` field defined
- Code should sum what's available and note "X items with unknown mass"

## Proposed Solution

### Option A: Best Effort Calculation (Recommended)

```python
def calculate_total_mass(items: List[Tuple[str, float, str]], kb) -> Tuple[float, int]:
    """
    Calculate total mass from items list.

    Returns:
        (total_mass_kg, items_with_unknown_mass)
    """
    total_kg = 0.0
    unknown_count = 0

    for item_id, qty, unit in items:
        item_def = kb.get_item(item_id)
        if not item_def:
            unknown_count += 1
            continue

        item_mass_kg = item_def.get('mass')
        if item_mass_kg is None:
            unknown_count += 1
            continue

        # Convert quantity to mass
        if unit == 'unit':
            total_kg += item_mass_kg * qty
        elif unit == 'kg':
            total_kg += qty  # Already in kg
        elif unit == 'L':
            # Need density, or skip
            unknown_count += 1
        else:
            unknown_count += 1

    return total_kg, unknown_count
```

**Display:**
```
Total imported mass: ~148.5 kg (3 items with unknown mass)
```

### Option B: Full Accounting

Track both mass and "mass unknown":
```
Total imported mass: 148.5 kg known + 3 items unknown
  Known: labor_bot_general_v0 (120.0 kg), harmonic_drive_reducer_medium (12.0 kg), ...
  Unknown: cable_drag_chain, led_ring_light, touch_sensor_capacitive
```

### Option C: Require Mass on All Items

Add validation rule requiring `mass` field on all items, but this is too strict (some items like `process_power` don't have meaningful mass).

## Implementation Tasks

- [ ] Locate mass calculation code in simulation display
- [ ] Implement mass lookup with None handling
- [ ] Add unit conversion for common units (kg, unit, L)
- [ ] Update display to show "X items with unknown mass"
- [ ] Add test case for mass calculation
- [ ] Document which items need mass data added

## Test Cases

**Test 1: Items with known mass**
```python
def test_import_mass_calculation_known():
    sim = create_simulation("test")
    sim.import_item("labor_bot_general_v0", 1, "unit")  # mass: 120 kg
    sim.import_item("steel_plate", 50, "kg")  # mass: 50 kg (direct)

    state = sim.get_state()
    assert state['total_imported_mass_kg'] == 170.0
    assert state['unknown_mass_count'] == 0
```

**Test 2: Items with unknown mass**
```python
def test_import_mass_calculation_unknown():
    sim = create_simulation("test")
    sim.import_item("item_without_mass", 1, "unit")
    sim.import_item("labor_bot_general_v0", 1, "unit")  # mass: 120 kg

    state = sim.get_state()
    assert state['total_imported_mass_kg'] == 120.0
    assert state['unknown_mass_count'] == 1
```

**Test 3: Mixed units**
```python
def test_import_mass_calculation_mixed_units():
    sim = create_simulation("test")
    sim.import_item("labor_bot_general_v0", 2, "unit")  # 2 × 120 kg = 240 kg
    sim.import_item("aluminum_alloy_ingot", 50, "kg")  # 50 kg

    state = sim.get_state()
    assert state['total_imported_mass_kg'] == 290.0
```

## Acceptance Criteria

- [ ] `view-state` shows accurate total imported mass
- [ ] Handles items with missing mass data gracefully
- [ ] Notes count of items with unknown mass
- [ ] All three test cases pass
- [ ] Documentation updated

## Related

- **Simulation**: `echo_genesis_934` (Labor Bot ISRU Manufacturing Test)
- **Report**: `simulations/echo_genesis_934/SIMULATION_REPORT.md`
- **Related Metric**: ISRU ratio calculation for mission planning
