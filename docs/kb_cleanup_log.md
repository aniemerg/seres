# KB Cleanup Log

Record KB cleanup decisions, consolidations, and deletions here.

Use this file for both:
- Decision entries: consolidation decisions where YAML remains active or is
  marked deprecated.
- Deletion entries: cleanup actions where YAML files are deleted after their
  complete original contents are preserved here.

Every cleanup entry should include:
- Date / agent
- Items/processes considered
- Decision and rationale
- Possible negative effects or lost distinctions
- Links to updated files (recipes/BOMs/notes)

Deletion rule:
- Do not delete a YAML entry until its original contents have been copied into
  this file.
- Do not delete a YAML entry until direct KB references have been migrated or
  explicitly judged obsolete.
- After recording the removed YAML here, the original YAML file may be deleted
  rather than retained as a deprecated KB entry.
- Run targeted validation, and preferably the indexer, after deletion.

## Entry Templates

### Decision Entry

```markdown
## YYYY-MM-DD / <agent> / <cleanup topic>

**Scope:**

**Items considered:**
- `id`

**Decision:**

**Rationale:**

**Possible negative effects or lost distinctions:**

**Files updated:**
```

### Deletion Entry

````markdown
## YYYY-MM-DD / <agent> / <entity_id> YAML Removal

- Deleted files:
  - `path/to/file.yaml`
- Entity types:
- Replacement / canonical ID:
- Validation:

### Removal Reason

### References Migrated

### Possible Negative Effects

### Removed YAML

`path/to/file.yaml`

```yaml
# Paste the complete deleted YAML content here.
```
````

## Cleanup Entries

## 2024-XX-XX — agent: codex
- Scope: Grinding/Polishing family (`surface_grinder`, `bench_grinder`, `polishing_station`).
- Decision: Prefer `surface_grinder` as default finishing tool. Mark `bench_grinder` and `polishing_station` as dedupe candidates with `alternatives: [surface_grinder]`. Retargeted finishing processes to rely on `surface_grinder` (deburring, surface finishing, mirror polishing). Surface grinder marked with `preferred_variant: simple` as default path.
- Files touched: `kb/items/machines/bench_grinder.yaml`, `kb/items/machines/polishing_station.yaml`, `kb/items/machines/surface_grinder.yaml`, `kb/processes/finishing_deburring_v0.yaml`, `kb/processes/surface_finishing_v0.yaml`, `kb/processes/mirror_polishing_v0.yaml`.

## 2024-XX-XX — agent: codex
- Scope: Plate rolling/press brake family (`rolling_mill`, `plate_rolling_mill`, `press_brake`, `press_brake_or_roller`).
- Decision: Prefer `plate_rolling_mill` as default forming tool; mark `press_brake` and `press_brake_or_roller` as dedupe candidates with alternatives pointing to the plate rolling mill (and press brake as secondary). `plate_rolling_mill` set `preferred_variant: simple`. Retargeted sheet metal processes to use `plate_rolling_mill` for forming (`sheet_metal_bending_and_forming_v0`, `sheet_metal_fabrication_v0`). Press brake/roller annotated as dedupe candidates.
- Files touched: `kb/items/machines/plate_rolling_mill.yaml`, `kb/items/machines/press_brake.yaml`, `kb/items/machines/press_brake_or_roller.yaml`, `kb/processes/sheet_metal_bending_and_forming_v0.yaml`, `kb/processes/sheet_metal_fabrication_v0.yaml`.

## 2024-12-15 / claude-worker-1 / Press Family Consolidation

**Task:** `dedupe:press_family_general`

**Machines considered:**
- `hydraulic_press` (600 kg) - general-purpose pressing/forming
- `hydraulic_press_small` (150 kg) - small press
- `press_hydraulic` (250 kg) - light/medium press
- `power_hammer_or_press_v0` (200 kg) - small power hammer/press
- `pressing_tools` (150 kg) - manual pressing tools
- `hot_press_v0` (950 kg) - hot press for sintering
- `press_brake` (1200 kg) - sheet metal bending
- `press_brake_or_roller` (300 kg) - sheet metal bending/rolling

**Decision:**
Keep 3 machines with distinct functions:
1. **`hydraulic_press`** (600 kg) - primary general-purpose press for all forming/pressing operations
2. **`hot_press_v0`** (950 kg) - specialized for high-temperature sintering/consolidation (genuinely different capability)
3. **`press_brake`** (1200 kg) - specialized for sheet metal bending operations

Consolidate into above:
- `hydraulic_press_small`, `press_hydraulic`, `power_hammer_or_press_v0`, `pressing_tools` → all use `hydraulic_press`
- `press_brake_or_roller` → use `press_brake`

**Rationale:**
- The four smaller hydraulic presses (150-250 kg) serve overlapping functions - just sizing differences, not functional differences
- Consolidating to one general-purpose `hydraulic_press` simplifies the toolchain without losing capability
- `hot_press_v0` provides genuine thermal capability needed for sintering - keep separate
- `press_brake` is specialized for sheet bending - different mechanics than general pressing
- Prefer consolidation over proliferation (Memo B principle)

**Files updated:**
- Processes: `bearing_installation_basic_v0.yaml`, `pressing_operations_basic_v0.yaml`, `metal_forming_basic_v0.yaml`, `ceramic_forming_basic_v0.yaml`, `sintering_basic_v0.yaml`, `welding_and_fabrication_v0.yaml`, `sheet_metal_fabrication_v0.yaml`
- Machines: Added DEPRECATED notes to `hydraulic_press_small.yaml`, `press_hydraulic.yaml`, `power_hammer_or_press_v0.yaml`, `pressing_tools.yaml`, `press_brake_or_roller.yaml`

**Next steps:**
- Indexer will detect deprecated machines and flag associated BOMs/recipes
- Consider removing or marking recipes/BOMs for deprecated machines as variants in future cleanup

## 2024-12-15 / claude-worker-1 / Cutting/Shear Family Consolidation

**Task:** `dedupe:cutting_shear_family`

**Machines considered:**
- `metal_cutting_saw` (250 kg) - bandsaw or cold saw for cutting metal stock
- `metal_shear_or_saw` (350 kg) - shear or bandsaw for cutting plate and sections
- `press_brake` (1200 kg) - already kept for bending (see press family consolidation)
- `press_brake_or_roller` (300 kg) - already deprecated (see press family consolidation)

**Decision:**
Keep **`metal_shear_or_saw`** (350 kg) as the primary metal cutting tool

Consolidate into above:
- `metal_cutting_saw` → use `metal_shear_or_saw`

**Rationale:**
- Both machines perform the same function: cutting metal stock for fabrication
- `metal_shear_or_saw` is more versatile (covers both shearing and sawing operations)
- No functional capability lost by consolidating
- Simpler toolchain with one cutting tool
- `press_brake` items excluded - already handled as sheet bending specialty tool

**Files updated:**
- Processes: `tube_bending_and_cutting_v0.yaml`
- Machines: Added DEPRECATED note to `metal_cutting_saw.yaml`

**Next steps:**
- Mark associated BOM/recipes as variants or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Milling/Turning Family Consolidation

**Task:** `dedupe:milling_turning_family`

**Machines considered:**
- `milling_machine_general_v0` (600 kg) - general-purpose milling, NOT used by any process
- `cnc_mill` (1200 kg) - CNC milling with precision capabilities
- `precision_lathe` (1200 kg) - precision turning, threading, and boring

**Decision:**
Keep both machines with distinct functions:
1. **`cnc_mill`** (1200 kg) - all milling operations (rotating cutter, stationary workpiece)
2. **`precision_lathe`** (1200 kg) - all turning operations (rotating workpiece, stationary cutter)

Consolidate into above:
- `milling_machine_general_v0` → use `cnc_mill`

**Rationale:**
- Milling and turning are fundamentally different machining operations with different mechanics
- Cannot consolidate lathe into mill - they perform non-overlapping functions
- `milling_machine_general_v0` is unused and redundant with `cnc_mill`
- CNC mill is more capable than general mill (programmable, precision, multi-axis)
- Both CNC mill and precision lathe are already in use by `machining_precision_v0` process

**Files updated:**
- Machines: Added DEPRECATED note to `milling_machine_general_v0.yaml`
- No process files needed updating (machine was unused)

**Next steps:**
- Mark recipe/BOM for deprecated machine as variant or remove in future cleanup

## 2026-07-15 / codex / Milling Machine YAML Removal

**Scope:** Follow-up cleanup for the milling-machine consolidation.

**Machines considered:**
- `cnc_mill` (785 kg) - canonical CNC milling machine
- `milling_machine_general_v0` (370 kg) - deprecated general milling machine
- `milling_machine_v0` (850 kg) - seed placeholder milling machine

**Decision:**
Keep **`cnc_mill`** as the only milling machine entry.

Delete:
- `milling_machine_general_v0`
- `milling_machine_v0`
- Their dedicated BOMs and recipes

**Rationale:**
- `milling_machine_general_v0` already stated it was consolidated into
  `cnc_mill`.
- `milling_machine_v0` was a seed placeholder with no process resource
  requirements outside its own BOM/recipe and seed listing.
- CNC milling is a functional superset for the migrated milling, machining,
  surface finishing, and gear-cutting operations.
- The mass range remains within the Conservative Mode 5x equivalence threshold.

**Possible negative effects or lost distinctions:**
- Removes the explicit lower-technology/manual milling-machine bootstrap path.
- May overestimate the complexity and imported control/compute burden for
  simple milling tasks.
- Concentrates simulation capacity demand onto `cnc_mill`.
- Changes the anvil-block runbook import from a 370 kg general mill to a 785 kg
  CNC mill, increasing apparent imported mass for that runbook.

**Files updated:**
- Process resource requirements using `milling_machine_general_v0` now use
  `cnc_mill`.
- `kb/items/machines/cnc_mill.yaml` lists the migrated supported processes.
- `docs/self_reproducing_set.txt` no longer lists `milling_machine_general_v0`.
- `kb/seeds/paper_reviews_dec2024_comprehensive_v0.yaml` now uses `cnc_mill`
  instead of `milling_machine_v0`.
- `simulations/anvil_block_basic_runbook/snapshot.json` and `events.jsonl` use
  `cnc_mill`.
- Full removed YAML payloads are recorded below in this file.

## 2024-12-15 / claude-worker-1 / Low-Temp Ovens Consolidation

**Task:** `dedupe:ovens_low_temp_family`

**Machines considered:**
- `drying_oven` (120 kg) - 50-300°C, drying/moisture removal, used by 2 processes
- `curing_oven` (400 kg) - low-temp for curing coatings/adhesives, used by 1 process
- `annealing_oven_small` (180 kg) - 200-900°C, annealing/stress relief, UNUSED
- `low_temp_oven` - does not exist as a machine
- `coating_drying_oven` - does not exist as a machine

**Decision:**
Keep 2 machines with distinct temperature ranges/purposes:
1. **`drying_oven`** (120 kg) - primary low-temp oven for drying and curing (50-300°C)
2. **`annealing_oven_small`** (180 kg) - heat treatment for stress relief (200-900°C, different purpose)

Consolidate into above:
- `curing_oven` → use `drying_oven`

**Rationale:**
- `drying_oven` temp range (50-300°C) fully covers curing operations (typically 50-100°C)
- Both `drying_oven` and `curing_oven` serve overlapping drying/curing functions
- `annealing_oven_small` has different purpose (stress relief heat treatment) and higher temps (up to 900°C)
- Although `annealing_oven_small` is currently unused, it provides genuine capability distinction worth preserving
- Two candidate machines (`low_temp_oven`, `coating_drying_oven`) don't exist - likely already consolidated

**Files updated:**
- Processes: `potting_and_encapsulation_v0.yaml`
- Machines: Added DEPRECATED note to `curing_oven.yaml`

**Next steps:**
- Consider using `annealing_oven_small` in heat treatment processes or remove if truly unnecessary
- Mark recipe/BOM for deprecated machine as variant or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Test Bench Family Consolidation

**Task:** `dedupe:test_bench_family`

**Machines considered:**
- `test_bench_electrical` (200 kg) - full electrical testing bench with instrumentation
- `electrical_test_equipment` (40 kg) - insulation/continuity/ground testers
- `test_equipment_electronics` (30 kg) - oscilloscopes/multimeters/signal generators
- `measurement_equipment` (30 kg) - mechanical metrology (calipers/micrometers/CMM)
- `optical_metrology_tools` (40 kg) - optical alignment tools (autocollimators/interferometers)

**Decision:**
Keep 3 machines with distinct measurement domains:
1. **`test_bench_electrical`** (200 kg) - all electrical/electronics testing (consolidates bench + portable instruments)
2. **`measurement_equipment`** (30 kg) - mechanical/dimensional measurement (different domain)
3. **`optical_metrology_tools`** (40 kg) - optical alignment (specialized for solar concentrators)

Consolidate into above:
- `electrical_test_equipment` → use `test_bench_electrical`
- `test_equipment_electronics` → use `test_bench_electrical`

**Rationale:**
- `test_bench_electrical` is a full bench setup that can include the functionality of both portable electrical and electronics test equipment
- `electrical_test_equipment` and `test_equipment_electronics` have significant overlap (both electrical/electronics testing)
- Consolidating to one electrical test bench simplifies the toolchain without losing capability
- `measurement_equipment` is fundamentally different (mechanical vs electrical measurement)
- `optical_metrology_tools` is specialized for optical alignment (solar concentrators, interferometry) - genuinely different purpose

**Files updated:**
- Processes: `load_testing_and_commissioning_v0.yaml`, `alignment_and_testing_basic_v0.yaml`, `electrical_wiring_and_controls_v0.yaml`, `electronics_assembly_v0.yaml`, `electrical_testing_v0.yaml`
- Machines: Added DEPRECATED notes to `electrical_test_equipment.yaml`, `test_equipment_electronics.yaml`

**Next steps:**
- Mark recipes/BOMs for deprecated machines as variants or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Air/Compressed Gas Family Consolidation

**Task:** `dedupe:air_compressed_family`

**Machines considered:**
- `air_compressor_small` (90 kg) - shop air supply, NOT used by any process
- `leak_test_equipment` (60 kg) - pressure/leak testing, **includes air compressor**, used by 3 processes
- `gas_handling_loop_v0` (120 kg) - gas recirculation loop, NOT used by any process

**Decision:**
Keep 2 machines with distinct purposes:
1. **`leak_test_equipment`** (60 kg) - pressure/leak testing (self-contained with compressor)
2. **`gas_handling_loop_v0`** (120 kg) - gas recirculation (different purpose than compressed air supply)

Consolidate into above:
- `air_compressor_small` → redundant (leak_test_equipment already includes compressor)

**Rationale:**
- `leak_test_equipment` notes explicitly state it "Includes air compressor" - already self-contained
- `air_compressor_small` is not used by any process
- Since leak testing equipment has its own compressor, a separate shop air compressor is redundant
- `gas_handling_loop_v0` serves a different purpose (gas recirculation, not compressed air) - keep separate even though unused
- If future high-volume shop air needs emerge, can add dedicated compressor later

**Files updated:**
- Machines: Added DEPRECATED note to `air_compressor_small.yaml`
- No process files needed updating (air_compressor_small was unused)

**Next steps:**
- Consider whether `gas_handling_loop_v0` is needed or should be removed (currently unused)
- Mark recipe/BOM for deprecated machine as variant or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Additive Manufacturing Scan: Fixtures/Enclosures/Mounts/Brackets/Covers

**Task:** `dedupe:additive_scan_fixtures`

**Scope:** Identify parts with fixture/enclosure/mount/bracket/cover keywords <~10 kg as candidates for additive manufacturing

**Parts found:** 81 parts matching keywords in kb/items/parts/
- Examples: enclosure_small, mounting_fixtures_adjustable, potting_fixtures_and_molds, electrical_cabinet, instrument_mounts_basic, tracking_mount_structure, vise_mounting_hardware, etc.

**Decision:**
This is a **scanning task**, not a consolidation task. The goal is to identify parts that could benefit from additive manufacturing (3D printing) rather than traditional manufacturing.

**Approach:**
Rather than manually reviewing 81 parts in this dedupe task, recommend systematic review approach:
1. Create work queue items for high-value candidates (fixtures, brackets, small enclosures)
2. Focus on parts where additive provides clear benefit:
   - Complex geometries difficult to machine
   - Low-volume custom parts
   - Integration of multiple features (mounting + cable management + airflow)
   - Rapid iteration/prototyping needs

**Parts immediately suitable for additive** (based on names):
- `enclosure_small` - small enclosures are ideal for additive
- `mounting_fixtures_adjustable` - adjustable fixtures benefit from integrated features
- `potting_fixtures_and_molds` - custom molds are excellent additive candidates
- `vise_mounting_hardware` - brackets and mounting hardware
- `instrument_mounts_basic` - mounting solutions

**Not recommended for additive:**
- Large structural frames (>10 kg, better welded/cast)
- Heavy-duty machine bases
- Pressure vessels or load-bearing components requiring certification

**Next steps:**
- Review the 81 candidate parts systematically to filter by mass (<10 kg)
- For each suitable candidate, add `manufacturing_method_options: [additive, traditional]` field
- Prioritize parts where additive reduces lead time or enables better functionality
- Consider this as ongoing work queue activity, not urgent dedupe consolidation

## 2024-12-15 / claude-worker-1 / Additive Manufacturing Scan: Handles/Knobs/Levers

**Task:** `dedupe:additive_scan_handles_knobs`

**Scope:** Identify parts with handle/knob/lever keywords <~5 kg as candidates for additive manufacturing

**Parts found:** 3 parts matching keywords in kb/items/parts/
- `wire_stripper_set` - tool handles
- `gas_supply_regulator` - likely has adjustment knobs/levers
- `crimper_frame_and_handles` - crimping tool handles

**Decision:**
Very few dedicated handle/knob/lever parts found (only 3). This suggests:
1. Most handles/knobs are integrated into larger assemblies (not standalone parts)
2. KB may not have detailed handle/knob parts defined yet
3. These interface elements may be implicit in tool/machine definitions

**Recommendation:**
- Low priority for dedicated scanning effort given small number of matches
- Handles/knobs are excellent additive candidates when they exist (ergonomic, custom grip patterns)
- Consider adding explicit handle/knob parts for machines where user interface matters
- For the 3 found parts, handles are likely components of larger tools (not standalone items <5 kg)

**Next steps:**
- If handles/knobs become explicit parts in the future, flag them as additive candidates
- Focus additive scanning efforts on higher-volume categories (fixtures, enclosures)

## 2024-12-15 / claude-worker-1 / Crushers Consolidation

**Task:** `dedupe:crushers`

**Machines considered:**
- `crusher_basic` (600 kg, unit??) - generic jaw/impact crusher, used by 1 process
- `rock_crusher_basic` (500 kg) - jaw/cone crusher for regolith/ore, used by 3 processes
- `jaw_crusher_v0` (900 kg) - medium jaw crusher, NOT used by any process

**Decision:**
Keep **`rock_crusher_basic`** (500 kg) as the primary crushing machine

Consolidate into above:
- `crusher_basic` → use `rock_crusher_basic`
- `jaw_crusher_v0` → use `rock_crusher_basic`

**Rationale:**
- All three machines serve identical function: primary crushing of regolith/rock/ore
- Differences are purely naming variations, not functional distinctions
- `rock_crusher_basic` is the most actively used (3 processes) and has the clearest name
- `jaw_crusher_v0` is completely unused - no processes reference it
- No meaningful difference in crushing mechanisms (all mention jaw or impact crushing)
- Simpler toolchain with one primary crusher

**Files updated:**
- Processes: `crushing_and_grinding_v0.yaml`
- Machines: Added DEPRECATED notes to `crusher_basic.yaml`, `jaw_crusher_v0.yaml`

**Next steps:**
- Mark recipes/BOMs for deprecated machines as variants or remove in future cleanup

## 2024-12-15 / claude-worker-1 / General Furnaces Consolidation

**Task:** `dedupe:furnaces_general`

**Machines considered:**
- `furnace_basic` (300 kg) - 200-1200°C, general heating/melting/heat treatment, used by 2 processes
- `casting_furnace_v0` (900 kg) - melting alloy for casting, used by 1 process
- `sintering_furnace_v0` (950 kg) - sintering operations, NOT used by any process

**Decision:**
Keep **`furnace_basic`** (300 kg) as the general-purpose furnace

Consolidate into above:
- `casting_furnace_v0` → use `furnace_basic`
- `sintering_furnace_v0` → use `furnace_basic`

**Rationale:**
- `furnace_basic` has broad capability: "heating, melting, heat_treating" with 200-1200°C range
- This temperature range fully covers both casting (~1000-1200°C) and sintering (~800-1200°C)
- Casting and sintering are operating modes, not fundamentally different equipment
- Both specialized furnaces are just heavier versions of the same basic function
- `sintering_furnace_v0` is completely unused by any process
- No unique molten metal handling or reducing atmosphere requirements mentioned
- Simpler toolchain with one multi-purpose furnace

**Files updated:**
- Processes: `casting_basic_v0.yaml`
- Machines: Added DEPRECATED notes to `casting_furnace_v0.yaml`, `sintering_furnace_v0.yaml`

**Next steps:**
- Mark recipes/BOMs for deprecated machines as variants or remove in future cleanup

## 2024-12-15 / claude-worker-1 / High-Temperature Furnaces Consolidation

**Task:** `dedupe:furnaces_high_temp`

**Machines considered:**
- `furnace_high_temp` (800 kg) - 1600-3000°C for carbothermal reduction/sintering, used by 6 processes
- `high_temp_furnace_v0` (1500 kg) - generic high-temp, NOT used by any process
- `heat_treatment_furnace` (600 kg) - 1000°C+ for metal heat treatment, used by 3 processes

**Decision:**
Keep 2 machines with distinct temperature ranges/purposes:
1. **`furnace_high_temp`** (800 kg) - ultra-high temp (1600-3000°C) for specialized chemistry
2. **`heat_treatment_furnace`** (600 kg) - moderate high temp (1000°C+) for metal heat treatment

Consolidate into above:
- `high_temp_furnace_v0` → use `furnace_high_temp`

**Rationale:**
- `furnace_high_temp` and `heat_treatment_furnace` serve **different purposes**:
  - Ultra-high temp (1600-3000°C): carbothermal reduction, tungsten sintering, specialized chemistry
  - Moderate high temp (1000°C+): metal heat treatment, stress relief, controlled cooling cycles
- Temperature ranges don't overlap significantly - 1000°C vs 1600-3000°C
- Heat treatment requires programmable thermal cycles for metallurgy
- Carbothermal reduction requires extreme temps not achievable in heat treatment furnace
- `high_temp_furnace_v0` is completely unused and redundant with `furnace_high_temp`
- Cannot consolidate - genuinely different capabilities required

**Files updated:**
- Machines: Added DEPRECATED note to `high_temp_furnace_v0.yaml`
- No process files needed updating (machine was unused)

**Next steps:**
- Mark recipe/BOM for deprecated machine as variant or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Hydraulic Pumps Consolidation

**Task:** `dedupe:hydraulic_pumps`

**Parts considered:**
- `hydraulic_pump_small` (25 kg) - used in 2 BOMs
- `hydraulic_pump_basic` (30 kg) - used in 1 BOM
- `hydraulic_pump_assembly` (40 kg) - used in 1 BOM
- `hydraulic_pump_heavy_duty` (80 kg) - used in 1 BOM

**Decision:**
Keep 2 sizes with distinct capacity differences:
1. **`hydraulic_pump_basic`** (30 kg) - standard hydraulic pump
2. **`hydraulic_pump_heavy_duty`** (80 kg) - high-pressure/high-flow (2.7x heavier)

Consolidate into above:
- `hydraulic_pump_small` → use `hydraulic_pump_basic` (only 1.2x difference)
- `hydraulic_pump_assembly` → use `hydraulic_pump_basic` (only 1.3x difference)

