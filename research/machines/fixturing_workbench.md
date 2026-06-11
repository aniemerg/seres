# Machine identity

- Queue item: `machine_reality_fixturing_workbench`
- KB item: `fixturing_workbench`
- KB name: Fixturing workbench
- KB file: `kb/items/machines/fixturing_workbench.yaml`
- Current KB kind: `machine`
- Current mass: 150 kg
- Current capability: `fixturing_table`
- Current BOM: `bom_fixturing_workbench_v0`
- Current recipe: `recipe_fixturing_workbench_v0`

# KB usage and needed function

`fixturing_workbench` is required by multiple welding and fabrication processes, including `welding_and_fabrication_v0`, `welding_structural_v0`, `welded_fabrication_basic_v0`, `welding_brazing_basic_v0`, `metal_fabrication_welding_v0`, and `fabricate_structural_steel_frame_v0`.

The BOM contains a heavy workbench frame, T-slot table top, vise mounting hardware, and fasteners. The recipe welds a heavy steel frame, machines T-slots/mounting holes/leveling surfaces, and assembles the table and hardware.

The needed function is stable, repeatable workholding: hold parts square, flat, and located during welding, brazing, fitting, structural assembly, and inspection/setup. This is more capable than a generic bench because the table pattern, clamps, stops, and fixturing hardware define alignment repeatability.

# Reality classification

Real practical shop equipment/workholding station, not a production machine by itself.

Modular welding and fixture tables are standard fabrication equipment. The KB's 150 kg mass is plausible for a small-to-medium heavy steel table with a machined top and accessories. It should be treated as passive shop equipment that enables other processes rather than as an active machine.

# Evidence links

- Siegmund welding tables and clamping systems are sold as precision welding/fixturing solutions for welding, assembly, and precision fabrication, with hardened table systems and extensive clamping accessories: https://weldingtablesandfixtures.com/
- BuildPro/Strong Hand modular welding tables are sold through welding suppliers with fixture tables, 5/8 in or 16 mm hole systems, clamps, stops, riser blocks, and fixturing kits: https://canadaweldingsupply.com/collections/buildpro-welding-fixture-tables-and-accessories
- Trick-Tools lists modular fixture tables, including Siegmund and BuildPro-style welding table systems for modular fixturing: https://www.trick-tools.com/tools/Modular-Fixture-Tables
- The Fabricator describes modular welding fixturing as useful for holding work consistently and repeatably, especially for temporary jobs, high-mix jobs, and short-run production: https://www.thefabricator.com/thewelder/article/cuttingweldprep/a-guide-to-modular-fixturing-in-welding
- WeldTables/Certiflat describes a tab-and-slot welding table kit with 16 mm holes on 2 in centers for clamps and repeated fixturing positions, supporting the KB's buildable/local-fabrication interpretation: https://weldtables.com/products/copy-of-3x4-large-heavy-duty-welding-table-top-kit-certiflat-by-tab-slot-u-weld
- Langmuir Systems sells the ArcFlat modular cast-iron weld fixture table with machined faces and fixture holes, another commercial example of the category: https://www.langmuirsystems.com/arcflat

# Commercial alternatives

Commercial alternatives include:

- Modular hole-grid welding tables such as Siegmund, BuildPro, ArcFlat, Certiflat, and similar systems.
- T-slotted platen tables and machine tables where T-slot clamps are preferred.
- Heavy flat welding benches with custom jigs for low-precision or one-off work.
- Dedicated welded jigs/fixtures for repeated production of a single assembly.
- General assembly workbench, which is cheaper but not equivalent for precision welding or repeatable fixture setup.

# Build or open-source references

The KB manufacturing route is realistic for a basic local version:

- weld a heavy frame from structural steel,
- fabricate or machine a thick table top,
- add a hole grid or T-slots,
- install leveling feet,
- make clamps, stops, squares, vise mounts, and fixture plates,
- inspect flatness and hole/slot spacing.

Commercial tables use precision machining, hardened/cast surfaces, nitrided/tool-steel tops, or cast iron for long-term flatness and spatter resistance. A local 150 kg table can be useful even if it is less precise and less wear-resistant than premium commercial products.

# Related machine research

Related local reports:

- `metal_forming_basic_v0.md`
- `hand_tools_basic.md`
- `inspection_tools_basic.md`
- `saw_or_cutting_tool.md`
- `refractory_installation_tools.md`
- `lifting_equipment.md`

Related KB items include `assembly_workbench_v0`, `workbench_basic`, `steel_workbench_heavy`, `fixture_mounting_plate_set`, `workpiece_fixture_set`, and `mounting_fixtures_adjustable`.

# Recommendation for KB realism

Keep `fixturing_workbench` as real and useful equipment, but classify it as workholding/shop infrastructure rather than a powered manufacturing machine.

Specific recommendations:

- Keep it separate from `workbench_basic` and `assembly_workbench_v0`; welding/fabrication fixture tables provide a distinct capability.
- If schema permits, classify as `tooling`, `workholding_equipment`, or `shop_equipment`.
- Preserve `fixturing_table` as a process requirement for welding and structural fabrication.
- Add or preserve compatible accessory items such as clamps, stops, squares, vise mounting hardware, and fixture plates.
- Keep 150 kg as a plausible small table mass, but avoid using it as a proxy for large structural fabrication; table size/flatness/load rating should matter for large frames.

# Confidence and open questions

Confidence: high that this is real practical equipment; high that the KB decomposition is plausible; medium on mass and precision because table capability depends on size, material, thickness, flatness tolerance, and accessory set.

Open questions:

- Does the KB need separate precision grades for rough welding table versus metrology/alignment fixture table?
- Are large frames limited by the table size/load rating, or does the simulator treat the fixture table as unlimited?
- Should `assembly_workbench_v0` and `fixturing_workbench` be linked hierarchically instead of parallel machine-like items?
