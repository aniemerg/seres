# Machine identity

- Queue item: `machine_reality_gravity_separator`
- KB item: `gravity_separator`
- KB name: Gravity separator
- KB file: `kb/items/machines/gravity_separator.yaml`
- Current KB kind: `machine`
- Current mass: 180 kg
- Current BOM: `bom_gravity_separator_v0`
- Current recipe: `recipe_gravity_separator_v0`

# KB usage and needed function

`gravity_separator` is used by `mineral_concentration_v0`, `mineral_processing_basic_v0`, `tungsten_density_separation_v0`, `tungsten_extraction_meteorite_v0`, `liquation_fe_tio2_separation_v0`, and related extraction/material concentration processes.

The BOM contains a separation table assembly, vibration drive module, air manifold/nozzles, control panel, frame/supports, and fasteners. The recipe fabricates a steel frame/deck, machines interfaces, and installs vibration, air manifold, and controls. That matches a dry air table/fluidized-bed density separator and partially overlaps with a wet shaking table.

The needed function is density-based particulate separation after crushing/screening, especially for upgrading heavy minerals from lighter gangue or separating metal-rich particles.

# Reality classification

Real practical machine category.

Gravity separators, shaking tables, air tables, jigs, spirals, and related density separators are real mineral/seed/grain processing equipment. The KB item is realistic as a compact gravity/density separator, but it is generic. A dry air table and a wet shaking table are related but not identical; water availability, dust control, particle size, gravity level, and atmosphere matter.

# Evidence links

- 911Metallurgist describes dry shaking air tables: air tables use shaking motion like wet shaking tables, but air is blown through a porous deck to separate heavy minerals: https://www.911metallurgist.com/blog/dry-shaking-air-table/
- 911Metallurgist describes shaking tables as efficient gravity separation equipment for sub-2 mm materials, used for concentrates such as gold, tin, tungsten, tantalum, and chromite: https://www.911metallurgist.com/equipments/shaker-tables/
- Oliver Manufacturing describes gravity separators/air tables as machines that divide heavier and lighter particles by specific density using air fluidization and deck motion: https://olivermanufacturing.com/all-products/category/gravity-separator/
- Oliver's process description explains air and vibration assisting density separation, with heavier particles settling and lighter particles remaining higher in the fluidized bed: https://olivermanufacturing.com/how-it-works-processing-machines/gravity-separation/
- Triple/S Dynamics describes industrial density/gravity separators, air tables, or fluidized bed separators using mechanical vibration and air fluidization for dry materials: https://www.sssdynamics.com/equipment/density-separation/
- NTNU notes gravity separation is one of the oldest separation methods and remains important for very dense minerals, supplementing flotation and magnetic separation without chemicals: https://www.ntnu.edu/igv/gravity-separation
- Deister describes shaking tables as gravity concentration equipment for fine minerals: https://www.deisterconcentrator.com/resources/deister-news/improving-mineral-processing-with-shaking-tables

# Commercial alternatives

Commercial alternatives include:

- Wet shaking table for fine mineral concentration with wash water.
- Dry air table/fluidized-bed separator for dry granular material.
- Jig concentrator for pulsating water/air density separation.
- Spiral concentrator for wet gravity separation at larger throughputs.
- Centrifugal concentrator or multi-gravity separator where finer particles or low gravity make simple settling less effective.
- Magnetic separator, electrostatic separator, or flotation cell when density contrast alone is insufficient.

# Build or open-source references

The KB recipe is plausible for a small dry density separator:

- welded frame and deck,
- adjustable slope,
- vibration/eccentric drive,
- air plenum/manifold/nozzles or porous deck,
- feed and collection splitters,
- control panel for air flow, vibration intensity, and deck angle.

For wet shaking-table operation, the KB would also need water handling, riffled deck geometry, wash-water distribution, slurry feed, and tailings/concentrate collection. For lunar use, dry air-table operation requires a pressurized or gas-handling environment; operation in vacuum is not equivalent.

# Related machine research

Related local reports:

- `screening_equipment.md`
- `vibrating_screen_v0.md`
- `dust_collection_system.md`
- `rock_crusher_basic.md`

Related KB items include `magnetic_separator_drum_v0`, `vibration_drive_module`, `screening_equipment`, and `mineral_concentration_v0`.

# Recommendation for KB realism

Keep `gravity_separator` as a real compact mineral-processing machine, but tighten scope.

Recommended refinements:

- Rename or annotate as `gravity_density_separator_table` or `dry_air_table_gravity_separator` if the current BOM remains air-table based.
- Do not imply one item covers all gravity separation methods; jigs, spirals, wet shaking tables, and centrifugal concentrators differ.
- Add process assumptions for particle size, feed preparation, density contrast, moisture, air/water medium, and throughput.
- For lunar/regolith scenarios, note that lower gravity weakens ordinary gravity separation; vibration/air fluidization, centrifugal assistance, or magnetic/electrostatic separation may be more realistic for some fractions.
- Keep it distinct from `screening_equipment`: screening separates by size, while gravity separation separates by density/specific gravity after size preparation.

# Confidence and open questions

Confidence: high that gravity/density separators are real; high that the KB BOM resembles a real air table; medium on lunar effectiveness because low gravity, vacuum, dust, and lack of water change separator design.

Open questions:

- Is the intended operation dry air-table separation, wet shaking-table separation, or an abstract density separator?
- Does simulation assume Earth gravity, lunar gravity, or pressurized habitat gravity conditions for separation performance?
- Are water, process gas, and dust collection modeled for separator operation?
