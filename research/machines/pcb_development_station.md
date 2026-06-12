# PCB development station

## Machine identity

- KB ID: `pcb_development_station`
- KB file: `kb/items/machines/pcb_development_station.yaml`
- KB name: PCB development station
- KB mass: 200 kg per unit
- Current KB role: photoresist development/wet-process station used as a submodule of simple PCB photolithography.

## KB usage and needed function

Local usage shows this item is a specific wet-process station, not the whole PCB fabrication line:

- It is listed in the imported/minimal machine set.
- It is required by `photolithography_process_simple_v0` together with `pcb_fab_equipment` and `uv_exposure_unit`.
- It is a component of `pcb_fab_equipment`.
- Its BOM includes a structural frame, small circulation/spray pump, bath reservoir, plumbing, controls/timers, power supply, and sensors.
- Its recipe notes say "Photoresist development station for PCB fabrication."

The needed function is developing exposed photoresist and supporting wet handling/rinsing around PCB photolithography. Etching, drilling, tinning/plating, and full board fabrication are broader functions covered by `pcb_fab_equipment` and related component items.

## Reality classification

Classification: real practical process station / submodule.

PCB development stations are realistic as part of a small PCB lab. The KB item is not a single universal PCB machine; it is a bath/spray/handling subsystem for photoresist development. The current 200 kg mass is plausible for a rugged enclosed wet station with reservoir, pump, plumbing, controls, and containment, but heavy for a hobby tray-based setup.

## Evidence links

The closely related local report `research/machines/pcb_fab_equipment.md` already collected relevant sources:

- Bungard Elektronik lists PCB lab machines including spray etching/developing machines and laboratory etching systems: https://www.bungard.de/en/machines
- LPKF sells benchtop PCB prototyping systems and circuit board plotters for PCB milling/drilling workflows: https://www.lpkfusa.com/pcb
- PCBWay's manufacturing overview shows PCB flows with imaging, etching, drilling, plating, soldermask, surface finish, and electrical test: https://www.pcbway.com/pcb-service.html
- DIY lab-scale PCB processes use exposure masks, UV exposure, development, etching, and drilling/cutting: https://justaddelectrons.com/blogi/diy-home-pcb-exposure-and-etching-process/
- Instructables documents a small DIY PCB lab using simple exposure/development/etching equipment: https://www.instructables.com/DIY-PCB-lab-for-under-3500/

These sources support the reality of a PCB development station as one part of a PCB prototyping/fabrication capability.

## Commercial alternatives

Commercial alternatives include:

- Spray developer/etcher units from PCB lab equipment vendors.
- Manual tray/tank development station with timer, rinse, and chemical storage.
- Combined develop/etch/rinse wet benches.
- Full PCB prototyping lab bundles that include UV exposure, developer, etcher, drill/router, and finishing equipment.

For the KB, `pcb_development_station` is best treated as a component of `pcb_fab_equipment`, not as an independent board factory.

## Build or open-source references

Low-end build paths are straightforward but chemically messy:

- Manual tray development with developer solution, rinse water, PPE, and timer.
- Spray/bath system with plastic reservoir, corrosion-compatible pump, plumbing, spray bars, heater if needed, controls, and secondary containment.
- DIY PCB lab references show that simple PCB development can be done with trays/tanks, UV exposure, developer, etchant, and a drill.

The difficult parts are process control, chemical compatibility, waste handling, fume/ventilation, and repeatability, not basic mechanical construction.

## Related machine research

Related local report:

- `research/machines/pcb_fab_equipment.md`

Related KB items:

- `pcb_fab_equipment`
- `pcb_fab_station`
- `uv_exposure_unit`
- `pcb_etching_tank_set`
- `pcb_drilling_station`
- `pcb_tinning_plating_bath`
- `chemical_bath_station`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep as a real PCB wet-process station, but clarify scope.

Recommended cleanup when KB edits are allowed:

- Rename or annotate as "PCB photoresist development station" or "PCB develop/rinse station."
- Keep it as a component/subsystem of `pcb_fab_equipment` unless separate capacity modeling is needed.
- Do not use it to represent the entire PCB fabrication process.
- Consider reducing or justifying the 200 kg mass. It is plausible for an enclosed wet bench but too heavy for a minimal tray-based station.
- Ensure consumables and hazards are modeled elsewhere: developer, etchant, rinse water, waste treatment, PPE/ventilation.

## Confidence and open questions

Confidence: high that the station is real as a PCB lab subsystem; medium on current mass and whether a separate ID is necessary.

Open questions:

- Does the KB need a separate development station if `pcb_fab_equipment` already bundles it?
- Is the intended station manual tray-based, spray-based, or an enclosed wet bench?
- How are developer chemistry, rinse water, and waste handling represented?