**Rationale:**
- Mass ratios: small (1.0x baseline), basic (1.2x), assembly (1.6x), heavy_duty (3.2x)
- Small/basic/assembly are all within 1.6x range - not meaningful capacity difference
- Heavy_duty is genuinely different (3.2x heavier, 200+ bar pressure rating vs standard)
- "Assembly" appears to just be an assembled version of basic pump, not a different capacity
- Keep only variants with >2x capacity difference per guidelines

**Files updated:**
- BOMs: `bom_punch_press_drill_v0.yaml`, `bom_press_brake_or_roller_v0.yaml`, `bom_loader_small_v0.yaml`
- Parts: Added DEPRECATED notes to `hydraulic_pump_small.yaml`, `hydraulic_pump_assembly.yaml`

**Next steps:**
- Mark recipes for deprecated parts as variants or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Kilns Consolidation

**Task:** `dedupe:kilns`

**Machines considered:**
- `kiln_basic` (800 kg, capability: kiln_firing) - used in 1 process
- `kiln_ceramic` (400 kg, capability: ceramic_firing) - used in 1 process

**Decision:**
Keep only `kiln_ceramic` as the canonical high-temperature ceramic kiln.

Consolidate into above:
- `kiln_basic` → use `kiln_ceramic`

**Rationale:**
- Both serve the same purpose: high-temperature ceramic firing/sintering
- `ceramic_sintering_v0` (uses kiln_basic): 1200-1400°C sintering, 4.0 kWh/kg, 6 hr/kg
- `firing_v0` (uses kiln_ceramic): vitrification/hardening, 3.5 kWh/kg, 6 hr/kg
- Energy and time requirements are nearly identical
- Mass difference is only 2x (800 kg vs 400 kg), at threshold but not exceeding >2-3x guideline
- No meaningful operational difference - both do batch ceramic firing with controlled heating cycles
- Task hints suggested preferring kiln_ceramic due to ceramic-specific features (bisque/glaze cycles)
- Ceramic kiln notes mention electric/solar-thermal options, more flexible

**Files updated:**
- Process: `ceramic_sintering_v0.yaml` (changed `kiln_basic` → `kiln_ceramic`)
- Machine: Added DEPRECATED note to `kiln_basic.yaml`

**Next steps:**
- Mark recipe/BOM for deprecated machine as variant or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Rolling Mills Consolidation

**Task:** `dedupe:rolling_mills`

**Machines considered:**
- `rolling_mill` (800 kg, capabilities: rolling, metal_forming) - used in 5 processes
- `plate_rolling_mill` (1500 kg, capabilities: rolling, metal_forming, plate_production) - used in 3 processes

**Decision:**
Keep only `plate_rolling_mill` as the canonical rolling mill for all rolling operations.

Consolidate into above:
- `rolling_mill` → use `plate_rolling_mill`

**Rationale:**
- Mass difference between rolling_mill (800 kg) and plate_rolling_mill (1500 kg) is only 1.9x, below our >2-3x threshold
- Both serve the same core function: compressing metal through rollers to reduce thickness
- rolling_basic_v0 process: converts ingots → sheet using hot rolling - plate_rolling_mill handles this
- Plate rolling mill can handle both ingot rolling and plate production, no need for separate general rolling mill
- All rolling operations can be consolidated to plate_rolling_mill without loss of capability

**Files updated:**
- Processes: `rolling_basic_v0.yaml` (rolling_mill → plate_rolling_mill), `metal_forming_basic_v0.yaml` (rolling_mill → plate_rolling_mill)
- Machines: Added DEPRECATED notes to `rolling_mill.yaml`

**Next steps:**
- Mark recipes/BOMs for deprecated machines as variants or remove in future cleanup

## 2024-12-15 / claude-worker-1 / Vacuum Pumps Consolidation

**Task:** `dedupe:vacuum_pumps`

**Items considered:**
- `vacuum_pump_basic` (kind: **part**, mass: 35 kg) - used in 1 BOM as a component
- `vacuum_pump_small` (kind: **machine**, mass: 35 kg) - used in 4 BOMs and 1 process, has own BOM

**Decision:**
Keep `vacuum_pump_small` as the canonical vacuum pump machine.

Consolidate into above:
- `vacuum_pump_basic` (part) → use `vacuum_pump_small` (machine)

**Rationale:**
- Both have identical mass (35 kg) and serve the same purpose (vacuum generation)
- This is a **categorization issue**, not a true overlap - vacuum pumps should be machines, not parts
- `vacuum_pump_small` is correctly categorized as a machine with:
  - Own BOM showing manufacturing steps (motor, housing, vanes, shaft, seals, gauge)
  - Used in processes requiring vacuum generation
  - Can be manufactured as a complete functional unit
- `vacuum_pump_basic` was incorrectly categorized as a part
  - Parts are components that go into assemblies
  - Complete functional units like pumps should be machines
  - No BOM showing internal structure
- No capacity/performance difference - same mass suggests same capability
- Consolidating removes the categorization confusion

**Files updated:**
- BOM: `bom_controlled_atmosphere_chamber_v0.yaml` (vacuum_pump_basic → vacuum_pump_small)
- Part: Added DEPRECATED note to `vacuum_pump_basic.yaml` explaining categorization issue

**Next steps:**
- Mark recipe for deprecated part as variant or remove in future cleanup
- Consider reviewing other items for similar categorization issues (functional units marked as parts vs machines)

## 2026-01-18 / claude-sonnet-4.5 / Heat Treatment Furnace Versioning Consolidation

**Task:** Consolidate `heat_treatment_furnace` and `heat_treatment_furnace_v0` duplicates

**Items considered:**
- `heat_treatment_furnace` (537 kg) - heat treatment furnace, no processes_supported field
- `heat_treatment_furnace_v0` (537 kg) - heat treatment furnace v0, has processes_supported field

**Decision:**
Keep only `heat_treatment_furnace_v0` as the canonical heat treatment furnace.

Consolidate into above:
- `heat_treatment_furnace` → use `heat_treatment_furnace_v0`

**Rationale:**
- Both items have **identical mass** (537 kg)
- Both use **identical BOM** (bom_heat_treatment_furnace_v0)
- Both serve identical function (heat treatment of metals with controlled cycles)
- Within 1× of each other (literally identical specs!)
- This is a clear case of proliferation - same machine with and without _v0 suffix
- `heat_treatment_furnace_v0` is more extensively used (23 references vs 1)
- `heat_treatment_furnace_v0` has `processes_supported` field properly defined
- Per conservative mode guidelines: items within 5× should be consolidated (these are 1×)
- Different from previous high-temp furnace consolidation (line 349-382) which kept heat_treatment_furnace separate from furnace_high_temp due to different temperature ranges - this consolidation is about versioning of the same machine

**Files updated:**
- Processes: `bearing_set_heavy_production_v0.yaml`, `heat_treat_basic_v0.yaml`, `heat_treatment_basic_v0.yaml`, `stress_relief_basic_v0.yaml` (all changed machine_id from heat_treatment_furnace to heat_treatment_furnace_v0)
- Recipe: `recipe_heat_treatment_furnace_v0.yaml` (changed produces_id and outputs from heat_treatment_furnace to heat_treatment_furnace_v0)
- Runbook: `heat_treatment_furnace_runbook.md` (updated to reference v0 version)
- Queue files: `machine_runbook_queue_nextgen.md`, `machine_runbook_queue_sequential.md` (updated references)
- Item: Deleted `kb/items/machines/heat_treatment_furnace.yaml`

**Next steps:**
- Run indexer to verify no broken references remain
- Consider consolidating the two runbooks (heat_treatment_furnace_runbook.md and heat_treatment_furnace_v0_runbook.md) as they're for the same machine

## 2026-01-18 / claude-sonnet-4.5 / Lathe Family Review and "Or" Machine Elimination

**Task:** Review lathe_engine_v0, precision_lathe, and roll_grinding_lathe_or_cylindrical_grinder_v0 for duplication; eliminate ambiguous "or" machine

**Machines considered:**
- `lathe_engine_v0` (180 kg) - general-purpose turning, used by 6 processes
- `precision_lathe` (1200 kg) - precision turning with tight tolerances, used by 9 processes
- `roll_grinding_lathe_or_cylindrical_grinder_v0` (600 kg) - "or" machine for roll grinding, used by 1 process
- `grinder_cylindrical_v0` (600 kg) - cylindrical grinder, unused

**Decision:**
Keep `lathe_engine_v0` and `precision_lathe` as separate machines (different precision tiers).
Keep `grinder_cylindrical_v0` as the canonical cylindrical grinder.
Delete `roll_grinding_lathe_or_cylindrical_grinder_v0` (consolidate with grinder_cylindrical_v0).

**Rationale:**

**Lathes (lathe_engine_v0 vs precision_lathe):**
- Mass ratio: 6.7× (1200 kg / 180 kg) - just exceeds 5× threshold
- Serve genuinely different precision tiers:
  - lathe_engine_v0: General turning operations (bearing production, robot fabrication, fasteners)
  - precision_lathe: Tight tolerance work (±0.005mm) for ball screws, lead screws, valve boring
- NOT duplicative - different capability classes
- Keep both

**"Or" Machine (roll_grinding_lathe_or_cylindrical_grinder_v0):**
- Identical mass (600 kg) to grinder_cylindrical_v0
- Ambiguous "or" naming violates single-function machine principle
- Process `roll_grinding_and_balancing_v0` performs grinding operations (not lathe turning)
- "Precision grind roll diameters and journals" is cylindrical grinding work
- grinder_cylindrical_v0 already exists with identical spec and proper naming
- Clear case of duplication + naming ambiguity
- Per conservative mode: identical specs (1×) → consolidate

**Machine Definition Principle Violation:**
- "Or" machines are anti-patterns - each machine definition should represent a single, specific machine
- Recipes and processes should reference unambiguous machine IDs
- "roll_grinding_lathe_or_cylindrical_grinder_v0" conflates two different machine types:
  - Lathe: rotating workpiece, stationary cutting tool (turning operations)
  - Cylindrical grinder: rotating workpiece, rotating grinding wheel (grinding operations)
- The actual process requires a cylindrical grinder, not a lathe

**Files updated:**
- Process: `roll_grinding_and_balancing_v0.yaml` (changed machine_id from roll_grinding_lathe_or_cylindrical_grinder_v0 to grinder_cylindrical_v0)
- Deleted: `kb/items/machines/roll_grinding_lathe_or_cylindrical_grinder_v0.yaml`
- Deleted: `kb/boms/bom_roll_grinding_lathe_or_cylindrical_grinder_v0.yaml`
- Deleted: `kb/recipes/recipe_roll_grinding_lathe_or_cylindrical_grinder_v0.yaml`

**Next steps:**
- Run indexer to verify no broken references

## 2026-07-15 / codex / milling_machine_general_v0 / milling_machine_v0 Deletion Payload

- Deleted files:
  - `kb/items/machines/milling_machine_general_v0.yaml`
  - `kb/items/machines/milling_machine_v0.yaml`
  - `kb/boms/bom_milling_machine_general_v0.yaml`
  - `kb/boms/bom_milling_machine_v0_v0.yaml`
  - `kb/recipes/recipe_machine_milling_machine_general_v0.yaml`
  - `kb/recipes/recipe_milling_machine_v0_v0.yaml`
- Entity types: machine, BOM, recipe
- Replacement / canonical ID: `cnc_mill`
- Removal status: deleted
- Validation: `UV_CACHE_DIR=/tmp/uv-cache uv run python -m src.cli validate --id item:cnc_mill`

### Removal Reason

`milling_machine_general_v0` and `milling_machine_v0` were redundant with
`cnc_mill`. `milling_machine_general_v0` already stated `DEPRECATED -
Consolidated into cnc_mill` in its notes, and its mass was within the 5x
Conservative Mode equivalence threshold relative to `cnc_mill` (370 kg vs
785 kg). `milling_machine_v0` was a seed placeholder with no direct process
resource requirements outside its own BOM/recipe and seed listing. CNC milling
is a functional superset for the migrated milling, gear-cutting, and machining
resource requirements.

### References Migrated

- `milling_machine_general_v0` -> `cnc_mill` in:
  - `kb/processes/aluminum_housing_machining_v0.yaml`
  - `kb/processes/aluminum_housing_machining_v1.yaml`
  - `kb/processes/bevel_gear_cutting_basic_v0.yaml`
  - `kb/processes/burner_or_heater_casting_fabrication_v0.yaml`
  - `kb/processes/cooling_loop_basic_fabrication_v0.yaml`
  - `kb/processes/fastener_kit_small_fabrication_v0.yaml`
  - `kb/processes/flywheel_vacuum_housing_machining_v0.yaml`
  - `kb/processes/gear_cutting_basic_v0.yaml`
  - `kb/processes/gear_cutting_v0.yaml`
  - `kb/processes/helical_gear_cutting_basic_v0.yaml`
  - `kb/processes/machining_finish_basic_v0.yaml`
  - `kb/processes/machining_raw_to_machined_part_v0.yaml`
  - `kb/processes/machining_raw_to_machined_part_v1.yaml`
  - `kb/processes/machining_rough_v0.yaml`
  - `kb/processes/machining_to_coolant_pump_v0.yaml`
  - `kb/processes/metal_cutting_basic_v0.yaml`
  - `kb/processes/metal_cutting_process_v0.yaml`
  - `kb/processes/power_conditioning_module_fabrication_v0.yaml`
  - `kb/processes/pump_housing_machining_v0.yaml`
  - `kb/processes/robot_arm_link_fabrication_v0.yaml`
  - `kb/processes/robot_wrist_fabrication_v0.yaml`
  - `kb/processes/spur_gear_cutting_basic_v0.yaml`
  - `kb/processes/steel_shaft_machining_v0.yaml`
  - `kb/processes/steel_shaft_machining_v1.yaml`
  - `kb/processes/surface_finishing_am_parts_v0.yaml`
  - `kb/processes/worm_gear_cutting_basic_v0.yaml`
  - `simulations/anvil_block_basic_runbook/snapshot.json`
  - `simulations/anvil_block_basic_runbook/events.jsonl`
- `milling_machine_general_v0` removed from `docs/self_reproducing_set.txt`
  because `cnc_mill` was already listed.
- `milling_machine_v0` -> `cnc_mill` in
  `kb/seeds/paper_reviews_dec2024_comprehensive_v0.yaml`.
- `cnc_mill.processes_supported` was expanded to include the migrated process
  IDs.

### Possible Negative Effects

- Loses the explicit lower-technology/manual milling-machine path.
- May overestimate machine complexity, control electronics, and imported compute
  requirements for simple milling, drilling-adjacent, and gear-cutting tasks.
- May concentrate simulator capacity demand onto `cnc_mill`, making CNC milling
  appear as a stronger bottleneck than a split manual/CNC machine set would.
- Changes the anvil-block runbook import from a 370 kg general milling machine
  to a 785 kg CNC mill; exported SimViewer data should be regenerated.
- Removes a seed-roadmap placeholder (`milling_machine_v0`) that may have been
  useful if later work wants to model a non-CNC machine-tool bootstrap path.

### Removed YAML

`kb/items/machines/milling_machine_general_v0.yaml`

```yaml
id: milling_machine_general_v0
kind: machine
name: Milling machine (general) v0
mass: 370.0
unit: unit
bom: bom_milling_machine_general_v0
notes: |
  Mass updated 2026-01 from 600 kg to 370 kg based on BOM component analysis:
  milling_table (57) + spindle_head_basic (60) + drive_motor_medium (90) +
  gearbox_reducer_medium (110) + bearing_set_heavy×2 (8) + cutting_tool_set_basic (25) +
  fastener_kit_medium (1) + power_conditioning_module (12) + control_compute_module_imported (2) +
  sensor_suite_general (5) = 370 kg.

  DEPRECATED - Consolidated into cnc_mill. General-purpose milling machine; coarse mass estimate.
recipe: recipe_machine_milling_machine_general_v0
unit_kind: discrete
```

`kb/items/machines/milling_machine_v0.yaml`

```yaml
id: milling_machine_v0
kind: machine
name: Milling machine
mass: 850.0
unit: unit
bom: bom_milling_machine_v0_v0
material_class: steel
notes: Placeholder milling machine derived from seed references. Mass and capabilities
  are conservative defaults to enable initial modeling; replace with detailed design
  later.
recipe: recipe_milling_machine_v0_v0
unit_kind: discrete
```

`kb/boms/bom_milling_machine_general_v0.yaml`

```yaml
id: bom_milling_machine_general_v0
owner_item_id: milling_machine_general_v0
components:
  - item_id: milling_table
    qty: 1
  - item_id: spindle_head_basic
    qty: 1
  - item_id: drive_motor_medium
    qty: 1
  - item_id: gearbox_reducer_medium
    qty: 1
  - item_id: bearing_set_heavy
    qty: 2
  - item_id: cutting_tool_set_basic
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
  - item_id: power_conditioning_module
    qty: 1
  - item_id: control_compute_module_imported
    qty: 1
  - item_id: sensor_suite_general
    qty: 1
notes: Coarse BOM; imported compute assumed.
```

`kb/boms/bom_milling_machine_v0_v0.yaml`

```yaml
id: bom_milling_machine_v0_v0
owner_item_id: milling_machine_v0
components:
  - item_id: milling_table
    qty: 1
  - item_id: spindle_head_basic
    qty: 1
  - item_id: drive_motor_medium
    qty: 1
  - item_id: gearbox_reducer_medium
    qty: 1
  - item_id: bearing_set_heavy
    qty: 2
  - item_id: cutting_tool_set_basic
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
  - item_id: power_conditioning_module
    qty: 1
  - item_id: control_compute_module_imported
    qty: 1
  - item_id: sensor_suite_general
    qty: 1
notes: Coarse BOM for milling_machine_v0; imported compute/controls, sensor suite
```

`kb/recipes/recipe_machine_milling_machine_general_v0.yaml`

```yaml
id: recipe_machine_milling_machine_general_v0
kind: recipe
target_item_id: milling_machine_general_v0
variant_id: v0
inputs:
  - item_id: milling_table
    qty: 1.0
    unit: unit
  - item_id: spindle_head_basic
    qty: 1.0
    unit: unit
  - item_id: drive_motor_medium
    qty: 1.0
    unit: unit
  - item_id: gearbox_reducer_medium
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
  - item_id: cutting_tool_set_basic
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
  - item_id: power_conditioning_module
    qty: 1.0
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1.0
    unit: unit
  - item_id: sensor_suite_general
    qty: 1.0
    unit: unit
outputs:
  - item_id: milling_machine_general_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: milling_table
        qty: 1.0
        unit: unit
      - item_id: spindle_head_basic
        qty: 1.0
        unit: unit
      - item_id: drive_motor_medium
        qty: 1.0
        unit: unit
      - item_id: gearbox_reducer_medium
        qty: 1.0
        unit: unit
      - item_id: bearing_set_heavy
        qty: 2.0
        unit: unit
      - item_id: cutting_tool_set_basic
        qty: 1.0
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1.0
        unit: unit
      - item_id: power_conditioning_module
        qty: 1.0
        unit: unit
      - item_id: control_compute_module_imported
        qty: 1.0
        unit: unit
      - item_id: sensor_suite_general
        qty: 1.0
        unit: unit
    outputs:
      - item_id: milling_machine_general_v0
        qty: 1.0
        unit: unit
    est_time_hr: 6.0
    labor_hours: 6.0
    machine_hours: 6.0
assumptions: Assemble per BOM; imported compute module remains.
notes: Coarse assembly route; refine with alignment and calibration later.
```

`kb/recipes/recipe_milling_machine_v0_v0.yaml`

```yaml
id: recipe_milling_machine_v0_v0
kind: recipe
target_item_id: milling_machine_v0
variant_id: v0
inputs:
  - item_id: bulk_material_or_parts
    qty: 850.0
    unit: kg
  - item_id: assembled_equipment
    qty: 850.0
    unit: kg
outputs:
  - item_id: milling_machine_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: bulk_material_or_parts
        qty: 850.0
        unit: kg
    outputs:
      - item_id: bulk_material_or_parts
        qty: 850.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
  - process_id: assembly_basic_v0
    inputs:
      - item_id: bulk_material_or_parts
        qty: 850.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 850.0
        unit: kg
    est_time_hr: 3.0
    labor_hours: 3.0
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 850.0
        unit: kg
    outputs:
      - item_id: milling_machine_v0
        qty: 1.0
        unit: unit
    est_time_hr: 0.5
    labor_hours: 0.5
assumptions: Assemble milling machine per BOM; imported compute/tools.
notes: Coarse route; refine with alignment/calibration later.
```
- Review other "or" machines in KB (14 found: ceramic_press_or_mold_set, power_hammer_or_press_v0, press_brake_or_roller, etc.) for similar cleanup
- Each "or" machine should be evaluated: does a specific machine already exist? Should the ambiguous machine be eliminated?

## 2026-01-18 / claude-sonnet-4.5 / Remove calibration_standards Miscategorization

**Task:** Remove calibration_standards which was incorrectly categorized as a machine

**Item considered:**
- `calibration_standards` (5 kg) - categorized as `kind: machine` but actually reference artifacts (gauge blocks, mass standards, etc.)

**Decision:**
Remove `calibration_standards` entirely. Fold its functionality into `measurement_equipment`.

**Rationale:**
- Calibration standards are **passive reference objects**, not machines
- They don't DO work - they're reference artifacts used during calibration
- Examples: gauge blocks (length), mass standards (weight), voltage references
- Creates circular dependency: what calibrates the machines that make calibration standards?
- In reality, calibration standards must be traceable to national standards (NIST, PTB, etc.) - cannot be bootstrapped
- Calibration capability can reasonably be considered part of `measurement_equipment` rather than requiring separate reference artifacts
- Simplifies the KB without losing functional modeling detail

**Category violation:**
- `kind: machine` should be for active equipment that performs work
- Passive reference objects should not be machines
- Alternative would have been `kind: part` + `is_import: true`, but user preferred complete removal

**Files updated:**
- Processes: `calibration_basic_v0.yaml`, `calibration_force_torque_sensor_v0.yaml` (removed calibration_standards from resource_requirements, updated notes to clarify standards are implicit in measurement_equipment)
- Deleted: `kb/items/machines/calibration_standards.yaml`
- Deleted: `kb/boms/bom_calibration_standards_v0.yaml`
- Deleted: `kb/recipes/recipe_calibration_standards_v0.yaml`

**Impact:**
- 2 processes updated (calibration_basic_v0, calibration_force_torque_sensor_v0)
- 30 recipes use these processes and continue to work unchanged
- No broken dependencies - processes remain functional with labor_bot + measurement_equipment

**Next steps:**
- Run indexer to verify no broken references

## 2026-07-15 / codex / AM Seed and Support Machine YAML Removal

- Deleted files:
  - `kb/items/machines/wire_arc_additive_machine_v0.yaml`
  - `kb/items/machines/ebm_machine_lunar_v0.yaml`
  - `kb/items/machines/ebm_powder_handling_system_v0.yaml`
  - `kb/items/machines/slm_machine_lunar_v0.yaml`
  - `kb/items/machines/lens_machine_lunar_v0.yaml`
  - `kb/items/machines/powder_quality_analysis_v0.yaml`
  - `kb/items/machines/build_atmosphere_control_v0.yaml`
  - `kb/items/machines/metal_powder_sieving_system_v0.yaml`
  - `kb/boms/bom_wire_arc_additive_machine_v0.yaml`
  - `kb/boms/bom_ebm_machine_lunar_v0_v0.yaml`
  - `kb/boms/bom_ebm_powder_handling_system_v0.yaml`
  - `kb/boms/bom_slm_machine_lunar_v0.yaml`
  - `kb/boms/bom_lens_machine_lunar_v0_v0.yaml`
  - `kb/boms/bom_powder_quality_analysis_v0.yaml`
  - `kb/boms/bom_build_atmosphere_control_v0.yaml`
  - `kb/boms/bom_metal_powder_sieving_system_v0.yaml`
  - `kb/recipes/recipe_machine_ebm_machine_lunar_v0.yaml`
  - `kb/recipes/recipe_ebm_powder_handling_system_v0.yaml`
  - `kb/recipes/recipe_slm_machine_lunar_v0_v0.yaml`
  - `kb/recipes/recipe_lens_machine_lunar_v0_v0.yaml`
  - `kb/recipes/recipe_powder_quality_analysis_v0.yaml`
  - `kb/recipes/recipe_build_atmosphere_control_v0.yaml`
  - `kb/recipes/recipe_metal_powder_sieving_system_v0.yaml`
  - `kb/processes/slm_machine_lunar_v0_assembly_v0.yaml`
  - `kb/processes/lens_machine_lunar_v0_assembly_v0.yaml`
  - `kb/processes/powder_quality_machine_assembly_v0.yaml`
