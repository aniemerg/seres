# Machine identity

- Queue item: `machine_reality_labor_bot_general_v0`
- KB item: `labor_bot_general_v0`
- KB name: General labor bot (automation)
- KB file: `kb/items/machines/labor_bot_general_v0.yaml`
- Current KB kind: `machine`
- Current mass: 120 kg
- Current BOM: `bom_labor_bot_general_v0`
- Current recipe: `recipe_machine_labor_bot_general_v0`
- Current role: primary explicit labor resource for assembly, machine loading, material handling, quality control, and general manipulation.

# KB usage and needed function

`labor_bot_general_v0` is a core SERES modeling primitive. The project documentation intentionally models labor as machine-hours from replicable robots rather than abstract human labor hours. `docs/simviewer_articles/parts_and_labor.md` defines this item as the default labor resource: a general-purpose 6-DOF manipulator with about 120 kg mass, 2 m reach, 20 kg payload, and +/-0.5 mm repeatability. Conservative Mode also instructs queue work to prefer labor bot plus tools over adding special-purpose machines unless payload, precision, environment, or throughput differs materially.

The KB item describes a 6R serial manipulator operating inside a pressurized habitat, not an EVA robot. Its BOM is detailed: base/frame, aluminum arm links, wrist, motor housings, BLDC motors, harmonic drives, power supply, controllers, servo drives, safety PLC, cameras, force/torque sensor, proximity/touch sensors, gripper, quick-change tool interface, cable harnesses, cable chains, thermal management, safety light curtain, and protective covers.

The needed function is credible: a general robot arm that can hold tools, load machines, move parts, assemble components, inspect, and act as the reusable labor bottleneck in simulation.

# Reality classification

Real practical machine class, but the KB item is also a deliberate modeling abstraction for generalized labor capacity.

Six-axis industrial robot arms and collaborative robot arms are real and commercially mature. The KB specifications are broadly plausible, especially for indoor machine tending, material handling, simple assembly, and inspection. The main realism caveats are:

- A 20 kg payload at around 2 m reach usually implies either a heavier industrial arm or a shorter-reach/lightweight collaborative arm.
- +/-0.5 mm repeatability is conservative compared with many industrial arms, but the task envelope "general labor" is broader than normal taught robot programs.
- True general-purpose autonomous assembly requires tooling, fixtures, perception, programming, force control, safety systems, calibration, and task-specific process knowledge; a robot arm alone is not a human-equivalent worker.
- Local manufacture of harmonic drives, servo drives, precision encoders, force/torque sensors, safety electronics, cameras, compute, and NdFeB motors is much harder than local fabrication of links and frames.

# Evidence links

- KUKA lists industrial robot families with different kinematics, payloads, reaches, and variants; examples include 6-axis arms from small payloads to hundreds of kilograms: https://www.kuka.com/en-us/products/robotics-systems/industrial-robots
- ABB describes a comprehensive 6-axis articulated robot portfolio for material handling, machine tending, spot welding, arc welding, and related industrial applications: https://www.abb.com/global/en/areas/robotics/products/robots
- Universal Robots UR20 is a 6-DOF collaborative robot with 20 kg payload, 1750 mm reach, and listed power consumption of hundreds of watts depending on program/settings: https://www.universal-robots.com/products/ur20/ and https://www.universal-robots.com/manuals/EN/HTML/SW10_6/Content/prod-usr-man/hardware/arm_UR20/appendix/technical_specifications_datasheet_UR20.htm
- FANUC CRX-20iA/L is a collaborative robot with 20 kg payload and 1418 mm reach, supporting compact industrial workspaces: https://www.fanucamerica.com/products/robots/series/collaborative-robot
- FANUC M-20iB/25 is a compact 6-axis industrial robot with 25 kg payload, 1853 mm reach, and 210 kg mechanical weight: https://www.fanucamerica.com/products/robots/series/m-20/m-20ib-25
- FANUC Europe describes the M-20 series as 6-axis medium payload robots with up to 2 m reach and up to 35 kg handling capacity: https://www.fanuc.eu/eu-en/m-20-series
- Robots Done Right summarizes key robot specification concepts such as axes, payload, reach, and repeatability, which match the KB's specification style: https://robotsdoneright.com/Articles/robot-specifications.html

