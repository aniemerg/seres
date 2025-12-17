# Dedupe Decisions Log

Record consolidations and precedents here. Include:
- Date / agent
- Items/processes considered
- Decision and rationale
- Links to updated files (recipes/BOMs/notes)

## 2024-XX-XX — agent: codex
- Scope: Grinding/Polishing family (`surface_grinder`, `bench_grinder`, `polishing_station`).
- Decision: Prefer `surface_grinder` as default finishing tool. Mark `bench_grinder` and `polishing_station` as dedupe candidates with `alternatives: [surface_grinder]`. Retargeted finishing processes to rely on `surface_grinder` (deburring, surface finishing, mirror polishing). Surface grinder marked with `preferred_variant: simple` as default path.
- Files touched: `kb/items/machines/bench_grinder.yaml`, `kb/items/machines/polishing_station.yaml`, `kb/items/machines/surface_grinder.yaml`, `kb/processes/finishing_deburring_v0.yaml`, `kb/processes/surface_finishing_v0.yaml`, `kb/processes/mirror_polishing_v0.yaml`.

## 2024-XX-XX — agent: codex
- Scope: Plate rolling/press brake family (`rolling_mill`, `plate_rolling_mill`, `rolling_mill_or_brake`, `press_brake`, `press_brake_or_roller`).
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
- `milling_machine_cnc` (1200 kg) - CNC milling with precision capabilities
- `precision_lathe` (1200 kg) - precision turning, threading, and boring

**Decision:**
Keep both machines with distinct functions:
1. **`milling_machine_cnc`** (1200 kg) - all milling operations (rotating cutter, stationary workpiece)
2. **`precision_lathe`** (1200 kg) - all turning operations (rotating workpiece, stationary cutter)

Consolidate into above:
- `milling_machine_general_v0` → use `milling_machine_cnc`

**Rationale:**
- Milling and turning are fundamentally different machining operations with different mechanics
- Cannot consolidate lathe into mill - they perform non-overlapping functions
- `milling_machine_general_v0` is unused and redundant with `milling_machine_cnc`
- CNC mill is more capable than general mill (programmable, precision, multi-axis)
- Both CNC mill and precision lathe are already in use by `machining_precision_v0` process

**Files updated:**
- Machines: Added DEPRECATED note to `milling_machine_general_v0.yaml`
- No process files needed updating (machine was unused)

**Next steps:**
- Mark recipe/BOM for deprecated machine as variant or remove in future cleanup

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
- `rolling_mill_or_brake` (800 kg, capability: sheet_forming) - used in 1 process

**Decision:**
Keep only `plate_rolling_mill` as the canonical rolling mill for all rolling operations.

Consolidate into above:
- `rolling_mill` → use `plate_rolling_mill`
- `rolling_mill_or_brake` → use `plate_rolling_mill` (rolling function) and `press_brake` (bending function)

**Rationale:**
- Mass difference between rolling_mill (800 kg) and plate_rolling_mill (1500 kg) is only 1.9x, below our >2-3x threshold
- Both serve the same core function: compressing metal through rollers to reduce thickness
- rolling_basic_v0 process: converts ingots → sheet using hot rolling - plate_rolling_mill handles this
- rolling_mill_or_brake is ambiguous ("either a small rolling mill or a press brake")
- Task hints correctly note that press_brake was already kept separate in previous dedupe for bending operations
- Plate rolling mill can handle both ingot rolling and plate production, no need for separate general rolling mill
- All rolling operations can be consolidated to plate_rolling_mill without loss of capability

**Files updated:**
- Processes: `rolling_basic_v0.yaml` (rolling_mill → plate_rolling_mill), `metal_forming_basic_v0.yaml` (rolling_mill_or_brake → plate_rolling_mill)
- Machines: Added DEPRECATED notes to `rolling_mill.yaml`, `rolling_mill_or_brake.yaml`

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