- Entity types: machine, BOM, recipe, process
- Replacement / canonical ID: none; these were unconnected AM seed/support entries
- Removal status: deleted
- Validation: `UV_CACHE_DIR=/tmp/uv-cache uv run python -m src.cli index`

### Removal Reason

These additive-manufacturing-related machines were present as seed, roadmap, support, or placeholder entries but were not directly required by any active AM build/deposition process. Direct AM production remains represented by connected machines such as `3d_printer_basic_v0`, `resource_3d_printer_cartesian_v0_machine`, `resource_3d_printer_multi_material_v0`, `wire_arc_additive_machine`, `ebf3_wire_feed_machine_v0`, and `selective_solar_sinterer_v0`.

The removed entries either had no process users, only appeared in seed files, or only had self-manufacturing assembly recipes. `lens_machine_lunar_v0` also appeared as an erroneous intermediate step in `recipe_condenser_lens_assembly_v0`; that recipe was kept, but the unrelated machine-building step was removed.

### References Migrated or Removed

- Removed AM seed references from `kb/seeds/paper_reviews_dec2024_comprehensive_v0.yaml` and `kb/seeds/papers_gap_seed_v0.yaml`.
- Removed deleted assembly process IDs from `kb/items/machines/assembly_station.yaml`.
- Removed the `lens_machine_lunar_v0_assembly_v0` step and its machine-frame/electronics inputs from `kb/recipes/recipe_condenser_lens_assembly_v0.yaml`.
- Deleted dedicated BOMs, recipes, and self-assembly processes for the removed machines.

### Possible Negative Effects

- Removes roadmap placeholders for SLM, EBM powder-bed, LENs, build-atmosphere control, AM powder QC, and metal powder sieving.
- Future AM modeling may need to recreate one or more of these entries if a concrete process begins using them.
- Narrows the currently modeled AM capability set to machines with direct process use, which may underrepresent AM support equipment needs.
- Deleting EBM/SLM support equipment can hide powder-bed-specific constraints until those processes are reintroduced.

### Removed YAML

`kb/items/machines/wire_arc_additive_machine_v0.yaml`

```yaml
id: wire_arc_additive_machine_v0
kind: machine
name: Wire-arc additive machine v0
mass: 850.0
unit: unit
bom: bom_wire_arc_additive_machine_v0
material_class: steel
is_import: true
notes: Wire feed arc additive machine with robotic arm or gantry for depositing metal
  feedstock; early placeholder for EBF3-style fabrication.
unit_kind: discrete
```

`kb/items/machines/ebm_machine_lunar_v0.yaml`

```yaml
id: ebm_machine_lunar_v0
kind: machine
name: Electron beam melting machine (lunar) v0
mass: 1800.0
unit: unit
material_class: steel
bom: bom_ebm_machine_lunar_v0_v0
notes: Electron Beam Melting (EBM) machine for metal additive manufacturing in vacuum.
  Includes electron gun, vacuum chamber, powder handling, and heated build platform.
  Power draw approximated for modeling purposes.
power_draw_kW: 60.0
energy_model:
  type: kWh_per_unit
  value: 2.5
  notes: Placeholder energy per unit produced by the machine in nominal operation
time_model:
  type: fixed_time
  hr_per_batch: 2.0
  notes: Placeholder build time per batch for one ebm machine
recipe: recipe_machine_ebm_machine_lunar_v0
unit_kind: discrete
```

`kb/items/machines/ebm_powder_handling_system_v0.yaml`

```yaml
id: ebm_powder_handling_system_v0
name: EBM Powder Handling System v0
kind: machine
mass: 60.0
unit: unit
bom: bom_ebm_powder_handling_system_v0
notes: Seed placeholder powder handling subsystem for Electron Beam Melting (EBM)
  machine. Delivers metal powder to the build area and recycles unused powder. Placeholder;
  refine with BOM later.
mass_source: ai_estimate
mass_confidence: medium
recipe: recipe_ebm_powder_handling_system_v0
unit_kind: discrete
```

`kb/items/machines/slm_machine_lunar_v0.yaml`

```yaml
id: slm_machine_lunar_v0
kind: machine
name: Selective Laser Melting Lunar Machine v0
mass: 500.0
unit: unit
material_class: metal
bom: bom_slm_machine_lunar_v0
notes: Seed item introduced to satisfy the Referenced-Only gap; detailed spec to be
  refined via iteration.
sources:
- paper_reviews_dec2024_comprehensive_v0
recipe: recipe_slm_machine_lunar_v0_v0
unit_kind: discrete
```

`kb/items/machines/lens_machine_lunar_v0.yaml`

```yaml
id: lens_machine_lunar_v0
kind: machine
name: Laser Engineered Net Shaping Lunar Machine v0
mass: 67.5
unit: unit
material_class: metal
bom: bom_lens_machine_lunar_v0_v0
notes: |
  Mass updated 2026-01 from 600 kg to 67.5 kg based on BOM component analysis:
  machine_frame_small (47.5) + power_electronics_module (20) = 67.5 kg.

  LENs machine for lunar additive manufacturing using a laser deposition process.
  Placeholder mass and capabilities; to be refined.
recipe: recipe_lens_machine_lunar_v0_v0
unit_kind: discrete
```

`kb/items/machines/powder_quality_analysis_v0.yaml`

```yaml
id: powder_quality_analysis_v0
kind: machine
name: Powder quality analysis system v0
mass: 30.0
unit: unit
bom: bom_powder_quality_analysis_v0
material_class: steel
notes: 'Analysis system for metal powder quality control in additive manufacturing.

  Source: docs/paper_reviews/ellery-2022-metalysis_missing_tech.md (AM feedstock)

  Measurements: Particle size distribution, morphology, composition

  Methods: Sieve analysis, optical microscopy, basic composition analysis

  Critical for: AM process quality, powder reuse decisions

  Ensures: Spherical particles, consistent size range, low contamination

  '
recipe: recipe_powder_quality_analysis_v0
unit_kind: discrete
```

`kb/items/machines/build_atmosphere_control_v0.yaml`

```yaml
id: build_atmosphere_control_v0
kind: machine
name: Build atmosphere control system v0
mass: 100.0
unit: unit
bom: bom_build_atmosphere_control_v0
material_class: steel
capabilities:
- gas_handling
- vacuum_control
- sensors
notes: 'Atmosphere control system for additive manufacturing build chambers.

  Source: docs/paper_reviews/ellery-2022-metalysis_missing_tech.md (AM process parameters)

  Functions: Inert gas purging, vacuum control, oxygen monitoring

  Gas types: Argon, nitrogen, or vacuum depending on material

  Purpose: Prevents oxidation during metal AM processes

  Components: Gas supply, flow controllers, vacuum pump, sensors

  Critical for reactive metals (Ti, Al) and high-quality builds

  '
recipe: recipe_build_atmosphere_control_v0
unit_kind: discrete
```

`kb/items/machines/metal_powder_sieving_system_v0.yaml`

```yaml
id: metal_powder_sieving_system_v0
kind: machine
name: Metal powder sieving system
mass: 60.0
unit: unit
bom: bom_metal_powder_sieving_system_v0
notes: Minimal, placeholder machine to resolve the referenced gap from Ellery seed
  sources. Represents a powder sieving/classification unit capable of sorting metal
  powder by particle size. No detailed energy or throughput modeling included at this
  iteration; used to close import gaps in the knowledge base.
recipe: recipe_metal_powder_sieving_system_v0
unit_kind: discrete
```

`kb/boms/bom_wire_arc_additive_machine_v0.yaml`

```yaml
id: bom_wire_arc_additive_machine_v0
owner_item_id: wire_arc_additive_machine_v0
components:
  - item_id: wire_feed_system_basic
    qty: 1
  - item_id: electron_gun_assembly
    qty: 1
  - item_id: motion_gantry_basic
    qty: 1
  - item_id: control_panel_basic
    qty: 1
  - item_id: power_output_terminals
    qty: 1
  - item_id: fastener_kit_large
    qty: 1
```

`kb/boms/bom_ebm_machine_lunar_v0_v0.yaml`

```yaml
id: bom_ebm_machine_lunar_v0_v0
owner_item_id: ebm_machine_lunar_v0
components:
- item_id: ebm_build_platform_heated_v0
  qty: 1.0
```

`kb/boms/bom_ebm_powder_handling_system_v0.yaml`

```yaml
id: bom_ebm_powder_handling_system_v0
owner_item_id: ebm_powder_handling_system_v0
components:
  - item_id: mill_shell_generic
    qty: 1
  - item_id: liner_set_abrasion_resistant
    qty: 1
  - item_id: collection_hopper_set
    qty: 1
  - item_id: bearing_set_heavy
    qty: 1
  - item_id: drive_motor_medium
    qty: 1
  - item_id: gearbox_reducer_medium
    qty: 1
  - item_id: support_frame_welded
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
notes: "Coarse BOM for EBAM powder handling subsystem; generic components drawn from existing machine BOMs."
```

`kb/boms/bom_slm_machine_lunar_v0.yaml`

```yaml
id: bom_slm_machine_lunar_v0
owner_item_id: slm_machine_lunar_v0
components:
- item_id: machine_frame_small
  qty: 1.0
- item_id: power_electronics_module
  qty: 1.0
notes: Placeholder BOM updated to include frame_small and power_electronics_module; to be refined.
```

`kb/boms/bom_lens_machine_lunar_v0_v0.yaml`

```yaml
id: bom_lens_machine_lunar_v0_v0
owner_item_id: lens_machine_lunar_v0
components:
- item_id: machine_frame_small
  qty: 1.0
- item_id: power_electronics_module
  qty: 1.0
notes: Placeholder BOM updated to include frame_small and power_electronics_module; to be refined.
```

`kb/boms/bom_powder_quality_analysis_v0.yaml`

```yaml
id: bom_powder_quality_analysis_v0
owner_item_id: powder_quality_analysis_v0
components:
- item_id: optical_microscope_v0
  qty: 1.0
  unit: unit
- item_id: screening_equipment
  qty: 1.0
  unit: unit
notes: |
  Minimal BOM for the powder quality analysis system. Includes an optical microscope and a screening/equipment module for particle sizing. Placeholder BOM; additional components (e.g., sample handling, control electronics) may be added as the model matures.
```

`kb/boms/bom_build_atmosphere_control_v0.yaml`

```yaml
id: bom_build_atmosphere_control_v0
owner_item_id: build_atmosphere_control_v0
components:
  - item_id: vacuum_pump_small
    qty: 1
  - item_id: gas_cylinder_mount
    qty: 2
  - item_id: flow_controller_valve_set
    qty: 1
  - item_id: oxygen_sensor_zirconia
    qty: 1
  - item_id: pressure_gauge_set
    qty: 1
  - item_id: piping_assembly_small
    qty: 1
  - item_id: control_panel_basic
    qty: 1
  - item_id: enclosure_steel_small
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
  - item_id: steel_frame_welded
    qty: 30.2
  - item_id: electrical_wire_and_connectors
    qty: 6.53
notes: |
  Bill of materials for build atmosphere control system.
  Vacuum pump evacuates chamber, gas cylinders supply inert gas.
  Flow controllers regulate gas flow, oxygen sensor monitors purity.
  Used in metal AM and other oxygen-sensitive processes.
```

`kb/boms/bom_metal_powder_sieving_system_v0.yaml`

```yaml
id: bom_metal_powder_sieving_system_v0
owner_item_id: metal_powder_sieving_system_v0
components:
  - item_id: screen_deck_basic
    qty: 1.0
  - item_id: vibrator_motor_small
    qty: 1.0
  - item_id: machine_frame_small
    qty: 1.0
  - item_id: collection_hopper_set
    qty: 1.0
  - item_id: power_conditioning_module
    qty: 1.0
notes: |
  Minimal BOM for metal powder sieving system. Composed of a basic screening deck, vibrator motor, small machine frame, collection hoppers, and power conditioning module. Placeholder BOM; additional subassemblies and sensors can be added as modeling matures.
```

`kb/recipes/recipe_machine_ebm_machine_lunar_v0.yaml`

```yaml
id: recipe_machine_ebm_machine_lunar_v0
target_item_id: ebm_machine_lunar_v0
variant_id: v0
inputs:
  - item_id: sheet_metal_or_structural_steel
    qty: 1850.0
    unit: kg
  - item_id: filler_wire_basic
    qty: 5.0
    unit: kg
  - item_id: ebm_build_platform_heated_v0
    qty: 30.0
    unit: kg
  - item_id: power_conditioning_module
    qty: 12.0
    unit: kg
  - item_id: control_compute_module_imported
    qty: 2.0
    unit: kg
  - item_id: sensor_suite_general
    qty: 5.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 10.0
    unit: kg
  - item_id: electronic_components_set
    qty: 5.0
    unit: kg
outputs:
  - item_id: ebm_machine_lunar_v0
    qty: 1800.0
    unit: kg
steps:
  - process_id: cutting_basic_v0
    inputs:
      - item_id: sheet_metal_or_structural_steel
        qty: 1850.0
        unit: kg
    outputs:
      - item_id: cut_parts
        qty: 1800.0
        unit: kg
    est_time_hr: 3.0
    machine_hours: 3.0
    labor_hours: 1.5
    notes: "Cut chamber panels, frame members, and mounting plates."
  - process_id: welded_fabrication_basic_v0
    inputs:
      - item_id: cut_parts
        qty: 1800.0
        unit: kg
      - item_id: filler_wire_basic
        qty: 5.0
        unit: kg
    outputs:
      - item_id: welded_fabrications
        qty: 1780.0
        unit: kg
    est_time_hr: 4.0
    machine_hours: 3.0
    labor_hours: 3.0
    notes: "Weld chamber, frame, and support structures."
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: welded_fabrications
        qty: 1780.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 1750.0
        unit: kg
    est_time_hr: 3.0
    machine_hours: 2.5
    labor_hours: 2.0
    notes: "Machine sealing surfaces, mounts for gun, feed, and build platform."
  - process_id: assembly_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 1750.0
        unit: kg
      - item_id: ebm_build_platform_heated_v0
        qty: 30.0
        unit: kg
      - item_id: power_conditioning_module
        qty: 12.0
        unit: kg
      - item_id: control_compute_module_imported
        qty: 2.0
        unit: kg
      - item_id: sensor_suite_general
        qty: 5.0
        unit: kg
      - item_id: fastener_kit_medium
        qty: 1.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 1800.0
        unit: kg
    est_time_hr: 3.0
    labor_hours: 3.0
    notes: "Install electron gun assembly, powder handling, build platform, and drives."
  - process_id: wiring_and_electronics_integration_v0
    inputs:
      - item_id: assembled_equipment
        qty: 1800.0
        unit: kg
      - item_id: electrical_wire_and_connectors
        qty: 10.0
        unit: kg
      - item_id: electronic_components_set
        qty: 5.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 1800.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: "Wire high-voltage gun supply, motion controls, heaters, and sensors."
  - process_id: integration_test_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 1800.0
        unit: kg
    outputs:
      - item_id: ebm_machine_lunar_v0
        qty: 1800.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 1.5
    notes: "Vacuum check, beam emission test, and motion calibration."
assumptions: "Coarse assembly path for lunar EBM machine; electron gun/powder subsystems assumed available."
notes: Local assembly route for EBM machine; refine with subsystem BOMs later.
```

`kb/recipes/recipe_ebm_powder_handling_system_v0.yaml`

```yaml
id: recipe_ebm_powder_handling_system_v0
kind: recipe
target_item_id: ebm_powder_handling_system_v0
inputs:
  - item_id: steel_plate_or_sheet
    qty: 50.0
    unit: kg
  - item_id: mill_shell_generic
    qty: 1
    unit: unit
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: unit
  - item_id: collection_hopper_set
    qty: 1
    unit: unit
  - item_id: bearing_set_heavy
    qty: 1
    unit: unit
  - item_id: drive_motor_medium
    qty: 1
    unit: unit
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: unit
  - item_id: support_frame_welded
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
  - item_id: assembled_equipment
    qty: 60.0
    unit: kg
outputs:
  - item_id: ebm_powder_handling_system_v0
    qty: 60.0
    unit: kg
steps:
  - process_id: metal_forming_basic_v0
    inputs:
      - item_id: steel_plate_or_sheet
        qty: 50.0
        unit: kg
    outputs:
      - item_id: formed_metal_part
        qty: 47.5
        unit: kg
  - process_id: welding_brazing_basic_v0
    inputs:
      - item_id: formed_metal_part
        qty: 47.5
        unit: kg
    outputs:
      - item_id: welded_assemblies
        qty: 47.0
        unit: kg
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: welded_assemblies
        qty: 47.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 46.5
        unit: kg
  - process_id: surface_treatment_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 46.5
        unit: kg
    outputs:
      - item_id: metal_part_surface_treated
        qty: 46.5
        unit: kg
  - process_id: enclosure_assembly_basic_v0
    inputs:
      - item_id: metal_part_surface_treated
        qty: 46.5
        unit: kg
      - item_id: mill_shell_generic
        qty: 1
        unit: unit
      - item_id: liner_set_abrasion_resistant
        qty: 1
        unit: unit
      - item_id: collection_hopper_set
        qty: 1
        unit: unit
      - item_id: bearing_set_heavy
        qty: 1
        unit: unit
      - item_id: drive_motor_medium
        qty: 1
        unit: unit
      - item_id: gearbox_reducer_medium
        qty: 1
        unit: unit
      - item_id: support_frame_welded
        qty: 1
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1
        unit: unit
    outputs:
      - item_id: assembled_equipment
        qty: 60.0
        unit: kg
  - process_id: alignment_and_testing_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 60.0
        unit: kg
    outputs:
      - item_id: ebm_powder_handling_system_v0
        qty: 60.0
        unit: kg
notes: "Placeholder recipe for EBM powder handling system; mirrors the ebm_vacuum_chamber_v0 production chain for seed path."
```

`kb/recipes/recipe_slm_machine_lunar_v0_v0.yaml`

```yaml
id: recipe_slm_machine_lunar_v0_v0
kind: recipe
name: Recipe for slm_machine_lunar_v0
target_item_id: slm_machine_lunar_v0
inputs:
  - item_id: machine_frame_small
    qty: 1.0
    unit: unit
  - item_id: power_electronics_module
    qty: 1.0
    unit: unit
  - item_id: steel_plate_or_sheet
    qty: 432.5
    unit: kg
outputs:
  - item_id: slm_machine_lunar_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: slm_machine_lunar_v0_assembly_v0
    inputs:
      - item_id: machine_frame_small
        qty: 1.0
        unit: unit
      - item_id: power_electronics_module
        qty: 1.0
        unit: unit
      - item_id: steel_plate_or_sheet
        qty: 432.5
        unit: kg
    outputs:
      - item_id: slm_machine_lunar_v0
        qty: 1.0
        unit: unit
notes: Assemble slm_machine_lunar_v0 from machine_frame_small and power_electronics_module using assembly_station.
```

`kb/recipes/recipe_lens_machine_lunar_v0_v0.yaml`

```yaml
id: recipe_lens_machine_lunar_v0_v0
kind: recipe
name: Recipe for lens_machine_lunar_v0
target_item_id: lens_machine_lunar_v0
variant_id: v0
inputs:
  - item_id: machine_frame_small
    qty: 1.0
    unit: unit
  - item_id: power_electronics_module
    qty: 1.0
    unit: unit
outputs:
  - item_id: lens_machine_lunar_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: lens_machine_lunar_v0_assembly_v0
    inputs:
      - item_id: machine_frame_small
        qty: 1.0
        unit: unit
      - item_id: power_electronics_module
        qty: 1.0
        unit: unit
    outputs:
      - item_id: lens_machine_lunar_v0
        qty: 1.0
        unit: unit
notes: Assemble lens_machine_lunar_v0 from machine_frame_small and power_electronics_module using assembly_station.
```

`kb/recipes/recipe_powder_quality_analysis_v0.yaml`

```yaml
id: recipe_powder_quality_analysis_v0
kind: recipe
target_item_id: powder_quality_analysis_v0
produces_id: powder_quality_analysis_v0
produces_qty: 1.0
produces_unit: unit
inputs:
  - item_id: optical_microscope_v0
    qty: 1.0
    unit: unit
  - item_id: screening_equipment
    qty: 1.0
    unit: unit
outputs:
  - item_id: powder_quality_analysis_v0
    qty: 1.0
    unit: unit
steps:
- process_id: powder_quality_machine_assembly_v0
  inputs:
    - item_id: optical_microscope_v0
      qty: 1.0
      unit: unit
    - item_id: screening_equipment
      qty: 1.0
      unit: unit
  outputs:
    - item_id: powder_quality_analysis_v0
      qty: 1.0
      unit: unit
notes: Assemble powder quality analysis system from optical microscope v0 and screening equipment v0
```

`kb/recipes/recipe_build_atmosphere_control_v0.yaml`

```yaml
id: recipe_build_atmosphere_control_v0
kind: recipe
target_item_id: build_atmosphere_control_v0
name: Recipe for atmosphere control system build v0
variant_id: v0
inputs:
  - item_id: vacuum_pump_small
    qty: 1
    unit: unit
  - item_id: gas_cylinder_mount
    qty: 2
    unit: unit
  - item_id: flow_controller_valve_set
    qty: 1
    unit: unit
  - item_id: oxygen_sensor_zirconia
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: piping_assembly_small
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: enclosure_steel_small
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
  - item_id: steel_frame_welded
    qty: 30.2
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 6.53
    unit: kg
outputs:
  - item_id: build_atmosphere_control_v0
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: vacuum_pump_small
        qty: 1
        unit: unit
      - item_id: gas_cylinder_mount
        qty: 2
        unit: unit
      - item_id: flow_controller_valve_set
        qty: 1
        unit: unit
      - item_id: oxygen_sensor_zirconia
        qty: 1
        unit: unit
      - item_id: pressure_gauge_set
        qty: 1
        unit: unit
      - item_id: piping_assembly_small
        qty: 1
        unit: unit
      - item_id: control_panel_basic
        qty: 1
        unit: unit
      - item_id: enclosure_steel_small
        qty: 1
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1
        unit: unit
      - item_id: steel_frame_welded
        qty: 30.2
        unit: kg
      - item_id: electrical_wire_and_connectors
        qty: 6.53
        unit: kg
    outputs:
      - item_id: build_atmosphere_control_v0
        qty: 1
        unit: unit
    byproducts:
      - item_id: waste
        qty: 0.2
        unit: kg
    est_time_hr: 9.5
    labor_hours: 7.0
    machine_hours: 3.5
    notes: "Receive components, assemble vacuum pump with gas cylinder mounts, integrate flow controllers and sensors, wire control panel and electrical systems, mount in steel enclosure, seal and test atmosphere control"
assumptions: "Vacuum pump evacuates chamber, gas cylinders supply inert gas, flow controllers regulate gas flow, oxygen sensor monitors purity"
notes: "Assembly of atmosphere control system for build chamber - used in metal AM and other oxygen-sensitive processes"
```

`kb/recipes/recipe_metal_powder_sieving_system_v0.yaml`

