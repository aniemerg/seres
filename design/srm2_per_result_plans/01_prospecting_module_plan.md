# 01 Prospecting Module + Kapvik Rover - Detailed KB Integration Plan

## Goal
Represent the report's "Kapvik-class rover + prospecting payload" in KB with:
- realistic major subsystems
- recipe-level multi-step construction (not single-step placeholders)
- process-level operations that schedule rover + tools
- conservative reuse of existing KB items where practical

This plan explicitly includes **updating existing Kapvik/rover recipes and BOMs**.
Detailed technical basis is documented in:
- `design/srm2_per_result_plans/01_kapvik_prospecting_detailed_research_report.md`

## Modeling rule for this plan (schema-consistent)
- **Recipe**: defines how an item is built across multiple steps.
- **Process**: defines one operation and required machine capacity/resources.
- For construction chains, prefer:
  - new/updated recipes composed of existing generic processes where possible
  - add a new process only when a distinct operation is needed in simulation

Reference basis: `docs/kb_schema_reference.md` and `docs/README.md` recipe/process guidance.

## Source Scope Summary (report 01 + report 02 re-read)
In-scope first-generation capability:
- standoff magnetic sensing
- spectral/context sensing
- shallow sampling/geotech probing
- rover-mounted, serviceable modularity

Added from re-read:
- dual-fluxgate boom architecture, station-mode measurement concept, and calibration workflow from report 02
- named Kapvik drivetrain/sensor evidence from the appended inferred-BOM section in report 01

Out of scope:
- deep drill and mini-lab in first pass

## Current KB Audit (Kapvik and adjacent)
### Existing IDs directly relevant
- Machine: `kapvik_microrover_30kg_v0`
- Recipe/BOM: `recipe_kapvik_microrover_30kg_v0`, `bom_kapvik_microrover_30kg_v0`
- Related rover parts:
  - `rover_wheel_assembly_v0`
  - `rover_suspension_rocker_bogie_v0`
  - `rover_chassis_structure_v0`
  - `rover_solar_array_v0`
  - `rover_power_system_battery_v0`
  - `rover_avionics_computer_v0`
- Related sensing machines:
  - `gamma_ray_spectrometer_v0` (import)
  - `nife_meteorite_magnetic_detection_v0` (placeholder)
  - `wheel_load_cell_system_v0`

### Quality gaps / inconsistencies that block high-fidelity use
1. `kapvik_microrover_30kg_v0` recipe is a single-step generic assembly.
2. Kapvik BOM uses **4 wheels**, while existing rover suspension notes describe **6-wheel rocker-bogie**.
3. Kapvik BOM references generic `battery_pack_medium` and `microcontroller_or_embedded_board` while rover-specific parts exist (`rover_power_system_battery_v0`, `rover_avionics_computer_v0`).
4. `rover_chassis_structure_v0` exists but is not used in the Kapvik recipe/BOM.
5. `rover_suspension_rocker_bogie_v0` exists but is not used in Kapvik BOM/recipe.
6. Some rover-adjacent machines are import or placeholder with weak BOM coupling (`gamma_ray_spectrometer_v0`, `rover_communication_system_v0`).
7. `wheel_load_cell_system_v0` has duplicate/placeholder BOM artifacts and likely needs normalization later (not a blocker for this phase).

## Decision
Do two linked upgrades:
1. **Normalize Kapvik rover definition first** (existing ID, no ID replacement).
2. **Add a modular prospecting payload chain** that mounts onto Kapvik.

This preserves existing simulation references while increasing fidelity.

## Proposed KB Deltas (Detailed)
### A) Update existing Kapvik rover chain (in-scope edits)
#### Files to update
- `kb/boms/bom_kapvik_microrover_30kg_v0.yaml`
- `kb/recipes/recipe_kapvik_microrover_30kg_v0.yaml`
- `kb/items/machines/kapvik_microrover_30kg_v0.yaml` (notes/capabilities only)

#### BOM updates (major parts)
- Replace wheel count with 6 for rocker-bogie consistency.
- Replace generic battery/computer references with rover-specific parts where possible.
- Add currently missing structural subsystems:
  - `rover_chassis_structure_v0` (qty 1)
  - `rover_suspension_rocker_bogie_v0` (qty 1)
  - `rover_power_system_battery_v0` (qty 1)
  - `rover_avionics_computer_v0` (qty 1)
- Keep conservative imported blocks where local chain is not mature (e.g., advanced sensor electronics).

