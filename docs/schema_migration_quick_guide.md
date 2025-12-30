NOTE: Migration/analysis document for pre-ADR-012 schema. See docs/kb_schema_reference.md for current rules.

# Schema Migration Quick Guide (ADR-012/014)

Quick reference for migrating processes from old schema to ADR-012/014 format.

**⭐ For complete documentation, see `docs/README.md` Energy and Time Models section.**

## Migration Checklist

When fixing a validation error on a process:

1. [ ] Add `process_type: continuous` or `batch`
2. [ ] Update `time_model` format (see below)
3. [ ] Update `energy_model` format (see below)
4. [ ] Infer `scaling_basis` from inputs/outputs
5. [ ] Validate: `python -m src.cli validate --id process:regolith_mining_highlands_v0`
   - Find process IDs: `ls kb/processes/` or `grep "^id:" kb/processes/*.yaml`

## 1. Add Process Type (REQUIRED)

Every process needs `process_type`:

```yaml
# Add this field:
process_type: continuous  # or: batch

# How to decide:
# - continuous: Rate-based, steady-state (crushing, machining, distillation)
# - batch: Discrete batches with setup (assembly, firing, molding)
```

## 2. Migrate Time Model

### Continuous Process (OLD → NEW)

**OLD format:**
```yaml
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # ❌ Deprecated field name
```

**NEW format:**
```yaml
process_type: continuous  # ✅ Add this
time_model:
  type: linear_rate
  rate: 10.0              # ✅ Just the number
  rate_unit: kg/hr        # ✅ Unit as separate field
  scaling_basis: input_material  # ✅ Which input/output drives time
```

**Another OLD format:**
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 0.1  # ❌ Deprecated (inverse rate)
```

**NEW format:**
```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: 10.0      # ✅ Invert: 1 / 0.1 = 10.0
  rate_unit: kg/hr
  scaling_basis: input_material
```

### Batch Process (OLD → NEW)

**OLD format:**
```yaml
time_model:
  type: fixed_time  # ❌ Old type name
  hr_per_batch: 1.5
```

**NEW format:**
```yaml
process_type: batch  # ✅ Add this
time_model:
  type: batch        # ✅ New type name (not 'fixed_time')
  hr_per_batch: 1.5
  setup_hr: 0.0      # ✅ Optional, can omit if 0
```

## 3. Migrate Energy Model

### Per-Unit Energy (OLD → NEW)

**OLD format:**
```yaml
energy_model:
  type: kWh_per_kg  # ❌ Old type name
  value: 0.3
```

**NEW format:**
```yaml
energy_model:
  type: per_unit    # ✅ New type name
  value: 0.3
  unit: kWh/kg      # ✅ Compound unit with "/"
  scaling_basis: input_material  # ✅ Which input/output drives energy
```

### Fixed Per Batch (OLD → NEW)

**OLD format:**
```yaml
energy_model:
  type: kWh_per_batch  # ❌ Old type name
  value: 120.0
```

**NEW format:**
```yaml
energy_model:
  type: fixed_per_batch  # ✅ New type name
  value: 120.0
  unit: kWh              # ✅ Simple unit (no "/kg" part)
```

## 4. Inferring scaling_basis

**Rule:** `scaling_basis` must be an `item_id` from the process's inputs or outputs.

### Single Input (Easy)

```yaml
inputs:
  - item_id: regolith_coarse
    qty: 1.0
    unit: kg

# Scaling basis is obvious:
time_model:
  scaling_basis: regolith_coarse
energy_model:
  scaling_basis: regolith_coarse
```

### Multiple Inputs (Choose Primary)

```yaml
inputs:
  - item_id: steel_sheet
    qty: 10.0
    unit: kg
  - item_id: cutting_fluid
    qty: 0.5
    unit: L    # Minor consumable

# Choose the primary material:
time_model:
  scaling_basis: steel_sheet  # Not cutting_fluid
energy_model:
  scaling_basis: steel_sheet