```yaml
id: recipe_metal_powder_sieving_system_v0
kind: recipe
target_item_id: metal_powder_sieving_system_v0
variant_id: v0
inputs:
  - item_id: screen_deck_basic
    qty: 1.0
    unit: unit
  - item_id: vibrator_motor_small
    qty: 1.0
    unit: unit
  - item_id: machine_frame_small
    qty: 1.0
    unit: unit
  - item_id: collection_hopper_set
    qty: 1.0
    unit: unit
  - item_id: power_conditioning_module
    qty: 1.0
    unit: unit
outputs:
  - item_id: metal_powder_sieving_system_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: screen_deck_basic
        qty: 1.0
        unit: unit
      - item_id: vibrator_motor_small
        qty: 1.0
        unit: unit
      - item_id: machine_frame_small
        qty: 1.0
        unit: unit
      - item_id: collection_hopper_set
        qty: 1.0
        unit: unit
      - item_id: power_conditioning_module
        qty: 1.0
        unit: unit
    outputs:
      - item_id: metal_powder_sieving_system_v0
        qty: 1.0
        unit: unit
notes: "Placeholder recipe to manufacture metal_powder_sieving_system_v0; uses BOM components via bom_metal_powder_sieving_system_v0. This is a minimal fix to satisfy the no_recipe gap."
```

`kb/processes/slm_machine_lunar_v0_assembly_v0.yaml`

```yaml
id: slm_machine_lunar_v0_assembly_v0
kind: process
name: SLM Lunar machine assembly v0
layer_tags:
- layer_7
- layer_8
process_type: batch
inputs:
- item_id: machine_frame_small
  qty: 1.0
  unit: unit
- item_id: power_electronics_module
  qty: 1.0
  unit: unit
outputs:
- item_id: slm_machine_lunar_v0
  qty: 1.0
  unit: unit
resource_requirements:
- machine_id: labor_bot_general_v0
  qty: 1
  unit: count
- machine_id: assembly_station
  qty: 1
  unit: count
energy_model:
  type: fixed_per_batch
  value: 6.0
  unit: kWh
time_model:
  type: batch
  hr_per_batch: 3.0
notes: Assembles slm_machine_lunar_v0 from machine_frame_small and power_electronics_module
  using assembly_station.
```

`kb/processes/lens_machine_lunar_v0_assembly_v0.yaml`

```yaml
id: lens_machine_lunar_v0_assembly_v0
kind: process
name: LENs Lunar machine assembly v0
layer_tags:
- layer_7
- layer_8
process_type: batch
inputs:
- item_id: machine_frame_small
  qty: 1.0
  unit: unit
- item_id: power_electronics_module
  qty: 1.0
  unit: unit
outputs:
- item_id: lens_machine_lunar_v0
  qty: 1.0
  unit: unit
resource_requirements:
- machine_id: labor_bot_general_v0
  qty: 1
  unit: count
- machine_id: assembly_station
  qty: 1
  unit: count
energy_model:
  type: fixed_per_batch
  value: 6.0
  unit: kWh
time_model:
  type: batch
  hr_per_batch: 3.0
notes: Assembles lens_machine_lunar_v0 from machine_frame_small and power_electronics_module
  using assembly_station.
```

`kb/processes/powder_quality_machine_assembly_v0.yaml`

```yaml
id: powder_quality_machine_assembly_v0
kind: process
name: Powder quality analysis system assembly v0
process_type: batch
inputs:
  - item_id: optical_microscope_v0
    qty: 1.0
    unit: unit
  - item_id: screening_equipment
    qty: 1.0
    unit: unit
outputs:
- item_id: powder_quality_analysis_v0
  qty: 1.0
  unit: unit
resource_requirements:
- machine_id: labor_bot_general_v0
  qty: 1
  unit: count
energy_model:
  type: fixed_per_batch
  value: 0.8
  unit: kWh
time_model:
  type: batch
  hr_per_batch: 1.5
notes: 'Assemble the powder quality analysis system from an optical microscope v0
  and screening equipment v0.

  This is a placeholder assembly process to enable local manufacturing of the machine
  in the KB.'
```
## 2026-07-16 / codex / Zero-Support High-Confidence Machine Removal

Status: applied

Source: `apps/simviewer/public/data/machine_usage_index.json` zero-support review.

Scope: 36 non-target `kind: machine` entries with `supported_process_count: 0`, plus exact self-production BOM/recipe YAMLs.

Decision rule: remove only entries whose exact KB references are the item definition and manufacturing routes for that same ID. Substring collisions such as `rock_crusher_basic`, `coil_winding_machine`, and `rolling_mill_v0` were not treated as references to the removed base ID.

Removal reason: supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item.

Possible negative impacts:
- Exact-ID lookups for these machines will disappear from KB and SimViewer exports.
- Self-production BOM/recipe paths for these IDs are removed; reintroduction should restore from this log or map to a surviving machine.
- Some generic aliases, for example broad press/test/power/winding labels, may need explicit remapping if future processes try to use them as capacity providers.

Per-entry summary:

| Machine ID | Deleted YAML count | Removal reason | Possible adverse impact |
| --- | ---: | --- | --- |
| `assembly_workbench_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `carbon_safety_system_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `carbon_safety_system_v0_v0` | 4 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `carbonyl_safety_system_v0_v0` | 4 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `chemical_reactor_unit_v1` | 4 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `chemical_reactor_unit_v1_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `crucible_set` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `crusher_basic` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `cryogenic_chiller_provider_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `cryogenic_chiller_provider_v0_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `electrical_test_equipment` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `electrolyzer_pem_v0_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `filler_material_station_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `hot_wire_cutter_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `hydraulic_press_small` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `kapvik_microrover_30kg_v0` | 1 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `kiln_basic` | 4 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `labor_bot_basic_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `labor_bot_specialist_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `power_conditioner` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `power_hammer_or_press_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `power_supply_high_voltage` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `precision_stage` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `press_brake_or_roller` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `press_hydraulic` | 5 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `pressure_test_rig_basic_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `programming_adapter_or_jig` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `punch_press_drill` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `refining_furnace_v0` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `rolling_mill` | 4 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `signal_generator` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `temperature_sensing` | 1 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `test_equipment_electronics` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `thermal_water_extractor` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `thermionic_generator` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |
| `winding_machine` | 3 | supported_process_count is 0 in apps/simviewer/public/data/machine_usage_index.json; not present in docs/self_reproducing_set.txt; exact KB references are limited to the item itself and recipes/BOMs that manufacture that same obsolete or duplicate item. | Future work that expects this exact ID will need to choose an existing concrete provider or restore the payload from this log; deleting the self-manufacturing recipe/BOM also removes a possible seed route if the item is later reintroduced. |

Deleted YAML payloads:

### `assembly_workbench_v0`

`kb/boms/bom_assembly_workbench_v0.yaml`

```yaml
id: bom_assembly_workbench_v0
owner_item_id: assembly_workbench_v0
components:
  - item_id: workbench_basic
    qty: 1
  - item_id: table_top_t_slot
    qty: 1
notes: Basic BOM for assembly_workbench_v0 combining a standard workbench base with a T-slotted table top.
```

`kb/items/machines/assembly_workbench_v0.yaml`

```yaml
id: assembly_workbench_v0
kind: machine
name: Assembly workbench v0
mass: 120.0
unit: unit
bom: bom_assembly_workbench_v0
capabilities:
- assembly
- fixturing_table
notes: Dedicated assembly workbench providing stable surface and fixturing for manual
  assembly tasks.
recipe: recipe_assembly_workbench_v0
unit_kind: discrete
```

`kb/recipes/recipe_assembly_workbench_v0.yaml`

```yaml
id: recipe_assembly_workbench_v0
kind: recipe
target_item_id: assembly_workbench_v0
inputs:
  - item_id: workbench_basic
    qty: 1
    unit: unit
  - item_id: table_top_t_slot
    qty: 1
    unit: unit
outputs:
  - item_id: assembly_workbench_v0
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: workbench_basic
        qty: 1
        unit: unit
      - item_id: table_top_t_slot
        qty: 1
        unit: unit
    outputs:
      - item_id: assembly_workbench_v0
        qty: 1
        unit: unit
    est_time_hr: 0.5
    labor_hours: 0.5
    notes: "Mount T-slotted table top onto workbench base"
notes: "Assembly workbench combining standard workbench base with T-slotted table top for fixturing."
```

### `carbon_safety_system_v0`

`kb/boms/bom_carbon_safety_system_v0.yaml`

```yaml
id: bom_carbon_safety_system_v0
owner_item_id: carbon_safety_system_v0
kind: bom
target_item_id: carbon_safety_system_v0
variant_id: v0
requires_ids:
  - gasket_sheet_core_v0_part
  - gas_inlet_manifold_v0
  - valve_body_cast_rough_v0
components:
  - item_id: gasket_sheet_core_v0_part
    qty: 1.0
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
notes: "Resolved referenced_only gap by aligning BOM with v0_seed and existing gasket_sheet_core_v0_part."
```

`kb/items/machines/carbon_safety_system_v0.yaml`

```yaml
id: carbon_safety_system_v0
name: Carbon Safety System v0
kind: machine
mass: 5.5
unit: unit
bom: bom_carbon_safety_system_v0
material_class: steel
capabilities:
- safety_monitoring
- emergency_shutdown
notes: Version v0 carbon safety system; aligns with non-versioned BOM reference.
recipe: recipe_carbon_safety_system_v0
unit_kind: discrete
```

`kb/recipes/recipe_carbon_safety_system_v0.yaml`

```yaml
id: recipe_carbon_safety_system_v0
kind: recipe
target_item_id: carbon_safety_system_v0
variant_id: v0
inputs:
  - item_id: gasket_sheet
    qty: 1.0
    unit: unit
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
    unit: unit
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
    unit: unit
outputs:
  - item_id: carbon_safety_system_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    est_time_hr: 8.0
    machine_hours: 8.0
    labor_hours: 4.0
    inputs:
      - item_id: gasket_sheet
        qty: 1.0
        unit: unit
      - item_id: gas_inlet_manifold_v0
        qty: 1.0
        unit: unit
      - item_id: valve_body_cast_rough_v0
        qty: 1.0
        unit: unit
    outputs:
      - item_id: carbon_safety_system_v0
        qty: 1.0
        unit: unit
notes: "Seed assembly path for carbon_safety_system_v0 using seed BOM components."
```

### `carbon_safety_system_v0_v0`

`kb/boms/bom_carbon_safety_system_v0_v0.yaml`

```yaml
id: bom_carbon_safety_system_v0_v0
kind: bom
owner_item_id: carbon_safety_system_v0_v0
target_item_id: carbon_safety_system_v0_v0
components:
  - item_id: gasket_sheet_part_v0
    qty: 1.0
    unit: unit
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
    unit: unit
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
    unit: unit
requires_ids:
  - gasket_sheet_part_v0
  - gas_inlet_manifold_v0
  - valve_body_cast_rough_v0
notes: "Resolved IDs by using gasket_sheet_part_v0 to avoid gasket_sheet ID duplication between material and part."
```

`kb/boms/bom_carbon_safety_system_v0_v0_seed.yaml`

```yaml
id: bom_carbon_safety_system_v0_v0_seed
kind: bom
owner_item_id: carbon_safety_system_v0_v0

target_item_id: carbon_safety_system_v0_v0
components:
  - item_id: gasket_sheet_part_v0
    qty: 1.0
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
requires_ids:
  - gasket_sheet_part_v0
  - gas_inlet_manifold_v0
  - valve_body_cast_rough_v0
notes: "Seed BOM mirrored for bom_carbon_safety_system_v0_v0 to resolve referenced_only gap."
```

`kb/items/machines/carbon_safety_system_v0_v0.yaml`

```yaml
id: carbon_safety_system_v0_v0
name: Carbon Safety System v0
kind: machine
mass: 60.0
unit: unit
bom: bom_carbon_safety_system_v0_v0
material_class: steel
capabilities:
- safety_monitoring
- emergency_shutdown
notes: Version v0.0 carbon safety system; separate item to satisfy no_recipe gap for
  BOM.
recipe: recipe_carbon_safety_system_v0_v0
unit_kind: discrete
```

`kb/recipes/recipe_carbon_safety_system_v0_v0.yaml`

```yaml
id: recipe_carbon_safety_system_v0_v0
kind: recipe
target_item_id: carbon_safety_system_v0_v0
variant_id: v0
inputs:
  - item_id: gasket_sheet_part_v0
    qty: 5.5
    unit: kg
  - item_id: gas_inlet_manifold_v0
    qty: 22.0
    unit: kg
  - item_id: valve_body_cast_rough_v0
    qty: 32.5
    unit: kg
outputs:
  - item_id: carbon_safety_system_v0_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    est_time_hr: 8.0
    machine_hours: 8.0
    labor_hours: 4.0
    inputs:
      - item_id: gasket_sheet_part_v0
        qty: 5.5
        unit: kg
      - item_id: gas_inlet_manifold_v0
        qty: 22.0
        unit: kg
      - item_id: valve_body_cast_rough_v0
        qty: 32.5
        unit: kg
    outputs:
      - item_id: carbon_safety_system_v0_v0
        qty: 1.0
        unit: unit
notes: "Seed assembly path for carbon_safety_system_v0_v0 using seed BOM components. Input masses scaled to balance output mass placeholder (60 kg)."
```

### `carbonyl_safety_system_v0_v0`

`kb/boms/bom_carbonyl_safety_system_v0_v0.yaml`

```yaml
id: bom_carbonyl_safety_system_v0_v0
owner_item_id: carbonyl_safety_system_v0_v0
kind: bom

target_item_id: carbonyl_safety_system_v0_v0
variant_id: v0
requires_ids:
  - gasket_sheet_part_v0
  - gas_inlet_manifold_v0
  - valve_body_cast_rough_v0
components:
  - item_id: gasket_sheet_part_v0
    qty: 1.0
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
notes: "Canonical BOM aligned with v0_seed; resolves referenced_only gap for carbonyl_safety_system_v0_v0 by using gasket_sheet_part_v0."
```

`kb/boms/bom_carbonyl_safety_system_v0_v0_seed.yaml`

```yaml
id: bom_carbonyl_safety_system_v0_v0_seed
kind: bom
owner_item_id: carbonyl_safety_system_v0_v0

target_item_id: carbonyl_safety_system_v0_v0
variant_id: v0
requires_ids:
  - gasket_sheet
  - gas_inlet_manifold_v0
  - valve_body_cast_rough_v0
components:
  - item_id: gasket_sheet
    qty: 1.0
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
notes: "Seed BOM to resolve referenced_only gap for carbonyl_safety_system_v0_v0."
```

`kb/items/machines/carbonyl_safety_system_v0_v0.yaml`

```yaml
id: carbonyl_safety_system_v0_v0
name: Carbonyl Safety System v0 v0
kind: machine
mass: 3.0
unit: unit
bom: bom_carbonyl_safety_system_v0_v0
capabilities:
- safety_monitoring
- emergency_shutdown
notes: 'Assumptions:

  - Mass aligned to current recipe component sum (3 kg).

  Versioned Carbonyl Safety System v0_v0 aligned with seed BOM to resolve referenced_only

  gap.

  '
recipe: recipe_carbonyl_safety_system_v0_v0
unit_kind: discrete
```

`kb/recipes/recipe_carbonyl_safety_system_v0_v0.yaml`

```yaml
id: recipe_carbonyl_safety_system_v0_v0
kind: recipe
target_item_id: carbonyl_safety_system_v0_v0
variant_id: v0
inputs:
  - item_id: gasket_sheet_part_v0
    qty: 1.0
    unit: kg
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
    unit: kg
  - item_id: valve_body_cast_rough_v0
    qty: 1.0
    unit: kg
outputs:
  - item_id: carbonyl_safety_system_v0_v0
    qty: 3.0
    unit: kg
steps:
  - process_id: assembly_basic_v0
    est_time_hr: 8.0
    machine_hours: 8.0
    labor_hours: 4.0
    inputs:
      - item_id: gasket_sheet_part_v0
        qty: 1.0
        unit: kg
      - item_id: gas_inlet_manifold_v0
        qty: 1.0
        unit: kg
      - item_id: valve_body_cast_rough_v0
        qty: 1.0
        unit: kg
    outputs:
      - item_id: carbonyl_safety_system_v0_v0
        qty: 3.0
        unit: kg
notes: "Seed assembly path for carbonyl_safety_system_v0_v0 using seed BOM components."
```

### `chemical_reactor_unit_v1`

`kb/boms/bom_chemical_reactor_unit_v1.yaml`

```yaml
id: bom_chemical_reactor_unit_v1
kind: bom
owner_item_id: chemical_reactor_unit_v1
target_item_id: chemical_reactor_unit_v1
variant_id: v1
components:
  - item_id: import_misc_components_set
    qty: 1.0
    unit: unit
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
    unit: unit
notes: Seed BOM for chemical_reactor_unit_v1; placeholder until real components are defined.
```

`kb/items/machines/chemical_reactor_unit_v1.yaml`

```yaml
id: chemical_reactor_unit_v1
name: Chemical Reactor Unit v1
kind: machine
mass: 220.0
mass_kg: 220.0
unit: unit
bom: bom_chemical_reactor_unit_v1
notes: Upgraded chemical reactor unit with similar capabilities to v0; placeholder
  BOM.
capabilities:
- molten_salt_electrolysis
- high_temperature_processing
- gas_extraction
recipe: recipe_chemical_reactor_unit_v1
unit_kind: discrete
```

`kb/recipes/recipe_chemical_reactor_unit_v1.yaml`

```yaml
id: recipe_chemical_reactor_unit_v1
kind: recipe
target_item_id: chemical_reactor_unit_v1
variant_id: v0
inputs:
  - item_id: equipment_imported
    qty: 220.0
    unit: kg
outputs:
  - item_id: chemical_reactor_unit_v1
    qty: 220.0
    unit: kg
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: equipment_imported
        qty: 220.0
        unit: kg
    outputs:
      - item_id: equipment_imported
        qty: 220.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
  - process_id: assembly_basic_v0
    inputs:
      - item_id: equipment_imported
        qty: 220.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 220.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 220.0
        unit: kg
    outputs:
      - item_id: chemical_reactor_unit_v1
        qty: 220.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
assumptions: "Placeholder recipe to resolve no_recipe gap for chemical_reactor_unit_v1; reuses basic import/assembly/inspection steps."
notes: "Placeholder path to validate integration; update BOM/actual steps as design matures."
```

`kb/recipes/recipe_chemical_reactor_unit_v1_v1.yaml`

```yaml
id: recipe_chemical_reactor_unit_v1_v1
kind: recipe
target_item_id: chemical_reactor_unit_v1
variant_id: v1
inputs:
  - item_id: bulk_material_or_parts
    qty: 47.0
    unit: kg
  - item_id: import_misc_components_set
    qty: 1.0
    unit: kg
  - item_id: gas_inlet_manifold_v0
    qty: 2.0
    unit: kg
outputs:
  - item_id: chemical_reactor_unit_v1
    qty: 50.0
    unit: kg
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: bulk_material_or_parts
        qty: 47.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
  - process_id: assembly_basic_v0
    inputs:
      - item_id: import_misc_components_set
        qty: 1.0
        unit: kg
      - item_id: gas_inlet_manifold_v0
        qty: 2.0
        unit: kg
      - item_id: bulk_material_or_parts
        qty: 47.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 50.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 50.0
        unit: kg
    outputs:
      - item_id: chemical_reactor_unit_v1
        qty: 50.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
assumptions: "Assemble chemical_reactor_unit_v1 from BOM components; placeholder steps for now."
notes: |
  Assumptions:
  - Output mass aligned to assembled_equipment placeholder (50 kg).
  Placeholder machine-assembly path to close no_recipe gap for chemical_reactor_unit_v1.
```

### `chemical_reactor_unit_v1_v0`

`kb/boms/bom_chemical_reactor_unit_v1_v0.yaml`

```yaml
id: bom_chemical_reactor_unit_v1_v0
kind: bom
owner_item_id: chemical_reactor_unit_v1_v0
target_item_id: chemical_reactor_unit_v1_v0
variant_id: v0
components:
  - item_id: import_misc_components_set
    qty: 1.0
    unit: unit
  - item_id: gas_inlet_manifold_v0
    qty: 1.0
    unit: unit
notes: Seed BOM for chemical_reactor_unit_v1_v0; placeholder until real components are defined.
```

`kb/items/machines/chemical_reactor_unit_v1_v0.yaml`

```yaml
id: chemical_reactor_unit_v1_v0
name: Chemical Reactor Unit v1
kind: machine
mass: 1200.0
mass_kg: 1200.0
unit: unit
bom: bom_chemical_reactor_unit_v1_v0
capabilities:
- chemical_reaction
- agitation
- gas_inlet
notes: Placeholder chemical reactor unit v1; to be refined with actual specs.
recipe: recipe_chemical_reactor_unit_v1_v0
unit_kind: discrete
```

`kb/recipes/recipe_chemical_reactor_unit_v1_v0.yaml`

```yaml
id: recipe_chemical_reactor_unit_v1_v0
kind: recipe
target_item_id: chemical_reactor_unit_v1_v0
variant_id: v0
inputs:
  - item_id: bulk_material_or_parts
    qty: 1.0
    unit: kg
outputs:
  - item_id: chemical_reactor_unit_v1_v0
    qty: 1.0
    unit: kg
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: bulk_material_or_parts
        qty: 1.0
        unit: kg
    outputs:
      - item_id: bulk_material_or_parts
        qty: 1.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
  - process_id: assembly_basic_v0
    inputs:
      - item_id: bulk_material_or_parts
        qty: 1.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 1.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 1.0
        unit: kg
    outputs:
      - item_id: chemical_reactor_unit_v1_v0
        qty: 1.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
assumptions: "Assemble chemical_reactor_unit_v1_v0 from BOM components; placeholder steps for now."
notes: "Placeholder machine-assembly path to close no_recipe gap for chemical_reactor_unit_v1_v0."
```

### `crucible_set`

`kb/boms/bom_crucible_set_v0.yaml`

```yaml
id: bom_crucible_set_v0
owner_item_id: crucible_set
components:
  - item_id: crucible_graphite_large
    qty: 2
  - item_id: crucible_graphite_small
    qty: 3
  - item_id: crucible_ceramic_refractory
    qty: 2
  - item_id: crucible_tongs_set
    qty: 1
notes: Set of crucibles in various sizes for metal casting with graphite and ceramic options.
```

`kb/items/machines/crucible_set.yaml`

```yaml
id: crucible_set
kind: machine
name: Crucible set
mass: 50.0
unit: unit
bom: bom_crucible_set_v0
notes: Set of refractory crucibles for holding molten metal during casting. Graphite
  or ceramic construction for various metal types.
recipe: recipe_crucible_set_v0
unit_kind: discrete
```

`kb/recipes/recipe_crucible_set_v0.yaml`

```yaml
id: recipe_crucible_set_v0
target_item_id: crucible_set
variant_id: v0
inputs:
  - item_id: refractory_castable
    qty: 50.0
    unit: kg
  - item_id: machined_part_raw
    qty: 5.0
    unit: kg
outputs:
  - item_id: crucible_set
    qty: 50.0
    unit: kg
steps:
  - process_id: refractory_casting_v0
    inputs:
      - item_id: refractory_castable
        qty: 50.0
        unit: kg
    outputs:
      - item_id: wet_material
        qty: 50.0
        unit: kg
    est_time_hr: 4.0
    labor_hours: 4.0
    notes: "Cast crucibles from refractory mix or graphite-clay composite"
  - process_id: drying_and_curing_v0
    inputs:
      - item_id: wet_material
        qty: 50.0
        unit: kg
    outputs:
      - item_id: dried_material
        qty: 50.0
        unit: kg
    est_time_hr: 12.0
    machine_hours: 12.0
    notes: "Dry crucibles slowly to prevent cracking"
  - process_id: firing_v0
    inputs:
      - item_id: dried_material
        qty: 50.0
        unit: kg
    outputs:
      - item_id: ceramic_fired_high_temp
        qty: 47.0
        unit: kg
    byproducts:
      - item_id: waste
        qty: 3.0
        unit: kg
    est_time_hr: 8.0
    machine_hours: 8.0
    notes: "Fire crucibles to final hardness and temperature resistance. ~6% shrinkage/loss during firing."
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 5.0
        unit: kg
    outputs:
      - item_id: finished_part_deburred
        qty: 3.0
        unit: kg
    byproducts:
      - item_id: metal_swarf
        qty: 2.0
        unit: kg
    est_time_hr: 2.0
    machine_hours: 2.0
    notes: "Machine crucible tongs from steel stock"
  - process_id: assembly_basic_v0
    inputs:
      - item_id: ceramic_fired_high_temp
        qty: 47.0
        unit: kg
      - item_id: finished_part_deburred
        qty: 3.0
        unit: kg
    outputs:
      - item_id: crucible_set
        qty: 50.0
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
    notes: "Assemble fired crucibles with machined tongs into complete set. Includes inspection and testing."
assumptions: Refractory or graphite crucibles formed, dried, and fired. Tongs fabricated from steel.
notes: Set of casting crucibles with handling tongs for metal melting operations. Graphite crucibles may be imported if local graphite is unavailable.
```