#### Recipe redesign (multi-step, not monolithic)
Replace single `assembly_basic_v0` step with staged steps such as:
1. `recipe_rover_chassis_structure_v0` output integration step
2. suspension integration (use `rover_suspension_rocker_bogie_v0`)
3. wheel + drive subsystem integration (6 wheel assemblies + motors + encoders)
4. power subsystem integration (`rover_power_system_battery_v0`, `rover_solar_array_v0`)
5. avionics/communications harnessing and checkout
6. final rover calibration and mobility acceptance

Use existing generic processes where available (`assembly_basic_v0`, `machining_finish_basic_v0`, alignment/testing processes). Add new process only where truly missing for rover acceptance testing.

### B) Add modular prospecting payload chain
#### New IDs
- Part: `prospecting_module_v0`
- Recipe: `recipe_prospecting_module_v0`
- BOM: `bom_prospecting_module_v0`

#### Optional submodules (recommended for maintainability)
- `magnetometer_payload_v0` (part)
- `spectral_imaging_payload_v0` (part)
- `shallow_sampler_geotech_head_v0` (part)

If submodule scope is too large for first pass, keep them as BOM components in `prospecting_module_v0` with imported placeholders and explicit notes.

#### Prospecting module recipe structure (multi-step)
1. structural frame and mount fabrication
2. sensor payload integration (mag + spectral context)
3. shallow sampler/geotech tool integration
4. wiring and control interface integration
5. dust/thermal protection integration
6. module-level calibration and acceptance test

### C) Process-level operations (simulation operations, not build recipes)
Add operation process for use during simulation:
- `prospecting_site_qualification_v0`

This process should:
- require `kapvik_microrover_30kg_v0` in `resource_requirements`
- require mounted `prospecting_module_v0` (as consumable/required item per current modeling pattern)
- output physical prospecting artifacts only if needed for closure logic (e.g., sampled regolith material variant)

Avoid forcing non-physical "software only" outputs unless they are needed as explicit simulation gating artifacts.

## Process/Machine Requirements for Operations
For `prospecting_site_qualification_v0`:
- Required machine: `kapvik_microrover_30kg_v0`
- Required module/parts:
  - `prospecting_module_v0`
  - optional `gamma_ray_spectrometer_v0` or `nife_meteorite_magnetic_detection_v0` depending on chosen sensing route
- Optional consumables:
  - replaceable sampler bits / wear kits (if modeled)

## Mapping of Report Components to KB (Reuse vs Add)
- Rover base platform: **reuse/update existing** `kapvik_microrover_30kg_v0`.
- Rocker-bogie: **reuse existing** `rover_suspension_rocker_bogie_v0`.
- Wheels: **reuse existing** `rover_wheel_assembly_v0`, update quantity and integration.
- Power: **reuse existing** `rover_power_system_battery_v0`, `rover_solar_array_v0`.
- Magnetics payload:
  - short term: can map to `nife_meteorite_magnetic_detection_v0` only as placeholder
  - preferred: add dedicated `magnetometer_payload_v0` under this report sequence
- Gamma-ray spectrometer:
  - keep as import support payload (`gamma_ray_spectrometer_v0`) unless localization is later scoped.

## Implementation Order (for this result only)
1. Normalize Kapvik BOM consistency (wheel count, subsystem coverage, part references).
2. Expand `recipe_kapvik_microrover_30kg_v0` to staged build.
3. Add `prospecting_module_v0` BOM + recipe (first-gen option A scope).
4. Add `prospecting_site_qualification_v0` operation process.
5. Validate all touched IDs with `python -m src.cli validate --id ...`.
6. Run full index and check for new queue regressions.

## Validation / Acceptance Criteria
1. Kapvik chain no longer single-step assembly-only.
2. Kapvik BOM and recipe are internally consistent with a rocker-bogie rover architecture.
3. Prospecting payload is represented as a buildable module with major parts.
4. Prospecting operation can be scheduled with explicit machine requirements.
5. No unresolved ID references introduced.

## Open Issues to Resolve Before Editing KB
1. Should Kapvik remain nominally "30kg" ID/name while using report data that cites ~41 kg class context? (Recommendation: keep ID unchanged; document mass basis in notes.)
2. For first pass, do you want dedicated submodule IDs (`magnetometer_payload_v0`, etc.) now, or a single integrated `prospecting_module_v0` with internal BOM placeholders?
3. Should we immediately localize any currently imported sensor machine in this chain, or keep import-first and focus on rover/platform realism first?

## Immediate Next Action
Implement this plan in KB for result 01 only (including existing Kapvik recipe/BOM updates), then re-index and review before moving to result 02.
