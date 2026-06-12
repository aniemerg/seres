# Machine identity

- Queue item: `machine_reality_grinding_wheels`
- KB item: `grinding_wheels`
- KB name: Grinding wheels
- KB file: `kb/items/machines/grinding_wheels.yaml`
- Current KB kind: `machine`
- Current mass: 7.5 kg
- Current import flag: `is_import: false`
- Current canonical recipe: `recipe_grinding_wheels_isru_v0`

# KB usage and needed function

`grinding_wheels` is required by grinding processes including `precision_grinding_basic_v0`, `grinding_process_precision_v0`, `grinding_and_finishing_v0`, and `grinding_basic_v0`, and it appears in machine BOMs such as `bench_grinder`, `bearing_grinding_machine_v0`, and `precision_grinding_system_v0`.

The needed function is consumable abrasive tooling: bonded abrasive wheels that remove metal/ceramic material, hold form, shed dull grains, tolerate wheel speed, and can be dressed/trued. This is not a machine by itself; it is required tooling/consumable for grinders.

The canonical KB recipe mixes `alumina_powder` with `glass_bulk`, presses wheel blanks, fires them at 1200-1400 C into a vitrified bond, then grinds/balances/dresses the wheels. That is directionally realistic for vitrified alumina wheels.

# Reality classification

Real practical consumable/tooling set, not a standalone machine.

Grinding wheels are standard industrial consumables. The KB's 7.5 kg mass is plausible for a set of wheels rather than one small wheel. The main realism issue is classification and quality control: grinding wheels are safety-critical rotating parts, and low-quality wheels can fracture. Wheel grade, grit size, structure/porosity, bond type, speed rating, balance, dressing, and compatible work material all matter.

# Evidence links

- Norton Abrasives explains grinding wheel specifications: abrasive grain letters commonly identify aluminum oxide, cBN, silicon carbide, diamond, and zirconia; wheel specs encode abrasive, grit, grade, structure, and bond: https://www.nortonabrasives.com/en-us/grinding-wheel-basics
- 3M describes vitrified grinding wheels and notes that bond holds abrasive grains together; bond volume affects grinding heat and exposure of active mineral grains: https://www.3m.com/3M/en_US/metalworking-us/applications/precision-grinding/technology/conventional/v450/
- Eagle Superabrasives describes vitrified bond grinding wheels as mixtures of abrasive grains such as aluminum oxide or silicon carbide with a vitrified/ceramic bond, heat-treated to create a rigid structure: https://www.eaglesuperabrasives.com/capabilities-bonds/vitrified-bond-grinding-wheels/
- 3M sells vitrified grinding wheels using white aluminum oxide, monocrystalline aluminum oxide, and ceramic grain blends for precision grinding applications: https://www.3m.com/3M/en_US/p/d/b5005066217/
- MSC lists commercial Norton surface grinding wheels with aluminum oxide abrasive and vitrified bond, supporting this as an off-the-shelf consumable category: https://www.mscdirect.com/browse/tn?searchterm=norton+grinding+wheels
- 3M conventional wheel literature describes vitrified and synthetic resin bonded wheels and notes that bond type and percentage influence strength, hardness, and cutting ability: https://multimedia.3m.com/mws/media/1548211O/portfolio-conventional-wheels-low-resolution-en.pdf
- Norton technical data describes silicon carbide abrasives and vitrified bonds for grinding nonmetallic materials, ceramics, glass, and similar applications: https://www.nortonabrasives.com/sites/mac3-acs-norton/files/Norton_Industrial_technical_data_health_safety_8.pdf

# Commercial alternatives

Commercial alternatives include:

- Aluminum oxide vitrified wheels for general ferrous grinding.
- White/friable aluminum oxide wheels for cooler precision grinding.
- Silicon carbide wheels for cast iron, nonferrous metals, carbide, ceramics, glass, rubber, and stone depending on grade.
- CBN wheels for hardened steel and production grinding.
- Diamond wheels for carbide, ceramics, glass, and hard nonferrous materials.
- Resin-bonded, vitrified-bonded, metal-bonded, and electroplated wheel constructions depending on duty.

# Build or open-source references

The KB ISRU route is plausible as a simplified vitrified alumina wheel route:

- prepare abrasive alumina grain,
- prepare glass/ceramic bond,
- control grain size distribution and bond fraction,
- press/mold blanks,
- fire/vitrify at high temperature,
- true, dress, balance, inspect, and speed-test the wheel.

The missing realism details are important:

- abrasive grains need controlled hardness, shape, friability, and size distribution;
- bond chemistry and porosity influence cutting behavior and heat;
- wheel speed rating and burst safety require proof testing;
- dressing tools are required to keep wheels cutting correctly;
- high-performance cBN/diamond wheels should remain imported or separate advanced items.

# Related machine research

Related local reports:

- `surface_grinder.md`
- `work_rest_adjustable.md`
- `cutting_tools_general.md`
- `inspection_tools_basic.md`

Related KB items include `grinding_wheel_aluminum_oxide`, `dressing_tool_diamond`, `surface_grinder`, `bench_grinder`, `grinder_cylindrical_v0`, and `bearing_grinding_machine_v0`.

# Recommendation for KB realism

Keep `grinding_wheels`, but treat it as consumable abrasive tooling rather than a machine.

Recommended refinements:

- Reclassify from `kind: machine` to part/tooling/consumable if schema supports process requirements on non-machines.
- Keep it separate from `surface_grinder`; the grinder is incomplete without wheels, and wheels wear out.
- Add wheel dressing/truing/balancing/speed-test assumptions to the recipe or notes.
- Keep the ISRU vitrified alumina/glass-bond route as a plausible low-to-medium performance wheel path.
- Do not let generic ISRU wheels stand in for diamond/cBN wheels, high-speed cutoff wheels, or specialized vitrified wheels unless the process requirements are loose enough.
- Update or reconcile the BOM, which still says imported placeholder, with the `is_import: false` canonical ISRU recipe.

# Confidence and open questions

Confidence: high that grinding wheels are real and necessary; high that they are consumables/tooling rather than machines; medium that the current ISRU recipe can produce precision-quality wheels without added grain/bond/porosity/safety detail.

Open questions:

- Does the simulator model wheel wear and replacement, or only availability of a wheel set?
- Are any processes demanding high-performance cBN/diamond wheels rather than alumina wheels?
- Should `grinding_wheel_aluminum_oxide` replace or become a variant of generic `grinding_wheels`?