### `crusher_basic`

`kb/boms/bom_crusher_basic_v0.yaml`

```yaml
id: bom_crusher_basic_v0
owner_item_id: crusher_basic
components:
  - item_id: crusher_frame_medium
    qty: 1
  - item_id: crushing_jaw_set
    qty: 1
  - item_id: drive_motor_medium
    qty: 1
  - item_id: vibration_motor_set
    qty: 1
  - item_id: gearbox_reducer_medium
    qty: 1
  - item_id: support_frame_welded
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
notes: Placeholder BOM for legacy crusher; aligns with jaw crusher layout. Will be deprecated once rock_crusher_basic fully replaces this entry.
```

`kb/items/machines/crusher_basic.yaml`

```yaml
id: crusher_basic
kind: machine
name: Crusher (basic)
mass: 600.0
unit: unit
material_class: steel
bom: bom_crusher_basic_v0
notes: DEPRECATED - Consolidated into rock_crusher_basic. Basic jaw or impact crusher
  for primary size reduction of regolith/ore. Coarse placeholder mass for small industrial
  unit.
recipe: recipe_machine_crusher_basic_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_crusher_basic_v0.yaml`

```yaml
id: recipe_machine_crusher_basic_v0
kind: recipe
target_item_id: crusher_basic
variant_id: external_supply_v0
inputs:
  - item_id: bulk_material_or_parts
    qty: 600.0
    unit: kg
outputs:
  - item_id: crusher_basic
    qty: 1.0
    unit: unit
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: bulk_material_or_parts
        qty: 600.0
        unit: kg
    outputs:
      - item_id: crusher_basic
        qty: 1.0
        unit: unit
    est_time_hr: 1.0
    notes: Receive imported crusher until local fabrication is modeled.
assumptions: Primary crushing equipment is imported early; replace with local build later.
notes: Import receiving step to unblock crushing/grinding processes.
```

### `cryogenic_chiller_provider_v0`

`kb/boms/bom_cryogenic_chiller_provider_v0.yaml`

```yaml
id: bom_cryogenic_chiller_provider_v0
owner_item_id: cryogenic_chiller_provider_v0
kind: bom
components:
  - item_id: import_misc_components_set
    qty: 1.0
scrap_rate: 0.0
notes: "Placeholder BOM for cryogenic_chiller_provider_v0; to be expanded with real components."
```

`kb/items/machines/cryogenic_chiller_provider_v0.yaml`

```yaml
id: cryogenic_chiller_provider_v0
kind: machine
name: Cryogenic chiller provider (seed)
mass: 600.0
unit: unit
bom: bom_cryogenic_chiller_provider_v0_v0
notes: Seed provider machine that offers the cryogenic_chiller_v0 resource capability.
recipe: recipe_cryogenic_chiller_provider_v0
unit_kind: discrete
```

`kb/recipes/recipe_cryogenic_chiller_provider_v0.yaml`

```yaml
id: recipe_cryogenic_chiller_provider_v0
kind: recipe
target_item_id: cryogenic_chiller_provider_v0
variant_id: v0
inputs:
  - item_id: cryogenic_chiller_v0
    qty: 300.0
    unit: kg
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 5.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 280.0
    unit: kg
outputs:
  - item_id: cryogenic_chiller_provider_v0
    qty: 600.0
    unit: kg
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: cryogenic_chiller_v0
        qty: 300.0
        unit: kg
      - item_id: control_panel_basic
        qty: 1
        unit: unit
      - item_id: pressure_gauge_set
        qty: 5.0
        unit: kg
      - item_id: steel_plate_or_sheet
        qty: 280.0
        unit: kg
    outputs:
      - item_id: cryogenic_chiller_provider_v0
        qty: 600.0
        unit: kg
    est_time_hr: 8.0
    machine_hours: 2.0
    labor_hours: 6.0
    notes: "Assemble cryogenic chiller unit with control panel and pressure monitoring into provider machine configuration"
assumptions: "Seed provider machine that offers the cryogenic_chiller_v0 resource capability"
notes: |
  Assumptions:
  - Added steel plate for skid, enclosure, and mounting structure not captured in base chiller BOM.
  Rationale:
  - Balances provider mass to 600 kg output.
```

### `cryogenic_chiller_provider_v0_v0`

`kb/boms/bom_cryogenic_chiller_provider_v0_v0.yaml`

```yaml
id: bom_cryogenic_chiller_provider_v0_v0
owner_item_id: cryogenic_chiller_provider_v0_v0
kind: bom
target_item_id: cryogenic_chiller_provider_v0_v0
variant_id: v0
components: []
components:
  - item_id: cryogenic_chiller_v0
    qty: 1
    unit: unit
    notes: "Primary cryogenic chiller unit"
  - item_id: control_panel_basic
    qty: 1
    unit: unit
    notes: "Controls and monitoring interface"
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
    notes: "Pressure monitoring for refrigerant loop"
notes: "Seed BOM for cryogenic chiller provider; refine with refrigeration loop details later."
```

`kb/items/machines/cryogenic_chiller_provider_v0_v0.yaml`

```yaml
id: cryogenic_chiller_provider_v0_v0
name: Cryogenic chiller provider v0 (seed)
kind: machine
mass: 600.0
unit: unit
bom: bom_cryogenic_chiller_provider_v0_v0
notes: Seed provider machine version v0_v0; aligns with BOM bom_cryogenic_chiller_provider_v0_v0.yaml.
recipe: recipe_cryogenic_chiller_provider_v0_v0
unit_kind: discrete
```

`kb/recipes/recipe_cryogenic_chiller_provider_v0_v0.yaml`

```yaml
id: recipe_cryogenic_chiller_provider_v0_v0
kind: recipe
target_item_id: cryogenic_chiller_provider_v0_v0
inputs:
  - item_id: regolith_metal_crude
    qty: 650.0
    unit: kg
  - item_id: cryogenic_chiller_v0
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: pressure_gauge_set
    qty: 1
    unit: unit
  - item_id: machine_frame_heavy
    qty: 1
    unit: unit
  - item_id: passive_thermal_insulation_v0
    qty: 80.0
    unit: kg
outputs:
  - item_id: cryogenic_chiller_provider_v0_v0
    qty: 1
    unit: unit
steps:
  - process_id: metal_casting_basic_v0
    inputs:
      - item_id: regolith_metal_crude
        qty: 650.0
        unit: kg
    outputs:
      - item_id: cast_metal_parts
        qty: 617.5
        unit: kg
    notes: "Casting structural components for cryogenic chiller provider"
  - process_id: welding_brazing_basic_v0
    inputs:
      - item_id: cast_metal_parts
        qty: 617.5
        unit: kg
    outputs:
      - item_id: welded_assemblies
        qty: 600.0
        unit: kg
    notes: "Weld/braze frame and subassemblies"
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: welded_assemblies
        qty: 600.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 600.0
        unit: kg
    notes: "Finish machining on interfaces and mounting surfaces"
  - process_id: assembly_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 600.0
        unit: kg
    outputs:
      - item_id: machine_frame_heavy
        qty: 1
        unit: unit
    notes: "Pre-assembly of subcomponents into machine shell"
  - process_id: machine_assembly_basic_v0
    inputs:
      - item_id: machine_frame_heavy
        qty: 1
        unit: unit
      - item_id: cryogenic_chiller_v0
        qty: 1
        unit: unit
      - item_id: control_panel_basic
        qty: 1
        unit: unit
      - item_id: pressure_gauge_set
        qty: 1
        unit: unit
      - item_id: passive_thermal_insulation_v0
        qty: 80.0
        unit: kg
    outputs:
      - item_id: cryogenic_chiller_provider_v0_v0
        qty: 1
        unit: unit
    notes: "Final assembly: frame, electronics, wiring into cryogenic_chiller_provider_v0_v0"
notes: "Prototype recipe to manufacture cryogenic_chiller_provider_v0_v0; BOM details to be refined."
```

### `electrical_test_equipment`

`kb/boms/bom_electrical_test_equipment_v0.yaml`

```yaml
id: bom_electrical_test_equipment_v0
owner_item_id: electrical_test_equipment
target_item_id: electrical_test_equipment
variant_id: v0
components:
  - item_id: multimeter_digital
    qty: 1
    unit: unit
    notes: "Basic electrical measurements"
  - item_id: insulation_resistance_tester
    qty: 1
    unit: unit
    notes: "High voltage insulation testing (megger)"
  - item_id: ground_resistance_tester
    qty: 1
    unit: unit
    notes: "Ground connection verification"
  - item_id: power_supply_bench
    qty: 1
    unit: unit
    notes: "Controlled power source for functional testing"
  - item_id: test_lead_set
    qty: 1
    unit: unit
    notes: "Test probes and connection leads"
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: unit
    notes: "Equipment enclosure and organization"
notes: Bill of materials for electrical test equipment. Complete electrical verification and testing system.
```

`kb/items/machines/electrical_test_equipment.yaml`

```yaml
id: electrical_test_equipment
kind: machine
name: Electrical test equipment
mass: 40
mass_kg: 40
unit: unit
bom: bom_electrical_test_equipment_v0
material_class: electronic
notes: Deprecated; replaced by test_bench_electrical (kb/items/machines/test_bench_electrical.yaml).
  Use test_bench_electrical as the canonical item for electrical test capabilities.
  The existing electrical_test_equipment recipe (recipe_electrical_test_equipment_v0.yaml)
  remains for historical modeling but new designs should align with test_bench_electrical.
recipe: recipe_electrical_test_equipment_v0
unit_kind: discrete
```

`kb/recipes/recipe_electrical_test_equipment_v0.yaml`

```yaml
id: recipe_electrical_test_equipment_v0
target_item_id: electrical_test_equipment
variant_id: v0
produces_qty: 40.0
produces_unit: kg
inputs:
  - item_id: sheet_metal_or_structural_steel
    qty: 15.0
    unit: kg
  - item_id: multimeter_digital
    qty: 1.0
    unit: unit
  - item_id: insulation_resistance_tester
    qty: 1.0
    unit: unit
  - item_id: ground_resistance_tester
    qty: 1.0
    unit: unit
  - item_id: power_supply_bench
    qty: 1.0
    unit: unit
  - item_id: test_lead_set
    qty: 1.0
    unit: unit
  - item_id: enclosure_electrical_medium
    qty: 1.0
    unit: unit
  - item_id: electrical_wire_and_connectors
    qty: 1.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 13.0
    unit: kg
outputs:
  - item_id: electrical_test_equipment
    qty: 40.0
    unit: kg
steps:
  - process_id: sheet_metal_fabrication_v0
    inputs:
      - item_id: sheet_metal_or_structural_steel
        qty: 15.0
        unit: kg
    outputs:
      - item_id: formed_sheet_metal_parts
        qty: 14.0
        unit: kg
    est_time_hr: 2.0
    machine_hours: 2.0
    notes: "Fabricate equipment enclosure and mounting panels"
  - process_id: wiring_and_electronics_integration_v0
    inputs:
      - item_id: electrical_wire_and_connectors
        qty: 1.0
        unit: kg
      - item_id: multimeter_digital
        qty: 1.0
        unit: unit
      - item_id: insulation_resistance_tester
        qty: 1.0
        unit: unit
      - item_id: ground_resistance_tester
        qty: 1.0
        unit: unit
      - item_id: power_supply_bench
        qty: 1.0
        unit: unit
      - item_id: test_lead_set
        qty: 1.0
        unit: unit
    outputs:
      - item_id: wired_electrical_system
        qty: 11.0
        unit: kg
    est_time_hr: 6.0
    labor_hours: 6.0
    notes: "Wire and integrate multimeter, insulation tester, ground tester, and power supply"
  - process_id: assembly_basic_v0
    inputs:
      - item_id: formed_sheet_metal_parts
        qty: 14.0
        unit: kg
      - item_id: wired_electrical_system
        qty: 11.0
        unit: kg
      - item_id: enclosure_electrical_medium
        qty: 1.0
        unit: unit
      - item_id: steel_plate_or_sheet
        qty: 13.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 40.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: "Assemble components in enclosure, install test leads and connections"
  - process_id: calibration_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 40.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 40.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: "Calibrate measurement instruments and verify accuracy"
  - process_id: integration_test_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 40.0
        unit: kg
    outputs:
      - item_id: electrical_test_equipment
        qty: 40.0
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
    notes: "Test all measurement functions and safety features"
assumptions: Comprehensive electrical testing equipment with imported measurement electronics. Locally assembled and calibrated.
notes: Electrical test equipment for system verification. Includes continuity, insulation resistance, and ground testing capabilities.
```

### `electrolyzer_pem_v0_v0`

`kb/boms/bom_electrolyzer_pem_v0_v0.yaml`

```yaml
id: bom_electrolyzer_pem_v0_v0
kind: bom
owner_item_id: electrolyzer_pem_v0_v0
components:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: unit
  - item_id: separator_membrane_porous
    qty: 1
    unit: unit
  - item_id: gas_collection_system
    qty: 1
    unit: unit
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
```

`kb/items/machines/electrolyzer_pem_v0_v0.yaml`

```yaml
id: electrolyzer_pem_v0_v0
name: PEM Electrolyzer (v0 v0)
kind: machine
mass: 100.0
mass_kg: 100.0
unit: unit
bom: bom_electrolyzer_pem_v0_v0
notes: 'PEM electrolyzer variant v0_v0; placeholder BOM to be refined from hardware
  data.


  Mass updated 2026-01 from 260 kg to 100 kg based on BOM component analysis:

  - Cell stack: 25 kg

  - Power supply: 40 kg

  - Gas collection system: 30 kg

  - Membrane: 0.15 kg

  - Fasteners: 1 kg

  - Housing/structure/misc: ~4 kg (estimated)

  Total: ~100 kg

  '
recipe: recipe_electrolyzer_pem_v0_v0
unit_kind: discrete
```

`kb/recipes/recipe_electrolyzer_pem_v0_v0.yaml`

```yaml
id: recipe_electrolyzer_pem_v0_v0
kind: recipe
name: PEM Electrolyzer v0 v0 production recipe
variant_id: v0
target_item_id: electrolyzer_pem_v0_v0
inputs:
  - item_id: electrolyzer_cell_stack
    qty: 25.0
    unit: kg
  - item_id: separator_membrane_porous
    qty: 0.15
    unit: kg
  - item_id: gas_collection_system
    qty: 30.0
    unit: kg
  - item_id: power_supply_dc_high_current
    qty: 40.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 4.0
    unit: kg
outputs:
  - item_id: electrolyzer_pem_v0_v0
    qty: 100.0
    unit: kg
steps:
  - process_id: machine_assembly_basic_v0
    inputs:
      - item_id: electrolyzer_cell_stack
        qty: 25.0
        unit: kg
      - item_id: separator_membrane_porous
        qty: 0.15
        unit: kg
      - item_id: power_supply_dc_high_current
        qty: 40.0
        unit: kg
      - item_id: gas_collection_system
        qty: 30.0
        unit: kg
      - item_id: fastener_kit_medium
        qty: 1.0
        unit: kg
      - item_id: steel_plate_or_sheet
        qty: 4.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 100.0
        unit: kg
    est_time_hr: 6.0
    machine_hours: 4.0
    labor_hours: 5.0
    notes: "Fabricate housing from steel plate, assemble PEM stack, install membrane, mount power supply and gas collection system, wire electrical connections. Total: 25 kg (stack) + 40 kg (power) + 30 kg (gas) + 0.15 kg (membrane) + 1 kg (fasteners) + 4 kg (housing) = 100.15 kg ≈ 100 kg."
  - process_id: leak_test_v0
    inputs:
      - item_id: assembled_equipment
        qty: 100.0
        unit: kg
    outputs:
      - item_id: electrolyzer_pem_v0_v0
        qty: 100.0
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
    notes: "Pressure test housing seals, verify electrical connections and gas output quality."
notes: |
  Recipe corrected 2026-01 to fix mass balance errors:
  - Removed generic intermediate items (assembled_equipment, assembled_electrical_equipment)
  - Consolidated 4 steps into 2: assembly + sealing/testing
  - Updated machine mass from 260 kg to 100 kg to match component total
  - All components now directly assembled in single step
  - Total time: ~7 hours (6 hr assembly + 1 hr seal/test)

  Placeholder recipe; BOM to be refined with actual PEM stack component data.
```

### `filler_material_station_v0`

`kb/boms/bom_filler_material_station_v0.yaml`

```yaml
id: bom_filler_material_station_v0
owner_item_id: filler_material_station_v0
components:
  - item_id: filler_wire_basic
    qty: 1
  - item_id: fastener_kit_small
    qty: 1
notes: Coarse BOM for filler material station; primarily filler consumable.
```

`kb/items/machines/filler_material_station_v0.yaml`

```yaml
id: filler_material_station_v0
kind: machine
name: Filler material station v0
mass: 15.0
unit: unit
bom: bom_filler_material_station_v0
notes: Station storing/distributing filler wire/rods for welding/brazing.
recipe: recipe_machine_filler_material_station_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_filler_material_station_v0.yaml`

```yaml
id: recipe_machine_filler_material_station_v0
target_item_id: filler_material_station_v0
variant_id: v0
inputs:
  - item_id: steel_plate_or_sheet
    qty: 11.7
    unit: kg
  - item_id: filler_wire_basic
    qty: 2.0
    unit: kg
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
outputs:
  - item_id: filler_material_station_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: steel_plate_or_sheet
        qty: 11.7
        unit: kg
      - item_id: filler_wire_basic
        qty: 2.0
        unit: kg
      - item_id: fastener_kit_small
        qty: 1.0
        unit: unit
    outputs:
      - item_id: assembled_equipment
        qty: 15.0
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
    notes: "Assemble filler material storage racks and dispensing mechanisms from BOM components"
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 15.0
        unit: kg
    outputs:
      - item_id: filler_material_station_v0
        qty: 1.0
        unit: unit
    est_time_hr: 0.25
    labor_hours: 0.25
    notes: "Verify storage capacity and accessibility of filler materials"
assumptions: Station for organizing and dispensing welding/brazing filler materials. Built from BOM components.
notes: Filler material storage and dispensing station. Keeps filler wire and rods organized for welding operations.
```

### `hot_wire_cutter_v0`

`kb/boms/bom_hot_wire_cutter_v0.yaml`

```yaml
id: bom_hot_wire_cutter_v0
owner_item_id: hot_wire_cutter_v0
components:
  - item_id: hot_wire_cutter_frame
    qty: 1
  - item_id: hot_wire_power_supply
    qty: 1
  - item_id: hot_wire_cutting_wire
    qty: 1
  - item_id: control_compute_module_imported
    qty: 1
  - item_id: sensor_suite_general
    qty: 1
  - item_id: fastener_kit_small
    qty: 1
notes: Coarse BOM for hot wire cutter; imported compute assumed.
```

`kb/items/machines/hot_wire_cutter_v0.yaml`

```yaml
id: hot_wire_cutter_v0
kind: machine
name: Hot wire cutter v0
mass: 40.0
unit: unit
bom: bom_hot_wire_cutter_v0
notes: Hot wire cutter for foam/blocks; coarse mass estimate.
recipe: recipe_machine_hot_wire_cutter_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_hot_wire_cutter_v0.yaml`

```yaml
id: recipe_machine_hot_wire_cutter_v0
kind: recipe
target_item_id: hot_wire_cutter_v0
variant_id: v0
inputs:
  - item_id: hot_wire_cutter_frame
    qty: 1.0
    unit: unit
  - item_id: hot_wire_power_supply
    qty: 1.0
    unit: unit
  - item_id: hot_wire_cutting_wire
    qty: 1.0
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1.0
    unit: unit
  - item_id: sensor_suite_general
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
outputs:
  - item_id: hot_wire_cutter_v0
    qty: 37.3
    unit: kg
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: control_compute_module_imported
        qty: 1.0
        unit: unit
      - item_id: sensor_suite_general
        qty: 1.0
        unit: unit
    outputs:
      - item_id: control_compute_module_imported
        qty: 1.0
        unit: unit
      - item_id: sensor_suite_general
        qty: 1.0
        unit: unit
    est_time_hr: 0.25
    labor_hours: 0.25
  - process_id: assembly_basic_v0
    inputs:
      - item_id: hot_wire_cutter_frame
        qty: 1.0
        unit: unit
      - item_id: hot_wire_power_supply
        qty: 1.0
        unit: unit
      - item_id: hot_wire_cutting_wire
        qty: 1.0
        unit: unit
      - item_id: control_compute_module_imported
        qty: 1.0
        unit: unit
      - item_id: sensor_suite_general
        qty: 1.0
        unit: unit
      - item_id: fastener_kit_small
        qty: 1.0
        unit: unit
    outputs:
      - item_id: assembled_equipment
        qty: 37.3
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 37.3
        unit: kg
    outputs:
      - item_id: hot_wire_cutter_v0
        qty: 37.3
        unit: kg
    est_time_hr: 0.25
    labor_hours: 0.25
assumptions: Assemble hot wire cutter from BOM; imported compute/sensors.
notes: Coarse route; add calibration/testing later.
```

### `hydraulic_press_small`

`kb/boms/bom_hydraulic_press_small_v0.yaml`

```yaml
id: bom_hydraulic_press_small_v0
owner_item_id: hydraulic_press_small
components:
  - item_id: press_frame_small
    qty: 1
  - item_id: press_cylinder_small
    qty: 1
  - item_id: press_platen_set_small
    qty: 1
  - item_id: hydraulic_power_unit_basic
    qty: 1
  - item_id: molding_control_unit
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
```

`kb/items/machines/hydraulic_press_small.yaml`

```yaml
id: hydraulic_press_small
kind: machine
name: Hydraulic press (small)
mass: 150
unit: unit
material_class: steel
bom: bom_hydraulic_press_small_v0
notes: DEPRECATED - Consolidated into hydraulic_press. Small hydraulic press for forming,
  stamping, and powder compaction. Includes press frame, hydraulic cylinder, pump,
  and controls. Lower tonnage than main production presses.
recipe: recipe_hydraulic_press_small_v0
unit_kind: discrete
```

`kb/recipes/recipe_hydraulic_press_small_v0.yaml`

```yaml
id: recipe_hydraulic_press_small_v0
target_item_id: hydraulic_press_small
variant_id: v0
inputs:
  - item_id: steel_stock
    qty: 180.0
    unit: kg
  - item_id: filler_wire_basic
    qty: 5.0
    unit: kg
  - item_id: press_cylinder_small
    qty: 1.0
    unit: unit
  - item_id: press_platen_set_small
    qty: 1.0
    unit: unit
  - item_id: hydraulic_power_unit_basic
    qty: 1.0
    unit: unit
  - item_id: molding_control_unit
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
outputs:
  - item_id: hydraulic_press_small
    qty: 1.0
    unit: unit
steps:
  - process_id: welded_fabrication_basic_v0
    inputs:
      - item_id: steel_stock
        qty: 180.0
        unit: kg
      - item_id: filler_wire_basic
        qty: 5.0
        unit: kg
    outputs:
      - item_id: welded_fabrications
        qty: 170.0
        unit: kg
    est_time_hr: 3.0
    machine_hours: 2.0
    labor_hours: 2.0
    notes: "Fabricate press frame and platen supports."
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: welded_fabrications
        qty: 170.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 160.0
        unit: kg
    est_time_hr: 1.5
    machine_hours: 1.5
    labor_hours: 0.5
    notes: "Machine mounting surfaces and cylinder interfaces."
  - process_id: assembly_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 160.0
        unit: kg
      - item_id: press_cylinder_small
        qty: 1.0
        unit: unit
      - item_id: press_platen_set_small
        qty: 1.0
        unit: unit
      - item_id: hydraulic_power_unit_basic
        qty: 1.0
        unit: unit
      - item_id: molding_control_unit
        qty: 1.0
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1.0
        unit: unit
    outputs:
      - item_id: hydraulic_press_small
        qty: 1.0
        unit: unit
    est_time_hr: 1.5
    labor_hours: 1.5
    notes: "Install cylinder, platens, hydraulic power unit, and controls."
assumptions: Low tonnage; uses basic hydraulic power unit; tolerances moderate.
notes: Assembly of small hydraulic press for forming/compaction tasks.
```

