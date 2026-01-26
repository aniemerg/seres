# Parts and Labor Modeling Guidelines

**Status**: Official Policy
**Version**: 1.0
**Last Updated**: 2025-12-21
**Supersedes**: `design/memos/parts_and_labor_guidelines.md`

## Overview

This document defines the core philosophy and practices for modeling parts, BOMs (Bills of Materials), and labor in the self-replicating system knowledge base. These guidelines are fundamental to keeping the KB tractable, minimizing combinatorial explosion, and ensuring the dependency graph remains computable.

**Key Principle**: Minimize the number of similar items (parts, machines, materials) by aggressive reuse while preserving material and process compatibility.

**Note:** These principles originated for parts but are now extended to **all item types** through [Conservative Mode](conservative_mode_guide.md), the default approach for queue work.

---

## Table of Contents

1. [Parts Philosophy](#parts-philosophy)
2. [Part Reuse Policy](#part-reuse-policy)
3. [Material Class System](#material-class-system)
4. [BOMs (Bills of Materials)](#boms-bills-of-materials)
5. [Labor Modeling](#labor-modeling)
6. [Workflow for Creating Parts/BOMs](#workflow-for-creating-partsboms)
7. [Common Reusable Components](#common-reusable-components)

---

## Parts Philosophy

### Core Principles

1. **One part = one identifiable thing**
   - Avoid "miscellaneous" buckets or vague groupings
   - Each part should represent a specific, nameable component
   - Exception: Kits for near-substitutable items (fasteners, gaskets)

2. **Always include estimated mass**
   - Within 5× of reality is acceptable for this modeling exercise
   - Do NOT leave masses null
   - Add `notes` field with provenance if guessed or uncertain
   - Example: `mass: 2.5  # AI estimate, typical 5kW motor ~2-3 kg`

3. **Prefer reuse over creation**
   - **CRITICAL**: Always check existing parts before creating new ones
   - Part proliferation is the primary threat to KB tractability
   - See [Part Reuse Policy](#part-reuse-policy) below

4. **Structure before precision**
   - Coarse estimates are acceptable if they preserve dependency structure
   - Capture uncertainty in `notes` or `source_tags` fields
   - Priority: correct relationships > exact numbers

---

## Part Reuse Policy

### ALWAYS Check Inventory First

**Before creating any new part**, you MUST:

1. **Check the inventory report**: `out/reports/inventory.md`
   ```bash
   # Regenerate if stale
   .venv/bin/python -m kbtool report inventory

   # Search for similar parts
   grep -i "motor\|bearing\|wire" out/reports/inventory.md
   ```

2. **Search by function and material class**
   - Look for parts with similar function (e.g., all motors, all bearings)
   - Check material compatibility (steel vs aluminum vs ceramic)
   - Review mass/size ranges

3. **Only create new parts if no reasonably equivalent part exists**

### Reasonable Equivalence Criteria

Parts are considered **reasonably equivalent** (and SHOULD be shared/reused) when:

#### ✅ Magnitude Within ~5×

Since this is an approximation exercise, differences less than 5× in dimensions, mass, or capability are essentially the same:

- **Structural components**: A strut and a strut 3× longer → **same part ID**
- **Motors/actuators**: 5 kW motor vs 10 kW motor → **same part ID**
- **Gears/bearings**: Aluminum gear vs similar gear 2× larger → **same part ID**
- **Mass variations**: 2 kg component vs 8 kg component → **same part ID** (within 5×)

**Rationale**: The goal is to model dependency structure, not precision manufacturing. Small variations are noise at the system level.

#### ✅ Shape Variations, Same Purpose

Parts that vary in shape but serve the same function and use similar construction methods:

- Support frame with cross beams vs without cross beams → **same part ID**
- Different pump housing geometries (same material, same process) → **same part ID**
- Bracket variations for different mounting points → **same part ID**

**Action**: Document specific differences in BOM/recipe `notes` field if relevant.

#### ✅ Similar Construction/Function

Parts made the same way and serving the same purpose:

- Different pump types (vacuum pump vs water pump) → **same part ID IF materials compatible**
- Various sensor mounts with same structural requirements → **same part ID**
- Cable harnesses of different lengths (same wire gauge/insulation) → **same part ID**

#### ❌ NOT Equivalent: Material Incompatibility

Parts are **NOT equivalent** when material properties matter for function or process compatibility:

- **Steel beam ≠ plastic beam** (structural strength differs)
- **Electrical conductor ≠ electrically resistive material** (function differs)
- **High-temp component ≠ low-melting material** (process incompatible)
- **Corrosion-resistant alloy ≠ reactive metal** (environment incompatible)

**Key Test**: Would substituting materials cause failure in the target process (melting, corrosion, mechanical failure, electrical malfunction)?

#### ❌ NOT Equivalent: Process Requirements Conflict

- Cannot substitute if material would fail in the target process
- Temperature limits (melting, thermal expansion)
- Chemical compatibility (acids, oxidation)
- Mechanical properties (strength, hardness, ductility)

### When Reusing Parts with Different Specs

If reusing a part with different specifications than originally defined:

1. Add variation details to the **BOM `notes`** field or **recipe `notes`** field
2. Example:
   ```yaml
   components:
     - item_id: motor_general_5kw
       qty: 1
       unit: unit
       notes: "Using general 5kW motor; this application needs ~8kW so slightly undersized, acceptable for approximation"
   ```

---

## Material Class System

### Purpose

The `material_class` field enables **generic substitution** in processes and recipes, dramatically reducing part proliferation.

**Problem Solved**: Without material classes, every specific material type (e.g., `regolith_lunar_mare`) must exactly match process inputs (e.g., `raw_ore_or_regolith`), creating fragile dependencies.

**Solution**: Items with the same `material_class` can substitute for each other in processes, enabling flexible material flows.

### How It Works

Items define a `material_class` field:

```yaml
# kb/items/materials/regolith_lunar_mare.yaml
id: regolith_lunar_mare
kind: material
material_class: regolith  # Generic class
material_subclass: lunar_regolith  # Optional refinement
composition:
  FeO: 0.15
  TiO2: 0.10
```

```yaml
# kb/items/materials/raw_ore_or_regolith.yaml
id: raw_ore_or_regolith
kind: material
material_class: regolith  # Same class
```

The simulation engine can match materials in two steps (disabled by default; exact match only unless explicitly enabled in the engine):

1. **Exact match**: Try exact `item_id` in inventory
2. **Class match**: If not found, search inventory for items with matching `material_class`

### Common Material Classes

Found in the KB (256+ materials already use this):

- `regolith`: Various regolith types (mare, highland, carbonaceous, silicate)
- `metal`: Steel, aluminum, copper, iron, etc.
- `raw_metal_block`: Generic metal stock (enables iron → steel substitution)
- `ceramic`: Alumina, zirconia, silicate ceramics
- `polymer`: Silicone, plastics, elastomers
- `glass`: Various glass compositions
- `composite`: Fiber-reinforced materials

### Why This Matters for Parts

Material classes allow recipes to specify generic inputs:

```yaml
# Instead of:
inputs:
  - item_id: steel_304_sheet  # Too specific!

# Use:
inputs:
  - item_id: metal_sheet_structural  # Has material_class: metal
    # Now accepts steel, aluminum, iron - whatever's available
```

**Impact**: Recipes become more flexible, reducing the need for variant recipes and duplicate parts.

### When to Use Material Classes vs Specific Materials

- **Use specific material** when composition matters (e.g., electrical conductivity, chemical reactivity)
- **Use material class** for structural, bulk, or functionally-equivalent applications
- **Document assumptions** in `notes` if using generic class for specific application

---

## BOMs (Bills of Materials)

### BOM Structure

BOMs enumerate parts and materials with quantities:

```yaml
id: bom_ball_mill_v0
owner_item_id: ball_mill_v0
components:
  - item_id: motor_general_5kw
    qty: 1
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2
    unit: unit
  - item_id: steel_drum_rotating
    qty: 1
    unit: unit
    mass: 150  # Optional: override if different from item definition
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
scrap_rate: 0.02  # Optional: 2% material loss during assembly
notes: "Simplified BOM; grinding media not yet included"
```

### BOM Best Practices

1. **Use kit parts for long-tail items**
   - Fasteners, gaskets, small hardware → `fastener_kit_medium`
   - Still point to identifiable part IDs (kits are real items in KB)

2. **Keep scrap rates explicit when known**
   - If unknown, omit (don't guess wildly)
   - Typical assembly scrap: 1-5%
   - Typical casting/machining scrap: 10-20%

3. **Prefer reusable parts** (see [Common Reusable Components](#common-reusable-components))

4. **Allow intentional incompleteness early**
   - Missing components are acceptable during modeling
   - Flag with `notes: "BOM incomplete - missing XYZ"`
   - Indexer will surface gaps

5. **Avoid premature BOM explosion**
   - Only create detailed BOMs when:
     - Item appears in top-N contributors (mass/energy/time)
     - Item is a bottleneck machine
     - Item is needed for simulation/recipe validation

6. **Software and digital items are NOT BOM components**
   - ❌ DO NOT include: software, source code, executables, algorithms, licenses
   - ❌ DO NOT include: abstract resources (compute time, data streams)
   - ✅ DO include: programmed microcontrollers (physical hardware with loaded firmware)
   - ✅ DO include: storage media with data if physically manufactured (ROM chips, etc.)
   - **Rationale**: BOMs track physical mass flow; software has no mass and breaks material closure analysis
   - **For firmware**: Treat programming as a recipe process step, not a BOM component

---

## Labor Modeling

### Philosophy

Labor is modeled as **explicit machine-hours** from **replicable robots** (labor bots), not abstract human labor.

**Rationale**: In a self-replicating system, labor capacity must itself be manufactured. Treating labor as machines:
- Makes labor capacity explicit in dependency graph
- Enables accounting for labor bot construction
- Allows scheduling/bottleneck analysis
- Maintains consistency with "replicate everything" policy

### Labor as Resource Requirements

Processes and recipes specify labor using `resource_requirements`:

```yaml
id: assembly_basic_v0
kind: process
name: Basic assembly
resource_requirements:
  - resource_type: labor_bot_general
    amount: 2.0
    unit: hr
  - resource_type: assembly_tools_basic
    amount: 1
    unit: unit
notes: "Manual assembly tasks: fitting, fastening, alignment"
```

### Current Labor Bots

The KB defines several labor bot types:

| Labor Bot | Mass | Capabilities | Notes |
|-----------|------|-------------|-------|
| `labor_bot_general_v0` | 120 kg | Assembly, quality control, material handling, mechanical/electrical assembly | 6-DOF industrial manipulator, 2m reach, 20kg payload, ±0.5mm repeatability. Detailed specs in kb/items/machines/labor_bot_general_v0.yaml |
| `labor_bot_basic_v0` | 120 kg | Simple tasks | Lightweight worker for basic operations |
| `labor_bot_specialist_v0` | 180 kg | High-skill programming, debugging, domain-specific tasks | Specialist for complex operations |
| `labor_bot_welder` | ? | Welding operations | Specialized for welding processes |
| `labor_bot_electronics` | ? | Electronics assembly | Specialized for electronics work |

**Primary bot**: `labor_bot_general_v0` is the most well-specified and should be the default for general assembly/manufacturing tasks.

### Labor Tier Guidelines

**Current policy**: Start with one general labor bot (`labor_bot_general_v0`).

**When to add new labor tiers**:
- Only add specialized labor bots if required capabilities differ by **>5×** from the general bot:
  - Payload capacity (heavy lift: >100 kg vs general 20 kg)
  - Precision (ultra-precise: <0.05 mm vs general ±0.5 mm)
  - Speed (high-speed pick-and-place vs general manipulation)
  - Environment (vacuum-rated, high-temp, etc.)

**Note**: Full tier specification is still evolving. Use judgment and document assumptions in `notes`.

### Sensors and Compute

- **Sensors should be explicit**: List major sensor components in BOMs (cameras, lidar, force sensors)
- **Compute can be imported**: Control computers/AI modules can be marked as imported items
  - Still list them in BOMs (e.g., `control_compute_module_imported`)
  - Don't hide compute; make imports explicit

---

## Workflow for Creating Parts/BOMs

### Step-by-Step Process

1. **Identify the need**
   - Working on a recipe/BOM and need a component
   - Identified gap from work queue

2. **Search existing parts** (MANDATORY)
   ```bash
   # Regenerate inventory if stale
   .venv/bin/python -m kbtool report inventory

   # Search by keyword
   grep -i "motor" out/reports/inventory.md
   grep -i "bearing" out/reports/inventory.md

   # Search by material class (in YAML files)
   grep -r "material_class: metal" kb/items/parts/
   ```

3. **Evaluate equivalence**
   - Check [Reasonable Equivalence Criteria](#reasonable-equivalence-criteria)
   - Ask: "Is an existing part within 5× magnitude?"
   - Ask: "Would material substitution cause process failure?"
   - **When in doubt, reuse**

4. **If reusing**: Document in BOM/recipe notes
   ```yaml
   components:
     - item_id: motor_general_5kw
       qty: 1
       unit: unit
       notes: "This application needs ~3kW; 5kW motor oversized but acceptable"
   ```

5. **If creating new part**:
   - Choose clear, descriptive ID (lowercase, snake_case)
   - Include estimated mass (within 5× is fine)
   - Add `material_class` for generic substitution
   - Add `notes` with provenance
   ```yaml
   id: motor_specialty_100kw
   kind: part
   name: Specialty high-power motor
   mass: 450  # AI estimate, scaled from 5kW motor
   unit: kg
   material_class: motor
   notes: |
     Created for applications requiring >50kW where motor_general_5kw
     inadequate (>5× threshold). Estimate based on scaling laws.
     Source: ai_estimate
   ```

6. **Run indexer and verify**
   ```bash
   python -m src.cli index
   # Check for new gaps, validation warnings
   ```

---

## Common Reusable Components

The following parts are designed for broad reuse across BOMs and recipes. **Always prefer these over creating new parts**:

### Structural
- `support_frame_welded` — General structural frames
- `mounting_bracket_steel` — Brackets and mounts
- `aluminum_housing` — Housings and enclosures

### Mechanical
- `bearing_set_heavy` — Heavy-duty bearings (various sizes acceptable)
- `bearing_set_small` — Small bearings
- `motor_general_5kw` — General-purpose motors (~5kW, accepts 2-10kW range)
- `drive_motor_medium` — Medium drive motors
- `gear_set_general` — General gearing

### Fasteners & Hardware
- `fastener_kit_medium` — Bolts, screws, washers (medium applications)
- `fastener_kit_small` — Small fasteners
- `gasket_set_general` — Seals and gaskets

### Electrical
- `copper_wire_general` — General copper wiring (unless gauge matters)
- `power_conditioning_module` — Power electronics
- `control_compute_module_imported` — Computing modules (imported)
- `control_panel_basic` — Control interfaces
- `cable_harness_general` — Wiring harnesses

### Sensors
- `sensor_suite_general` — General sensors (cameras, proximity, etc.)
- `force_torque_sensor_6axis` — Load sensing

### Labor
- `labor_bot_general_v0` — Primary labor resource for assembly/manufacturing

**Note**: This list is representative, not exhaustive. Check inventory for current parts.

---

## Integration with Project Principles

These guidelines directly support the project's core principles:

1. **Structure before precision** (docs/project_overview.md)
   - Part reuse preserves dependency structure while accepting coarse estimates
   - Material classes enable generic flows without exact material specs

2. **Processes before machines** (docs/project_overview.md)
   - Parts are chosen to support processes, not vice versa
   - Generic parts enable process flexibility

3. **Incompleteness is a feature** (docs/project_overview.md)
   - Missing parts/BOMs are acceptable; gaps are surfaced by indexer
   - Prefer placeholder imports over premature detailed modeling

4. **Iteration guided by bottlenecks** (docs/project_overview.md)
   - Only create detailed parts for top contributors to mass/energy/time
   - Don't model the long tail prematurely

---

## Extension to All Items: Conservative Mode

The principles in this document (particularly the Part Reuse Policy and 5× equivalence rule) have been **generalized to all KB work** through **Conservative Mode**.

**See `docs/conservative_mode_guide.md` for:**
- Decision trees for all gap types (`referenced_only`, `no_recipe`, `missing_field`, etc.)
- Labor bot vs special machine decision guide
- Phase/state variation handling (water → water_vapor, etc.)
- Complete integration with existing guidelines

Conservative Mode treats parts_and_labor_guidelines.md as the foundation and extends it to materials, machines, processes, and all other KB entities.

---

## Related Documentation

- **`docs/conservative_mode_guide.md`** — Queue work philosophy (extends these principles to all items)
- **`docs/project_overview.md`** — Project philosophy and goals
- **`docs/kb_schema_reference.md`** — Formal specification and data model
- **`docs/knowledge_acquisition_protocol.md`** — Knowledge acquisition methodology
- **`docs/material_class_system.md`** — Material class implementation details
- **`docs/README.md`** — Onboarding and workflow guide
- **`docs/labor_bot_design_memo.md`** — Labor bot specifications

---

## Questions or Exceptions?

If you encounter situations where these guidelines conflict or are unclear:

1. Document the issue in `notes` field
2. Make a conservative choice (prefer reuse, prefer generic)
3. Flag for review in work queue or PR comments
4. Update this document as precedents emerge