```

**How to choose:**
- Use the **primary material** being processed (not lubricants/consumables)
- For chemical processes, use the **limiting reactant**
- For assembly, use the **main component**
- When in doubt, use the **largest mass input**

### Output Scaling (Less Common)

```yaml
# Electrolysis: water → hydrogen + oxygen
inputs:
  - item_id: water
    qty: 1.0
    unit: kg
outputs:
  - item_id: hydrogen_gas
    qty: 0.111
    unit: kg
  - item_id: oxygen_gas
    qty: 0.889
    unit: kg

# Can scale by input OR output:
time_model:
  scaling_basis: water  # Common: use input
energy_model:
  scaling_basis: water  # Often same as time_model
```

## 5. Unit Conversions

### Rate Unit Format

**Format:** `<unit>/<time_unit>`

**Valid examples:**
- `kg/hr` — Most common
- `L/hr` — For liquids
- `unit/hr` — For count-based (natural: 12 unit/hr, not 0.083 hr/unit)
- `m/hr` — For linear processes
- `L/min` — Converted to /hr internally

**Invalid:**
- `kg per hour` ❌ (use `/` not `per`)
- `kg/h` ❌ (use `hr` not `h`)

### Energy Unit Format

**For per_unit type:** `<energy>/<unit>`
- `kWh/kg` — Most common
- `kWh/unit` — For count-based
- `MJ/kg` — Alternative energy unit
- `kWh/L` — For liquids

**For fixed_per_batch type:** Simple energy unit (no `/`)
- `kWh` — Most common
- `MJ` — Alternative

## 6. Complete Migration Example

**BEFORE (Old Schema):**
```yaml
id: metal_casting_basic_v0
kind: process
# ❌ Missing process_type
inputs:
  - item_id: steel_liquid
    qty: 1.0
    unit: kg
outputs:
  - item_id: steel_ingot
    qty: 1.0
    unit: kg
time_model:
  type: fixed_time  # ❌ Old type name
  hr_per_batch: 1.5
energy_model:
  type: kWh_per_kg  # ❌ Old type name
  value: 3.5
```

**AFTER (New Schema):**
```yaml
id: metal_casting_basic_v0
kind: process
process_type: batch  # ✅ Added

inputs:
  - item_id: steel_liquid
    qty: 1.0
    unit: kg
outputs:
  - item_id: steel_ingot
    qty: 1.0
    unit: kg

time_model:
  type: batch  # ✅ New type name
  hr_per_batch: 1.5

energy_model:
  type: per_unit  # ✅ New type name
  value: 3.5
  unit: kWh/kg    # ✅ Compound unit
  scaling_basis: steel_liquid  # ✅ Inferred from input
```

## 7. Common Validation Errors

After migration, check for these:

1. **`process_type_required`** → Add `process_type: continuous` or `batch`
2. **`energy_model_type_invalid`** → Change `kWh_per_kg` to `per_unit`
3. **`required_field_missing`** → Add `scaling_basis`, `unit`, `rate_unit`
4. **`deprecated_field`** → Remove `rate_kg_per_hr`, `hr_per_kg`, use new format
5. **`invalid_compound_unit`** → Use `/` format: `kg/hr`, not `kg per hr`
6. **`scaling_basis_not_found`** → Ensure `scaling_basis` matches an actual input/output `item_id`

## Quick Validation

After fixing a process:

```bash
# Validate specific process (replace with your process ID)
python -m src.cli validate --id process:regolith_mining_highlands_v0

# Check if error is gone (replace with your process ID)
grep "process:regolith_mining_highlands_v0" out/validation_issues.jsonl
# Should return nothing if fixed

# Find process IDs:
ls kb/processes/
# or: grep "^id:" kb/processes/*.yaml
```

## Need More Help?

- **Complete schema reference**: `docs/README.md` → Energy and Time Models section
- **Validation rules**: `docs/README.md` → Validation Rules section
- **Full specification**: `docs/ADRs/ADR-012-process-types-and-time-model.md`
- **Energy details**: `docs/ADRs/ADR-014-energy-model-redesign.md`