### `kapvik_microrover_30kg_v0`

`kb/items/machines/kapvik_microrover_30kg_v0.yaml`

```yaml
id: kapvik_microrover_30kg_v0
kind: machine
name: Kapvik microrover 30 kg
mass: 30.0
unit: unit
is_import: true
deprecated: true
upgraded_to:
  - kapvik_microrover_v0
upgrade_note: "Canonical Kapvik rover ID drops size suffix; use kapvik_microrover_v0."
upgrade_since: "2026-03-03"
notes: 'Deprecated legacy Kapvik ID retained for migration visibility only.

  Use kapvik_microrover_v0 for all active references.'
unit_kind: discrete
```

### `kiln_basic`

`kb/boms/bom_kiln_basic.yaml`

```yaml
id: bom_kiln_basic
owner_item_id: kiln_basic
target_item_id: kiln_basic
variant_id: v0
components:
  - item_id: steel_shell_thick
    qty: 300
    unit: kg
  - item_id: refractory_brick_set
    qty: 200
    unit: kg
  - item_id: heating_element_set_basic
    qty: 1
    unit: unit
  - item_id: insulation_pack_high_temp
    qty: 1
    unit: unit
  - item_id: temperature_controller_basic
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
notes: BOM for basic batch kiln.
```

`kb/items/machines/kiln_basic.yaml`

```yaml
id: kiln_basic
kind: machine
name: Basic kiln
mass: 723.9
unit: unit
material_class: steel
bom: bom_kiln_basic
notes: DEPRECATED - Consolidated into kiln_ceramic. Batch kiln for firing ceramics/refractories;
  insulated shell with heating elements or burners. Mass aligned to kiln_basic assembly inputs.
recipe: recipe_kiln_basic_v0
unit_kind: discrete
```

`kb/recipes/recipe_kiln_basic_import_v0.yaml`

```yaml
id: recipe_kiln_basic_import_v0
kind: recipe
target_item_id: kiln_basic
produces_qty: 1.0
produces_unit: unit
inputs:
  - item_id: steel_shell_thick
    qty: 300.0
    unit: kg
  - item_id: refractory_brick_set
    qty: 200.0
    unit: kg
  - item_id: heating_element_set_basic
    qty: 1
    unit: unit
  - item_id: insulation_pack_high_temp
    qty: 1
    unit: unit
  - item_id: temperature_controller_basic
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 50.0
    unit: kg
  - item_id: welding_rod_steel
    qty: 26.0
    unit: kg
outputs:
  - item_id: kiln_basic
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: steel_shell_thick
        qty: 300.0
        unit: kg
      - item_id: refractory_brick_set
        qty: 200.0
        unit: kg
      - item_id: heating_element_set_basic
        qty: 1
        unit: unit
      - item_id: insulation_pack_high_temp
        qty: 1
        unit: unit
      - item_id: temperature_controller_basic
        qty: 1
        unit: unit
      - item_id: power_conditioning_module
        qty: 1
        unit: unit
      - item_id: fastener_kit_medium
        qty: 50.0
        unit: kg
      - item_id: welding_rod_steel
        qty: 26.0
        unit: kg
    outputs:
      - item_id: kiln_basic
        qty: 1
        unit: unit
    est_time_hr: 27.0
    machine_hours: 16.0
    labor_hours: 11.0
    notes: "Form steel shell, install refractory lining, install heating elements, assemble insulation and controls, calibrate temperature controller"
assumptions: "Replaced placeholder import path with concrete kiln construction steps."
notes: "Concrete production path to replace import placeholder for kiln_basic."
```

`kb/recipes/recipe_kiln_basic_v0.yaml`

```yaml
id: recipe_kiln_basic_v0
kind: recipe
target_item_id: kiln_basic
inputs:
  - item_id: steel_sheet_3mm
    qty: 310.0
    unit: kg
  - item_id: furnace_chamber_unequipped
    qty: 0.4166
    unit: unit
    notes: "Intermediate for heating element installation"
  - item_id: refractory_brick_set
    qty: 200
    unit: kg
  - item_id: heating_element_set_basic
    qty: 1
    unit: unit
  - item_id: insulation_pack_high_temp
    qty: 1
    unit: unit
  - item_id: temperature_controller_basic
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
outputs:
  - item_id: kiln_basic
    qty: 1.0
    unit: unit
steps:
  - process_id: steel_shell_thick_forming_v0
    inputs:
      - item_id: steel_sheet_3mm
        qty: 310.0
        unit: kg
    outputs:
      - item_id: steel_shell_thick
        qty: 300.0
        unit: kg
    est_time_hr: 6.0
    machine_hours: 4.0
    labor_hours: 2.0
    notes: "Form thick steel shell for basic kiln"
  - process_id: refractory_lining_installation_v0
    inputs:
      - item_id: steel_shell_thick
        qty: 300.0
        unit: kg
      - item_id: refractory_brick_set
        qty: 200
        unit: kg
    outputs:
      - item_id: furnace_chamber_unequipped
        qty: 0.4166
        unit: unit
    est_time_hr: 12.0
    machine_hours: 8.0
    labor_hours: 4.0
    notes: "Install refractory brick lining"
  - process_id: heating_element_installation_v0
    inputs:
      - item_id: furnace_chamber_unequipped
        qty: 0.4166
        unit: unit
      - item_id: heating_element_set_basic
        qty: 1
        unit: unit
    outputs:
      - item_id: furnace_chamber_equipped
        qty: 1
        unit: unit
    est_time_hr: 3.0
    machine_hours: 1.0
    labor_hours: 2.0
    notes: "Install heating element set_basic"
  - process_id: assembly_basic_v0
    inputs:
      - item_id: furnace_chamber_equipped
        qty: 1
        unit: unit
      - item_id: insulation_pack_high_temp
        qty: 1
        unit: unit
      - item_id: temperature_controller_basic
        qty: 1
        unit: unit
      - item_id: power_conditioning_module
        qty: 1
        unit: unit
    outputs:
      - item_id: kiln_basic
        qty: 1
        unit: unit
    est_time_hr: 6.0
    machine_hours: 3.0
    labor_hours: 3.0
    notes: "Assemble insulation pack, temperature controller, and power conditioning module. Calibrate temperature controller and sensors, verify heating uniformity and control accuracy."
assumptions: "Local fabrication path for basic kiln; uses steel_shell_thick, refractory lining, heating elements, insulation, temperature control, and power conditioning modules."
notes: |
  Concrete production path to replace import placeholder for kiln_basic.
  Builds a basic kiln from steel shell, refractory lining, heating elements, insulation, and control systems.
```

### `labor_bot_basic_v0`

`kb/boms/bom_labor_bot_basic_v0.yaml`

```yaml
id: bom_labor_bot_basic_v0
kind: bom
owner_item_id: labor_bot_basic_v0
components:
  - item_id: machine_frame_small
    qty: 1
    notes: "Base frame for lightweight labor bot."
  - item_id: robot_arm_link_aluminum
    qty: 2
    notes: "Upper arm and forearm links."
  - item_id: robot_wrist_3axis
    qty: 1
    notes: "Basic 3-axis wrist module."
  - item_id: motor_electric_small
    qty: 4
    notes: "Small motors for joints and wrist."
  - item_id: harmonic_drive_reducer_medium
    qty: 4
    notes: "Gear reducers for joint actuation."
  - item_id: power_distribution_board
    qty: 1
    notes: "Power distribution for control electronics."
  - item_id: computer_core_imported
    qty: 1
    notes: "Embedded controller for basic motion and coordination."
  - item_id: sensor_suite_general
    qty: 1
    notes: "Basic sensing package."
  - item_id: led_ring_light
    qty: 1
    notes: "Illumination for inspection tasks."
  - item_id: electric_parallel_gripper
    qty: 1
    notes: "Simple end effector for handling parts."
  - item_id: assembled_cable_harness
    qty: 3
    notes: "Motor and signal cabling."
  - item_id: cable_drag_chain
    qty: 1
    notes: "Cable routing chain."
  - item_id: protective_cover_set
    qty: 1
    notes: "Safety covers for moving components."
notes: "Placeholder BOM; to be refined as design progresses."
```

`kb/items/machines/labor_bot_basic_v0.yaml`

```yaml
id: labor_bot_basic_v0
kind: machine
name: Basic labor bot v0
mass: 120.0
unit: unit
bom: bom_labor_bot_basic_v0
notes: Basic humanoid labor bot for simple tasks; serves as a lightweight worker.
recipe: recipe_labor_bot_basic_v0
unit_kind: discrete
```

`kb/recipes/recipe_labor_bot_basic_v0.yaml`

```yaml
id: recipe_labor_bot_basic_v0
kind: recipe
name: Recipe for basic labor bot v0
target_item_id: labor_bot_basic_v0
variant_id: v0
inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: count
  - item_id: robot_arm_link_aluminum
    qty: 2
    unit: unit
  - item_id: robot_wrist_3axis
    qty: 1
    unit: unit
  - item_id: motor_electric_small
    qty: 4
    unit: unit
  - item_id: harmonic_drive_reducer_medium
    qty: 4
    unit: count
  - item_id: power_distribution_board
    qty: 1
    unit: count
  - item_id: computer_core_imported
    qty: 1
    unit: count
  - item_id: sensor_suite_general
    qty: 1
    unit: count
  - item_id: led_ring_light
    qty: 1
    unit: count
  - item_id: electric_parallel_gripper
    qty: 1
    unit: unit
  - item_id: assembled_cable_harness
    qty: 3
    unit: count
  - item_id: cable_drag_chain
    qty: 1
    unit: count
  - item_id: protective_cover_set
    qty: 1
    unit: count
outputs:
  - item_id: labor_bot_basic_v0
    qty: 1
    unit: count
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: machine_frame_small
        qty: 1
        unit: count
      - item_id: robot_arm_link_aluminum
        qty: 2
        unit: unit
      - item_id: robot_wrist_3axis
        qty: 1
        unit: unit
      - item_id: motor_electric_small
        qty: 4
        unit: unit
      - item_id: harmonic_drive_reducer_medium
        qty: 4
        unit: count
      - item_id: power_distribution_board
        qty: 1
        unit: count
      - item_id: computer_core_imported
        qty: 1
        unit: count
      - item_id: sensor_suite_general
        qty: 1
        unit: count
      - item_id: led_ring_light
        qty: 1
        unit: count
      - item_id: electric_parallel_gripper
        qty: 1
        unit: unit
      - item_id: assembled_cable_harness
        qty: 3
        unit: count
      - item_id: cable_drag_chain
        qty: 1
        unit: count
      - item_id: protective_cover_set
        qty: 1
        unit: count
    outputs:
      - item_id: labor_bot_basic_v0
        qty: 1
        unit: count
    est_time_hr: 1.5
    labor_hours: 1.5
assumptions: "Assemble per BOM; parts produced via BOM; imported compute treated as part."
notes: "Basic labor bot assembly path; refined to include explicit BOM inputs."
```

### `labor_bot_specialist_v0`

`kb/boms/bom_labor_bot_specialist_v0.yaml`

```yaml
id: bom_labor_bot_specialist_v0
owner_item_id: labor_bot_specialist_v0
components:
  - item_id: support_frame_welded
    qty: 1
  - item_id: drive_motor_medium
    qty: 1
  - item_id: bearing_set_heavy
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
  - item_id: power_conditioning_module
    qty: 1
  - item_id: control_compute_module_imported
    qty: 1
notes: Placeholder BOM for specialist labor bot.
```

`kb/items/machines/labor_bot_specialist_v0.yaml`

```yaml
id: labor_bot_specialist_v0
kind: machine
name: Specialist labor bot v0
mass: 180.0
unit: unit
bom: bom_labor_bot_specialist_v0
recipe_id: recipe_machine_labor_bot_specialist_v0
notes: Specialist labor bot for high-skill programming, debugging, and domain-specific
  tasks.
recipe: recipe_machine_labor_bot_specialist_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_labor_bot_specialist_v0.yaml`

```yaml
id: recipe_machine_labor_bot_specialist_v0
target_item_id: labor_bot_specialist_v0
variant_id: v0
inputs:
  - item_id: support_frame_welded
    qty: 1
    unit: unit
  - item_id: drive_motor_medium
    qty: 1
    unit: unit
  - item_id: bearing_set_heavy
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1
    unit: unit
outputs:
  - item_id: labor_bot_specialist_v0
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: support_frame_welded
        qty: 1
        unit: unit
      - item_id: drive_motor_medium
        qty: 1
        unit: unit
      - item_id: bearing_set_heavy
        qty: 1
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1
        unit: unit
      - item_id: power_conditioning_module
        qty: 1
        unit: unit
      - item_id: control_compute_module_imported
        qty: 1
        unit: unit
    outputs:
      - item_id: labor_bot_specialist_v0
        qty: 1
        unit: unit
    est_time_hr: 3.0
    labor_hours: 3.0
    notes: "Assemble specialist labor bot from frame, motors, bearings, fasteners, power module, and control module"
assumptions: Assemble specialist bot; base assembly route similar to labor_bot_general_v0.
notes: Basic assembly route for specialist bot.
```

### `power_conditioner`

`kb/boms/bom_power_conditioner_v0.yaml`

```yaml
id: bom_power_conditioner_v0
owner_item_id: power_conditioner
components:
  - item_id: transformer_step_down_high_current
    qty: 1
  - item_id: capacitor_bank_power
    qty: 1
  - item_id: inductor_filter_large
    qty: 3
  - item_id: enclosure_electrical_medium
    qty: 1
notes: Power conditioning circuitry.
```

`kb/items/machines/power_conditioner_unit.yaml`

```yaml
id: power_conditioner
kind: machine
name: Power Conditioning Unit
mass: 100.0
mass_kg: 100.0
unit: unit
bom: bom_power_conditioner_v0
recipe: recipe_machine_power_conditioner_v0
notes: Power conditioning and filtering equipment for clean electrical supply.
unit_kind: discrete
```

`kb/recipes/recipe_machine_power_conditioner_v0.yaml`

```yaml
id: recipe_machine_power_conditioner_v0
kind: recipe
target_item_id: power_conditioner
variant_id: v0
inputs:
  - item_id: transformer_step_down_high_current
    qty: 80.0
    unit: kg
  - item_id: capacitor_bank_power
    qty: 10.0
    unit: kg
  - item_id: inductor_filter_large
    qty: 6.0
    unit: kg
  - item_id: enclosure_electrical_medium
    qty: 4.0
    unit: kg
outputs:
  - item_id: power_conditioner
    qty: 100.0
    unit: kg
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: transformer_step_down_high_current
        qty: 80.0
        unit: kg
      - item_id: capacitor_bank_power
        qty: 10.0
        unit: kg
      - item_id: inductor_filter_large
        qty: 6.0
        unit: kg
      - item_id: enclosure_electrical_medium
        qty: 4.0
        unit: kg
    outputs:
      - item_id: power_conditioner
        qty: 100.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: "Assemble and test power conditioner from BOM components (100 kg total)"
notes: "Assemble power conditioner from BOM components; placeholder assembly recipe."
```

### `power_hammer_or_press_v0`

`kb/boms/bom_power_hammer_or_press_v0.yaml`

```yaml
id: bom_power_hammer_or_press_v0
owner_item_id: power_hammer_or_press_v0
components:
  - item_id: hammer_frame_basic
    qty: 120
    unit: kg
  - item_id: hammer_head_basic
    qty: 40
    unit: kg
  - item_id: hammer_drive_motor
    qty: 1
    unit: unit
  - item_id: anvil_block_basic
    qty: 1
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
notes: Coarse BOM for power hammer/press; imported compute/sensors assumed.
```

`kb/items/machines/power_hammer_or_press_v0.yaml`

```yaml
id: power_hammer_or_press_v0
kind: machine
name: Power hammer or press v0
mass: 290.0
unit: unit
bom: bom_power_hammer_or_press_v0
notes: 'DEPRECATED - Consolidated into hydraulic_press. Small power hammer/press for
  forming tasks.


  Mass updated 2026-01 from 200 kg to 290 kg based on BOM component analysis:

  - Frame: 120 kg

  - Hammer head: 40 kg

  - Drive motor: 30 kg

  - Anvil block: 80 kg

  - Controls/sensors/electronics: ~20 kg

  Total: 290 kg

  '
recipe: recipe_machine_power_hammer_or_press_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_power_hammer_or_press_v0.yaml`

```yaml
id: recipe_machine_power_hammer_or_press_v0
target_item_id: power_hammer_or_press_v0
variant_id: v0
produces_qty: 1
produces_unit: unit
inputs:
  - item_id: hammer_frame_basic
    qty: 1
    unit: unit
  - item_id: hammer_head_basic
    qty: 1
    unit: unit
  - item_id: hammer_drive_motor
    qty: 1
    unit: unit
  - item_id: anvil_block_basic
    qty: 1
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
outputs:
  - item_id: power_hammer_or_press_v0
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: hammer_frame_basic
        qty: 1
        unit: unit
      - item_id: hammer_head_basic
        qty: 1
        unit: unit
      - item_id: hammer_drive_motor
        qty: 1
        unit: unit
      - item_id: anvil_block_basic
        qty: 1
        unit: unit
      - item_id: control_compute_module_imported
        qty: 1
        unit: unit
      - item_id: sensor_suite_general
        qty: 1
        unit: unit
      - item_id: power_conditioning_module
        qty: 1
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1
        unit: unit
    outputs:
      - item_id: power_hammer_or_press_v0
        qty: 1
        unit: unit
    est_time_hr: 4.0
    labor_hours: 4.0
    notes: "Assemble frame, mount anvil, install hammer head and drive motor, integrate controls and sensors. Major components: 120 kg frame + 40 kg head + 30 kg motor + 80 kg anvil + electronics ≈ 280 kg total. Testing and calibration included in assembly time."
assumptions: Assemble hammer/press per BOM; imported compute/sensors.
notes: |
  Recipe corrected 2026-01 to fix mass balance errors:
  - Removed unused bulk_material_or_parts import step
  - Changed all component specifications from kg to unit counts
  - Updated machine mass from 200 kg to 290 kg to match component total
  - Removed inspection step to eliminate circular dependency (testing included in assembly)
  - Simplified to 1 step: assembly with integrated testing
  - Total time: ~4 hours

  Note: Item marked DEPRECATED - consolidated into hydraulic_press.
```

### `power_supply_high_voltage`

`kb/boms/bom_power_supply_high_voltage_v0.yaml`

```yaml
id: bom_power_supply_high_voltage_v0
owner_item_id: power_supply_high_voltage
components:
  - item_id: high_voltage_transformer
    qty: 1
  - item_id: hv_rectifier_stack
    qty: 1
  - item_id: power_electronics_module
    qty: 1
  - item_id: hv_enclosure_and_interlocks
    qty: 1
  - item_id: control_circuit_board_power
    qty: 1
  - item_id: cooling_fan_and_ducting
    qty: 1
  - item_id: power_output_terminals
    qty: 1
  - item_id: fastener_kit_small
    qty: 1
```

`kb/items/machines/power_supply_high_voltage.yaml`

```yaml
id: power_supply_high_voltage
kind: machine
name: Power supply (high voltage)
mass: 60.0
unit: unit
bom: bom_power_supply_high_voltage_v0
material_class: electronic
notes: High-voltage power supply for testing and specialized equipment; adjustable
  output with current limiting and safety interlocks.
recipe: recipe_power_supply_high_voltage_v0
unit_kind: discrete
```

`kb/recipes/recipe_power_supply_high_voltage_v0.yaml`

```yaml
id: recipe_power_supply_high_voltage_v0
target_item_id: power_supply_high_voltage
variant_id: v0
inputs:
  - item_id: enclosure_electrical_medium
    qty: 12.0
    unit: kg
  - item_id: control_circuit_board_basic
    qty: 2.0
    unit: kg
  - item_id: relay_electromagnetic_v0
    qty: 2.0
    unit: kg
  - item_id: control_components
    qty: 3.0
    unit: kg
  - item_id: assembled_wire_harness
    qty: 3.0
    unit: kg
  - item_id: terminal_block_set
    qty: 2.0
    unit: kg
  - item_id: fastener_kit_small
    qty: 0.5
    unit: kg
  - item_id: din_rail_steel
    qty: 0.5
    unit: kg
  - item_id: sheet_metal_or_structural_steel
    qty: 35.0
    unit: kg
outputs:
  - item_id: power_supply_high_voltage
    qty: 60.0
    unit: kg
steps:
  - process_id: control_panel_assembly_v0
    inputs:
      - item_id: enclosure_electrical_medium
        qty: 12.0
        unit: kg
      - item_id: control_circuit_board_basic
        qty: 2.0
        unit: kg
      - item_id: relay_electromagnetic_v0
        qty: 2.0
        unit: kg
      - item_id: control_components
        qty: 3.0
        unit: kg
      - item_id: assembled_wire_harness
        qty: 3.0
        unit: kg
      - item_id: terminal_block_set
        qty: 2.0
        unit: kg
      - item_id: fastener_kit_small
        qty: 0.5
        unit: kg
      - item_id: din_rail_steel
        qty: 0.5
        unit: kg
      - item_id: sheet_metal_or_structural_steel
        qty: 35.0
        unit: kg
    outputs:
      - item_id: control_panel_assembly_v0
        qty: 60.0
        unit: kg
    est_time_hr: 1.5
    labor_hours: 1.5
    notes: "Assemble enclosure, mount transformer, rectifier, and cooling."
  - process_id: electrical_assembly_basic_v0
    inputs:
      - item_id: control_panel_assembly_v0
        qty: 60.0
        unit: kg
    outputs:
      - item_id: control_panel_assembly_v0
        qty: 60.0
        unit: kg
    est_time_hr: 1.5
    labor_hours: 1.5
    notes: "Wire HV circuits, controls, and safety interlocks."
  - process_id: integration_test_basic_v0
    inputs:
      - item_id: control_panel_assembly_v0
        qty: 60.0
        unit: kg
    outputs:
      - item_id: power_supply_high_voltage
        qty: 60.0
        unit: kg
    est_time_hr: 0.7
    labor_hours: 0.7
    notes: "Bench test HV output, regulation, and interlock functionality."
assumptions: HV components partly imported; safety interlocks essential.
notes: Assembly of adjustable high-voltage power supply.
```

### `precision_stage`

`kb/boms/bom_precision_stage_v0.yaml`

```yaml
id: bom_precision_stage_v0
owner_item_id: precision_stage
components:
  - item_id: linear_guide_rails
    qty: 3
  - item_id: stepper_motor_precision
    qty: 3
  - item_id: ball_screw_assembly
    qty: 3
  - item_id: metal_sheet_or_plate
    qty: 2.0
    unit: kg
    notes: Aluminum mounting plate (material_class metal allows aluminum)
notes: Precision positioning stage components.
```

`kb/items/machines/precision_positioning_stage.yaml`

```yaml
id: precision_stage
kind: machine
name: Precision Positioning Stage
mass: 75.0
unit: unit
bom: bom_precision_stage_v0
notes: Precision XYZ positioning stage for accurate part placement and measurement.
recipe: recipe_precision_stage_v0
unit_kind: discrete
```

`kb/recipes/recipe_precision_stage_v0.yaml`