# Commercial alternatives

Commercial alternatives include:

- Collaborative arm in the UR20/FANUC CRX-20 class: closer to safe human-adjacent manipulation, lower integration burden, but shorter reach/lower speed and still not general autonomy.
- Industrial 6-axis arm in the FANUC M-20/KUKA/ABB class: closer payload/reach, higher speed and stiffness, but typically heavier and requires guarded work cells.
- SCARA robot: good for light planar assembly and pick/place, not a general 6-DOF labor replacement.
- Cartesian gantry: good for large-volume repetitive handling, not flexible general manipulation.
- Mobile manipulator or humanoid robot: broader mobility, but much higher complexity and lower maturity for industrial self-reproduction modeling.
- Labor bot plus specific tools/fixtures: best modeling pattern for most low-throughput processes.

# Build or open-source references

Open-source and research robot arms exist, but they are not equivalent to an industrial 20 kg payload, 2 m reach manipulator. Local build realism should follow the KB's current split:

- locally feasible earlier: steel/aluminum frame, arm links, housings, covers, cable routing, some harnesses, brackets, thermal hardware;
- difficult but eventually plausible with advanced KB chains: motors, precision bearings, machined gear components, grippers, structural calibration fixtures;
- likely imported for a long time: harmonic drives or equivalent zero-backlash reducers, high-resolution encoders, servo drives, safety PLCs, cameras, force/torque sensors, industrial compute, reliable software stack, rare-earth magnets.

The current 140 hour assembly time is plausible as integration/assembly time when all subassemblies are already available, but it does not represent the full difficulty of manufacturing and validating precision robot components.

# Related machine research

Related local reports:

- `control_compute_module_imported.md`
- `hand_tools_basic.md`
- `inspection_tools_basic.md`
- `lifting_equipment.md`
- `wire_crimping_tools.md`
- `refractory_installation_tools.md`
- `soldering_station.md`

Related docs:

- `docs/labor_bot_design_memo.md`
- `docs/labor_bot_parts_mapping.md`
- `docs/labor_bot_recipe_analysis.md`
- `docs/simviewer_articles/parts_and_labor.md`

# Recommendation for KB realism

Keep `labor_bot_general_v0`; it is a real machine class and a necessary SERES modeling primitive.

Recommended realism notes:

- Keep the indoor/pressurized-habitat assumption explicit. Do not use this item for EVA, abrasive regolith fieldwork, high-temperature proximity, vacuum, or dusty excavation without a specialized robot.
- Keep payload and precision limits visible: around 20 kg payload and +/-0.5 mm repeatability. Use lifting equipment for heavier objects and precision machines/metrology for tighter tolerances.
- Treat it as a robot arm plus end effector and work-cell safety/integration, not as a human-equivalent autonomous worker.
- Consider increasing mass or clarifying "lunar gravity effective payload" if the 20 kg at 2 m reach is meant to be Earth-equivalent payload. Commercial examples suggest a 20-25 kg, ~1.8-2.0 m industrial arm is often heavier than 120 kg.
- Preserve imported status or imported subcomponents for compute, sensing, servo electronics, encoders, and rare-earth magnets unless the KB has explicit production chains.
- Continue the Conservative Mode pattern: prefer `labor_bot_general_v0` plus tools for low-throughput manipulation, but do not use it to replace active process machines such as mills, grinders, furnaces, pumps, presses, power converters, or continuous feedback systems.

# Confidence and open questions

Confidence: high that the machine class is real; high that it is appropriate as an explicit labor resource; medium on the exact mass/payload/reach combination; medium on autonomy assumptions because real industrial robots normally need task-specific programming, fixtures, guarding, and integration.

Open questions:

- Is the 20 kg payload intended as Earth-equivalent payload, lunar effective payload, or payload at the flange including end effector?
- Does the simulator model work-cell setup time, tool changing, fixture setup, and programming/calibration, or only productive labor hours?
- Should the KB add a lighter/cheaper collaborative arm variant and a heavier guarded industrial arm variant, or is the current general bot intentionally the conservative middle?
