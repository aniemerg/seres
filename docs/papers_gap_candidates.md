# Paper-Derived Gap Candidates (Initial Pass)

Draft list of processes/machines/materials that self-replicating systems may need (not yet verified against KB). Each paper gets a quick sweep; items marked with "??" need validation before queuing work.

## Ellery – Self-Replicating Machines (Feasible) (skimmed full paper)
- 3D-printable actuator/motor path: printable motor components, winding, commutation; electron-beam freeform fabrication (EBF3) as metal additive; metal powdering step for printers.
- Thermal lance / simple ceramic casting route (3D-printed molds + lance) for high-temp ceramics.
- Cartesian/gantry assembler with multi-DOF wrist for self-assembly; universal fixture/jigging process.
- Teleoperation/telesupervision station (imported compute + haptics) to reduce on-site hardware sophistication.
- RepRap-style self-replication: printed threaded rods, fasteners (cement/adhesive substitute), printed sensors/encoders — recipes missing.

## Ellery – Neural Electronics on the Moon (2022) (skimmed full paper)
- Vacuum tube chain gaps: glass-to-metal sealing process; oxide-coated tungsten cathode coating station; getter deposition/activation; kovar/ceramic insulated wiring; tube vacuum sealing.
- Magnetic core memory: ferrite toroid fabrication/sintering; core threading assembly machine (4-axis gantry) and wiring process.
- Neural analog circuits: analog test benches (oscillator/amplifier) and tube socket/pin header parts/recipes.
- Recurrent/analog neural hardware: standard module as an item (neural tile) + test recipe.

## I-SAIRAS 2020 – Sustainable Lunar Exploration (skimmed)
- Metalysis FFC core: NaCl/HCl pre-processing for pure oxides; CaCl2 electrolyte recycle; FFC reactor unit + control; acid leach/prep process.
- Unit chemical processor family: generic reactor vessel (cylindrical/rounded) with pump/valve control; catalyst regeneration/packed-bed regen process.
- Material composition management controls: sensors (temp/pressure/flow) + control recipe for unit ops.

## NASA TM 20210009988 – Bootstrapping Space Industry (skim abstract/structure)
- (Optional/import) Teleop/VR workstation (imported compute + haptics) for supervision; not core to replication.
- (Nice-to-have) Standard pallet/bin/container system; simple sheet-metal bin/box recipes if logistics need it.
- Modular fixture system for transport/handling (pallet forks, quick latches) — defer unless logistics becomes a bottleneck.

## NASA ICES 2024 – ISRU Modeling (skim abstract)
- Water processing chain: auger dryer (LADI-style) as machine/process; cold trap module and radiator sizing; LOX/LH2 storage tanks.
- End-to-end integration: synchronized excavation → dryer → cold trap → electrolysis; may need a “water ISRU train” recipe.

## NASA ISRU Progress (2012) (skim abstract)
- Hydrogen reduction loop with gas recycle: H2/O2 separation/recirculation module; high-temp valve/seal/gasket materials/process.
- Reactor corrosion mitigation: corrosion-resistant liners/coatings for reduction reactors.

## NIAC Chirikjian – Self-Replicating Lunar Factories (skim abstract)
- Modular truss/beam kits and node connectors; lattice-builder gantry (coarse cartesian).
- Bulk regolith bricks/blocks via sintering: brick press/sinter path.
- (Later) Self-docking/power-sharing couplers for robots — useful for swarms, not core to first replication.

## NSS Bootstrapping Lunar Industry (2016) (skim abstract)
- (Optional) Solar array cleaning: brushes/blowers, electrostatic dust removal.
- Dust-mitigation coatings for optics/arrays; anti-static surface treatment process (defer unless arrays/optics become bottlenecks).

## MIT ISRU Architecture (2008) (skim)
- Emphasis on plant architectures; suggests scalable plant modules; night-survival thermal storage (regolith/PCM blocks) is nice-to-have, not core.

## Heat Pipe Solar Receiver (2009) (read abstract)
- Sodium (or NaK) heat-pipe solar receiver for 1000–1100°C hydrogen reduction: heat pipe receiver item/process; Na/K handling/fill/seal; Haynes 230 envelope or equivalent. (Optional if existing concentrator + furnace path suffices early.)
- Variable conductance/pressure-controlled heat pipes for passive power distribution to multiple reactors (later).
- Reactor/receiver integration fixtures.

## JHU Self-Replicating Robots (2002) (skim)
- Modular self-rep kit: docking/power-sharing couplers; modular limbs/tool-plates for repair/upgrade.

## RepRap Robotica (2011) (skim)
- Wire/arc metal additive process and machine; metal feedstock wire production.
- Printed linear guides/bearings/endstops; printer self-rep variants (control enclosure, mounts).

## Lunar ISRU Lomax (2019) (FFC oxygen) (skim figures)
- Metalysis FFC reactor specifics: CaCl2 electrolyte cell, inert anode, ~900–950°C operation; HCl pre-processing of regolith; oxygen off-gas handling; byproduct metal powder handling.

## NASA Polar Illumination (2008) (skim)
- Tall mast/array deployment; guy wires/cable stays; polar positioning hardware (defer unless polar ops needed).
- Power beaming/reflector concepts (treat as import/boundary for now).

## NASA ISRU Modeling Optimization (UCF) (skim)
- Parameterized recipes/process variants for reduction/electrolysis; tunable energy/time settings for optimization studies (later).

---
Next steps: validate each bullet against current KB, then enqueue specific gaps (missing items/processes) into the work queue. Items with "??" need confirmation from text before queuing.