```yaml
id: recipe_precision_stage_v0
target_item_id: precision_stage
variant_id: v0
inputs:
  - item_id: machined_part_raw
    qty: 75.0
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 2.0
    unit: kg
  - item_id: electronic_components_set
    qty: 1.0
    unit: kg
steps:
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 75.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 75.0
        unit: kg
    est_time_hr: 16.0
    machine_hours: 16.0
    notes: "Machine precision linear guides and mounting surfaces"
  - process_id: assembly_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 75.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 74.0
        unit: kg
    est_time_hr: 12.0
    labor_hours: 12.0
    notes: "Assemble XYZ stages, ball screws, and linear bearings"
  - process_id: wiring_and_electronics_integration_v0
    inputs:
      - item_id: electrical_wire_and_connectors
        qty: 2.0
        unit: kg
      - item_id: electronic_components_set
        qty: 1.0
        unit: kg
    outputs:
      - item_id: assembled_electronics
        qty: 1.0
        unit: kg
    est_time_hr: 8.0
    labor_hours: 8.0
    notes: "Install stepper motors, encoders, and control electronics"
  - process_id: calibration_and_test_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 74.0
        unit: kg
      - item_id: assembled_electronics
        qty: 1.0
        unit: kg
    outputs:
      - item_id: precision_stage
        qty: 75.0
        unit: kg
    est_time_hr: 6.0
    labor_hours: 6.0
    notes: "Calibrate positioning accuracy and repeatability"
assumptions: |
  Precision XYZ positioning stage assembly.
  Ball screws and linear guides for micron-level positioning.
  Total mass ~75 kg.
notes: |
  Manufacturing recipe for precision positioning stage.
  Used for accurate part placement, measurement, and inspection.
  Total assembly time ~42 hours.
```

### `press_brake_or_roller`

`kb/boms/bom_press_brake_or_roller_v0.yaml`

```yaml
id: bom_press_brake_or_roller_v0
owner_item_id: press_brake_or_roller
target_item_id: press_brake_or_roller
variant_id: v0
components:
  - item_id: machine_frame_heavy
    qty: 1
    unit: unit
    notes: "Heavy steel frame for bending operations (~150 kg)"
  - item_id: hydraulic_cylinder_industrial
    qty: 2
    unit: unit
    notes: "Hydraulic cylinders for bending force (~30 kg each)"
  - item_id: press_brake_die_set
    qty: 1
    unit: unit
    notes: "Interchangeable dies for different bend angles (~40 kg)"
  - item_id: hydraulic_pump_basic
    qty: 1
    unit: unit
    notes: "Hydraulic pump for press operation (~30 kg)"
  - item_id: linear_guide_rails
    qty: 1
    unit: unit
    notes: "Linear guides for precise bending motion (~20 kg)"
  - item_id: control_panel_basic
    qty: 1
    unit: unit
    notes: "Controls for angle and depth adjustment (~20 kg)"
notes: Press brake for precision sheet metal bending. Total mass ~300 kg including frame, hydraulics, dies, and controls.
```

`kb/items/machines/press_brake_or_roller.yaml`

```yaml
id: press_brake_or_roller
kind: machine
name: Press brake or roller
mass: 300.0
unit: unit
bom: bom_press_brake_or_roller_v0
notes: DEPRECATED - Consolidated into press_brake. Press brake for bending sheet metal
  or roller for forming curved sections. Hydraulic or mechanical operation for precise
  angle bending and forming operations.
alternatives:
- plate_rolling_mill
- press_brake
dedupe_candidate: true
recipe: recipe_machine_press_brake_or_roller_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_press_brake_or_roller_v0.yaml`

```yaml
id: recipe_machine_press_brake_or_roller_v0
target_item_id: press_brake_or_roller
variant_id: v0
inputs:
  - item_id: steel_plate_or_sheet
    qty: 250.0
    unit: kg
  - item_id: steel_stock
    qty: 80.0
    unit: kg
  - item_id: filler_wire_basic
    qty: 5.0
    unit: kg
  - item_id: hydraulic_control_valve_set
    qty: 1.0
    unit: kg
  - item_id: piping_components
    qty: 1.0
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 2.0
    unit: kg
  - item_id: electronic_components_set
    qty: 1.0
    unit: kg
outputs:
  - item_id: press_brake_or_roller
    qty: 1.0
    unit: unit
steps:
  - process_id: cutting_basic_v0
    inputs:
      - item_id: steel_plate_or_sheet
        qty: 250.0
        unit: kg
    outputs:
      - item_id: cut_parts
        qty: 250.0
        unit: kg
    est_time_hr: 1.5
    machine_hours: 1.5
    labor_hours: 0.7
    notes: "Cut frame plates, gussets, and tooling mounts."
  - process_id: welded_fabrication_basic_v0
    inputs:
      - item_id: steel_stock
        qty: 80.0
        unit: kg
      - item_id: filler_wire_basic
        qty: 5.0
        unit: kg
      - item_id: cut_parts
        qty: 250.0
        unit: kg
    outputs:
      - item_id: welded_fabrications
        qty: 330.0
        unit: kg
    est_time_hr: 2.5
    machine_hours: 2.0
    labor_hours: 2.0
    notes: "Weld frame, beam/roller supports, and hinge hardware."
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: welded_fabrications
        qty: 330.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 320.0
        unit: kg
    est_time_hr: 1.2
    machine_hours: 1.0
    labor_hours: 0.8
    notes: "Finish tooling faces, pivot holes, and mounting surfaces."
  - process_id: hydraulic_system_assembly_v0
    est_time_hr: 1.5
    labor_hours: 1.5
    notes: "Install cylinder/actuation, hoses, valves, and power unit."
  - process_id: hydraulic_system_integration_v0
    inputs:
      - item_id: hydraulic_control_valve_set
        qty: 1.0
        unit: kg
      - item_id: piping_components
        qty: 1.0
        unit: kg
    outputs:
      - item_id: hydraulic_system_medium
        qty: 1.0
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
    notes: "Fill/bleed hydraulics and perform basic motion checks."
  - process_id: wiring_and_electronics_integration_v0
    inputs:
      - item_id: machined_part_raw
        qty: 320.0
        unit: kg
      - item_id: electrical_wire_and_connectors
        qty: 2.0
        unit: kg
      - item_id: electronic_components_set
        qty: 1.0
        unit: kg
      - item_id: hydraulic_system_medium
        qty: 1.0
        unit: kg
    outputs:
      - item_id: wired_electrical_system
        qty: 320.0
        unit: kg
    est_time_hr: 0.7
    labor_hours: 0.7
    notes: "Wire controls, safety interlocks, and limit switches."
  - process_id: integration_test_basic_v0
    inputs:
      - item_id: wired_electrical_system
        qty: 320.0
        unit: kg
    outputs:
      - item_id: press_brake_or_roller
        qty: 1.0
        unit: unit
    est_time_hr: 0.6
    labor_hours: 0.5
    notes: "Cycle press brake/roller, verify angles/roll radius and safety stops."
assumptions: "Coarse build for small press brake or plate roller; hydraulics and controls are basic."
notes: Local assembly recipe for press brake/roller.
```

### `press_hydraulic`

`kb/boms/bom_press_hydraulic_v0.yaml`

```yaml
id: bom_press_hydraulic_v0
owner_item_id: press_hydraulic
components:
  - item_id: press_frame_light
    qty: 1
  - item_id: hydraulic_cylinder_press
    qty: 1
  - item_id: hydraulic_system_medium
    qty: 1
  - item_id: press_platen_set
    qty: 1
  - item_id: power_conditioning_module
    qty: 1
  - item_id: control_compute_module_imported
    qty: 1
  - item_id: sensor_suite_general
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
notes: Coarse BOM for light/medium press; imported compute/sensors assumed.
```

`kb/items/machines/press_hydraulic.yaml`

```yaml
id: press_hydraulic
kind: machine
name: Hydraulic press (light/medium)
mass: 250.0
unit: unit
bom: bom_press_hydraulic_v0
notes: DEPRECATED - Consolidated into hydraulic_press. Light/medium hydraulic press
  for assembly press fits and light forming; capacity scoped to early self-replication
  (not 50-100 tons).
recipe: recipe_machine_press_hydraulic_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_press_hydraulic_v0.yaml`

```yaml
id: recipe_machine_press_hydraulic_v0
target_item_id: press_hydraulic
variant_id: v0
inputs:
  - item_id: press_frame_light
    qty: 1
    unit: unit
  - item_id: hydraulic_cylinder_press
    qty: 1
    unit: unit
  - item_id: hydraulic_system_medium
    qty: 1
    unit: unit
  - item_id: press_platen_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: press_frame_light
        qty: 1
        unit: unit
      - item_id: hydraulic_cylinder_press
        qty: 1
        unit: unit
      - item_id: hydraulic_system_medium
        qty: 1
        unit: unit
      - item_id: press_platen_set
        qty: 1
        unit: unit
      - item_id: power_conditioning_module
        qty: 1
        unit: unit
      - item_id: control_compute_module_imported
        qty: 1
        unit: unit
      - item_id: sensor_suite_general
        qty: 1
        unit: unit
      - item_id: fastener_kit_medium
        qty: 1
        unit: unit
    outputs:
      - item_id: assembled_equipment
        qty: 250.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: "Assemble hydraulic press from BOM components"
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 250.0
        unit: kg
    outputs:
      - item_id: press_hydraulic
        qty: 1
        unit: unit
    est_time_hr: 0.5
    labor_hours: 0.5
    notes: "Inspect and test hydraulic press"
assumptions: Assemble light/medium press per BOM; imported compute/sensors.
notes: |
  Assumptions:
  - Use assembled_equipment as intermediate to avoid self-reference in inspection.
  Rationale:
  - Breaks circular dependency while preserving assembly + inspection flow.
```

`kb/recipes/recipe_press_hydraulic_v0.yaml`

```yaml
id: recipe_press_hydraulic_v0
kind: recipe
name: Recipe for hydraulic press
produces_id: press_hydraulic
produces_qty: 1.0
produces_unit: unit
inputs:
  - item_id: regolith_metal_crude
    qty: 260.0
    unit: kg
  - item_id: hydraulic_control_valve_set
    qty: 1.0
    unit: kg
  - item_id: piping_components
    qty: 1.0
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 2.0
    unit: kg
  - item_id: electronic_components_set
    qty: 1.0
    unit: kg
outputs:
  - item_id: press_hydraulic
    qty: 1.0
    unit: unit
steps:
- process_id: metal_casting_basic_v0
  inputs:
    - item_id: regolith_metal_crude
      qty: 260.0
      unit: kg
  outputs:
    - item_id: cast_metal_parts
      qty: 247.0
      unit: kg
  notes: Cast frame, columns, and base (approx 600 kg)
- process_id: welding_brazing_basic_v0
  inputs:
    - item_id: cast_metal_parts
      qty: 247.0
      unit: kg
  outputs:
    - item_id: welded_assemblies
      qty: 247.0
      unit: kg
  notes: Weld hydraulic cylinder mounting, reinforcement gussets
- process_id: machining_finish_basic_v0
  inputs:
    - item_id: welded_assemblies
      qty: 247.0
      unit: kg
  outputs:
    - item_id: machined_part_raw
      qty: 247.0
      unit: kg
  notes: Machine ram guides, platen surfaces, cylinder mounting bores
- process_id: assembly_basic_v0
  inputs:
    - item_id: machined_part_raw
      qty: 247.0
      unit: kg
  outputs:
    - item_id: assembled_equipment
      qty: 247.0
      unit: kg
  notes: Assemble hydraulic cylinders, rams, platens, pressure gauges
- process_id: hydraulic_system_integration_v0
  inputs:
    - item_id: hydraulic_control_valve_set
      qty: 1.0
      unit: kg
    - item_id: piping_components
      qty: 1.0
      unit: kg
  outputs:
    - item_id: hydraulic_system_medium
      qty: 1.0
      unit: kg
  notes: Install hydraulic pump, valves, hoses, and pressure controls
- process_id: wiring_and_electronics_integration_v0
  inputs:
    - item_id: assembled_equipment
      qty: 247.0
      unit: kg
    - item_id: hydraulic_system_medium
      qty: 1.0
      unit: kg
    - item_id: electrical_wire_and_connectors
      qty: 2.0
      unit: kg
    - item_id: electronic_components_set
      qty: 1.0
      unit: kg
  outputs:
    - item_id: press_hydraulic
      qty: 1.0
      unit: unit
  byproducts:
    - item_id: assembly_waste
      qty: 1.0
      unit: kg
  notes: Install electrical controls, safety interlocks, pressure sensors
notes: Multi-purpose hydraulic press for bearing installation, forming, and press fit operations.
target_item_id: press_hydraulic
```

`kb/recipes/recipe_press_hydraulic_v1.yaml`

```yaml
id: recipe_press_hydraulic_v1
kind: recipe
name: Recipe for hydraulic press v1
produces_id: press_hydraulic
produces_qty: 1.0
produces_unit: unit
inputs:
  - item_id: regolith_metal_crude
    qty: 260.0
    unit: kg
  - item_id: hydraulic_control_valve_set
    qty: 1.0
    unit: kg
  - item_id: piping_components
    qty: 1.0
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 2.0
    unit: kg
  - item_id: electronic_components_set
    qty: 1.0
    unit: kg
outputs:
  - item_id: press_hydraulic
    qty: 1.0
    unit: unit
steps:
- process_id: metal_casting_basic_v0
  inputs:
    - item_id: regolith_metal_crude
      qty: 260.0
      unit: kg
  outputs:
    - item_id: cast_metal_parts
      qty: 247.0
      unit: kg
  notes: Cast frame, columns, and base (approx 600 kg)
- process_id: welding_brazing_basic_v0
  inputs:
    - item_id: cast_metal_parts
      qty: 247.0
      unit: kg
  outputs:
    - item_id: welded_assemblies
      qty: 247.0
      unit: kg
  notes: Weld hydraulic cylinder mounting, reinforcement gussets
- process_id: machining_finish_basic_v0
  inputs:
    - item_id: welded_assemblies
      qty: 247.0
      unit: kg
  outputs:
    - item_id: machined_part_raw
      qty: 247.0
      unit: kg
  notes: Machine ram guides, platen surfaces, cylinder mounting bores
- process_id: assembly_basic_v0
  inputs:
    - item_id: machined_part_raw
      qty: 247.0
      unit: kg
  outputs:
    - item_id: assembled_equipment
      qty: 247.0
      unit: kg
  notes: Assemble hydraulic cylinders, rams, platens, pressure gauges
- process_id: hydraulic_system_integration_v0
  inputs:
    - item_id: hydraulic_control_valve_set
      qty: 1.0
      unit: kg
    - item_id: piping_components
      qty: 1.0
      unit: kg
  outputs:
    - item_id: hydraulic_system_medium
      qty: 1.0
      unit: kg
  notes: Install hydraulic pump, valves, hoses, and pressure controls
- process_id: wiring_and_electronics_integration_v0
  inputs:
    - item_id: assembled_equipment
      qty: 247.0
      unit: kg
    - item_id: hydraulic_system_medium
      qty: 1.0
      unit: kg
    - item_id: electrical_wire_and_connectors
      qty: 2.0
      unit: kg
    - item_id: electronic_components_set
      qty: 1.0
      unit: kg
  outputs:
    - item_id: press_hydraulic
      qty: 1.0
      unit: unit
  notes: Install electrical controls, safety interlocks, pressure sensors
notes: Alternative production route for hydraulic press; provides explicit path for indexer.
target_item_id: press_hydraulic
```

### `pressure_test_rig_basic_v0`

`kb/boms/bom_pressure_test_rig_basic_v0.yaml`

```yaml
id: bom_pressure_test_rig_basic_v0
owner_item_id: pressure_test_rig_basic_v0
components:
  - item_id: hydraulic_pump_high_pressure
    qty: 1.0
    unit: each
    notes: "High-pressure hydraulic pump"
  - item_id: pressure_vessel_steel
    qty: 1.0
    unit: each
    notes: "Pressure vessel (steel)"
  - item_id: press_platen_steel
    qty: 1.0
    unit: each
  - item_id: brick_mold_steel_set
    qty: 1.0
    unit: each
    notes: "Brick mold set for test rig"
  - item_id: hydraulic_hoses_and_fittings
    qty: 1.0
    unit: each
  - item_id: pressure_gauge_set
    qty: 1.0
    unit: each
  - item_id: control_panel_basic
    qty: 1.0
    unit: each
  - item_id: electric_motor_3_phase_5kw
    qty: 1.0
    unit: each
  - item_id: steel_frame_heavy_duty
    qty: 1.0
    unit: each
  - item_id: hydraulic_cylinder_large
    qty: 1.0
    unit: each
  - item_id: pressure_control_valve_set
    qty: 1.0
    unit: each
notes: "Seed BOM for pressure_test_rig_basic; composed from available KB parts. Assumes all components are present; refine mass flow later."
```

`kb/items/machines/pressure_test_rig_basic_v0.yaml`

```yaml
id: pressure_test_rig_basic_v0
name: Pressure test rig (basic) v0
kind: machine
mass: 600.0
mass_kg: 600.0
unit: unit
bom: bom_pressure_test_rig_basic_v0
notes: Seed variant for the pressure test rig; mass and BOM are placeholders for initial
  modeling.
recipe: recipe_pressure_test_rig_basic_v0
unit_kind: discrete
```

`kb/recipes/recipe_pressure_test_rig_basic_v0.yaml`

```yaml
id: recipe_pressure_test_rig_basic_v0
kind: recipe
target_item_id: pressure_test_rig_basic_v0
variant_id: v0
inputs:
  - item_id: hydraulic_pump_high_pressure
    qty: 60.0
    unit: kg
  - item_id: pressure_vessel_steel
    qty: 150.0
    unit: kg
  - item_id: press_platen_steel
    qty: 200.0
    unit: kg
  - item_id: brick_mold_steel_set
    qty: 100.0
    unit: kg
  - item_id: hydraulic_hoses_and_fittings
    qty: 8.0
    unit: kg
  - item_id: pressure_gauge_set
    qty: 5.0
    unit: kg
  - item_id: control_panel_basic
    qty: 1.0
    unit: unit
  - item_id: electric_motor_3_phase_5kw
    qty: 1.0
    unit: unit
  - item_id: steel_frame_heavy_duty
    qty: 1200.0
    unit: kg
  - item_id: hydraulic_cylinder_large
    qty: 40.0
    unit: kg
  - item_id: pressure_control_valve_set
    qty: 6.0
    unit: kg
outputs:
  - item_id: pressure_test_rig_basic_v0
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: hydraulic_pump_high_pressure
        qty: 60.0
        unit: kg
      - item_id: pressure_vessel_steel
        qty: 150.0
        unit: kg
      - item_id: press_platen_steel
        qty: 200.0
        unit: kg
      - item_id: brick_mold_steel_set
        qty: 100.0
        unit: kg
      - item_id: hydraulic_hoses_and_fittings
        qty: 8.0
        unit: kg
      - item_id: pressure_gauge_set
        qty: 5.0
        unit: kg
      - item_id: control_panel_basic
        qty: 1.0
        unit: unit
      - item_id: electric_motor_3_phase_5kw
        qty: 1.0
        unit: unit
      - item_id: steel_frame_heavy_duty
        qty: 1200.0
        unit: kg
      - item_id: hydraulic_cylinder_large
        qty: 40.0
        unit: kg
      - item_id: pressure_control_valve_set
        qty: 6.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 1774.0
        unit: kg
    notes: "Assemble components for the pressure test rig"
  - process_id: pressure_test_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 1774.0
        unit: kg
    outputs:
      - item_id: pressure_test_rig_basic_v0
        qty: 1.0
        unit: unit
    notes: "Run basic pressure test on the assembled rig"
notes: "Minimal recipe to assemble a pressure test rig and perform a basic pressure test. Will refine with a full BOM and validation later."
```

### `programming_adapter_or_jig`

`kb/boms/bom_programming_adapter_or_jig_v0.yaml`

```yaml
id: bom_programming_adapter_or_jig_v0
owner_item_id: programming_adapter_or_jig
variant_id: v0
components:
  - item_id: plastic_housing_molded
    qty: 0.3
    unit: kg
    notes: Molded body or housing for the fixture.
  - item_id: pogo_pin_set
    qty: 1
    unit: unit
    notes: Spring probes for electrical contact.
  - item_id: connector_electrical_small
    qty: 1
    unit: unit
    notes: Programming header or socket.
  - item_id: wire_copper_insulated
    qty: 0.1
    unit: kg
    notes: Internal wiring and harness.
notes: |
  Bill of materials for programming_adapter_or_jig.
  Based on recipe_programming_adapter_or_jig_v0 inputs.
```

`kb/items/parts/programming_adapter_or_jig.yaml`

```yaml
id: programming_adapter_or_jig
kind: machine
name: Programming adapter or jig
mass: 0.5
unit: unit
material_class: composite
bom: bom_programming_adapter_or_jig_v0
notes: Adapter or jig for programming microcontrollers, FPGAs, or embedded systems.
  Includes pogo pin fixture, ZIF socket, or ISP header connector. Provides reliable
  electrical connection for firmware programming and testing. Used in electronics
  manufacturing and repair.
recipe: recipe_programming_adapter_or_jig_v0
unit_kind: discrete
```

`kb/recipes/recipe_programming_adapter_or_jig_v0.yaml`

```yaml
id: recipe_programming_adapter_or_jig_v0
target_item_id: programming_adapter_or_jig
variant_id: v0
inputs:
  - item_id: plastic_housing_molded
    qty: 0.33
    unit: kg
  - item_id: pogo_pin_set
    qty: 1
    unit: unit
  - item_id: connector_electrical_small
    qty: 1
    unit: unit
  - item_id: wire_copper_insulated
    qty: 0.1
    unit: kg
outputs:
  - item_id: programming_adapter_or_jig
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: plastic_housing_molded
        qty: 0.33
        unit: kg
      - item_id: pogo_pin_set
        qty: 1
        unit: unit
      - item_id: connector_electrical_small
        qty: 1
        unit: unit
      - item_id: wire_copper_insulated
        qty: 0.1
        unit: kg
    outputs:
      - item_id: programming_adapter_or_jig
        qty: 1
        unit: unit
    est_time_hr: 5.0
    machine_hours: 2.0
    labor_hours: 3.0
    notes: "Machine jig body and alignment features, install pogo pins/connectors/socket, wire programming connections to cable header, test connectivity and alignment"
assumptions: Programming adapter for microcontroller firmware loading. Pogo pins and connectors may be imported initially, jig body manufactured locally.
notes: Essential tool for electronics manufacturing. Provides reliable, repeatable connection for programming embedded systems during production.
```

### `punch_press_drill`

`kb/boms/bom_punch_press_drill.yaml`

```yaml
id: bom_punch_press_drill
owner_item_id: punch_press_drill
target_item_id: punch_press_drill
variant_id: v0
components:
  - item_id: machine_frame_heavy
    qty: 1
    unit: unit
    notes: "Heavy steel frame for punch and drill operations (~200 kg)"
  - item_id: hydraulic_cylinder_industrial
    qty: 2
    unit: unit
    notes: "Hydraulic cylinders for punch ram and clamping (~30 kg each)"
  - item_id: spindle_head_basic
    qty: 1
    unit: unit
    notes: "Drill spindle head (~60 kg)"
  - item_id: punch_die_set
    qty: 1
    unit: unit
    notes: "Interchangeable punch dies and holders (~40 kg)"
  - item_id: linear_guide_rails
    qty: 1
    unit: unit
    notes: "Linear rails for table positioning (~20 kg)"
  - item_id: hydraulic_pump_basic
    qty: 1
    unit: unit
    notes: "Hydraulic pump for punch system (~30 kg)"
  - item_id: control_panel_basic
    qty: 1
    unit: unit
    notes: "Controls for punch/drill mode selection (~20 kg)"
notes: Combined punch press and drilling machine for sheet metal fabrication. Total mass ~400 kg.
```

`kb/items/machines/punch_press_drill.yaml`

