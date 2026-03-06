# Electrostatic Separator Machine Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/03_electrostatic_separator_machine.md`
Purpose: citation-grade mapping from report architecture to concrete KB machine/part/BOM/recipe entries.

## 1) Source extraction summary
The result file defines a first-generation lunar electrostatic separator as:
- tribocharger + parallel-plate free-fall separation (recommended baseline)
- positioned downstream of comminution/sizing and often magnetic pre-separation
- requiring feed conditioning, HV field region, sealed collection, and interlocked controls

Key report constraints to preserve in KB:
- explicit HV safety chain (enclosure/interlocks, discharge path, monitoring)
- explicit feed path (metered feeder, deagglomeration, controlled drop)
- modular cassette behavior and maintainable wear parts

## 2) Existing KB coverage audit (reuse targets)
Reusable existing IDs:
- machines:
  - `vibratory_feeder_v0`
  - `magnetic_separator_drum_v0`
  - `screening_equipment`
- parts:
  - `separator_frame`
  - `hopper_feed_system`
  - `collection_hopper_set`
  - `hv_rectifier_stack`
  - `transformer_power_high_voltage`
  - `hv_enclosure_and_interlocks`
  - `sensor_suite_general`
  - `control_compute_module_imported`
  - `fastener_kit_medium`

Coverage gap:
- no electrostatic-separation machine ID
- no explicit tribocharger module
- no explicit electrostatic plate electrode assembly
- no explicit sealed multi-bin carousel for split collection
- no integrated 30 kV-class supply module for this machine context

## 3) Recommended KB structure for result 03
### New machine layer
- `electrostatic_separator_v0`
- `bom_electrostatic_separator_v0`
- `recipe_machine_electrostatic_separator_v0`

### New part layer
- `tribocharger_module_v0`
- `separator_plate_electrode_set_v0`
- `hv_supply_module_30kv_v0`
- `sealed_bin_carousel_v0`

### New recipe layer
- `recipe_tribocharger_module_v0`
- `recipe_separator_plate_electrode_set_v0`
- `recipe_hv_supply_module_30kv_v0`
- `recipe_sealed_bin_carousel_v0`

## 4) Machine decomposition (authoritative for KB edits)
`electrostatic_separator_v0` should be represented as these major build blocks:
1. Structural chassis and enclosure interface:
   - `separator_frame`
   - mounting and guarding through `hv_enclosure_and_interlocks`
2. Feed conditioning and introduction:
   - `vibratory_feeder_v0`
   - `hopper_feed_system`
   - `tribocharger_module_v0`
3. Separation field:
   - `separator_plate_electrode_set_v0`
   - `hv_supply_module_30kv_v0`
4. Product collection:
   - `sealed_bin_carousel_v0`
   - optional shared `collection_hopper_set` interfaces
5. Control and instrumentation:
   - `sensor_suite_general`
   - `control_compute_module_imported`

## 5) Part-level design intent
### `tribocharger_module_v0`
- Represents replaceable tribocharging contact geometry and channel set.
- Built from steel structural stock + ceramic insulation + wiring + fasteners.

### `separator_plate_electrode_set_v0`
- Represents matched electrode plates + standoff/insulation hardware + harness.
- Built from structural steel, ceramic insulators, and electrical wiring hardware.

### `hv_supply_module_30kv_v0`
- Integrates existing HV transformer + rectifier + enclosure/interlocks into one machine-ready module.
- Keeps semiconductor-heavy leaves at existing imported/legacy boundaries; avoids new black-box machine import.

### `sealed_bin_carousel_v0`
- Represents multi-bin sealed collection tray/carousel for split fractions.
- Built from structural sheet + hopper/collection components.

## 6) Simulator-facing implications
- Result 03 should only introduce the machine/manufacturing chain.
- Operational beneficiation process should be added in result 04 and reference:
  - `electrostatic_separator_v0`
  - upstream prep machines (`screening_equipment`, crusher chain, optional magnetic separator)

## 7) Conservative-mode compliance notes
- Reused existing separator/HV/feed parts where functionally equivalent.
- Added only the minimum new modules required to express distinct electrostatic separator physics and maintainability.
- Did not create placeholder-only machine IDs.

## 8) Validation checklist for result 03 implementation
- `python -m src.cli validate --id item:electrostatic_separator_v0`
- `python -m src.cli validate --id item:tribocharger_module_v0`
- `python -m src.cli validate --id item:separator_plate_electrode_set_v0`
- `python -m src.cli validate --id item:hv_supply_module_30kv_v0`
- `python -m src.cli validate --id item:sealed_bin_carousel_v0`
- full index after 03 edits to catch cross-file reference issues.
