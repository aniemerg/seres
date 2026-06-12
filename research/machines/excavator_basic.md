# Machine identity

- Queue item: `machine_reality_excavator_basic`
- KB item: `excavator_basic`
- KB name: Excavator (basic)
- KB file: `kb/items/machines/excavator_basic.yaml`
- Current KB kind: `machine`
- Current mass: 2000 kg
- Current BOM: `bom_excavator_basic_v0`
- Current recipe: `recipe_excavator_basic_v0`

# KB usage and needed function

`excavator_basic` is used for `rock_excavation_basic_v0` and appears in the minimal/self-reproducing set for surface material extraction. Related regolith mining processes currently use more abstract mining process IDs, while the excavator item provides the concrete machine for digging, trenching, and bulk material handling.

The KB describes a hydraulic boom and bucket system for regolith, ore, and soil. The BOM/recipe include tracks/running gear, hydraulic boom assembly, excavator bucket, hydraulic cylinders, pump, valves, motors, controls, operator cabin, frame, and fasteners. That is a realistic mini-excavator architecture.

# Reality classification

Real practical machine, but scale and environment need clarification.

A 2000 kg mass is plausible for a small mini excavator. It is not a full-size construction excavator and should not be assumed to handle deep mining, hard rock ripping, or high-throughput excavation without support equipment. For lunar/regolith use, a terrestrial hydraulic excavator is only an analog: low gravity, vacuum, dust, thermal cycling, launch mass, traction, sealing, lubricant behavior, and autonomous operation change the design.

# Evidence links

- CASE lists mini excavators including the CX15EV electric mini excavator at 1,445 kg, CX17C at 1,775 kg, and CX19D at 1,880 kg, supporting the KB's 2-ton scale: https://www.casece.com/en-us/northamerica/products/excavators/mini-excavators
- Volvo's ECR25 Electric compact excavator has a 5,908-6,129 lb operating weight and 0.04-0.16 yd3 bucket capacity, showing real electric-hydraulic compact excavators: https://www.volvoce.com/united-states/en-us/products/electric-machines/ecr25-electric/
- DOZR summarizes mini excavator operating weights as roughly 2,000-22,000 lb, with small mini excavators from 2,000-10,000 lb: https://dozr.com/blog/mini-excavator-spec-guide
- NASA's Infrastructure Pilot Excavator project is explicitly a Moon mining robot intended to dig lunar regolith and transport it across the surface: https://www.nasa.gov/infrastructure-pilot-excavator/
- NASA lunar ISRU excavation review notes robotic excavation technologies are necessary and that lunar excavators differ substantially from terrestrial excavators due to harsh environment and launch mass/volume limits: https://www.hou.usra.edu/meetings/lunarisru2019/presentations/5066_Mueller.pdf
- South Dakota State work on a bucket-wheel excavator for NASA's Break the Ice Lunar Challenge shows active research into lunar excavation mechanisms for icy simulated regolith: https://openprairie.sdstate.edu/etd2/860/

# Commercial alternatives

Commercial/technical alternatives include:

- 1-3 ton electric or diesel mini excavator for terrestrial analog work.
- Compact tracked loader/front-end loader for scooping and short-haul material handling.
- Bucket-wheel or bucket-ladder excavator for continuous regolith collection.
- RASSOR-style counter-rotating bucket drum excavator for low-gravity traction limits.
- Auger/drill-based excavation for ice-cemented or polar regolith.
- Conveyor/screener/crusher train for continuous mining after excavation.

# Build or open-source references

The KB recipe is plausible as assembly from major subcomponents, but local manufacture is difficult:

- welded/cast heavy frame and track undercarriage,
- hydraulic cylinders, pumps, valves, hoses, seals, and filtration,
- boom/stick/bucket weldments and wear plates,
- electric or diesel prime mover,
- controls, sensors, safety, and autonomy,
- dust-tolerant bearings, seals, lubricants, and maintenance access.

For lunar use, hydraulic fluids and seals may be problematic outside a pressurized environment. Electric actuators or sealed hydraulic systems may be needed. Bucket wear and dust handling should be explicit.

# Related machine research

Related local reports:

- `drilling_equipment_v0.md`
- `rock_crusher_basic.md`
- `screening_equipment.md`
- `vibrating_screen_v0.md`
- `dust_collection_system.md`
- `lifting_equipment.md`

Related KB items include `loader_small`, `bucket_assembly_small`, `excavator_bucket`, `hydraulic_power_unit_basic`, and `regolith_mining_*` processes.

# Recommendation for KB realism

Keep `excavator_basic` as a real machine, but scope it as a compact electric-hydraulic mini excavator or small regolith excavator.

Recommended refinements:

- Clarify whether this is terrestrial-style mini excavator, lunar-adapted excavator, or generic excavation capacity.
- Keep the 2000 kg mass for a compact excavator; do not use it as a proxy for large mining equipment.
- For lunar surface operation, add notes about low-gravity traction, dust sealing, thermal/vacuum compatibility, autonomy, power source, and hydraulic fluid/seal limits.
- Use `drilling_equipment_v0` or specialized excavation for ice-cemented polar regolith, hard rock, or subsurface sampling.
- Keep `loader_small` distinct if the required task is short-haul scooping/transport rather than digging with a boom.

# Confidence and open questions

Confidence: high that the item is real; high that 2-ton mini-excavator mass is plausible; medium that a terrestrial excavator architecture is appropriate for lunar regolith mining.

Open questions:

- Is the modeled excavator intended to operate inside a pressurized worksite, outside on the lunar surface, or in a generic environment?
- Are hydraulic systems acceptable for the intended environment, or should electric actuators be modeled?
- What throughput and bucket capacity are expected for regolith mining processes?