```yaml
id: punch_press_drill
kind: machine
name: Punch press / drill
mass: 340.0
mass_kg: 340.0
unit: unit
bom: bom_punch_press_drill
notes: Combined punch press and drill machine for making holes and cutouts in sheet
  metal and plate. Hydraulic or mechanical punch mechanism plus drill spindle.
recipe: recipe_machine_punch_press_drill_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_punch_press_drill_v0.yaml`

```yaml
id: recipe_machine_punch_press_drill_v0
target_item_id: punch_press_drill
variant_id: v0
inputs:
  - item_id: metal_feedstock
    qty: 320.0
    unit: kg
  - item_id: machined_part_raw
    qty: 310.0
    unit: kg
  - item_id: welded_fabrications
    qty: 310.0
    unit: kg
  - item_id: motor_electric_small
    qty: 1
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2
    unit: unit
  - item_id: fastener_kit_large
    qty: 1
    unit: unit
  - item_id: electronic_components_set
    qty: 1
    unit: kg
  - item_id: control_panel_basic
    qty: 1
    unit: kg
  - item_id: assembled_equipment
    qty: 340.0
    unit: kg
  - item_id: assembled_electrical_system
    qty: 340.0
    unit: kg
outputs:
  - item_id: punch_press_drill
    qty: 1
    unit: unit
steps:
  - process_id: machining_finish_basic_v0
    inputs:
    - item_id: metal_feedstock
      qty: 320.0
      unit: kg
    outputs:
    - item_id: machined_part_raw
      qty: 310.0
      unit: kg
    est_time_hr: 10.0
    machine_hours: 10.0
    labor_hours: 5.0
    notes: "Machine base, column, ram, and punch tooling components"
  - process_id: welding_and_fabrication_v0
    inputs:
    - item_id: machined_part_raw
      qty: 310.0
      unit: kg
    outputs:
    - item_id: welded_fabrications
      qty: 310.0
      unit: kg
    est_time_hr: 6.0
    labor_hours: 6.0
    notes: "Weld machine frame and structural components for rigidity"
  - process_id: assembly_basic_v0
    inputs:
    - item_id: welded_fabrications
      qty: 310.0
      unit: kg
    - item_id: motor_electric_small
      qty: 1
      unit: unit
    - item_id: bearing_set_heavy
      qty: 2
      unit: unit
    - item_id: fastener_kit_large
      qty: 1
      unit: unit
    outputs:
    - item_id: assembled_equipment
      qty: 340.0
      unit: kg
    est_time_hr: 8.0
    labor_hours: 8.0
    notes: "Assemble press mechanism, drive system, and tooling mounts"
  - process_id: wiring_and_electronics_integration_v0
    inputs:
    - item_id: assembled_equipment
      qty: 340.0
      unit: kg
    - item_id: electronic_components_set
      qty: 1
      unit: kg
    - item_id: control_panel_basic
      qty: 1
      unit: kg
    outputs:
    - item_id: assembled_electrical_system
      qty: 340.0
      unit: kg
    est_time_hr: 3.0
    labor_hours: 3.0
    notes: "Wire motor controls and safety interlocks"
  - process_id: integration_test_basic_v0
    inputs:
    - item_id: assembled_electrical_system
      qty: 340.0
      unit: kg
    outputs:
    - item_id: punch_press_drill
      qty: 1
      unit: unit
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: "Test punching and drilling operations across full stroke"
assumptions: "Mechanical or hydraulic punch press with drill capability. Steel frame construction."
notes: "Punch press and drill machine for sheet metal hole punching and drilling operations."
```

### `refining_furnace_v0`

`kb/boms/bom_refining_furnace_v0.yaml`

```yaml
id: bom_refining_furnace_v0
owner_item_id: refining_furnace_v0
components:
  - item_id: furnace_shell_insulated
    qty: 1.0
    unit: unit
  - item_id: refractory_lining_set
    qty: 1.0
    unit: unit
  - item_id: heating_element_set_basic
    qty: 1.0
    unit: unit
  - item_id: temperature_controller_basic
    qty: 1.0
    unit: unit
notes: "Placeholder BOM for refining_furnace_v0; all components are established in KB; no further expansion yet."
```

`kb/items/machines/refining_furnace_v0.yaml`

```yaml
id: refining_furnace_v0
name: Refining Furnace
kind: machine
mass: 462.0
mass_kg: 462.0
unit: unit
bom: bom_refining_furnace_v0
capabilities:
- refining
- heating
notes: 'Assumptions:

  - Mass aligned to current assembly inputs (462 kg).

  Placeholder refining furnace v0; used to close BOM gap bom_refining_furnace_v0.yaml.

  '
recipe: recipe_refining_furnace_v0
unit_kind: discrete
```

`kb/recipes/recipe_refining_furnace_v0.yaml`

```yaml
id: recipe_refining_furnace_v0
kind: recipe
variant_id: v0
target_item_id: refining_furnace_v0
inputs:
  - item_id: furnace_shell_insulated
    qty: 1
    unit: unit
  - item_id: refractory_lining_set
    qty: 1
    unit: unit
  - item_id: heating_element_set_basic
    qty: 1
    unit: unit
  - item_id: temperature_controller_basic
    qty: 1
    unit: unit
outputs:
  - item_id: refining_furnace_v0
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: furnace_shell_insulated
        qty: 1
        unit: unit
      - item_id: refractory_lining_set
        qty: 1
        unit: unit
      - item_id: heating_element_set_basic
        qty: 1
        unit: unit
      - item_id: temperature_controller_basic
        qty: 1
        unit: unit
    outputs:
      - item_id: refining_furnace_v0
        qty: 1
        unit: unit
    est_time_hr: 24.0
    machine_hours: 8.0
    labor_hours: 16.0
    notes: "Assemble furnace shell, install refractory lining, mount heating elements, integrate temperature control system"
assumptions: "Standard refining furnace assembly from pre-fabricated components"
notes: "Assembly of refining furnace for metallurgical refining operations"
```

### `rolling_mill`

`kb/boms/bom_rolling_mill_v0_v0_seed.yaml`

```yaml
id: bom_rolling_mill_v0_v0_seed
kind: bom
owner_item_id: rolling_mill

target_item_id: rolling_mill_v0_v0
components:
  - item_id: import_misc_components_set
    qty: 1.0
requires_ids:
  - import_misc_components_set
notes: "Seed BOM mirroring bom_rolling_mill_v0_v0 to resolve referenced_only gap."
```

`kb/items/machines/rolling_mill.yaml`

```yaml
id: rolling_mill
kind: machine
name: Rolling mill
mass: 800.0
unit: unit
bom: bom_rolling_mill_v0
material_class: steel
notes: DEPRECATED - Consolidated into plate_rolling_mill. Hot rolling mill for converting
  ingots and billets into sheet, plate, bar, and other forms. Heavy rollers compress
  heated metal through multiple passes to achieve desired thickness and shape. Essential
  for producing sheet metal and stock material.
recipe: recipe_rolling_mill_v1
unit_kind: discrete
```

`kb/recipes/recipe_rolling_mill_base_v0.yaml`

```yaml
id: recipe_rolling_mill_base_v0
kind: recipe
name: Rolling mill base production (v0)
target_item_id: rolling_mill
variant_id: base_v0
inputs:
  - item_id: steel_drum
    qty: 36
    unit: unit
  - item_id: motor_assembly
    qty: 2
    unit: unit
  - item_id: bearing_set
    qty: 4
    unit: unit
  - item_id: grinding_media_steel
    qty: 50.0
    unit: kg
steps:
  - process_id: machine_assembly_basic_v0
    inputs:
      - item_id: steel_drum
        qty: 36
        unit: unit
      - item_id: motor_assembly
        qty: 2
        unit: unit
      - item_id: bearing_set
        qty: 4
        unit: unit
      - item_id: grinding_media_steel
        qty: 50.0
        unit: kg
    outputs:
      - item_id: rolling_mill
        qty: 1
        unit: unit
    est_time_hr: 8.0
    labor_hours: 8.0
    notes: "Assemble rolling mill from BOM components: drum, motor, bearings, and grinding media"
notes: "Base variant recipe to produce the rolling_mill item from BOM components; aligns with bom_rolling_mill_v0.yaml. Simplified to single assembly step."
```

`kb/recipes/recipe_rolling_mill_v1.yaml`

```yaml
id: recipe_rolling_mill_v1
kind: recipe
name: Rolling mill assembly v1
target_item_id: rolling_mill
inputs:
  - item_id: steel_drum
    qty: 1.0
    unit: unit
  - item_id: motor_assembly
    qty: 1.0
    unit: unit
  - item_id: bearing_set
    qty: 2.0
    unit: unit
  - item_id: grinding_media_steel
    qty: 50.0
    unit: kg
  - item_id: bulk_material_or_parts
    qty: 750.0
    unit: kg
outputs:
  - item_id: rolling_mill
    qty: 1.0
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: steel_drum
        qty: 1.0
        unit: unit
      - item_id: motor_assembly
        qty: 1.0
        unit: unit
      - item_id: bearing_set
        qty: 2.0
        unit: unit
      - item_id: grinding_media_steel
        qty: 50.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 50.0
        unit: kg
  - process_id: machining_finish_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 50.0
        unit: kg
    outputs:
      - item_id: machined_part_raw
        qty: 50.0
        unit: kg
  - process_id: welding_brazing_basic_v0
    inputs:
      - item_id: machined_part_raw
        qty: 50.0
        unit: kg
    outputs:
      - item_id: welded_assemblies
        qty: 50.0
        unit: kg
  - process_id: machine_assembly_basic_v0
    inputs:
      - item_id: welded_assemblies
        qty: 50.0
        unit: kg
      - item_id: bulk_material_or_parts
        qty: 750.0
        unit: kg
    outputs:
      - item_id: rolling_mill
        qty: 1.0
        unit: unit
notes: "Upgrade path for rolling_mill; aligns with current rolling_mill item and seed BOM."
assumptions: "Relies on BOM bom_rolling_mill_v0.yaml for parts and subassemblies."
```

### `signal_generator`

`kb/boms/bom_signal_generator_v0.yaml`

```yaml
id: bom_signal_generator_v0
owner_item_id: signal_generator
components:
  - item_id: oscillator_circuit_vacuum_tube_v0
    qty: 1
  - item_id: amplifier_circuit_vacuum_tube_v0
    qty: 1
  - item_id: control_panel_basic
    unit: unit
    qty: 1
  - item_id: power_supply_bench
    qty: 1
notes: Signal generation equipment.
```

`kb/items/machines/signal_generator_v0.yaml`

```yaml
id: signal_generator
kind: machine
name: Signal Generator
mass: 25.0
unit: unit
bom: bom_signal_generator_v0
notes: Electronic signal generator for test and measurement applications.
recipe: recipe_signal_generator_v0
unit_kind: discrete
```

`kb/recipes/recipe_signal_generator_v0.yaml`

```yaml
id: recipe_signal_generator_v0
kind: recipe
name: Signal generator assembly
target_item_id: signal_generator
variant_id: v0
inputs:
  - item_id: oscillator_circuit_vacuum_tube_v0
    qty: 1
    unit: unit
  - item_id: amplifier_circuit_vacuum_tube_v0
    qty: 1
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: power_supply_bench
    qty: 1
    unit: unit
outputs:
  - item_id: signal_generator
    qty: 1
    unit: unit
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: oscillator_circuit_vacuum_tube_v0
        qty: 1
        unit: unit
      - item_id: amplifier_circuit_vacuum_tube_v0
        qty: 1
        unit: unit
      - item_id: control_panel_basic
        qty: 1
        unit: unit
      - item_id: power_supply_bench
        qty: 1
        unit: unit
    outputs:
      - item_id: signal_generator
        qty: 1
        unit: unit
    est_time_hr: 1.0
notes: "Assemble signal generator from BOM; placeholder assembly step."
```

### `temperature_sensing`

`kb/items/parts/temperature_sensing.yaml`

```yaml
id: temperature_sensing
kind: machine
name: Temperature sensing equipment
mass: 2.0
unit: unit
material_class: electronic
capabilities:
  - temperature_measurement
  - thermal_sensing
is_import: true
deprecated: true
replaced_by:
  default:
    - thermocouple_contact_temperature_sensor_v0
    - temperature_controller_module
  low_medium_temperature_contact:
    - rtd_contact_temperature_sensor_v0
    - temperature_controller_module
  high_temperature_non_contact:
    - optical_pyrometer_temperature_sensor_v0
    - temperature_controller_module
notes: Set of temperature sensors including thermocouples, RTDs, pyrometers, and associated
  signal conditioning electronics for high-temperature processes. Deprecated generic
  bundle; replace with a specific sensor assembly plus the shared temperature_controller_module.
unit_kind: discrete
```

### `test_equipment_electronics`

`kb/boms/bom_test_equipment_electronics.yaml`

```yaml
id: bom_test_equipment_electronics
owner_item_id: test_equipment_electronics
components:
- item_id: multimeter_digital
  qty: 1.0
  unit: unit
- item_id: oscilloscope_basic
  qty: 1.0
  unit: unit
- item_id: power_supply_low_voltage
  qty: 1.0
  unit: unit
- item_id: test_lead_set
  qty: 1.0
  unit: kit
- item_id: hand_tools_basic
  qty: 1.0
  unit: kit
```

`kb/items/machines/test_equipment_electronics.yaml`

```yaml
id: test_equipment_electronics
kind: machine
name: Electronics test equipment
mass: 9.6
unit: unit
bom: bom_test_equipment_electronics
material_class: electronic
notes: DEPRECATED - Consolidated into test_bench_electrical. Electronics test and
  measurement equipment. Includes multimeters, oscilloscopes, signal generators, power
  supplies, and function generators. Used for circuit testing, troubleshooting, and
  validation. Essential for electronics development and quality control.
recipe: recipe_machine_test_equipment_electronics_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_test_equipment_electronics_v0.yaml`

```yaml
id: recipe_machine_test_equipment_electronics_v0
target_item_id: test_equipment_electronics
variant_id: v0
inputs:
  - item_id: multimeter_digital
    qty: 1.0
    unit: unit
  - item_id: oscilloscope_basic
    qty: 1.0
    unit: unit
  - item_id: power_supply_low_voltage
    qty: 1.0
    unit: unit
  - item_id: test_lead_set
    qty: 1.0
    unit: kit
  - item_id: hand_tools_basic
    qty: 1.0
    unit: kit
outputs:
  - item_id: test_equipment_electronics
    qty: 9.6
    unit: kg
steps:
  - process_id: electronics_assembly_v0
    inputs:
      - item_id: multimeter_digital
        qty: 1.0
        unit: unit
      - item_id: oscilloscope_basic
        qty: 1.0
        unit: unit
      - item_id: power_supply_low_voltage
        qty: 1.0
        unit: unit
      - item_id: test_lead_set
        qty: 1.0
        unit: kit
      - item_id: hand_tools_basic
        qty: 1.0
        unit: kit
    outputs:
      - item_id: assembled_electronics
        qty: 9.6
        unit: kg
    est_time_hr: 12.0
    labor_hours: 10.0
    notes: "Assemble various test instruments: multimeters, oscilloscopes, signal generators, power supplies"
  - process_id: calibration_basic_v0
    inputs:
      - item_id: assembled_electronics
        qty: 9.6
        unit: kg
    outputs:
      - item_id: assembled_electronics
        qty: 9.6
        unit: kg
    est_time_hr: 8.0
    labor_hours: 6.0
    notes: "Calibrate all test equipment against reference standards"
  - process_id: integration_test_basic_v0
    inputs:
      - item_id: assembled_electronics
        qty: 9.6
        unit: kg
    outputs:
      - item_id: assembled_electronics
        qty: 9.6
        unit: kg
    est_time_hr: 2.0
    labor_hours: 1.5
    notes: "Test all equipment functionality and accuracy"
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_electronics
        qty: 9.6
        unit: kg
    outputs:
      - item_id: test_equipment_electronics
        qty: 9.6
        unit: kg
    est_time_hr: 1.0
    labor_hours: 1.0
    notes: "Verify calibration and operational status"
assumptions: "Electronics test and measurement equipment set. Includes multimeters, oscilloscopes, signal generators, and power supplies. 9.6 kg collection of test instruments."
notes: "Assembly of electronics test equipment set. Total assembly time ~23 hours. Requires calibration against known standards. Essential for electronics development and quality control."
```

### `thermal_water_extractor`

`kb/boms/bom_thermal_water_extractor_v0.yaml`

```yaml
id: bom_thermal_water_extractor_v0
owner_item_id: thermal_water_extractor
components:
  - item_id: heating_chamber_large
    qty: 1
  - item_id: vapor_condenser_cold_trap
    qty: 1
  - item_id: coolant_reservoir
    qty: 1
    notes: "Used as water collection tank"
  - item_id: insulation_thermal_blanket
    qty: 1
  - item_id: temperature_control_system_v0
    qty: 1
notes: Thermal water extraction equipment.
```

`kb/items/machines/thermal_water_extractor_v0.yaml`

```yaml
id: thermal_water_extractor
kind: machine
name: Thermal Water Extraction System
mass: 185.0
unit: unit
bom: bom_thermal_water_extractor_v0
recipe: recipe_machine_thermal_water_extractor_v0
notes: 'Assumptions:

  - Mass aligned to current recipe component sum (185 kg).

  Thermal extraction system for recovering water from hydrated materials.

  '
unit_kind: discrete
```

`kb/recipes/recipe_machine_thermal_water_extractor_v0.yaml`

```yaml
id: recipe_machine_thermal_water_extractor_v0
kind: recipe
target_item_id: thermal_water_extractor
variant_id: v0
inputs:
  - item_id: heating_chamber_large
    qty: 150.0
    unit: kg
  - item_id: vapor_condenser_cold_trap
    qty: 4.0
    unit: kg
  - item_id: coolant_reservoir
    qty: 20.0
    unit: kg
  - item_id: insulation_thermal_blanket
    qty: 1
    unit: kg
  - item_id: temperature_control_system_v0
    qty: 10.0
    unit: kg
outputs:
  - item_id: thermal_water_extractor
    qty: 185.0
    unit: kg
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: heating_chamber_large
        qty: 150.0
        unit: kg
      - item_id: vapor_condenser_cold_trap
        qty: 4.0
        unit: kg
      - item_id: coolant_reservoir
        qty: 20.0
        unit: kg
      - item_id: insulation_thermal_blanket
        qty: 1
        unit: kg
      - item_id: temperature_control_system_v0
        qty: 10.0
        unit: kg
    outputs:
      - item_id: thermal_water_extractor
        qty: 185.0
        unit: kg
notes: "Assemble thermal water extractor from BOM components; placeholder assembly recipe."
```

### `thermionic_generator`

`kb/boms/bom_thermionic_generator_v0.yaml`

```yaml
id: bom_thermionic_generator_v0
owner_item_id: thermionic_generator
components:
  - item_id: thermionic_converter
    qty: 10
  - item_id: heat_source_nuclear
    qty: 1
  - item_id: heat_rejection_radiator
    qty: 1
  - item_id: power_conditioning_module
    qty: 1
notes: Thermionic power generation equipment.
```

`kb/items/machines/thermionic_generator_v0.yaml`

```yaml
id: thermionic_generator
kind: machine
name: Thermionic Power Generator
mass: 350.0
unit: unit
bom: bom_thermionic_generator_v0
notes: Thermionic emission-based power generation system.
unit_kind: discrete
```

`kb/recipes/recipe_thermionic_generator_v0.yaml`

```yaml
id: recipe_thermionic_generator_v0
target_item_id: thermionic_generator
variant_id: v0
inputs:
  - item_id: thermionic_converter
    qty: 10
    unit: unit
  - item_id: heat_rejection_radiator
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: thermal_interface_material
    qty: 5.0
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 2.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
outputs:
  - item_id: thermionic_generator
    qty: 350.0
    unit: kg
steps:
  - process_id: assembly_basic_v0
    inputs:
      - item_id: thermionic_converter
        qty: 10
        unit: unit
      - item_id: heat_rejection_radiator
        qty: 1
        unit: unit
      - item_id: power_conditioning_module
        qty: 1
        unit: unit
      - item_id: thermal_interface_material
        qty: 5.0
        unit: kg
      - item_id: electrical_wire_and_connectors
        qty: 2.0
        unit: kg
      - item_id: fastener_kit_medium
        qty: 1
        unit: unit
    outputs:
      - item_id: thermionic_generator
        qty: 350.0
        unit: kg
    est_time_hr: 52.0
    labor_hours: 52.0
    notes: "Complete thermionic generator assembly: mount radiator, install and series-connect 10 thermionic converter modules, integrate power conditioning, braze thermal connections, wire electrical connections, vacuum leak test, integration test under load."
assumptions: |
  Thermionic power generator assembly from pre-fabricated components.
  10 converters (80 kg) connected in series for ~10-15V output voltage.
  Radiator (250 kg) sized for 70-90% waste heat rejection.
  Power conditioning (12 kg) converts DC output to usable form.
  Thermal interface material (5 kg) for bonding heat paths.
  Total input 350 kg yields 350 kg generator (1 unit).
  Removed heat_source_nuclear (item doesn't exist) - heat source integration deferred to operational setup.
notes: |
  Manufacturing recipe for thermionic emission-based power generation system.
  Converts thermal energy directly to electrical power via thermionic emission.
  Efficiency: 15-20% typical (Russian TOPAZ reactors achieved 20%).
  Critical assembly: thermal interface bonding, vacuum integrity, electrical series connection.
  Applications: base load power from nuclear/solar thermal, waste heat recovery from ISRU.
  Consolidated into single-step assembly for simplicity.
```

### `winding_machine`

`kb/boms/bom_winding_machine_v0.yaml`

```yaml
id: bom_winding_machine_v0
owner_item_id: winding_machine
components:
  - item_id: winding_machine_frame
    qty: 1
  - item_id: winding_drive_motor
    qty: 1
  - item_id: tension_control_unit
    qty: 1
  - item_id: winding_drums
    qty: 1
  - item_id: control_compute_module_imported
    qty: 1
  - item_id: sensor_suite_general
    qty: 1
  - item_id: power_conditioning_module
    qty: 1
  - item_id: fastener_kit_medium
    qty: 1
notes: Coarse BOM for winding machine; imported compute/sensors assumed.
```

`kb/items/machines/winding_machine.yaml`

```yaml
id: winding_machine
kind: machine
name: Winding machine
mass: 150.0
unit: unit
bom: bom_winding_machine_v0
notes: Motorized winding machine with tension control for spooling wire, fiber, and
  cable onto drums or bobbins. Variable speed drive with adjustable tensioning.
recipe: recipe_machine_winding_machine_v0
unit_kind: discrete
```

`kb/recipes/recipe_machine_winding_machine_v0.yaml`

```yaml
id: recipe_machine_winding_machine_v0
target_item_id: winding_machine
variant_id: v0
inputs:
  - item_id: import_misc_components_set
    qty: 150.0
    unit: kg
outputs:
  - item_id: winding_machine
    qty: 1.0
    unit: unit
steps:
  - process_id: import_receiving_basic_v0
    inputs:
      - item_id: import_misc_components_set
        qty: 150.0
        unit: kg
    outputs:
      - item_id: import_misc_components_set
        qty: 50.0
        unit: kg
    est_time_hr: 0.5
    labor_hours: 0.5
  - process_id: assembly_basic_v0
    inputs:
      - item_id: import_misc_components_set
        qty: 150.0
        unit: kg
    outputs:
      - item_id: assembled_equipment
        qty: 150.0
        unit: kg
    est_time_hr: 2.0
    labor_hours: 2.0
    machine_hours: 2.0
  - process_id: inspection_basic_v0
    inputs:
      - item_id: assembled_equipment
        qty: 150.0
        unit: kg
    outputs:
      - item_id: winding_machine
        qty: 1.0
        unit: unit
    est_time_hr: 0.5
    labor_hours: 0.5
assumptions: Assemble winding machine per BOM; imported compute/sensors.
notes: |
  Coarse route; refine with calibration later.
  Mass balance: inspection step uses 3x assembled_equipment to match 150 kg output mass.
  Mass balance: import_misc_components_set scaled to 50 kg to match assembly output mass.
```

